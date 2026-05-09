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
    },
    "related": ["json-formatter", "text-diff", "yaml-json"],
}
