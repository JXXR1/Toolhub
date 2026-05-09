TOOL = {
    "slug": "xml-to-json",
    "category": "data",
    "icon": "⇄",
    "tags": ["xml", "json", "convert", "transform", "attributes", "data"],
    "i18n": {
        "en": {
            "name": "XML ↔ JSON Converter",
            "tagline": "Convert XML to JSON or JSON back to XML. Handles attributes, text nodes, and arrays sensibly.",
            "description": "Free online XML to JSON converter (and JSON back to XML). Uses the browser's native XML parser; attributes go to a configurable prefix; repeated elements collapse to arrays. Runs entirely in your browser.",
        },
        "de": {"name": "XML ↔ JSON Konverter", "tagline": "XML in JSON konvertieren oder JSON zurück in XML. Verarbeitet Attribute, Textknoten und Arrays sinnvoll.", "description": "Kostenloser XML-zu-JSON-Konverter (und JSON zurück zu XML). Verwendet den XML-Parser des Browsers; Attribute mit konfigurierbarem Präfix; wiederholte Elemente werden zu Arrays. Komplett im Browser."},
        "es": {"name": "Conversor XML ↔ JSON", "tagline": "Convierte XML a JSON o JSON de vuelta a XML. Maneja atributos, nodos de texto y arrays correctamente.", "description": "Conversor XML a JSON gratuito (y JSON de vuelta a XML). Usa el parser XML del navegador; los atributos van con prefijo configurable; los elementos repetidos se vuelven arrays. 100% en el navegador."},
        "fr": {"name": "Convertisseur XML ↔ JSON", "tagline": "Convertissez XML en JSON ou JSON en XML. Gère attributs, nœuds texte et tableaux intelligemment.", "description": "Convertisseur XML vers JSON gratuit (et JSON vers XML). Utilise le parser XML du navigateur ; attributs avec préfixe configurable ; éléments répétés deviennent des tableaux. 100% dans le navigateur."},
        "it": {"name": "Convertitore XML ↔ JSON", "tagline": "Converti XML in JSON o JSON in XML. Gestisce attributi, nodi testo e array sensibilmente.", "description": "Convertitore XML a JSON gratuito (e JSON a XML). Usa il parser XML del browser; attributi con prefisso configurabile; elementi ripetuti diventano array. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Direction</label>
      <select id="xj-dir" onchange="xjRun()">
        <option value="x2j" selected>XML → JSON</option>
        <option value="j2x">JSON → XML</option>
      </select>
    </div>
    <div>
      <label>Attribute prefix</label>
      <input type="text" id="xj-attr" value="@" oninput="xjRun()" maxlength="3" style="font-family:ui-monospace,monospace">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Text node key</label>
      <input type="text" id="xj-text" value="#text" oninput="xjRun()" maxlength="8" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>Indent</label>
      <select id="xj-indent" onchange="xjRun()">
        <option value="2" selected>2 spaces</option>
        <option value="4">4 spaces</option>
        <option value="0">None</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="xj-in" oninput="xjRun()" spellcheck="false" placeholder="<library><book id=&quot;1&quot;>...</book></library>" style="min-height:160px"><library><book id="1" lang="en"><title>The Pragmatic Programmer</title><author>Andy Hunt</author></book><book id="2" lang="en"><title>Clean Code</title><author>Robert Martin</author></book></library></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="xj-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('xj-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function xjElToObj(el, opts){
  const obj = {};
  // attributes
  for(const a of el.attributes || []){
    obj[opts.attrPrefix + a.name] = a.value;
  }
  const children = Array.from(el.childNodes);
  const elementChildren = children.filter(c => c.nodeType === 1);
  const textChildren = children.filter(c => c.nodeType === 3 || c.nodeType === 4);
  const text = textChildren.map(c => c.nodeValue).join('').trim();

  if(elementChildren.length === 0 && Object.keys(obj).length === 0){
    return text;
  }
  if(elementChildren.length === 0){
    if(text !== '') obj[opts.textKey] = text;
    return obj;
  }

  // Group children by tagName
  const byTag = {};
  for(const child of elementChildren){
    const name = child.nodeName;
    const val = xjElToObj(child, opts);
    if(byTag[name] === undefined) byTag[name] = val;
    else if(Array.isArray(byTag[name])) byTag[name].push(val);
    else byTag[name] = [byTag[name], val];
  }
  Object.assign(obj, byTag);
  if(text !== '') obj[opts.textKey] = text;
  return obj;
}

function xjXmlToJson(xml, opts){
  const dom = new DOMParser().parseFromString(xml, 'application/xml');
  const err = dom.querySelector('parsererror');
  if(err) throw new Error('XML parse error: ' + (err.textContent || '').trim().split('\\n')[0]);
  const root = dom.documentElement;
  return { [root.nodeName]: xjElToObj(root, opts) };
}

function xjEscAttr(v){
  return String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
}
function xjEscText(v){
  return String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function xjValidName(s){
  return /^[A-Za-z_][\\w\\-.]*$/.test(s);
}

function xjObjToXml(name, val, opts, depth){
  const ind = opts.indent ? '  '.repeat(depth) : '';
  const nl = opts.indent ? '\\n' : '';
  if(!xjValidName(name)) throw new Error('Invalid XML element name: ' + name);
  if(val === null || val === undefined){ return ind + '<' + name + '/>' + nl; }
  if(typeof val !== 'object'){
    return ind + '<' + name + '>' + xjEscText(val) + '</' + name + '>' + nl;
  }
  if(Array.isArray(val)){
    return val.map(v => xjObjToXml(name, v, opts, depth)).join('');
  }
  // object with attrs / children
  const attrs = [];
  const children = [];
  let textVal = null;
  for(const k of Object.keys(val)){
    if(k.startsWith(opts.attrPrefix) && opts.attrPrefix){
      const an = k.slice(opts.attrPrefix.length);
      if(!xjValidName(an)) throw new Error('Invalid XML attribute name: ' + an);
      attrs.push(an + '="' + xjEscAttr(val[k]) + '"');
    } else if(k === opts.textKey){
      textVal = val[k];
    } else {
      children.push([k, val[k]]);
    }
  }
  const attrStr = attrs.length ? ' ' + attrs.join(' ') : '';
  if(children.length === 0 && textVal === null){
    return ind + '<' + name + attrStr + '/>' + nl;
  }
  if(children.length === 0){
    return ind + '<' + name + attrStr + '>' + xjEscText(textVal) + '</' + name + '>' + nl;
  }
  let out = ind + '<' + name + attrStr + '>' + nl;
  for(const [k,v] of children){ out += xjObjToXml(k, v, opts, depth+1); }
  if(textVal !== null && textVal !== '') out += (opts.indent ? '  '.repeat(depth+1) : '') + xjEscText(textVal) + nl;
  out += ind + '</' + name + '>' + nl;
  return out;
}

function xjJsonToXml(json, opts){
  const obj = JSON.parse(json);
  if(typeof obj !== 'object' || obj === null) throw new Error('JSON must be an object with one root key');
  const keys = Object.keys(obj);
  if(keys.length !== 1) throw new Error('JSON must have exactly one root key (got ' + keys.length + ')');
  const root = keys[0];
  return xjObjToXml(root, obj[root], opts, 0).trim();
}

function xjRun(){
  const dir = document.getElementById('xj-dir').value;
  const attr = document.getElementById('xj-attr').value || '@';
  const textKey = document.getElementById('xj-text').value || '#text';
  const indentChoice = parseInt(document.getElementById('xj-indent').value, 10);
  const inp = document.getElementById('xj-in').value;
  const out = document.getElementById('xj-out');
  out.classList.remove('error');
  if(!inp.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    if(dir === 'x2j'){
      const obj = xjXmlToJson(inp, {attrPrefix: attr, textKey});
      out.textContent = JSON.stringify(obj, null, indentChoice);
    } else {
      out.textContent = xjJsonToXml(inp, {attrPrefix: attr, textKey, indent: indentChoice > 0});
    }
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + e.message;
  }
}
document.addEventListener('DOMContentLoaded', xjRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>XML and JSON are the two dominant data interchange formats and you regularly need to translate between them — for migrating from a SOAP API to a REST one, plumbing legacy feeds into a modern stack, or just reading XML in a tool that only speaks JSON. The mapping is opinionated rather than reversible-by-default, because XML has features (attributes, mixed content, ordered children) that JSON doesn't. This tool uses the conventional <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a>-style mapping: attributes get a prefix (default <code>@</code>), text nodes go to a key (default <code>#text</code>), and repeated child elements collapse to arrays. Both directions run in your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Converting an RSS / Atom / SOAP response into JSON to consume in a JS app.</li>
  <li>Generating XML config from a JSON template (build configs, Spring beans, OOXML scaffolds).</li>
  <li>Quickly extracting nested values — convert XML to JSON, then use any JSON tool you already know.</li>
  <li>Round-tripping data and confirming the shape survives the conversion.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Single child vs array.</strong> A document with one <code>&lt;item&gt;</code> becomes <code>{"item": {...}}</code>; the same document with two becomes <code>{"item": [..., ...]}</code>. Consumers must handle both shapes (or normalise on the way out).</li>
  <li><strong>Element order is not guaranteed.</strong> JSON objects don't preserve key order across all parsers/transmissions. If your XML has order-significant siblings, JSON is the wrong destination.</li>
  <li><strong>Mixed content collapses.</strong> An element like <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> doesn't round-trip — text and inline elements interleave in a way that has no clean object representation.</li>
  <li><strong>Attribute prefix collisions.</strong> If an XML element has a child whose name starts with <code>@</code>, change the prefix to something else first.</li>
  <li><strong>Namespaces are kept verbatim.</strong> <code>ns:tag</code> stays as the JSON key <code>"ns:tag"</code>. <code>xmlns:</code> attributes likewise.</li>
  <li><strong>Numbers and booleans aren't auto-coerced.</strong> XML text is always strings; <code>"1"</code> stays <code>"1"</code> in JSON. Coerce types in your application code if you need them.</li>
  <li><strong>JSON → XML requires a single root key.</strong> XML demands exactly one root element; the input JSON must be an object with one top-level key.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>XML und JSON sind die zwei dominanten Austauschformate und Übersetzung zwischen ihnen ist Alltag. Das Mapping ist konventionell, nicht standardisiert: Attribute erhalten ein Präfix (Standard <code>@</code>), Textknoten einen Schlüssel (Standard <code>#text</code>), wiederholte Kindelemente werden zu Arrays. Beide Richtungen im Browser.</p>
<h3>Wann verwenden</h3>
<ul>
<li>RSS/Atom/SOAP in JSON umwandeln für JS-Apps.</li>
<li>XML-Config aus JSON-Template generieren.</li>
<li>Verschachtelte Werte einfacher extrahieren.</li>
<li>Round-Trip prüfen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Eines vs Array.</strong> Ein <code>&lt;item&gt;</code> wird Objekt, zwei werden Array — Konsumenten müssen beide Formen handhaben.</li>
<li><strong>Element-Reihenfolge nicht garantiert.</strong> JSON-Objekt-Schlüssel sind nicht zwingend geordnet.</li>
<li><strong>Mixed Content kollabiert.</strong> <code>&lt;p&gt;hi &lt;b&gt;welt&lt;/b&gt;!&lt;/p&gt;</code> trippt nicht round-trip.</li>
<li><strong>Präfix-Kollisionen.</strong> Wenn Tag-Name mit <code>@</code> beginnt, anderes Präfix wählen.</li>
<li><strong>Namespaces wörtlich.</strong> <code>ns:tag</code> bleibt <code>"ns:tag"</code>.</li>
<li><strong>Keine Typ-Inferenz.</strong> XML-Text ist immer String.</li>
<li><strong>JSON → XML braucht genau einen Root-Key.</strong></li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>XML y JSON son los dos formatos dominantes y traducir entre ellos es habitual. El mapeo es convencional: atributos con prefijo (<code>@</code>), nodos de texto con clave (<code>#text</code>), elementos hijos repetidos se vuelven arrays. Ambas direcciones en el navegador.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Convertir RSS/Atom/SOAP a JSON para apps JS.</li>
<li>Generar XML config desde plantillas JSON.</li>
<li>Extraer valores anidados más fácil.</li>
<li>Verificar round-trip.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Único vs array.</strong> Un <code>&lt;item&gt;</code> es objeto, dos son array — los consumidores deben manejar ambas formas.</li>
<li><strong>Orden no garantizado.</strong> Las claves JSON no preservan orden de manera fiable.</li>
<li><strong>Contenido mixto colapsa.</strong> No hace round-trip limpio.</li>
<li><strong>Colisiones de prefijo.</strong> Si una etiqueta empieza con <code>@</code>, cambia el prefijo.</li>
<li><strong>Namespaces literales.</strong> <code>ns:tag</code> permanece como <code>"ns:tag"</code>.</li>
<li><strong>Sin inferencia de tipos.</strong> El texto XML siempre es string.</li>
<li><strong>JSON → XML necesita exactamente una clave raíz.</strong></li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>XML et JSON sont les deux formats dominants et traduire entre eux est quotidien. Le mapping est conventionnel : attributs avec préfixe (<code>@</code>), nœuds texte avec clé (<code>#text</code>), enfants répétés en tableaux. Les deux directions dans le navigateur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Convertir RSS/Atom/SOAP en JSON pour apps JS.</li>
<li>Générer XML config depuis un template JSON.</li>
<li>Extraire valeurs imbriquées plus facilement.</li>
<li>Vérifier round-trip.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Un seul vs tableau.</strong> Un <code>&lt;item&gt;</code> est objet, deux deviennent tableau — gérer les deux formes côté consommateur.</li>
<li><strong>Ordre non garanti.</strong> Les clés JSON ne préservent pas l'ordre de manière fiable.</li>
<li><strong>Le contenu mixte s'effondre.</strong> Pas de round-trip propre.</li>
<li><strong>Collisions de préfixe.</strong> Si une balise commence par <code>@</code>, changer le préfixe.</li>
<li><strong>Namespaces littéraux.</strong> <code>ns:tag</code> reste <code>"ns:tag"</code>.</li>
<li><strong>Pas d'inférence de type.</strong> Le texte XML est toujours string.</li>
<li><strong>JSON → XML exige exactement une clé racine.</strong></li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>XML e JSON sono i due formati dominanti e tradurre tra loro è quotidiano. La mappatura è convenzionale: attributi con prefisso (<code>@</code>), nodi testo con chiave (<code>#text</code>), figli ripetuti diventano array. Entrambe le direzioni nel browser.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Convertire RSS/Atom/SOAP in JSON per app JS.</li>
<li>Generare XML config da template JSON.</li>
<li>Estrarre valori annidati più facilmente.</li>
<li>Verificare round-trip.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Singolo vs array.</strong> Un <code>&lt;item&gt;</code> è oggetto, due diventano array — gestire entrambe le forme.</li>
<li><strong>Ordine non garantito.</strong> Le chiavi JSON non preservano l'ordine in modo affidabile.</li>
<li><strong>Contenuto misto collassa.</strong> Nessun round-trip pulito.</li>
<li><strong>Collisioni di prefisso.</strong> Se un tag inizia con <code>@</code>, cambia prefisso.</li>
<li><strong>Namespace letterali.</strong> <code>ns:tag</code> resta <code>"ns:tag"</code>.</li>
<li><strong>Niente inferenza di tipo.</strong> Il testo XML è sempre stringa.</li>
<li><strong>JSON → XML richiede esattamente una chiave radice.</strong></li>
</ul>
""",
    },
    "related": ["xml-formatter", "json-formatter", "yaml-json", "csv-to-json"],
}
