TOOL = {
    "slug": "html-formatter",
    "category": "developer",
    "icon": "</>",
    "tags": ["html", "format", "beautify", "minify", "indent", "tidy"],
    "i18n": {
        "en": {
            "name": "HTML Formatter",
            "tagline": "Format and beautify HTML or minify it. Indent size, comment stripping, and self-closing tag awareness.",
            "description": "Free online HTML formatter and minifier. Pretty-print with configurable indentation, optionally strip comments, and respect void/self-closing tags. Runs entirely in your browser.",
        },
        "de": {"name": "HTML-Formatierer", "tagline": "HTML formatieren und einrücken oder minimieren. Einrückgröße, Kommentar-Strippen und Self-Closing-Bewusstsein.", "description": "Kostenloser HTML-Formatierer und -Minifizierer. Pretty-Print mit konfigurierbarer Einrückung, optional Kommentare entfernen, Void-/Self-Closing-Tags respektieren. Komplett im Browser."},
        "es": {"name": "Formateador HTML", "tagline": "Formatea y embellece HTML o minifícalo. Tamaño de indentación, eliminación de comentarios y reconocimiento de etiquetas auto-cerradas.", "description": "Formateador y minimizador HTML gratuito. Pretty-print con indentación configurable, eliminación opcional de comentarios y respeto a etiquetas void/auto-cerradas. 100% en el navegador."},
        "fr": {"name": "Formateur HTML", "tagline": "Formatez et embellissez du HTML ou minifiez-le. Taille d'indentation, suppression de commentaires, gestion des balises auto-fermantes.", "description": "Formateur et minifieur HTML gratuit. Pretty-print avec indentation configurable, suppression optionnelle des commentaires, respect des balises void/auto-fermantes. 100% dans le navigateur."},
        "it": {"name": "Formattatore HTML", "tagline": "Formatta e abbellisce HTML o minifica. Dimensione indentazione, rimozione commenti, consapevolezza tag auto-chiudenti.", "description": "Formattatore e minificatore HTML gratuito. Pretty-print con indentazione configurabile, rimozione opzionale dei commenti, rispetto dei tag void/auto-chiudenti. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="hf-in" oninput="hfRun()" spellcheck="false" placeholder="<!doctype html><html><head><title>x</title></head><body><h1>hi</h1></body></html>" style="min-height:160px"><!doctype html><html lang="en"><head><meta charset="utf-8"><title>Toolhub demo</title><!-- a comment --></head><body><header><h1>Hello</h1><nav><a href="/">home</a><a href="/about">about</a></nav></header><main><p>Some <strong>bold</strong> text and an <img src="/x.png" alt="x"> image.</p></main></body></html></textarea>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="hf-mode" onchange="hfRun()">
        <option value="pretty" selected>{LBL_BEAUTIFY}</option>
        <option value="minify">{LBL_MINIFY}</option>
      </select>
    </div>
    <div>
      <label>Indent</label>
      <select id="hf-indent" onchange="hfRun()">
        <option value="2" selected>2 spaces</option>
        <option value="4">4 spaces</option>
        <option value="tab">Tab</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label><input type="checkbox" id="hf-strip" onchange="hfRun()"> Strip comments</label>
    </div>
    <div>
      <label><input type="checkbox" id="hf-collapse" checked onchange="hfRun()"> Collapse whitespace in text</label>
    </div>
  </div>
  <div class="meta" id="hf-status" style="margin-top:0.6rem;font-family:ui-monospace,monospace;font-size:0.82rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="hf-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('hf-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
const HF_VOID = new Set(['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']);
const HF_INLINE = new Set(['a','abbr','b','bdi','bdo','br','cite','code','data','dfn','em','i','kbd','mark','q','rp','rt','ruby','s','samp','small','span','strong','sub','sup','time','u','var','wbr']);
const HF_PRESERVE = new Set(['pre','textarea','script','style','code']);

// Lightweight HTML tokenizer — sufficient for formatting; not a strict HTML5 parser.
function hfTokenize(html){
  const tokens = [];
  let i = 0;
  while(i < html.length){
    if(html.startsWith('<!--', i)){
      const end = html.indexOf('-->', i+4);
      const stop = end === -1 ? html.length : end + 3;
      tokens.push({t:'comment', v: html.slice(i, stop)});
      i = stop; continue;
    }
    if(html.startsWith('<!', i)){
      const end = html.indexOf('>', i);
      const stop = end === -1 ? html.length : end+1;
      tokens.push({t:'doctype', v: html.slice(i, stop)});
      i = stop; continue;
    }
    if(html.startsWith('<?', i)){
      const end = html.indexOf('?>', i);
      const stop = end === -1 ? html.length : end+2;
      tokens.push({t:'pi', v: html.slice(i, stop)});
      i = stop; continue;
    }
    if(html[i] === '<' && html[i+1] === '/'){
      const end = html.indexOf('>', i);
      const stop = end === -1 ? html.length : end+1;
      const inner = html.slice(i+2, stop-1).trim();
      tokens.push({t:'close', name: inner.toLowerCase(), v: html.slice(i, stop)});
      i = stop; continue;
    }
    if(html[i] === '<' && /[a-zA-Z]/.test(html[i+1])){
      // open or self-closing
      // find matching > but skip inside attribute strings
      let j = i+1;
      let inStr = null;
      while(j < html.length){
        const c = html[j];
        if(inStr){ if(c === inStr) inStr = null; }
        else if(c === '"' || c === "'") inStr = c;
        else if(c === '>') break;
        j++;
      }
      const stop = j < html.length ? j+1 : html.length;
      const raw = html.slice(i, stop);
      const m = raw.match(/^<\\s*([A-Za-z][A-Za-z0-9-]*)/);
      const name = m ? m[1].toLowerCase() : '';
      const selfClosing = /\\/\\s*>$/.test(raw);
      tokens.push({t:'open', name, v: raw, selfClosing});
      i = stop;
      // For preserve tags, swallow content verbatim until matching close
      if(HF_PRESERVE.has(name) && !selfClosing){
        const re = new RegExp('</\\\\s*' + name + '\\\\s*>', 'i');
        const rest = html.slice(i);
        const cm = rest.match(re);
        if(cm){
          tokens.push({t:'rawtext', v: rest.slice(0, cm.index), parent: name});
          tokens.push({t:'close', name, v: rest.slice(cm.index, cm.index + cm[0].length)});
          i += cm.index + cm[0].length;
        } else {
          tokens.push({t:'rawtext', v: rest, parent: name});
          i = html.length;
        }
      }
      continue;
    }
    // text
    let j = i;
    while(j < html.length && html[j] !== '<') j++;
    tokens.push({t:'text', v: html.slice(i, j)});
    i = j;
  }
  return tokens;
}

function hfFormat(html, opts){
  const tokens = hfTokenize(html);
  const indent = opts.indent;
  let depth = 0;
  let out = '';
  let lastWasBlock = true;
  function pad(){ return indent.repeat(Math.max(0, depth)); }
  for(let i = 0; i < tokens.length; i++){
    const t = tokens[i];
    if(t.t === 'comment'){
      if(opts.stripComments) continue;
      if(out && !out.endsWith('\\n')) out += '\\n';
      out += pad() + t.v + '\\n';
      lastWasBlock = true; continue;
    }
    if(t.t === 'doctype' || t.t === 'pi'){
      if(out && !out.endsWith('\\n')) out += '\\n';
      out += pad() + t.v + '\\n';
      lastWasBlock = true; continue;
    }
    if(t.t === 'open'){
      const isVoid = HF_VOID.has(t.name) || t.selfClosing;
      const isInline = HF_INLINE.has(t.name);
      const next = tokens[i+1];
      const next2 = tokens[i+2];
      // Inline tag with simple text-only content -> keep on one line
      if(isInline && next && next.t === 'text' && next2 && next2.t === 'close' && next2.name === t.name){
        if(lastWasBlock){ if(out && !out.endsWith('\\n')) out += '\\n'; out += pad(); }
        out += t.v + (opts.collapse ? next.v.replace(/\\s+/g, ' ').replace(/^\\s|\\s$/g, x=>x) : next.v) + next2.v;
        i += 2;
        lastWasBlock = false;
        continue;
      }
      if(out && !out.endsWith('\\n')) out += '\\n';
      out += pad() + t.v + '\\n';
      if(!isVoid) depth++;
      lastWasBlock = true; continue;
    }
    if(t.t === 'close'){
      depth = Math.max(0, depth-1);
      if(out && !out.endsWith('\\n')) out += '\\n';
      out += pad() + t.v + '\\n';
      lastWasBlock = true; continue;
    }
    if(t.t === 'text'){
      let s = t.v;
      if(opts.collapse) s = s.replace(/\\s+/g, ' ');
      if(s.trim() === '') continue;
      if(lastWasBlock){
        if(out && !out.endsWith('\\n')) out += '\\n';
        out += pad() + s.trim() + '\\n';
        lastWasBlock = true;
      } else {
        out += s;
      }
      continue;
    }
    if(t.t === 'rawtext'){
      // verbatim content for pre/script/style/textarea
      out += t.v;
      lastWasBlock = false;
      continue;
    }
  }
  return out.replace(/\\n{3,}/g, '\\n\\n').replace(/\\n+$/, '').trim() + '\\n';
}

function hfMinify(html, opts){
  const tokens = hfTokenize(html);
  let out = '';
  for(const t of tokens){
    if(t.t === 'comment'){ if(opts.stripComments) continue; out += t.v; continue; }
    if(t.t === 'doctype' || t.t === 'pi'){ out += t.v; continue; }
    if(t.t === 'open' || t.t === 'close'){ out += t.v.replace(/\\s+/g, ' ').replace(/\\s+>/g,'>'); continue; }
    if(t.t === 'rawtext'){ out += t.v; continue; }
    if(t.t === 'text'){
      const s = t.v.replace(/\\s+/g, ' ');
      if(s === ' ' && (out.endsWith('>') || out.endsWith(' '))) continue;
      out += s;
    }
  }
  return out.trim();
}

function hfRun(){
  const inp = document.getElementById('hf-in').value;
  const out = document.getElementById('hf-out');
  const status = document.getElementById('hf-status');
  out.classList.remove('error');
  if(!inp.trim()){ out.textContent = '{LBL_NO_INPUT}'; status.textContent=''; return; }
  try {
    const mode = document.getElementById('hf-mode').value;
    const stripComments = document.getElementById('hf-strip').checked;
    const collapse = document.getElementById('hf-collapse').checked;
    const indentChoice = document.getElementById('hf-indent').value;
    const indent = indentChoice === 'tab' ? '\\t' : ' '.repeat(parseInt(indentChoice, 10));
    const result = mode === 'pretty'
      ? hfFormat(inp, {indent, stripComments, collapse})
      : hfMinify(inp, {stripComments});
    out.textContent = result;
    const inSize = new Blob([inp]).size;
    const outSize = new Blob([result]).size;
    if(mode === 'minify'){
      const saving = inSize ? Math.max(0, Math.round((1 - outSize/inSize) * 100)) : 0;
      status.textContent = `${inSize.toLocaleString()} → ${outSize.toLocaleString()} bytes (-${saving}%)`;
    } else {
      status.textContent = `${inSize.toLocaleString()} → ${outSize.toLocaleString()} bytes`;
    }
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + e.message;
    status.textContent = '';
  }
}
document.addEventListener('DOMContentLoaded', hfRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>HTML markup arrives in your editor in all sorts of states — minified for production, generated by templating engines with no regard for whitespace, hand-typed and indented inconsistently. This tool reformats any HTML fragment with consistent indentation per nested element, recognising void elements (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) and inline elements (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>) so the output looks like real HTML, not a layout-by-rule. Minify mode strips inter-tag whitespace and optionally comments. Everything stays in your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Pretty-printing a minified HTML email or a "view source" copy of a page so you can read its structure.</li>
  <li>Cleaning up a snippet from a CMS / WYSIWYG before pasting into a code review.</li>
  <li>Minifying a static HTML asset before deploying — fewer bytes over the wire, no comments leaked.</li>
  <li>Stripping author comments from a template before publishing.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a pragmatic tokenizer, not a full HTML5 parser.</strong> It works well on real-world fragments but won't recover from severely malformed input the way browsers do (browsers run the full HTML parsing algorithm and fix up errors silently — this tool doesn't).</li>
  <li><strong>Whitespace inside <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> is preserved.</strong> These elements are treated as raw and aren't re-indented.</li>
  <li><strong>Inline elements stay on the same line as their parent text</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> won't be split across lines.</li>
  <li><strong>"Collapse whitespace" changes the rendered output for some content.</strong> Two spaces become one. If your design relies on multiple spaces or non-breaking sequences, leave it off.</li>
  <li><strong>Self-closing notation in HTML is cosmetic.</strong> <code>&lt;br/&gt;</code> and <code>&lt;br&gt;</code> are equivalent in HTML5; this tool preserves whatever you wrote.</li>
  <li><strong>Minify is not a security boundary.</strong> Don't rely on stripping comments to hide secrets — they were already shipped to the client.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>HTML-Markup kommt in allen möglichen Zuständen — minimiert, von Template-Engines erzeugt, von Hand inkonsistent eingerückt. Dieses Tool formatiert mit Einrückung pro Element und erkennt Void- (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>) und Inline-Elemente. Minify-Modus entfernt Whitespace und optional Kommentare. Alles im Browser.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Minimiertes HTML eines View-Source lesbar machen.</li>
<li>CMS-Snippet vor Code-Review aufräumen.</li>
<li>Statisches HTML vor Deploy minifizieren.</li>
<li>Autor-Kommentare vor Veröffentlichung entfernen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Pragmatischer Tokenizer, kein HTML5-Parser.</strong> Schwer fehlerhafte Eingaben werden nicht repariert.</li>
<li><strong>Whitespace in <code>pre</code>, <code>textarea</code>, <code>script</code>, <code>style</code> bleibt erhalten.</strong></li>
<li><strong>Inline-Elemente auf derselben Zeile wie Eltern-Text.</strong></li>
<li><strong>"Whitespace kollabieren" verändert sichtbare Ausgabe.</strong></li>
<li><strong>Self-Closing in HTML ist kosmetisch.</strong></li>
<li><strong>Minify ist keine Security-Grenze.</strong></li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>El HTML llega en todos los estados: minificado, generado por templates, escrito a mano. Esta herramienta reformatea con indentación consistente, reconoce elementos void (<code>&lt;img&gt;</code>) e inline (<code>&lt;a&gt;</code>). Minify quita espacios y opcionalmente comentarios. Todo en el navegador.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Hacer legible un view-source minificado.</li>
<li>Limpiar un snippet de CMS antes de un review.</li>
<li>Minificar HTML estático antes de desplegar.</li>
<li>Eliminar comentarios de autor antes de publicar.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Tokenizador pragmático, no parser HTML5.</strong> No repara entradas muy malformadas.</li>
<li><strong>Espacios en <code>pre</code>, <code>textarea</code>, <code>script</code>, <code>style</code> se preservan.</strong></li>
<li><strong>Inline en la misma línea que el texto padre.</strong></li>
<li><strong>"Colapsar espacios" altera la salida renderizada.</strong></li>
<li><strong>Auto-cerrado en HTML es cosmético.</strong></li>
<li><strong>Minify no es seguridad.</strong></li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Le HTML arrive dans tous les états : minifié, généré par templates, indenté à la main. Cet outil reformate avec indentation cohérente, reconnaît les éléments void (<code>&lt;img&gt;</code>) et inline (<code>&lt;a&gt;</code>). Le mode minify supprime les espaces et les commentaires en option. Tout dans le navigateur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Rendre lisible un view-source minifié.</li>
<li>Nettoyer un snippet CMS avant revue.</li>
<li>Minifier du HTML statique avant déploiement.</li>
<li>Supprimer commentaires d'auteur avant publication.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Tokenizer pragmatique, pas un parser HTML5.</strong> Ne répare pas les entrées très mal formées.</li>
<li><strong>Espaces dans <code>pre</code>, <code>textarea</code>, <code>script</code>, <code>style</code> préservés.</strong></li>
<li><strong>Éléments inline sur la même ligne que le texte parent.</strong></li>
<li><strong>« Réduire les espaces » modifie le rendu.</strong></li>
<li><strong>Auto-fermant en HTML est cosmétique.</strong></li>
<li><strong>Minify n'est pas une frontière de sécurité.</strong></li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>L'HTML arriva in ogni stato: minificato, generato da template, scritto a mano. Questo strumento riformatta con indentazione coerente, riconosce elementi void (<code>&lt;img&gt;</code>) e inline (<code>&lt;a&gt;</code>). Minify rimuove spazi e commenti opzionalmente. Tutto nel browser.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Rendere leggibile un view-source minificato.</li>
<li>Pulire snippet CMS prima di una review.</li>
<li>Minificare HTML statico prima del deploy.</li>
<li>Rimuovere commenti d'autore prima della pubblicazione.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Tokenizer pragmatico, non parser HTML5.</strong> Non ripara input gravemente malformati.</li>
<li><strong>Spazi in <code>pre</code>, <code>textarea</code>, <code>script</code>, <code>style</code> preservati.</strong></li>
<li><strong>Inline sulla stessa riga del testo genitore.</strong></li>
<li><strong>"Comprimi spazi" modifica il rendering.</strong></li>
<li><strong>Auto-chiudente in HTML è cosmetico.</strong></li>
<li><strong>Minify non è una barriera di sicurezza.</strong></li>
</ul>
""",
    },
    "related": ["html-encoder", "css-minifier", "js-minifier", "xml-formatter"],
}
