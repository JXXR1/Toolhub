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
        "pt": {"name": "Conversor XML ↔ JSON", "tagline": "Converta XML para JSON ou JSON de volta para XML. Lida com attributes, text nodes e arrays de forma sensata.", "description": "Conversor XML para JSON online gratuito (e JSON de volta para XML). Usa o parser XML nativo do navegador; attributes vão para um prefixo configurável; elementos repetidos viram arrays. Roda inteiramente no seu navegador."},
        "pl": {"name": "Konwerter XML ↔ JSON", "tagline": "Konwertuj XML na JSON albo JSON z powrotem na XML. Sensownie obsługuje atrybuty, węzły tekstowe i tablice.", "description": "Darmowy online konwerter XML do JSON (i JSON z powrotem na XML). Używa natywnego parsera XML przeglądarki; atrybuty trafiają z konfigurowalnym prefiksem; powtórzone elementy zwijają się do tablic. Działa w całości w przeglądarce."},
        "ja": {"name": "XML ↔ JSON コンバーター", "tagline": "XML を JSON に、または JSON を XML に変換。属性・テキストノード・配列を妥当に処理。", "description": "オンライン無料の XML → JSON（および JSON → XML）コンバーター。ブラウザの XML パーサを使用し、属性は設定可能なプレフィックス付き、繰り返し要素は配列にまとめます。すべてブラウザ内で動作します。"},
        "nl": {"name": "XML ↔ JSON Converter", "tagline": "Converteer XML naar JSON of JSON terug naar XML. Handelt attributes, text-nodes en arrays verstandig af.", "description": "Gratis online XML-naar-JSON converter (en JSON terug naar XML). Gebruikt de native XML-parser van de browser; attributes krijgen een configureerbaar prefix; herhaalde elementen storten in arrays. Draait volledig in je browser."},
        "tr": {"name": "XML ↔ JSON Dönüştürücü", "tagline": "XML'i JSON'a veya JSON'u XML'e geri dönüştür. Attribute'ları, text node'ları ve dizileri akıllıca işler.", "description": "Ücretsiz online XML'den JSON'a dönüştürücü (ve JSON'dan XML'e geri). Tarayıcının yerel XML parser'ını kullanır; attribute'lar ayarlanabilir bir önek alır; tekrarlayan elementler dizilere indirgenir. Tamamen tarayıcında çalışır."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>XML e JSON são os dois formatos dominantes de troca de dados e você regularmente precisa traduzir entre eles — para migrar de uma API SOAP para uma REST, encanar feeds legados em uma stack moderna, ou simplesmente ler XML em uma ferramenta que só fala JSON. O mapeamento é opinativo, não reversível por padrão, porque XML tem recursos (attributes, conteúdo misto, filhos ordenados) que JSON não tem. Esta ferramenta usa o mapeamento convencional estilo <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a>: attributes ganham um prefixo (default <code>@</code>), text nodes vão para uma chave (default <code>#text</code>) e elementos filhos repetidos viram arrays. As duas direções rodam no seu navegador.</p>

<h3>Quando usar</h3>
<ul>
  <li>Convertendo uma resposta RSS / Atom / SOAP para JSON para consumir num app JS.</li>
  <li>Gerando config XML a partir de um template JSON (configs de build, Spring beans, scaffolds OOXML).</li>
  <li>Extraindo rapidamente valores aninhados — converta XML para JSON, depois use qualquer ferramenta JSON que você já conhece.</li>
  <li>Fazendo round-trip de dados e confirmando que o formato sobrevive à conversão.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Um filho vs array.</strong> Um documento com um <code>&lt;item&gt;</code> vira <code>{"item": {...}}</code>; o mesmo documento com dois vira <code>{"item": [..., ...]}</code>. Os consumidores precisam tratar ambas as formas (ou normalizar na saída).</li>
  <li><strong>Ordem dos elementos não é garantida.</strong> Objetos JSON não preservam ordem de chaves entre todos os parsers/transmissões. Se seu XML tem irmãos cuja ordem é significativa, JSON é o destino errado.</li>
  <li><strong>Conteúdo misto colapsa.</strong> Um elemento como <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> não faz round-trip — texto e elementos inline se entrelaçam de um jeito que não tem representação limpa em objeto.</li>
  <li><strong>Colisões de prefixo de atributo.</strong> Se um elemento XML tem um filho cujo nome começa com <code>@</code>, mude o prefixo para outra coisa antes.</li>
  <li><strong>Namespaces são mantidos literalmente.</strong> <code>ns:tag</code> permanece como a chave JSON <code>"ns:tag"</code>. Atributos <code>xmlns:</code> idem.</li>
  <li><strong>Numbers e booleans não são auto-coercidos.</strong> Texto XML é sempre string; <code>"1"</code> permanece <code>"1"</code> em JSON. Faça a coerção de tipos no código da sua aplicação se precisar.</li>
  <li><strong>JSON → XML exige uma única chave raiz.</strong> XML demanda exatamente um elemento raiz; o JSON de entrada deve ser um objeto com uma única chave de topo.</li>
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
        "pl": """
<h2>Do czego to służy?</h2>
<p>XML i JSON to dwa dominujące formaty wymiany danych i regularnie musisz tłumaczyć między nimi — przy migracji z API SOAP na RESTowe, podpinaniu starych feedów do nowoczesnego stacka albo po prostu czytaniu XML-a w narzędziu, które mówi tylko po JSON-owemu. Mapowanie jest opiniotwórcze, nie odwracalne by-default, bo XML ma ficzery (atrybuty, mixed content, uporządkowane dzieci), których JSON nie ma. To narzędzie używa konwencjonalnego mapowania w stylu <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a>: atrybuty dostają prefiks (domyślnie <code>@</code>), węzły tekstowe trafiają pod klucz (domyślnie <code>#text</code>), a powtórzone elementy potomne zwijają się do tablic. Obie strony działają w przeglądarce.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Konwersja odpowiedzi RSS / Atom / SOAP na JSON do konsumpcji w apce JS.</li>
  <li>Generowanie XML configa z szablonu JSON (configi buildowe, beany Springa, scaffoldy OOXML).</li>
  <li>Szybkie wyciąganie zagnieżdżonych wartości — przekonwertuj XML na JSON, potem użyj dowolnego narzędzia JSON-owego, które już znasz.</li>
  <li>Round-trip danych i potwierdzenie, że kształt przeżywa konwersję.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Pojedyncze dziecko vs tablica.</strong> Dokument z jednym <code>&lt;item&gt;</code> staje się <code>{"item": {...}}</code>; ten sam dokument z dwoma — <code>{"item": [..., ...]}</code>. Konsumenci muszą obsłużyć obie formy (albo znormalizować na wyjściu).</li>
  <li><strong>Kolejność elementów nie jest gwarantowana.</strong> Obiekty JSON nie zachowują kolejności kluczy w sposób spójny we wszystkich parserach/transmisjach. Jeśli twój XML ma rodzeństwo o znaczącej kolejności — JSON to zła destynacja.</li>
  <li><strong>Mixed content się składa.</strong> Element typu <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> nie robi round-tripu — tekst i inline'owe elementy przeplatają się w sposób, który nie ma czystej reprezentacji obiektowej.</li>
  <li><strong>Kolizje prefiksu atrybutów.</strong> Jeśli element XML ma dziecko, którego nazwa zaczyna się od <code>@</code>, najpierw zmień prefiks na coś innego.</li>
  <li><strong>Namespace'y są trzymane dosłownie.</strong> <code>ns:tag</code> zostaje jako klucz JSON <code>"ns:tag"</code>. Atrybuty <code>xmlns:</code> tak samo.</li>
  <li><strong>Liczby i boole nie są auto-konwertowane.</strong> Tekst XML zawsze jest stringiem; <code>"1"</code> zostaje <code>"1"</code> w JSON. Konwertuj typy w kodzie aplikacji, jeśli ich potrzebujesz.</li>
  <li><strong>JSON → XML wymaga jednego klucza root.</strong> XML wymaga dokładnie jednego elementu root; wejściowy JSON musi być obiektem z jednym kluczem na top-level.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>XML と JSON は二大データ交換形式で、SOAP API から REST への移行、レガシーフィードのモダンスタックへの取り込み、JSON しか扱えないツールでの XML 閲覧など、相互変換は日常です。マッピングは標準化されておらず慣例的です（XML の属性、混在コンテンツ、順序付き子要素は JSON にそのまま対応する概念がないため）。本ツールは <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a> 風のマッピングを採用します。属性はプレフィックス付き（既定 <code>@</code>）、テキストノードは固定キー（既定 <code>#text</code>）、繰り返しの子要素は配列にまとめます。両方向ともブラウザ内で動作します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>RSS / Atom / SOAP のレスポンスを JS アプリで使えるよう JSON に変換するとき。</li>
  <li>JSON テンプレートから XML 設定（ビルド設定、Spring Bean、OOXML 雛形）を生成するとき。</li>
  <li>ネストされた値を素早く取り出したい — XML を JSON に変換してから、JSON 用の好みのツールで処理。</li>
  <li>変換でデータ形状が壊れないかラウンドトリップを確認したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>子要素 1 つと配列で形が変わります。</strong> <code>&lt;item&gt;</code> が 1 個なら <code>{"item": {...}}</code>、2 個以上なら <code>{"item": [..., ...]}</code> になります。コンシューマは両方の形を扱うか、出力時に正規化してください。</li>
  <li><strong>要素の順序は保証されません。</strong> JSON のキー順はパーサや伝送経路で必ずしも保たれません。順序が意味を持つ XML の兄弟要素には JSON は不向きです。</li>
  <li><strong>混在コンテンツは潰れます。</strong> <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> のようなテキストとインライン要素の織り交ぜは綺麗にラウンドトリップしません。</li>
  <li><strong>属性プレフィックスの衝突。</strong> 子要素名が <code>@</code> から始まる場合、属性プレフィックスを別の文字に変更してください。</li>
  <li><strong>名前空間はそのまま保持。</strong> <code>ns:tag</code> は JSON キーでも <code>"ns:tag"</code>。<code>xmlns:</code> 属性も同様です。</li>
  <li><strong>数値や真偽値の自動変換は行いません。</strong> XML テキストは常に文字列であり、<code>"1"</code> は JSON でも <code>"1"</code> のまま。必要ならアプリ側で型変換してください。</li>
  <li><strong>JSON → XML には単一ルートキーが必要。</strong> XML はルート要素がちょうど 1 つ必要です。入力 JSON はトップレベルにキーが 1 つだけのオブジェクトでなければなりません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>XML en JSON zijn de twee dominante data-interchange formaten en je moet regelmatig tussen ze vertalen — om van een SOAP API naar een REST over te stappen, legacy feeds in een moderne stack te plumbing, of gewoon XML te lezen in een tool die alleen JSON spreekt. De mapping heeft een mening in plaats van reversible-by-default, omdat XML features heeft (attributes, mixed content, ordered children) die JSON niet heeft. Deze tool gebruikt de conventionele <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a>-stijl mapping: attributes krijgen een prefix (default <code>@</code>), text-nodes gaan naar een key (default <code>#text</code>), en herhaalde child-elementen storten in arrays. Beide richtingen draaien in je browser.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een RSS / Atom / SOAP-response converteren naar JSON om in een JS-app te consumeren.</li>
  <li>XML-config genereren uit een JSON-template (build configs, Spring beans, OOXML scaffolds).</li>
  <li>Snel geneste values extraheren — converteer XML naar JSON, gebruik dan elke JSON-tool die je al kent.</li>
  <li>Data round-trippen en bevestigen dat de vorm de conversie overleeft.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Single child vs array.</strong> Een document met één <code>&lt;item&gt;</code> wordt <code>{"item": {...}}</code>; hetzelfde document met twee wordt <code>{"item": [..., ...]}</code>. Consumers moeten beide vormen afhandelen (of normaliseren op de weg uit).</li>
  <li><strong>Element-volgorde wordt niet gegarandeerd.</strong> JSON-objects behouden key-volgorde niet over alle parsers/transmissies. Als je XML order-significante siblings heeft, is JSON de verkeerde bestemming.</li>
  <li><strong>Mixed content stort in.</strong> Een element als <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> round-trippt niet — text en inline-elementen interleaven op een manier die geen schone object-representatie heeft.</li>
  <li><strong>Attribute-prefix collisions.</strong> Als een XML-element een child heeft wiens naam met <code>@</code> begint, verander het prefix eerst naar iets anders.</li>
  <li><strong>Namespaces blijven letterlijk behouden.</strong> <code>ns:tag</code> blijft als JSON-key <code>"ns:tag"</code>. <code>xmlns:</code>-attributes idem.</li>
  <li><strong>Getallen en booleans worden niet auto-gecoerced.</strong> XML-text is altijd strings; <code>"1"</code> blijft <code>"1"</code> in JSON. Coerce types in je applicatiecode als je ze nodig hebt.</li>
  <li><strong>JSON → XML vereist één root-key.</strong> XML eist precies één root-element; de input-JSON moet een object zijn met één top-level key.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>XML ve JSON iki baskın veri değişim biçimidir ve düzenli olarak aralarında çeviri yapman gerekir — bir SOAP API'den REST'e geçiş, eski feed'leri modern bir yığına bağlama veya sadece JSON konuşan bir araçta XML okuma. Eşleme tarafsız değildir, varsayılan olarak tersinir değildir, çünkü XML JSON'da olmayan özelliklere (nitelikler, karışık içerik, sıralı child'lar) sahiptir. Bu araç geleneksel <a href="https://www.npmjs.com/package/fast-xml-parser" target="_blank" rel="noopener noreferrer">fast-xml-parser</a>-stili eşlemeyi kullanır: nitelikler bir önek alır (varsayılan <code>@</code>), text node'ları bir anahtara gider (varsayılan <code>#text</code>) ve tekrarlanan child elementler array'lere çöker. Her iki yön de tarayıcında çalışır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir RSS / Atom / SOAP yanıtını bir JS uygulamasında tüketmek için JSON'a dönüştürme.</li>
  <li>Bir JSON template'tan XML config üretme (build config'leri, Spring bean'leri, OOXML scaffold'lar).</li>
  <li>İç içe değerleri hızlıca çıkarma — XML'i JSON'a dönüştür, sonra bildiğin herhangi bir JSON aracını kullan.</li>
  <li>Veriyi round-trip yapma ve şeklin dönüşümden sağ çıktığını doğrulama.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Tek child - array.</strong> Bir <code>&lt;item&gt;</code> olan bir belge <code>{"item": {...}}</code> olur; iki olan aynı belge <code>{"item": [..., ...]}</code> olur. Tüketicilerin her iki şekli de işlemesi gerekir.</li>
  <li><strong>Element sırası garanti edilmez.</strong> JSON nesneleri tüm parser'lar/iletim'ler arasında anahtar sırasını korumaz. XML'in sıra-anlamlı kardeşleri varsa, JSON yanlış hedeftir.</li>
  <li><strong>Karışık içerik çöker.</strong> <code>&lt;p&gt;hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;</code> gibi bir element round-trip yapmaz — metin ve inline elementler temiz bir nesne temsiline sahip olmayan bir şekilde iç içe geçer.</li>
  <li><strong>Nitelik öneki çakışmaları.</strong> Bir XML elementinin adı <code>@</code> ile başlayan bir child'ı varsa, önce öneki başka bir şeye değiştir.</li>
  <li><strong>Namespace'ler aynen korunur.</strong> <code>ns:tag</code> JSON anahtarı olarak <code>"ns:tag"</code> kalır. <code>xmlns:</code> nitelikleri de benzer şekilde.</li>
  <li><strong>Sayılar ve boolean'lar otomatik dönüştürülmez.</strong> XML metni her zaman string'tir; <code>"1"</code> JSON'da <code>"1"</code> kalır. İhtiyacın varsa uygulama kodunda türleri dönüştür.</li>
  <li><strong>JSON → XML tek bir kök anahtar gerektirir.</strong> XML tam olarak bir kök element ister; giriş JSON tek bir üst seviye anahtarı olan bir nesne olmalıdır.</li>
</ul>
""",
    },
    "related": ["xml-formatter", "json-formatter", "yaml-json", "csv-to-json"],
    "howto": {"flow": "transform", "action": "convert", "noun": "XML"},
}
