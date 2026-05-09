TOOL = {
    "slug": "markdown-table-editor",
    "category": "text",
    "icon": "▦",
    "tags": ["markdown", "table", "editor", "github", "gfm", "alignment"],
    "i18n": {
        "en": {
            "name": "Markdown Table Editor",
            "tagline": "Visually edit a table — rows, columns, alignment per column — and copy the GitHub-flavoured Markdown.",
            "description": "Free online Markdown table editor. Click cells to edit, add/remove rows and columns, set per-column alignment, and copy the GitHub-flavoured Markdown output. Runs entirely in your browser.",
        },
        "de": {"name": "Markdown-Tabellen-Editor", "tagline": "Tabelle visuell bearbeiten — Zeilen, Spalten, Ausrichtung pro Spalte — und das GitHub-Markdown kopieren.", "description": "Kostenloser Markdown-Tabellen-Editor. Zellen klicken und bearbeiten, Zeilen/Spalten hinzufügen/entfernen, Ausrichtung pro Spalte setzen und GitHub-Markdown kopieren. Komplett im Browser."},
        "es": {"name": "Editor de Tablas Markdown", "tagline": "Edita visualmente una tabla — filas, columnas, alineación por columna — y copia el Markdown estilo GitHub.", "description": "Editor de tablas Markdown gratuito. Haz clic en celdas para editar, añade/quita filas y columnas, define alineación por columna y copia el Markdown GFM. 100% en el navegador."},
        "fr": {"name": "Éditeur de Tableau Markdown", "tagline": "Éditez visuellement un tableau — lignes, colonnes, alignement par colonne — et copiez le Markdown GitHub.", "description": "Éditeur de tableau Markdown gratuit. Cliquez pour éditer, ajoutez/supprimez lignes et colonnes, alignement par colonne et copie du Markdown GFM. 100% dans le navigateur."},
        "it": {"name": "Editor di Tabelle Markdown", "tagline": "Modifica visualmente una tabella — righe, colonne, allineamento per colonna — e copia il Markdown stile GitHub.", "description": "Editor di tabelle Markdown gratuito. Clicca le celle per modificare, aggiungi/rimuovi righe e colonne, allineamento per colonna e copia il Markdown GFM. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <div class="button-row">
    <button class="secondary" onclick="mtAddRow()">+ Row</button>
    <button class="secondary" onclick="mtAddCol()">+ Column</button>
    <button class="secondary" onclick="mtDelRow()">− Row</button>
    <button class="secondary" onclick="mtDelCol()">− Column</button>
    <button class="secondary" onclick="mtClear()">Reset</button>
  </div>
  <div style="overflow-x:auto;border:1px solid var(--border);border-radius:6px;background:var(--code-bg);padding:0.4rem">
    <table id="mt-table" style="border-collapse:collapse;width:100%;min-width:300px">
      <thead><tr id="mt-head"></tr></thead>
      <thead><tr id="mt-align"></tr></thead>
      <tbody id="mt-body"></tbody>
    </table>
  </div>
  <div class="meta" style="margin-top:0.5rem">Click any cell to edit. Use the dropdown row to set per-column alignment.</div>
</div>
<div class="tool-card">
  <label>Paste an existing Markdown table (optional)</label>
  <textarea id="mt-import" oninput="mtImport()" spellcheck="false" placeholder="| col 1 | col 2 |&#10;|---|---|&#10;| a | b |" style="min-height:100px"></textarea>
</div>
<div class="tool-card">
  <label>Markdown {LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="mt-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('mt-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<style>
#mt-table th, #mt-table td { border: 1px solid var(--border); padding: 0; min-width: 70px; }
#mt-table input { width: 100%; padding: 0.4rem 0.5rem; background: transparent; border: none; color: var(--text); font-family: inherit; font-size: 0.88rem; }
#mt-table input:focus { background: var(--surface); outline: 2px solid var(--accent); }
#mt-table select { width: 100%; padding: 0.3rem 0.5rem; background: var(--surface); border: none; color: var(--text-muted); font-size: 0.78rem; border-radius: 0; }
#mt-table thead tr:first-child input { font-weight: 600; }
</style>
<script>
let MT = {
  cols: 3,
  rows: 2,
  align: ['left','left','left'],
  data: [
    ['Header 1','Header 2','Header 3'],
    ['Cell A1','Cell B1','Cell C1'],
    ['Cell A2','Cell B2','Cell C2']
  ]
};

function mtRender(){
  const head = document.getElementById('mt-head');
  const align = document.getElementById('mt-align');
  const body = document.getElementById('mt-body');
  head.innerHTML = '';
  align.innerHTML = '';
  body.innerHTML = '';
  for(let c = 0; c < MT.cols; c++){
    const th = document.createElement('th');
    const inp = document.createElement('input');
    inp.value = MT.data[0][c] ?? '';
    inp.dataset.r = 0; inp.dataset.c = c;
    inp.oninput = () => { MT.data[0][c] = inp.value; mtBuildOutput(); };
    th.appendChild(inp);
    head.appendChild(th);
  }
  for(let c = 0; c < MT.cols; c++){
    const th = document.createElement('th');
    const sel = document.createElement('select');
    ['left','center','right'].forEach(a => {
      const o = document.createElement('option');
      o.value = a; o.textContent = a;
      if(MT.align[c] === a) o.selected = true;
      sel.appendChild(o);
    });
    sel.onchange = () => { MT.align[c] = sel.value; mtBuildOutput(); };
    th.appendChild(sel);
    align.appendChild(th);
  }
  for(let r = 1; r < MT.rows + 1; r++){
    const tr = document.createElement('tr');
    for(let c = 0; c < MT.cols; c++){
      const td = document.createElement('td');
      const inp = document.createElement('input');
      inp.value = MT.data[r] ? (MT.data[r][c] ?? '') : '';
      inp.dataset.r = r; inp.dataset.c = c;
      inp.oninput = () => {
        if(!MT.data[r]) MT.data[r] = [];
        MT.data[r][c] = inp.value;
        mtBuildOutput();
      };
      td.appendChild(inp);
      tr.appendChild(td);
    }
    body.appendChild(tr);
  }
  mtBuildOutput();
}

function mtAddRow(){
  MT.rows++;
  MT.data.push(new Array(MT.cols).fill(''));
  mtRender();
}
function mtDelRow(){
  if(MT.rows <= 1) return;
  MT.rows--;
  MT.data.pop();
  mtRender();
}
function mtAddCol(){
  MT.cols++;
  MT.align.push('left');
  for(let r = 0; r < MT.data.length; r++){
    MT.data[r].push(r === 0 ? 'Header ' + MT.cols : '');
  }
  mtRender();
}
function mtDelCol(){
  if(MT.cols <= 1) return;
  MT.cols--;
  MT.align.pop();
  for(let r = 0; r < MT.data.length; r++) MT.data[r].pop();
  mtRender();
}
function mtClear(){
  MT = {
    cols: 3, rows: 2, align: ['left','left','left'],
    data: [['Header 1','Header 2','Header 3'], ['','',''], ['','','']]
  };
  document.getElementById('mt-import').value = '';
  mtRender();
}

function mtPad(s, n){
  s = String(s);
  if(s.length >= n) return s;
  return s + ' '.repeat(n - s.length);
}
function mtAlignBar(width, mode){
  const w = Math.max(width, 3);
  if(mode === 'center') return ':' + '-'.repeat(w-2) + ':';
  if(mode === 'right') return '-'.repeat(w-1) + ':';
  return '-'.repeat(w);
}
function mtBuildOutput(){
  const widths = new Array(MT.cols).fill(3);
  for(let r = 0; r < MT.rows + 1; r++){
    for(let c = 0; c < MT.cols; c++){
      const v = (MT.data[r] && MT.data[r][c]) || '';
      widths[c] = Math.max(widths[c], v.length);
    }
  }
  const lines = [];
  // header
  lines.push('| ' + MT.data[0].map((v,c) => mtPad(v ?? '', widths[c])).join(' | ') + ' |');
  // separator
  lines.push('| ' + widths.map((w,c) => mtAlignBar(w, MT.align[c])).join(' | ') + ' |');
  // body
  for(let r = 1; r < MT.rows + 1; r++){
    const row = MT.data[r] || [];
    lines.push('| ' + new Array(MT.cols).fill(0).map((_,c) => mtPad(row[c] ?? '', widths[c])).join(' | ') + ' |');
  }
  document.getElementById('mt-out').textContent = lines.join('\\n');
}

function mtImport(){
  const txt = document.getElementById('mt-import').value;
  if(!txt.trim()) return;
  const lines = txt.split('\\n').filter(l => /\\|/.test(l));
  if(lines.length < 2) return;
  function splitRow(l){
    let s = l.trim();
    if(s.startsWith('|')) s = s.slice(1);
    if(s.endsWith('|')) s = s.slice(0, -1);
    return s.split('|').map(c => c.trim());
  }
  const header = splitRow(lines[0]);
  const sep = splitRow(lines[1]);
  if(!sep.every(c => /^:?-+:?$/.test(c))) return;
  const align = sep.map(c => {
    const left = c.startsWith(':');
    const right = c.endsWith(':');
    if(left && right) return 'center';
    if(right) return 'right';
    return 'left';
  });
  const body = lines.slice(2).map(splitRow);
  MT.cols = header.length;
  MT.rows = body.length;
  if(MT.rows === 0){ MT.rows = 1; body.push(new Array(MT.cols).fill('')); }
  MT.align = align;
  MT.data = [header, ...body.map(r => {
    const out = r.slice(0, MT.cols);
    while(out.length < MT.cols) out.push('');
    return out;
  })];
  mtRender();
}

document.addEventListener('DOMContentLoaded', mtRender);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Markdown tables are great in the rendered output and miserable to write by hand. Pipe characters, alignment colons, the right number of dashes per column — by the time you've nudged everything into place, you could have written it as HTML. This editor gives you a familiar grid: click any cell to edit, use the buttons to add or remove rows and columns, set alignment per column from a dropdown, and copy the GitHub-flavoured Markdown when you're done. You can also paste an existing Markdown table at the bottom and it'll load into the grid for further editing.</p>

<h3>When to use it</h3>
<ul>
  <li>Authoring a comparison table for a README, GitHub issue, or PR description.</li>
  <li>Re-editing a table from a doc — paste the existing Markdown, tweak in the grid, copy back.</li>
  <li>Producing a properly-aligned ASCII-padded table (the output is right-padded so it's also readable as plain text).</li>
  <li>Drafting a release-notes table without fighting the pipe-and-dash syntax.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Inline pipes break GFM tables.</strong> A literal <code>|</code> inside a cell ends the cell. Escape it as <code>\\|</code> when you need it.</li>
  <li><strong>Cell content is single-line.</strong> Markdown tables don't support line breaks inside cells without HTML (<code>&lt;br&gt;</code>). For multi-line content, write the table in HTML.</li>
  <li><strong>Alignment is rendered, not enforced.</strong> The output also pads to align in the source, but the actual rendered alignment comes from the colons in the separator row, not the spacing.</li>
  <li><strong>The first row is always treated as the header.</strong> GFM tables have a mandatory header. If your data has no natural header, use blank cells in row 1.</li>
  <li><strong>Some Markdown flavours are stricter than GFM.</strong> CommonMark itself doesn't define tables; GFM, MultiMarkdown, and various others all support slightly different variants. The output here targets GFM (GitHub, GitLab, most modern renderers).</li>
  <li><strong>Pasting an unformatted CSV won't work.</strong> The "import" textarea expects a Markdown table (with the <code>|---|</code> separator). For CSV → Markdown, use the CSV-to-JSON tool first or hand-paste rows.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Markdown-Tabellen sind toll im Rendering und mühsam von Hand zu schreiben. Dieser Editor gibt dir ein Raster: Zelle anklicken zum Bearbeiten, Buttons für Zeilen/Spalten, Ausrichtung pro Spalte. Existierende Markdown-Tabelle kann unten eingefügt und ins Raster geladen werden.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Vergleichstabelle für README/Issue/PR erstellen.</li>
<li>Bestehende Tabelle einfügen, anpassen, zurückkopieren.</li>
<li>Korrekt ausgerichtete ASCII-Tabelle erzeugen.</li>
<li>Release-Notes-Tabelle ohne Pipe-Stress.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Pipes brechen Tabellen.</strong> <code>|</code> in Zellen mit <code>\\|</code> escapen.</li>
<li><strong>Zellen sind einzeilig.</strong> Für Mehrzeiligkeit HTML <code>&lt;br&gt;</code>.</li>
<li><strong>Ausrichtung kommt aus den Doppelpunkten</strong>, nicht aus dem Padding.</li>
<li><strong>Erste Zeile ist immer Header.</strong></li>
<li><strong>Nicht alle Markdown-Varianten gleich.</strong> Output zielt auf GFM.</li>
<li><strong>CSV-Paste funktioniert nicht.</strong> Erwartet Markdown-Tabelle mit <code>|---|</code>.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Las tablas Markdown se renderizan bien pero son tediosas a mano. Este editor te da una cuadrícula: clic para editar, botones para filas/columnas, alineación por columna. Pega una tabla Markdown existente abajo para cargarla.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Crear tabla de comparación para README/Issue/PR.</li>
<li>Pegar tabla existente, ajustar, copiar.</li>
<li>Generar ASCII alineado.</li>
<li>Tabla de release notes sin pelearse con pipes.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Pipes rompen tablas.</strong> Escapa <code>|</code> en celdas como <code>\\|</code>.</li>
<li><strong>Celdas de una línea.</strong> Para varias líneas usa <code>&lt;br&gt;</code> HTML.</li>
<li><strong>La alineación viene de los dos puntos</strong>, no del padding.</li>
<li><strong>Primera fila siempre es header.</strong></li>
<li><strong>No todos los Markdown soportan tablas.</strong> El output apunta a GFM.</li>
<li><strong>Pegar CSV no funciona.</strong> Espera tabla Markdown con <code>|---|</code>.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Les tableaux Markdown s'affichent bien mais sont pénibles à écrire à la main. Cet éditeur offre une grille : clic pour éditer, boutons pour lignes/colonnes, alignement par colonne. Collez un tableau Markdown existant en bas pour le charger.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Créer un tableau comparatif pour README/Issue/PR.</li>
<li>Coller un tableau existant, ajuster, recopier.</li>
<li>Générer un ASCII aligné.</li>
<li>Tableau de release-notes sans bagarre avec les pipes.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Les pipes cassent les tableaux.</strong> Échapper <code>|</code> en <code>\\|</code> dans les cellules.</li>
<li><strong>Cellules sur une ligne.</strong> Pour multilignes utiliser <code>&lt;br&gt;</code> HTML.</li>
<li><strong>L'alignement vient des deux-points</strong>, pas du padding.</li>
<li><strong>La première ligne est toujours l'en-tête.</strong></li>
<li><strong>Toutes les variantes Markdown ne supportent pas les tableaux.</strong> Sortie cible GFM.</li>
<li><strong>Coller du CSV ne marche pas.</strong> Attend un tableau Markdown avec <code>|---|</code>.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Le tabelle Markdown si rendono bene ma sono tediose a mano. Questo editor offre una griglia: clic per modificare, pulsanti per righe/colonne, allineamento per colonna. Incolla una tabella Markdown esistente in basso per caricarla.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Creare tabella di confronto per README/Issue/PR.</li>
<li>Incollare tabella esistente, modificare, copiare.</li>
<li>Generare ASCII allineato.</li>
<li>Tabella di release notes senza lottare con i pipe.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>I pipe rompono le tabelle.</strong> Esci <code>|</code> nelle celle come <code>\\|</code>.</li>
<li><strong>Celle a una riga.</strong> Per più righe usa <code>&lt;br&gt;</code> HTML.</li>
<li><strong>L'allineamento viene dai due punti</strong>, non dal padding.</li>
<li><strong>La prima riga è sempre l'header.</strong></li>
<li><strong>Non tutte le varianti Markdown supportano tabelle.</strong> Output mira a GFM.</li>
<li><strong>Incollare CSV non funziona.</strong> Si aspetta tabella Markdown con <code>|---|</code>.</li>
</ul>
""",
    },
    "related": ["markdown-to-html", "csv-to-json", "json-to-csv", "ascii-table"],
}
