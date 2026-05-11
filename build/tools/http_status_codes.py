TOOL = {
    "slug": "http-status-codes",
    "category": "developer",
    "icon": "🌐",
    "tags": ["http", "status", "code", "rest", "api", "response", "rfc"],
    "i18n": {
        "en": {
            "name": "HTTP Status Codes",
            "tagline": "Look up any HTTP status code (1xx–5xx). Meaning, common causes, and the RFC reference.",
            "description": "Free HTTP status code reference. Search every standard HTTP status code (100–599), see its meaning, common causes, and the RFC where it's defined. Filter as you type.",
        },
        "de": {"name": "HTTP-Statuscodes", "tagline": "Schlage jeden HTTP-Statuscode nach (1xx–5xx). Bedeutung, häufige Ursachen und RFC-Referenz.", "description": "Kostenlose Referenz für HTTP-Statuscodes. Durchsuche jeden Standard-HTTP-Statuscode (100–599) mit Bedeutung, häufigen Ursachen und der zugehörigen RFC. Filter beim Tippen."},
        "es": {"name": "Códigos de Estado HTTP", "tagline": "Consulta cualquier código de estado HTTP (1xx–5xx). Significado, causas habituales y RFC.", "description": "Referencia gratuita de códigos HTTP. Busca cualquier código estándar (100–599) con su significado, causas habituales y RFC. Filtra al escribir."},
        "fr": {"name": "Codes HTTP", "tagline": "Recherchez n'importe quel code HTTP (1xx–5xx). Signification, causes courantes et référence RFC.", "description": "Référence gratuite des codes HTTP. Recherchez tout code standard (100–599) avec sa signification, ses causes courantes et la RFC. Filtrage en direct."},
        "it": {"name": "Codici di Stato HTTP", "tagline": "Cerca qualsiasi codice HTTP (1xx–5xx). Significato, cause comuni e riferimento RFC.", "description": "Riferimento gratuito per i codici HTTP. Cerca qualsiasi codice standard (100–599) con significato, cause comuni e RFC. Filtra mentre digiti."},
        "pt": {"name": "Códigos de Status HTTP", "tagline": "Consulte qualquer código de status HTTP (1xx–5xx). Significado, causas comuns e a referência da RFC.", "description": "Referência grátis de códigos de status HTTP. Pesquise qualquer código padrão (100–599), veja seu significado, causas comuns e a RFC onde está definido. Filtra enquanto você digita."},
        "pl": {"name": "Kody Statusu HTTP", "tagline": "Sprawdź dowolny kod statusu HTTP (1xx–5xx). Znaczenie, typowe przyczyny i odwołanie do RFC.", "description": "Darmowa referencja kodów statusu HTTP. Wyszukaj dowolny standardowy kod (100–599), zobacz jego znaczenie, typowe przyczyny i RFC, w którym jest zdefiniowany. Filtruj podczas pisania."},
        "ja": {"name": "HTTP ステータスコード", "tagline": "任意の HTTP ステータスコード（1xx–5xx）を検索。意味、よくある原因、RFC 参照を表示。", "description": "無料の HTTP ステータスコードリファレンス。標準のすべての HTTP ステータスコード（100–599）を検索し、意味・よくある原因・定義元の RFC を確認できます。入力に応じてリアルタイムフィルタ。"},
        "nl": {"name": "HTTP-statuscodes", "tagline": "Zoek elke HTTP-statuscode op (1xx–5xx). Betekenis, veelvoorkomende oorzaken en de RFC-referentie.", "description": "Gratis HTTP-statuscode-referentie. Zoek elke standaard HTTP-statuscode (100–599), zie de betekenis, veelvoorkomende oorzaken en de RFC waarin hij is gedefinieerd. Filter tijdens het typen."},
    },
    "body": """
<div class="tool-card">
  <label>Filter</label>
  <input type="text" id="hs-q" oninput="hsRun()" placeholder="Type a code or phrase — '404', 'auth', 'redirect', 'gateway'…" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">
    <button class="filter-btn" data-cls="all" onclick="hsCls('all')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--accent);color:#fff;border-radius:14px;cursor:pointer;font-size:0.8rem">{LBL_ALL}</button>
    <button class="filter-btn" data-cls="1" onclick="hsCls('1')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);border-radius:14px;cursor:pointer;font-size:0.8rem">1xx Info</button>
    <button class="filter-btn" data-cls="2" onclick="hsCls('2')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);border-radius:14px;cursor:pointer;font-size:0.8rem">2xx Success</button>
    <button class="filter-btn" data-cls="3" onclick="hsCls('3')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);border-radius:14px;cursor:pointer;font-size:0.8rem">3xx Redirect</button>
    <button class="filter-btn" data-cls="4" onclick="hsCls('4')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);border-radius:14px;cursor:pointer;font-size:0.8rem">4xx Client</button>
    <button class="filter-btn" data-cls="5" onclick="hsCls('5')" style="padding:0.3rem 0.7rem;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);border-radius:14px;cursor:pointer;font-size:0.8rem">5xx Server</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="hs-out"></div>
</div>
""",
    "script": """
<style>
.hs-list{display:grid;gap:0.5rem}
.hs-row{display:grid;grid-template-columns:auto 1fr;gap:0.7rem;padding:0.7rem 0.85rem;border:1px solid var(--border);background:var(--bg-elev);border-radius:8px;align-items:start}
.hs-code{font-family:ui-monospace,monospace;font-weight:700;font-size:1.05rem;padding:0.2rem 0.5rem;border-radius:5px;min-width:3.4rem;text-align:center}
.hs-1{background:rgba(139,148,158,0.15);color:var(--text-muted);border:1px solid rgba(139,148,158,0.3)}
.hs-2{background:rgba(63,185,80,0.15);color:#3fb950;border:1px solid rgba(63,185,80,0.4)}
.hs-3{background:rgba(88,166,255,0.15);color:#58a6ff;border:1px solid rgba(88,166,255,0.4)}
.hs-4{background:rgba(247,147,30,0.15);color:#f7931e;border:1px solid rgba(247,147,30,0.4)}
.hs-5{background:rgba(248,81,73,0.15);color:#f85149;border:1px solid rgba(248,81,73,0.4)}
.hs-name{font-weight:600;color:var(--text)}
.hs-desc{color:var(--text-muted);font-size:0.85rem;margin-top:0.2rem}
.hs-rfc{color:var(--text-muted);font-size:0.75rem;margin-top:0.2rem;font-family:ui-monospace,monospace}
.hs-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0}
</style>
<script>
const HTTP_CODES = [
  [100,'Continue','Server got the request headers and the client should send the body. Used with Expect: 100-continue.','RFC 9110 §15.2.1'],
  [101,'Switching Protocols','Server is switching protocols (e.g. to WebSocket) per the Upgrade header.','RFC 9110 §15.2.2'],
  [102,'Processing','Server has accepted the request but processing is not yet complete (WebDAV).','RFC 2518'],
  [103,'Early Hints','Hints (typically Link headers for preload) before the final response.','RFC 8297'],
  [200,'OK','Standard success. Body contains the requested resource.','RFC 9110 §15.3.1'],
  [201,'Created','Resource created. Should include a Location header pointing at the new resource.','RFC 9110 §15.3.2'],
  [202,'Accepted','Request accepted for asynchronous processing — outcome not yet known.','RFC 9110 §15.3.3'],
  [203,'Non-Authoritative Information','Body is from a transforming proxy, not the origin.','RFC 9110 §15.3.4'],
  [204,'No Content','Success with no body. Common for DELETE and idempotent PUT.','RFC 9110 §15.3.5'],
  [205,'Reset Content','Success — client should reset the document view (e.g. clear a form).','RFC 9110 §15.3.6'],
  [206,'Partial Content','Successful range request — body contains only the requested bytes.','RFC 9110 §15.3.7'],
  [207,'Multi-Status','XML body containing multiple status codes (WebDAV).','RFC 4918'],
  [208,'Already Reported','Members of a binding already enumerated (WebDAV).','RFC 5842'],
  [226,'IM Used','Server has fulfilled the request via instance manipulations.','RFC 3229'],
  [300,'Multiple Choices','Multiple representations available. Rare in practice.','RFC 9110 §15.4.1'],
  [301,'Moved Permanently','Resource has moved. Cache the redirect; future requests should use Location.','RFC 9110 §15.4.2'],
  [302,'Found','Temporary redirect. Historically ambiguous about method preservation — prefer 307 or 303.','RFC 9110 §15.4.3'],
  [303,'See Other','Redirect to a different resource (often after a POST). Always GET the new URL.','RFC 9110 §15.4.4'],
  [304,'Not Modified','Cached copy is still fresh — sent in response to conditional GET (If-None-Match / If-Modified-Since).','RFC 9110 §15.4.5'],
  [305,'Use Proxy','Deprecated. Was used to indicate a required proxy.','RFC 9110 (deprecated)'],
  [307,'Temporary Redirect','Like 302 but explicitly preserves the request method.','RFC 9110 §15.4.8'],
  [308,'Permanent Redirect','Like 301 but explicitly preserves the request method.','RFC 9110 §15.4.9'],
  [400,'Bad Request','Server cannot process due to malformed syntax (bad JSON, missing required field, oversized header).','RFC 9110 §15.5.1'],
  [401,'Unauthorized','Authentication required or failed. Despite the name, it means "unauthenticated".','RFC 9110 §15.5.2'],
  [402,'Payment Required','Reserved. Some APIs (Stripe, GitHub) use it for billing-related rejections.','RFC 9110 §15.5.3'],
  [403,'Forbidden','Authenticated but not allowed to access this resource. No login prompt should follow.','RFC 9110 §15.5.4'],
  [404,'Not Found','Resource does not exist. Don\\'t use to hide 403 unless you want stealth.','RFC 9110 §15.5.5'],
  [405,'Method Not Allowed','Endpoint exists but the HTTP method is not supported. Must return Allow header.','RFC 9110 §15.5.6'],
  [406,'Not Acceptable','Cannot produce a representation matching the Accept header.','RFC 9110 §15.5.7'],
  [407,'Proxy Authentication Required','Like 401 but for an intermediate proxy.','RFC 9110 §15.5.8'],
  [408,'Request Timeout','Client took too long sending the request. Usually retriable.','RFC 9110 §15.5.9'],
  [409,'Conflict','Request conflicts with current resource state (e.g. edit collision, duplicate username).','RFC 9110 §15.5.10'],
  [410,'Gone','Resource was here but is permanently removed. Stronger signal than 404.','RFC 9110 §15.5.11'],
  [411,'Length Required','Server refuses request without a Content-Length header.','RFC 9110 §15.5.12'],
  [412,'Precondition Failed','Conditional request (If-Match, If-Unmodified-Since) was not met.','RFC 9110 §15.5.13'],
  [413,'Content Too Large','Request body too big for server to process (was "Payload Too Large").','RFC 9110 §15.5.14'],
  [414,'URI Too Long','URL exceeds server limits — usually too many query params.','RFC 9110 §15.5.15'],
  [415,'Unsupported Media Type','Request body is in a format the endpoint cannot accept (wrong Content-Type).','RFC 9110 §15.5.16'],
  [416,'Range Not Satisfiable','Range header asked for bytes outside the resource length.','RFC 9110 §15.5.17'],
  [417,'Expectation Failed','Expect request-header could not be met by the server.','RFC 9110 §15.5.18'],
  [418,"I'm a teapot",'April Fools joke (RFC 2324). Some APIs use it for "deliberately refused".','RFC 2324'],
  [421,'Misdirected Request','Request sent to a server that cannot produce a response for it (e.g. wrong virtual host).','RFC 9110 §15.5.20'],
  [422,'Unprocessable Content','Syntactically valid but semantically wrong (validation failure on a JSON body).','RFC 9110 §15.5.21'],
  [423,'Locked','Resource is locked (WebDAV).','RFC 4918'],
  [424,'Failed Dependency','A previous request failed; this one depended on it (WebDAV).','RFC 4918'],
  [425,'Too Early','Server unwilling to risk processing a request that might be replayed.','RFC 8470'],
  [426,'Upgrade Required','Client must upgrade to a different protocol (e.g. TLS).','RFC 9110 §15.5.22'],
  [428,'Precondition Required','Server requires the request to be conditional (If-Match etc) to prevent lost updates.','RFC 6585'],
  [429,'Too Many Requests','Rate-limited. Should include Retry-After.','RFC 6585'],
  [431,'Request Header Fields Too Large','Headers (often a single one) exceed server limits.','RFC 6585'],
  [451,'Unavailable For Legal Reasons','Resource removed for legal reasons (court order, government censorship).','RFC 7725'],
  [500,'Internal Server Error','Generic server fault — usually a bug or unhandled exception.','RFC 9110 §15.6.1'],
  [501,'Not Implemented','Server does not support the functionality required.','RFC 9110 §15.6.2'],
  [502,'Bad Gateway','Upstream server returned an invalid response. Common at reverse proxies / load balancers.','RFC 9110 §15.6.3'],
  [503,'Service Unavailable','Server is overloaded or down for maintenance. Should include Retry-After.','RFC 9110 §15.6.4'],
  [504,'Gateway Timeout','Upstream server did not respond in time. Common at reverse proxies / load balancers.','RFC 9110 §15.6.5'],
  [505,'HTTP Version Not Supported','Client used an HTTP version the server refuses.','RFC 9110 §15.6.6'],
  [506,'Variant Also Negotiates','Content negotiation loop / misconfiguration.','RFC 2295'],
  [507,'Insufficient Storage','Server cannot store the representation (WebDAV — disk full).','RFC 4918'],
  [508,'Loop Detected','Infinite loop encountered during processing (WebDAV).','RFC 5842'],
  [510,'Not Extended','Further extensions to the request are required.','RFC 2774'],
  [511,'Network Authentication Required','Captive portal — user must authenticate to gain network access.','RFC 6585']
];
let HS_CLS = 'all';
function hsCls(c){
  HS_CLS = c;
  document.querySelectorAll('.filter-btn').forEach(b => {
    if(b.dataset.cls === c){ b.style.background='var(--accent)'; b.style.color='#fff'; }
    else { b.style.background='var(--surface)'; b.style.color='var(--text-muted)'; }
  });
  hsRun();
}
function hsRun(){
  const q = (document.getElementById('hs-q').value || '').toLowerCase().trim();
  const out = document.getElementById('hs-out');
  const matches = HTTP_CODES.filter(([code, name, desc, rfc]) => {
    const cls = String(Math.floor(code/100));
    if(HS_CLS !== 'all' && cls !== HS_CLS) return false;
    if(!q) return true;
    return String(code).includes(q) || name.toLowerCase().includes(q) || desc.toLowerCase().includes(q) || rfc.toLowerCase().includes(q);
  });
  if(matches.length === 0){ out.innerHTML = '<div class="hs-empty">No matching status codes.</div>'; return; }
  const rows = matches.map(([code, name, desc, rfc]) => {
    const cls = Math.floor(code/100);
    return `<div class="hs-row"><div class="hs-code hs-${cls}">${code}</div><div><div class="hs-name">${name}</div><div class="hs-desc">${desc}</div><div class="hs-rfc">${rfc}</div></div></div>`;
  }).join('');
  out.innerHTML = `<div class="hs-list">${rows}</div>`;
}
document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(hsRun));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>HTTP status codes are the three-digit numbers a server sends back to tell the client how the request went. They group into five families: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), 5xx (server error). Most developers know the headline codes — 200, 301, 404, 500 — but the long tail (409 Conflict, 422 Unprocessable, 504 Gateway Timeout) is where the real bugs live. This tool gives you the full list with meanings and the RFC where each is defined.</p>

<h3>When to use it</h3>
<ul>
  <li>Reading an API doc that returns a code you don't recognise (425? 451?).</li>
  <li>Picking the right code to return from your own API — 404 vs 410, 401 vs 403, 422 vs 400.</li>
  <li>Diagnosing a 502/504 — is the upstream down or just slow?</li>
  <li>Settling whether 200-with-an-error-body or a real 4xx is the right move.</li>
  <li>Looking up the RFC reference for a code review or design doc.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>401 means unauthenticated, 403 means unauthorized.</strong> The names are misleading — 401 says "I don't know who you are", 403 says "I know who you are and you can't have it". Use 403 only if a re-authentication wouldn't help.</li>
  <li><strong>302 is method-ambiguous.</strong> Browsers historically changed POST→GET on a 302 redirect. Use 307 (preserves method) or 303 (always GET) to be explicit.</li>
  <li><strong>404 is not 410.</strong> 404 = "I don't know"; 410 = "I know and it's gone forever". Use 410 when search engines should drop the URL.</li>
  <li><strong>200 with an error body is not "RESTful".</strong> If the request failed at the resource level, return a 4xx with the error in the body.</li>
  <li><strong>418 is a joke.</strong> Don't use I'm-a-teapot in production — clients and proxies treat it inconsistently.</li>
  <li><strong>RFC 9110 supersedes RFC 7231/7232/7233/7234/7235.</strong> If you're citing the spec, use 9110 (June 2022) unless you specifically need an older version.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Códigos de status HTTP são os números de três dígitos que um servidor devolve pra dizer ao cliente como a request foi. Eles se agrupam em cinco famílias: 1xx (informacional), 2xx (sucesso), 3xx (redirecionamento), 4xx (erro do cliente), 5xx (erro do servidor). A maioria dos devs conhece os códigos famosos — 200, 301, 404, 500 — mas é na cauda longa (409 Conflict, 422 Unprocessable, 504 Gateway Timeout) que os bugs reais moram. Esta ferramenta dá a lista completa com significados e a RFC onde cada um está definido.</p>

<h3>Quando usar</h3>
<ul>
  <li>Lendo a doc de uma API que devolve um código que você não reconhece (425? 451?).</li>
  <li>Escolhendo o código certo pra retornar da sua própria API — 404 vs 410, 401 vs 403, 422 vs 400.</li>
  <li>Diagnosticando um 502/504 — o upstream está fora do ar ou só lento?</li>
  <li>Decidindo se 200 com error body ou um 4xx de verdade é o caminho certo.</li>
  <li>Procurando a referência da RFC pra um code review ou documento de design.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>401 significa não autenticado, 403 significa não autorizado.</strong> Os nomes confundem — 401 diz "não sei quem você é", 403 diz "sei quem você é e você não pode acessar isto". Use 403 só se uma re-autenticação não fosse ajudar.</li>
  <li><strong>302 é ambíguo quanto ao método.</strong> Historicamente browsers mudavam POST→GET num redirect 302. Use 307 (preserva o método) ou 303 (sempre GET) para ser explícito.</li>
  <li><strong>404 não é 410.</strong> 404 = "não sei"; 410 = "sei e foi embora pra sempre". Use 410 quando search engines deveriam descartar a URL.</li>
  <li><strong>200 com error body não é "RESTful".</strong> Se a request falhou no nível do recurso, retorne um 4xx com o erro no body.</li>
  <li><strong>418 é uma piada.</strong> Não use I'm-a-teapot em produção — clientes e proxies tratam de forma inconsistente.</li>
  <li><strong>RFC 9110 substitui RFC 7231/7232/7233/7234/7235.</strong> Se vai citar a spec, use 9110 (junho de 2022) a menos que precise especificamente de uma versão mais antiga.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>HTTP-Statuscodes sind die dreistelligen Zahlen, die ein Server zurückgibt, um den Ausgang der Anfrage zu signalisieren. Sie gruppieren sich in fünf Klassen: 1xx, 2xx, 3xx, 4xx, 5xx. Dieses Tool liefert die komplette Liste mit Bedeutung und RFC-Referenz.</p>
<h3>Wann verwenden</h3>
<ul>
<li>API-Dokumentation enthält einen unbekannten Code (z.B. 425, 451).</li>
<li>Den richtigen Code für die eigene API wählen — 404 vs 410, 401 vs 403.</li>
<li>Ein 502/504 untersuchen — ist der Upstream offline oder nur langsam?</li>
<li>Die RFC-Referenz für ein Designdokument nachschlagen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>401 heißt "nicht authentifiziert", 403 heißt "nicht berechtigt".</strong> Die Namen sind irreführend.</li>
<li><strong>302 ist methoden-mehrdeutig.</strong> Verwende 307 (behält Methode) oder 303 (immer GET).</li>
<li><strong>404 ≠ 410.</strong> 410 sagt: dauerhaft entfernt — Suchmaschinen sollen die URL entfernen.</li>
<li><strong>200 mit Fehler-Body ist nicht RESTful.</strong> Bei Fehlschlägen einen 4xx zurückgeben.</li>
<li><strong>418 ist ein Witz.</strong> Nicht in Produktion verwenden.</li>
<li><strong>RFC 9110 ersetzt RFC 7231 ff.</strong> Auf RFC 9110 verweisen.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Los códigos de estado HTTP son los números de tres cifras que un servidor devuelve para indicar el resultado de la petición. Se agrupan en cinco familias: 1xx, 2xx, 3xx, 4xx, 5xx. Esta herramienta ofrece la lista completa con significado y referencia RFC.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Una documentación de API muestra un código desconocido (425, 451…).</li>
<li>Elegir el código correcto para tu propia API — 404 vs 410, 401 vs 403.</li>
<li>Diagnosticar un 502/504 — ¿el upstream está caído o solo lento?</li>
<li>Buscar la RFC para un documento de diseño.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>401 significa "no autenticado", 403 significa "no autorizado".</strong> Los nombres confunden.</li>
<li><strong>302 es ambiguo respecto al método.</strong> Usa 307 (preserva método) o 303 (siempre GET).</li>
<li><strong>404 ≠ 410.</strong> 410 dice "se eliminó para siempre" — los buscadores deben olvidar la URL.</li>
<li><strong>200 con cuerpo de error no es RESTful.</strong> Devuelve un 4xx en caso de fallo.</li>
<li><strong>418 es una broma.</strong> No usar en producción.</li>
<li><strong>RFC 9110 reemplaza RFC 7231 y siguientes.</strong> Cita 9110.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Les codes de statut HTTP sont les nombres à trois chiffres renvoyés par un serveur pour indiquer le résultat de la requête. Ils se regroupent en cinq familles : 1xx, 2xx, 3xx, 4xx, 5xx. Cet outil fournit la liste complète avec signification et référence RFC.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Une doc d'API affiche un code que vous ne reconnaissez pas (425, 451…).</li>
<li>Choisir le bon code pour votre propre API — 404 vs 410, 401 vs 403.</li>
<li>Diagnostiquer un 502/504 — l'upstream est-il tombé ou simplement lent ?</li>
<li>Trouver la RFC pour un document de conception.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>401 = non authentifié, 403 = non autorisé.</strong> Les noms prêtent à confusion.</li>
<li><strong>302 est ambigu sur la méthode.</strong> Préférez 307 (préserve la méthode) ou 303 (toujours GET).</li>
<li><strong>404 ≠ 410.</strong> 410 indique "supprimé définitivement" — les moteurs de recherche doivent oublier l'URL.</li>
<li><strong>200 avec corps d'erreur n'est pas RESTful.</strong> En cas d'échec, renvoyer un 4xx.</li>
<li><strong>418 est une blague.</strong> Pas en production.</li>
<li><strong>RFC 9110 remplace RFC 7231 et suivantes.</strong> Citez 9110.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>I codici di stato HTTP sono i numeri a tre cifre restituiti da un server per indicare l'esito della richiesta. Si raggruppano in cinque famiglie: 1xx, 2xx, 3xx, 4xx, 5xx. Questo strumento offre l'elenco completo con significato e riferimento RFC.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Una documentazione API mostra un codice sconosciuto (425, 451…).</li>
<li>Scegliere il codice corretto per la tua API — 404 vs 410, 401 vs 403.</li>
<li>Diagnosticare un 502/504 — upstream giù o solo lento?</li>
<li>Trovare l'RFC per un documento di design.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>401 = non autenticato, 403 = non autorizzato.</strong> I nomi confondono.</li>
<li><strong>302 è ambiguo sul metodo.</strong> Usa 307 (preserva metodo) o 303 (sempre GET).</li>
<li><strong>404 ≠ 410.</strong> 410 indica "rimosso definitivamente" — i motori di ricerca devono dimenticare l'URL.</li>
<li><strong>200 con corpo di errore non è RESTful.</strong> In caso di fallimento, restituire un 4xx.</li>
<li><strong>418 è uno scherzo.</strong> Non in produzione.</li>
<li><strong>RFC 9110 sostituisce RFC 7231 ecc.</strong> Citare 9110.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Kody statusu HTTP to trzycyfrowe liczby, które serwer odsyła klientowi, żeby powiedzieć, jak poszło z requestem. Grupują się w pięć rodzin: 1xx (informacyjne), 2xx (sukces), 3xx (przekierowanie), 4xx (błąd klienta), 5xx (błąd serwera). Większość deweloperów zna nagłówkowe kody — 200, 301, 404, 500 — ale w długim ogonie (409 Conflict, 422 Unprocessable, 504 Gateway Timeout) mieszkają prawdziwe bugi. To narzędzie daje pełną listę ze znaczeniami i RFC, w którym każdy jest zdefiniowany.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Czytasz dokumentację API, która zwraca kod, którego nie kojarzysz (425? 451?).</li>
  <li>Wybierasz odpowiedni kod do zwrotu z własnego API — 404 vs 410, 401 vs 403, 422 vs 400.</li>
  <li>Diagnozujesz 502/504 — upstream jest down, czy tylko wolny?</li>
  <li>Rozstrzygasz, czy 200-z-error-body, czy prawdziwe 4xx jest właściwe.</li>
  <li>Szukasz odwołania do RFC do code review albo dokumentu design.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>401 znaczy nieuwierzytelniony, 403 znaczy bez uprawnień.</strong> Nazwy mylą — 401 mówi "nie wiem, kim jesteś", 403 mówi "wiem, kim jesteś, i nie wolno ci". Używaj 403 tylko wtedy, gdy ponowne uwierzytelnienie nie pomogłoby.</li>
  <li><strong>302 jest dwuznaczne co do metody.</strong> Przeglądarki historycznie zmieniały POST→GET przy redirekcie 302. Używaj 307 (zachowuje metodę) albo 303 (zawsze GET), żeby być jednoznacznym.</li>
  <li><strong>404 to nie 410.</strong> 404 = "nie wiem"; 410 = "wiem i to zniknęło na zawsze". Używaj 410, gdy wyszukiwarki mają porzucić URL.</li>
  <li><strong>200 z error body to nie "RESTowo".</strong> Jeśli request padł na poziomie zasobu, zwracaj 4xx z błędem w body.</li>
  <li><strong>418 to żart.</strong> Nie używaj I'm-a-teapot na produkcji — klienci i proxy traktują to niespójnie.</li>
  <li><strong>RFC 9110 zastępuje RFC 7231/7232/7233/7234/7235.</strong> Jeśli cytujesz spec, użyj 9110 (czerwiec 2022), chyba że specjalnie potrzebujesz starszej wersji.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>HTTP ステータスコードはサーバーがクライアントにリクエスト結果を伝える 3 桁の数字です。1xx（情報）、2xx（成功）、3xx（リダイレクト）、4xx（クライアントエラー）、5xx（サーバーエラー）の 5 系統に分かれます。多くの開発者は 200、301、404、500 など見出し的なコードは知っていますが、実際のバグは 409 Conflict、422 Unprocessable、504 Gateway Timeout などのロングテールに潜んでいます。本ツールはコードの意味と、それぞれが定義されている RFC を含めた完全なリストを提供します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>API ドキュメントに見覚えのないコード（425？ 451？）が出てきたとき。</li>
  <li>自前の API から返すコードを選びたいとき — 404 か 410、401 か 403、422 か 400。</li>
  <li>502 / 504 を切り分けたい — upstream がダウンか、ただ遅いだけか。</li>
  <li>「200 でエラーボディ」と「ちゃんとした 4xx」のどちらが正解か決めたいとき。</li>
  <li>コードレビューや設計ドキュメントのために RFC 参照を引きたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>401 は「未認証」、403 は「権限なし」です。</strong> 名前が紛らわしいですが、401 は「あなたが誰か分からない」、403 は「あなたが誰か分かっていて、それでもダメ」です。再認証で解決しないなら 403 を使います。</li>
  <li><strong>302 はメソッドに対して曖昧です。</strong> ブラウザは歴史的に 302 で POST→GET へ変えてきました。明示したければ 307（メソッド保持）か 303（常に GET）を使ってください。</li>
  <li><strong>404 と 410 は別物です。</strong> 404 = 「分からない」、410 = 「永久に消えた」。検索エンジンに URL を捨てさせたいときは 410 を返してください。</li>
  <li><strong>200 + エラーボディは「RESTful」ではありません。</strong> リソースレベルで失敗したなら 4xx を返し、ボディにエラー情報を入れてください。</li>
  <li><strong>418 はジョークです。</strong> 本番で I'm a teapot を使わないでください。クライアントやプロキシで扱いがバラバラです。</li>
  <li><strong>RFC 9110 が RFC 7231/7232/7233/7234/7235 を統合・更新しています。</strong> 仕様を引用するときは特に古い版が必要でない限り 9110（2022 年 6 月）を引いてください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>HTTP-statuscodes zijn de driecijferige nummers die een server terugstuurt om de client te vertellen hoe het request ging. Ze groeperen in vijf families: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client error), 5xx (server error). De meeste developers kennen de headline-codes — 200, 301, 404, 500 — maar de long tail (409 Conflict, 422 Unprocessable, 504 Gateway Timeout) is waar de echte bugs leven. Deze tool geeft je de volle lijst met betekenis en de RFC waar elk is gedefinieerd.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een API-doc lezen die een code teruggeeft die je niet herkent (425? 451?).</li>
  <li>De juiste code kiezen om vanuit je eigen API terug te geven — 404 vs 410, 401 vs 403, 422 vs 400.</li>
  <li>Een 502/504 diagnosticeren — is de upstream down of gewoon traag?</li>
  <li>Beslechten of 200-met-een-error-body of een echte 4xx de juiste move is.</li>
  <li>De RFC-referentie opzoeken voor een code review of design doc.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>401 betekent unauthenticated, 403 betekent unauthorized.</strong> De namen zijn misleidend — 401 zegt "ik weet niet wie je bent", 403 zegt "ik weet wie je bent en je mag het niet hebben". Gebruik 403 alleen als opnieuw authenticeren niet zou helpen.</li>
  <li><strong>302 is method-ambigu.</strong> Browsers veranderden historisch POST→GET op een 302-redirect. Gebruik 307 (behoudt method) of 303 (altijd GET) om expliciet te zijn.</li>
  <li><strong>404 is geen 410.</strong> 404 = "ik weet het niet"; 410 = "ik weet het en hij is voor altijd weg". Gebruik 410 als zoekmachines de URL moeten droppen.</li>
  <li><strong>200 met een error-body is niet "RESTful".</strong> Als het request op resource-niveau is mislukt, geef een 4xx terug met de error in de body.</li>
  <li><strong>418 is een grap.</strong> Gebruik I'm-a-teapot niet in productie — clients en proxies behandelen het inconsistent.</li>
  <li><strong>RFC 9110 supersedet RFC 7231/7232/7233/7234/7235.</strong> Als je de spec citeert, gebruik 9110 (juni 2022) tenzij je specifiek een oudere versie nodig hebt.</li>
</ul>
""",
    },
    "related": ["mime-type-lookup", "url-encoder", "jwt-decoder"],
}
