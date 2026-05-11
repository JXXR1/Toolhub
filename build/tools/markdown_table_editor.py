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
        "pt": {"name": "Editor de Tabelas Markdown", "tagline": "Edite uma tabela visualmente — linhas, colunas, alinhamento por coluna — e copie o Markdown estilo GitHub.", "description": "Editor de tabelas Markdown gratuito online. Clique nas células para editar, adicione/remova linhas e colunas, defina alinhamento por coluna e copie o Markdown estilo GitHub (GFM). Roda inteiramente no seu navegador."},
        "pl": {"name": "Edytor Tabel Markdown", "tagline": "Edytuj tabelę wizualnie — wiersze, kolumny, wyrównanie per kolumna — i skopiuj Markdown w stylu GitHuba.", "description": "Darmowy online edytor tabel Markdown. Klikaj komórki, by edytować, dodawaj/usuwaj wiersze i kolumny, ustaw wyrównanie per kolumna i skopiuj wyjście Markdown w stylu GitHuba (GFM). Działa w całości w przeglądarce."},
        "ja": {"name": "Markdown テーブルエディター", "tagline": "テーブルをビジュアルに編集 — 行・列・列ごとの揃えまで — して、GitHub 風 Markdown をコピー。", "description": "オンライン無料の Markdown テーブルエディター。セルをクリックして編集、行や列を追加／削除、列ごとの揃えを設定し、GitHub 風 Markdown 出力をコピーできます。すべてブラウザ内で動作します。"},
        "nl": {"name": "Markdown Table Editor", "tagline": "Bewerk visueel een tabel — rows, kolommen, alignment per kolom — en kopieer de GitHub-flavoured Markdown.", "description": "Gratis online Markdown table editor. Klik cellen om te bewerken, voeg rows en kolommen toe of verwijder, stel per-kolom alignment in en kopieer de GitHub-flavoured Markdown output. Draait volledig in je browser."},
    },
    "body": """
<div class="tool-card">
  <div class="button-row">
    <button class="secondary" onclick="mtAddRow()" aria-label="Add row">+ Row</button>
    <button class="secondary" onclick="mtAddCol()" aria-label="Add column">+ Column</button>
    <button class="secondary" onclick="mtDelRow()" aria-label="Remove row">− Row</button>
    <button class="secondary" onclick="mtDelCol()" aria-label="Remove column">− Column</button>
    <button class="secondary" onclick="mtClear()">{LBL_RESET}</button>
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
#mt-table input { width: 100%; padding: 0.4rem 0.5rem; background: transparent; border: none; color: var(--text); font-family: inherit; font-size: 0.88rem; min-height: auto; }
#mt-table input:focus { background: var(--surface); outline: 2px solid var(--accent); }
#mt-table select { width: 100%; padding: 0.3rem 0.5rem; background: var(--surface); border: none; color: var(--text-muted); font-size: 0.78rem; border-radius: 0; min-height: auto; }
#mt-table thead tr:first-child input { font-weight: 600; }
@media (max-width: 600px) {
  #mt-table input { font-size: 16px; padding: 0.55rem 0.5rem; }
  #mt-table select { font-size: 0.85rem; padding: 0.45rem 0.5rem; }
}
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

document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(mtRender));
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
        "pt": """
<h2>Para que serve?</h2>
<p>Tabelas Markdown ficam ótimas no resultado renderizado e são chatas de escrever na mão. Caracteres pipe, dois-pontos de alinhamento, o número certo de traços por coluna — quando você termina de ajustar tudo, podia ter escrito em HTML. Este editor te dá uma grade familiar: clique em qualquer célula para editar, use os botões para adicionar ou remover linhas e colunas, defina alinhamento por coluna num dropdown e copie o Markdown estilo GitHub quando terminar. Você também pode colar uma tabela Markdown existente embaixo e ela é carregada na grade para edição.</p>

