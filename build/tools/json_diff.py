TOOL = {
    "slug": "json-diff",
    "category": "developer",
    "icon": "{}±",
    "tags": ["json", "diff", "compare", "structural", "delta", "merge"],
    "i18n": {
        "en": {
            "name": "JSON Diff",
            "tagline": "Structural diff for two JSON documents — keys added, removed, changed, and value changes shown side by side.",
            "description": "Free online JSON diff. Computes a structural delta between two JSON documents — added/removed keys, changed values, and a clean side-by-side view. Runs entirely in your browser.",
        },
        "de": {"name": "JSON-Diff", "tagline": "Strukturelles Diff zweier JSON-Dokumente — hinzugefügte, entfernte und geänderte Schlüssel und Werte nebeneinander.", "description": "Kostenloses JSON-Diff. Berechnet ein strukturelles Delta zwischen zwei JSON-Dokumenten — Schlüssel hinzugefügt/entfernt, Werte geändert. Komplett im Browser."},
        "es": {"name": "Diff JSON", "tagline": "Diff estructural entre dos documentos JSON — claves añadidas, eliminadas, modificadas y cambios de valor lado a lado.", "description": "Diff JSON gratuito. Calcula un delta estructural entre dos documentos JSON — claves añadidas/eliminadas, valores modificados. 100% en el navegador."},
        "fr": {"name": "Diff JSON", "tagline": "Diff structurel entre deux documents JSON — clés ajoutées, supprimées, modifiées et changements de valeur côte à côte.", "description": "Diff JSON gratuit. Calcule un delta structurel entre deux documents JSON — clés ajoutées/supprimées, valeurs modifiées. 100% dans le navigateur."},
        "it": {"name": "Diff JSON", "tagline": "Diff strutturale tra due documenti JSON — chiavi aggiunte, rimosse, modificate e cambi di valore affiancati.", "description": "Diff JSON gratuito. Calcola un delta strutturale tra due documenti JSON — chiavi aggiunte/rimosse, valori modificati. 100% nel browser."},
        "pt": {"name": "Diff JSON", "tagline": "Diff estrutural de dois documentos JSON — chaves adicionadas, removidas, alteradas e mudanças de valor lado a lado.", "description": "Diff JSON grátis online. Calcula um delta estrutural entre dois documentos JSON — chaves adicionadas/removidas, valores alterados, e uma visão lado a lado limpa. Roda totalmente no seu browser."},
        "pl": {"name": "Diff JSON", "tagline": "Strukturalny diff dwóch dokumentów JSON — dodane, usunięte, zmienione klucze i zmiany wartości obok siebie.", "description": "Darmowy online diff JSON. Liczy strukturalną deltę między dwoma dokumentami JSON — dodane/usunięte klucze, zmienione wartości i czysty widok side-by-side. Działa w całości w przeglądarce."},
        "ja": {"name": "JSON 差分", "tagline": "2 つの JSON ドキュメントの構造的差分 — 追加・削除・変更されたキーと値の変化を並べて表示。", "description": "オンライン無料の JSON 差分ツール。2 つの JSON ドキュメントの構造的なデルタ（追加／削除されたキー、値の変化）を計算し、見やすい並列表示を提供します。すべてブラウザ内で動作します。"},
        "nl": {"name": "JSON Diff", "tagline": "Structurele diff voor twee JSON-documenten — keys toegevoegd, verwijderd, gewijzigd en waarde-wijzigingen naast elkaar getoond.", "description": "Gratis online JSON-diff. Berekent een structurele delta tussen twee JSON-documenten — toegevoegde/verwijderde keys, gewijzigde waarden en een schone side-by-side view. Draait volledig in je browser."},
        "tr": {"name": "JSON Diff", "tagline": "İki JSON belgesi için yapısal diff — eklenen, silinen, değişen anahtarlar ve değer değişiklikleri yan yana gösterilir.", "description": "Ücretsiz online JSON diff. İki JSON belgesi arasında yapısal delta hesaplar — eklenen/silinen anahtarlar, değişen değerler ve temiz yan yana görünüm. Tamamen tarayıcında çalışır."},
        "id": {"name": "JSON Diff", "tagline": "Diff struktural dua dokumen JSON — kunci yang ditambah, dihapus, diubah, dan perubahan nilai ditampilkan berdampingan.", "description": "Tool JSON diff gratis. Bandingkan dua dokumen JSON secara struktural dan lihat kunci yang ditambah, dihapus, diubah, dan perubahan nilai berdampingan. Tidak peduli urutan kunci, fokus pada struktur."},
        "vi": {"name": "JSON Diff", "tagline": "Diff theo cấu trúc của hai tài liệu JSON — key được thêm, bị xóa, được thay đổi và thay đổi giá trị hiển thị cạnh nhau.", "description": "JSON diff miễn phí trực tuyến. So sánh hai tài liệu JSON theo cấu trúc, hiển thị key được thêm, bị xóa, được thay đổi và thay đổi giá trị một cách trực quan. Chạy hoàn toàn trong trình duyệt."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Left (A)</label>
      <textarea id="jd-a" oninput="jdRun()" spellcheck="false" placeholder='{"name":"alice","age":30}'></textarea>
    </div>
    <div>
      <label>Right (B)</label>
      <textarea id="jd-b" oninput="jdRun()" spellcheck="false" placeholder='{"name":"alice","age":31,"email":"a@x.com"}'></textarea>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Mode</label>
      <select id="jd-mode" onchange="jdRun()">
        <option value="changes">Changes only</option>
        <option value="full">Full side-by-side</option>
        <option value="patch">JSON Patch (RFC 6902)</option>
      </select>
    </div>
    <div>
      <label>Array compare</label>
      <select id="jd-arr" onchange="jdRun()">
        <option value="index">By index</option>
        <option value="value">By value (set-like)</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="jd-summary" class="meta" style="margin-bottom:0.5rem"></div>
  <div id="jd-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.jd-list{display:grid;gap:0.4rem;font-family:ui-monospace,monospace;font-size:0.85rem}
.jd-row{padding:0.45rem 0.65rem;border-radius:6px;border:1px solid var(--border);background:var(--bg-elev);display:grid;grid-template-columns:auto 1fr;gap:0.6rem;align-items:start}
.jd-tag{font-size:0.7rem;font-weight:700;padding:0.1rem 0.45rem;border-radius:4px;letter-spacing:0.04em}
.jd-add{background:rgba(63,185,80,0.15);color:#3fb950;border:1px solid rgba(63,185,80,0.4)}
.jd-rem{background:rgba(248,81,73,0.15);color:#f85149;border:1px solid rgba(248,81,73,0.4)}
.jd-chg{background:rgba(88,166,255,0.15);color:#58a6ff;border:1px solid rgba(88,166,255,0.4)}
.jd-path{color:var(--text-muted);font-size:0.78rem;margin-bottom:0.2rem}
.jd-val{word-break:break-word;overflow-wrap:anywhere}
.jd-old{color:#f85149;text-decoration:line-through;opacity:0.85}
.jd-new{color:#3fb950}
.jd-arrow{color:var(--text-muted);margin:0 0.4rem}
.jd-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0}
.jd-summary-row{display:inline-flex;gap:0.7rem;font-family:ui-monospace,monospace;font-size:0.8rem}
</style>
<script>
function jdParse(s, label){
  s = s.trim();
  if(!s) return {ok:false, empty:true};
  try { return {ok:true, val: JSON.parse(s)}; }
  catch(e){ return {ok:false, err: label+': '+e.message}; }
}
function jdType(v){
  if(v === null) return 'null';
  if(Array.isArray(v)) return 'array';
  return typeof v;
}
function jdEqual(a,b){
  const ta = jdType(a), tb = jdType(b);
  if(ta !== tb) return false;
  if(ta === 'object'){
    const ka = Object.keys(a), kb = Object.keys(b);
    if(ka.length !== kb.length) return false;
    for(const k of ka){ if(!(k in b) || !jdEqual(a[k], b[k])) return false; }
    return true;
  }
  if(ta === 'array'){
    if(a.length !== b.length) return false;
    for(let i=0;i<a.length;i++) if(!jdEqual(a[i], b[i])) return false;
    return true;
  }
  return a === b || (Number.isNaN(a) && Number.isNaN(b));
}
function jdEsc(p){ return String(p).replace(/~/g,'~0').replace(/\\//g,'~1'); }
function jdDiff(a, b, path, mode, ops){
  const ta = jdType(a), tb = jdType(b);
  if(ta !== tb || (ta !== 'object' && ta !== 'array')){
    if(!jdEqual(a,b)) ops.push({op:'replace', path, from: a, value: b, type:'chg'});
    return;
  }
  if(ta === 'object'){
    const keys = new Set([...Object.keys(a), ...Object.keys(b)]);
    for(const k of [...keys].sort()){
      const sub = path + '/' + jdEsc(k);
      if(!(k in a)) ops.push({op:'add', path: sub, value: b[k], type:'add'});
      else if(!(k in b)) ops.push({op:'remove', path: sub, from: a[k], type:'rem'});
      else jdDiff(a[k], b[k], sub, mode, ops);
    }
    return;
  }
  // array
  if(mode === 'value'){
    // set-like: items only in B added, items only in A removed; ignore order
    const aJson = a.map(x => JSON.stringify(x));
    const bJson = b.map(x => JSON.stringify(x));
    const aSet = new Set(aJson), bSet = new Set(bJson);
    bJson.forEach((j,i) => { if(!aSet.has(j)) ops.push({op:'add', path: path+'/'+i, value: b[i], type:'add'}); });
    aJson.forEach((j,i) => { if(!bSet.has(j)) ops.push({op:'remove', path: path+'/'+i, from: a[i], type:'rem'}); });
    return;
  }
  // by index
  const max = Math.max(a.length, b.length);
  for(let i=0;i<max;i++){
    const sub = path + '/' + i;
    if(i >= a.length) ops.push({op:'add', path: sub, value: b[i], type:'add'});
    else if(i >= b.length) ops.push({op:'remove', path: sub, from: a[i], type:'rem'});
    else jdDiff(a[i], b[i], sub, mode, ops);
  }
}
function jdFmt(v){ return JSON.stringify(v); }
function jdRender(ops, mode){
  const out = document.getElementById('jd-out');
  if(mode === 'patch'){
    const patch = ops.map(o => o.op === 'replace' ? {op:'replace', path:o.path, value:o.value} : o.op === 'add' ? {op:'add', path:o.path, value:o.value} : {op:'remove', path:o.path});
    out.innerHTML = '<pre class="output" style="margin:0">' + JSON.stringify(patch, null, 2) + '</pre>';
    return;
  }
  if(ops.length === 0){
    out.innerHTML = '<div class="jd-empty">✓ No structural differences</div>';
    return;
  }
  const html = ops.map(o => {
    const tag = o.type === 'add' ? '<span class="jd-tag jd-add">+ ADD</span>' :
                o.type === 'rem' ? '<span class="jd-tag jd-rem">− REM</span>' :
                                   '<span class="jd-tag jd-chg">~ CHG</span>';
    let body;
    if(o.type === 'chg') body = `<span class="jd-old">${jdFmt(o.from)}</span><span class="jd-arrow">→</span><span class="jd-new">${jdFmt(o.value)}</span>`;
    else if(o.type === 'add') body = `<span class="jd-new">${jdFmt(o.value)}</span>`;
    else body = `<span class="jd-old">${jdFmt(o.from)}</span>`;
    return `<div class="jd-row">${tag}<div><div class="jd-path">${o.path || '/'}</div><div class="jd-val">${body}</div></div></div>`;
  }).join('');
  out.innerHTML = '<div class="jd-list">' + html + '</div>';
}
function jdRun(){
  const a = jdParse(document.getElementById('jd-a').value, 'Left');
  const b = jdParse(document.getElementById('jd-b').value, 'Right');
  const out = document.getElementById('jd-out');
  const sum = document.getElementById('jd-summary');
  out.classList.remove('error');
  if(a.empty || b.empty){ out.textContent='{LBL_NO_INPUT}'; sum.textContent=''; return; }
  if(!a.ok){ out.classList.add('error'); out.textContent = '✗ ' + a.err; sum.textContent=''; return; }
  if(!b.ok){ out.classList.add('error'); out.textContent = '✗ ' + b.err; sum.textContent=''; return; }
  const mode = document.getElementById('jd-mode').value;
  const arrMode = document.getElementById('jd-arr').value;
  const ops = [];
  jdDiff(a.val, b.val, '', arrMode, ops);
  const adds = ops.filter(o => o.type === 'add').length;
  const rems = ops.filter(o => o.type === 'rem').length;
  const chgs = ops.filter(o => o.type === 'chg').length;
  sum.innerHTML = `<span class="jd-summary-row"><span style="color:#3fb950">+${adds} added</span> <span style="color:#f85149">−${rems} removed</span> <span style="color:#58a6ff">~${chgs} changed</span></span>`;
  jdRender(ops, mode);
}
document.addEventListener('DOMContentLoaded', jdRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A plain-text diff on JSON tells you which lines changed; a structural diff tells you which <em>data points</em> changed. They're often very different — a re-formatted document with no semantic change is "every line different" to a text diff but "no changes" here. This tool walks both JSON trees and reports each path where they differ, using <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a> syntax (<code>/users/0/name</code>) so the output is unambiguous regardless of formatting.</p>

<h3>When to use it</h3>
<ul>
  <li>Comparing two API responses to see what actually changed in a release, ignoring whitespace/key-order noise.</li>
  <li>Diffing config files before/after a migration to confirm only the intended fields moved.</li>
  <li>Generating an RFC 6902 JSON Patch document to ship to a system that supports it (PATCH endpoints, JSON-Merge-Patch fallbacks).</li>
  <li>Eyeballing two test fixtures to see what makes one fail when the other passes.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Array compare mode matters.</strong> "By index" reports an inserted element as remove+add for everything after it. "By value" treats arrays as sets, missing genuine reorderings. Pick the one that matches how your data is meant to be ordered.</li>
  <li><strong>Number-vs-string isn't structural.</strong> <code>{"id": 1}</code> and <code>{"id": "1"}</code> show as a change because the types differ. Normalise types before diffing if that matters.</li>
  <li><strong>RFC 6902 is a one-way patch, not a merge.</strong> Apply it with a real RFC 6902 implementation, not by string-replacement.</li>
  <li><strong>Big trees get noisy.</strong> If the diff is hundreds of operations long, you're probably comparing two unrelated documents — re-check the inputs.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um diff de texto puro em JSON te diz quais linhas mudaram; um diff estrutural te diz quais <em>pontos de dado</em> mudaram. Os dois costumam ser bem diferentes — um documento reformatado sem mudança semântica é "toda linha diferente" pra um text diff, mas "nenhuma mudança" aqui. Esta ferramenta percorre as duas árvores JSON e reporta cada path onde elas divergem, usando a sintaxe <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">JSON Pointer da RFC 6901</a> (<code>/users/0/name</code>) pra que o output seja inequívoco independentemente da formatação.</p>

<h3>Quando usar</h3>
<ul>
  <li>Comparar duas respostas de API pra ver o que de fato mudou numa release, ignorando barulho de whitespace e ordem de chave.</li>
  <li>Fazer diff de arquivos de config antes/depois de uma migração pra confirmar que só os campos pretendidos mudaram.</li>
  <li>Gerar um documento JSON Patch da RFC 6902 pra enviar a um sistema que aceita (endpoints PATCH, fallbacks de JSON-Merge-Patch).</li>
  <li>Olhar duas test fixtures pra ver o que faz uma falhar quando a outra passa.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>O modo de comparação de array importa.</strong> "By index" reporta um elemento inserido como remove+add em tudo depois dele. "By value" trata arrays como conjuntos, perdendo reordenações reais. Escolha o que casa com a forma como seus dados deveriam estar ordenados.</li>
  <li><strong>Number-vs-string não é estrutural.</strong> <code>{"id": 1}</code> e <code>{"id": "1"}</code> aparecem como mudança porque os tipos diferem. Normalize tipos antes do diff se isso importa.</li>
  <li><strong>RFC 6902 é um patch unidirecional, não um merge.</strong> Aplique com uma implementação real de RFC 6902, não por substituição de string.</li>
  <li><strong>Árvores grandes ficam barulhentas.</strong> Se o diff tem centenas de operações, provavelmente você está comparando dois documentos sem relação — confira os inputs.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Diff tekstowy na JSON-ie mówi ci, które linie się zmieniły; diff strukturalny mówi, które <em>punkty danych</em> się zmieniły. To często bardzo różne rzeczy — przeformatowany dokument bez zmiany semantycznej dla diffa tekstowego to "każda linia inna", a tu "brak zmian". To narzędzie chodzi po obu drzewach JSON i raportuje każdy path, gdzie się różnią, używając składni <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a> (<code>/users/0/name</code>), żeby wyjście było jednoznaczne niezależnie od formatowania.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Porównanie dwóch odpowiedzi API, żeby zobaczyć, co faktycznie się zmieniło w releasie, ignorując szum białych znaków i kolejności kluczy.</li>
  <li>Diff plików configa przed/po migracji, żeby potwierdzić, że ruszyły tylko zamierzone pola.</li>
  <li>Generowanie dokumentu JSON Patch wg RFC 6902 do wysłania do systemu, który to wspiera (endpointy PATCH, fallbacki JSON-Merge-Patch).</li>
  <li>Patrzenie na dwie fixture testowe, żeby zobaczyć, co sprawia, że jedna pada, a druga przechodzi.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Tryb porównywania tablic ma znaczenie.</strong> "By index" raportuje wstawiony element jako remove+add dla wszystkiego za nim. "By value" traktuje tablice jako zbiory, gubiąc faktyczne zmiany kolejności. Wybierz ten, który pasuje do tego, jak twoje dane mają być uporządkowane.</li>
  <li><strong>Number-vs-string nie jest strukturalne.</strong> <code>{"id": 1}</code> i <code>{"id": "1"}</code> pokazują się jako zmiana, bo typy się różnią. Znormalizuj typy przed diffem, jeśli to ważne.</li>
  <li><strong>RFC 6902 to jednokierunkowy patch, nie merge.</strong> Aplikuj go prawdziwą implementacją RFC 6902, nie podstawianiem stringów.</li>
  <li><strong>Duże drzewa robią szum.</strong> Jeśli diff ma setki operacji, prawdopodobnie porównujesz dwa niepowiązane dokumenty — sprawdź wejście jeszcze raz.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>JSON に対してプレーンテキスト diff をかけると「どの行が変わったか」しか分かりません。構造的 diff は「どの<em>データポイント</em>が変わったか」を教えてくれます。同じ意味で再フォーマットしただけのドキュメントは、テキスト diff では「全行が違う」になりますが、構造的には「変更なし」です。本ツールは両方の JSON ツリーを巡回し、差分のあるパスを <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a>（<code>/users/0/name</code>）で報告するため、フォーマットに左右されない明確な出力になります。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>2 つの API レスポンスを比較し、空白やキー順序のノイズを無視して、リリースで実際に何が変わったか確認したいとき。</li>
  <li>マイグレーション前後の設定ファイルを比較し、意図したフィールドだけ動いたか確認したいとき。</li>
  <li>RFC 6902 の JSON Patch を生成し、それを受け付けるシステム（PATCH エンドポイント、JSON-Merge-Patch のフォールバック）に送りたいとき。</li>
  <li>2 つのテストフィクスチャを見比べ、片方だけ落ちる原因を推測したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>配列比較モードは大事です。</strong> 「by index」は要素を 1 つ挿入すると以後の全要素が remove+add になります。「by value」は集合扱いなので、本物の並び替えを見落とします。データの想定順序に合うほうを選んでください。</li>
  <li><strong>数値と文字列は構造的には別物です。</strong> <code>{"id": 1}</code> と <code>{"id": "1"}</code> は型が違うため変更として表示されます。気になる場合は事前に型を正規化してください。</li>
  <li><strong>RFC 6902 は一方向のパッチであり、マージではありません。</strong> 本物の RFC 6902 実装で適用してください。文字列置換で適用してはいけません。</li>
  <li><strong>巨大なツリーはノイジーになります。</strong> 数百件もの差分が出るなら、関係のない 2 つのドキュメントを比べている可能性が高いので、入力を確認してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een plain-text diff op JSON vertelt je welke regels veranderden; een structurele diff vertelt je welke <em>data points</em> veranderden. Vaak heel verschillend — een geherformatteerd document zonder semantische verandering is "elke regel anders" voor een tekst-diff maar "geen veranderingen" hier. Deze tool loopt beide JSON-bomen door en rapporteert elk pad waar ze verschillen, met <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a>-syntax (<code>/users/0/name</code>) zodat de output ondubbelzinnig is ongeacht formatting.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Twee API-responses vergelijken om te zien wat er daadwerkelijk in een release veranderde, ongeacht whitespace/key-order-ruis.</li>
  <li>Config files diffen voor/na een migratie om te bevestigen dat alleen de bedoelde velden zijn veranderd.</li>
  <li>Een RFC 6902 JSON Patch-document genereren om naar een systeem te sturen dat het ondersteunt (PATCH endpoints, JSON-Merge-Patch fallbacks).</li>
  <li>Twee test fixtures bekijken om te zien waarom de ene faalt waar de andere passeert.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Array compare mode doet ertoe.</strong> "By index" rapporteert een ingevoegd element als remove+add voor alles erna. "By value" behandelt arrays als sets, mist echte reorderings. Kies degene die past bij hoe je data bedoeld is.</li>
  <li><strong>Number-vs-string is niet structureel.</strong> <code>{"id": 1}</code> en <code>{"id": "1"}</code> tonen als een wijziging omdat de types verschillen. Normaliseer types voor diff-en als dat ertoe doet.</li>
  <li><strong>RFC 6902 is een one-way patch, geen merge.</strong> Pas het toe met een echte RFC 6902-implementatie, niet door string-replacement.</li>
  <li><strong>Grote bomen worden ruizig.</strong> Als de diff honderden operations lang is, vergelijk je waarschijnlijk twee ongerelateerde documenten — check de inputs.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>JSON üzerinde düz metin diff hangi satırların değiştiğini söyler; yapısal diff hangi <em>veri noktalarının</em> değiştiğini söyler. Sıklıkla çok farklılaşır — anlam değişikliği olmayan yeniden biçimlendirilmiş bir belge metin diff için "her satır farklı"dır ama burada "değişiklik yok"tur. Bu araç her iki JSON ağacında yürür ve farklı oldukları her yolu raporlar, biçimlendirme ne olursa olsun çıktının belirsiz olmaması için <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a> sözdizimini (<code>/users/0/name</code>) kullanır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>İki API yanıtını karşılaştırarak bir sürümde gerçekten ne değiştiğini görme, boşluk/anahtar-sırası gürültüsünü yok sayma.</li>
  <li>Bir geçişten önce/sonra config dosyalarını diff'leyerek yalnızca amaçlanan alanların taşındığını doğrulama.</li>
  <li>Destekleyen bir sisteme gönderilecek bir RFC 6902 JSON Patch belgesi üretme (PATCH endpoint'leri, JSON-Merge-Patch fallback'leri).</li>
  <li>Birinin başarısız olmasını diğerinin başarılı olmasını sağlayan şeyin ne olduğunu görmek için iki test fixture'ına bakma.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Array karşılaştırma modu önemlidir.</strong> "İndeks ile" eklenen bir elementi sonrasındaki her şey için remove+add olarak raporlar. "Değer ile" array'leri set olarak ele alır, gerçek yeniden sıralamaları kaçırır. Verinin nasıl sıralanması gerektiğine uyan birini seç.</li>
  <li><strong>Sayı-vs-string yapısal değildir.</strong> <code>{"id": 1}</code> ve <code>{"id": "1"}</code> türler farklı olduğu için değişiklik olarak gösterilir. Önemliyse, diff'lemeden önce türleri normalize et.</li>
  <li><strong>RFC 6902 tek yönlü bir patch'tir, merge değil.</strong> String-değiştirme ile değil, gerçek bir RFC 6902 uygulamasıyla uygula.</li>
  <li><strong>Büyük ağaçlar gürültülü olur.</strong> Diff yüzlerce işlem uzunsa, muhtemelen iki ilgisiz belgeyi karşılaştırıyorsun — girdileri yeniden kontrol et.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Plain-text diff pada JSON memberitahu kamu baris mana yang berubah; structural diff memberitahu <em>data point</em> mana yang berubah. Sering kali keduanya sangat berbeda — dokumen yang diformat ulang tanpa perubahan semantik akan tampak "setiap baris berbeda" bagi text diff tapi "tidak ada perubahan" di sini. Tool ini menelusuri kedua tree JSON dan melaporkan setiap path tempat keduanya berbeda, menggunakan sintaks <a href="https://datatracker.ietf.org/doc/html/rfc6901" target="_blank" rel="noopener noreferrer">RFC 6901 JSON Pointer</a> (<code>/users/0/name</code>) supaya output-nya tidak ambigu apa pun formattingnya.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Membandingkan dua response API untuk melihat apa yang sebenarnya berubah di sebuah release, mengabaikan noise whitespace/urutan key.</li>
  <li>Mendiff file config sebelum/sesudah migrasi untuk memastikan hanya field yang dimaksud yang bergerak.</li>
  <li>Menghasilkan dokumen RFC 6902 JSON Patch untuk dikirim ke sistem yang mendukungnya (endpoint PATCH, fallback JSON-Merge-Patch).</li>
  <li>Melihat dua test fixture untuk memahami apa yang membuat satu fail sementara yang lain pass.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Mode pembandingan array itu penting.</strong> "By index" melaporkan satu element yang disisipkan sebagai remove+add untuk semua element setelahnya. "By value" memperlakukan array sebagai set, kehilangan reorder yang sesungguhnya. Pilih yang sesuai dengan bagaimana data kamu seharusnya tersusun.</li>
  <li><strong>Number-vs-string bukan struktural.</strong> <code>{"id": 1}</code> dan <code>{"id": "1"}</code> muncul sebagai perubahan karena type-nya beda. Normalisasi type sebelum diff jika itu penting.</li>
  <li><strong>RFC 6902 adalah patch satu arah, bukan merge.</strong> Apply dengan implementasi RFC 6902 asli, bukan dengan string-replacement.</li>
  <li><strong>Tree besar jadi noisy.</strong> Kalau diff-nya ratusan operasi, kemungkinan kamu membandingkan dua dokumen yang tidak berkaitan — periksa lagi input-nya.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>So sánh hai tài liệu JSON dòng-by-dòng dưới dạng văn bản hiếm khi cho bạn câu trả lời bạn muốn — thứ tự key có thể khác, indent có thể khác, và một thay đổi nhỏ ở giá trị có thể trông như nhiều khác biệt. Diff theo cấu trúc cho bạn cảm giác về thay đổi ngữ nghĩa: key nào được thêm, bị xóa hoặc được cập nhật, và từ giá trị nào sang giá trị nào.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Review thay đổi config trong code review — JSON config trước vs sau.</li>
  <li>Debug response API khác nhau giữa staging và production.</li>
  <li>Audit thay đổi schema giữa các phiên bản API.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Thứ tự mảng quan trọng.</strong> JSON treat mảng là sắp xếp; <code>[1, 2]</code> ≠ <code>[2, 1]</code>. Tool này đánh dấu reorder dưới dạng thay đổi.</li>
  <li><strong>Thứ tự key không quan trọng (đối với JSON đúng).</strong> Tool diff bỏ qua thứ tự key trên object — chỉ key tồn tại và giá trị mới quan trọng.</li>
  <li><strong>Kiểu quan trọng.</strong> <code>"123"</code> (string) khác <code>123</code> (number) và sẽ hiển thị dưới dạng thay đổi.</li>
</ul>
""",
    },
    "related": ["json-formatter", "text-diff", "yaml-json"],
    "howto": {"flow": "compare",   "action": "compare", "noun": "JSON"},
}
