TOOL = {
    "slug": "markdown-to-html",
    "category": "text",
    "icon": "M↓",
    "tags": ["markdown", "md", "html", "convert", "preview", "render"],
    "i18n": {
        "en": {
            "name": "Markdown to HTML",
            "tagline": "Convert Markdown to clean HTML with a live preview. Supports headings, lists, code, tables, images, and links.",
            "description": "Free online Markdown to HTML converter. CommonMark-flavoured: headings, lists, fenced code, tables, images, blockquotes, inline formatting. Live preview + copy.",
        },
        "de": {"name": "Markdown zu HTML", "tagline": "Markdown in sauberes HTML umwandeln mit Live-Vorschau. Überschriften, Listen, Code, Tabellen, Bilder und Links.", "description": "Kostenloser Markdown-zu-HTML-Konverter. CommonMark-Stil: Überschriften, Listen, Codeblöcke, Tabellen, Bilder, Zitate, Inline-Formatierung. Live-Vorschau + Kopieren."},
        "es": {"name": "Markdown a HTML", "tagline": "Convierte Markdown a HTML limpio con vista previa en vivo. Encabezados, listas, código, tablas, imágenes y enlaces.", "description": "Conversor Markdown a HTML gratuito. Estilo CommonMark: encabezados, listas, código, tablas, imágenes, citas, formato en línea. Vista previa + copiar."},
        "fr": {"name": "Markdown vers HTML", "tagline": "Convertissez Markdown en HTML propre avec aperçu en direct. Titres, listes, code, tableaux, images et liens.", "description": "Convertisseur Markdown vers HTML gratuit. Style CommonMark : titres, listes, blocs code, tableaux, images, citations, format en ligne. Aperçu live + copier."},
        "it": {"name": "Markdown a HTML", "tagline": "Converti Markdown in HTML pulito con anteprima live. Intestazioni, liste, codice, tabelle, immagini e link.", "description": "Convertitore Markdown-HTML gratuito. Stile CommonMark: intestazioni, liste, blocchi codice, tabelle, immagini, citazioni, formattazione inline. Anteprima + copia."},
        "pt": {"name": "Markdown para HTML", "tagline": "Converta Markdown em HTML limpo com preview ao vivo. Suporta cabeçalhos, listas, código, tabelas, imagens e links.", "description": "Conversor Markdown para HTML gratuito online. Estilo CommonMark: cabeçalhos, listas, blocos de código fenced, tabelas, imagens, blockquotes, formatação inline. Preview ao vivo + copiar."},
        "pl": {"name": "Markdown do HTML", "tagline": "Konwertuj Markdowna na czysty HTML z podglądem na żywo. Wspiera nagłówki, listy, kod, tabele, obrazki i linki.", "description": "Darmowy online konwerter Markdown do HTML. W smaku CommonMark: nagłówki, listy, fenced bloki kodu, tabele, obrazki, blockquote'y, formatowanie inline. Podgląd na żywo + kopia."},
    },
    "body": """
<div class="md-grid">
  <div class="tool-card">
    <label>Markdown</label>
    <textarea id="md-in" oninput="mdRun()" spellcheck="false"># Hello world

A simple **Markdown** parser with _live preview_.

## Features
- CommonMark basics
- Fenced \\`\\`\\`code\\`\\`\\` blocks
- Tables, images, links

| Item | Qty |
|------|----:|
| Tea  |   2 |
| Milk |   1 |

> Quotes work too.

```js
console.log("hi");
```
</textarea>
  </div>
  <div class="tool-card">
    <label>Preview</label>
    <div id="md-prev" class="md-preview"></div>
  </div>
</div>
<div class="tool-card">
  <label>HTML output</label>
  <div class="output-row">
    <pre class="output" id="md-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('md-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<style>
.md-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.md-grid textarea{min-height:340px;font-family:ui-monospace,monospace;font-size:0.88rem}
.md-preview{min-height:340px;padding:0.9rem 1rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;overflow:auto;font-size:0.94rem;line-height:1.55}
.md-preview h1,.md-preview h2,.md-preview h3{margin:0.7rem 0 0.4rem}
.md-preview h1{font-size:1.5rem;border-bottom:1px solid var(--border);padding-bottom:0.3rem}
.md-preview h2{font-size:1.25rem}
.md-preview h3{font-size:1.1rem}
.md-preview p{margin:0.5rem 0}
.md-preview pre{background:var(--bg);border:1px solid var(--border);padding:0.7rem;border-radius:6px;overflow:auto;font-size:0.85rem}
.md-preview code{font-family:ui-monospace,monospace;background:var(--bg);padding:0.1rem 0.3rem;border-radius:4px;font-size:0.88em}
.md-preview pre code{background:transparent;padding:0}
.md-preview blockquote{border-left:3px solid var(--border);padding:0.2rem 0.8rem;margin:0.6rem 0;color:var(--text-muted)}
.md-preview table{border-collapse:collapse;margin:0.6rem 0}
.md-preview th,.md-preview td{border:1px solid var(--border);padding:0.3rem 0.6rem}
.md-preview th{background:var(--bg)}
.md-preview ul,.md-preview ol{margin:0.4rem 0;padding-left:1.5rem}
.md-preview li{margin:0.15rem 0}
.md-preview img{max-width:100%;border-radius:6px}
.md-preview a{color:#3b82f6}
.md-preview hr{border:none;border-top:1px solid var(--border);margin:0.8rem 0}
@media(max-width:760px){.md-grid{grid-template-columns:1fr}}
</style>
<script>
function mdEsc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
function mdInline(s){
  s = s.replace(/!\\[([^\\]]*)\\]\\(([^)\\s]+)(?:\\s+"([^"]*)")?\\)/g, (_,a,u,t)=>`<img src="${mdEsc(u)}" alt="${mdEsc(a)}"${t?` title="${mdEsc(t)}"`:''}>`);
  s = s.replace(/\\[([^\\]]+)\\]\\(([^)\\s]+)(?:\\s+"([^"]*)")?\\)/g, (_,t,u,ti)=>`<a href="${mdEsc(u)}"${ti?` title="${mdEsc(ti)}"`:''}>${t}</a>`);
  s = s.replace(/`([^`]+)`/g, (_,c)=>`<code>${mdEsc(c)}</code>`);
  s = s.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>');
  s = s.replace(/__([^_]+)__/g, '<strong>$1</strong>');
  s = s.replace(/(^|[^*])\\*([^*\\n]+)\\*/g, '$1<em>$2</em>');
  s = s.replace(/(^|[^_])_([^_\\n]+)_/g, '$1<em>$2</em>');
  s = s.replace(/~~([^~]+)~~/g, '<del>$1</del>');
  return s;
}
function mdRender(md){
  const lines = md.split('\\n');
  const out = [];
  let i = 0;
  while(i < lines.length){
    const line = lines[i];
    // Fenced code
    let m = line.match(/^```\\s*(\\w*)\\s*$/);
    if(m){
      const lang = m[1] || '';
      const code = [];
      i++;
      while(i < lines.length && !lines[i].match(/^```\\s*$/)){ code.push(lines[i]); i++; }
      i++;
      out.push(`<pre><code${lang?` class="lang-${mdEsc(lang)}"`:''}>${mdEsc(code.join('\\n'))}</code></pre>`);
      continue;
    }
    // Headings
    m = line.match(/^(#{1,6})\\s+(.+)$/);
    if(m){ out.push(`<h${m[1].length}>${mdInline(mdEsc(m[2]))}</h${m[1].length}>`); i++; continue; }
    // Horizontal rule
    if(/^\\s*([-*_])\\s*\\1\\s*\\1[\\s\\S]*$/.test(line) && line.trim().replace(/[\\s\\-*_]/g,'')===''){ out.push('<hr>'); i++; continue; }
    // Blockquote
    if(/^>\\s?/.test(line)){
      const buf = [];
      while(i < lines.length && /^>\\s?/.test(lines[i])){ buf.push(lines[i].replace(/^>\\s?/, '')); i++; }
      out.push(`<blockquote>${mdRender(buf.join('\\n'))}</blockquote>`);
      continue;
    }
    // Lists
    if(/^\\s*([-*+]|\\d+\\.)\\s+/.test(line)){
      const ordered = /^\\s*\\d+\\./.test(line);
      const tag = ordered ? 'ol' : 'ul';
      const items = [];
      while(i < lines.length && /^\\s*([-*+]|\\d+\\.)\\s+/.test(lines[i])){
        items.push(`<li>${mdInline(mdEsc(lines[i].replace(/^\\s*([-*+]|\\d+\\.)\\s+/, '')))}</li>`);
        i++;
      }
      out.push(`<${tag}>${items.join('')}</${tag}>`);
      continue;
    }
    // Tables
    if(i+1 < lines.length && /\\|/.test(line) && /^\\s*\\|?\\s*:?-+:?\\s*(\\|\\s*:?-+:?\\s*)+\\|?\\s*$/.test(lines[i+1])){
      const splitRow = r => r.replace(/^\\s*\\|/,'').replace(/\\|\\s*$/,'').split('|').map(c=>c.trim());
      const header = splitRow(line);
      const aligns = splitRow(lines[i+1]).map(c=>{
        const l=c.startsWith(':'), r=c.endsWith(':');
        return l&&r?'center':r?'right':l?'left':'';
      });
      i += 2;
      const rows = [];
      while(i < lines.length && /\\|/.test(lines[i]) && lines[i].trim()){
        rows.push(splitRow(lines[i]));
        i++;
      }
      const th = header.map((c,j)=>`<th${aligns[j]?` style="text-align:${aligns[j]}"`:''}>${mdInline(mdEsc(c))}</th>`).join('');
      const tb = rows.map(r=>'<tr>'+r.map((c,j)=>`<td${aligns[j]?` style="text-align:${aligns[j]}"`:''}>${mdInline(mdEsc(c))}</td>`).join('')+'</tr>').join('');
      out.push(`<table><thead><tr>${th}</tr></thead><tbody>${tb}</tbody></table>`);
      continue;
    }
    // Blank line
    if(!line.trim()){ i++; continue; }
    // Paragraph (collect until blank)
    const para = [];
    while(i < lines.length && lines[i].trim() && !/^(#{1,6}\\s|>\\s|\\s*([-*+]|\\d+\\.)\\s|```)/.test(lines[i])){
      para.push(lines[i]);
      i++;
    }
    out.push(`<p>${mdInline(mdEsc(para.join(' ')))}</p>`);
  }
  return out.join('\\n');
}
function mdRun(){
  const raw = document.getElementById('md-in').value;
  const html = mdRender(raw);
  document.getElementById('md-prev').innerHTML = html;
  document.getElementById('md-out').textContent = html;
}
document.addEventListener('DOMContentLoaded', mdRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Markdown is the most-written authoring format on the planet — README files, blog posts, GitHub issues, chat messages, doc sites. HTML is what browsers render. This tool converts Markdown into clean HTML with a live preview so you can see what the rendered output will look like before pasting it into a CMS, generating a static page, or shipping it as part of an email template.</p>

<h3>Supported syntax</h3>
<ul>
  <li>Headings <code>#</code> through <code>######</code>; bold, italic, strike</li>
  <li>Inline <code>`code`</code> and fenced <code>```lang</code> blocks</li>
  <li>Bullet / numbered / nested lists</li>
  <li>Links <code>[text](url)</code> and images <code>![alt](url)</code></li>
  <li>Blockquotes, pipe tables with alignment, horizontal rules</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a fast in-browser parser, not a spec suite.</strong> CommonMark and GFM have edge cases (nested emphasis, link reference definitions, autolink expansion) that diverge between implementations. For strict conformance, use <code>marked</code>, <code>markdown-it</code>, or <code>remark</code> in a build step.</li>
  <li><strong>HTML embedded inside Markdown</strong> mostly passes through as-is, but some implementations sanitise it. Don't rely on this for security; treat untrusted markdown as untrusted HTML.</li>
  <li><strong>Tables vs alignment.</strong> Pipe tables need a separator row (<code>|---|</code>) and use <code>:---:</code> / <code>:---</code> / <code>---:</code> for centre/left/right alignment. Forgetting the separator is the most common reason a "table" renders as one paragraph.</li>
  <li><strong>Smart punctuation.</strong> Some renderers convert <code>--</code> to en-dashes and straight quotes to curly. This tool doesn't — pass through a typography pass if you need that.</li>
  <li><strong>Round-tripping isn't lossless.</strong> Markdown → HTML → Markdown will normalise heading style, list spacing, and link form. The semantics survive; the exact bytes don't.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Markdown é o formato de autoria mais escrito do planeta — arquivos README, posts de blog, issues do GitHub, mensagens de chat, sites de documentação. HTML é o que os browsers renderizam. Esta ferramenta converte Markdown em HTML limpo com preview ao vivo, para você ver como o resultado renderizado vai ficar antes de colar num CMS, gerar uma página estática ou enviar como parte de um template de e-mail.</p>

<h3>Sintaxe suportada</h3>
<ul>
  <li>Cabeçalhos <code>#</code> até <code>######</code>; bold, itálico, strike</li>
  <li>Inline <code>`code`</code> e blocos fenced <code>```lang</code></li>
  <li>Listas com bullet / numeradas / aninhadas</li>
  <li>Links <code>[texto](url)</code> e imagens <code>![alt](url)</code></li>
  <li>Blockquotes, tabelas com pipe e alinhamento, linhas horizontais</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Este é um parser rápido no browser, não uma suíte de conformidade.</strong> CommonMark e GFM têm casos extremos (ênfase aninhada, definições de referência de link, expansão de autolink) que divergem entre implementações. Para conformidade estrita, use <code>marked</code>, <code>markdown-it</code> ou <code>remark</code> num passo de build.</li>
  <li><strong>HTML embutido dentro do Markdown</strong> em geral passa direto, mas algumas implementações sanitizam. Não confie nisso para segurança; trate markdown não confiável como HTML não confiável.</li>
  <li><strong>Tabelas vs alinhamento.</strong> Tabelas com pipe precisam de uma linha separadora (<code>|---|</code>) e usam <code>:---:</code> / <code>:---</code> / <code>---:</code> para centralizar/esquerda/direita. Esquecer o separador é o motivo mais comum de uma "tabela" renderizar como um parágrafo.</li>
  <li><strong>Smart punctuation.</strong> Alguns renderers convertem <code>--</code> em travessão e aspas retas em curvas. Esta ferramenta não — passe por um passo de tipografia se precisar disso.</li>
  <li><strong>Round-trip não é lossless.</strong> Markdown → HTML → Markdown vai normalizar estilo de cabeçalho, espaçamento de lista e forma do link. A semântica sobrevive; os bytes exatos não.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Markdown to najczęściej pisany format autorski na świecie — pliki README, posty blogowe, GitHub issues, wiadomości na czacie, strony dokumentacji. HTML to to, co renderuje przeglądarka. To narzędzie konwertuje Markdowna na czysty HTML z podglądem na żywo, żebyś mógł zobaczyć, jak wyrenderowany wynik będzie wyglądał, zanim wkleisz go w CMS, wygenerujesz statyczną stronę albo wyślesz jako część szablonu maila.</p>

<h3>Wspierana składnia</h3>
<ul>
  <li>Nagłówki <code>#</code> do <code>######</code>; bold, italic, strike</li>
  <li>Inline'owy <code>`code`</code> i fenced'owe bloki <code>```lang</code></li>
  <li>Listy punktowane / numerowane / zagnieżdżone</li>
  <li>Linki <code>[tekst](url)</code> i obrazki <code>![alt](url)</code></li>
  <li>Blockquote'y, tabele z pipe'ami i wyrównaniem, linie poziome</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To szybki parser w przeglądarce, nie suite zgodności.</strong> CommonMark i GFM mają edge case'y (zagnieżdżone emfazy, definicje referencji linków, ekspansja autolinków), które różnią się między implementacjami. Po ścisłą zgodność użyj <code>marked</code>, <code>markdown-it</code> albo <code>remark</code> w buildzie.</li>
  <li><strong>HTML osadzony w Markdownie</strong> w większości przechodzi tak jak jest, ale niektóre implementacje go sanityzują. Nie polegaj na tym dla bezpieczeństwa; traktuj nieufnego markdowna jak nieufny HTML.</li>
  <li><strong>Tabele vs wyrównanie.</strong> Tabele z pipe'ami potrzebują wiersza separatora (<code>|---|</code>) i używają <code>:---:</code> / <code>:---</code> / <code>---:</code> dla wyśrodkowania/lewej/prawej. Pominięcie separatora to najczęstszy powód, dla którego "tabela" renderuje się jako jeden akapit.</li>
  <li><strong>Smart punctuation.</strong> Niektóre renderery konwertują <code>--</code> na półpauzę i proste cudzysłowy na drukarskie. To narzędzie tego nie robi — przepuść przez krok typograficzny, jeśli tego potrzebujesz.</li>
  <li><strong>Round-trip nie jest bezstratny.</strong> Markdown → HTML → Markdown znormalizuje styl nagłówków, odstępy w listach i formę linków. Semantyka przeżyje; dokładne bajty nie.</li>
</ul>
""",
    },
    "related": ["html-encoder", "lorem-ipsum", "json-formatter"],
}
