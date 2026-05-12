TOOL = {
    "slug": "url-parser",
    "category": "developer",
    "icon": "🔍",
    "tags": ["url", "parse", "query", "host", "path", "fragment", "search params"],
    "i18n": {
        "en": {
            "name": "URL Parser",
            "tagline": "Paste any URL — see the protocol, host, port, path, query parameters (decoded), hash, and origin laid out.",
            "description": "Free online URL parser. Decodes any URL into protocol, host, port, path, query string, hash, and origin, with each query parameter shown decoded. Runs entirely in your browser.",
        },
        "de": {"name": "URL-Parser", "tagline": "URL einfügen — Protokoll, Host, Port, Pfad, Query-Parameter (decodiert), Hash und Origin auf einen Blick.", "description": "Kostenloser URL-Parser. Zerlegt jede URL in Protokoll, Host, Port, Pfad, Query-String, Hash und Origin; Query-Parameter decodiert. Komplett im Browser."},
        "es": {"name": "Analizador de URL", "tagline": "Pega cualquier URL — verás protocolo, host, puerto, ruta, parámetros de consulta (decodificados), hash y origen.", "description": "Analizador URL gratuito. Decodifica cualquier URL en protocolo, host, puerto, ruta, query, hash y origen; parámetros decodificados. 100% en el navegador."},
        "fr": {"name": "Analyseur d'URL", "tagline": "Collez une URL — protocole, hôte, port, chemin, paramètres de requête (décodés), fragment et origine.", "description": "Analyseur d'URL gratuit. Décode toute URL en protocole, hôte, port, chemin, query, fragment et origine ; paramètres décodés. 100% dans le navigateur."},
        "it": {"name": "Analizzatore URL", "tagline": "Incolla un URL — protocollo, host, porta, percorso, parametri query (decodificati), hash e origine.", "description": "Analizzatore URL gratuito. Decodifica qualsiasi URL in protocollo, host, porta, percorso, query, hash e origine; parametri decodificati. 100% nel browser."},
        "pt": {"name": "Parser de URL", "tagline": "Cole qualquer URL — veja protocol, host, porta, path, query parameters (decodificados), hash e origin organizados.", "description": "Parser de URL online gratuito. Decodifica qualquer URL em protocol, host, porta, path, query string, hash e origin, com cada query parameter exibido decodificado. Roda inteiramente no seu navegador."},
        "pl": {"name": "Parser URL", "tagline": "Wklej dowolny URL — zobacz protocol, host, port, path, query parameters (zdekodowane), hash i origin rozłożone na części.", "description": "Darmowy online parser URL. Dekoduje dowolny URL na protocol, host, port, path, query string, hash i origin, z każdym query parameterem wyświetlonym zdekodowanym. Działa w całości w przeglądarce."},
        "ja": {"name": "URL パーサー", "tagline": "URL を貼ると、protocol・host・port・path・query パラメータ（デコード済み）・hash・origin に分解して表示。", "description": "オンライン無料の URL パーサー。任意の URL を protocol、host、port、path、query string、hash、origin に分解し、各クエリパラメータをデコード済みで表示します。すべてブラウザ内で動作します。"},
        "nl": {"name": "URL Parser", "tagline": "Plak elke URL — zie protocol, host, port, path, query parameters (gedecodeerd), hash en origin uitgesplitst.", "description": "Gratis online URL parser. Decodeert elke URL naar protocol, host, port, path, query string, hash en origin, met elke query-parameter gedecodeerd getoond. Draait volledig in je browser."},
        "tr": {"name": "URL Parser", "tagline": "Herhangi bir URL'i yapıştır — protokolü, host'u, port'u, path'i, query parametrelerini (decoded), hash'i ve origin'i ayrıştırılmış olarak gör.", "description": "Ücretsiz online URL parser. Herhangi bir URL'i protokol, host, port, path, query string, hash ve origin'e çözer; her query parametresi decoded gösterilir. Tamamen tarayıcında çalışır."},
        "id": {"name": "URL Parser", "tagline": "Tempel URL apa pun — lihat protokol, host, port, path, parameter query (di-decode), hash, dan origin yang sudah diurai.", "description": "URL parser gratis. Tempel URL apa pun dan lihat protokol, host, port, path, parameter query yang di-decode, hash, dan origin-nya. Bantu debug masalah routing dan inspeksi link yang kompleks."},
        "vi": {"name": "Trình phân tích URL", "tagline": "Dán bất kỳ URL nào — xem protocol, host, port, path, tham số query (đã decode), hash và origin đã phân tích.", "description": "Trình phân tích URL miễn phí trực tuyến. Tách bất kỳ URL nào thành protocol, host, port, path, tham số query (đã decode), hash và origin để debug API và tích hợp."},
    },
    "body": """
<div class="tool-card">
  <label>URL</label>
  <input type="text" id="up-in" oninput="upRun()" placeholder="https://user:pw@example.com:8080/path/to?lang=en&items=1&items=2#section" value="https://www.example.com:8080/products/search?q=hello%20world&category=books&page=2#reviews" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
  <div class="meta" style="margin-top:0.5rem">Both URL-encoded and decoded views shown for query values.</div>
</div>
<div class="tool-card">
  <label>Components</label>
  <div id="up-components" class="output">{LBL_NO_INPUT}</div>
</div>
<div class="tool-card">
  <label>Query parameters</label>
  <div id="up-params" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.up-table { width: 100%; }
.up-table td { padding: 0.4rem 0.5rem; border-bottom: 1px solid var(--border); font-family: ui-monospace, monospace; font-size: 0.85rem; vertical-align: top; word-break: break-all; }
.up-table td:first-child { width: 30%; color: var(--text-muted); }
.up-empty { color: var(--text-muted); font-style: italic; }
</style>
<script>
function upEsc(s){ return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

function upRun(){
  const v = document.getElementById('up-in').value.trim();
  const comps = document.getElementById('up-components');
  const params = document.getElementById('up-params');
  comps.classList.remove('error');
  params.classList.remove('error');
  if(!v){ comps.textContent = '{LBL_NO_INPUT}'; params.textContent = '{LBL_NO_INPUT}'; return; }
  let url;
  try { url = new URL(v); }
  catch(e){
    // Try with prepended https:// for hostname-only inputs
    try { url = new URL('https://' + v); }
    catch(e2){
      comps.classList.add('error');
      comps.textContent = '✗ Not a valid URL — ' + e.message;
      params.textContent = '';
      return;
    }
  }

  const rows = [
    ['Origin', url.origin || '<i class="up-empty">(opaque)</i>'],
    ['Protocol', url.protocol],
    ['Username', url.username || '<i class="up-empty">(none)</i>'],
    ['Password', url.password ? '<i class="up-empty">(set)</i>' : '<i class="up-empty">(none)</i>'],
    ['Host', url.host],
    ['Hostname', url.hostname],
    ['Port', url.port || '<i class="up-empty">(default)</i>'],
    ['Pathname', url.pathname || '<i class="up-empty">(empty)</i>'],
    ['Search', url.search || '<i class="up-empty">(empty)</i>'],
    ['Hash', url.hash || '<i class="up-empty">(empty)</i>'],
  ];
  comps.innerHTML = '<table class="up-table">' + rows.map(r => `<tr><td>${r[0]}</td><td>${typeof r[1] === 'string' && !r[1].startsWith('<') ? upEsc(r[1]) : r[1]}</td></tr>`).join('') + '</table>';

  const sp = url.searchParams;
  const keys = [];
  for(const k of sp.keys()) if(!keys.includes(k)) keys.push(k);
  if(keys.length === 0){
    params.innerHTML = '<i class="up-empty">No query parameters.</i>';
  } else {
    let rowsHtml = '<table class="up-table"><tr><td><b>Key</b></td><td><b>Decoded value</b></td><td><b>Raw</b></td></tr>';
    for(const k of keys){
      const all = sp.getAll(k);
      all.forEach((vv, i) => {
        // Re-encode to show "raw" form as it would appear in the URL
        const raw = encodeURIComponent(k) + '=' + encodeURIComponent(vv);
        const keyDisp = i === 0 ? upEsc(k) : '';
        rowsHtml += `<tr><td>${keyDisp}${all.length > 1 ? ' <span class="up-empty">[' + i + ']</span>' : ''}</td><td>${upEsc(vv)}</td><td><span style="color:var(--text-muted)">${upEsc(raw)}</span></td></tr>`;
      });
    }
    rowsHtml += '</table>';
    params.innerHTML = rowsHtml;
  }
}
document.addEventListener('DOMContentLoaded', upRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A URL is a structured string with seven well-defined parts (scheme, authority, host, port, path, query, fragment) that you eyeball as one blob. When something is wrong — the wrong parameter, an unexpected port, an extra encoded character — it's much easier to spot in a parsed table than in the raw string. This tool uses the browser's native <code>URL</code> object so the parse exactly matches what JavaScript sees, then breaks each query parameter out so the decoded values are visible alongside the raw form.</p>

<h3>When to use it</h3>
<ul>
  <li>Debugging an OAuth callback URL where the <code>state</code> or <code>code</code> looks wrong.</li>
  <li>Inspecting a tracking URL (UTM tags, click-tokens) and seeing the actual values rather than the encoded blob.</li>
  <li>Confirming a webhook URL parses the way the receiving service expects — particularly the path and any query.</li>
  <li>Eyeballing why a deep link works in one app and not another (port? scheme? authority?).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Repeated query keys are real.</strong> <code>?a=1&amp;a=2</code> is two values for <code>a</code>; tools that read only the first miss data. The parser shows all values per key.</li>
  <li><strong>The fragment never reaches the server.</strong> Anything after <code>#</code> stays in the browser. If your backend isn't seeing data you put in the URL, check whether it's actually in the fragment.</li>
  <li><strong>Encoding matters.</strong> <code>%20</code> in a query value decodes to space; <code>+</code> in a query value <em>also</em> decodes to space (per <code>application/x-www-form-urlencoded</code>). The browser's <code>URL.searchParams</code> handles both.</li>
  <li><strong>Default ports don't appear in <code>port</code>.</strong> A URL like <code>https://example.com/</code> has <code>port</code> empty (the default 443 is implied).</li>
  <li><strong>Punycode hostnames.</strong> <code>example.中国</code> is stored as <code>xn--fiqs8s</code> internally; <code>hostname</code> may show the ASCII form depending on the browser.</li>
  <li><strong>Origin is sometimes "null".</strong> For <code>file://</code>, <code>data:</code>, or sandboxed contexts, origin is opaque.</li>
  <li><strong>This is parsing, not validation.</strong> A URL can parse cleanly and still be wrong for your application (e.g. wrong host, missing path).</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Uma URL é uma string estruturada com sete partes bem definidas (scheme, authority, host, porta, path, query, fragment) que você enxerga como um único bloco. Quando algo está errado — o parâmetro errado, uma porta inesperada, um caractere codificado a mais — é muito mais fácil identificar numa tabela parseada do que na string crua. Esta ferramenta usa o objeto <code>URL</code> nativo do navegador, então o parse corresponde exatamente ao que o JavaScript enxerga, e separa cada query parameter para que os valores decodificados fiquem visíveis ao lado da forma raw.</p>

<h3>Quando usar</h3>
<ul>
  <li>Debugando uma URL de callback OAuth onde o <code>state</code> ou <code>code</code> parece errado.</li>
  <li>Inspecionando uma URL de tracking (UTM tags, click-tokens) e vendo os valores reais em vez do bloco codificado.</li>
  <li>Confirmando que uma URL de webhook é parseada como o serviço receptor espera — em particular o path e qualquer query.</li>
  <li>Investigando por que um deep link funciona em um app e não em outro (porta? scheme? authority?).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Chaves de query repetidas são reais.</strong> <code>?a=1&amp;a=2</code> são dois valores para <code>a</code>; ferramentas que leem só o primeiro perdem dados. O parser mostra todos os valores por chave.</li>
  <li><strong>O fragment nunca chega ao servidor.</strong> Tudo depois de <code>#</code> fica no navegador. Se seu backend não está vendo dados que você colocou na URL, verifique se eles não estão no fragment.</li>
  <li><strong>Encoding importa.</strong> <code>%20</code> em um valor de query decodifica para espaço; <code>+</code> em um valor de query <em>também</em> decodifica para espaço (segundo <code>application/x-www-form-urlencoded</code>). O <code>URL.searchParams</code> do navegador trata os dois.</li>
  <li><strong>Portas padrão não aparecem em <code>port</code>.</strong> Uma URL como <code>https://example.com/</code> tem <code>port</code> vazio (a 443 padrão é implícita).</li>
  <li><strong>Hostnames com Punycode.</strong> <code>example.中国</code> é armazenado internamente como <code>xn--fiqs8s</code>; <code>hostname</code> pode mostrar a forma ASCII dependendo do navegador.</li>
  <li><strong>Origin às vezes é "null".</strong> Para <code>file://</code>, <code>data:</code> ou contextos sandboxed, origin é opaco.</li>
  <li><strong>Isto é parsing, não validação.</strong> Uma URL pode parsear corretamente e ainda estar errada para sua aplicação (ex.: host errado, path faltando).</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Eine URL hat sieben definierte Teile (Schema, Authority, Host, Port, Pfad, Query, Fragment), die man als eine Zeichenkette sieht. In einer aufgeschlüsselten Tabelle sieht man Probleme leichter. Das Tool nutzt das native <code>URL</code>-Objekt des Browsers — Parse passt genau zu dem, was JS sieht.</p>
<h3>Wann verwenden</h3>
<ul>
<li>OAuth-Callback debuggen wenn <code>state</code> oder <code>code</code> komisch aussieht.</li>
<li>Tracking-URL (UTM, Click-Tokens) decodiert betrachten.</li>
<li>Webhook-URL prüfen.</li>
<li>Deep Links zwischen Apps vergleichen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Wiederholte Keys sind real.</strong> <code>?a=1&amp;a=2</code> = zwei Werte.</li>
<li><strong>Fragment erreicht den Server nicht.</strong> Alles nach <code>#</code> bleibt im Browser.</li>
<li><strong><code>+</code> und <code>%20</code> decodieren beide zu Space</strong> (Query-String).</li>
<li><strong>Standard-Ports erscheinen nicht in <code>port</code>.</strong></li>
<li><strong>Punycode-Hostnames.</strong> Browser-abhängige Anzeige.</li>
<li><strong>Origin kann "null" sein</strong> bei file://, data:, sandboxed.</li>
<li><strong>Parsing ≠ Validierung.</strong></li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Una URL tiene siete partes (esquema, autoridad, host, puerto, ruta, query, fragmento) que ves como una sola cadena. Una tabla descompuesta hace fácil detectar lo que está mal. La herramienta usa el objeto <code>URL</code> nativo del navegador.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Depurar callback OAuth con <code>state</code> o <code>code</code> raros.</li>
<li>Examinar URL de tracking (UTM, click-tokens) decodificada.</li>
<li>Verificar URL de webhook.</li>
<li>Comparar deep links entre apps.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Claves repetidas son reales.</strong> <code>?a=1&amp;a=2</code> = dos valores.</li>
<li><strong>El fragmento no llega al servidor.</strong> Todo tras <code>#</code> se queda en el navegador.</li>
<li><strong><code>+</code> y <code>%20</code> ambos decodifican a espacio</strong> en query.</li>
<li><strong>Los puertos por defecto no aparecen en <code>port</code>.</strong></li>
<li><strong>Punycode en hostnames.</strong> Visualización dependiente del navegador.</li>
<li><strong>Origin puede ser "null"</strong> con file://, data:, sandbox.</li>
<li><strong>Parsing ≠ validación.</strong></li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Une URL a sept parties (schéma, autorité, hôte, port, chemin, query, fragment) qu'on voit comme une seule chaîne. Un tableau éclaté facilite le repérage des erreurs. L'outil utilise l'objet <code>URL</code> natif du navigateur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Débugger un callback OAuth avec <code>state</code> ou <code>code</code> bizarres.</li>
<li>Inspecter une URL de tracking (UTM) décodée.</li>
<li>Vérifier une URL de webhook.</li>
<li>Comparer deep links entre apps.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Les clés répétées sont réelles.</strong> <code>?a=1&amp;a=2</code> = deux valeurs.</li>
<li><strong>Le fragment n'atteint pas le serveur.</strong> Tout après <code>#</code> reste dans le navigateur.</li>
<li><strong><code>+</code> et <code>%20</code> décodent tous deux en espace</strong> dans la query.</li>
<li><strong>Les ports par défaut n'apparaissent pas dans <code>port</code>.</strong></li>
<li><strong>Punycode dans les hostnames.</strong> Affichage selon navigateur.</li>
<li><strong>Origin peut être « null »</strong> avec file://, data:, sandbox.</li>
<li><strong>Parsing ≠ validation.</strong></li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Un URL ha sette parti (schema, autorità, host, porta, percorso, query, frammento) che si vedono come una stringa unica. Una tabella scomposta rende facile individuare errori. Lo strumento usa l'oggetto <code>URL</code> nativo del browser.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Debug callback OAuth con <code>state</code> o <code>code</code> strani.</li>
<li>Ispezionare URL di tracking (UTM) decodificato.</li>
<li>Verificare URL di webhook.</li>
<li>Confrontare deep link tra app.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Chiavi ripetute sono reali.</strong> <code>?a=1&amp;a=2</code> = due valori.</li>
<li><strong>Il frammento non raggiunge il server.</strong> Tutto dopo <code>#</code> resta nel browser.</li>
<li><strong><code>+</code> e <code>%20</code> entrambi decodificano in spazio</strong> nella query.</li>
<li><strong>Le porte di default non compaiono in <code>port</code>.</strong></li>
<li><strong>Punycode negli hostname.</strong> Visualizzazione browser-dipendente.</li>
<li><strong>Origin può essere "null"</strong> con file://, data:, sandbox.</li>
<li><strong>Parsing ≠ validazione.</strong></li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>URL to ustrukturyzowany string z siedmioma jasno zdefiniowanymi częściami (scheme, authority, host, port, path, query, fragment), który widzisz jako jedną bryłę. Gdy coś jest nie tak — zły parametr, niespodziewany port, dodatkowy zakodowany znak — znacznie łatwiej to wypatrzeć w sparsowanej tabeli niż w surowym stringu. To narzędzie używa natywnego obiektu <code>URL</code> przeglądarki, więc parse dokładnie odpowiada temu, co widzi JavaScript, a potem wyciąga każdy query parameter, żeby zdekodowane wartości były widoczne obok formy raw.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Debug callback URL OAuth, gdzie <code>state</code> albo <code>code</code> wygląda źle.</li>
  <li>Inspekcja URL-a trackingowego (UTM tagi, click-tokeny) i widzenie faktycznych wartości zamiast zakodowanej bryły.</li>
  <li>Potwierdzenie, że URL webhooka parsuje się tak, jak oczekuje serwis odbiorczy — w szczególności path i ewentualna query.</li>
  <li>Sprawdzenie, dlaczego deep link działa w jednej apce, a w drugiej nie (port? scheme? authority?).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Powtórzone klucze query są realne.</strong> <code>?a=1&amp;a=2</code> to dwie wartości dla <code>a</code>; narzędzia czytające tylko pierwszą gubią dane. Parser pokazuje wszystkie wartości per klucz.</li>
  <li><strong>Fragment nigdy nie dociera do serwera.</strong> Wszystko po <code>#</code> zostaje w przeglądarce. Jeśli twój backend nie widzi danych, które wsadziłeś w URL, sprawdź, czy aby nie są w fragmencie.</li>
  <li><strong>Encoding ma znaczenie.</strong> <code>%20</code> w wartości query dekoduje się do spacji; <code>+</code> w wartości query <em>też</em> dekoduje się do spacji (wg <code>application/x-www-form-urlencoded</code>). Przeglądarkowy <code>URL.searchParams</code> obsługuje obie.</li>
  <li><strong>Domyślne porty nie pojawiają się w <code>port</code>.</strong> URL typu <code>https://example.com/</code> ma puste <code>port</code> (domyślne 443 jest dorozumiane).</li>
  <li><strong>Hostname'y w Punycode.</strong> <code>example.中国</code> jest wewnętrznie trzymane jako <code>xn--fiqs8s</code>; <code>hostname</code> może pokazać formę ASCII, zależnie od przeglądarki.</li>
  <li><strong>Origin bywa "null".</strong> Dla <code>file://</code>, <code>data:</code> albo sandboxowanych kontekstów origin jest opaque.</li>
  <li><strong>To parsowanie, nie walidacja.</strong> URL może parsować się czysto i dalej być zły dla twojej aplikacji (np. zły host, brakujący path).</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>URL は scheme、authority、host、port、path、query、fragment の 7 つの構成要素を持つ構造化文字列ですが、見た目は 1 本の文字列です。何かが間違っているとき（パラメータ、ポート、余分なエンコード文字など）、生の文字列より分解されたテーブルの方がはるかに気付きやすくなります。本ツールはブラウザ標準の <code>URL</code> オブジェクトを使うため、JavaScript が見るのと同じパース結果を表示し、各クエリパラメータを raw とデコード済みの両方で表示します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>OAuth コールバック URL の <code>state</code> や <code>code</code> がおかしいときのデバッグ。</li>
  <li>トラッキング URL（UTM タグ、クリックトークン）の実値をエンコードされた塊ではなく素のまま確認したいとき。</li>
  <li>Webhook URL が受け側サービスの期待通りにパースされるか確認したいとき（特に path とクエリ）。</li>
  <li>あるアプリでは動くディープリンクが別アプリで動かない原因（port？ scheme？ authority？）を見つけたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>同じキーの複数値は実在します。</strong> <code>?a=1&amp;a=2</code> は <code>a</code> に 2 つの値があります。最初しか読まないツールはデータを取りこぼします。本パーサはキーごとの全値を表示します。</li>
  <li><strong>fragment はサーバーに到達しません。</strong> <code>#</code> 以降はブラウザ内で完結します。バックエンドに届かないデータがあれば、fragment に入っていないか確認してください。</li>
  <li><strong>エンコーディングが重要。</strong> クエリ値の <code>%20</code> も <code>+</code> も（<code>application/x-www-form-urlencoded</code> 上は）スペースにデコードされます。ブラウザの <code>URL.searchParams</code> は両方を扱います。</li>
  <li><strong>デフォルトポートは <code>port</code> に出ません。</strong> <code>https://example.com/</code> の <code>port</code> は空文字列です（443 は暗黙）。</li>
  <li><strong>Punycode のホスト名。</strong> <code>example.中国</code> は内部的に <code>xn--fiqs8s</code>。ブラウザによって ASCII 表記で表示されることがあります。</li>
  <li><strong>origin が "null" のことがあります。</strong> <code>file://</code>、<code>data:</code>、サンドボックスコンテキストでは origin は不透明値です。</li>
  <li><strong>これはパースであって検証ではありません。</strong> パースに成功しても、アプリにとって正しい URL とは限りません（host が違う、path が抜けているなど）。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een URL is een gestructureerde string met zeven goed-gedefinieerde delen (scheme, authority, host, port, path, query, fragment) die je als één blob inschat. Als er iets mis is — de verkeerde parameter, een onverwachte port, een extra encoded karakter — is dat veel makkelijker te spotten in een geparseerde tabel dan in de raw string. Deze tool gebruikt het native <code>URL</code>-object van de browser zodat de parse precies matcht met wat JavaScript ziet, en splitst dan elke query-parameter uit zodat de decoded values naast de raw vorm zichtbaar zijn.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een OAuth callback-URL debuggen waar de <code>state</code> of <code>code</code> verkeerd lijkt.</li>
  <li>Een tracking-URL (UTM-tags, click-tokens) inspecteren en de daadwerkelijke values zien in plaats van de encoded blob.</li>
  <li>Bevestigen dat een webhook-URL parset zoals de ontvangende service verwacht — vooral het path en de eventuele query.</li>
  <li>Inschatten waarom een deep link in de ene app werkt en niet in de andere (port? scheme? authority?).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Herhaalde query-keys zijn echt.</strong> <code>?a=1&amp;a=2</code> is twee values voor <code>a</code>; tools die alleen de eerste lezen missen data. De parser toont alle values per key.</li>
  <li><strong>Het fragment bereikt nooit de server.</strong> Alles na <code>#</code> blijft in de browser. Als je backend data niet ziet die je in de URL hebt gezet, check of die eigenlijk in het fragment staat.</li>
  <li><strong>Encoding doet ertoe.</strong> <code>%20</code> in een query-value decodeert naar spatie; <code>+</code> in een query-value <em>ook</em> naar spatie (volgens <code>application/x-www-form-urlencoded</code>). De browser's <code>URL.searchParams</code> handelt beide af.</li>
  <li><strong>Default ports verschijnen niet in <code>port</code>.</strong> Een URL als <code>https://example.com/</code> heeft <code>port</code> leeg (de default 443 wordt geïmpliceerd).</li>
  <li><strong>Punycode hostnames.</strong> <code>example.中国</code> wordt intern opgeslagen als <code>xn--fiqs8s</code>; <code>hostname</code> kan de ASCII-vorm tonen afhankelijk van de browser.</li>
  <li><strong>Origin is soms "null".</strong> Voor <code>file://</code>, <code>data:</code> of sandboxed contexts is origin opaque.</li>
  <li><strong>Dit is parsing, geen validatie.</strong> Een URL kan schoon parsen en nog steeds verkeerd zijn voor je applicatie (bijv. verkeerde host, missing path).</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir URL, tek bir blob olarak gözle gördüğün yedi iyi tanımlanmış parçaya (scheme, authority, host, port, path, query, fragment) sahip yapılandırılmış bir string'tir. Bir şey yanlış olduğunda — yanlış parametre, beklenmeyen port, fazla kodlanmış karakter — bunu ham string'de değil, parse edilmiş bir tabloda tespit etmek çok daha kolaydır. Bu araç tarayıcının yerel <code>URL</code> nesnesini kullanır, böylece parse JavaScript'in gördüğüyle tam eşleşir, sonra her query parametresini ayırır, böylece çözülmüş değerler ham formla birlikte görünür olur.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li><code>state</code> veya <code>code</code> yanlış görünen bir OAuth callback URL'ini debug etme.</li>
  <li>Bir takip URL'ini (UTM tag'leri, click-token'lar) inceleme ve kodlanmış blob yerine gerçek değerleri görme.</li>
  <li>Bir webhook URL'inin alıcı servisin beklediği şekilde parse olduğunu doğrulama — özellikle path ve herhangi bir query.</li>
  <li>Bir deep link'in neden bir uygulamada çalışıp başkasında çalışmadığını anlama (port? scheme? authority?).</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Tekrarlanan query anahtarları gerçektir.</strong> <code>?a=1&amp;a=2</code> <code>a</code> için iki değerdir; sadece ilkini okuyan araçlar veriyi kaçırır. Parser her anahtar başına tüm değerleri gösterir.</li>
  <li><strong>Fragment sunucuya asla ulaşmaz.</strong> <code>#</code>'dan sonraki her şey tarayıcıda kalır. Backend'in URL'e koyduğun veriyi görmüyorsa, gerçekten fragment'ta olup olmadığını kontrol et.</li>
  <li><strong>Kodlama önemlidir.</strong> Bir query değerindeki <code>%20</code> boşluğa çözülür; bir query değerindeki <code>+</code> <em>de</em> boşluğa çözülür (<code>application/x-www-form-urlencoded</code>'a göre). Tarayıcının <code>URL.searchParams</code>'ı her ikisini de işler.</li>
  <li><strong>Varsayılan port'lar <code>port</code>'ta görünmez.</strong> <code>https://example.com/</code> gibi bir URL'in <code>port</code>'u boştur (varsayılan 443 ima edilir).</li>
  <li><strong>Punycode hostname'leri.</strong> <code>example.中国</code> dahili olarak <code>xn--fiqs8s</code> olarak saklanır; <code>hostname</code> tarayıcıya bağlı olarak ASCII formu gösterebilir.</li>
  <li><strong>Origin bazen "null"dur.</strong> <code>file://</code>, <code>data:</code> veya sandbox'lı bağlamlar için origin opaktır.</li>
  <li><strong>Bu parsing'dir, doğrulama değil.</strong> Bir URL temiz parse edebilir ve hâlâ uygulaman için yanlış olabilir (örn. yanlış host, eksik path).</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>URL adalah string terstruktur dengan tujuh bagian yang terdefinisi dengan baik (scheme, authority, host, port, path, query, fragment) yang kamu lihat sebagai satu blob. Saat ada yang salah — parameter keliru, port tak terduga, karakter yang ke-encode berlebihan — jauh lebih mudah menemukannya di tabel yang sudah di-parse daripada di string mentah. Tool ini menggunakan objek <code>URL</code> bawaan browser, jadi hasil parse persis sama dengan yang dilihat JavaScript, lalu memecah setiap query parameter sehingga value yang sudah di-decode terlihat berdampingan dengan bentuk mentahnya.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Debug URL callback OAuth yang <code>state</code> atau <code>code</code>-nya kelihatan salah.</li>
  <li>Memeriksa URL tracking (UTM tags, click-token) dan melihat value sebenarnya alih-alih blob yang sudah di-encode.</li>
  <li>Memverifikasi bahwa URL webhook ter-parse seperti yang diharapkan service penerima — terutama path dan query apa pun.</li>
  <li>Memahami kenapa sebuah deep link bekerja di satu aplikasi tapi tidak di yang lain (port? scheme? authority?).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Key query yang berulang itu nyata.</strong> <code>?a=1&amp;a=2</code> adalah dua value untuk <code>a</code>; tool yang hanya membaca yang pertama akan kehilangan data. Parser ini menampilkan semua value per key.</li>
  <li><strong>Fragment tidak pernah sampai ke server.</strong> Apa pun setelah <code>#</code> tetap di browser. Jika backend tidak melihat data yang kamu taruh di URL, cek apakah data itu sebenarnya ada di fragment.</li>
  <li><strong>Encoding itu penting.</strong> <code>%20</code> di value query ter-decode menjadi spasi; <code>+</code> di value query <em>juga</em> ter-decode menjadi spasi (per <code>application/x-www-form-urlencoded</code>). <code>URL.searchParams</code> browser menangani keduanya.</li>
  <li><strong>Port default tidak muncul di <code>port</code>.</strong> URL seperti <code>https://example.com/</code> punya <code>port</code> kosong (default 443 tersirat).</li>
  <li><strong>Hostname punycode.</strong> <code>example.中国</code> disimpan secara internal sebagai <code>xn--fiqs8s</code>; <code>hostname</code> bisa menampilkan bentuk ASCII tergantung browser.</li>
  <li><strong>Origin kadang-kadang "null".</strong> Untuk <code>file://</code>, <code>data:</code>, atau konteks sandbox, origin bersifat opaque.</li>
  <li><strong>Ini parsing, bukan validasi.</strong> URL bisa ter-parse bersih dan tetap salah untuk aplikasimu (mis. host keliru, path hilang).</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Một URL như <code>https://api.example.com:8443/v2/users?id=42#section</code> có nhiều phần: protocol, host, port, path, query, hash. Khi debug, bạn thường muốn nhìn vào các phần đó tách biệt. Tool này dùng <code>URL</code> API tích hợp của trình duyệt để phân tích chính xác bất kỳ URL nào, hiển thị các phần và param query đã decode.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Debug API integration — kiểm tra URL có tất cả các param dự kiến không.</li>
  <li>Tách host từ URL cấu hình.</li>
  <li>Decode param query phức tạp được encoded nhiều lớp.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>URL không phải URI.</strong> URI là superset; URL là tập con cụ thể có scheme và authority.</li>
  <li><strong>Hash không gửi đến server.</strong> Phần sau <code>#</code> chỉ tồn tại trong trình duyệt — server không thấy. Web app SPA dùng nó cho client-side routing.</li>
  <li><strong>Port mặc định không xuất hiện.</strong> <code>https://example.com</code> dùng port 443 nhưng bạn không thấy nó trong URL. Tool này hiển thị nó.</li>
</ul>
""",
    },
    "related": ["url-encoder", "query-string-builder", "jwt-decoder", "base64-encoder"],
    "howto": {"flow": "transform", "action": "convert", "noun": "URL"},
}
