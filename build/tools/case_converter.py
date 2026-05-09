TOOL = {
    "slug": "case-converter",
    "category": "text",
    "icon": "Aa",
    "tags": ["case", "convert", "camel", "snake", "kebab", "pascal", "title", "upper", "lower"],
    "i18n": {
        "en": {
            "name": "Case Converter",
            "tagline": "Convert text between UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE, and dot.case.",
            "description": "Free online case converter. Switch text between upper, lower, title, sentence, camel, pascal, snake, kebab, constant, and dot case in one click.",
        },
        "de": {"name": "Schreibweisen-Konverter", "tagline": "Wandle Text zwischen GROSS, klein, Titel, Satz, camelCase, PascalCase, snake_case, kebab-case, KONSTANTE und dot.case um.", "description": "Kostenloser Schreibweisen-Konverter für GROSS, klein, Titel, Satz, camel, pascal, snake, kebab, konstante und Punkt-Schreibweise."},
        "es": {"name": "Conversor de Mayúsculas", "tagline": "Convierte texto entre MAYÚSCULAS, minúsculas, Título, Oración, camelCase, PascalCase, snake_case, kebab-case, CONSTANTE y dot.case.", "description": "Conversor de mayúsculas/minúsculas gratuito. MAYÚS, minús, título, oración, camel, pascal, snake, kebab, constante y punto."},
        "fr": {"name": "Convertisseur de Casse", "tagline": "Convertissez du texte entre MAJUSCULES, minuscules, Titre, Phrase, camelCase, PascalCase, snake_case, kebab-case, CONSTANTE et dot.case.", "description": "Convertisseur de casse gratuit. MAJ, min, titre, phrase, camel, pascal, snake, kebab, constante et point."},
        "it": {"name": "Convertitore di Maiuscole/Minuscole", "tagline": "Converti testo tra MAIUSCOLO, minuscolo, Titolo, Frase, camelCase, PascalCase, snake_case, kebab-case, COSTANTE e dot.case.", "description": "Convertitore di maiuscole/minuscole gratuito. MAIUSC, minusc, titolo, frase, camel, pascal, snake, kebab, costante e punto."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="cc-input" oninput="ccRun()" placeholder="Paste or type any text here" spellcheck="false">The Quick Brown Fox Jumps Over the Lazy Dog</textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="case-grid" id="cc-out"></div>
</div>
""",
    "script": """
<style>
.case-grid{display:grid;gap:0.6rem}
.case-row{display:grid;grid-template-columns:140px 1fr auto;gap:0.6rem;align-items:center;padding:0.55rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px}
.case-row .lbl{font-size:0.78rem;color:var(--text-muted);font-family:ui-monospace,monospace}
.case-row .val{font-family:ui-monospace,monospace;font-size:0.9rem;word-break:break-word;overflow-wrap:anywhere}
.case-row button{padding:0.3rem 0.65rem;font-size:0.78rem}
@media(max-width:600px){.case-row{grid-template-columns:1fr;gap:0.25rem}.case-row button{justify-self:start}}
</style>
<script>
function ccWords(s){
  return s
    .replace(/([a-z\\d])([A-Z])/g, '$1 $2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2')
    .replace(/[_\\-\\.\\s/]+/g, ' ')
    .trim()
    .split(/\\s+/)
    .filter(Boolean);
}
const CC_FORMS = [
  ['UPPER',     w => w.map(x=>x.toUpperCase()).join(' ')],
  ['lower',     w => w.map(x=>x.toLowerCase()).join(' ')],
  ['Title',     w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join(' ')],
  ['Sentence',  w => w.length ? (w[0][0].toUpperCase()+w[0].slice(1).toLowerCase()+(w.length>1?' '+w.slice(1).map(x=>x.toLowerCase()).join(' '):'')) : ''],
  ['camelCase', w => w.map((x,i)=>i===0?x.toLowerCase():x[0].toUpperCase()+x.slice(1).toLowerCase()).join('')],
  ['PascalCase',w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join('')],
  ['snake_case',w => w.map(x=>x.toLowerCase()).join('_')],
  ['kebab-case',w => w.map(x=>x.toLowerCase()).join('-')],
  ['CONSTANT',  w => w.map(x=>x.toUpperCase()).join('_')],
  ['dot.case',  w => w.map(x=>x.toLowerCase()).join('.')],
  ['path/case', w => w.map(x=>x.toLowerCase()).join('/')],
  ['Train-Case',w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join('-')],
  ['inverse',   (w,raw) => raw.split('').map(c=>c===c.toLowerCase()?c.toUpperCase():c.toLowerCase()).join('')],
  ['aLtErNaTe', (w,raw) => raw.split('').map((c,i)=>i%2?c.toUpperCase():c.toLowerCase()).join('')],
];
function ccCopy(text, btn){
  navigator.clipboard.writeText(text);
  const old = btn.textContent;
  btn.textContent = '✓';
  setTimeout(()=>btn.textContent = old, 900);
}
function ccRun(){
  const raw = document.getElementById('cc-input').value;
  const words = ccWords(raw);
  const out = document.getElementById('cc-out');
  out.innerHTML = '';
  CC_FORMS.forEach(([label, fn]) => {
    const val = fn(words, raw);
    const row = document.createElement('div');
    row.className = 'case-row';
    const l = document.createElement('div'); l.className = 'lbl'; l.textContent = label;
    const v = document.createElement('div'); v.className = 'val'; v.textContent = val || '—';
    const b = document.createElement('button'); b.className = 'secondary'; b.textContent = '{LBL_COPY}';
    b.onclick = () => ccCopy(val, b);
    row.appendChild(l); row.appendChild(v); row.appendChild(b);
    out.appendChild(row);
  });
}
document.addEventListener('DOMContentLoaded', ccRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Every language and platform has its own conventions for naming things — JavaScript wants <code>camelCase</code>, Python wants <code>snake_case</code>, CSS wants <code>kebab-case</code>, environment variables want <code>CONSTANT_CASE</code>. Translating between them by hand is fiddly, especially with edge cases (acronyms, numbers, existing separators). This tool splits any input into words by detecting case transitions, separators (<code>_ - . /</code>), and whitespace, then re-joins them in 14 different styles.</p>

<h3>When to use it</h3>
<ul>
  <li>Renaming a field from API JSON (camelCase) to a Python ORM column (snake_case).</li>
  <li>Generating CSS class names from design-system token names that arrive in PascalCase.</li>
  <li>Converting a list of headings into kebab-case slugs, or environment-variable names into CONSTANT_CASE.</li>
  <li>Quickly converting "The Quick Brown Fox" into Title Case, Sentence case, or Train-Case for a headline / button label.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Acronyms are tricky.</strong> Should "XMLHttpRequest" become "XML_Http_Request" or "Xml_Http_Request"? This tool treats consecutive capitals as one word boundary (<code>xml http request</code>), then re-cases — which matches Java/JS conventions but not all style guides.</li>
  <li><strong>Numbers attach to the previous word.</strong> "Item2" becomes one word "item2", not two. Add a separator if you want them split.</li>
  <li><strong>"camelCase first letter"</strong> is always lowercase even if the input started with a capital. PascalCase preserves the capital.</li>
  <li><strong>Round-tripping isn't always lossless.</strong> Going camelCase → kebab-case → camelCase loses the original capitalisation hint at word boundaries; the case-detection heuristic does its best but can't recover what wasn't preserved.</li>
</ul>
""",
    },
    "related": ["slug-generator", "word-counter", "text-diff"],
}
