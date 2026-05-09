TOOL = {
    "slug": "unicode-inspector",
    "category": "text",
    "icon": "🔎",
    "tags": ["unicode", "code point", "utf-8", "character", "inspect", "invisible", "encoding"],
    "i18n": {
        "en": {
            "name": "Unicode Inspector",
            "tagline": "Paste text → table of every code point. Hex, decimal, UTF-8 bytes, category. Spot invisible characters.",
            "description": "Free Unicode inspector. Paste any text and see each Unicode code point: hex, decimal, UTF-8 byte sequence, general category, and a name where known. Highlights invisible and confusable characters.",
        },
        "de": {"name": "Unicode-Inspektor", "tagline": "Text einfügen → Tabelle jedes Code-Points. Hex, Dezimal, UTF-8-Bytes, Kategorie. Unsichtbare Zeichen sichtbar machen.", "description": "Kostenloser Unicode-Inspektor. Text einfügen und für jeden Unicode-Code-Point sehen: Hex, Dezimal, UTF-8-Byte-Sequenz, Kategorie. Hebt unsichtbare und verwechselbare Zeichen hervor."},
        "es": {"name": "Inspector Unicode", "tagline": "Pega texto → tabla de cada code point. Hex, decimal, bytes UTF-8, categoría. Detecta caracteres invisibles.", "description": "Inspector Unicode gratuito. Pega cualquier texto y ve cada code point: hex, decimal, secuencia de bytes UTF-8, categoría general. Resalta caracteres invisibles y confundibles."},
        "fr": {"name": "Inspecteur Unicode", "tagline": "Collez du texte → tableau de chaque point de code. Hex, décimal, octets UTF-8, catégorie. Repère les caractères invisibles.", "description": "Inspecteur Unicode gratuit. Collez du texte et voyez chaque point de code Unicode : hex, décimal, séquence d'octets UTF-8, catégorie générale. Met en évidence les caractères invisibles et confondants."},
        "it": {"name": "Ispettore Unicode", "tagline": "Incolla testo → tabella di ogni code point. Hex, decimale, byte UTF-8, categoria. Trova caratteri invisibili.", "description": "Ispettore Unicode gratuito. Incolla qualsiasi testo e vedi ogni code point Unicode: hex, decimale, sequenza di byte UTF-8, categoria. Evidenzia caratteri invisibili e confondibili."},
        "pt": {"name": "Inspetor Unicode", "tagline": "Cole texto → tabela de cada code point. Hex, decimal, bytes UTF-8, categoria. Detecte caracteres invisíveis.", "description": "Inspetor Unicode gratuito. Cole qualquer texto e veja cada code point Unicode: hex, decimal, sequência de bytes UTF-8, categoria geral e o nome quando conhecido. Destaca caracteres invisíveis e confundíveis."},
        "pl": {"name": "Inspektor Unicode", "tagline": "Wklej tekst → tabela każdego code pointa. Hex, decimal, bajty UTF-8, kategoria. Wyłapuj niewidzialne znaki.", "description": "Darmowy inspektor Unicode. Wklej dowolny tekst i zobacz każdy code point Unicode: hex, decimal, sekwencję bajtów UTF-8, kategorię ogólną i nazwę, gdy znana. Podświetla znaki niewidzialne i zwodnicze."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="ui-in" oninput="uiRun()" placeholder="Paste text — try a string with emoji, accents, or invisible characters" spellcheck="false">Hello, café 🌍</textarea>
  <div class="meta" id="ui-summary" style="margin-top:0.5rem;font-family:ui-monospace,monospace;font-size:0.82rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ui-out" style="overflow:auto"></div>
</div>
""",
    "script": """
<style>
.ui-table{width:100%;border-collapse:collapse;font-family:ui-monospace,monospace;font-size:0.82rem}
.ui-table th{position:sticky;top:0;background:var(--surface);color:var(--text-muted);font-weight:600;font-size:0.75rem;text-align:left;padding:0.45rem 0.6rem;border-bottom:1px solid var(--border)}
.ui-table td{padding:0.4rem 0.6rem;border-bottom:1px solid var(--border);vertical-align:top}
.ui-table tr:hover{background:var(--card-hover)}
.ui-glyph{font-size:1.05rem;font-weight:600;color:var(--text);min-width:1.5rem;display:inline-block}
.ui-warn{color:#f7931e}
.ui-bad{color:#f85149}
.ui-cat{color:var(--text-muted);font-size:0.75rem}
.ui-bytes{color:var(--accent);font-size:0.78rem}
.ui-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0}
</style>
<script>
// Compact category lookup for common ranges
const UI_INVISIBLE = new Set([
  0x00A0, 0x1680, 0x180E, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006,
  0x2007, 0x2008, 0x2009, 0x200A, 0x200B, 0x200C, 0x200D, 0x200E, 0x200F,
  0x202F, 0x205F, 0x3000, 0xFEFF, 0x2028, 0x2029, 0x061C, 0x202A, 0x202B,
  0x202C, 0x202D, 0x202E, 0x2060, 0x2061, 0x2062, 0x2063, 0x2064, 0x206A,
  0x206B, 0x206C, 0x206D, 0x206E, 0x206F, 0xFFF9, 0xFFFA, 0xFFFB
]);
const UI_NAMED = {
  0x0009:'CHARACTER TABULATION', 0x000A:'LINE FEED', 0x000B:'LINE TABULATION',
  0x000C:'FORM FEED', 0x000D:'CARRIAGE RETURN', 0x0020:'SPACE',
  0x00A0:'NO-BREAK SPACE', 0x00AD:'SOFT HYPHEN', 0x00B7:'MIDDLE DOT',
  0x180E:'MONGOLIAN VOWEL SEPARATOR',
  0x200B:'ZERO WIDTH SPACE', 0x200C:'ZERO WIDTH NON-JOINER', 0x200D:'ZERO WIDTH JOINER',
  0x200E:'LEFT-TO-RIGHT MARK', 0x200F:'RIGHT-TO-LEFT MARK',
  0x2028:'LINE SEPARATOR', 0x2029:'PARAGRAPH SEPARATOR',
  0x202A:'LEFT-TO-RIGHT EMBEDDING', 0x202B:'RIGHT-TO-LEFT EMBEDDING',
  0x202C:'POP DIRECTIONAL FORMATTING', 0x202D:'LEFT-TO-RIGHT OVERRIDE',
  0x202E:'RIGHT-TO-LEFT OVERRIDE', 0x202F:'NARROW NO-BREAK SPACE',
  0x205F:'MEDIUM MATHEMATICAL SPACE',
  0x2060:'WORD JOINER', 0x2063:'INVISIBLE SEPARATOR', 0x2064:'INVISIBLE PLUS',
  0x3000:'IDEOGRAPHIC SPACE', 0xFEFF:'BYTE ORDER MARK / ZERO WIDTH NO-BREAK SPACE',
  0xFE0F:'VARIATION SELECTOR-16 (emoji presentation)',
  0xFE0E:'VARIATION SELECTOR-15 (text presentation)',
  0x061C:'ARABIC LETTER MARK',
};
function uiCat(cp){
  if(cp <= 0x1F || cp === 0x7F) return ['Cc', 'control'];
  if(cp >= 0x80 && cp <= 0x9F) return ['Cc', 'control'];
  if(cp === 0x20) return ['Zs', 'space'];
  if(cp >= 0x30 && cp <= 0x39) return ['Nd', 'digit'];
  if((cp >= 0x41 && cp <= 0x5A) || (cp >= 0x61 && cp <= 0x7A)) return ['L', 'letter'];
  if(cp >= 0xD800 && cp <= 0xDFFF) return ['Cs', 'surrogate'];
  if(UI_INVISIBLE.has(cp)) return ['Cf', 'format/invisible'];
  if(cp >= 0xE000 && cp <= 0xF8FF) return ['Co', 'private-use'];
  if(cp >= 0x1D400 && cp <= 0x1D7FF) return ['L', 'math letter'];
  if(cp >= 0x1F300 && cp <= 0x1FAFF) return ['So', 'symbol/emoji'];
  if(cp >= 0x2600 && cp <= 0x27BF) return ['So', 'symbol/dingbat'];
  if(cp >= 0x2000 && cp <= 0x206F) return ['P', 'punctuation/format'];
  if(cp >= 0x4E00 && cp <= 0x9FFF) return ['Lo', 'han ideograph'];
  if(cp >= 0x3040 && cp <= 0x309F) return ['Lo', 'hiragana'];
  if(cp >= 0x30A0 && cp <= 0x30FF) return ['Lo', 'katakana'];
  if(cp >= 0xAC00 && cp <= 0xD7AF) return ['Lo', 'hangul'];
  if(cp >= 0x0590 && cp <= 0x05FF) return ['L', 'hebrew'];
  if(cp >= 0x0600 && cp <= 0x06FF) return ['L', 'arabic'];
  if(cp >= 0x0400 && cp <= 0x04FF) return ['L', 'cyrillic'];
  if(cp >= 0x0370 && cp <= 0x03FF) return ['L', 'greek'];
  if((cp >= 0x80 && cp <= 0xFF)) return ['?', 'latin-1 supplement'];
  return ['?', '—'];
}
function uiToUtf8(cp){
  const bytes = [];
  if(cp < 0x80) bytes.push(cp);
  else if(cp < 0x800){
    bytes.push(0xC0 | (cp >> 6), 0x80 | (cp & 0x3F));
  } else if(cp < 0x10000){
    bytes.push(0xE0 | (cp >> 12), 0x80 | ((cp >> 6) & 0x3F), 0x80 | (cp & 0x3F));
  } else {
    bytes.push(0xF0 | (cp >> 18), 0x80 | ((cp >> 12) & 0x3F), 0x80 | ((cp >> 6) & 0x3F), 0x80 | (cp & 0x3F));
  }
  return bytes.map(b => b.toString(16).toUpperCase().padStart(2,'0')).join(' ');
}
function uiName(cp){
  if(UI_NAMED[cp]) return UI_NAMED[cp];
  if(cp <= 0x1F){
    const ctrls = ['NULL','START OF HEADING','START OF TEXT','END OF TEXT','END OF TRANSMISSION','ENQUIRY','ACKNOWLEDGE','BELL','BACKSPACE','TAB','LINE FEED','VERTICAL TAB','FORM FEED','CARRIAGE RETURN','SHIFT OUT','SHIFT IN','DATA LINK ESCAPE','DEVICE CONTROL ONE','DEVICE CONTROL TWO','DEVICE CONTROL THREE','DEVICE CONTROL FOUR','NEGATIVE ACK','SYNCHRONOUS IDLE','END OF TRANS BLOCK','CANCEL','END OF MEDIUM','SUBSTITUTE','ESCAPE','FILE SEP','GROUP SEP','RECORD SEP','UNIT SEP'];
    return 'CONTROL: ' + ctrls[cp];
  }
  if(cp === 0x7F) return 'DELETE';
  return '';
}
function uiGlyph(cp){
  if(cp === 0x20) return '<span class="ui-warn">␠</span>';
  if(cp === 0x09) return '<span class="ui-warn">↹</span>';
  if(cp === 0x0A) return '<span class="ui-warn">↵</span>';
  if(cp === 0x0D) return '<span class="ui-warn">␍</span>';
  if(cp <= 0x1F || cp === 0x7F) return '<span class="ui-bad">␀</span>';
  if(UI_INVISIBLE.has(cp)) return '<span class="ui-bad">⌧</span>';
  return String.fromCodePoint(cp);
}
function uiEsc(s){ return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function uiRun(){
  const s = document.getElementById('ui-in').value;
  const out = document.getElementById('ui-out');
  const sum = document.getElementById('ui-summary');
  if(s === ''){ out.innerHTML = '<div class="ui-empty">Paste text above.</div>'; sum.textContent = ''; return; }
  const codePoints = [...s];
  let totalBytes = 0;
  let invisibleCount = 0;
  const rows = codePoints.map((ch, i) => {
    const cp = ch.codePointAt(0);
    const utf8 = uiToUtf8(cp);
    totalBytes += utf8.split(' ').length;
    const [cat, catName] = uiCat(cp);
    const isInv = UI_INVISIBLE.has(cp) || (cp <= 0x1F) || cp === 0x7F;
    if(isInv) invisibleCount++;
    const name = uiName(cp);
    const hex = 'U+' + cp.toString(16).toUpperCase().padStart(4,'0');
    return `<tr${isInv?' style="background:rgba(247,147,30,0.08)"':''}><td>${i}</td><td><span class="ui-glyph">${uiGlyph(cp)}</span></td><td>${hex}</td><td>${cp}</td><td><span class="ui-bytes">${utf8}</span></td><td><span class="ui-cat">${cat} · ${catName}</span></td><td><span class="ui-cat">${uiEsc(name)}</span></td></tr>`;
  }).join('');
  out.innerHTML = `<table class="ui-table">
    <thead><tr><th>#</th><th>Glyph</th><th>Code point</th><th>Decimal</th><th>UTF-8</th><th>Category</th><th>Name</th></tr></thead>
    <tbody>${rows}</tbody></table>`;
  const utf16 = s.length;
  const summary = `${codePoints.length} code points · ${utf16} UTF-16 units · ${totalBytes} UTF-8 bytes` + (invisibleCount ? ` · <span class="ui-warn">${invisibleCount} invisible/control character${invisibleCount===1?'':'s'}</span>` : '');
  sum.innerHTML = summary;
}
document.addEventListener('DOMContentLoaded', uiRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>"Why won't this string compare equal?" "Why is this username refused as already taken when it looks free?" "Why does this filename break my shell?" The answer is almost always: the bytes don't match what your eyes see. Two characters can <em>look</em> identical but be different code points (Latin "a" vs Cyrillic "а"); whitespace can hide non-breaking spaces, zero-width joiners, or right-to-left overrides; an emoji can be one code point or four. This tool decomposes any text down to its individual Unicode code points, with hex, decimal, UTF-8 byte sequence, category, and a name where known.</p>

<h3>When to use it</h3>
<ul>
  <li>Diagnosing a "looks the same but isn't equal" string bug.</li>
  <li>Finding invisible characters (zero-width space, BOM, RTL override) hiding inside copy-pasted text.</li>
  <li>Counting bytes vs code points vs UTF-16 code units before storing in a fixed-width column.</li>
  <li>Inspecting an emoji to see which ZWJ sequence it uses.</li>
  <li>Spotting homoglyph attacks in domain names or usernames.</li>
  <li>Generating exact UTF-8 byte sequences for a hex dump.</li>
</ul>

<h3>Reading the output</h3>
<ul>
  <li><strong>Code point</strong> — the abstract Unicode value, written <code>U+XXXX</code>. There are 1.1 million of them; the highest in use is U+10FFFF.</li>
  <li><strong>UTF-8</strong> — how that code point is encoded as bytes in modern files (1–4 bytes each).</li>
  <li><strong>UTF-16 code units</strong> — what JavaScript strings (<code>s.length</code>) and Java strings count. A code point above U+FFFF (most emoji) takes <em>two</em> UTF-16 units (a surrogate pair).</li>
  <li><strong>Category</strong> — Unicode's general category abbreviation: L=letter, N=number, P=punctuation, S=symbol, Z=separator, C=control/format/private.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Length is ambiguous.</strong> "👨‍👩‍👧" has 1 grapheme cluster, 5 code points, 11 UTF-16 units, and 18 UTF-8 bytes — all "lengths" that something might report.</li>
  <li><strong>Zero-width joiner sequences vs sequence selectors.</strong> Many emoji are ZWJ sequences: family, profession, skin-tone variants. Reordering or stripping a ZWJ changes what's rendered.</li>
  <li><strong>Normalisation matters.</strong> "café" can be e+◌́ (NFD) or é (NFC). They look identical but are different bytes; databases and comparison code must normalise to the same form.</li>
  <li><strong>Right-to-left overrides are dangerous.</strong> A filename containing U+202E can flip its display order — making <code>resu&#x202E;txt.exe</code> look like <code>resuexe.txt</code> in a file browser. Used in phishing.</li>
  <li><strong>The name column is partial.</strong> A real Unicode database has names for every code point; the inspector only ships names for control characters and common format/whitespace characters where the name is the most useful diagnostic.</li>
  <li><strong>Surrogate halves shouldn't appear standalone.</strong> If you see U+D800–U+DFFF in the output, the input is a malformed UTF-16 string (lone surrogate). Most APIs will refuse to encode that to UTF-8.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>"Por que essa string não compara igual?" "Por que esse username é recusado como já existente quando parece livre?" "Por que esse nome de arquivo quebra meu shell?" A resposta é quase sempre: os bytes não batem com o que seus olhos veem. Dois caracteres podem <em>parecer</em> idênticos mas serem code points diferentes (o "a" latino vs o "а" cirílico); whitespace pode esconder no-break spaces, zero-width joiners ou overrides RTL; um emoji pode ser um code point ou quatro. Esta ferramenta decompõe qualquer texto até seus code points Unicode individuais, com hex, decimal, sequência de bytes UTF-8, categoria e um nome quando conhecido.</p>

<h3>Quando usar</h3>
<ul>
  <li>Diagnosticar um bug de string "parece igual mas não é igual".</li>
  <li>Encontrar caracteres invisíveis (zero-width space, BOM, override RTL) escondidos em texto colado.</li>
  <li>Contar bytes vs code points vs unidades UTF-16 antes de armazenar em uma coluna de largura fixa.</li>
  <li>Inspecionar um emoji para ver qual sequência ZWJ ele usa.</li>
  <li>Detectar ataques de homoglyph em domínios ou usernames.</li>
  <li>Gerar sequências exatas de bytes UTF-8 para um hex dump.</li>
</ul>

<h3>Lendo a saída</h3>
<ul>
  <li><strong>Code point</strong> — o valor Unicode abstrato, escrito <code>U+XXXX</code>. Existem 1,1 milhão deles; o mais alto em uso é U+10FFFF.</li>
  <li><strong>UTF-8</strong> — como aquele code point é codificado em bytes em arquivos modernos (1–4 bytes cada).</li>
  <li><strong>Unidades UTF-16</strong> — o que strings JavaScript (<code>s.length</code>) e strings Java contam. Um code point acima de U+FFFF (a maioria dos emoji) ocupa <em>duas</em> unidades UTF-16 (um surrogate pair).</li>
  <li><strong>Categoria</strong> — abreviação da categoria geral do Unicode: L=letra, N=número, P=pontuação, S=símbolo, Z=separador, C=control/format/private.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>O comprimento é ambíguo.</strong> "👨‍👩‍👧" tem 1 cluster de grafema, 5 code points, 11 unidades UTF-16 e 18 bytes UTF-8 — todos "tamanhos" que algum sistema pode reportar.</li>
  <li><strong>Sequências zero-width joiner vs seletores de sequência.</strong> Muitos emoji são sequências ZWJ: família, profissão, variantes de tom de pele. Reordenar ou remover um ZWJ muda o que é renderizado.</li>
  <li><strong>Normalização importa.</strong> "café" pode ser e+◌́ (NFD) ou é (NFC). Parecem idênticos mas são bytes diferentes; bancos de dados e código de comparação precisam normalizar para a mesma forma.</li>
  <li><strong>Overrides right-to-left são perigosos.</strong> Um nome de arquivo contendo U+202E pode inverter sua ordem de exibição — fazendo <code>resu&#x202E;txt.exe</code> parecer <code>resuexe.txt</code> num gerenciador de arquivos. Usado em phishing.</li>
  <li><strong>A coluna de nome é parcial.</strong> Uma base Unicode de verdade tem nomes para cada code point; o inspetor só traz nomes para caracteres de controle e caracteres comuns de format/whitespace, onde o nome é o diagnóstico mais útil.</li>
  <li><strong>Metades de surrogate não devem aparecer sozinhas.</strong> Se você vê U+D800–U+DFFF na saída, a entrada é uma string UTF-16 malformada (lone surrogate). A maioria das APIs vai se recusar a codificar isso para UTF-8.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Wenn Strings ungleich verglichen werden, obwohl sie gleich aussehen, oder ein Username als "vergeben" abgelehnt wird, obwohl er frei wirkt — die Bytes stimmen nicht überein. Lateinisches "a" vs kyrillisches "а", versteckte Zero-Width-Spaces, RTL-Overrides — die Liste ist lang. Dieses Tool zerlegt jeden Text in einzelne Unicode-Code-Points mit Hex, Dezimal, UTF-8-Bytes, Kategorie und Name (soweit bekannt).</p>
<h3>Wann verwenden</h3>
<ul>
<li>"Sieht gleich aus, ist aber ungleich"-Bugs untersuchen.</li>
<li>Unsichtbare Zeichen (BOM, ZWS, RTL-Override) finden.</li>
<li>Bytes vs Code-Points vs UTF-16-Units zählen.</li>
<li>Emoji auf ZWJ-Sequenz prüfen.</li>
<li>Homoglyph-Angriffe in Domains/Usernames erkennen.</li>
</ul>
<h3>Ausgabe lesen</h3>
<ul>
<li><strong>Code Point</strong> — abstrakter Unicode-Wert <code>U+XXXX</code>.</li>
<li><strong>UTF-8</strong> — Byte-Encoding (1–4 Bytes pro Code-Point).</li>
<li><strong>UTF-16-Units</strong> — was JS und Java zählen; ein Code-Point > U+FFFF braucht 2 Units.</li>
<li><strong>Kategorie</strong> — L Buchstabe, N Zahl, P Punktuation, S Symbol, C Steuerzeichen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Länge ist mehrdeutig.</strong> 👨‍👩‍👧 = 1 Cluster, 5 Code-Points, 11 UTF-16-Units, 18 UTF-8-Bytes.</li>
<li><strong>Normalisierung zählt.</strong> "café" kann NFC oder NFD sein — gleiche Optik, andere Bytes.</li>
<li><strong>RTL-Overrides sind gefährlich.</strong> U+202E in Dateinamen für Phishing.</li>
<li><strong>Standalone-Surrogate</strong> bedeuten kaputten UTF-16-Input.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Cuando dos cadenas que parecen iguales no comparan iguales, o un nombre de usuario aparentemente libre es rechazado, los bytes no coinciden con lo que ves. "a" latina vs "а" cirílica, espacios de ancho cero, overrides RTL — el catálogo es largo. Esta herramienta descompone cualquier texto en sus code points individuales con hex, decimal, bytes UTF-8, categoría y nombre conocido.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Bugs de "se ve igual pero no es igual".</li>
<li>Encontrar caracteres invisibles (BOM, ZWS, RTL).</li>
<li>Contar bytes vs code points vs unidades UTF-16.</li>
<li>Inspeccionar la secuencia ZWJ de un emoji.</li>
<li>Detectar ataques de homoglyph en dominios.</li>
</ul>
<h3>Lectura</h3>
<ul>
<li><strong>Code point</strong> — valor Unicode abstracto <code>U+XXXX</code>.</li>
<li><strong>UTF-8</strong> — bytes (1–4 por code point).</li>
<li><strong>Unidades UTF-16</strong> — lo que JS y Java cuentan; > U+FFFF usa 2.</li>
<li><strong>Categoría</strong> — L letra, N número, P puntuación, S símbolo, C control.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>La longitud es ambigua.</strong> 👨‍👩‍👧 = 1 cluster, 5 code points, 11 UTF-16, 18 bytes UTF-8.</li>
<li><strong>La normalización importa.</strong> "café" puede ser NFC o NFD.</li>
<li><strong>Los RTL overrides son peligrosos.</strong> U+202E en nombres de fichero para phishing.</li>
<li><strong>Substitutos sueltos</strong> indican UTF-16 mal formado.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Quand deux chaînes identiques visuellement ne sont pas égales, ou qu'un identifiant apparemment libre est refusé : les octets ne correspondent pas à ce que vous voyez. "a" latin vs "а" cyrillique, espaces de largeur nulle, overrides RTL. Cet outil décompose tout texte en points de code Unicode avec hex, décimal, octets UTF-8, catégorie et nom.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Bugs "ça a l'air pareil, ce n'est pas égal".</li>
<li>Trouver caractères invisibles (BOM, ZWS, RTL).</li>
<li>Compter octets vs points de code vs unités UTF-16.</li>
<li>Inspecter la séquence ZWJ d'un emoji.</li>
<li>Détecter homoglyphes dans les domaines.</li>
</ul>
<h3>Lecture</h3>
<ul>
<li><strong>Point de code</strong> — valeur Unicode <code>U+XXXX</code>.</li>
<li><strong>UTF-8</strong> — octets (1–4 par point de code).</li>
<li><strong>UTF-16</strong> — ce que JS et Java comptent ; > U+FFFF prend 2 unités.</li>
<li><strong>Catégorie</strong> — L lettre, N nombre, P ponctuation, S symbole, C contrôle.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Longueur ambiguë.</strong> 👨‍👩‍👧 = 1 cluster, 5 points de code, 11 UTF-16, 18 octets UTF-8.</li>
<li><strong>La normalisation compte.</strong> "café" peut être NFC ou NFD.</li>
<li><strong>RTL overrides dangereux.</strong> U+202E dans les noms de fichier pour le phishing.</li>
<li><strong>Substituts isolés</strong> = UTF-16 cassé.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Quando due stringhe apparentemente identiche non sono uguali, o uno username sembra libero ma è rifiutato: i byte non coincidono con ciò che vedi. "a" latina vs "а" cirillica, spazi a larghezza zero, override RTL. Questo strumento decompone qualsiasi testo nei singoli code point Unicode con hex, decimale, byte UTF-8, categoria e nome.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Bug "sembra uguale ma non lo è".</li>
<li>Trovare caratteri invisibili (BOM, ZWS, RTL).</li>
<li>Contare byte vs code point vs unità UTF-16.</li>
<li>Ispezionare la sequenza ZWJ di un emoji.</li>
<li>Rilevare attacchi homoglyph nei domini.</li>
</ul>
<h3>Lettura</h3>
<ul>
<li><strong>Code point</strong> — valore Unicode <code>U+XXXX</code>.</li>
<li><strong>UTF-8</strong> — byte (1–4 per code point).</li>
<li><strong>UTF-16</strong> — ciò che contano JS e Java; > U+FFFF usa 2 unità.</li>
<li><strong>Categoria</strong> — L lettera, N numero, P punteggiatura, S simbolo, C controllo.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>La lunghezza è ambigua.</strong> 👨‍👩‍👧 = 1 cluster, 5 code point, 11 UTF-16, 18 byte UTF-8.</li>
<li><strong>La normalizzazione conta.</strong> "café" può essere NFC o NFD.</li>
<li><strong>RTL override pericolosi.</strong> U+202E nei nomi file per phishing.</li>
<li><strong>Surrogati isolati</strong> = UTF-16 malformato.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>"Dlaczego ten string nie porównuje się jako równy?" "Dlaczego ten username jest odrzucany jako już zajęty, choć wygląda na wolny?" "Dlaczego ta nazwa pliku łamie mi shell?" Odpowiedź prawie zawsze brzmi: bajty nie pasują do tego, co widzą oczy. Dwa znaki mogą <em>wyglądać</em> identycznie, ale być różnymi code pointami (łacińskie "a" vs cyryliczne "а"); whitespace może ukrywać non-breaking spaces, zero-width joinery albo right-to-left override'y; emoji może być jednym code pointem albo czterema. To narzędzie rozkłada dowolny tekst na poszczególne code pointy Unicode, z hex, decimal, sekwencją bajtów UTF-8, kategorią i nazwą, gdy znana.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Diagnoza buga "wygląda tak samo, ale nie jest równe".</li>
  <li>Znalezienie niewidzialnych znaków (zero-width space, BOM, override RTL) ukrytych w skopiowanym tekście.</li>
  <li>Liczenie bajtów vs code pointów vs jednostek UTF-16 przed zapisem do kolumny o stałej szerokości.</li>
  <li>Inspekcja emoji, żeby zobaczyć, której sekwencji ZWJ używa.</li>
  <li>Wyłapywanie ataków homoglyph w nazwach domen albo username'ach.</li>
  <li>Generowanie dokładnych sekwencji bajtów UTF-8 do hex dumpa.</li>
</ul>

<h3>Czytanie wyjścia</h3>
<ul>
  <li><strong>Code point</strong> — abstrakcyjna wartość Unicode, zapisana <code>U+XXXX</code>. Jest ich 1,1 mln; najwyższy w użyciu to U+10FFFF.</li>
  <li><strong>UTF-8</strong> — jak ten code point jest kodowany w bajty w nowoczesnych plikach (1–4 bajty na znak).</li>
  <li><strong>Jednostki UTF-16</strong> — to, co liczą stringi JavaScriptu (<code>s.length</code>) i stringi Javy. Code point powyżej U+FFFF (większość emoji) zajmuje <em>dwie</em> jednostki UTF-16 (parę surrogate'ów).</li>
  <li><strong>Kategoria</strong> — skrót ogólnej kategorii Unicode: L=letter, N=number, P=punctuation, S=symbol, Z=separator, C=control/format/private.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Długość jest dwuznaczna.</strong> "👨‍👩‍👧" ma 1 grapheme cluster, 5 code pointów, 11 jednostek UTF-16 i 18 bajtów UTF-8 — to wszystko "długości", które coś może raportować.</li>
  <li><strong>Sekwencje zero-width joiner vs sekwencje selektorów.</strong> Wiele emoji to sekwencje ZWJ: rodzina, profesja, warianty tonu skóry. Przestawienie albo wycięcie ZWJ zmienia to, co jest renderowane.</li>
  <li><strong>Normalizacja ma znaczenie.</strong> "café" może być e+◌́ (NFD) albo é (NFC). Wyglądają identycznie, ale to różne bajty; bazy i kod porównujący muszą znormalizować do tej samej formy.</li>
  <li><strong>Right-to-left override'y są niebezpieczne.</strong> Nazwa pliku zawierająca U+202E może odwrócić swoje wyświetlanie — sprawiając, że <code>resu&#x202E;txt.exe</code> wygląda jak <code>resuexe.txt</code> w eksploratorze plików. Używane w phishingu.</li>
  <li><strong>Kolumna nazw jest częściowa.</strong> Prawdziwa baza Unicode ma nazwy dla każdego code pointa; inspektor podaje nazwy tylko dla znaków sterujących i typowych znaków format/whitespace, gdzie nazwa jest najbardziej użyteczną diagnostyką.</li>
  <li><strong>Połówki surrogate'ów nie powinny pojawiać się samodzielnie.</strong> Jeśli widzisz U+D800–U+DFFF w wyjściu, wejście to zniekształcony string UTF-16 (lone surrogate). Większość API odmówi zakodowania tego do UTF-8.</li>
</ul>
""",
    },
    "related": ["ascii-table", "emoji-picker", "html-encoder"],
}
