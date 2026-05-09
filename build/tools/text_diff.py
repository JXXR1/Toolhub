TOOL = {
    "slug": "text-diff",
    "category": "text",
    "icon": "±",
    "tags": ["diff", "compare", "text", "lines", "patch", "changes"],
    "i18n": {
        "en": {
            "name": "Text Diff",
            "tagline": "Compare two blocks of text and see line-by-line additions, removals, and unchanged context. Side-by-side or unified view.",
            "description": "Free online text diff tool. Line-level Myers diff with side-by-side and unified views, ignore-whitespace and ignore-case toggles. Runs in your browser.",
        },
        "de": {"name": "Text-Diff", "tagline": "Vergleiche zwei Textblöcke und sieh zeilenweise Ergänzungen, Löschungen und Kontext. Side-by-side oder unified.", "description": "Kostenloses Text-Diff-Tool. Zeilenweiser Myers-Diff mit Side-by-side und Unified-Ansicht, Whitespace und Groß-/Kleinschreibung ignorierbar. Läuft im Browser."},
        "es": {"name": "Comparador de Texto", "tagline": "Compara dos bloques de texto y ve adiciones, eliminaciones y contexto línea por línea. Vista lado a lado o unificada.", "description": "Comparador de texto en línea gratuito. Diff de Myers por línea con vista lado a lado y unificada, ignorar espacios y mayúsculas. En el navegador."},
        "fr": {"name": "Comparateur de Texte", "tagline": "Comparez deux blocs de texte ligne par ligne. Ajouts, suppressions, contexte. Vue côte à côte ou unifiée.", "description": "Comparateur de texte gratuit en ligne. Diff Myers par ligne avec vue côte-à-côte et unifiée, ignore les espaces ou la casse. Dans le navigateur."},
        "it": {"name": "Confronto Testo", "tagline": "Confronta due blocchi di testo e vedi aggiunte, rimozioni e contesto riga per riga. Vista affiancata o unificata.", "description": "Strumento di diff di testo gratuito online. Diff di Myers per riga con vista affiancata e unificata, ignora spazi e maiuscole. Nel browser."},
    },
    "body": """
<div class="td-grid">
  <div class="tool-card">
    <label>Original</label>
    <textarea id="td-a" oninput="tdRun()" spellcheck="false">The quick brown fox
jumps over the lazy dog.
Line three.
Shared line.</textarea>
  </div>
  <div class="tool-card">
    <label>Changed</label>
    <textarea id="td-b" oninput="tdRun()" spellcheck="false">The quick brown fox
leaps over the lazy dog.
Line three.
Shared line.
A new line at the end.</textarea>
  </div>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>View</label>
      <select id="td-view" onchange="tdRun()">
        <option value="split">Side-by-side</option>
        <option value="unified">Unified</option>
      </select>
    </div>
    <div style="display:flex;flex-direction:column;gap:0.4rem;font-size:0.9rem;justify-content:end">
      <label><input type="checkbox" id="td-ws" onchange="tdRun()"> Ignore whitespace</label>
      <label><input type="checkbox" id="td-case" onchange="tdRun()"> Ignore case</label>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="td-out" class="td-result"></div>
  <div class="meta" id="td-stats" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<style>
.td-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.td-grid textarea{min-height:180px;font-family:ui-monospace,monospace;font-size:0.88rem}
.td-result{font-family:ui-monospace,monospace;font-size:0.86rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;overflow:auto;max-height:520px}
.td-line{display:grid;grid-template-columns:50px 1fr;gap:0;align-items:start;border-bottom:1px solid var(--border)}
.td-line:last-child{border-bottom:none}
.td-line .gut{padding:0.2rem 0.5rem;color:var(--text-muted);font-size:0.78rem;text-align:right;background:var(--bg);user-select:none}
.td-line .body{padding:0.2rem 0.6rem;white-space:pre-wrap;word-break:break-word}
.td-add{background:rgba(16,185,129,0.12)}
.td-add .body{color:#10b981}
.td-add .body::before{content:'+ '}
.td-del{background:rgba(239,68,68,0.12)}
.td-del .body{color:#ef4444}
.td-del .body::before{content:'− '}
.td-eq .body::before{content:'  '}
.td-split{display:grid;grid-template-columns:1fr 1fr}
.td-split>div{overflow:auto;border-right:1px solid var(--border)}
.td-split>div:last-child{border-right:none}
@media(max-width:760px){.td-grid{grid-template-columns:1fr}.td-split{grid-template-columns:1fr}.td-split>div:not(:last-child){border-right:none;border-bottom:1px solid var(--border)}}
</style>
<script>
function tdLcs(a, b){
  const m = a.length, n = b.length;
  const dp = Array.from({length:m+1}, () => new Uint32Array(n+1));
  for(let i=m-1;i>=0;i--) for(let j=n-1;j>=0;j--){
    dp[i][j] = a[i]===b[j] ? dp[i+1][j+1]+1 : Math.max(dp[i+1][j], dp[i][j+1]);
  }
  const ops = [];
  let i=0,j=0;
  while(i<m && j<n){
    if(a[i]===b[j]){ ops.push(['eq', a[i], b[j], i, j]); i++; j++; }
    else if(dp[i+1][j] >= dp[i][j+1]){ ops.push(['del', a[i], null, i, null]); i++; }
    else { ops.push(['add', null, b[j], null, j]); j++; }
  }
  while(i<m){ ops.push(['del', a[i], null, i, null]); i++; }
  while(j<n){ ops.push(['add', null, b[j], null, j]); j++; }
  return ops;
}
function tdRun(){
  const rawA = document.getElementById('td-a').value;
  const rawB = document.getElementById('td-b').value;
  const ws = document.getElementById('td-ws').checked;
  const cs = document.getElementById('td-case').checked;
  const view = document.getElementById('td-view').value;
  const norm = s => { let n = s; if(ws) n = n.replace(/\\s+/g,' ').trim(); if(cs) n = n.toLowerCase(); return n; };
  const linesA = rawA.split('\\n');
  const linesB = rawB.split('\\n');
  const cmpA = linesA.map(norm);
  const cmpB = linesB.map(norm);
  const ops = tdLcs(cmpA, cmpB);
  let adds=0, dels=0;
  ops.forEach(o => { if(o[0]==='add') adds++; else if(o[0]==='del') dels++; });
  const out = document.getElementById('td-out');
  if(view === 'unified'){
    const rows = ops.map(o => {
      if(o[0]==='eq')  return `<div class="td-line td-eq"><div class="gut">${o[3]+1}</div><div class="body">${tdEsc(linesA[o[3]])}</div></div>`;
      if(o[0]==='del') return `<div class="td-line td-del"><div class="gut">${o[3]+1}</div><div class="body">${tdEsc(linesA[o[3]])}</div></div>`;
      return `<div class="td-line td-add"><div class="gut">${o[4]+1}</div><div class="body">${tdEsc(linesB[o[4]])}</div></div>`;
    });
    out.innerHTML = rows.join('');
  } else {
    const left = [], right = [];
    let i=0;
    while(i<ops.length){
      if(ops[i][0]==='eq'){
        left.push(`<div class="td-line td-eq"><div class="gut">${ops[i][3]+1}</div><div class="body">${tdEsc(linesA[ops[i][3]])}</div></div>`);
        right.push(`<div class="td-line td-eq"><div class="gut">${ops[i][4]+1}</div><div class="body">${tdEsc(linesB[ops[i][4]])}</div></div>`);
        i++;
      } else {
        const dels = [], adds = [];
        while(i<ops.length && ops[i][0]==='del'){ dels.push(ops[i]); i++; }
        while(i<ops.length && ops[i][0]==='add'){ adds.push(ops[i]); i++; }
        const max = Math.max(dels.length, adds.length);
        for(let k=0;k<max;k++){
          if(dels[k]) left.push(`<div class="td-line td-del"><div class="gut">${dels[k][3]+1}</div><div class="body">${tdEsc(linesA[dels[k][3]])}</div></div>`);
          else        left.push(`<div class="td-line td-eq"><div class="gut"></div><div class="body"></div></div>`);
          if(adds[k]) right.push(`<div class="td-line td-add"><div class="gut">${adds[k][4]+1}</div><div class="body">${tdEsc(linesB[adds[k][4]])}</div></div>`);
          else        right.push(`<div class="td-line td-eq"><div class="gut"></div><div class="body"></div></div>`);
        }
      }
    }
    out.innerHTML = `<div class="td-split"><div>${left.join('')}</div><div>${right.join('')}</div></div>`;
  }
  document.getElementById('td-stats').textContent = `+${adds} additions · −${dels} deletions · ${ops.length-adds-dels} unchanged`;
}
function tdEsc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') || '&nbsp;'}
document.addEventListener('DOMContentLoaded', tdRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Comparing two versions of a piece of text — a paragraph, a config file, a SQL query, a list — and seeing exactly which lines were added, removed, or left alone. Even when you don't have <code>git diff</code> handy or the text isn't in version control. The output is the same line-level diff you'd see in a code review: green for additions, red for removals, plain for unchanged context.</p>

<h3>When to use it</h3>
<ul>
  <li>Spotting what's different between two emails, contracts, or pasted blobs that "look the same".</li>
  <li>Comparing config files or environment variables across two environments (staging vs prod).</li>
  <li>Reviewing changes to a piece of copy that was edited in Word/Docs by someone else.</li>
  <li>Diffing two query results, log snippets, or JSON blobs (use the JSON Formatter first to canonicalize).</li>
  <li>Quick sanity check on a search-and-replace before committing it.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — easier to scan small changes line-by-line; the original is on the left, the new version on the right.</li>
  <li><strong>Unified</strong> — closer to <code>git diff</code> output; better for sharing or printing, and easier to follow when changes are sparse.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a line diff, not a word diff.</strong> One character changed in the middle of a long line marks the entire line as changed. For prose-level diffing of paragraphs, you may want a tool that tokenises into words.</li>
  <li><strong>"Ignore whitespace" affects comparison only, not display.</strong> Lines that differ only in trailing spaces or indentation collapse into the unchanged column, but the original whitespace is still shown.</li>
  <li><strong>"Ignore case" likewise.</strong> "TODO" and "todo" compare equal, but the original casing is rendered.</li>
  <li><strong>Order matters.</strong> If you swap two lines, the diff shows both as removed-and-re-added, not as a "moved" pair. There's no move detection.</li>
  <li><strong>Big inputs (10k+ lines) can be slow.</strong> The LCS algorithm is O(m·n) — fine for typical files, sluggish for very large ones. Diff small chunks at a time.</li>
  <li><strong>Trailing newlines</strong> count as a line. Two inputs that differ only in whether they end with a newline will show one trailing addition or removal.</li>
</ul>
""",
    },
    "related": ["json-formatter", "case-converter", "regex-tester"],
}
