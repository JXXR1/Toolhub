TOOL = {
    "slug": "json-path",
    "category": "developer",
    "icon": "/{}",
    "tags": ["json", "jsonpath", "query", "filter", "extract", "data"],
    "i18n": {
        "en": {
            "name": "JSONPath Tester",
            "tagline": "Run JSONPath queries against any JSON document. See matched nodes and their paths in real time.",
            "description": "Free online JSONPath tester. Query nested JSON with $.., wildcards, array slices, and filter expressions. Live results, paste your JSON and start querying.",
        },
        "de": {"name": "JSONPath-Tester", "tagline": "Führe JSONPath-Abfragen gegen JSON-Dokumente aus. Sieh Treffer und Pfade in Echtzeit.", "description": "Kostenloser JSONPath-Tester. Frage verschachteltes JSON mit $.., Wildcards, Array-Slices und Filtern ab. Live-Ergebnisse."},
        "es": {"name": "Tester JSONPath", "tagline": "Ejecuta consultas JSONPath contra cualquier documento JSON. Coincidencias y rutas en tiempo real.", "description": "Tester gratuito de JSONPath. Consulta JSON anidado con $.., comodines, cortes de array y filtros. Resultados en vivo."},
        "fr": {"name": "Testeur JSONPath", "tagline": "Exécutez des requêtes JSONPath sur tout document JSON. Résultats et chemins en temps réel.", "description": "Testeur JSONPath gratuit. Interrogez du JSON imbriqué avec $.., wildcards, slices, filtres. Résultats en direct."},
        "it": {"name": "Tester JSONPath", "tagline": "Esegui query JSONPath su qualsiasi documento JSON. Match e percorsi in tempo reale.", "description": "Tester JSONPath gratuito. Interroga JSON annidato con $.., wildcard, slice, filtri. Risultati live."},
    },
    "body": """
<div class="tool-card">
  <label>JSON document</label>
  <textarea id="jp-doc" oninput="jpRun()" spellcheck="false" style="font-family:ui-monospace,monospace;min-height:220px">{
  "store": {
    "books": [
      {"title": "Moby Dick",        "author": "Melville",   "price": 12.99, "tags": ["classic", "sea"]},
      {"title": "Dune",             "author": "Herbert",    "price": 14.50, "tags": ["sci-fi"]},
      {"title": "The Pragmatic Programmer", "author": "Hunt", "price": 24.00, "tags": ["tech"]}
    ],
    "bicycle": {"color": "red", "price": 320}
  }
}</textarea>
</div>
<div class="tool-card">
  <label>JSONPath query</label>
  <input type="text" id="jp-query" oninput="jpRun()" value="$.store.books[*].title" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
  <div class="meta" style="margin-top:0.4rem">Try:
    <code>$..price</code>,
    <code>$.store.books[?(@.price &lt; 20)].title</code>,
    <code>$.store.books[*].tags[0]</code>,
    <code>$..*</code>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div class="output-row">
    <pre class="output" id="jp-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('jp-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="jp-meta" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<script>
// Compact JSONPath implementation supporting:
//   $              root
//   .name / [name] property access
//   ..             recursive descent
//   *              wildcard
//   [n]            index, [n,m,...] union, [start:end:step] slice
//   [?(expr)]      filter — supports @.prop, @['prop'], comparisons, &&, ||, regex via =~
function jpTokenize(q){
  // Convert to a list of tokens. Quick and dirty but handles the common cases.
  if(!q.startsWith('$')) throw new Error('JSONPath must start with $');
  const tokens = [];
  let i = 1;
  while(i < q.length){
    const c = q[i];
    if(c === '.'){
      if(q[i+1] === '.'){
        tokens.push({type:'descend'});
        i += 2;
      } else {
        i++;
      }
      // After . may come name or *
      if(i < q.length && q[i] !== '[' && q[i] !== '.'){
        let m = q.slice(i).match(/^([A-Za-z_$][\\w$-]*|\\*)/);
        if(!m) throw new Error('Unexpected after . at ' + i);
        tokens.push({type:'name', name: m[1]});
        i += m[1].length;
      }
    } else if(c === '['){
      const close = q.indexOf(']', i);
      if(close === -1) throw new Error('Unclosed [');
      const inner = q.slice(i+1, close).trim();
      if(inner.startsWith('?(') && inner.endsWith(')')){
        tokens.push({type:'filter', expr: inner.slice(2,-1)});
      } else if(inner === '*'){
        tokens.push({type:'name', name:'*'});
      } else if(/^['"]/.test(inner)){
        tokens.push({type:'name', name: inner.slice(1,-1)});
      } else if(inner.includes(':')){
        const [s,e,st] = inner.split(':');
        tokens.push({type:'slice', start: s===''?null:+s, end: e===''?null:+e, step: st===undefined||st===''?1:+st});
      } else if(inner.includes(',')){
        tokens.push({type:'union', items: inner.split(',').map(x=>x.trim()).map(x => /^-?\\d+$/.test(x)?+x:x.replace(/^['"]|['"]$/g,''))});
      } else if(/^-?\\d+$/.test(inner)){
        tokens.push({type:'index', i: +inner});
      } else {
        tokens.push({type:'name', name: inner});
      }
      i = close + 1;
    } else {
      i++;
    }
  }
  return tokens;
}
function jpEvalFilter(expr, ctx){
  // Replace @ with ctx, then eval. Convert =~ /re/ to RegExp.test.
  // Convert @.prop or @['prop'] to ctx.prop / ctx['prop'].
  let js = expr.replace(/@/g, '__ctx');
  // simple regex match: var =~ /re/flags  →  /re/flags.test(var)
  js = js.replace(/(\\S+?)\\s*=~\\s*\\/(.*?)\\/([gimsy]*)/g, (_,v,re,fl) => `(new RegExp(${JSON.stringify(re)}, ${JSON.stringify(fl)})).test(${v})`);
  try {
    const fn = new Function('__ctx', `try { return !!(${js}); } catch(e) { return false; }`);
    return fn(ctx);
  } catch(e){ return false; }
}
function jpApply(tokens, doc){
  let cur = [{path:'$', node: doc}];
  for(const t of tokens){
    const next = [];
    for(const {path, node} of cur){
      if(t.type === 'descend'){
        // Recursive: include all descendants
        const visit = (n, p) => {
          next.push({path:p, node:n});
          if(Array.isArray(n)) n.forEach((v,i) => visit(v, p+'['+i+']'));
          else if(n && typeof n === 'object') Object.entries(n).forEach(([k,v]) => visit(v, p+'.'+k));
        };
        visit(node, path);
      } else if(t.type === 'name'){
        if(t.name === '*'){
          if(Array.isArray(node)) node.forEach((v,i) => next.push({path:path+'['+i+']', node:v}));
          else if(node && typeof node === 'object') Object.entries(node).forEach(([k,v]) => next.push({path:path+'.'+k, node:v}));
        } else if(node && typeof node === 'object' && t.name in node){
          next.push({path: path + '.' + t.name, node: node[t.name]});
        }
      } else if(t.type === 'index'){
        if(Array.isArray(node)){
          const i = t.i < 0 ? node.length + t.i : t.i;
          if(i >= 0 && i < node.length) next.push({path:path+'['+i+']', node:node[i]});
        }
      } else if(t.type === 'slice'){
        if(Array.isArray(node)){
          let {start, end, step} = t;
          if(start === null) start = step > 0 ? 0 : node.length-1;
          if(end === null)   end   = step > 0 ? node.length : -node.length-1;
          if(start < 0) start += node.length;
          if(end < 0) end += node.length;
          if(step > 0){
            for(let i = start; i < end; i += step) if(i>=0&&i<node.length) next.push({path:path+'['+i+']', node:node[i]});
          } else {
            for(let i = start; i > end; i += step) if(i>=0&&i<node.length) next.push({path:path+'['+i+']', node:node[i]});
          }
        }
      } else if(t.type === 'union'){
        for(const k of t.items){
          if(typeof k === 'number'){
            if(Array.isArray(node)){
              const i = k < 0 ? node.length + k : k;
              if(i >= 0 && i < node.length) next.push({path:path+'['+i+']', node:node[i]});
            }
          } else if(node && typeof node === 'object' && k in node){
            next.push({path:path+'.'+k, node:node[k]});
          }
        }
      } else if(t.type === 'filter'){
        const items = Array.isArray(node) ? node.map((v,i) => ({path: path+'['+i+']', node: v}))
                    : (node && typeof node === 'object' ? Object.entries(node).map(([k,v]) => ({path: path+'.'+k, node: v})) : []);
        for(const it of items){
          if(jpEvalFilter(t.expr, it.node)) next.push(it);
        }
      }
    }
    cur = next;
  }
  return cur;
}
function jpRun(){
  const docStr = document.getElementById('jp-doc').value;
  const q = document.getElementById('jp-query').value;
  const out = document.getElementById('jp-out');
  const meta = document.getElementById('jp-meta');
  out.classList.remove('error');
  let doc;
  try { doc = JSON.parse(docStr); }
  catch(e){ out.classList.add('error'); out.textContent = '✗ Invalid JSON: ' + e.message; meta.textContent=''; return; }
  let tokens;
  try { tokens = jpTokenize(q); }
  catch(e){ out.classList.add('error'); out.textContent = '✗ Bad query: ' + e.message; meta.textContent=''; return; }
  let results;
  try { results = jpApply(tokens, doc); }
  catch(e){ out.classList.add('error'); out.textContent = '✗ Query error: ' + e.message; meta.textContent=''; return; }
  if(results.length === 0){
    out.textContent = '(no matches)';
    meta.textContent = '0 matches';
    return;
  }
  const values = results.map(r => r.node);
  out.textContent = JSON.stringify(values, null, 2);
  const paths = results.slice(0, 10).map(r => '  ' + r.path).join('\\n');
  meta.innerHTML = `${results.length} match${results.length===1?'':'es'}<br><pre style="margin:0.4rem 0 0;font-size:0.82rem;color:var(--text-muted)">${paths}${results.length>10?'\\n  …':''}</pre>`;
}
document.addEventListener('DOMContentLoaded', jpRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>JSONPath is to JSON what XPath is to XML — a query language for plucking specific values out of a nested document without writing custom code. <code>$.store.books[*].title</code> says "give me every book title under store"; <code>$..price</code> says "every <em>price</em> anywhere in the document". This tool runs a query live against any JSON you paste, showing both the matched values and the paths they came from, so you can iterate on the query until it returns exactly what you want.</p>

<h3>When to use it</h3>
<ul>
  <li>Drafting a query for a tool that uses JSONPath: jq-like CLI utilities, Postman tests, Stedi, n8n, or AWS CloudWatch / Step Functions.</li>
  <li>Pulling specific fields out of a large API response without writing a script.</li>
  <li>Filtering an array by a field value (e.g. "all orders where total &gt; 100").</li>
  <li>Sanity-checking that a deeply nested path actually resolves to a value before plumbing it into code.</li>
</ul>

<h3>Quick syntax reference</h3>
<ul>
  <li><strong><code>$</code></strong> — root of the document.</li>
  <li><strong><code>.name</code></strong> or <strong><code>['name']</code></strong> — child by name.</li>
  <li><strong><code>..</code></strong> — recursive descent (any depth).</li>
  <li><strong><code>*</code></strong> — wildcard (any property or array element).</li>
  <li><strong><code>[n]</code></strong> — array index (negative counts from the end).</li>
  <li><strong><code>[start:end:step]</code></strong> — array slice (Python-style).</li>
  <li><strong><code>[a, b, c]</code></strong> — union of indices or names.</li>
  <li><strong><code>[?(@.field &gt; 5)]</code></strong> — filter expression. <code>@</code> = current item; supports <code>== != &lt; &gt; &lt;= &gt;= &amp;&amp; ||</code> and <code>=~ /regex/</code>.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>JSONPath has no single official spec.</strong> The original Stefan Gössner draft has been the de-facto reference for years; RFC 9535 (Feb 2024) finally standardised it. Implementations differ slightly — what works in Postman may not work in Jaeger.</li>
  <li><strong>Dot vs bracket.</strong> <code>$.foo-bar</code> looks like "foo minus bar" to the parser; use <code>$['foo-bar']</code> for property names with hyphens, dots, or spaces.</li>
  <li><strong>Filter expressions are JavaScript-flavoured here</strong> — that's a deliberate convenience but doesn't match RFC 9535 strictly. Don't rely on this tool's filters working byte-identical in another implementation.</li>
  <li><strong><code>$..*</code></strong> returns every node in the tree (depth-first), which can be a lot. Useful for exploring an unfamiliar document.</li>
  <li><strong>Numeric strings.</strong> <code>{"1": "a"}</code> — accessing with <code>$['1']</code> works; <code>$.1</code> doesn't (numbers aren't valid as dot-property names).</li>
  <li><strong>Ordering.</strong> Object property order isn't guaranteed by JSON. If your filter depends on order, sort first.</li>
</ul>
""",
    },
    "related": ["json-formatter", "json-diff", "regex-tester"],
}
