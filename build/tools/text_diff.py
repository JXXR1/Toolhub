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
        "pt": {"name": "Diff de Texto", "tagline": "Compare dois blocos de texto e veja adições, remoções e contexto inalterado linha a linha. Visão lado a lado ou unificada.", "description": "Ferramenta de diff de texto gratuita online. Diff de Myers em nível de linha com visão lado a lado e unificada, com toggles para ignorar whitespace e ignorar case. Roda no navegador."},
        "pl": {"name": "Diff Tekstu", "tagline": "Porównaj dwa bloki tekstu i zobacz dodania, usunięcia i niezmieniony kontekst linia po linii. Widok side-by-side albo unified.", "description": "Darmowe narzędzie do diffowania tekstu online. Myers diff na poziomie linii z widokiem side-by-side i unified, togle do ignorowania białych znaków i wielkości liter. Działa w przeglądarce."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>Comparar duas versões de um trecho de texto — um parágrafo, um arquivo de config, uma query SQL, uma lista — e ver exatamente quais linhas foram adicionadas, removidas ou ficaram iguais. Mesmo quando você não tem <code>git diff</code> à mão ou o texto não está em controle de versão. A saída é o mesmo diff em nível de linha que você veria num code review: verde para adições, vermelho para remoções, plano para contexto inalterado.</p>

<h3>Quando usar</h3>
<ul>
  <li>Detectar o que está diferente entre dois e-mails, contratos ou blocos colados que "parecem iguais".</li>
  <li>Comparar arquivos de config ou variáveis de ambiente entre dois ambientes (staging vs prod).</li>
  <li>Revisar mudanças num texto que foi editado no Word/Docs por outra pessoa.</li>
  <li>Fazer diff de dois resultados de query, trechos de log ou blobs JSON (use o JSON Formatter primeiro para canonicalizar).</li>
  <li>Verificação rápida de sanidade num search-and-replace antes de commitar.</li>
</ul>

<h3>Lado a lado vs unificada</h3>
<ul>
  <li><strong>Lado a lado</strong> — mais fácil de scanear pequenas mudanças linha a linha; o original fica à esquerda, a versão nova à direita.</li>
  <li><strong>Unificada</strong> — mais próxima da saída do <code>git diff</code>; melhor para compartilhar ou imprimir, e mais fácil de acompanhar quando as mudanças são esparsas.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Isto é diff de linha, não de palavra.</strong> Um caractere alterado no meio de uma linha longa marca a linha inteira como alterada. Para diff em nível de prosa de parágrafos, talvez você queira uma ferramenta que tokenize em palavras.</li>
  <li><strong>"Ignorar whitespace" afeta só a comparação, não a exibição.</strong> Linhas que diferem apenas em espaços no fim ou indentação caem na coluna inalterada, mas o whitespace original continua sendo mostrado.</li>
  <li><strong>"Ignorar case" do mesmo jeito.</strong> "TODO" e "todo" comparam iguais, mas o case original é renderizado.</li>
  <li><strong>Ordem importa.</strong> Se você troca duas linhas de lugar, o diff mostra as duas como removidas-e-readicionadas, não como um par "movido". Não há detecção de movimento.</li>
  <li><strong>Entradas grandes (10k+ linhas) podem ser lentas.</strong> O algoritmo LCS é O(m·n) — tudo bem para arquivos típicos, lento para muito grandes. Faça diff em pedaços pequenos.</li>
  <li><strong>Newlines no final</strong> contam como linha. Duas entradas que diferem só em terminar ou não com newline vão mostrar uma adição ou remoção no final.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Porównanie dwóch wersji kawałka tekstu — akapitu, pliku configa, query SQL, listy — i zobaczenie, które linie dokładnie zostały dodane, usunięte albo zostały bez zmian. Nawet kiedy nie masz pod ręką <code>git diff</code> albo tekst nie jest w version control. Wyjście to ten sam line-level diff, jaki widzisz w code review: zielony dla dodań, czerwony dla usunięć, zwykły dla niezmienionego kontekstu.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wykrycie, czym się różnią dwa maile, kontrakty albo wklejone bloby, które "wyglądają tak samo".</li>
  <li>Porównanie configów albo zmiennych środowiskowych między dwoma środowiskami (staging vs prod).</li>
  <li>Review zmian w copy, które ktoś inny edytował w Wordzie/Docsach.</li>
  <li>Diff dwóch wyników query, snippetów logów albo blobów JSON (najpierw przepuść przez JSON Formatter, żeby skanonizować).</li>
  <li>Szybki sanity check search-and-replace przed zacommitowaniem.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — łatwiej skanować małe zmiany linia po linii; oryginał po lewej, nowa wersja po prawej.</li>
  <li><strong>Unified</strong> — bliższe wyjściu <code>git diff</code>; lepsze do dzielenia się albo drukowania, łatwiejsze do śledzenia, gdy zmiany są rozproszone.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To diff linii, nie słów.</strong> Jeden zmieniony znak w środku długiej linii oznacza całą linię jako zmienioną. Do diffowania prozatorskiego na poziomie akapitów może chcesz narzędzia, które tokenizuje na słowa.</li>
  <li><strong>"Ignoruj białe znaki" wpływa tylko na porównanie, nie na wyświetlanie.</strong> Linie różniące się tylko końcowymi spacjami albo wcięciem zwijają się w niezmienioną kolumnę, ale oryginalny whitespace nadal jest pokazany.</li>
  <li><strong>"Ignoruj case" tak samo.</strong> "TODO" i "todo" porównują się jako równe, ale oryginalna wielkość liter jest renderowana.</li>
  <li><strong>Kolejność ma znaczenie.</strong> Jeśli zamienisz dwie linie miejscami, diff pokaże obie jako usunięte-i-dodane-na-nowo, nie jako parę "przeniesioną". Nie ma detekcji przenosin.</li>
  <li><strong>Duże inputy (10k+ linii) bywają wolne.</strong> Algorytm LCS jest O(m·n) — OK dla typowych plików, ślamazarny dla bardzo dużych. Diffuj małymi kawałkami.</li>
  <li><strong>Końcowe newliny</strong> liczą się jako linia. Dwa inputy różniące się tylko tym, czy kończą się newlinem, pokażą jedno końcowe dodanie albo usunięcie.</li>
</ul>
""",
    },
    "related": ["json-formatter", "case-converter", "regex-tester"],
}
