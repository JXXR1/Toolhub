TOOL = {
    "slug": "slug-generator",
    "category": "text",
    "icon": "/-",
    "tags": ["slug", "url", "seo", "kebab", "permalink", "transliterate"],
    "i18n": {
        "en": {
            "name": "Slug Generator",
            "tagline": "Turn any title into a clean URL slug — transliterates accents, strips punctuation, joins with hyphens.",
            "description": "Free online URL slug generator. Lowercases, transliterates accented characters (à → a, ñ → n), strips punctuation, and joins words with a chosen separator. Stop-word removal optional.",
        },
        "de": {"name": "Slug-Generator", "tagline": "Wandle jeden Titel in einen sauberen URL-Slug um — transliteriert Akzente, entfernt Satzzeichen, verbindet mit Bindestrichen.", "description": "Kostenloser URL-Slug-Generator. Kleinbuchstaben, Transliteration von Akzentzeichen (à → a, ñ → n), Satzzeichen entfernen, Wörter mit Trennzeichen verbinden."},
        "es": {"name": "Generador de Slug", "tagline": "Convierte cualquier título en un slug URL limpio — translitera acentos, elimina puntuación, une con guiones.", "description": "Generador de slugs URL gratuito. Minúsculas, transliteración de acentos (à → a, ñ → n), eliminación de puntuación y unión de palabras con separador."},
        "fr": {"name": "Générateur de Slug", "tagline": "Transformez tout titre en slug URL propre — translittère les accents, supprime la ponctuation, joint avec tirets.", "description": "Générateur de slug URL gratuit. Minuscules, translittération des accents (à → a, ñ → n), suppression de la ponctuation et jonction des mots."},
        "it": {"name": "Generatore di Slug", "tagline": "Trasforma qualsiasi titolo in uno slug URL pulito — translittera accenti, rimuove punteggiatura, unisce con trattini.", "description": "Generatore di slug URL gratuito. Minuscole, traslitterazione di accenti (à → a, ñ → n), rimozione punteggiatura e unione parole con separatore."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="sg-input" oninput="sgRun()" placeholder="The Quick Brown Fox: A Café Story (1956)" spellcheck="false">The Quick Brown Fox: A Café Story (1956)</textarea>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Separator</label>
      <select id="sg-sep" onchange="sgRun()">
        <option value="-">- (hyphen, default)</option>
        <option value="_">_ (underscore)</option>
        <option value=".">. (dot)</option>
        <option value="">none</option>
      </select>
    </div>
    <div>
      <label>Case</label>
      <select id="sg-case" onchange="sgRun()">
        <option value="lower">lowercase</option>
        <option value="upper">UPPERCASE</option>
        <option value="preserve">preserve</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.5rem">
    <div>
      <label><input type="checkbox" id="sg-stop" onchange="sgRun()"> Strip English stop words</label>
    </div>
    <div>
      <label>Max length <input type="number" id="sg-max" value="80" min="1" max="500" oninput="sgRun()" style="width:80px;display:inline-block"></label>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="sg-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('sg-out', this)">{LBL_COPY}</button>
  </div>
  <div id="sg-meta" class="meta" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<script>
const SG_STOP = new Set(['a','an','and','the','of','to','in','on','at','for','by','with','from','is','are','was','were','be','been','as','it','this','that','these','those']);
function sgTransliterate(s){
  // NFD normalize then strip combining diacritics
  s = s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  // common European ligatures + special letters
  const map = {
    'ß':'ss','æ':'ae','Æ':'AE','œ':'oe','Œ':'OE',
    'ø':'o','Ø':'O','å':'a','Å':'A','ł':'l','Ł':'L',
    'ð':'d','Ð':'D','þ':'th','Þ':'Th',
    '€':'eur','£':'gbp','$':'usd','¥':'jpy','%':'pct','&':'and','@':'at','+':'plus','=':'eq'
  };
  return s.replace(/[ßæÆœŒøØåÅłŁðÐþÞ€£$¥%&@+=]/g, c => map[c] || c);
}
function sgRun(){
  const raw = document.getElementById('sg-input').value;
  const sep = document.getElementById('sg-sep').value;
  const cas = document.getElementById('sg-case').value;
  const strip = document.getElementById('sg-stop').checked;
  const maxLen = Math.max(1, parseInt(document.getElementById('sg-max').value) || 80);
  const out = document.getElementById('sg-out');
  const meta = document.getElementById('sg-meta');
  if(!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent=''; return; }
  let s = sgTransliterate(raw);
  // collapse anything not letter/digit to a space
  s = s.replace(/[^A-Za-z0-9]+/g, ' ').trim();
  let words = s.split(/\\s+/);
  if(strip) words = words.filter(w => !SG_STOP.has(w.toLowerCase()));
  if(words.length === 0) words = [s.replace(/\\s+/g,'')];
  if(cas === 'lower') words = words.map(w => w.toLowerCase());
  else if(cas === 'upper') words = words.map(w => w.toUpperCase());
  let slug = words.join(sep);
  if(slug.length > maxLen){
    slug = slug.slice(0, maxLen);
    if(sep) slug = slug.replace(new RegExp('\\\\' + sep + '+$'), '');
  }
  out.textContent = slug || '—';
  meta.textContent = `${slug.length} characters · ${words.length} words${strip?' (after stop-word removal)':''}`;
}
document.addEventListener('DOMContentLoaded', sgRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A URL slug is the human-readable last segment of a URL — <code>/blog/the-quick-brown-fox</code> rather than <code>/blog/post-4827</code>. Good slugs are lowercase, hyphenated, ASCII-only, and short enough to read at a glance, but generating them from real titles full of accents, punctuation, and emoji is fiddly to get right. This tool transliterates accents, strips junk, joins with your chosen separator, and truncates at a clean boundary so the output is safe to drop straight into a route or filename.</p>

<h3>When to use it</h3>
<ul>
  <li>Generating <code>/blog/&lt;slug&gt;</code> URLs from article titles — especially when titles contain accented characters (à, ñ, ø) or punctuation (colons, parentheses, em dashes).</li>
  <li>Producing safe filenames from user-supplied names — uploads, exports, generated reports.</li>
  <li>Building stable identifiers for tags, categories, or anchors (<code>#getting-started</code>) from human labels.</li>
  <li>Bulk-converting a list of headings to kebab-case for a static-site build step.</li>
</ul>

<h3>How the conversion works</h3>
<ol>
  <li>NFD-normalizes Unicode and strips combining diacritics (<code>café → cafe</code>).</li>
  <li>Maps common European ligatures and special letters: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, plus a few currency/math symbols (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Replaces every non-alphanumeric run with a single space.</li>
  <li>Optionally drops common English stop words (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Lowercases (or preserves case), joins with your separator, and truncates at the limit without leaving a dangling separator.</li>
</ol>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Non-Latin scripts get dropped.</strong> Diacritic stripping handles à/ñ/ø, but it can't romanize Chinese, Japanese, Cyrillic, Arabic, or Hebrew character-by-character — those need language-specific tables (Hanyu Pinyin, ICU transliteration) which are deliberately out of scope here. Such characters disappear after the strip step.</li>
  <li><strong>Stop-word removal is English-only.</strong> "El gato negro" doesn't lose <em>el</em>; "Le chat noir" doesn't lose <em>le</em>. Leave the toggle off for non-English titles.</li>
  <li><strong>Truncation can change meaning.</strong> "introduction-to-rust-programming" cut to 20 chars becomes "introduction-to-rust" — fine; cut to 16 becomes "introduction-to" — clearly worse. Set the limit by hand for content where the tail matters.</li>
  <li><strong>Slugs aren't unique.</strong> Two different titles can collapse to the same slug ("Café" and "Cafe" both → <code>cafe</code>). If you're using slugs as URL keys, append a short ID or a suffix on collision.</li>
  <li><strong>Don't change shipped slugs.</strong> Once a URL is live and indexed, regenerating its slug breaks links and SEO. If a title changes, keep the old slug or set up a 301 redirect.</li>
</ul>
""",
    },
    "related": ["case-converter", "url-encoder", "lorem-ipsum"],
}
