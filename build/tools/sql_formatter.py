TOOL = {
    "slug": "sql-formatter",
    "category": "developer",
    "icon": "🗄",
    "tags": ["sql", "format", "beautify", "minify", "indent", "mysql", "postgres", "ansi"],
    "i18n": {
        "en": {
            "name": "SQL Formatter",
            "tagline": "Format and beautify SQL with proper indentation, or minify to a single line. Dialect-aware (ANSI / MySQL / Postgres).",
            "description": "Free online SQL formatter. Pretty-prints any SELECT/INSERT/UPDATE/DDL with consistent indentation, keyword casing, and clause alignment. Also minifies to a single line. Runs entirely in your browser.",
        },
        "de": {"name": "SQL-Formatierer", "tagline": "SQL formatieren und einrücken oder zu einer Zeile minimieren. Dialekt-bewusst (ANSI / MySQL / Postgres).", "description": "Kostenloser SQL-Formatierer. Druckt SELECT/INSERT/UPDATE/DDL mit konsistenter Einrückung, Keyword-Schreibweise und Klausel-Ausrichtung. Auch Minify auf eine Zeile. Komplett im Browser."},
        "es": {"name": "Formateador SQL", "tagline": "Formatea y embellece SQL con indentación, o minifícalo a una línea. Consciente del dialecto (ANSI / MySQL / Postgres).", "description": "Formateador SQL gratuito. Pretty-print de SELECT/INSERT/UPDATE/DDL con indentación consistente, mayúsculas de palabras clave y alineación de cláusulas. También minifica. 100% en el navegador."},
        "fr": {"name": "Formateur SQL", "tagline": "Formatez et embellissez du SQL avec indentation, ou minifiez sur une ligne. Conscient du dialecte (ANSI / MySQL / Postgres).", "description": "Formateur SQL gratuit. Pretty-print de SELECT/INSERT/UPDATE/DDL avec indentation cohérente, casse des mots-clés et alignement des clauses. Minify aussi. 100% dans le navigateur."},
        "it": {"name": "Formattatore SQL", "tagline": "Formatta e abbellisce SQL con indentazione corretta, o minifica su una riga. Consapevole del dialetto (ANSI / MySQL / Postgres).", "description": "Formattatore SQL gratuito. Pretty-print di SELECT/INSERT/UPDATE/DDL con indentazione coerente, maiuscole di parole chiave e allineamento clausole. Minifica anche. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="sf-in" oninput="sfRun()" spellcheck="false" placeholder="select * from users u join orders o on o.user_id=u.id where u.active=1 and o.total>100 order by o.total desc limit 10;" style="min-height:160px">select u.id, u.email, count(o.id) as order_count, sum(o.total) as total_spent from users u left join orders o on o.user_id = u.id where u.signup_date >= '2025-01-01' and u.active = true group by u.id, u.email having count(o.id) > 5 order by total_spent desc limit 100;</textarea>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="sf-mode" onchange="sfRun()">
        <option value="pretty" selected>{LBL_BEAUTIFY}</option>
        <option value="minify">{LBL_MINIFY}</option>
      </select>
    </div>
    <div>
      <label>Dialect</label>
      <select id="sf-dialect" onchange="sfRun()">
        <option value="ansi" selected>ANSI / standard</option>
        <option value="mysql">MySQL</option>
        <option value="postgres">PostgreSQL</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Indent</label>
      <select id="sf-indent" onchange="sfRun()">
        <option value="2" selected>2 spaces</option>
        <option value="4">4 spaces</option>
        <option value="tab">Tab</option>
      </select>
    </div>
    <div>
      <label>Keyword case</label>
      <select id="sf-case" onchange="sfRun()">
        <option value="upper" selected>UPPERCASE</option>
        <option value="lower">lowercase</option>
        <option value="keep">Keep as typed</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="sf-out" style="margin:0;flex:1">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('sf-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
const SF_TOP = ['SELECT','FROM','WHERE','GROUP BY','HAVING','ORDER BY','LIMIT','OFFSET','UNION','UNION ALL','INTERSECT','EXCEPT','VALUES','RETURNING','WITH'];
const SF_JOINS = ['LEFT JOIN','RIGHT JOIN','INNER JOIN','FULL JOIN','LEFT OUTER JOIN','RIGHT OUTER JOIN','FULL OUTER JOIN','CROSS JOIN','JOIN'];
const SF_NEWLINE_BEFORE = ['ON','AND','OR'];
const SF_KW_BASE = ['SELECT','FROM','WHERE','GROUP','BY','HAVING','ORDER','LIMIT','OFFSET','UNION','ALL','INTERSECT','EXCEPT','VALUES','RETURNING','WITH','AS','ON','AND','OR','NOT','IN','LIKE','ILIKE','BETWEEN','IS','NULL','TRUE','FALSE','CASE','WHEN','THEN','ELSE','END','DISTINCT','INSERT','INTO','UPDATE','SET','DELETE','CREATE','TABLE','INDEX','VIEW','DROP','ALTER','ADD','COLUMN','PRIMARY','KEY','FOREIGN','REFERENCES','CONSTRAINT','UNIQUE','DEFAULT','CHECK','LEFT','RIGHT','INNER','OUTER','FULL','CROSS','JOIN','USING','ASC','DESC','EXISTS','ANY','SOME','BEGIN','COMMIT','ROLLBACK','TRANSACTION','EXPLAIN','ANALYZE','CAST','COUNT','SUM','AVG','MIN','MAX','COALESCE','NULLIF','IF','REPLACE'];
const SF_DIALECT_KW = {
  mysql: ['DUAL','LIMIT','OFFSET','IGNORE','LOW_PRIORITY','HIGH_PRIORITY','STRAIGHT_JOIN','SQL_CALC_FOUND_ROWS','LOCK','SHARE','UPDATE','SEPARATOR','GROUP_CONCAT'],
  postgres: ['ILIKE','RETURNING','LATERAL','MATERIALIZED','USING','CONFLICT','DO','NOTHING','ARRAY','UNNEST','OVER','PARTITION'],
  ansi: ['LATERAL','OVER','PARTITION','WINDOW','ROWS','RANGE','PRECEDING','FOLLOWING','UNBOUNDED','CURRENT','ROW']
};

function sfTokenize(sql){
  const out = [];
  let i = 0;
  while(i < sql.length){
    const c = sql[i];
    // line comment
    if(c === '-' && sql[i+1] === '-'){
      const end = sql.indexOf('\\n', i);
      const stop = end === -1 ? sql.length : end;
      out.push({t:'comment', v: sql.slice(i, stop)});
      i = stop;
      continue;
    }
    // block comment
    if(c === '/' && sql[i+1] === '*'){
      const end = sql.indexOf('*/', i+2);
      const stop = end === -1 ? sql.length : end+2;
      out.push({t:'comment', v: sql.slice(i, stop)});
      i = stop;
      continue;
    }
    // strings: ' or "
    if(c === "'" || c === '"' || c === '`'){
      let j = i+1;
      while(j < sql.length){
        if(sql[j] === c && sql[j-1] !== '\\\\'){ if(sql[j+1] === c){ j += 2; continue; } break; }
        j++;
      }
      out.push({t:'str', v: sql.slice(i, j+1)});
      i = j+1;
      continue;
    }
    // whitespace
    if(/\\s/.test(c)){ i++; continue; }
    // numbers
    if(/[0-9]/.test(c)){
      let j = i;
      while(j < sql.length && /[0-9.eE+\\-]/.test(sql[j]) && !(sql[j] === '-' && sql[j-1] !== 'e' && sql[j-1] !== 'E')) j++;
      out.push({t:'num', v: sql.slice(i, j)});
      i = j;
      continue;
    }
    // identifier / keyword
    if(/[A-Za-z_$]/.test(c)){
      let j = i;
      while(j < sql.length && /[A-Za-z0-9_$.]/.test(sql[j])) j++;
      const v = sql.slice(i, j);
      out.push({t:'word', v});
      i = j;
      continue;
    }
    // operators / punctuation
    const two = sql.slice(i, i+2);
    if(['<=','>=','<>','!=','||','::'].includes(two)){
      out.push({t:'op', v: two}); i += 2; continue;
    }
    out.push({t:'punc', v: c});
    i++;
  }
  return out;
}

function sfApplyCase(word, mode){
  if(mode === 'upper') return word.toUpperCase();
  if(mode === 'lower') return word.toLowerCase();
  return word;
}

function sfFormat(sql, opts){
  const indent = opts.indent;
  const caseMode = opts.case;
  const dialectKW = new Set([...SF_KW_BASE, ...(SF_DIALECT_KW[opts.dialect] || [])].map(k => k.toUpperCase()));
  const tokens = sfTokenize(sql);
  // Pre-pass: combine multi-word keywords (LEFT JOIN, GROUP BY, ORDER BY, UNION ALL, etc.)
  const combined = [];
  for(let i = 0; i < tokens.length; i++){
    const t = tokens[i];
    if(t.t === 'word'){
      const u = t.v.toUpperCase();
      const next = tokens[i+1];
      const next2 = tokens[i+2];
      const tryThree = next && next.t === 'word' && next2 && next2.t === 'word'
        ? (u + ' ' + next.v.toUpperCase() + ' ' + next2.v.toUpperCase()) : null;
      const tryTwo = next && next.t === 'word' ? (u + ' ' + next.v.toUpperCase()) : null;
      const all = [...SF_TOP, ...SF_JOINS];
      if(tryThree && all.includes(tryThree)){
        combined.push({t:'kw', v: tryThree, isTop: SF_TOP.includes(tryThree), isJoin: SF_JOINS.includes(tryThree)});
        i += 2; continue;
      }
      if(tryTwo && all.includes(tryTwo)){
        combined.push({t:'kw', v: tryTwo, isTop: SF_TOP.includes(tryTwo), isJoin: SF_JOINS.includes(tryTwo)});
        i += 1; continue;
      }
      if(dialectKW.has(u)){
        combined.push({t:'kw', v: u, isTop: false, isJoin: false});
      } else {
        combined.push({t:'ident', v: t.v});
      }
      continue;
    }
    combined.push(t);
  }

  // Render
  let out = '';
  let depth = 0; // paren depth — affects sub-clause indent
  let needSpace = false;
  let lastChar = '';
  const pad = () => indent.repeat(depth);

  function write(s){ out += s; lastChar = s.slice(-1); needSpace = !/\\s$/.test(s) && s !== ''; }
  function nl(extraIndent){ out = out.replace(/[ \\t]+$/, ''); out += '\\n' + indent.repeat(depth) + (extraIndent ? indent : ''); needSpace = false; }

  for(let i = 0; i < combined.length; i++){
    const t = combined[i];
    if(t.t === 'kw'){
      const upper = t.v;
      const display = caseMode === 'keep' ? sql.slice(0,0) /* fallback */ : sfApplyCase(t.v, caseMode);
      // Top-level clause: line break before, no indent inside parens beyond depth
      if(t.isTop){
        if(out.trim() !== '') nl(false);
        write((caseMode === 'keep' ? upper : display));
        // Force newline+indent after top keyword in many cases:
        // SELECT/FROM/WHERE/etc — items after will be inline; we just leave one space
        continue;
      }
      if(t.isJoin){
        if(out.trim() !== '') nl(false);
        write(caseMode === 'keep' ? upper : display);
        continue;
      }
      if(SF_NEWLINE_BEFORE.includes(upper) && depth === 0){
        nl(true);
        write(caseMode === 'keep' ? upper : display);
        continue;
      }
      // keyword inline
      if(needSpace) write(' ');
      write(caseMode === 'keep' ? upper : display);
      continue;
    }
    if(t.t === 'comment'){
      if(out.trim() !== ''){ nl(false); }
      write(t.v);
      nl(false);
      continue;
    }
    if(t.t === 'punc'){
      if(t.v === '('){
        write('(');
        depth++;
        continue;
      }
      if(t.v === ')'){
        depth = Math.max(0, depth-1);
        out = out.replace(/[ \\t]+$/, '');
        write(')');
        continue;
      }
      if(t.v === ','){
        out = out.replace(/[ \\t]+$/, '');
        write(',');
        // newline-after-comma inside SELECT list when at depth 0 only
        if(depth === 0){ nl(true); }
        else { write(' '); }
        continue;
      }
      if(t.v === ';'){ write(';'); continue; }
      // other punc: just write
      if(needSpace && !'.'.includes(t.v) && !')'.includes(t.v)) write('');
      write(t.v);
      continue;
    }
    if(t.t === 'op'){
      if(needSpace) write(' ');
      write(t.v);
      write(' ');
      continue;
    }
    if(t.t === 'str' || t.t === 'num' || t.t === 'ident'){
      if(needSpace && !/^[).,;]/.test(t.v) && lastChar !== '.' && lastChar !== '(' && lastChar !== '') write(' ');
      write(t.v);
      continue;
    }
  }
  return out.split('\\n').map(l => l.replace(/\\s+$/, '')).join('\\n').replace(/\\n{3,}/g, '\\n\\n').trim();
}

function sfMinify(sql){
  const tokens = sfTokenize(sql);
  const parts = [];
  for(const t of tokens){
    if(t.t === 'comment') continue;
    parts.push(t.v);
  }
  // Re-join with single spaces, but no space before punctuation
  let s = '';
  for(let i = 0; i < parts.length; i++){
    const cur = parts[i];
    const prev = parts[i-1] || '';
    const noSpaceBefore = /^[),;.]$/.test(cur);
    const noSpaceAfter = /[(.]$/.test(prev);
    if(s && !noSpaceBefore && !noSpaceAfter) s += ' ';
    s += cur;
  }
  return s.replace(/\\s+/g, ' ').trim();
}

function sfRun(){
  const inp = document.getElementById('sf-in').value;
  const out = document.getElementById('sf-out');
  out.classList.remove('error');
  if(!inp.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const mode = document.getElementById('sf-mode').value;
    if(mode === 'minify'){ out.textContent = sfMinify(inp); return; }
    const indentChoice = document.getElementById('sf-indent').value;
    const indent = indentChoice === 'tab' ? '\\t' : ' '.repeat(parseInt(indentChoice, 10));
    const opts = {
      indent,
      case: document.getElementById('sf-case').value,
      dialect: document.getElementById('sf-dialect').value
    };
    out.textContent = sfFormat(inp, opts);
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + e.message;
  }
}
document.addEventListener('DOMContentLoaded', sfRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>SQL ranges from a one-liner you typed in <code>psql</code> to a 200-line analytics query that nobody can read until it's indented properly. This formatter takes any SELECT, INSERT, UPDATE, or DDL and rewrites it with consistent indentation, line breaks before each clause, and uniform keyword casing. The minify mode does the opposite — squashes everything to a single line for embedding in code or scripts. The whole thing runs in your browser; queries never leave the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Reformatting a query you copied out of a log file, ORM, or chat message into something diffable and reviewable.</li>
  <li>Normalising team conventions (UPPERCASE keywords, 2-space indent) before committing a migration script.</li>
  <li>Squashing a long pretty-printed query into a single line so it fits in a YAML config or a one-line CLI argument.</li>
  <li>Spotting structural problems — unbalanced parens, a missing comma in the SELECT list, or a JOIN with no ON — that are obvious once the query is indented.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>The formatter is structural, not semantic.</strong> It won't tell you if a query is correct SQL, only how to indent the tokens it sees. A syntax error in the input becomes a syntax error in the output.</li>
  <li><strong>Dialect-specific keywords vary.</strong> <code>ILIKE</code>, <code>RETURNING</code>, <code>LATERAL</code> are Postgres; <code>STRAIGHT_JOIN</code>, <code>SQL_CALC_FOUND_ROWS</code> are MySQL. Pick the right dialect or those words won't be recognised as keywords.</li>
  <li><strong>String literals are preserved verbatim.</strong> A multi-line string in single quotes keeps its line breaks; the formatter doesn't reflow text inside <code>'...'</code>.</li>
  <li><strong>Comments survive but get isolated on their own lines.</strong> If you had a <code>-- inline comment</code> mid-line, it'll move to its own line during pretty-print.</li>
  <li><strong>Minify strips comments.</strong> If you need them, don't minify.</li>
  <li><strong>It's not a linter.</strong> Use a real SQL parser (e.g. <code>sqlfluff</code>) for validation, style enforcement, and dialect checking in CI.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>SQL reicht vom Einzeiler im <code>psql</code> bis zur 200-Zeilen-Analytics-Query, die niemand lesen kann, bis sie eingerückt ist. Dieser Formatierer formatiert SELECT, INSERT, UPDATE oder DDL mit konsistenter Einrückung, Zeilenumbrüchen vor jeder Klausel und einheitlicher Keyword-Schreibweise. Der Minify-Modus macht das Gegenteil. Alles läuft im Browser.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Eine aus Log/ORM kopierte Query in etwas Lesbares umformatieren.</li>
<li>Team-Konventionen vor einem Migrations-Commit normalisieren.</li>
<li>Eine pretty-printed Query auf eine Zeile zusammenfassen.</li>
<li>Strukturprobleme (unbalancierte Klammern, fehlende Kommas) sichtbar machen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Strukturell, nicht semantisch.</strong> Validiert keine SQL-Syntax.</li>
<li><strong>Dialekt-spezifische Keywords.</strong> <code>ILIKE</code>, <code>RETURNING</code> sind Postgres; <code>STRAIGHT_JOIN</code> ist MySQL — Dialekt korrekt wählen.</li>
<li><strong>String-Literale bleiben unverändert.</strong></li>
<li><strong>Kommentare überleben aber landen auf eigenen Zeilen.</strong></li>
<li><strong>Minify entfernt Kommentare.</strong></li>
<li><strong>Kein Linter.</strong> Für CI <code>sqlfluff</code> o.ä. nutzen.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Una consulta SQL puede ser de una línea o de 200 líneas que nadie lee hasta indentarla. Este formateador reescribe SELECT/INSERT/UPDATE/DDL con indentación consistente, saltos de línea antes de cada cláusula y mayúsculas/minúsculas uniformes. Minify hace lo contrario. Todo en el navegador.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Reformatear una consulta copiada de un log u ORM.</li>
<li>Normalizar convenciones de equipo antes de un commit.</li>
<li>Aplastar una consulta a una línea para YAML o CLI.</li>
<li>Detectar paréntesis desbalanceados o comas faltantes.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Estructural, no semántico.</strong> No valida sintaxis SQL.</li>
<li><strong>Palabras clave por dialecto.</strong> <code>ILIKE</code>, <code>RETURNING</code> = Postgres; <code>STRAIGHT_JOIN</code> = MySQL.</li>
<li><strong>Las cadenas literales se preservan.</strong></li>
<li><strong>Los comentarios sobreviven pero van a líneas propias.</strong></li>
<li><strong>Minify elimina comentarios.</strong></li>
<li><strong>No es un linter.</strong> Usa <code>sqlfluff</code> en CI.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Une requête SQL peut être un one-liner ou 200 lignes illisibles tant qu'elles ne sont pas indentées. Ce formateur réécrit SELECT/INSERT/UPDATE/DDL avec indentation cohérente, sauts de ligne avant chaque clause et casse uniforme. Le mode minify fait l'inverse. Tout dans le navigateur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Reformater une requête copiée d'un log ou ORM.</li>
<li>Normaliser les conventions d'équipe avant un commit.</li>
<li>Compresser une requête en une ligne pour YAML ou CLI.</li>
<li>Repérer parenthèses non équilibrées ou virgules manquantes.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Structurel, pas sémantique.</strong> Ne valide pas la syntaxe SQL.</li>
<li><strong>Mots-clés selon dialecte.</strong> <code>ILIKE</code>, <code>RETURNING</code> = Postgres ; <code>STRAIGHT_JOIN</code> = MySQL.</li>
<li><strong>Les littéraux chaîne sont préservés.</strong></li>
<li><strong>Les commentaires survivent mais sont isolés sur leur ligne.</strong></li>
<li><strong>Minify supprime les commentaires.</strong></li>
<li><strong>Pas un linter.</strong> Utiliser <code>sqlfluff</code> en CI.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Una query SQL può essere una riga o 200 righe illeggibili finché non sono indentate. Questo formattatore riscrive SELECT/INSERT/UPDATE/DDL con indentazione coerente, a-capo prima di ogni clausola e maiuscole/minuscole uniformi. Minify fa il contrario. Tutto nel browser.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Riformattare una query copiata da log o ORM.</li>
<li>Normalizzare convenzioni di team prima di un commit.</li>
<li>Comprimere una query su una riga per YAML o CLI.</li>
<li>Vedere parentesi sbilanciate o virgole mancanti.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Strutturale, non semantico.</strong> Non valida la sintassi SQL.</li>
<li><strong>Parole chiave per dialetto.</strong> <code>ILIKE</code>, <code>RETURNING</code> = Postgres; <code>STRAIGHT_JOIN</code> = MySQL.</li>
<li><strong>I letterali stringa sono preservati.</strong></li>
<li><strong>I commenti sopravvivono ma su righe proprie.</strong></li>
<li><strong>Minify rimuove i commenti.</strong></li>
<li><strong>Non è un linter.</strong> Usa <code>sqlfluff</code> in CI.</li>
</ul>
""",
    },
    "related": ["json-formatter", "xml-formatter", "regex-tester", "css-minifier"],
}
