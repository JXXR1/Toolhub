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
        "pt": {"name": "Formatador de XML", "tagline": "Formate e minifique XML. Valide se está bem-formado com linha e coluna em caso de erro.", "description": "Formatador e minificador de XML online gratuito. Pretty-print de XML com indentação configurável, ou remova whitespace para minificar. Valida well-formedness usando o parser XML do navegador — linha e coluna do erro são exibidos."},
        "pl": {"name": "Formatter XML", "tagline": "Sformatuj i zminifikuj XML. Waliduj poprawność (well-formed) z linią i kolumną przy błędach.", "description": "Darmowy online formatter i minifikator XML. Pretty-print XML z konfigurowalnym wcięciem albo wycinanie białych znaków do minifikacji. Waliduje well-formedness parserem XML przeglądarki — linia i kolumna błędu pokazane."},
        "ja": {"name": "XML フォーマッター", "tagline": "XML を整形・圧縮。well-formed の検証では行と列でエラー位置を表示。", "description": "オンライン無料の XML フォーマッター／ミニファイア。設定可能なインデントでの整形、または空白除去によるミニファイに対応します。ブラウザの XML パーサで well-formed を検証し、エラー時は行と列を表示します。"},
        "nl": {"name": "XML Formatter", "tagline": "Formatteer en minify XML. Valideer well-formedness met regel en kolom bij fouten.", "description": "Gratis online XML formatter en minifier. Pretty-print XML met configureerbare indent, of strip whitespace om te minify-en. Valideert well-formedness via de XML-parser van de browser — foutregel en -kolom getoond."},
        "tr": {"name": "XML Formatter", "tagline": "XML'i biçimlendir ve küçült. Hatalarda satır ve sütun ile well-formedness doğrula.", "description": "Ücretsiz online XML formatter ve minifier. XML'i ayarlanabilir indent ile güzel yazdır veya boşlukları temizleyerek küçült. Tarayıcının XML parser'ı ile well-formedness'i doğrular — hata satırı ve sütunu gösterilir."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>XML continua por toda parte — respostas SOAP, arquivos de configuração, feeds RSS/Atom, marcação SVG, internals de OOXML. Quando você precisa ler, comparar ou compartilhar um pedaço de XML, a diferença entre uma blob minificada de uma linha e uma árvore bem indentada é a diferença entre adivinhação e leitura. Esta ferramenta faz pretty-print de qualquer XML bem-formado com indentação configurável, ou minifica para transporte, e usa o parser XML nativo do navegador para sinalizar problemas de formação com linha e coluna quando possível.</p>

<h3>Quando usar</h3>
<ul>
  <li>Inspecionando um SOAP envelope ou uma config XML de um vendor que chegou como uma linha minificada.</li>
  <li>Limpando um SVG para ter o path data um elemento por linha.</li>
  <li>Removendo whitespace de pretty-print antes de enviar XML pela rede.</li>
  <li>Validando rapidamente que um arquivo XML que você gerou está bem-formado antes de entregar a um parser estrito.</li>
  <li>Comparando dois documentos XML — pretty-print primeiro, depois faça o diff das árvores lado a lado.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Bem-formado ≠ válido.</strong> "Bem-formado" significa que a sintaxe parseia (tags balanceadas, atributos com aspas, uma raiz). "Válido" significa que está em conformidade com um DTD ou schema. Esta ferramenta verifica apenas well-formedness — validação de schema precisa do arquivo de schema.</li>
  <li><strong>Whitespace pode ser significativo.</strong> Em <code>&lt;name&gt; Alice &lt;/name&gt;</code> os espaços antes e depois fazem parte do valor (XML usa <code>xml:space="preserve"</code> por padrão). Re-indentar muda isso. Se seu XML é sensível a whitespace (XHTML <code>&lt;pre&gt;</code>, blocos de código embutidos), pretty-print é a ferramenta errada.</li>
  <li><strong>Self-closing vs vazio explícito.</strong> <code>&lt;br/&gt;</code> e <code>&lt;br&gt;&lt;/br&gt;</code> são equivalentes em XML mas diferem em HTML. O formatador normaliza elementos vazios para a forma self-closing.</li>
  <li><strong>CDATA, comentários e processing instructions são preservados.</strong> Seu conteúdo interno não é reformatado.</li>
  <li><strong>Namespaces sobrevivem.</strong> Declarações <code>xmlns:foo</code> e nomes qualificados <code>foo:bar</code> fazem round-trip sem modificação.</li>
  <li><strong>Ordem dos atributos pode mudar.</strong> O parser XML não preserva estritamente a ordem de atributos entre ferramentas; se você está fazendo checksum de XML, canonicalize antes (XML C14N).</li>
  <li><strong>Peculiaridades do parser do browser.</strong> Browsers diferentes reportam erros de parse em formatos diferentes. A extração de linha/coluna é best-effort e pode mostrar só a mensagem em alguns browsers.</li>
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
        "pl": """
<h2>Do czego to służy?</h2>
<p>XML nadal jest wszędzie — odpowiedzi SOAP, pliki konfiguracyjne, feedy RSS/Atom, markup SVG, wnętrzności OOXML. Gdy musisz przeczytać, zdiffować albo udostępnić kawałek XML-a, różnica między jednoliniową zminifikowaną bryłą a porządnie wciętym drzewem to różnica między zgadywaniem a czytaniem. To narzędzie pretty-printuje dowolny well-formed XML z konfigurowalnym wcięciem albo minifikuje go pod transport, i używa natywnego parsera XML przeglądarki, żeby flagować nieprawidłowości z linią i kolumną tam, gdzie się da.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Inspekcja envelope'a SOAP albo configa XML od dostawcy, który przyszedł jako jedna zminifikowana linia.</li>
  <li>Czyszczenie SVG, żeby path data było jeden element na linię.</li>
  <li>Wycięcie białych znaków pretty-printu przed wysłaniem XML-a po sieci.</li>
  <li>Sanity check, że XML, który wygenerowałeś, jest well-formed, zanim wepchasz go do strict parsera.</li>
  <li>Diff dwóch dokumentów XML — najpierw pretty-print, potem diff drzew obok siebie.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Well-formed ≠ valid.</strong> "Well-formed" znaczy, że składnia parsuje (tagi się zgadzają, atrybuty w cudzysłowach, jeden root). "Valid" znaczy zgodność z DTD albo schemą. To narzędzie sprawdza tylko well-formedness — walidacja schematu wymaga pliku schematu.</li>
  <li><strong>Białe znaki bywają znaczące.</strong> W <code>&lt;name&gt; Alice &lt;/name&gt;</code> spacje na początku/końcu są częścią wartości (XML domyślnie ma <code>xml:space="preserve"</code>). Ponowne wcięcie je zmienia. Jeśli twój XML jest wrażliwy na białe znaki (XHTML <code>&lt;pre&gt;</code>, osadzone bloki kodu), pretty-print to złe narzędzie.</li>
  <li><strong>Self-closing vs jawnie pusty.</strong> <code>&lt;br/&gt;</code> i <code>&lt;br&gt;&lt;/br&gt;</code> są równoważne w XML, ale różnią się w HTML. Formatter normalizuje puste elementy do formy self-closing.</li>
  <li><strong>CDATA, komentarze i processing instructions są zachowywane.</strong> Ich wewnętrzna treść nie jest reformatowana.</li>
  <li><strong>Namespace'y przeżywają.</strong> Deklaracje <code>xmlns:foo</code> i kwalifikowane nazwy <code>foo:bar</code> robią round-trip bez modyfikacji.</li>
  <li><strong>Kolejność atrybutów może się zmienić.</strong> Parser XML nie zachowuje ściśle kolejności atrybutów między narzędziami; jeśli liczysz checksum z XML-a, najpierw kanonikalizuj (XML C14N).</li>
  <li><strong>Dziwactwa parserów przeglądarek.</strong> Różne przeglądarki raportują błędy parsowania w różnych formatach. Wyciąganie linia/kolumna jest best-effort i w niektórych przeglądarkach pokaże tylko komunikat.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>XML はいまだに至るところで使われています。SOAP レスポンス、設定ファイル、RSS/Atom フィード、SVG、OOXML の中身など。XML を読み、差分を取り、共有する場面では、1 行に圧縮された塊と整形済みのツリーの差は「読める」と「推測する」の違いに直結します。本ツールは well-formed な XML を任意のインデントで整形、または転送用にミニファイし、ブラウザの XML パーサで構文を検証して、可能な場合は行と列でエラー位置を表示します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>1 行で送られてきた SOAP エンベロープやベンダー XML 設定の中身を確認したいとき。</li>
  <li>SVG を整形して、path データを 1 要素 1 行で読めるようにしたいとき。</li>
  <li>転送前に整形用の空白を除去したいとき。</li>
  <li>厳密パーサに渡す前に、自分が生成した XML が well-formed か確認したいとき。</li>
  <li>2 つの XML を整形してから並べて diff を取りたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>well-formed ≠ valid。</strong> 「well-formed」は構文（タグの対応、属性のクォート、ルートが 1 つ）が成立すること。「valid」は DTD やスキーマに従うこと。本ツールは well-formed のみ検証します。スキーマ検証にはスキーマファイルが必要です。</li>
  <li><strong>空白は意味を持つことがあります。</strong> <code>&lt;name&gt; Alice &lt;/name&gt;</code> の前後の空白は値の一部です（XML はデフォルト <code>xml:space="preserve"</code>）。再インデントで変わります。XHTML の <code>&lt;pre&gt;</code> や埋め込みコードのように空白が重要な XML では pretty-print は不向きです。</li>
  <li><strong>self-closing と明示的に空のタグ。</strong> XML では <code>&lt;br/&gt;</code> と <code>&lt;br&gt;&lt;/br&gt;</code> は等価ですが、HTML では異なります。本フォーマッターは空要素を self-closing 形式へ正規化します。</li>
  <li><strong>CDATA、コメント、processing instruction は保持されます。</strong> 内部内容は再整形しません。</li>
  <li><strong>名前空間は維持されます。</strong> <code>xmlns:foo</code> 宣言や <code>foo:bar</code> の修飾名はそのままラウンドトリップします。</li>
  <li><strong>属性順は変わることがあります。</strong> XML パーサはツール間で属性順を厳密には維持しません。チェックサムを取るなら先に正規化（XML C14N）してください。</li>
  <li><strong>ブラウザのパーサ差異。</strong> ブラウザによってエラー報告のフォーマットが異なります。行・列の抽出はベストエフォートで、ブラウザによってはメッセージのみ表示されます。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>XML is nog steeds overal — SOAP-responses, configuratiebestanden, RSS/Atom-feeds, SVG-markup, OOXML-binnenwerk. Als je een stuk XML moet lezen, diffen of delen, is het verschil tussen een one-line geminifieerde blob en een correct geïndenteerde boom het verschil tussen gokwerk en lezen. Deze tool pretty-print elk well-formed XML met configureerbare indentatie, of minified het voor transport, en gebruikt de native XML-parser van de browser om malformedness te flaggen met een regel en kolom waar mogelijk.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een SOAP-envelope of een vendor's XML-config inspecteren die als één geminifieerde regel aankwam.</li>
  <li>Een SVG opschonen zodat de path-data één element per regel is.</li>
  <li>Pretty-print whitespace strippen voor XML over de lijn te sturen.</li>
  <li>Sanity check dat een XML-bestand dat je hebt gegenereerd well-formed is voor je het naar een strikte parser geeft.</li>
  <li>Twee XML-documenten diffen — pretty-print eerst, dan de bomen side by side diffen.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Well-formed ≠ valid.</strong> "Well-formed" betekent dat de syntax parset (tags balanceren, attributes ge-quote'd, één root). "Valid" betekent dat het voldoet aan een DTD of schema. Deze tool checkt alleen well-formedness — schema-validatie vereist het schema-bestand.</li>
  <li><strong>Whitespace kan significant zijn.</strong> In <code>&lt;name&gt; Alice &lt;/name&gt;</code> zijn de leading/trailing spaties onderdeel van de value (XML defaultet op <code>xml:space="preserve"</code>). Her-indenteren verandert ze. Als je XML whitespace-gevoelig is (XHTML <code>&lt;pre&gt;</code>, embedded code blocks), is pretty-print het verkeerde gereedschap.</li>
  <li><strong>Self-closing vs expliciet leeg.</strong> <code>&lt;br/&gt;</code> en <code>&lt;br&gt;&lt;/br&gt;</code> zijn equivalent in XML maar verschillen in HTML. De formatter normaliseert lege elementen naar self-closing form.</li>
  <li><strong>CDATA, comments en processing instructions blijven behouden.</strong> Hun inner content wordt niet herformatteerd.</li>
  <li><strong>Namespaces overleven.</strong> <code>xmlns:foo</code> declarations en <code>foo:bar</code> qualified names round-trippen zonder wijziging.</li>
  <li><strong>Attribute-volgorde kan verschuiven.</strong> De XML-parser behoudt attribute-volgorde niet strikt tussen tools; als je XML checksumt, canonicaliseer eerst (XML C14N).</li>
  <li><strong>Browser-parser quirks.</strong> Verschillende browsers rapporteren parse-fouten met verschillende formaten. De regel/kolom-extractie is best-effort en toont op sommige browsers alleen het bericht.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>XML hâlâ her yerdedir — SOAP yanıtları, yapılandırma dosyaları, RSS/Atom feed'leri, SVG markup, OOXML iç bileşenleri. Bir XML parçasını okuman, diff'lemen veya paylaşman gerektiğinde, tek satırlık minify edilmiş bir blob ile düzgün indent edilmiş bir ağaç arasındaki fark tahmin etme ile okuma arasındaki farktır. Bu araç herhangi bir well-formed XML'i ayarlanabilir indent ile güzel yazdırır veya taşıma için minify eder ve bozukluğu mümkün olan yerlerde satır ve sütunla işaretlemek için tarayıcının yerel XML parser'ını kullanır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Tek minify edilmiş satır olarak gelen bir SOAP zarfını veya vendor XML config'ini inceleme.</li>
  <li>Bir SVG'yi temizleme, böylece path verisi satır başına bir element olur.</li>
  <li>Wire üzerinde XML göndermeden önce güzel-yazdır boşluğunu temizleme.</li>
  <li>Ürettiğin bir XML dosyasının katı bir parser'a vermeden önce well-formed olduğunun sanity check'i.</li>
  <li>İki XML belgesini diff'leme — önce güzel yazdır, sonra ağaçları yan yana diff'le.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Well-formed ≠ geçerli.</strong> "Well-formed" sözdiziminin parse ettiği anlamına gelir (tag'ler dengelenir, nitelikler tırnaklı, tek bir kök). "Geçerli" bir DTD veya şemaya uyduğu anlamına gelir. Bu araç yalnızca well-formedness'i kontrol eder — şema doğrulama şema dosyasını gerektirir.</li>
  <li><strong>Boşluk anlamlı olabilir.</strong> <code>&lt;name&gt; Alice &lt;/name&gt;</code>'da baştaki/sondaki boşluklar değerin parçasıdır (XML varsayılan olarak <code>xml:space="preserve"</code>'dir). Yeniden indent etme onları değiştirir. XML'in boşluk-hassas ise (XHTML <code>&lt;pre&gt;</code>, gömülü kod blokları), güzel-yazdır yanlış araçtır.</li>
  <li><strong>Self-closing - açık boş.</strong> <code>&lt;br/&gt;</code> ve <code>&lt;br&gt;&lt;/br&gt;</code> XML'de eşdeğerdir ama HTML'de farklıdır. Formatter boş elementleri self-closing forma normalize eder.</li>
  <li><strong>CDATA, yorumlar ve processing instruction'lar korunur.</strong> İç içerikleri yeniden biçimlendirilmez.</li>
  <li><strong>Namespace'ler hayatta kalır.</strong> <code>xmlns:foo</code> tanımları ve <code>foo:bar</code> nitelikli adlar değişiklik olmadan round-trip yapar.</li>
  <li><strong>Nitelik sırası kayabilir.</strong> XML parser araçlar arasında nitelik sırasını katı şekilde korumaz; XML checksum'ı yapıyorsan, önce kanonikleştir (XML C14N).</li>
  <li><strong>Tarayıcı parser tuhaflıkları.</strong> Farklı tarayıcılar parse hatalarını farklı biçimlerde raporlar. Satır/sütun çıkarımı en iyi çabadır ve bazı tarayıcılarda yalnızca mesajı gösterebilir.</li>
</ul>
""",
    },
    "related": ["json-formatter", "yaml-json", "html-encoder"],
    "howto": {"flow": "transform", "action": "format",  "noun": "XML"},
}
