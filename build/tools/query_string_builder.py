TOOL = {
    "slug": "query-string-builder",
    "category": "developer",
    "icon": "?=",
    "tags": ["query string", "url", "params", "encode", "build", "key value"],
    "i18n": {
        "en": {
            "name": "Query String Builder",
            "tagline": "Add key/value rows; get a correctly URL-encoded query string out. Supports array (a[]=1) and bracket-less repeated keys.",
            "description": "Free online query string builder. Add rows of key/value pairs and get a properly percent-encoded ?a=1&b=hello%20world string out, with optional array bracket notation. Runs entirely in your browser.",
        },
        "de": {"name": "Query-String-Builder", "tagline": "Schlüssel/Wert-Zeilen hinzufügen; korrekt URL-codierten Query-String erhalten. Unterstützt Arrays (a[]=1) und wiederholte Schlüssel.", "description": "Kostenloser Query-String-Builder. Schlüssel/Wert-Paare als Zeilen hinzufügen und einen korrekt prozent-codierten ?a=1&b=hello%20world-String erhalten, optional mit Array-Klammer-Notation. Komplett im Browser."},
        "es": {"name": "Constructor de Query String", "tagline": "Añade filas clave/valor y obtén un query string correctamente codificado. Soporta arrays (a[]=1) y claves repetidas.", "description": "Constructor de query string gratuito. Añade pares clave/valor y obtén una cadena ?a=1&b=hello%20world correctamente percent-encoded, con notación opcional de corchetes para arrays. 100% en el navegador."},
        "fr": {"name": "Constructeur de Query String", "tagline": "Ajoutez des lignes clé/valeur ; obtenez un query string correctement encodé. Supporte les tableaux (a[]=1) et les clés répétées.", "description": "Constructeur de query string gratuit. Ajoutez des paires clé/valeur et obtenez une chaîne ?a=1&b=hello%20world correctement percent-encoded, avec notation crochets optionnelle. 100% dans le navigateur."},
        "it": {"name": "Costruttore Query String", "tagline": "Aggiungi righe chiave/valore; ottieni un query string correttamente URL-codificato. Supporta array (a[]=1) e chiavi ripetute.", "description": "Costruttore di query string gratuito. Aggiungi coppie chiave/valore e ottieni una stringa ?a=1&b=hello%20world correttamente percent-encoded, con notazione bracket opzionale per array. 100% nel browser."},
        "pt": {"name": "Construtor de Query String", "tagline": "Adicione linhas de chave/valor; obtenha um query string corretamente URL-encoded. Suporta arrays (a[]=1) e chaves repetidas.", "description": "Construtor de query string gratuito. Adicione pares chave/valor e obtenha uma string ?a=1&b=hello%20world corretamente percent-encoded, com notação opcional de colchetes para arrays. 100% no navegador."},
        "pl": {"name": "Builder Query Stringów", "tagline": "Dodawaj wiersze key/value; dostań poprawnie URL-encodowanego query stringa. Wspiera tablice (a[]=1) i powtarzane klucze.", "description": "Darmowy builder query stringów online. Dodawaj pary key/value i dostań poprawnie percent-encodowany ciąg ?a=1&b=hello%20world, z opcjonalną notacją tablic w nawiasach. Działa w całości w przeglądarce."},
    },
    "body": """
<div class="tool-card">
  <label>Base URL (optional)</label>
  <input type="text" id="qs-base" oninput="qsBuild()" placeholder="https://api.example.com/search" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
</div>
<div class="tool-card">
  <label>Parameters</label>
  <div id="qs-rows"></div>
  <div class="button-row">
    <button class="secondary" onclick="qsAdd()">+ Add row</button>
    <button class="secondary" onclick="qsClear()">Reset</button>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Array notation</label>
      <select id="qs-array" onchange="qsBuild()">
        <option value="brackets" selected>a[]=1&amp;a[]=2 (PHP / Rails)</option>
        <option value="repeat">a=1&amp;a=2 (repeat key)</option>
        <option value="comma">a=1,2 (comma-separated)</option>
      </select>
    </div>
    <div>
      <label>Space encoding</label>
      <select id="qs-space" onchange="qsBuild()">
        <option value="percent" selected>%20 (URI standard)</option>
        <option value="plus">+ (form data)</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>Query string</label>
  <div class="output-row">
    <pre class="output" id="qs-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('qs-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="qs-full" style="margin-top:0.5rem;font-family:ui-monospace,monospace;font-size:0.82rem"></div>
</div>
""",
    "script": """
<style>
.qs-row { display: grid; grid-template-columns: 1fr 1fr auto auto; gap: 0.5rem; margin-bottom: 0.5rem; align-items: center; }
.qs-row input { font-family: ui-monospace, monospace; font-size: 0.88rem; }
.qs-row button { padding: 0.4rem 0.6rem; font-size: 0.85rem; }
.qs-row label.qs-multi { display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.78rem; color: var(--text-muted); white-space: nowrap; cursor: pointer; }
@media (max-width: 600px){ .qs-row { grid-template-columns: 1fr 1fr; } .qs-row > :nth-child(3), .qs-row > :nth-child(4) { grid-column: span 1; } }
</style>
<script>
let QS_ROWS = [
  {key: 'q', val: 'hello world', multi: false},
  {key: 'lang', val: 'en', multi: false},
  {key: 'tags', val: 'fast,minimal', multi: true}
];

function qsRender(){
  const wrap = document.getElementById('qs-rows');
  wrap.innerHTML = '';
  QS_ROWS.forEach((row, i) => {
    const div = document.createElement('div');
    div.className = 'qs-row';
    div.innerHTML = `
      <input type="text" placeholder="key" value="">
      <input type="text" placeholder="value" value="">
      <label class="qs-multi"><input type="checkbox"> multi</label>
      <button class="secondary">×</button>
    `;
    const inputs = div.querySelectorAll('input');
    inputs[0].value = row.key;
    inputs[1].value = row.val;
    inputs[2].checked = !!row.multi;
    inputs[0].oninput = () => { QS_ROWS[i].key = inputs[0].value; qsBuild(); };
    inputs[1].oninput = () => { QS_ROWS[i].val = inputs[1].value; qsBuild(); };
    inputs[2].onchange = () => { QS_ROWS[i].multi = inputs[2].checked; qsBuild(); };
    div.querySelector('button').onclick = () => { QS_ROWS.splice(i, 1); qsRender(); qsBuild(); };
    wrap.appendChild(div);
  });
}

function qsAdd(){ QS_ROWS.push({key:'', val:'', multi:false}); qsRender(); qsBuild(); }
function qsClear(){ QS_ROWS = [{key:'', val:'', multi:false}]; qsRender(); qsBuild(); }

function qsEncode(s, spaceMode){
  let out = encodeURIComponent(s);
  if(spaceMode === 'plus') out = out.replace(/%20/g, '+');
  return out;
}

function qsBuild(){
  const arrayMode = document.getElementById('qs-array').value;
  const spaceMode = document.getElementById('qs-space').value;
  const parts = [];
  for(const row of QS_ROWS){
    if(!row.key) continue;
    if(row.multi){
      const values = row.val.split(',').map(s => s.trim()).filter(s => s !== '');
      if(values.length === 0){ parts.push(qsEncode(row.key, spaceMode) + '='); continue; }
      if(arrayMode === 'comma'){
        parts.push(qsEncode(row.key, spaceMode) + '=' + values.map(v => qsEncode(v, spaceMode)).join(','));
      } else if(arrayMode === 'brackets'){
        for(const v of values) parts.push(qsEncode(row.key, spaceMode) + '[]=' + qsEncode(v, spaceMode));
      } else {
        for(const v of values) parts.push(qsEncode(row.key, spaceMode) + '=' + qsEncode(v, spaceMode));
      }
    } else {
      parts.push(qsEncode(row.key, spaceMode) + '=' + qsEncode(row.val, spaceMode));
    }
  }
  const qs = parts.length ? '?' + parts.join('&') : '';
  const out = document.getElementById('qs-out');
  if(!qs){ out.textContent = '(no parameters)'; }
  else out.textContent = qs;
  const base = document.getElementById('qs-base').value.trim();
  document.getElementById('qs-full').textContent = base ? base + qs : '';
}

document.addEventListener('DOMContentLoaded', () => { qsRender(); qsBuild(); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A query string is just a list of key/value pairs glued together with <code>?</code>, <code>=</code>, and <code>&amp;</code>, but writing one by hand correctly is fiddly: spaces become <code>%20</code> (or <code>+</code>, depending), each value gets percent-encoded, and arrays have at least three competing conventions. This tool lets you type the keys and values you want, ticks "multi" for the ones you want repeated, and produces the correctly-encoded string ready to paste after <code>?</code>.</p>

<h3>When to use it</h3>
<ul>
  <li>Crafting an API URL with several parameters that include spaces, accents, or punctuation.</li>
  <li>Building a tracking link (UTM tags) without typos in the encoded values.</li>
  <li>Constructing a deep link or share URL that has to round-trip through email, chat, or social.</li>
  <li>Confirming the right array notation for an API — <code>a[]=1</code>, <code>a=1&amp;a=2</code>, or <code>a=1,2</code> — by trying each.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Array conventions are not standardised.</strong> PHP and Rails use <code>a[]=1&amp;a[]=2</code>; Python's <code>requests</code> defaults to repeating <code>a=1&amp;a=2</code>; ASP.NET often uses commas. Match what your API expects.</li>
  <li><strong><code>+</code> vs <code>%20</code>.</strong> <code>application/x-www-form-urlencoded</code> uses <code>+</code> for spaces; URI query strings strictly use <code>%20</code>. Most servers accept both, but some don't — pick the one your API documents.</li>
  <li><strong>Empty values are different from missing keys.</strong> <code>?a=</code> means "a is the empty string"; omitting <code>a</code> means "no value provided". Some APIs treat them differently.</li>
  <li><strong>Reserved-character interplay.</strong> <code>=</code>, <code>&amp;</code>, <code>#</code>, <code>?</code> inside values are encoded; literal versions in keys/values would terminate the parameter or whole query.</li>
  <li><strong>Order can matter.</strong> Some signed-URL schemes (S3, Stripe webhooks, OAuth 1.0) require parameters in a specific order before signing. The tool preserves your row order.</li>
  <li><strong>Length limits.</strong> Browsers and servers cap query-string length around 2–8 KB. Stuffing JSON into a query parameter is a smell.</li>
  <li><strong>Don't put secrets in the query string.</strong> They show up in server logs, browser history, and Referer headers. Use the request body or an Authorization header instead.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um query string é só uma lista de pares chave/valor colados com <code>?</code>, <code>=</code> e <code>&amp;</code>, mas escrever um corretamente à mão é chato: espaços viram <code>%20</code> (ou <code>+</code>, dependendo), cada valor é percent-encoded e arrays têm pelo menos três convenções concorrentes. Esta ferramenta deixa você digitar as chaves e valores que quer, marcar "multi" para os que devem ser repetidos e produz a string corretamente codificada, pronta para colar depois do <code>?</code>.</p>

<h3>Quando usar</h3>
<ul>
  <li>Montar uma URL de API com vários parâmetros que incluem espaços, acentos ou pontuação.</li>
  <li>Construir um link de tracking (UTM) sem erros de digitação nos valores codificados.</li>
  <li>Construir um deep link ou URL de compartilhamento que vai passar por e-mail, chat ou redes sociais.</li>
  <li>Confirmar a notação de array correta para uma API — <code>a[]=1</code>, <code>a=1&amp;a=2</code> ou <code>a=1,2</code> — testando cada uma.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Convenções de array não são padronizadas.</strong> PHP e Rails usam <code>a[]=1&amp;a[]=2</code>; o <code>requests</code> do Python por padrão repete <code>a=1&amp;a=2</code>; ASP.NET costuma usar vírgulas. Combine com o que sua API espera.</li>
  <li><strong><code>+</code> vs <code>%20</code>.</strong> <code>application/x-www-form-urlencoded</code> usa <code>+</code> para espaços; query strings de URI usam estritamente <code>%20</code>. A maioria dos servidores aceita os dois, mas alguns não — use o que sua API documenta.</li>
  <li><strong>Valores vazios são diferentes de chaves ausentes.</strong> <code>?a=</code> significa "a é a string vazia"; omitir <code>a</code> significa "nenhum valor fornecido". Algumas APIs tratam diferente.</li>
  <li><strong>Caracteres reservados.</strong> <code>=</code>, <code>&amp;</code>, <code>#</code>, <code>?</code> dentro de valores são codificados; versões literais em chaves/valores encerrariam o parâmetro ou a query inteira.</li>
  <li><strong>A ordem pode importar.</strong> Alguns esquemas de URL assinada (S3, webhooks Stripe, OAuth 1.0) exigem parâmetros em ordem específica antes da assinatura. A ferramenta preserva a ordem das suas linhas.</li>
  <li><strong>Limites de tamanho.</strong> Navegadores e servidores limitam o query string em torno de 2–8 KB. Enfiar JSON num parâmetro de query é sinal de problema.</li>
  <li><strong>Não coloque segredos no query string.</strong> Eles aparecem em logs do servidor, histórico do navegador e headers Referer. Use o body da requisição ou um header Authorization.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Ein Query-String ist eine Liste von Schlüssel/Wert-Paaren mit <code>?</code>, <code>=</code>, <code>&amp;</code> verbunden — von Hand fehleranfällig zu schreiben. Dieses Tool nimmt deine Eingaben und erzeugt den korrekt codierten String.</p>
<h3>Wann verwenden</h3>
<ul>
<li>API-URL mit mehreren Parametern.</li>
<li>Tracking-Link (UTM) tippfehlerfrei.</li>
<li>Deep Link / Share-URL für E-Mail/Chat.</li>
<li>Array-Notation der API ausprobieren.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Array-Konventionen sind nicht standardisiert.</strong> PHP/Rails: <code>a[]=1</code>; Python: <code>a=1&amp;a=2</code>; ASP.NET: Komma.</li>
<li><strong><code>+</code> vs <code>%20</code>.</strong> Form-Encoding vs URI.</li>
<li><strong>Leer ≠ fehlend.</strong> <code>?a=</code> ≠ kein <code>a</code>.</li>
<li><strong>Reservierte Zeichen.</strong> <code>=&amp;#?</code> in Werten müssen codiert werden.</li>
<li><strong>Reihenfolge kann zählen</strong> (signierte URLs).</li>
<li><strong>Längenlimit.</strong> Browser/Server bei 2–8 KB.</li>
<li><strong>Keine Geheimnisse</strong> — landen in Logs/History/Referer.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Un query string es una lista de pares clave/valor con <code>?</code>, <code>=</code>, <code>&amp;</code> — escribirlo a mano es propenso a errores. Esta herramienta toma tus entradas y produce la cadena correctamente codificada.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>URL de API con múltiples parámetros.</li>
<li>Enlace de tracking (UTM) sin erratas.</li>
<li>Deep link / share-URL para email/chat.</li>
<li>Probar la notación de arrays que espera tu API.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Convenciones de arrays no estandarizadas.</strong> PHP/Rails: <code>a[]=1</code>; Python: <code>a=1&amp;a=2</code>; ASP.NET: comas.</li>
<li><strong><code>+</code> vs <code>%20</code>.</strong> Form-encoded vs URI.</li>
<li><strong>Vacío ≠ ausente.</strong> <code>?a=</code> ≠ sin <code>a</code>.</li>
<li><strong>Caracteres reservados.</strong> <code>=&amp;#?</code> en valores deben codificarse.</li>
<li><strong>El orden puede importar</strong> (URLs firmadas).</li>
<li><strong>Límite de longitud.</strong> 2–8 KB típicamente.</li>
<li><strong>Sin secretos</strong> — acaban en logs/historial/Referer.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Un query string est une liste de paires clé/valeur reliées par <code>?</code>, <code>=</code>, <code>&amp;</code> — fastidieux à écrire à la main. Cet outil prend vos entrées et produit la chaîne correctement encodée.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>URL d'API avec plusieurs paramètres.</li>
<li>Lien de tracking (UTM) sans coquilles.</li>
<li>Deep link / URL de partage pour email/chat.</li>
<li>Essayer la notation tableau attendue par l'API.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Conventions tableaux non standardisées.</strong> PHP/Rails : <code>a[]=1</code> ; Python : <code>a=1&amp;a=2</code> ; ASP.NET : virgules.</li>
<li><strong><code>+</code> vs <code>%20</code>.</strong> Form-encoded vs URI.</li>
<li><strong>Vide ≠ absent.</strong> <code>?a=</code> ≠ pas de <code>a</code>.</li>
<li><strong>Caractères réservés.</strong> <code>=&amp;#?</code> dans les valeurs doivent être encodés.</li>
<li><strong>L'ordre peut compter</strong> (URLs signées).</li>
<li><strong>Limite de longueur.</strong> 2–8 KB typiquement.</li>
<li><strong>Pas de secrets</strong> — finissent dans les logs/historique/Referer.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Un query string è una lista di coppie chiave/valore unite con <code>?</code>, <code>=</code>, <code>&amp;</code> — scriverlo a mano è soggetto a errori. Questo strumento prende le tue voci e produce la stringa correttamente codificata.</p>
<h3>Quando usarlo</h3>
<ul>
<li>URL API con più parametri.</li>
<li>Link di tracking (UTM) senza refusi.</li>
<li>Deep link / share-URL per email/chat.</li>
<li>Provare la notazione array che si aspetta l'API.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Convenzioni array non standardizzate.</strong> PHP/Rails: <code>a[]=1</code>; Python: <code>a=1&amp;a=2</code>; ASP.NET: virgole.</li>
<li><strong><code>+</code> vs <code>%20</code>.</strong> Form-encoded vs URI.</li>
<li><strong>Vuoto ≠ assente.</strong> <code>?a=</code> ≠ niente <code>a</code>.</li>
<li><strong>Caratteri riservati.</strong> <code>=&amp;#?</code> nei valori vanno codificati.</li>
<li><strong>L'ordine può contare</strong> (URL firmati).</li>
<li><strong>Limite lunghezza.</strong> 2–8 KB tipicamente.</li>
<li><strong>Niente segreti</strong> — finiscono in log/cronologia/Referer.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Query string to zwykła lista par key/value sklejona <code>?</code>, <code>=</code> i <code>&amp;</code>, ale napisanie go ręcznie poprawnie jest upierdliwe: spacje stają się <code>%20</code> (albo <code>+</code>, zależnie), każda wartość jest percent-encodowana, a tablice mają co najmniej trzy konkurujące konwencje. To narzędzie pozwala wpisać klucze i wartości, których chcesz, zaznaczyć "multi" tym, które mają się powtarzać, i produkuje poprawnie zakodowany string gotowy do wklejenia po <code>?</code>.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Tworzenie URL-a API z kilkoma parametrami zawierającymi spacje, znaki diakrytyczne albo interpunkcję.</li>
  <li>Budowa linka trackingowego (tagi UTM) bez literówek w zakodowanych wartościach.</li>
  <li>Konstrukcja deep linka albo share URL-a, który ma round-trip przez maila, czat albo social.</li>
  <li>Potwierdzenie właściwej notacji tablic dla API — <code>a[]=1</code>, <code>a=1&amp;a=2</code> albo <code>a=1,2</code> — przez wypróbowanie każdej.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Konwencje tablic nie są ustandaryzowane.</strong> PHP i Rails używają <code>a[]=1&amp;a[]=2</code>; pythonowy <code>requests</code> domyślnie powtarza <code>a=1&amp;a=2</code>; ASP.NET często używa przecinków. Dopasuj do tego, czego oczekuje twoje API.</li>
  <li><strong><code>+</code> vs <code>%20</code>.</strong> <code>application/x-www-form-urlencoded</code> używa <code>+</code> dla spacji; query stringi URI ściśle używają <code>%20</code>. Większość serwerów akceptuje oba, ale niektóre nie — wybierz to, co dokumentuje twoje API.</li>
  <li><strong>Pusta wartość różni się od brakującego klucza.</strong> <code>?a=</code> znaczy "a to pusty string"; pominięcie <code>a</code> znaczy "wartość nie podana". Niektóre API traktują to inaczej.</li>
  <li><strong>Interakcja zarezerwowanych znaków.</strong> <code>=</code>, <code>&amp;</code>, <code>#</code>, <code>?</code> wewnątrz wartości są kodowane; literałne wersje w kluczach/wartościach zakończyłyby parametr albo całą query.</li>
  <li><strong>Kolejność może mieć znaczenie.</strong> Niektóre schematy podpisanych URL-i (S3, webhooki Stripe, OAuth 1.0) wymagają parametrów w konkretnej kolejności przed podpisem. Narzędzie zachowuje kolejność twoich wierszy.</li>
  <li><strong>Limity długości.</strong> Przeglądarki i serwery ograniczają długość query stringa w okolicach 2–8 KB. Wciskanie JSON-a w parametr query to smell.</li>
  <li><strong>Nie wstawiaj sekretów do query stringa.</strong> Wpadną w logi serwera, historię przeglądarki i nagłówki Referer. Używaj body requesta albo nagłówka Authorization.</li>
</ul>
""",
    },
    "related": ["url-parser", "url-encoder", "json-formatter", "jwt-decoder"],
}
