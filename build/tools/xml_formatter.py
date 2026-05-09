TOOL = {
    "slug": "xml-formatter",
    "category": "developer",
    "icon": "&lt;/&gt;",
    "tags": ["xml", "format", "beautify", "minify", "validate", "well-formed"],
    "i18n": {
        "en": {
            "name": "XML Formatter",
            "tagline": "Format and minify XML. Validate well-formedness with line and column on errors.",
            "description": "Free online XML formatter and minifier. Pretty-print XML with configurable indent, or strip whitespace to minify. Validates well-formedness using the browser's XML parser — error line and column shown.",
        },
        "de": {"name": "XML-Formatierer", "tagline": "XML formatieren und minimieren. Wohlgeformtheit prüfen mit Zeile und Spalte bei Fehlern.", "description": "Kostenloser XML-Formatierer und -Minifizierer. Pretty-Print mit konfigurierbarer Einrückung oder Whitespace strippen. Prüft Wohlgeformtheit mit dem XML-Parser des Browsers — Zeile und Spalte bei Fehlern."},
        "es": {"name": "Formateador XML", "tagline": "Formatea y minimiza XML. Valida la buena forma con línea y columna en errores.", "description": "Formateador y minimizador XML gratuito. Pretty-print con sangría configurable o sin espacios. Valida buena forma con el parser XML del navegador — línea y columna en errores."},
        "fr": {"name": "Formateur XML", "tagline": "Formatez et minifiez du XML. Validez la bien-formation avec ligne et colonne en cas d'erreur.", "description": "Formateur et minifieur XML gratuit. Pretty-print avec indentation configurable ou suppression des espaces. Valide la bien-formation avec le parseur XML du navigateur — ligne et colonne en cas d'erreur."},
        "it": {"name": "Formattatore XML", "tagline": "Formatta e minifica XML. Valida la ben-formattezza con riga e colonna in caso di errori.", "description": "Formattatore e minificatore XML gratuito. Pretty-print con indentazione configurabile o rimozione spazi. Valida la ben-formattezza con il parser XML del browser — riga e colonna in caso di errori."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="xf-in" oninput="xfRun()" placeholder="<root><item id=&quot;1&quot;>hello</item></root>" spellcheck="false" style="min-height:180px"><root><item id="1">hello</item><item id="2"><nested>world</nested></item></root></textarea>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="xf-mode" onchange="xfRun()">
        <option value="pretty" selected>Pretty-print (indent)</option>
        <option value="minify">Minify (strip whitespace)</option>
      </select>
    </div>
    <div>
      <label>Indent</label>
      <select id="xf-indent" onchange="xfRun()">
        <option value="2" selected>2 spaces</option>
        <option value="4">4 spaces</option>
        <option value="tab">Tab</option>
      </select>
    </div>
  </div>
  <div class="meta" id="xf-status" style="margin-top:0.6rem;font-family:ui-monospace,monospace;font-size:0.82rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="xf-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('xf-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<style>
.xf-ok{color:#3fb950}
.xf-err{color:#f85149}
</style>
<script>
function xfEsc(s){ return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function xfParseError(xmlString){
  // Parse via DOMParser; check for parsererror element
  const dom = new DOMParser().parseFromString(xmlString, 'application/xml');
  const errEl = dom.querySelector('parsererror');
  if(!errEl) return {ok: true, dom};
  // Try to extract line/column from message text
  const msg = errEl.textContent || 'Parse error';
  // Firefox: "Line Number 3, Column 7:"
  // Chrome: "error on line 3 at column 7"
  let line = null, col = null;
  let m = msg.match(/[Ll]ine\\s*(?:[Nn]umber\\s*)?:?\\s*(\\d+)/);
  if(m) line = parseInt(m[1], 10);
  m = msg.match(/[Cc]olumn\\s*:?\\s*(\\d+)/);
  if(m) col = parseInt(m[1], 10);
  return {ok: false, msg: msg.trim().split('\\n')[0], line, col};
}
function xfFormat(node, depth, indent, lines){
  const pad = indent.repeat(depth);
  if(node.nodeType === Node.DOCUMENT_NODE){
    // XML declaration handling: DOMParser strips it; we'll prepend if input had one — caller does that.
    for(const child of node.childNodes) xfFormat(child, depth, indent, lines);
    return;
  }
  if(node.nodeType === Node.ELEMENT_NODE){
    const name = node.nodeName;
    const attrs = Array.from(node.attributes).map(a => `${a.name}="${xfEscAttr(a.value)}"`).join(' ');
    const open = `<${name}${attrs ? ' ' + attrs : ''}`;
    const children = Array.from(node.childNodes);
    // Self-closing if no children
    if(children.length === 0){
      lines.push(pad + open + '/>');
      return;
    }
    // Single text child (no element children) — keep on one line
    const allText = children.every(c => c.nodeType === Node.TEXT_NODE || c.nodeType === Node.CDATA_SECTION_NODE);
    if(allText){
      const textContent = children.map(c => {
        if(c.nodeType === Node.CDATA_SECTION_NODE) return '<![CDATA[' + c.nodeValue + ']]>';
        return xfEsc(c.nodeValue);
      }).join('');
      const trimmed = textContent.replace(/^\\s+|\\s+$/g,'');
      if(trimmed === ''){
        lines.push(pad + open + '/>');
      } else {
        lines.push(pad + open + '>' + trimmed + '</' + name + '>');
      }
      return;
    }
    // Mixed / element children — block form
    lines.push(pad + open + '>');
    for(const child of children){
      if(child.nodeType === Node.TEXT_NODE){
        const t = (child.nodeValue || '').replace(/^\\s+|\\s+$/g,'');
        if(t !== '') lines.push(indent.repeat(depth+1) + xfEsc(t));
      } else if(child.nodeType === Node.CDATA_SECTION_NODE){
        lines.push(indent.repeat(depth+1) + '<![CDATA[' + child.nodeValue + ']]>');
      } else if(child.nodeType === Node.COMMENT_NODE){
        lines.push(indent.repeat(depth+1) + '<!--' + child.nodeValue + '-->');
      } else if(child.nodeType === Node.PROCESSING_INSTRUCTION_NODE){
        lines.push(indent.repeat(depth+1) + '<?' + child.target + ' ' + child.data + '?>');
      } else {
        xfFormat(child, depth+1, indent, lines);
      }
    }
    lines.push(pad + '</' + name + '>');
    return;
  }
  if(node.nodeType === Node.COMMENT_NODE){
    lines.push(pad + '<!--' + node.nodeValue + '-->');
    return;
  }
  if(node.nodeType === Node.PROCESSING_INSTRUCTION_NODE){
    lines.push(pad + '<?' + node.target + ' ' + node.data + '?>');
    return;
  }
  if(node.nodeType === Node.TEXT_NODE){
    const t = (node.nodeValue || '').replace(/^\\s+|\\s+$/g,'');
    if(t !== '') lines.push(pad + xfEsc(t));
  }
}
function xfEscAttr(v){
  return String(v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;').replace(/\\n/g,'&#10;').replace(/\\r/g,'&#13;');
}
function xfMinify(node, parts){
  if(node.nodeType === Node.DOCUMENT_NODE){
    for(const child of node.childNodes) xfMinify(child, parts);
    return;
  }
  if(node.nodeType === Node.ELEMENT_NODE){
    const name = node.nodeName;
    const attrs = Array.from(node.attributes).map(a => `${a.name}="${xfEscAttr(a.value)}"`).join(' ');
    const open = `<${name}${attrs ? ' ' + attrs : ''}`;
    const children = Array.from(node.childNodes);
    if(children.length === 0){ parts.push(open + '/>'); return; }
    parts.push(open + '>');
    for(const child of children){
      if(child.nodeType === Node.TEXT_NODE){
        const t = (child.nodeValue || '').replace(/^\\s+|\\s+$/g,'');
        if(t !== '') parts.push(xfEsc(t));
      } else if(child.nodeType === Node.CDATA_SECTION_NODE){
        parts.push('<![CDATA[' + child.nodeValue + ']]>');
      } else if(child.nodeType === Node.COMMENT_NODE){
        parts.push('<!--' + child.nodeValue + '-->');
      } else if(child.nodeType === Node.PROCESSING_INSTRUCTION_NODE){
        parts.push('<?' + child.target + ' ' + child.data + '?>');
      } else {
        xfMinify(child, parts);
      }
    }
    parts.push('</' + name + '>');
  }
}
function xfRun(){
  const inp = document.getElementById('xf-in').value;
  const out = document.getElementById('xf-out');
  const status = document.getElementById('xf-status');
  if(inp.trim() === ''){ out.classList.remove('error'); out.textContent = '{LBL_NO_INPUT}'; status.textContent = ''; return; }
  const parsed = xfParseError(inp);
  if(!parsed.ok){
    out.classList.add('error');
    let posStr = '';
    if(parsed.line !== null) posStr = ` at line ${parsed.line}` + (parsed.col !== null ? `, column ${parsed.col}` : '');
    out.textContent = '✗ Not well-formed XML' + posStr + '\\n\\n' + parsed.msg;
    status.innerHTML = '<span class="xf-err">✗ Parse error</span>';
    return;
  }
  out.classList.remove('error');
  const mode = document.getElementById('xf-mode').value;
  const indentChoice = document.getElementById('xf-indent').value;
  const indent = indentChoice === 'tab' ? '\\t' : ' '.repeat(parseInt(indentChoice, 10));
  // Preserve XML declaration if it existed
  const declMatch = inp.match(/^\\s*(<\\?xml[^?]*\\?>)/);
  const decl = declMatch ? declMatch[1] : '';
  if(mode === 'pretty'){
    const lines = [];
    xfFormat(parsed.dom, 0, indent, lines);
    let result = lines.join('\\n');
    if(decl) result = decl + '\\n' + result;
    out.textContent = result;
    const inSize = new Blob([inp]).size;
    const outSize = new Blob([result]).size;
    status.innerHTML = `<span class="xf-ok">✓ Well-formed</span> · ${inSize.toLocaleString()} → ${outSize.toLocaleString()} bytes`;
  } else {
    const parts = [];
    xfMinify(parsed.dom, parts);
    let result = parts.join('');
    if(decl) result = decl + result;
    out.textContent = result;
    const inSize = new Blob([inp]).size;
    const outSize = new Blob([result]).size;
    const saving = inSize ? Math.max(0, Math.round((1 - outSize/inSize) * 100)) : 0;
    status.innerHTML = `<span class="xf-ok">✓ Well-formed</span> · ${inSize.toLocaleString()} → ${outSize.toLocaleString()} bytes (-${saving}%)`;
  }
}
document.addEventListener('DOMContentLoaded', xfRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>XML is still everywhere — SOAP responses, configuration files, RSS/Atom feeds, SVG markup, OOXML innards. When you need to read, diff, or share a chunk of XML, the difference between a one-line minified blob and a properly indented tree is the difference between guesswork and reading. This tool pretty-prints any well-formed XML with configurable indentation, or minifies it for transport, and uses the browser's native XML parser to flag malformedness with a line and column where possible.</p>

<h3>When to use it</h3>
<ul>
  <li>Inspecting a SOAP envelope or a vendor's XML config that arrived as one minified line.</li>
  <li>Cleaning up an SVG so the path data is one element per line.</li>
  <li>Stripping pretty-print whitespace before sending XML over the wire.</li>
  <li>Sanity-checking that an XML file you generated is well-formed before handing it to a strict parser.</li>
  <li>Diffing two XML documents — pretty-print first, then diff the trees side by side.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Well-formed ≠ valid.</strong> "Well-formed" means the syntax parses (tags balance, attributes quoted, one root). "Valid" means it conforms to a DTD or schema. This tool checks well-formedness only — schema validation needs the schema file.</li>
  <li><strong>Whitespace can be significant.</strong> In <code>&lt;name&gt; Alice &lt;/name&gt;</code> the leading/trailing spaces are part of the value (XML defaults to <code>xml:space="preserve"</code>). Re-indenting changes them. If your XML is whitespace-sensitive (XHTML <code>&lt;pre&gt;</code>, embedded code blocks), pretty-print is the wrong tool.</li>
  <li><strong>Self-closing vs explicit empty.</strong> <code>&lt;br/&gt;</code> and <code>&lt;br&gt;&lt;/br&gt;</code> are equivalent in XML but differ in HTML. The formatter normalises empty elements to self-closing form.</li>
  <li><strong>CDATA, comments, and processing instructions are preserved.</strong> Their inner content isn't reformatted.</li>
  <li><strong>Namespaces survive.</strong> <code>xmlns:foo</code> declarations and <code>foo:bar</code> qualified names round-trip without modification.</li>
  <li><strong>Attribute order may shift.</strong> The XML parser doesn't strictly preserve attribute order across tools; if you're checksumming XML, canonicalise it first (XML C14N).</li>
  <li><strong>Browser parser quirks.</strong> Different browsers report parse errors with different formats. The line/column extraction is best-effort and may show only the message on some browsers.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>XML ist überall — SOAP, Konfigurationsdateien, RSS/Atom, SVG, OOXML. Eine eingerückte Baumdarstellung ist der Unterschied zwischen "lesen können" und "raten". Dieses Tool formatiert oder minimiert wohlgeformtes XML und verwendet den XML-Parser des Browsers, um Fehler mit Zeile und Spalte zu melden.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Eine SOAP-Envelope oder herstellerspezifische XML-Config inspizieren.</li>
<li>SVG aufräumen.</li>
<li>Whitespace vor dem Senden strippen.</li>
<li>XML auf Wohlgeformtheit prüfen.</li>
<li>Zwei XML-Dokumente diffen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Wohlgeformt ≠ valide.</strong> Schema-Validierung braucht das Schema.</li>
<li><strong>Whitespace kann signifikant sein.</strong> Standardmäßig <code>xml:space="preserve"</code> — bei whitespace-sensitivem XML kein Pretty-Print.</li>
<li><strong>Selbstschließend vs explizit leer.</strong> Tool normalisiert auf selbstschließend.</li>
<li><strong>CDATA, Kommentare, PIs bleiben erhalten.</strong></li>
<li><strong>Namespaces bleiben erhalten.</strong></li>
<li><strong>Attribut-Reihenfolge.</strong> Vor Checksum kanonisieren (XML C14N).</li>
<li><strong>Browser-Parser-Eigenheiten.</strong> Zeile/Spalte sind Best-Effort.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>XML sigue por todas partes: SOAP, configuraciones, RSS/Atom, SVG, OOXML. Una representación indentada es la diferencia entre leer y adivinar. Esta herramienta formatea o minimiza XML bien formado y usa el parser XML del navegador para señalar errores con línea y columna.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Inspeccionar un envelope SOAP o una config XML de proveedor.</li>
<li>Limpiar un SVG.</li>
<li>Quitar espacios antes de enviar.</li>
<li>Comprobar buena forma.</li>
<li>Diff entre dos XML.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Bien formado ≠ válido.</strong> La validación de esquema necesita el esquema.</li>
<li><strong>El espacio puede ser significativo.</strong> Por defecto <code>xml:space="preserve"</code> — no usar pretty-print en XML sensible al espacio.</li>
<li><strong>Auto-cerrado vs vacío explícito.</strong> La herramienta normaliza a auto-cerrado.</li>
<li><strong>CDATA, comentarios y PIs se conservan.</strong></li>
<li><strong>Los namespaces se conservan.</strong></li>
<li><strong>Orden de atributos.</strong> Para checksum, canonicaliza (XML C14N) antes.</li>
<li><strong>Diferencias entre parsers.</strong> Línea/columna best-effort.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>XML est encore partout : SOAP, configurations, RSS/Atom, SVG, OOXML. Une représentation indentée fait la différence entre lire et deviner. Cet outil formate ou minifie du XML bien formé et utilise le parser XML du navigateur pour signaler les erreurs avec ligne et colonne.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Inspecter une enveloppe SOAP ou une config XML.</li>
<li>Nettoyer un SVG.</li>
<li>Supprimer les espaces avant envoi.</li>
<li>Vérifier la bien-formation.</li>
<li>Diffuser entre deux XML.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Bien formé ≠ valide.</strong> La validation de schéma nécessite le schéma.</li>
<li><strong>L'espace peut être significatif.</strong> Par défaut <code>xml:space="preserve"</code> — pas de pretty-print sur du XML sensible aux espaces.</li>
<li><strong>Auto-fermant vs vide explicite.</strong> L'outil normalise en auto-fermant.</li>
<li><strong>CDATA, commentaires et PI sont préservés.</strong></li>
<li><strong>Les namespaces sont préservés.</strong></li>
<li><strong>Ordre des attributs.</strong> Pour un checksum, canoniser (XML C14N).</li>
<li><strong>Différences entre parseurs.</strong> Ligne/colonne best-effort.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>XML è ancora ovunque: SOAP, configurazioni, RSS/Atom, SVG, OOXML. Una rappresentazione indentata fa la differenza tra leggere e indovinare. Questo strumento formatta o minifica XML ben formato e usa il parser XML del browser per segnalare errori con riga e colonna.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Ispezionare un envelope SOAP o una config XML.</li>
<li>Pulire un SVG.</li>
<li>Rimuovere spazi prima dell'invio.</li>
<li>Verificare la ben-formattezza.</li>
<li>Diff tra due XML.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Ben formato ≠ valido.</strong> La validazione di schema richiede lo schema.</li>
<li><strong>Lo spazio può essere significativo.</strong> Default <code>xml:space="preserve"</code> — niente pretty-print su XML sensibile allo spazio.</li>
<li><strong>Auto-chiudente vs vuoto esplicito.</strong> Lo strumento normalizza ad auto-chiudente.</li>
<li><strong>CDATA, commenti e PI sono preservati.</strong></li>
<li><strong>I namespace sono preservati.</strong></li>
<li><strong>Ordine attributi.</strong> Per il checksum, canonicalizza (XML C14N).</li>
<li><strong>Differenze fra parser.</strong> Riga/colonna best-effort.</li>
</ul>
""",
    },
    "related": ["json-formatter", "yaml-json", "html-encoder"],
}