<h3>Quando usar</h3>
<ul>
  <li>Criar uma tabela comparativa para um README, issue do GitHub ou descrição de PR.</li>
  <li>Reeditar uma tabela de uma documentação — cole o Markdown existente, ajuste na grade, copie de volta.</li>
  <li>Produzir uma tabela ASCII com padding alinhado (a saída tem padding à direita, então também é legível como texto puro).</li>
  <li>Rascunhar uma tabela de release notes sem brigar com a sintaxe de pipes e traços.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Pipes inline quebram tabelas GFM.</strong> Um <code>|</code> literal dentro de uma célula encerra a célula. Faça escape como <code>\\|</code> quando precisar.</li>
  <li><strong>Conteúdo da célula é de uma linha só.</strong> Tabelas Markdown não suportam quebras de linha dentro de células sem HTML (<code>&lt;br&gt;</code>). Para conteúdo multilinha, escreva a tabela em HTML.</li>
  <li><strong>Alinhamento é renderizado, não forçado.</strong> A saída também aplica padding para alinhar no source, mas o alinhamento renderizado de fato vem dos dois-pontos na linha separadora, não do espaçamento.</li>
  <li><strong>A primeira linha sempre é tratada como header.</strong> Tabelas GFM têm header obrigatório. Se seus dados não têm um header natural, use células em branco na linha 1.</li>
  <li><strong>Algumas variantes Markdown são mais rígidas que GFM.</strong> O CommonMark em si não define tabelas; GFM, MultiMarkdown e várias outras suportam variantes ligeiramente diferentes. A saída aqui mira GFM (GitHub, GitLab, a maioria dos renderers modernos).</li>
  <li><strong>Colar um CSV sem formatação não funciona.</strong> A textarea de "import" espera uma tabela Markdown (com o separador <code>|---|</code>). Para CSV → Markdown, use a ferramenta CSV-to-JSON primeiro ou cole as linhas na mão.</li>
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
        "pl": """
<h2>Do czego to służy?</h2>
<p>Tabele Markdown są świetne w wyrenderowanym wyniku i upierdliwe w pisaniu ręcznie. Pipe'y, dwukropki wyrównania, odpowiednia liczba kresek per kolumna — zanim ułożysz wszystko na miejscu, mogłeś napisać to w HTML-u. Ten edytor daje znajomą siatkę: kliknij dowolną komórkę, żeby edytować, używaj przycisków do dodawania albo usuwania wierszy i kolumn, ustaw wyrównanie per kolumna z dropdowna, a potem skopiuj Markdowna w stylu GitHuba. Możesz też wkleić istniejącą tabelę Markdown na dole, a załaduje się do siatki do dalszej edycji.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Pisanie tabeli porównawczej do README, GitHub issue albo opisu PR.</li>
  <li>Reedycja tabeli z dokumentacji — wklej istniejącego Markdowna, podstrojuj w siatce, skopiuj z powrotem.</li>
  <li>Generowanie poprawnie wyrównanej tabeli ASCII (wyjście jest paddowane z prawej, więc jest też czytelne jako zwykły tekst).</li>
  <li>Szkic tabeli release notes bez walki ze składnią pipe'ów i myślników.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Inline'owe pipe'y łamią tabele GFM.</strong> Dosłowny <code>|</code> w komórce kończy komórkę. Escape'uj jako <code>\\|</code>, kiedy go potrzebujesz.</li>
  <li><strong>Treść komórki jest jednoliniowa.</strong> Tabele Markdown nie wspierają końców linii w komórkach bez HTML-a (<code>&lt;br&gt;</code>). Do treści wieloliniowej pisz tabelę w HTML.</li>
  <li><strong>Wyrównanie jest renderowane, nie wymuszane.</strong> Wyjście paddinguje też tak, żeby wyrównać w źródle, ale faktyczne wyrównanie w renderze bierze się z dwukropków w linii separatora, nie ze spacji.</li>
  <li><strong>Pierwszy wiersz zawsze jest traktowany jako nagłówek.</strong> Tabele GFM mają obowiązkowy header. Jeśli twoje dane nie mają naturalnego nagłówka, używaj pustych komórek w wierszu 1.</li>
  <li><strong>Niektóre dialekty Markdowna są surowsze niż GFM.</strong> CommonMark sam nie definiuje tabel; GFM, MultiMarkdown i kilka innych wspierają lekko różne warianty. Wyjście tu celuje w GFM (GitHub, GitLab, większość nowoczesnych rendererów).</li>
  <li><strong>Wklejenie niezformatowanego CSV nie zadziała.</strong> Textarea "import" oczekuje tabeli Markdown (z separatorem <code>|---|</code>). Do CSV → Markdown użyj najpierw narzędzia CSV-to-JSON albo wklej wiersze ręcznie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>Markdown のテーブルはレンダリング後の見た目は良い一方、手書きは面倒です。パイプ、揃えのコロン、列ごとに必要なハイフン数 — 全部を整える頃には HTML で書いた方が早かった、ということになりがちです。本エディターは見慣れたグリッドを提供します。セルをクリックして編集、ボタンで行・列の追加削除、列単位の揃えをドロップダウンから設定、最後に GitHub 風 Markdown をコピーできます。下部に既存の Markdown テーブルを貼ると、グリッドにロードして編集を続けられます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>README、GitHub issue、PR の説明用に比較表を作りたいとき。</li>
  <li>ドキュメントの既存テーブルを編集したいとき — 既存 Markdown を貼ってグリッドで調整、コピーして戻せます。</li>
  <li>桁を揃えた ASCII テーブルとしても読める出力（右パディングされるので素のテキストでも読みやすい）が必要なとき。</li>
  <li>パイプとハイフンの構文と戦わずにリリースノートのテーブルを下書きしたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>セル内のパイプは GFM テーブルを壊します。</strong> セル内のリテラル <code>|</code> はセルを終端させます。必要なら <code>\\|</code> でエスケープしてください。</li>
  <li><strong>セルは 1 行のみ。</strong> Markdown テーブルは HTML（<code>&lt;br&gt;</code>）なしではセル内改行に対応しません。複数行が必要なら HTML テーブルで書きましょう。</li>
  <li><strong>揃えは描画されますが強制ではありません。</strong> 出力はソース上も整えるためにパディングしますが、レンダリングでの揃えはあくまで区切り行のコロンに依存し、空白の数ではありません。</li>
  <li><strong>1 行目は常にヘッダーとして扱われます。</strong> GFM テーブルにはヘッダーが必須です。自然なヘッダーがない場合は 1 行目を空セルにしてください。</li>
  <li><strong>Markdown 方言によっては GFM より厳しいです。</strong> CommonMark はそもそもテーブルを定義していません。GFM、MultiMarkdown などで微妙に異なる方言があります。本ツールの出力は GFM（GitHub、GitLab、ほとんどのモダンレンダラー）を対象としています。</li>
  <li><strong>素の CSV は読み込めません。</strong> インポート用テキストエリアは <code>|---|</code> 区切りを含む Markdown テーブルを期待します。CSV → Markdown 変換が必要なら、CSV-to-JSON ツールを経由するか、手で行を貼り付けてください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Markdown-tabellen zijn top in de rendered output en ellendig om met de hand te schrijven. Pipe-tekens, alignment-colons, het juiste aantal streepjes per kolom — tegen de tijd dat je alles op zijn plek hebt geduwd, had je het als HTML kunnen schrijven. Deze editor geeft je een vertrouwd grid: klik elke cel om te bewerken, gebruik de knoppen om rows en kolommen toe te voegen of te verwijderen, stel alignment per kolom in vanuit een dropdown en kopieer de GitHub-flavoured Markdown wanneer je klaar bent. Je kunt ook een bestaande Markdown-tabel onderaan plakken en die wordt in het grid geladen voor verder bewerken.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een vergelijkings-tabel maken voor een README, GitHub issue of PR-beschrijving.</li>
  <li>Een tabel uit een doc opnieuw bewerken — plak de bestaande Markdown, tweak in het grid, kopieer terug.</li>
  <li>Een goed-uitgelijnde ASCII-padded tabel produceren (de output is rechts-padded zodat hij ook als plain text leesbaar is).</li>
  <li>Een release-notes tabel opstellen zonder met de pipe-and-dash syntax te vechten.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Inline pipes breken GFM-tabellen.</strong> Een letterlijke <code>|</code> in een cel beëindigt de cel. Escape het als <code>\|</code> wanneer je het nodig hebt.</li>
  <li><strong>Cel-content is single-line.</strong> Markdown-tabellen ondersteunen geen line breaks in cellen zonder HTML (<code>&lt;br&gt;</code>). Voor multi-line content schrijf je de tabel in HTML.</li>
  <li><strong>Alignment is rendered, niet enforced.</strong> De output padt ook om in de source uit te lijnen, maar de daadwerkelijke rendered alignment komt van de colons in de separator-row, niet van de spacing.</li>
  <li><strong>De eerste row wordt altijd als header behandeld.</strong> GFM-tabellen hebben een verplichte header. Als je data geen natuurlijke header heeft, gebruik blanke cellen in row 1.</li>
  <li><strong>Sommige Markdown-flavours zijn strenger dan GFM.</strong> CommonMark zelf definieert geen tabellen; GFM, MultiMarkdown en diverse andere ondersteunen lichtjes verschillende varianten. De output hier targets GFM (GitHub, GitLab, de meeste moderne renderers).</li>
  <li><strong>Een unformatted CSV plakken werkt niet.</strong> Het "import"-textarea verwacht een Markdown-tabel (met de <code>|---|</code> separator). Voor CSV → Markdown gebruik de CSV-to-JSON tool eerst of plak rijen met de hand.</li>
</ul>
""",
    },
    "related": ["markdown-to-html", "csv-to-json", "json-to-csv", "ascii-table"],
    "howto": {"flow": "transform", "action": "format",  "noun": "table"},
}
