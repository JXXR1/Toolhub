TOOL = {
    "slug": "url-encoder",
    "category": "encoding",
    "icon": "🔗",
    "tags": ["url", "encode", "decode", "percent", "querystring"],
    "i18n": {
        "en": {
            "name": "URL Encoder / Decoder",
            "tagline": "Percent-encode strings for URLs or decode percent-encoded ones back to plain text.",
            "description": "Free online URL encoder and decoder. Encodes special characters as percent-escapes for URLs, query strings, and form data. Component-safe.",
        },
        "de": {"name": "URL Encoder / Decoder", "tagline": "Strings für URLs prozent-codieren oder zurück in Klartext decodieren.", "description": "Kostenloser URL Encoder und Decoder. Sonderzeichen für URLs, Query-Strings und Formulardaten escapen."},
        "es": {"name": "Codificador / Decodificador URL", "tagline": "Codifica cadenas para URLs (porcentaje) o decodifica de vuelta a texto plano.", "description": "Codificador y decodificador URL gratuito. Escapa caracteres especiales para URLs, query strings y datos de formulario."},
        "fr": {"name": "Encodeur / Décodeur URL", "tagline": "Encodez en pourcentage pour URLs ou décodez vers texte brut.", "description": "Encodeur et décodeur URL gratuit. Échappe les caractères spéciaux pour URLs, query strings et formulaires."},
        "it": {"name": "Encoder / Decoder URL", "tagline": "Codifica stringhe per URL (percent-encoding) o decodifica in testo semplice.", "description": "Encoder e decoder URL gratuito. Escape di caratteri speciali per URL, query string e dati form."},
        "pt": {"name": "Encoder / Decoder de URL", "tagline": "Faça percent-encoding de strings para URLs ou decodifique de volta para texto puro.", "description": "Encoder e decoder de URL online gratuito. Codifica caracteres especiais como percent-escapes para URLs, query strings e dados de formulário. Component-safe."},
        "pl": {"name": "Encoder / Decoder URL", "tagline": "Percent-encoduj stringi pod URL-e albo dekoduj zakodowane procentowo z powrotem na zwykły tekst.", "description": "Darmowy online encoder i decoder URL. Koduje znaki specjalne jako percent-escape pod URL-e, query stringi i form data. Component-safe."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="url-mode" onchange="urlRun()">
        <option value="enc">{LBL_ENCODE}</option>
        <option value="dec">{LBL_DECODE}</option>
      </select>
    </div>
    <div>
      <label>Scope</label>
      <select id="url-scope" onchange="urlRun()">
        <option value="component">Component (encodes /, ?, #, &amp;)</option>
        <option value="uri">Full URI (preserves /, ?, #, &amp;)</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="url-in" oninput="urlRun()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="url-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('url-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function urlRun(){
  const mode = document.getElementById('url-mode').value;
  const scope = document.getElementById('url-scope').value;
  const raw = document.getElementById('url-in').value;
  const out = document.getElementById('url-out');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    let res;
    if (mode === 'enc') res = scope === 'component' ? encodeURIComponent(raw) : encodeURI(raw);
    else                res = scope === 'component' ? decodeURIComponent(raw) : decodeURI(raw);
    out.textContent = res;
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; }
}
document.addEventListener('DOMContentLoaded', urlRun);
</script>
""",
    "help": {
        "en": """
<h2>What URL encoding does</h2>
<p>URLs and HTTP headers are restricted to a small ASCII subset. Anything outside that set — including spaces, accented letters, emoji, and several reserved punctuation characters — has to be <em>percent-encoded</em>: replaced by <code>%</code> followed by two hex digits per byte. <code>café</code> becomes <code>caf%C3%A9</code> (UTF-8). Decoding reverses that.</p>

<h3>When to use which scope</h3>
<ul>
  <li><strong>Component</strong> — pick this for individual <em>values</em> you'll splice into a URL: query-string values, path segments, fragment text, header values. Encodes the structural characters <code>/ ? # &amp; = +</code> so they don't accidentally end up parsed as URL syntax.</li>
  <li><strong>Full URI</strong> — pick this for a whole URL you want to clean up. Preserves <code>/ ? # &amp; = +</code> as URL structure, only encodes <em>illegal</em> characters (spaces, non-ASCII, etc.).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't double-encode.</strong> Encoding an already-encoded string turns <code>%20</code> into <code>%2520</code>. If your input shows <code>%XX</code> sequences, decode first.</li>
  <li><strong>Spaces aren't always <code>%20</code>.</strong> In <em>application/x-www-form-urlencoded</em> bodies, spaces are <code>+</code>. This tool follows the JavaScript <code>encodeURIComponent</code> convention (always <code>%20</code>); decode handles both.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Modern browsers and <code>encodeURIComponent</code> always use UTF-8. Some older systems still produce Latin-1 percent-escapes — those won't round-trip cleanly here.</li>
  <li><strong>Reserved characters are case-insensitive in the percent-escape but case-sensitive in the decoded result</strong> — <code>%2F</code> and <code>%2f</code> both decode to <code>/</code>, but the original character's case is preserved.</li>
</ul>
""",
        "pt": """
<h2>O que o URL encoding faz</h2>
<p>URLs e headers HTTP são restritos a um pequeno subconjunto do ASCII. Qualquer coisa fora desse conjunto — incluindo espaços, letras acentuadas, emoji e vários caracteres de pontuação reservados — precisa ser <em>percent-encoded</em>: substituída por <code>%</code> seguido de dois dígitos hex por byte. <code>café</code> vira <code>caf%C3%A9</code> (UTF-8). A decodificação reverte isso.</p>

<h3>Quando usar cada scope</h3>
<ul>
  <li><strong>Component</strong> — escolha esta opção para <em>valores</em> individuais que você vai inserir em uma URL: valores de query string, segmentos de path, texto de fragment, valores de header. Codifica os caracteres estruturais <code>/ ? # &amp; = +</code> para que não sejam interpretados acidentalmente como sintaxe de URL.</li>
  <li><strong>Full URI</strong> — escolha esta para uma URL inteira que você quer limpar. Preserva <code>/ ? # &amp; = +</code> como estrutura da URL, codificando apenas caracteres <em>ilegais</em> (espaços, não-ASCII, etc.).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não codifique duas vezes.</strong> Codificar uma string já codificada transforma <code>%20</code> em <code>%2520</code>. Se sua entrada já tem sequências <code>%XX</code>, decodifique primeiro.</li>
  <li><strong>Espaços nem sempre são <code>%20</code>.</strong> Em corpos <em>application/x-www-form-urlencoded</em>, espaços são <code>+</code>. Esta ferramenta segue a convenção do <code>encodeURIComponent</code> do JavaScript (sempre <code>%20</code>); a decodificação aceita os dois.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Browsers modernos e <code>encodeURIComponent</code> sempre usam UTF-8. Alguns sistemas antigos ainda produzem percent-escapes em Latin-1 — esses não fazem round-trip corretamente aqui.</li>
  <li><strong>Caracteres reservados são case-insensitive no percent-escape mas case-sensitive no resultado decodificado</strong> — <code>%2F</code> e <code>%2f</code> ambos decodificam para <code>/</code>, mas o case original do caractere é preservado.</li>
</ul>
""",
        "pl": """
<h2>Co robi URL encoding</h2>
<p>URL-e i nagłówki HTTP są ograniczone do małego podzbioru ASCII. Wszystko poza nim — w tym spacje, litery z diakrytykami, emoji i kilka zarezerwowanych znaków interpunkcyjnych — musi być <em>percent-encoded</em>: zastąpione <code>%</code> i dwiema cyframi hex na bajt. <code>café</code> staje się <code>caf%C3%A9</code> (UTF-8). Dekodowanie odwraca to.</p>

<h3>Kiedy którego scope użyć</h3>
<ul>
  <li><strong>Component</strong> — wybierz to dla pojedynczych <em>wartości</em>, które wkleisz do URL-a: wartości query stringa, segmenty path, tekst fragmentu, wartości nagłówków. Koduje znaki strukturalne <code>/ ? # &amp; = +</code>, żeby nie zostały przypadkowo sparsowane jako składnia URL-a.</li>
  <li><strong>Full URI</strong> — wybierz to dla całego URL-a, który chcesz uporządkować. Zachowuje <code>/ ? # &amp; = +</code> jako strukturę URL-a, koduje tylko znaki <em>nielegalne</em> (spacje, non-ASCII itd.).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie koduj podwójnie.</strong> Zakodowanie już zakodowanego stringa zamienia <code>%20</code> w <code>%2520</code>. Jeśli wejście pokazuje sekwencje <code>%XX</code>, najpierw zdekoduj.</li>
  <li><strong>Spacje nie zawsze to <code>%20</code>.</strong> W ciałach <em>application/x-www-form-urlencoded</em> spacje to <code>+</code>. To narzędzie idzie za konwencją JS-owego <code>encodeURIComponent</code> (zawsze <code>%20</code>); dekodowanie obsługuje obie.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Nowoczesne przeglądarki i <code>encodeURIComponent</code> zawsze używają UTF-8. Niektóre starsze systemy nadal produkują percent-escape w Latin-1 — te nie zrobią tu czystego round-tripu.</li>
  <li><strong>Znaki zarezerwowane są case-insensitive w percent-escape, ale case-sensitive w zdekodowanym wyniku</strong> — <code>%2F</code> i <code>%2f</code> oba dekodują do <code>/</code>, ale oryginalna wielkość znaku jest zachowana.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "html-encoder", "qr-code-generator"],
}
