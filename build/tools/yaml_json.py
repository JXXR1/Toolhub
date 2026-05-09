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
    },
    "related": ["json-formatter", "json-diff", "csv-to-json"],
}
