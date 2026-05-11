TOOL = {
    "slug": "yaml-json",
    "category": "data",
    "icon": "🔁",
    "tags": ["yaml", "json", "convert", "kubernetes", "config", "data"],
    "i18n": {
        "en": {
            "name": "YAML ↔ JSON Converter",
            "tagline": "Convert between YAML and JSON in either direction. Useful for Kubernetes manifests, CI configs, and OpenAPI specs.",
            "description": "Free online YAML to JSON and JSON to YAML converter. Bidirectional, runs entirely in your browser. Handles anchors, aliases, and multi-document YAML.",
        },
        "de": {
            "name": "YAML ↔ JSON Konverter",
            "tagline": "Konvertiere zwischen YAML und JSON in beide Richtungen. Für Kubernetes-Manifeste, CI-Configs und OpenAPI-Specs.",
            "description": "Kostenloser YAML-zu-JSON und JSON-zu-YAML Konverter. Bidirektional, läuft komplett im Browser. Anker, Aliase und Multi-Dokument-YAML unterstützt.",
        },
        "es": {
            "name": "Conversor YAML ↔ JSON",
            "tagline": "Convierte entre YAML y JSON en ambas direcciones. Útil para manifiestos Kubernetes, configs CI y specs OpenAPI.",
            "description": "Conversor YAML a JSON y JSON a YAML gratuito. Bidireccional, todo en tu navegador. Soporta anclas, alias y YAML multi-documento.",
        },
        "fr": {
            "name": "Convertisseur YAML ↔ JSON",
            "tagline": "Convertissez entre YAML et JSON dans les deux sens. Idéal pour manifestes Kubernetes, configs CI et specs OpenAPI.",
            "description": "Convertisseur YAML vers JSON et JSON vers YAML gratuit. Bidirectionnel, tout dans votre navigateur. Ancres, alias et YAML multi-documents supportés.",
        },
        "it": {
            "name": "Convertitore YAML ↔ JSON",
            "tagline": "Converti tra YAML e JSON in entrambe le direzioni. Utile per manifesti Kubernetes, config CI e specifiche OpenAPI.",
            "description": "Convertitore YAML-JSON e JSON-YAML gratuito. Bidirezionale, tutto nel browser. Supporta ancore, alias e YAML multi-documento.",
        },
        "pt": {
            "name": "Conversor YAML ↔ JSON",
            "tagline": "Converta entre YAML e JSON nas duas direções. Útil para manifests do Kubernetes, configs de CI e specs OpenAPI.",
            "description": "Conversor de YAML para JSON e JSON para YAML online gratuito. Bidirecional, roda inteiramente no seu navegador. Suporta anchors, aliases e YAML multi-documento.",
        },
        "pl": {
            "name": "Konwerter YAML ↔ JSON",
            "tagline": "Konwertuj między YAML a JSON w obie strony. Przydatne do manifestów Kubernetes, configów CI i speców OpenAPI.",
            "description": "Darmowy online konwerter YAML do JSON i JSON do YAML. Dwukierunkowy, działa w całości w przeglądarce. Obsługuje anchory, aliasy i wielodokumentowy YAML.",
        },
        "ja": {
            "name": "YAML ↔ JSON コンバーター",
            "tagline": "YAML と JSON を双方向に変換。Kubernetes マニフェスト、CI 設定、OpenAPI 仕様などに便利。",
            "description": "オンライン無料の YAML → JSON / JSON → YAML コンバーター。双方向で、すべてブラウザ内で動作。アンカー、エイリアス、複数ドキュメント YAML にも対応します。",
        },
        "nl": {"name": "YAML ↔ JSON Converter", "tagline": "Converteer tussen YAML en JSON in beide richtingen. Nuttig voor Kubernetes manifests, CI-configs en OpenAPI-specs.", "description": "Gratis online YAML-naar-JSON en JSON-naar-YAML converter. Bidirectioneel, draait volledig in je browser. Handelt anchors, aliases en multi-document YAML af."},
        "tr": {"name": "YAML ↔ JSON Dönüştürücü", "tagline": "YAML ve JSON arasında her iki yöne dönüştür. Kubernetes manifest'leri, CI config'leri ve OpenAPI spec'leri için kullanışlı.", "description": "Ücretsiz online YAML'den JSON'a ve JSON'dan YAML'a dönüştürücü. Çift yönlü, tamamen tarayıcında çalışır. Anchor'ları, alias'ları ve çoklu belge YAML'ı işler."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_FROM}</label>
      <select id="yj-from" onchange="yjSwap()">
        <option value="yaml">YAML</option>
        <option value="json">JSON</option>
      </select>
    </div>
    <div>
      <label>{LBL_TO}</label>
      <select id="yj-to" onchange="yjConv()">
        <option value="json">JSON</option>
        <option value="yaml">YAML</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="yj-in" oninput="yjConv()" spellcheck="false" placeholder="apiVersion: v1
kind: ConfigMap
metadata:
  name: example
data:
  message: hello"></textarea>
  <div class="button-row">
    <button onclick="yjConv()">{LBL_CONVERT}</button>
    <button class="secondary" onclick="document.getElementById('yj-in').value=''; yjConv()">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="yj-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('yj-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
<script>
function yjSwap(){
  const f = document.getElementById('yj-from').value;
  const t = document.getElementById('yj-to');
  // ensure 'to' is the OTHER format
  t.value = (f === 'yaml') ? 'json' : 'yaml';
  yjConv();
}
function yjConv(){
  const from = document.getElementById('yj-from').value;
  const to = document.getElementById('yj-to').value;
  const raw = document.getElementById('yj-in').value;
  const out = document.getElementById('yj-out');
  out.classList.remove('error');
  if (!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    let data;
    if (from === 'yaml') data = jsyaml.load(raw);
    else data = JSON.parse(raw);
    if (to === 'json') out.textContent = JSON.stringify(data, null, 2);
    else out.textContent = jsyaml.dump(data, { indent: 2, lineWidth: 120 });
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + (e.message || String(e));
  }
}
document.addEventListener('DOMContentLoaded', yjConv);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>YAML and JSON describe the same things — nested maps, lists, primitives — but trade off readability vs strictness. YAML is friendlier for humans (Kubernetes manifests, GitHub Actions, OpenAPI, most CI configs); JSON is what APIs and machine-readable formats ship. This converter flips between them losslessly for the structures both can express. YAML uses <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> (YAML 1.2); JSON uses the native API. Both directions run in your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Pasting an OpenAPI / k8s / docker-compose YAML into a tool that needs JSON.</li>
  <li>Converting an API response (JSON) into YAML for a config file.</li>
  <li>Auditing a YAML file's actual structure when ambiguous indentation makes parentage unclear.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>The "Norway problem".</strong> YAML 1.1 coerced <code>NO</code>, <code>YES</code>, <code>ON</code>, <code>OFF</code> into booleans. YAML 1.2 doesn't, but downstream parsers may. Quote ambiguous strings to be safe.</li>
  <li><strong>Multi-document YAML</strong> (<code>---</code> separators) — only the first document is converted.</li>
  <li><strong>Custom tags</strong> (<code>!!python/object</code>, <code>!Ref</code>, etc.) violate strict YAML 1.2. CloudFormation YAML and PyYAML pickle dumps will fail; clean tags first.</li>
  <li><strong>Anchors and aliases get expanded</strong> on YAML→JSON. JSON has no references, so <code>*ref</code> nodes inline. Round-tripping gives a value-equivalent but textually-larger YAML.</li>
  <li><strong>Numbers vs strings.</strong> Unquoted YAML <code>3.14</code> is a float; <code>"3.14"</code> is a string.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>YAML e JSON descrevem as mesmas coisas — maps aninhados, listas, primitivos — mas fazem um trade-off entre legibilidade e rigidez. YAML é mais amigável para humanos (manifests do Kubernetes, GitHub Actions, OpenAPI, a maioria das configs de CI); JSON é o que APIs e formatos legíveis por máquina entregam. Este conversor faz a troca entre os dois sem perdas para as estruturas que ambos conseguem expressar. YAML usa o <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> (YAML 1.2); JSON usa a API nativa. As duas direções rodam no seu navegador.</p>

<h3>Quando usar</h3>
<ul>
  <li>Colando um YAML de OpenAPI / k8s / docker-compose em uma ferramenta que precisa de JSON.</li>
  <li>Convertendo uma resposta de API (JSON) para YAML para um arquivo de config.</li>
  <li>Auditando a estrutura real de um arquivo YAML quando a indentação ambígua deixa a hierarquia confusa.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>O "Norway problem".</strong> YAML 1.1 coercia <code>NO</code>, <code>YES</code>, <code>ON</code>, <code>OFF</code> em booleans. YAML 1.2 não, mas parsers downstream podem. Coloque aspas em strings ambíguas para garantir.</li>
  <li><strong>YAML multi-documento</strong> (separadores <code>---</code>) — apenas o primeiro documento é convertido.</li>
  <li><strong>Tags customizadas</strong> (<code>!!python/object</code>, <code>!Ref</code>, etc.) violam o YAML 1.2 estrito. YAML do CloudFormation e dumps de pickle do PyYAML vão falhar; limpe as tags antes.</li>
  <li><strong>Anchors e aliases são expandidos</strong> no YAML→JSON. JSON não tem referências, então nodes <code>*ref</code> são inline. Round-tripping dá um YAML equivalente em valor mas textualmente maior.</li>
  <li><strong>Números vs strings.</strong> YAML <code>3.14</code> sem aspas é um float; <code>"3.14"</code> é string.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>YAML i JSON opisują te same rzeczy — zagnieżdżone mapy, listy, prymitywy — ale robią trade-off między czytelnością a ścisłością. YAML jest bardziej przyjazny ludziom (manifesty Kubernetes, GitHub Actions, OpenAPI, większość configów CI); JSON to to, co wysyłają API i formaty czytelne maszynowo. Ten konwerter przerzuca między nimi bezstratnie dla struktur, które oba potrafią wyrazić. YAML używa <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> (YAML 1.2); JSON używa natywnego API. Obie strony działają w przeglądarce.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wklejenie YAML-a OpenAPI / k8s / docker-compose w narzędzie, które potrzebuje JSON-a.</li>
  <li>Konwersja odpowiedzi API (JSON) na YAML do pliku configa.</li>
  <li>Audyt faktycznej struktury pliku YAML, gdy dwuznaczne wcięcie sprawia, że hierarchia jest niejasna.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>"Norway problem".</strong> YAML 1.1 konwertował <code>NO</code>, <code>YES</code>, <code>ON</code>, <code>OFF</code> na boole. YAML 1.2 już nie, ale parsery downstream mogą. Cudzysłowuj dwuznaczne stringi, żeby być bezpiecznym.</li>
  <li><strong>Wielodokumentowy YAML</strong> (separatory <code>---</code>) — konwertowany jest tylko pierwszy dokument.</li>
  <li><strong>Custom tagi</strong> (<code>!!python/object</code>, <code>!Ref</code> itd.) łamią ścisły YAML 1.2. YAML CloudFormation i dumpy pickle z PyYAML padną; najpierw posprzątaj tagi.</li>
  <li><strong>Anchory i aliasy są rozwijane</strong> przy YAML→JSON. JSON nie ma referencji, więc nody <code>*ref</code> są inline. Round-trip daje YAML równoważny wartością, ale tekstowo większy.</li>
  <li><strong>Liczby vs stringi.</strong> Niezacudzysłowione YAML-owe <code>3.14</code> to float; <code>"3.14"</code> to string.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>YAML と JSON は同じものを表現できます（ネストしたマップ、リスト、プリミティブ）が、可読性と厳密さのトレードオフが異なります。YAML は人間に優しく（Kubernetes マニフェスト、GitHub Actions、OpenAPI、多くの CI 設定）、JSON は API や機械可読フォーマットの定番です。本コンバーターは双方が表現可能な構造について、損失なく変換します。YAML には <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a>（YAML 1.2）、JSON にはネイティブ API を使用し、両方向ともブラウザ内で動作します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>OpenAPI / k8s / docker-compose の YAML を、JSON が必要なツールに渡したいとき。</li>
  <li>API レスポンス（JSON）を設定ファイル用に YAML に変換したいとき。</li>
  <li>あいまいなインデントで親子関係が分かりにくい YAML の実構造を確認したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>「ノルウェー問題」。</strong> YAML 1.1 は <code>NO</code>、<code>YES</code>、<code>ON</code>、<code>OFF</code> をブール値に強制変換しました。YAML 1.2 は変換しませんが、下流の古いパーサが変換することがあります。曖昧な文字列は引用しておくのが安全です。</li>
  <li><strong>複数ドキュメント YAML</strong>（<code>---</code> 区切り） — 最初のドキュメントだけが変換されます。</li>
  <li><strong>独自タグ</strong>（<code>!!python/object</code>、<code>!Ref</code> など）は厳格な YAML 1.2 を破ります。CloudFormation の YAML や PyYAML の pickle ダンプは失敗するので、先にタグを整理してください。</li>
  <li><strong>アンカーとエイリアスは展開されます。</strong> JSON には参照がないため、YAML→JSON 時に <code>*ref</code> はインライン化されます。再変換した YAML は値としては等価ですが、テキストが冗長になります。</li>
  <li><strong>数値と文字列。</strong> 引用なしの YAML <code>3.14</code> は float、<code>"3.14"</code> は string です。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>YAML en JSON beschrijven dezelfde dingen — geneste maps, lijsten, primitives — maar wisselen leesbaarheid af tegen strictness. YAML is vriendelijker voor mensen (Kubernetes manifests, GitHub Actions, OpenAPI, de meeste CI-configs); JSON is wat API's en machine-readable formaten shippen. Deze converter flipt tussen beide losslessly voor de structuren die beide kunnen uitdrukken. YAML gebruikt <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> (YAML 1.2); JSON gebruikt de native API. Beide richtingen draaien in je browser.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een OpenAPI / k8s / docker-compose YAML plakken in een tool die JSON nodig heeft.</li>
  <li>Een API-response (JSON) converteren naar YAML voor een config-file.</li>
  <li>De daadwerkelijke structuur van een YAML-file auditen wanneer ambigue indentatie parentage onduidelijk maakt.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Het "Norway-probleem".</strong> YAML 1.1 coerced <code>NO</code>, <code>YES</code>, <code>ON</code>, <code>OFF</code> naar booleans. YAML 1.2 doet dat niet, maar downstream-parsers misschien wel. Quote ambigue strings om veilig te zijn.</li>
  <li><strong>Multi-document YAML</strong> (<code>---</code> separators) — alleen het eerste document wordt geconverteerd.</li>
  <li><strong>Custom tags</strong> (<code>!!python/object</code>, <code>!Ref</code>, enz.) schenden strikte YAML 1.2. CloudFormation YAML en PyYAML pickle-dumps zullen falen; ruim tags eerst op.</li>
  <li><strong>Anchors en aliases worden ge-expandeerd</strong> bij YAML→JSON. JSON heeft geen references, dus <code>*ref</code>-nodes worden inline gezet. Round-trippen geeft een value-equivalente maar textueel-grotere YAML.</li>
  <li><strong>Getallen vs strings.</strong> Unquoted YAML <code>3.14</code> is een float; <code>"3.14"</code> is een string.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>YAML ve JSON aynı şeyleri tanımlar — iç içe map'ler, listeler, primitive'ler — ama okunabilirlik vs katılık değiş tokuş yaparlar. YAML insanlar için daha dostçadır (Kubernetes manifest'leri, GitHub Actions, OpenAPI, çoğu CI config'i); JSON API'lerin ve makine tarafından okunabilir biçimlerin gönderdiği şeydir. Bu dönüştürücü her ikisinin de ifade edebileceği yapılar için kayıpsız olarak aralarında çevirir. YAML <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> kullanır (YAML 1.2); JSON yerel API'yi kullanır. Her iki yön de tarayıcında çalışır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>JSON gerektiren bir araca bir OpenAPI / k8s / docker-compose YAML yapıştırma.</li>
  <li>Bir API yanıtını (JSON) bir config dosyası için YAML'a dönüştürme.</li>
  <li>Belirsiz indent ebeveynliği belirsiz yaptığında bir YAML dosyasının gerçek yapısını denetleme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>"Norveç problemi".</strong> YAML 1.1 <code>NO</code>, <code>YES</code>, <code>ON</code>, <code>OFF</code>'u boolean'a zorladı. YAML 1.2 zorlamaz, ama aşağı akış parser'lar yapabilir. Güvende olmak için belirsiz string'leri tırnakla.</li>
  <li><strong>Çoklu belge YAML</strong> (<code>---</code> ayraçları) — yalnızca ilk belge dönüştürülür.</li>
  <li><strong>Özel tag'ler</strong> (<code>!!python/object</code>, <code>!Ref</code>, vb.) katı YAML 1.2'yi ihlal eder. CloudFormation YAML ve PyYAML pickle dump'ları başarısız olacaktır; önce tag'leri temizle.</li>
  <li><strong>Anchor'lar ve alias'lar YAML→JSON'da genişletilir.</strong> JSON'da referans yoktur, bu yüzden <code>*ref</code> node'ları inline olur. Round-trip değer-eşdeğer ama metinsel olarak daha büyük bir YAML verir.</li>
  <li><strong>Sayılar - string'ler.</strong> Tırnaksız YAML <code>3.14</code> bir float'tır; <code>"3.14"</code> bir string'tir.</li>
</ul>
""",
    },
    "related": ["json-formatter", "json-diff", "csv-to-json"],
    "howto": {"flow": "transform", "action": "convert", "noun": "YAML/JSON"},
}
