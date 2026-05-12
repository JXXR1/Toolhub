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
        "pt": {"name": "Formatador HTML", "tagline": "Formata e embeleza HTML ou minifica. Tamanho de indentação, remoção de comentários e reconhecimento de tags auto-fechantes.", "description": "Formatador e minificador HTML grátis online. Pretty-print com indentação configurável, remoção opcional de comentários e respeito por tags void/auto-fechantes. Roda totalmente no seu browser."},
        "pl": {"name": "Formatter HTML", "tagline": "Sformatuj i upiększ HTML albo zminifikuj. Rozmiar wcięcia, usuwanie komentarzy i świadomość tagów samozamykających.", "description": "Darmowy online formatter i minifikator HTML. Pretty-print z konfigurowalnym wcięciem, opcjonalne usuwanie komentarzy i respektowanie tagów void/samozamykających. Działa w całości w przeglądarce."},
        "ja": {"name": "HTML フォーマッター", "tagline": "HTML を整形・圧縮。インデント幅、コメント除去、自己終了タグの自動認識に対応。", "description": "オンライン無料の HTML フォーマッター / ミニファイア。設定可能なインデントでの整形、コメントの任意除去、void / 自己終了タグの認識に対応。すべてブラウザ内で動作します。"},
        "nl": {"name": "HTML Formatter", "tagline": "Formatteer en beautify HTML of minify het. Indent size, comment stripping en self-closing tag awareness.", "description": "Gratis online HTML formatter en minifier. Pretty-print met configureerbare indentatie, optioneel comments strippen, en void/self-closing tags respecteren. Draait volledig in je browser."},
        "tr": {"name": "HTML Formatter", "tagline": "HTML'i biçimlendir ve güzelleştir ya da küçült. Indent boyutu, yorum temizleme ve self-closing tag farkındalığı.", "description": "Ücretsiz online HTML formatter ve minifier. Ayarlanabilir indent ile güzel yazdır, opsiyonel olarak yorumları sil, void/self-closing tag'lere uy. Tamamen tarayıcında çalışır."},
        "id": {"name": "HTML Formatter", "tagline": "Format dan beautify HTML atau minify-nya. Ukuran indent, pengupasan komentar, dan kesadaran self-closing tag.", "description": "HTML formatter gratis. Beautify HTML berantakan dengan indentasi yang tepat atau minify HTML rapi dengan menghapus whitespace dan komentar. Sadar self-closing tag dan mempertahankan konten pre/code."},
        "vi": {"name": "HTML Formatter", "tagline": "Format và làm đẹp HTML hoặc minify nó. Kích thước indent, loại bỏ comment và nhận biết self-closing tag.", "description": "HTML formatter miễn phí trực tuyến. Làm đẹp markup lộn xộn với indent có thể cấu hình, hoặc minify để loại bỏ whitespace. Self-closing tag và CSS/JS inline được xử lý đúng."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>O markup HTML chega no seu editor em todos os tipos de estado — minificado para produção, gerado por engines de template sem nenhum cuidado com whitespace, digitado à mão e indentado de forma inconsistente. Esta ferramenta reformata qualquer fragmento HTML com indentação consistente por elemento aninhado, reconhecendo elementos void (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) e elementos inline (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>) para que o output pareça HTML de verdade, não algo formatado por regra cega. O modo minify remove whitespace entre tags e, opcionalmente, comentários. Tudo fica no seu browser.</p>

<h3>Quando usar</h3>
<ul>
  <li>Fazer pretty-print de um e-mail HTML minificado ou de uma cópia de "view source" para conseguir ler a estrutura.</li>
  <li>Limpar um trecho vindo de CMS / editor WYSIWYG antes de colar num code review.</li>
  <li>Minificar um asset HTML estático antes do deploy — menos bytes na rede, sem comentários vazando.</li>
  <li>Remover comentários do autor de um template antes de publicar.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Este é um tokenizer pragmático, não um parser HTML5 completo.</strong> Funciona bem em fragmentos do mundo real, mas não recupera de input gravemente malformado como os browsers fazem (browsers rodam o algoritmo completo de parsing HTML e corrigem erros silenciosamente — esta ferramenta não).</li>
  <li><strong>Whitespace dentro de <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> é preservado.</strong> Esses elementos são tratados como raw e não são reindentados.</li>
  <li><strong>Elementos inline ficam na mesma linha do texto pai</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> não é quebrado em várias linhas.</li>
  <li><strong>"Colapsar whitespace" muda o output renderizado em alguns conteúdos.</strong> Dois espaços viram um. Se seu design depende de múltiplos espaços ou sequências non-breaking, deixe desligado.</li>
  <li><strong>Notação self-closing em HTML é cosmética.</strong> <code>&lt;br/&gt;</code> e <code>&lt;br&gt;</code> são equivalentes em HTML5; esta ferramenta preserva o que você escreveu.</li>
  <li><strong>Minify não é uma fronteira de segurança.</strong> Não confie em remoção de comentários para esconder segredos — eles já foram enviados pro cliente.</li>
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
        "pl": """
<h2>Do czego to służy?</h2>
<p>HTML w edytorze trafia do nas w różnych stanach — zminifikowany na produkcję, generowany przez engine'y szablonów bez troski o białe znaki, klepany ręcznie i niespójnie wcinany. To narzędzie reformatuje dowolny fragment HTML ze spójnym wcięciem na zagnieżdżony element, rozpoznając elementy void (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) i inline (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>), żeby wynik wyglądał jak prawdziwy HTML, nie jak układ z reguły. Tryb minify usuwa białe znaki między tagami i opcjonalnie komentarze. Wszystko zostaje w przeglądarce.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Pretty-print zminifikowanego maila HTML albo "view source" strony, żeby przeczytać strukturę.</li>
  <li>Sprzątanie snippetu z CMS / WYSIWYG przed wklejeniem do code review.</li>
  <li>Minifikacja statycznego assetu HTML przed deployem — mniej bajtów na drucie, brak wycieku komentarzy.</li>
  <li>Usuwanie komentarzy autora z szablonu przed publikacją.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To pragmatyczny tokenizer, nie pełny parser HTML5.</strong> Sprawdza się na realnych fragmentach, ale nie poradzi sobie z mocno zepsutym inputem tak, jak przeglądarki (przeglądarki uruchamiają pełny algorytm parsowania HTML i po cichu naprawiają błędy — to narzędzie nie).</li>
  <li><strong>Białe znaki wewnątrz <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> są zachowywane.</strong> Te elementy są traktowane jako raw i nie są reindentowane.</li>
  <li><strong>Elementy inline zostają w tej samej linii co tekst rodzica</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> nie zostanie podzielony na linie.</li>
  <li><strong>"Collapse whitespace" zmienia renderowany wynik dla niektórych treści.</strong> Dwie spacje stają się jedną. Jeśli design polega na wielu spacjach albo non-breaking sequence'ach, zostaw wyłączone.</li>
  <li><strong>Notacja samozamykająca w HTML jest kosmetyczna.</strong> <code>&lt;br/&gt;</code> i <code>&lt;br&gt;</code> są równoważne w HTML5; narzędzie zachowuje to, co napisałeś.</li>
  <li><strong>Minify to nie granica bezpieczeństwa.</strong> Nie polegaj na usuwaniu komentarzy do ukrywania sekretów — i tak były wysłane do klienta.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>HTML マークアップは、本番向けにミニファイされたもの、テンプレートエンジンが空白を気にせず生成したもの、手書きで一貫しないインデントのものなど、いろいろな状態でやってきます。本ツールは任意の HTML を、ネスト要素ごとに一貫したインデントで整形します。void 要素（<code>&lt;img&gt;</code>、<code>&lt;br&gt;</code>、<code>&lt;meta&gt;</code>）やインライン要素（<code>&lt;a&gt;</code>、<code>&lt;span&gt;</code>、<code>&lt;strong&gt;</code>）を識別するため、出力は機械的でなく自然な HTML になります。Minify モードはタグ間の空白を削除し、必要に応じてコメントも除去します。すべてブラウザ内で完結します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ミニファイ済みの HTML メールやページの「ソース表示」コピーを、構造を読み取れるよう整形したいとき。</li>
  <li>CMS や WYSIWYG のスニペットをコードレビュー前に綺麗にしたいとき。</li>
  <li>静的 HTML のアセットをデプロイ前にミニファイし、転送量を減らしたい・コメントの漏洩を防ぎたいとき。</li>
  <li>テンプレートから著者コメントを除去して公開したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>これは実用本位のトークナイザで、完全な HTML5 パーサーではありません。</strong> 実際のフラグメントには十分強いですが、ひどく壊れた入力からの復元はブラウザほど巧みには行いません（ブラウザは完全な HTML パースアルゴリズムでエラーを黙って修復しますが、本ツールはそこまで行いません）。</li>
  <li><strong><code>&lt;pre&gt;</code>、<code>&lt;textarea&gt;</code>、<code>&lt;script&gt;</code>、<code>&lt;style&gt;</code> 内の空白は保持されます。</strong> これらの要素は raw として扱われ、再インデントは行いません。</li>
  <li><strong>インライン要素は親テキストと同じ行に置かれます。</strong> <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> は改行されません。</li>
  <li><strong>「空白の圧縮」は一部のコンテンツでレンダリング結果を変えます。</strong> 連続スペースが 1 つにまとまります。複数スペースや non-breaking 系列に依存するデザインでは無効にしてください。</li>
  <li><strong>HTML での自己終了表記は装飾的です。</strong> HTML5 では <code>&lt;br/&gt;</code> と <code>&lt;br&gt;</code> は等価であり、本ツールは入力どおりを保持します。</li>
  <li><strong>Minify はセキュリティ境界ではありません。</strong> コメント除去で秘密を隠そうとしないでください。それらは既にクライアントに配信されています。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>HTML-markup arriveert in je editor in allerlei staten — geminifieerd voor productie, gegenereerd door templating engines zonder regard voor whitespace, met de hand getypt en inconsistent geïndenteerd. Deze tool herformatteert elk HTML-fragment met consistente indentatie per geneste element, en herkent void elements (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) en inline elements (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>) zodat de output op echte HTML lijkt, niet op layout-per-regel. Minify-mode strijkt inter-tag whitespace en optioneel comments. Alles blijft in je browser.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Pretty-printen van een geminifieerde HTML-email of een "view source"-kopie van een pagina zodat je de structuur kunt lezen.</li>
  <li>Een snippet uit een CMS / WYSIWYG opschonen voor je in een code review plakt.</li>
  <li>Een statisch HTML-asset minify-en voor je deployt — minder bytes over de wire, geen comments gelekt.</li>
  <li>Author-comments strippen uit een template voor publicatie.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Dit is een pragmatische tokenizer, geen volledige HTML5-parser.</strong> Hij werkt goed op real-world fragments maar herstelt niet van zwaar malformed input zoals browsers doen (browsers draaien het volle HTML-parsing-algoritme en herstellen errors stil — deze tool niet).</li>
  <li><strong>Whitespace binnen <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> blijft behouden.</strong> Deze elementen worden als raw behandeld en niet opnieuw geïndenteerd.</li>
  <li><strong>Inline elementen blijven op dezelfde regel als hun parent-tekst</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> wordt niet over regels gesplitst.</li>
  <li><strong>"Collapse whitespace" verandert de gerenderde output voor sommige content.</strong> Twee spaties worden één. Als je design afhangt van meerdere spaties of non-breaking sequences, laat het uit.</li>
  <li><strong>Self-closing notatie in HTML is cosmetisch.</strong> <code>&lt;br/&gt;</code> en <code>&lt;br&gt;</code> zijn equivalent in HTML5; deze tool behoudt wat je hebt geschreven.</li>
  <li><strong>Minify is geen security boundary.</strong> Vertrouw niet op comments strippen om secrets te verbergen — die zijn al naar de client verzonden.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>HTML markup editörüne her türlü durumda gelir — production için küçültülmüş, boşluğa aldırmayan template motorları tarafından üretilmiş, tutarsız şekilde elle yazılmış ve girintilenmiş. Bu araç herhangi bir HTML parçasını her iç içe element için tutarlı indent ile yeniden biçimlendirir, void elementleri (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) ve inline elementleri (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>) tanır, böylece çıktı gerçek HTML gibi görünür, kural başına bir düzen değil. Minify modu tag'ler arası boşluğu ve isteğe bağlı yorumları temizler. Her şey tarayıcında kalır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Yapısını okuyabilmen için küçültülmüş bir HTML e-postasını veya bir sayfanın "kaynağı görüntüle" kopyasını güzel yazdırma.</li>
  <li>Bir kod incelemesine yapıştırmadan önce bir CMS / WYSIWYG'den bir snippet'i temizleme.</li>
  <li>Deploy etmeden önce statik bir HTML varlığını minify etme — wire üzerinde daha az byte, yorum sızıntısı yok.</li>
  <li>Yayınlamadan önce bir template'tan yazar yorumlarını çıkarma.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Bu pragmatik bir tokenizer'dır, tam bir HTML5 parser değil.</strong> Gerçek dünya parçaları üzerinde iyi çalışır ama tarayıcıların ciddi şekilde bozuk girdileri kurtardığı gibi kurtarmaz.</li>
  <li><strong><code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> içindeki boşluk korunur.</strong> Bu elementler ham olarak ele alınır ve yeniden indent edilmez.</li>
  <li><strong>Inline elementler ebeveyn metniyle aynı satırda kalır</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> satırlara bölünmez.</li>
  <li><strong>"Boşluğu daralt" bazı içerik için render edilen çıktıyı değiştirir.</strong> İki boşluk bir olur. Tasarımın birden fazla boşluğa veya non-breaking dizilere dayanıyorsa, kapat.</li>
  <li><strong>HTML'de self-closing notasyon kozmetiktir.</strong> <code>&lt;br/&gt;</code> ve <code>&lt;br&gt;</code> HTML5'te eşdeğerdir; bu araç ne yazdıysan korur.</li>
  <li><strong>Minify güvenlik sınırı değildir.</strong> Sırları gizlemek için yorumları temizlemeye güvenme — zaten istemciye gönderilmişlerdi.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Markup HTML datang ke editor kamu dalam berbagai keadaan — di-minify untuk production, dihasilkan template engine yang tidak peduli whitespace, diketik manual dengan indentasi tidak konsisten. Tool ini memformat ulang fragment HTML apa pun dengan indentasi konsisten per elemen bersarang, mengenali void element (<code>&lt;img&gt;</code>, <code>&lt;br&gt;</code>, <code>&lt;meta&gt;</code>) dan inline element (<code>&lt;a&gt;</code>, <code>&lt;span&gt;</code>, <code>&lt;strong&gt;</code>) sehingga output terlihat seperti HTML asli, bukan layout satu-baris-per-aturan. Mode minify menyatukan whitespace antar tag dan opsional menghapus comment. Semuanya tetap di browser kamu.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Pretty-print email HTML yang di-minify atau salinan "view source" dari halaman supaya kamu bisa membaca strukturnya.</li>
  <li>Membersihkan snippet dari CMS / WYSIWYG sebelum di-paste ke code review.</li>
  <li>Minify aset HTML statis sebelum deploy — lebih sedikit byte di kabel, tidak ada comment yang bocor.</li>
  <li>Menghapus comment author dari template sebelum publish.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Ini tokenizer pragmatis, bukan parser HTML5 lengkap.</strong> Bekerja baik pada fragment dunia nyata tapi tidak melakukan recovery dari input yang sangat malformed seperti browser (browser menjalankan algoritma parsing HTML lengkap dan memperbaiki error secara diam-diam — tool ini tidak).</li>
  <li><strong>Whitespace di dalam <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code> dipertahankan.</strong> Element-element ini diperlakukan sebagai raw dan tidak diindent ulang.</li>
  <li><strong>Inline element tetap di baris yang sama dengan text parent</strong> — <code>&lt;p&gt;some &lt;b&gt;bold&lt;/b&gt; text&lt;/p&gt;</code> tidak akan dipecah ke beberapa baris.</li>
  <li><strong>"Collapse whitespace" mengubah output rendered untuk sebagian content.</strong> Dua spasi jadi satu. Kalau desainmu bergantung pada multiple space atau sekuens non-breaking, biarkan off.</li>
  <li><strong>Notasi self-closing di HTML itu kosmetik.</strong> <code>&lt;br/&gt;</code> dan <code>&lt;br&gt;</code> ekuivalen di HTML5; tool ini mempertahankan yang kamu tulis.</li>
  <li><strong>Minify bukan batas keamanan.</strong> Jangan andalkan strip comment untuk menyembunyikan secret — secret itu sudah dikirim ke client.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>HTML hand-edited tích lũy whitespace lộn xộn — indent không nhất quán, dòng dài, thuộc tính trộn lẫn. Tool này pretty-print bất kỳ HTML nào với indent rõ ràng, hoặc minify nó để loại bỏ tất cả whitespace không cần thiết cho production. Nó hiểu các thẻ tự-đóng và inline CSS/JS.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Làm sạch HTML cũ với indent không nhất quán trước khi cam kết.</li>
  <li>Minify markup tĩnh để giảm kích thước payload.</li>
  <li>Định dạng response API trả về HTML cho dễ đọc.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Whitespace có thể có ý nghĩa.</strong> Trong <code>&lt;pre&gt;</code>, <code>&lt;textarea&gt;</code>, và một số <code>&lt;span&gt;</code> inline, whitespace là một phần của content. Tool này cố gắng giữ chúng, nhưng kiểm tra output.</li>
  <li><strong>Minify HTML đơn giản hơn minify CSS/JS.</strong> Đa số tiết kiệm đến từ collapse whitespace; phần khó (chấp nhận attribute không có quote, drop tag tự-đóng tùy chọn) thường không an toàn nếu chưa được phân tích cẩn thận.</li>
  <li><strong>Đừng format template.</strong> File chứa <code>{{handlebars}}</code>, <code>&lt;?php&gt;</code> hoặc <code>&lt;%erb%&gt;</code> có thể bị phá vỡ bởi formatter HTML — chúng không phải là HTML hợp lệ cho đến khi được render.</li>
</ul>
""",
    },
    "related": ["html-encoder", "css-minifier", "js-minifier", "xml-formatter"],
    "howto": {"flow": "transform", "action": "format",  "noun": "HTML"},
}
