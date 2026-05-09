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
        "pt": {"name": "Testador JSONPath", "tagline": "Roda queries JSONPath contra qualquer documento JSON. Veja os nós correspondentes e seus paths em tempo real.", "description": "Testador JSONPath grátis online. Consulta JSON aninhado com $.., wildcards, array slices e expressões de filtro. Resultados ao vivo, cole seu JSON e comece a consultar."},
        "pl": {"name": "Tester JSONPath", "tagline": "Uruchamiaj zapytania JSONPath na dowolnym dokumencie JSON. Zobacz dopasowane węzły i ich ścieżki w czasie rzeczywistym.", "description": "Darmowy online tester JSONPath. Odpytuj zagnieżdżony JSON za pomocą $.., wildcardów, slice'ów tablic i wyrażeń filtrujących. Wyniki na żywo, wklej swój JSON i zacznij szukać."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>JSONPath está pra JSON assim como XPath está pra XML — uma linguagem de query pra extrair valores específicos de um documento aninhado sem escrever código sob medida. <code>$.store.books[*].title</code> diz "me dá todo título de livro abaixo de store"; <code>$..price</code> diz "todo <em>price</em> em qualquer lugar do documento". Esta ferramenta roda uma query ao vivo contra qualquer JSON que você colar, mostrando tanto os valores correspondentes quanto os paths de onde vieram, pra que você itere a query até retornar exatamente o que quer.</p>

<h3>Quando usar</h3>
<ul>
  <li>Rascunhar uma query para uma ferramenta que usa JSONPath: utilitários CLI estilo jq, testes do Postman, Stedi, n8n ou AWS CloudWatch / Step Functions.</li>
  <li>Pescar campos específicos de uma resposta grande de API sem escrever script.</li>
  <li>Filtrar um array por um valor de campo (ex.: "todas as orders onde total &gt; 100").</li>
  <li>Verificar se um path muito aninhado de fato resolve pra um valor antes de plumbar isso no código.</li>
</ul>

<h3>Referência rápida de sintaxe</h3>
<ul>
  <li><strong><code>$</code></strong> — raiz do documento.</li>
  <li><strong><code>.name</code></strong> ou <strong><code>['name']</code></strong> — filho por nome.</li>
  <li><strong><code>..</code></strong> — descida recursiva (qualquer profundidade).</li>
  <li><strong><code>*</code></strong> — wildcard (qualquer propriedade ou elemento de array).</li>
  <li><strong><code>[n]</code></strong> — índice de array (negativo conta a partir do fim).</li>
  <li><strong><code>[start:end:step]</code></strong> — slice de array (estilo Python).</li>
  <li><strong><code>[a, b, c]</code></strong> — união de índices ou nomes.</li>
  <li><strong><code>[?(@.field &gt; 5)]</code></strong> — expressão de filtro. <code>@</code> = item atual; suporta <code>== != &lt; &gt; &lt;= &gt;= &amp;&amp; ||</code> e <code>=~ /regex/</code>.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>JSONPath não tem uma única spec oficial.</strong> O draft original do Stefan Gössner foi a referência de fato por anos; a RFC 9535 (fev/2024) finalmente padronizou. As implementações divergem um pouco — o que funciona no Postman pode não funcionar no Jaeger.</li>
  <li><strong>Ponto vs colchete.</strong> <code>$.foo-bar</code> parece "foo menos bar" pro parser; use <code>$['foo-bar']</code> para nomes de propriedade com hífen, ponto ou espaço.</li>
  <li><strong>As expressões de filtro aqui têm sabor JavaScript</strong> — é uma conveniência deliberada, mas não bate exatamente com a RFC 9535. Não confie que os filtros desta ferramenta vão funcionar byte a byte numa outra implementação.</li>
  <li><strong><code>$..*</code></strong> retorna todo nó da árvore (depth-first), o que pode ser muita coisa. Útil pra explorar um documento desconhecido.</li>
  <li><strong>Strings numéricas.</strong> <code>{"1": "a"}</code> — acessar com <code>$['1']</code> funciona; <code>$.1</code> não (números não são válidos como nomes de propriedade com ponto).</li>
  <li><strong>Ordenação.</strong> JSON não garante ordem de propriedades de objetos. Se seu filtro depende de ordem, ordene antes.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>JSONPath ma się do JSON-a tak, jak XPath do XML-a — to język zapytań do wyciągania konkretnych wartości z zagnieżdżonego dokumentu bez pisania custom kodu. <code>$.store.books[*].title</code> mówi "daj mi każdy tytuł książki ze store"; <code>$..price</code> mówi "każdy <em>price</em> w dowolnym miejscu dokumentu". To narzędzie uruchamia zapytanie na żywo na dowolnym wklejonym JSON-ie, pokazując zarówno dopasowane wartości, jak i ścieżki, z których pochodzą, żebyś mógł iterować zapytanie, aż zwróci dokładnie to, czego chcesz.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Pisanie zapytania do narzędzia, które używa JSONPath: CLI w stylu jq, testy w Postmanie, Stedi, n8n albo AWS CloudWatch / Step Functions.</li>
  <li>Wyciąganie konkretnych pól z dużej odpowiedzi API bez pisania skryptu.</li>
  <li>Filtrowanie tablicy po wartości pola (np. "wszystkie zamówienia, gdzie total &gt; 100").</li>
  <li>Sprawdzenie, czy głęboko zagnieżdżony path faktycznie rozwiązuje się do wartości, zanim wpiszesz to do kodu.</li>
</ul>

<h3>Szybka referencja składni</h3>
<ul>
  <li><strong><code>$</code></strong> — korzeń dokumentu.</li>
  <li><strong><code>.name</code></strong> albo <strong><code>['name']</code></strong> — dziecko po nazwie.</li>
  <li><strong><code>..</code></strong> — descent rekurencyjny (dowolna głębokość).</li>
  <li><strong><code>*</code></strong> — wildcard (dowolna właściwość albo element tablicy).</li>
  <li><strong><code>[n]</code></strong> — indeks tablicy (ujemny liczy od końca).</li>
  <li><strong><code>[start:end:step]</code></strong> — slice tablicy (w stylu Pythona).</li>
  <li><strong><code>[a, b, c]</code></strong> — unia indeksów albo nazw.</li>
  <li><strong><code>[?(@.field &gt; 5)]</code></strong> — wyrażenie filtrujące. <code>@</code> = bieżący element; obsługuje <code>== != &lt; &gt; &lt;= &gt;= &amp;&amp; ||</code> i <code>=~ /regex/</code>.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>JSONPath nie ma jednej oficjalnej speca.</strong> Pierwotny draft Stefana Gössnera był de facto referencją przez lata; RFC 9535 (luty 2024) wreszcie to wystandaryzowało. Implementacje delikatnie się różnią — to, co działa w Postmanie, może nie zadziałać w Jaegerze.</li>
  <li><strong>Kropka vs nawias.</strong> <code>$.foo-bar</code> wygląda dla parsera jak "foo minus bar"; używaj <code>$['foo-bar']</code> dla nazw właściwości z myślnikami, kropkami albo spacjami.</li>
  <li><strong>Wyrażenia filtrujące mają tu smak JavaScript</strong> — to świadoma wygoda, ale nie pasuje ściśle do RFC 9535. Nie polegaj na tym, że filtry tego narzędzia zadziałają bajt-w-bajt w innej implementacji.</li>
  <li><strong><code>$..*</code></strong> zwraca każdy węzeł w drzewie (depth-first), co może być sporo. Przydaje się do eksploracji nieznanego dokumentu.</li>
  <li><strong>Numeryczne stringi.</strong> <code>{"1": "a"}</code> — dostęp przez <code>$['1']</code> działa; <code>$.1</code> nie (liczby nie są poprawne jako nazwy properties po kropce).</li>
  <li><strong>Kolejność.</strong> JSON nie gwarantuje kolejności properties obiektów. Jeśli filtr zależy od kolejności, najpierw posortuj.</li>
</ul>
""",
    },
    "related": ["json-formatter", "json-diff", "regex-tester"],
}
