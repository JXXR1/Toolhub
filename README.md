# Toolhub

> 60 free developer tools. 9 languages. No signup. No tracking. Open source.

**Live at:** [toolhub.software](https://toolhub.software)

---

## What is this

A static site of 60 self-contained developer utilities — JSON formatter, regex tester, JWT decoder, CIDR calculator, password generator, base64 encoder, hash generator, cron builder, and ~52 more. Everything runs entirely in your browser. Nothing is uploaded.

Built as the alternative to the typical "free X tool" sites that are ad-laden, popup-ridden, and quietly route your inputs through third-party trackers.

## What's in it

- **60 tools** across developer / design / text / math / data / encoding / datetime / security / media / validation / utility categories
- **9 languages** (en, de, es, fr, it, pt-BR, pl, ja, nl) — proper translations, not auto-MT, with localized help blocks (3 sub-sections per tool)
- **Privacy-first** — no signup, no accounts, no third-party trackers, no remote tool execution
- **PWA** — works offline once cached, installable as an app
- **Schema-rich** — every tool ships with SoftwareApplication, WebApplication, BreadcrumbList, FAQPage, and (for procedural tools) HowTo structured data for SERP rich snippets
- **Accessible** — WCAG AA contrast, proper landmarks, ARIA-correct controls, keyboard navigable
- **Fast** — pages are 17-29 KB. Lighthouse: home perf 99, a11y 93, BP 100, SEO 100

## How it works

```
build/
├── template.html         # single tool-page template with {{PLACEHOLDER}} tokens
├── i18n.py               # UI string translations (9 langs)
├── pages.py              # non-tool static pages (about, contact, privacy, etc.)
├── tools/                # one Python manifest per tool — TOOL dict export
│   ├── json_formatter.py
│   ├── cidr_calculator.py
│   └── …
└── build.py              # loads manifests, renders per-tool + per-lang HTML

bin/
├── addtool               # scaffold a new tool (slug, category, optional --from)
├── removetool            # cleanly remove a tool + its rendered pages + cross-references
└── gen-og-images         # generate per-tool og-images (PIL)
```

Render the site:
```bash
python3 build/build.py                  # render all tools × all langs
python3 build/build.py --update-index   # regenerate the home-page tool index
python3 build/build.py --only <slug>    # render a single tool
```

Add a new tool:
```bash
bin/addtool my-new-tool --cat developer --icon "🔧"
# (then edit build/tools/my_new_tool.py to fill in the manifest)
```

Generate per-tool og-images after content changes:
```bash
bin/gen-og-images           # regenerate all 60 + the base image
bin/gen-og-images --only <slug>
```

## Tool manifest schema

```python
TOOL = {
    "slug": "kebab-case",
    "category": "developer|design|encoding|datetime|math|text|media|validation|utility|data",
    "icon": "emoji or short symbol",
    "tags": [...],
    "i18n": {
        "en": {"name": ..., "tagline": ..., "description": ...},
        "de": {...}, "es": {...}, "fr": {...}, "it": {...},
        "pt": {...}, "pl": {...}, "ja": {...}, "nl": {...},
    },
    "body": "<HTML for the tool UI — use {LBL_*} placeholders>",
    "script": "<script>...</script>",
    "help": {
        "en": "<HTML — must include 'What is this for?', 'When to use it', 'Common gotchas' sections>",
        ...
    },
    "related": ["slug-1", "slug-2", ...],
    "howto_steps": {...},   # optional — per-lang HowTo schema steps
}
```

A build-time assertion fails if any tool or UI key is missing a language. That's how the catalogue stays consistent across 9 langs.

## Deploy

GitHub Pages from `main` branch. CNAME at root points at `toolhub.software`. DNS A records point at GitHub Pages IPs (185.199.108-111.153).

```
deploy_env in build/template.html TOOLHUB_CONFIG:
  "sandbox"     - ads off, "SANDBOX" badge visible (dev mode)
  "production"  - real AdSense slots, no badge
```

Build refuses production builds if `adsenseClientId` doesn't match `ca-pub-\d{16}` or all slot IDs are empty.

## Contributing

Spotted a bug, missing tool, or translation oddity?

- **Bugs / missing tools / suggestions:** [GitHub Issues](https://github.com/JXXR1/Toolhub/issues)
- **Translation contributions:** especially welcome for Turkish, Indonesian, Vietnamese, Hindi, Slovak, Czech (queued for addition). Please open an issue with what you'd like to contribute first.

No code-of-conduct boilerplate — just be civil.

## Why no AI-generated slop

Help blocks are human-written (within reason) and translated by careful human review, not raw LLM output. Tool implementations are hand-built. If you spot anything that smells like LLM-generated boilerplate, please flag it.

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgements

- Built solo as a side project
- Plausible for privacy-respecting analytics
- GitHub Pages for free static hosting
- The various open-source libraries credited in individual tool source

## Stats

- 60 tools
- 9 languages (en, de, es, fr, it, pt-BR, pl, ja, nl)
- 540 tool pages + 54 static pages = ~604 sitemap URLs
- Total site size: ~5 MB
- Per-page weight: 17-29 KB

---

If Toolhub saved you time, consider:
- ⭐ Starring the repo
- ☕ [Buy me a coffee](https://www.buymeacoffee.com/JXXR1) *(link active once configured)*
- 💖 [GitHub Sponsors](https://github.com/sponsors/JXXR1) *(link active once configured)*
- 🌊 If you spin up a DigitalOcean droplet via [this affiliate link](https://m.do.co/c/JXXR1) *(link active once configured)*, I get a small commission at no cost to you.
