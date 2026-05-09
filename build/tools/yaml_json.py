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
    },
    "related": ["json-formatter", "json-diff", "csv-to-json"],
}
