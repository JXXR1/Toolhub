#!/usr/bin/env python3
"""
Toolhub generator — renders unified tool pages from manifest.

Inputs:
  build/template.html   — page template with {{PLACEHOLDER}} tokens
  build/i18n.py         — shared UI string translations
  build/tools/*.py      — one module per tool, exporting TOOL dict

Outputs:
  /<slug>/index.html              (English)
  /<lang>/<slug>/index.html       (each translation)

Run:
  cd /root/projects/toolhub-deploy && python3 build/build.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
TEMPLATE = (BUILD / "template.html").read_text()
PAGE_TEMPLATE = (BUILD / "page_template.html").read_text()

ADSENSE_CLIENT_RE = re.compile(r"^ca-pub-\d{16}$")


def assert_deploy_config_coherent():
    """Refuse to ship a production build with broken AdSense config.

    Parses the TOOLHUB_CONFIG object literal out of template.html and, when
    deploy_env=="production", asserts:
      - adsenseClientId matches /^ca-pub-\\d{16}$/
      - at least one of adSlotIds.content/footer/indexTop/indexBottom is set

    sandbox mode is always allowed regardless of AdSense fields.
    """
    m = re.search(
        r"window\.TOOLHUB_CONFIG\s*=\s*\{([\s\S]*?)\};",
        TEMPLATE,
    )
    if not m:
        print("ERROR: could not find window.TOOLHUB_CONFIG in template.html")
        sys.exit(1)
    body = m.group(1)

    def field(name):
        mm = re.search(name + r"\s*:\s*\"([^\"]*)\"", body)
        return mm.group(1) if mm else ""

    deploy_env = field("deploy_env") or "sandbox"
    if deploy_env not in ("sandbox", "production"):
        print(f'ERROR: TOOLHUB_CONFIG.deploy_env="{deploy_env}" — expected "sandbox" or "production"')
        sys.exit(1)
    if deploy_env == "sandbox":
        print(f'  ✓ deploy_env="sandbox" — AdSense gated off, ad slots will render as placeholders')
        return

    client = field("adsenseClientId")
    # Pull adSlotIds sub-object
    sm = re.search(r"adSlotIds\s*:\s*\{([^}]*)\}", body)
    slots_blob = sm.group(1) if sm else ""
    slots = dict(re.findall(r"(\w+)\s*:\s*\"([^\"]*)\"", slots_blob))
    any_slot = any(slots.get(k) for k in ("content", "footer", "indexTop", "indexBottom"))

    if not ADSENSE_CLIENT_RE.match(client) or not any_slot:
        print('ERROR: deploy_env="production" but AdSense config is incomplete or invalid')
        if not ADSENSE_CLIENT_RE.match(client):
            print(f'  - adsenseClientId="{client}" does not match ca-pub-NNNNNNNNNNNNNNNN (16 digits)')
        if not any_slot:
            print('  - adSlotIds.{content,footer,indexTop,indexBottom} are all empty')
        sys.exit(1)
    print(f'  ✓ deploy_env="production" — AdSense config validated ({client})')

# Load i18n
spec = importlib.util.spec_from_file_location("i18n", BUILD / "i18n.py")
i18n_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(i18n_mod)
UI = i18n_mod.UI
LANGS = i18n_mod.LANGS  # ["en", "de", "es", "fr", "it", "pt", "pl", "ja", "nl"]

# Load static content pages (about, contact, for-schools)
spec = importlib.util.spec_from_file_location("pages", BUILD / "pages.py")
pages_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages_mod)
PAGES = pages_mod.PAGES

# Load all tool modules
TOOLS = []
for tool_file in sorted((BUILD / "tools").glob("*.py")):
    if tool_file.name.startswith("_"):
        continue
    spec = importlib.util.spec_from_file_location(tool_file.stem, tool_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "TOOL"):
        print(f"  ! {tool_file.name} has no TOOL export, skipping")
        continue
    TOOLS.append(mod.TOOL)


def lang_path(lang: str, slug: str) -> str:
    """URL path for a tool in a given language."""
    if lang == "en":
        return f"/{slug}/"
    return f"/{lang}/{slug}/"


def home_path(lang: str) -> str:
    return "/" if lang == "en" else f"/{lang}/"


def privacy_path(lang: str) -> str:
    return "/privacy/" if lang == "en" else f"/{lang}/privacy/"


def page_path(lang: str, slug: str) -> str:
    """URL path for a static content page in a given language."""
    if lang == "en":
        return f"/{slug}/"
    return f"/{lang}/{slug}/"


def output_path(lang: str, slug: str) -> Path:
    if lang == "en":
        return ROOT / slug / "index.html"
    return ROOT / lang / slug / "index.html"


def fill_placeholders(text: str, mapping: dict) -> str:
    """Replace all {{KEY}} placeholders. Multiple passes to handle nested."""
    for _ in range(3):
        for k, v in mapping.items():
            text = text.replace("{{" + k + "}}", str(v))
    return text


def fill_braces(text: str, mapping: dict) -> str:
    """Replace {KEY} placeholders (used inside body/script for label substitution)."""
    for k, v in mapping.items():
        text = text.replace("{" + k + "}", str(v))
    return text


OG_LOCALES = {"en": "en_GB", "de": "de_DE", "es": "es_ES", "fr": "fr_FR", "it": "it_IT", "pt": "pt_BR", "pl": "pl_PL", "ja": "ja_JP", "nl": "nl_NL"}

CATEGORY_TO_APP_CAT = {
    # schema.org/SoftwareApplication applicationCategory enum-ish values
    "developer":  "DeveloperApplication",
    "encoding":   "DeveloperApplication",
    "data":       "DeveloperApplication",
    "validation": "DeveloperApplication",
    "datetime":   "UtilityApplication",
    "math":       "UtilityApplication",
    "text":       "UtilityApplication",
    "design":     "DesignApplication",
    "security":   "SecurityApplication",
    "media":      "MultimediaApplication",
}

SUBCATEGORY_LABELS = {
    "developer":  "Developer Tools",
    "text":       "Text Tools",
    "encoding":   "Encoding & Decoding",
    "data":       "Data Tools",
    "security":   "Security Tools",
    "media":      "Media Tools",
    "validation": "Validation Tools",
    "design":     "Design Tools",
    "datetime":   "Date & Time Tools",
    "math":       "Math Tools",
}


def alternate_links(slug: str) -> str:
    """rel=alternate hreflang block — every lang + x-default pointing at EN."""
    lines = []
    for L in LANGS:
        href = f"https://toolhub.software{lang_path(L, slug)}"
        lines.append(f'<link rel="alternate" hreflang="{L}" href="{href}">')
    # x-default → English
    lines.append(f'<link rel="alternate" hreflang="x-default" href="https://toolhub.software{lang_path("en", slug)}">')
    return "\n  ".join(lines)


def render_tool(tool: dict, lang: str) -> str:
    slug = tool["slug"]
    ui = UI[lang]
    t_i18n = tool["i18n"][lang]

    # Body and script labels — common placeholders the body/script can use
    label_map = {
        "LBL_INPUT": ui["input"],
        "LBL_OUTPUT": ui["output"],
        "LBL_RESULT": ui["result"],
        "LBL_FORMAT": ui["format"],
        "LBL_GENERATE": ui["generate"],
        "LBL_CONVERT": ui["convert"],
        "LBL_COMPARE": ui["compare"],
        "LBL_VALIDATE": ui["validate"],
        "LBL_ENCODE": ui["encode"],
        "LBL_DECODE": ui["decode"],
        "LBL_MINIFY": ui["minify"],
        "LBL_BEAUTIFY": ui["beautify"],
        "LBL_COPY": ui["copy"],
        "LBL_CLEAR": ui["clear"],
        "LBL_DOWNLOAD": ui["download"],
        "LBL_RESET": ui["reset"],
        "LBL_SWAP": ui["swap"],
        "LBL_NOW": ui["now"],
        "LBL_REMOVE": ui["remove"],
        "LBL_ADD": ui["add"],
        "LBL_ALL": ui["all"],
        "LBL_ROLL": ui["roll"],
        "LBL_OPTIONS": ui["options"],
        "LBL_LENGTH": ui["length"],
        "LBL_COUNT": ui["count"],
        "LBL_TYPE": ui["type"],
        "LBL_FROM": ui["from"],
        "LBL_TO": ui["to"],
        "LBL_NO_INPUT": ui["no_input"],
        "LBL_INVALID": ui["invalid_input"],
        "LBL_INSTALL_APP": ui["install_app"],
    }
    body = fill_braces(tool["body"], label_map)
    script = fill_braces(tool.get("script", ""), label_map)

    # Help block
    help_text = tool.get("help", {}).get(lang) or tool.get("help", {}).get("en", "")
    if help_text:
        # Wrap with .help div if not already
        help_block = f'<div class="help">{help_text}</div>'
    else:
        help_block = ""

    # Related tools
    related = tool.get("related", [])
    if related:
        # Build "Related Tools" block
        rels = []
        for rel_slug in related:
            rel = next((t for t in TOOLS if t["slug"] == rel_slug), None)
            if rel:
                rel_name = rel["i18n"][lang]["name"]
                rels.append(f'<a href="{lang_path(lang, rel_slug)}">{rel_name}</a>')
        if rels:
            related_html = (
                f'<div class="related"><span class="meta">{ui["related_tools"]}:</span> '
                + " ".join(rels)
                + "</div>"
            )
            help_block = (
                help_block.replace("</div>", related_html + "</div>")
                if help_block
                else f'<div class="help">{related_html}</div>'
            )

    sel = {l: ('selected="selected"' if l == lang else "") for l in LANGS}

    cat = tool.get("category", "developer")
    feature_list_json = json.dumps(tool.get("tags", []), ensure_ascii=False)

    placeholders = {
        "LANG": lang if lang != "en" else "en",
        "TITLE": t_i18n["name"],
        "TAGLINE": t_i18n["tagline"],
        "DESCRIPTION": t_i18n["description"],
        "PATH": lang_path(lang, slug),
        "HOME": home_path(lang),
        "PRIVACY": privacy_path(lang),
        "PRIVACY_LBL": ui["privacy"],
        "ABOUT": page_path(lang, "about"),
        "ABOUT_LBL": ui["about"],
        "CONTACT": page_path(lang, "contact"),
        "CONTACT_LBL": ui["contact"],
        "FOR_SCHOOLS": page_path(lang, "for-schools"),
        "FOR_SCHOOLS_LBL": ui["for_schools"],
        "DATA_HANDLING": page_path(lang, "how-we-handle-your-data"),
        "DATA_HANDLING_LBL": ui["data_handling"],
        "AFFILIATE_DISCLOSURE": page_path(lang, "affiliate-disclosure"),
        "AFFILIATE_DISCLOSURE_LBL": ui["affiliate_disclosure"],
        "ALL_TOOLS": ui["all_tools"],
        "THEME_TIP": ui["theme_tip"],
        "INSTALL_APP": ui["install_app"],
        "SLUG": slug,
        "TOOL_BODY": body,
        "TOOL_SCRIPT": script,
        "HELP_BLOCK": help_block,
        "SEL_EN": sel["en"],
        "SEL_DE": sel["de"],
        "SEL_ES": sel["es"],
        "SEL_FR": sel["fr"],
        "SEL_IT": sel["it"],
        "SEL_PT": sel["pt"],
        "SEL_PL": sel["pl"],
        "SEL_JA": sel["ja"],
        "SEL_NL": sel["nl"],
        "ALTERNATE_LINKS": alternate_links(slug),
        "OG_LOCALE": OG_LOCALES.get(lang, "en_GB"),
        "INLANG": lang,
        "APP_CATEGORY": CATEGORY_TO_APP_CAT.get(cat, "UtilityApplication"),
        "APP_SUBCATEGORY": SUBCATEGORY_LABELS.get(cat, cat.title()),
        "FEATURE_LIST": feature_list_json,
        "OG_IMAGE_URL": f"https://toolhub.software/og-images/{slug}.png",
    }

    return fill_placeholders(TEMPLATE, placeholders)


def assert_translations_complete():
    """Verify every tool has all LANGS in i18n, and every UI key has all LANGS.

    Hard-fail on i18n / UI gaps (visible name/tagline/button strings).
    Warn-only on help gaps (long-form help falls back to English at render time).
    """
    problems = []
    # UI dict completeness — every key must appear in every lang
    en_keys = set(UI["en"].keys())
    for lang in LANGS:
        if lang not in UI:
            problems.append(f"UI dict missing entire lang: {lang}")
            continue
        missing = en_keys - set(UI[lang].keys())
        extra = set(UI[lang].keys()) - en_keys
        for k in sorted(missing):
            problems.append(f"UI[{lang}] missing key: {k}")
        for k in sorted(extra):
            problems.append(f"UI[{lang}] has extra key not in UI[en]: {k}")
    # Per-tool i18n completeness (name / tagline / description — directly user-visible)
    help_warnings = []
    for tool in TOOLS:
        slug = tool["slug"]
        i18n_langs = set(tool.get("i18n", {}).keys())
        help_langs = set(tool.get("help", {}).keys())
        for lang in LANGS:
            if lang not in i18n_langs:
                problems.append(f"{slug}: i18n missing lang: {lang}")
            if lang not in help_langs:
                help_warnings.append(f"{slug}:{lang}")
    # Static pages — name/h1/body must exist for every lang
    for slug, page in PAGES.items():
        page_langs = set(page.get("i18n", {}).keys())
        for lang in LANGS:
            if lang not in page_langs:
                problems.append(f"page {slug}: i18n missing lang: {lang}")
                continue
            entry = page["i18n"][lang]
            for key in ("title", "h1", "description", "body"):
                if not entry.get(key):
                    problems.append(f"page {slug}:{lang} missing {key}")
    if problems:
        print("  ✗ Translation completeness check FAILED:")
        for p in problems:
            print(f"    - {p}")
        sys.exit(1)
    if help_warnings:
        print(f"  ⚠ {len(help_warnings)} help-translation gaps (English fallback used; non-fatal)")
    print(f"  ✓ i18n + UI completeness OK ({len(TOOLS)} tools × {len(LANGS)} langs, {len(en_keys)} UI keys, {len(PAGES)} static pages)")


def write_tool_pages():
    written = 0
    for tool in TOOLS:
        for lang in LANGS:
            out = output_path(lang, tool["slug"])
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render_tool(tool, lang))
            written += 1
    print(f"  ✓ Rendered {written} pages ({len(TOOLS)} tools × {len(LANGS)} languages)")


def render_page(page: dict, lang: str) -> str:
    slug = page["slug"]
    ui = UI[lang]
    p_i18n = page["i18n"][lang]
    sel = {l: ('selected="selected"' if l == lang else "") for l in LANGS}
    placeholders = {
        "LANG": lang,
        "TITLE": p_i18n["title"],
        "H1": p_i18n["h1"],
        "DESCRIPTION": p_i18n["description"],
        "BODY": p_i18n["body"],
        "PATH": page_path(lang, slug),
        "HOME": home_path(lang),
        "PRIVACY": privacy_path(lang),
        "PRIVACY_LBL": ui["privacy"],
        "ABOUT": page_path(lang, "about"),
        "ABOUT_LBL": ui["about"],
        "CONTACT": page_path(lang, "contact"),
        "CONTACT_LBL": ui["contact"],
        "FOR_SCHOOLS": page_path(lang, "for-schools"),
        "FOR_SCHOOLS_LBL": ui["for_schools"],
        "DATA_HANDLING": page_path(lang, "how-we-handle-your-data"),
        "DATA_HANDLING_LBL": ui["data_handling"],
        "AFFILIATE_DISCLOSURE": page_path(lang, "affiliate-disclosure"),
        "AFFILIATE_DISCLOSURE_LBL": ui["affiliate_disclosure"],
        "ALL_TOOLS": ui["all_tools"],
        "THEME_TIP": ui["theme_tip"],
        "SLUG": slug,
        "SEL_EN": sel["en"],
        "SEL_DE": sel["de"],
        "SEL_ES": sel["es"],
        "SEL_FR": sel["fr"],
        "SEL_IT": sel["it"],
        "SEL_PT": sel["pt"],
        "SEL_PL": sel["pl"],
        "SEL_JA": sel["ja"],
        "SEL_NL": sel["nl"],
        "ALTERNATE_LINKS": alternate_links(slug),
        "OG_LOCALE": OG_LOCALES.get(lang, "en_GB"),
        "INLANG": lang,
        "SCHEMA_TYPE": page.get("schema", "WebPage"),
        "OG_IMAGE_URL": "https://toolhub.software/og-image.png",
    }
    return fill_placeholders(PAGE_TEMPLATE, placeholders)


def write_static_pages():
    written = 0
    for page in PAGES.values():
        for lang in LANGS:
            out = output_path(lang, page["slug"])
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render_page(page, lang))
            written += 1
    print(f"  ✓ Rendered {written} static-page files ({len(PAGES)} pages × {len(LANGS)} languages)")


def update_index_tools_arrays():
    """Update the TOOLS array in root + lang index.html files."""
    # Build the manifest each lang's index needs
    for lang in LANGS:
        index_path = ROOT / "index.html" if lang == "en" else ROOT / lang / "index.html"
        if not index_path.exists():
            print(f"  ! Skipping missing {index_path}")
            continue
        text = index_path.read_text()

        # Generate a fresh JS array for this lang
        lines = []
        for t in TOOLS:
            i = t["i18n"][lang]
            entry = {
                "slug": t["slug"],
                "name": i["name"],
                "desc": i["tagline"],
                "icon": t["icon"],
                "cat": t["category"],
                "tags": t["tags"],
            }
            lines.append("      " + json.dumps(entry, ensure_ascii=False))
        new_array = "    const TOOLS = [\n" + ",\n".join(lines) + "\n    ];"

        # Replace existing TOOLS array (matches  const TOOLS = [ ... ];  )
        new_text, n = re.subn(
            r"const TOOLS\s*=\s*\[[\s\S]*?\];",
            new_array,
            text,
            count=1,
        )
        if n == 0:
            print(f"  ! No TOOLS array found in {index_path}")
            continue
        index_path.write_text(new_text)
        print(f"  ✓ Updated TOOLS array in {index_path.relative_to(ROOT)}")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--update-index", action="store_true",
                   help="Regenerate the TOOLS array in index.html files (only safe when ALL tools are in the manifest)")
    p.add_argument("--only", help="Render only this slug (comma-separated for multiple)")
    args = p.parse_args()
    if args.only:
        wanted = set(args.only.split(","))
        TOOLS[:] = [t for t in TOOLS if t["slug"] in wanted]
    print(f"Toolhub generator — {len(TOOLS)} tools × {len(LANGS)} languages ({len(PAGES)} static pages)")
    assert_deploy_config_coherent()
    assert_translations_complete()
    write_tool_pages()
    write_static_pages()
    if args.update_index:
        update_index_tools_arrays()
    else:
        print("  (skipping index TOOLS array regeneration; pass --update-index when all tools migrated)")
    print("Done.")
