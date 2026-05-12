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
LANGS = i18n_mod.LANGS  # ["en", "de", "es", "fr", "it", "pt", "pl", "ja", "nl", "tr", "id", "vi", "hi", "sk", "cs"]

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


OG_LOCALES = {"en": "en_GB", "de": "de_DE", "es": "es_ES", "fr": "fr_FR", "it": "it_IT", "pt": "pt_BR", "pl": "pl_PL", "ja": "ja_JP", "nl": "nl_NL", "tr": "tr_TR", "id": "id_ID", "vi": "vi_VN", "hi": "hi_IN", "sk": "sk_SK", "cs": "cs_CZ"}

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


# --- FAQPage extraction ---------------------------------------------------
# Pull (question, answer) pairs out of the help block. Each <h2>/<h3> heading
# becomes the question; everything between that heading and the next heading
# becomes the answer (HTML stripped, whitespace collapsed).
_HEADING_RE = re.compile(r"<(h[23])\b[^>]*>(.*?)</\1>", re.DOTALL | re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_ENTITY_REPLACEMENTS = (
    ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
    ("&quot;", '"'), ("&#39;", "'"), ("&nbsp;", " "),
)


def _strip_html(s: str) -> str:
    s = _TAG_RE.sub(" ", s)
    for a, b in _ENTITY_REPLACEMENTS:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def extract_faq_pairs(help_html: str):
    """Return [(question, answer_text), ...] from H2/H3 sections in help_html."""
    matches = list(_HEADING_RE.finditer(help_html))
    pairs = []
    for i, m in enumerate(matches):
        q = _strip_html(m.group(2))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(help_html)
        a = _strip_html(help_html[start:end])
        if q and a:
            pairs.append((q, a))
    return pairs


def render_faq_schema(tool: dict, lang: str) -> str:
    help_html = tool.get("help", {}).get(lang) or tool.get("help", {}).get("en", "")
    if not help_html:
        return ""
    pairs = extract_faq_pairs(help_html)
    if not pairs:
        return ""
    doc = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(doc, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


# --- HowTo schema ---------------------------------------------------------
# Tool manifests declare a compact `howto` field:
#   "howto": {"flow": "transform", "action": "format", "noun": "JSON"}
# where flow ∈ {transform, generate, calculate, compare} and action is a key
# in i18n.UI (format/encode/decode/convert/generate/validate/compare/...).
# noun is either a string (used across all languages — e.g. "JSON", "URL")
# or a {lang: str} dict for translation.
#
# Tools without a `howto` field emit no HowTo schema (pure-reference tools).

# 3-step (name_tpl, text_tpl) pairs per flow per language.
# Placeholders: {noun} {action} {input} {output} {copy}
HOWTO_TEMPLATES = {
    "transform": {
        "en": [("Paste your {noun}",          "Drop your {noun} into the {input} field."),
               ("Click {action}",             "Press the {action} button to run the tool."),
               ("Copy the result",            "Hit {copy} to copy the {output}.")],
        "de": [("{noun} einfügen",            "Füge dein {noun} in das {input}-Feld ein."),
               ("{action} klicken",           "Drücke {action}, um das Tool auszuführen."),
               ("Ergebnis kopieren",          "Drücke {copy}, um die {output} zu kopieren.")],
        "es": [("Pega tu {noun}",             "Coloca tu {noun} en el campo {input}."),
               ("Haz clic en {action}",       "Pulsa el botón {action} para ejecutar la herramienta."),
               ("Copia el resultado",         "Pulsa {copy} para copiar la {output}.")],
        "fr": [("Collez votre {noun}",        "Placez votre {noun} dans le champ {input}."),
               ("Cliquez sur {action}",       "Appuyez sur le bouton {action} pour exécuter l'outil."),
               ("Copiez le résultat",         "Appuyez sur {copy} pour copier la {output}.")],
        "it": [("Incolla il {noun}",          "Metti il {noun} nel campo {input}."),
               ("Clicca {action}",            "Premi il pulsante {action} per eseguire lo strumento."),
               ("Copia il risultato",         "Premi {copy} per copiare l'{output}.")],
        "pt": [("Cole seu {noun}",            "Coloque seu {noun} no campo {input}."),
               ("Clique em {action}",         "Pressione o botão {action} para rodar a ferramenta."),
               ("Copie o resultado",          "Pressione {copy} para copiar a {output}.")],
        "pl": [("Wklej {noun}",               "Umieść {noun} w polu {input}."),
               ("Kliknij {action}",           "Naciśnij przycisk {action}, aby uruchomić narzędzie."),
               ("Skopiuj wynik",              "Naciśnij {copy}, aby skopiować {output}.")],
        "ja": [("{noun} を貼り付け",            "{noun} を {input} 欄に貼り付けます。"),
               ("{action} をクリック",          "{action} ボタンを押してツールを実行します。"),
               ("結果をコピー",                "{copy} を押して {output} をコピーします。")],
        "nl": [("Plak je {noun}",             "Zet je {noun} in het {input}-veld."),
               ("Klik op {action}",           "Druk op de {action}-knop om de tool te draaien."),
               ("Kopieer het resultaat",      "Druk op {copy} om de {output} te kopiëren.")],
        "tr": [("{noun} verisini yapıştır",   "{noun} verisini {input} alanına bırak."),
               ("{action} düğmesine tıkla",   "Aracı çalıştırmak için {action} düğmesine bas."),
               ("Sonucu kopyala",             "{output} alanını kopyalamak için {copy} düğmesine bas.")],
        "id": [("Tempel {noun}-mu",           "Letakkan {noun}-mu di kolom {input}."),
               ("Klik {action}",              "Tekan tombol {action} untuk menjalankan alat."),
               ("Salin hasilnya",             "Tekan {copy} untuk menyalin {output}.")],
        "vi": [("Dán {noun} của bạn",         "Đưa {noun} của bạn vào ô {input}."),
               ("Nhấn {action}",              "Bấm nút {action} để chạy công cụ."),
               ("Sao chép kết quả",           "Bấm {copy} để sao chép {output}.")],
        "hi": [("अपना {noun} पेस्ट करें",       "अपना {noun} {input} फ़ील्ड में डालें।"),
               ("{action} पर क्लिक करें",       "टूल चलाने के लिए {action} बटन दबाएं।"),
               ("परिणाम कॉपी करें",            "{output} को कॉपी करने के लिए {copy} दबाएं।")],
        "sk": [("Vlož svoj {noun}",            "Vlož svoj {noun} do poľa {input}."),
               ("Klikni na {action}",          "Stlač tlačidlo {action}, aby si spustil nástroj."),
               ("Skopíruj výsledok",           "Stlač {copy}, aby si skopíroval {output}.")],
        "cs": [("Vlož svůj {noun}",            "Vlož svůj {noun} do pole {input}."),
               ("Klikni na {action}",          "Stiskni tlačítko {action}, abys spustil nástroj."),
               ("Zkopíruj výsledek",           "Stiskni {copy}, abys zkopíroval {output}.")],
    },
    "generate": {
        "en": [("Set your options",           "Pick the {noun} options you need."),
               ("Click {action}",             "Press {action} to produce a fresh {noun}."),
               ("Copy the result",            "Hit {copy} to copy the generated {noun}.")],
        "de": [("Optionen wählen",            "Wähle die gewünschten {noun}-Optionen."),
               ("{action} klicken",           "Drücke {action}, um ein neues {noun} zu erzeugen."),
               ("Ergebnis kopieren",          "Drücke {copy}, um das erzeugte {noun} zu kopieren.")],
        "es": [("Elige las opciones",         "Selecciona las opciones de {noun} que necesitas."),
               ("Haz clic en {action}",       "Pulsa {action} para producir un nuevo {noun}."),
               ("Copia el resultado",         "Pulsa {copy} para copiar el {noun} generado.")],
        "fr": [("Choisissez vos options",     "Sélectionnez les options de {noun} dont vous avez besoin."),
               ("Cliquez sur {action}",       "Appuyez sur {action} pour produire un nouveau {noun}."),
               ("Copiez le résultat",         "Appuyez sur {copy} pour copier le {noun} généré.")],
        "it": [("Imposta le opzioni",         "Scegli le opzioni di {noun} che ti servono."),
               ("Clicca {action}",            "Premi {action} per produrre un nuovo {noun}."),
               ("Copia il risultato",         "Premi {copy} per copiare il {noun} generato.")],
        "pt": [("Defina as opções",           "Escolha as opções de {noun} que precisar."),
               ("Clique em {action}",         "Pressione {action} para gerar um novo {noun}."),
               ("Copie o resultado",          "Pressione {copy} para copiar o {noun} gerado.")],
        "pl": [("Ustaw opcje",                "Wybierz opcje {noun}, jakich potrzebujesz."),
               ("Kliknij {action}",           "Naciśnij {action}, aby wygenerować nowy {noun}."),
               ("Skopiuj wynik",              "Naciśnij {copy}, aby skopiować wygenerowany {noun}.")],
        "ja": [("オプションを設定",            "必要な {noun} のオプションを選びます。"),
               ("{action} をクリック",         "{action} を押して新しい {noun} を生成します。"),
               ("結果をコピー",                "{copy} を押して生成された {noun} をコピーします。")],
        "nl": [("Stel je opties in",          "Kies de {noun}-opties die je nodig hebt."),
               ("Klik op {action}",           "Druk op {action} om een nieuwe {noun} te produceren."),
               ("Kopieer het resultaat",      "Druk op {copy} om de gegenereerde {noun} te kopiëren.")],
        "tr": [("Seçenekleri ayarla",         "İhtiyacın olan {noun} seçeneklerini seç."),
               ("{action} düğmesine tıkla",   "Yeni bir {noun} üretmek için {action} düğmesine bas."),
               ("Sonucu kopyala",             "Üretilen {noun} verisini kopyalamak için {copy} düğmesine bas.")],
        "id": [("Atur opsi",                  "Pilih opsi {noun} yang kamu butuhkan."),
               ("Klik {action}",              "Tekan {action} untuk menghasilkan {noun} baru."),
               ("Salin hasilnya",             "Tekan {copy} untuk menyalin {noun} yang dihasilkan.")],
        "vi": [("Đặt tùy chọn",               "Chọn các tùy chọn {noun} bạn cần."),
               ("Nhấn {action}",              "Bấm {action} để tạo {noun} mới."),
               ("Sao chép kết quả",           "Bấm {copy} để sao chép {noun} đã tạo.")],
        "hi": [("अपने विकल्प चुनें",            "जो {noun} विकल्प चाहिए वे चुनें।"),
               ("{action} पर क्लिक करें",       "नया {noun} बनाने के लिए {action} दबाएं।"),
               ("परिणाम कॉपी करें",            "बनाए गए {noun} को कॉपी करने के लिए {copy} दबाएं।")],
        "sk": [("Nastav možnosti",             "Vyber si možnosti {noun}, ktoré potrebuješ."),
               ("Klikni na {action}",          "Stlač {action}, aby si vytvoril nový {noun}."),
               ("Skopíruj výsledok",           "Stlač {copy}, aby si skopíroval vygenerovaný {noun}.")],
        "cs": [("Nastav možnosti",             "Vyber si možnosti {noun}, které potřebuješ."),
               ("Klikni na {action}",          "Stiskni {action}, abys vytvořil nový {noun}."),
               ("Zkopíruj výsledek",           "Stiskni {copy}, abys zkopíroval vygenerovaný {noun}.")],
    },
    "calculate": {
        "en": [("Enter your values",          "Type the {noun} inputs the tool needs."),
               ("Read the calculation",       "The {noun} result updates instantly — no button needed."),
               ("Use or copy the result",     "Hit {copy} if you need the {noun} value somewhere else.")],
        "de": [("Werte eingeben",             "Tippe die {noun}-Eingaben ein, die das Tool braucht."),
               ("Berechnung ablesen",         "Das {noun}-Ergebnis aktualisiert sich sofort — kein Klick nötig."),
               ("Ergebnis nutzen oder kopieren", "Drücke {copy}, falls du den {noun}-Wert woanders brauchst.")],
        "es": [("Introduce tus valores",      "Escribe los datos de {noun} que necesita la herramienta."),
               ("Mira el cálculo",            "El resultado de {noun} se actualiza al instante — sin botón."),
               ("Usa o copia el resultado",   "Pulsa {copy} si necesitas el valor de {noun} en otro sitio.")],
        "fr": [("Saisissez vos valeurs",      "Tapez les entrées de {noun} dont l'outil a besoin."),
               ("Lisez le calcul",            "Le résultat de {noun} se met à jour instantanément — pas de bouton."),
               ("Utilisez ou copiez le résultat", "Appuyez sur {copy} si vous avez besoin de la valeur de {noun} ailleurs.")],
        "it": [("Inserisci i valori",         "Digita gli input di {noun} che lo strumento richiede."),
               ("Leggi il calcolo",           "Il risultato di {noun} si aggiorna subito — senza pulsanti."),
               ("Usa o copia il risultato",   "Premi {copy} se ti serve il valore di {noun} altrove.")],
        "pt": [("Digite seus valores",        "Insira os dados de {noun} que a ferramenta precisa."),
               ("Leia o cálculo",             "O resultado de {noun} atualiza na hora — sem botão."),
               ("Use ou copie o resultado",   "Pressione {copy} se precisar do valor de {noun} em outro lugar.")],
        "pl": [("Wpisz swoje wartości",       "Wpisz dane {noun}, których potrzebuje narzędzie."),
               ("Odczytaj wynik",             "Wynik {noun} aktualizuje się natychmiast — bez przycisku."),
               ("Użyj lub skopiuj wynik",     "Naciśnij {copy}, jeśli potrzebujesz wartości {noun} gdzie indziej.")],
        "ja": [("値を入力",                   "ツールが必要とする {noun} の入力を打ち込みます。"),
               ("計算結果を確認",              "{noun} の結果はその場で更新されます — ボタン不要です。"),
               ("結果を使うかコピー",           "他の場所で {noun} の値が必要なら {copy} を押します。")],
        "nl": [("Voer je waarden in",         "Typ de {noun}-invoer in die de tool nodig heeft."),
               ("Lees de berekening",         "Het {noun}-resultaat werkt direct bij — geen knop nodig."),
               ("Gebruik of kopieer het resultaat", "Druk op {copy} als je de {noun}-waarde ergens anders nodig hebt.")],
        "tr": [("Değerlerini gir",            "Aracın ihtiyaç duyduğu {noun} girişlerini yaz."),
               ("Hesaplamayı oku",            "{noun} sonucu anında güncellenir — düğmeye gerek yok."),
               ("Sonucu kullan veya kopyala", "{noun} değerini başka bir yerde lazım edersen {copy} düğmesine bas.")],
        "id": [("Masukkan nilai-nilaimu",     "Ketik input {noun} yang dibutuhkan alat."),
               ("Baca hasilnya",              "Hasil {noun} diperbarui seketika — tanpa tombol."),
               ("Gunakan atau salin hasil",   "Tekan {copy} jika kamu butuh nilai {noun} di tempat lain.")],
        "vi": [("Nhập các giá trị của bạn",   "Gõ dữ liệu {noun} mà công cụ cần."),
               ("Đọc kết quả tính toán",      "Kết quả {noun} cập nhật tức thì — không cần nút."),
               ("Dùng hoặc sao chép kết quả", "Bấm {copy} nếu bạn cần giá trị {noun} ở nơi khác.")],
        "hi": [("अपने मान दर्ज करें",          "टूल को जो {noun} इनपुट चाहिए वे टाइप करें।"),
               ("गणना देखें",                  "{noun} परिणाम तुरंत अपडेट होता है — कोई बटन नहीं चाहिए।"),
               ("परिणाम इस्तेमाल करें या कॉपी करें", "अगर {noun} मान कहीं और चाहिए तो {copy} दबाएं।")],
        "sk": [("Zadaj svoje hodnoty",         "Napíš {noun} vstupy, ktoré nástroj potrebuje."),
               ("Prečítaj výpočet",            "Výsledok {noun} sa aktualizuje okamžite — bez tlačidla."),
               ("Použi alebo skopíruj výsledok", "Stlač {copy}, ak potrebuješ hodnotu {noun} inde.")],
        "cs": [("Zadej své hodnoty",           "Napiš {noun} vstupy, které nástroj potřebuje."),
               ("Přečti si výpočet",           "Výsledek {noun} se aktualizuje okamžitě — bez tlačítka."),
               ("Použij nebo zkopíruj výsledek", "Stiskni {copy}, pokud potřebuješ hodnotu {noun} jinde.")],
    },
    "compare": {
        "en": [("Paste both {noun} versions", "Drop each version of your {noun} into the two input fields."),
               ("Click {action}",             "Press {action} to spot the differences."),
               ("Read the diff",              "Scan the highlighted differences in the {output}.")],
        "de": [("Beide {noun}-Versionen einfügen", "Füge jede Version deines {noun} in eines der beiden Felder ein."),
               ("{action} klicken",           "Drücke {action}, um die Unterschiede zu finden."),
               ("Diff ablesen",               "Lies die hervorgehobenen Unterschiede in der {output} ab.")],
        "es": [("Pega las dos versiones de {noun}", "Coloca cada versión de tu {noun} en uno de los dos campos."),
               ("Haz clic en {action}",       "Pulsa {action} para detectar las diferencias."),
               ("Lee la diferencia",          "Revisa las diferencias resaltadas en la {output}.")],
        "fr": [("Collez les deux versions de {noun}", "Placez chaque version de votre {noun} dans l'un des deux champs."),
               ("Cliquez sur {action}",       "Appuyez sur {action} pour repérer les différences."),
               ("Lisez le diff",              "Parcourez les différences surlignées dans la {output}.")],
        "it": [("Incolla entrambe le versioni di {noun}", "Metti ciascuna versione del tuo {noun} in uno dei due campi."),
               ("Clicca {action}",            "Premi {action} per individuare le differenze."),
               ("Leggi il diff",              "Scorri le differenze evidenziate nell'{output}.")],
        "pt": [("Cole as duas versões do {noun}", "Coloque cada versão do seu {noun} em um dos dois campos."),
               ("Clique em {action}",         "Pressione {action} para encontrar as diferenças."),
               ("Leia o diff",                "Veja as diferenças destacadas na {output}.")],
        "pl": [("Wklej obie wersje {noun}",   "Umieść każdą wersję {noun} w jednym z dwóch pól."),
               ("Kliknij {action}",           "Naciśnij {action}, aby znaleźć różnice."),
               ("Odczytaj diff",              "Przejrzyj podświetlone różnice w {output}.")],
        "ja": [("両方の {noun} を貼り付け",     "それぞれの {noun} を 2 つの入力欄に貼り付けます。"),
               ("{action} をクリック",         "{action} を押して違いを検出します。"),
               ("差分を確認",                  "{output} のハイライト済みの差分を確認します。")],
        "nl": [("Plak beide {noun}-versies",  "Zet elke versie van je {noun} in een van de twee invoervelden."),
               ("Klik op {action}",           "Druk op {action} om de verschillen op te sporen."),
               ("Lees de diff",               "Bekijk de gemarkeerde verschillen in de {output}.")],
        "tr": [("İki {noun} sürümünü yapıştır","{noun} verisinin her sürümünü iki giriş alanından birine bırak."),
               ("{action} düğmesine tıkla",   "Farkları bulmak için {action} düğmesine bas."),
               ("Diff'i incele",              "{output} alanında vurgulanan farkları gözden geçir.")],
        "id": [("Tempel kedua versi {noun}",  "Letakkan tiap versi {noun}-mu di salah satu dari dua kolom input."),
               ("Klik {action}",              "Tekan {action} untuk menemukan perbedaannya."),
               ("Baca diff-nya",              "Telusuri perbedaan yang disorot di {output}.")],
        "vi": [("Dán cả hai phiên bản {noun}","Đưa từng phiên bản {noun} của bạn vào một trong hai ô nhập."),
               ("Nhấn {action}",              "Bấm {action} để phát hiện các khác biệt."),
               ("Đọc diff",                   "Xem các khác biệt được làm nổi bật trong {output}.")],
        "hi": [("दोनों {noun} संस्करण पेस्ट करें", "अपने {noun} के हर संस्करण को दो इनपुट फ़ील्ड में से एक में डालें।"),
               ("{action} पर क्लिक करें",        "अंतर ढूंढने के लिए {action} दबाएं।"),
               ("diff देखें",                   "{output} में हाइलाइट किए गए अंतर देखें।")],
        "sk": [("Vlož obe verzie {noun}",      "Daj každú verziu {noun} do jedného z dvoch vstupných polí."),
               ("Klikni na {action}",          "Stlač {action}, aby si zistil rozdiely."),
               ("Prečítaj diff",               "Pozri si zvýraznené rozdiely v {output}.")],
        "cs": [("Vlož obě verze {noun}",       "Dej každou verzi {noun} do jednoho ze dvou vstupních polí."),
               ("Klikni na {action}",          "Stiskni {action}, aby ses dostal k rozdílům."),
               ("Přečti si diff",              "Podívej se na zvýrazněné rozdíly v {output}.")],
    },
}


# Pre-translated nouns used across many manifests. Tools reference these by key
# (e.g. "noun": "text") to avoid duplicating translations.
NOUNS = {
    "text":     {"en": "text",     "de": "Text",     "es": "texto",    "fr": "texte",    "it": "testo",    "pt": "texto",    "pl": "tekst",    "ja": "テキスト",   "nl": "tekst",      "tr": "metin",      "id": "teks",       "vi": "văn bản",    "hi": "टेक्स्ट", "sk": "text", "cs": "text"},
    "password": {"en": "password", "de": "Passwort", "es": "contraseña","fr": "mot de passe","it": "password","pt": "senha",  "pl": "hasło",    "ja": "パスワード", "nl": "wachtwoord", "tr": "parola",     "id": "kata sandi", "vi": "mật khẩu",   "hi": "पासवर्ड", "sk": "heslo", "cs": "heslo"},
    "image":    {"en": "image",    "de": "Bild",     "es": "imagen",   "fr": "image",    "it": "immagine", "pt": "imagem",   "pl": "obraz",    "ja": "画像",       "nl": "afbeelding", "tr": "görsel",     "id": "gambar",     "vi": "hình ảnh",   "hi": "इमेज", "sk": "obrázok", "cs": "obrázek"},
    "color":    {"en": "color",    "de": "Farbe",    "es": "color",    "fr": "couleur",  "it": "colore",   "pt": "cor",      "pl": "kolor",    "ja": "色",         "nl": "kleur",      "tr": "renk",       "id": "warna",      "vi": "màu",        "hi": "रंग", "sk": "farba", "cs": "barva"},
    "date":     {"en": "date",     "de": "Datum",    "es": "fecha",    "fr": "date",     "it": "data",     "pt": "data",     "pl": "data",     "ja": "日付",       "nl": "datum",      "tr": "tarih",      "id": "tanggal",    "vi": "ngày",       "hi": "तारीख", "sk": "dátum", "cs": "datum"},
    "time":     {"en": "time",     "de": "Zeit",     "es": "hora",     "fr": "heure",    "it": "ora",      "pt": "hora",     "pl": "czas",     "ja": "時刻",       "nl": "tijd",       "tr": "saat",       "id": "waktu",      "vi": "thời gian",  "hi": "समय", "sk": "čas", "cs": "čas"},
    "timestamp":{"en": "timestamp","de": "Timestamp","es": "timestamp","fr": "timestamp","it": "timestamp","pt": "timestamp","pl": "znacznik czasu","ja": "タイムスタンプ","nl": "timestamp",  "tr": "timestamp",  "id": "timestamp",  "vi": "timestamp",  "hi": "timestamp", "sk": "timestamp", "cs": "timestamp"},
    "number":   {"en": "number",   "de": "Zahl",     "es": "número",   "fr": "nombre",   "it": "numero",   "pt": "número",   "pl": "liczba",   "ja": "数値",       "nl": "getal",      "tr": "sayı",       "id": "angka",      "vi": "số",         "hi": "संख्या", "sk": "číslo", "cs": "číslo"},
    "shadow":   {"en": "shadow",   "de": "Schatten", "es": "sombra",   "fr": "ombre",    "it": "ombra",    "pt": "sombra",   "pl": "cień",     "ja": "シャドウ",   "nl": "schaduw",    "tr": "gölge",      "id": "bayangan",   "vi": "bóng đổ",    "hi": "shadow", "sk": "tieň", "cs": "stín"},
    "gradient": {"en": "gradient", "de": "Verlauf",  "es": "degradado","fr": "dégradé",  "it": "gradiente","pt": "gradiente","pl": "gradient", "ja": "グラデーション","nl": "gradiënt",  "tr": "gradyan",    "id": "gradien",    "vi": "gradient",   "hi": "gradient", "sk": "gradient", "cs": "přechod"},
    "file size":{"en": "file size","de": "Dateigröße","es": "tamaño de archivo","fr": "taille de fichier","it": "dimensione file","pt": "tamanho de arquivo","pl": "rozmiar pliku","ja": "ファイルサイズ","nl": "bestandsgrootte","tr": "dosya boyutu","id": "ukuran file","vi": "kích thước file","hi": "फ़ाइल साइज़", "sk": "veľkosť súboru", "cs": "velikost souboru"},
    "unit":     {"en": "unit",     "de": "Einheit",  "es": "unidad",   "fr": "unité",    "it": "unità",    "pt": "unidade",  "pl": "jednostka","ja": "単位",       "nl": "eenheid",    "tr": "birim",      "id": "satuan",     "vi": "đơn vị",     "hi": "इकाई", "sk": "jednotka", "cs": "jednotka"},
    "percentage":{"en":"percentage","de":"Prozentwert","es":"porcentaje","fr":"pourcentage","it":"percentuale","pt":"porcentagem","pl":"procent","ja":"パーセント","nl":"percentage", "tr":"yüzde",       "id":"persentase",  "vi":"phần trăm",   "hi":"प्रतिशत", "sk": "percento", "cs": "procento"},
    "table":    {"en": "table",    "de": "Tabelle",  "es": "tabla",    "fr": "tableau",  "it": "tabella",  "pt": "tabela",   "pl": "tabela",   "ja": "表",         "nl": "tabel",      "tr": "tablo",      "id": "tabel",      "vi": "bảng",       "hi": "तालिका", "sk": "tabuľka", "cs": "tabulka"},
    "bill":     {"en": "bill",     "de": "Rechnung", "es": "cuenta",   "fr": "addition", "it": "conto",    "pt": "conta",    "pl": "rachunek", "ja": "請求額",     "nl": "rekening",   "tr": "hesap",      "id": "tagihan",    "vi": "hóa đơn",    "hi": "बिल", "sk": "účet", "cs": "účet"},
    "card number":{"en":"card number","de":"Kartennummer","es":"número de tarjeta","fr":"numéro de carte","it":"numero di carta","pt":"número do cartão","pl":"numer karty","ja":"カード番号","nl":"kaartnummer","tr":"kart numarası","id":"nomor kartu","vi":"số thẻ",  "hi":"कार्ड नंबर", "sk": "číslo karty", "cs": "číslo karty"},
    "email":    {"en": "email",    "de": "E-Mail",   "es": "correo",   "fr": "e-mail",   "it": "email",    "pt": "e-mail",   "pl": "e-mail",   "ja": "メール",     "nl": "e-mail",     "tr": "e-posta",    "id": "email",      "vi": "email",      "hi": "ईमेल", "sk": "e-mail", "cs": "e-mail"},
    "cron expression":{"en":"cron expression","de":"Cron-Ausdruck","es":"expresión cron","fr":"expression cron","it":"espressione cron","pt":"expressão cron","pl":"wyrażenie cron","ja":"cron 式","nl":"cron-expressie","tr":"cron ifadesi","id":"ekspresi cron","vi":"biểu thức cron","hi":"cron expression", "sk": "cron výraz", "cs": "cron výraz"},
    "query string":{"en":"query string","de":"Query-String","es":"cadena de consulta","fr":"chaîne de requête","it":"stringa di query","pt":"query string","pl":"query string","ja":"クエリ文字列","nl":"query-string","tr":"query string","id":"query string","vi":"query string","hi":"query string", "sk": "query string", "cs": "query string"},
    "color pair":{"en":"color pair","de":"Farbpaar","es":"par de colores","fr":"paire de couleurs","it":"coppia di colori","pt":"par de cores","pl":"para kolorów","ja":"色のペア","nl":"kleurenpaar","tr":"renk çifti","id":"pasangan warna","vi":"cặp màu",     "hi":"रंग जोड़ी", "sk": "dvojica farieb", "cs": "dvojice barev"},
    "roll":     {"en": "dice roll","de": "Würfelwurf","es":"tirada",   "fr": "lancer",   "it": "lancio",   "pt": "rolagem",  "pl": "rzut",     "ja": "ロール",     "nl": "worp",       "tr": "zar atışı",  "id": "lemparan dadu","vi": "lượt tung xúc xắc","hi": "पासे का दांव", "sk": "hod kockou", "cs": "hod kostkou"},
    "slug":     {"en": "slug",     "de": "Slug",     "es": "slug",     "fr": "slug",     "it": "slug",     "pt": "slug",     "pl": "slug",     "ja": "スラッグ",   "nl": "slug",       "tr": "slug",       "id": "slug",       "vi": "slug",       "hi": "slug", "sk": "slug", "cs": "slug"},
}


def _resolve_noun(noun, lang: str) -> str:
    if isinstance(noun, str) and noun in NOUNS:
        return NOUNS[noun][lang]
    if isinstance(noun, dict):
        return noun.get(lang) or noun.get("en", "")
    return str(noun)


def render_howto_schema(tool: dict, lang: str) -> str:
    spec = tool.get("howto")
    if not spec:
        return ""
    flow = spec.get("flow", "transform")
    if flow not in HOWTO_TEMPLATES:
        return ""
    action_key = spec.get("action", "format")
    noun = _resolve_noun(spec.get("noun", ""), lang)
    ui = UI[lang]
    fmt = {
        "noun": noun,
        "action": ui.get(action_key, ui["format"]),
        "input": ui["input"],
        "output": ui["output"],
        "copy": ui["copy"],
    }
    steps_tpl = HOWTO_TEMPLATES[flow].get(lang) or HOWTO_TEMPLATES[flow]["en"]
    steps = []
    for name_tpl, text_tpl in steps_tpl:
        name = name_tpl.format(**fmt).strip()
        text = text_tpl.format(**fmt).strip()
        # Tidy up double spaces from empty noun substitution.
        name = re.sub(r"\s+", " ", name)
        text = re.sub(r"\s+", " ", text)
        steps.append({"@type": "HowToStep", "name": name, "text": text})

    t_i18n = tool["i18n"][lang]
    doc = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": f"How to use {t_i18n['name']}" if lang == "en" else t_i18n["name"],
        "description": t_i18n["tagline"],
        "step": steps,
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(doc, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


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
        "LBL_INSTALL_APP_HINT": ui["install_app_hint"],
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
        "INSTALL_APP_HINT": ui["install_app_hint"],
        "LANGUAGE": ui["language"],
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
        "SEL_TR": sel["tr"],
        "SEL_ID": sel["id"],
        "SEL_VI": sel["vi"],
        "SEL_HI": sel["hi"],
        "SEL_SK": sel["sk"],
        "SEL_CS": sel["cs"],
        "ALTERNATE_LINKS": alternate_links(slug),
        "OG_LOCALE": OG_LOCALES.get(lang, "en_GB"),
        "INLANG": lang,
        "APP_CATEGORY": CATEGORY_TO_APP_CAT.get(cat, "UtilityApplication"),
        "APP_SUBCATEGORY": SUBCATEGORY_LABELS.get(cat, cat.title()),
        "FEATURE_LIST": feature_list_json,
        "OG_IMAGE_URL": f"https://toolhub.software/og-images/{slug}.png",
        "FAQPAGE_SCHEMA_JSON": render_faq_schema(tool, lang),
        "HOWTO_SCHEMA_JSON": render_howto_schema(tool, lang),
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
        "LANGUAGE": ui["language"],
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
        "SEL_TR": sel["tr"],
        "SEL_ID": sel["id"],
        "SEL_VI": sel["vi"],
        "SEL_HI": sel["hi"],
        "SEL_SK": sel["sk"],
        "SEL_CS": sel["cs"],
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
