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
    },
    "related": ["url-encoder", "query-string-builder", "jwt-decoder", "base64-encoder"],
}
