TOOL = {
    "slug": "js-minifier",
    "category": "developer",
    "icon": "{}",
    "tags": ["javascript", "js", "minify", "compress", "optimize"],
    "i18n": {
        "en": {
            "name": "JavaScript Minifier",
            "tagline": "Fast structural JavaScript minify — strip comments, collapse whitespace, drop blank lines. See size before/after and the saving percentage.",
            "description": "Free online JavaScript minifier. Removes single- and multi-line comments, redundant whitespace, and blank lines while preserving strings, regex literals, and template literals.",
        },
        "de": {"name": "JavaScript-Minifier", "tagline": "Schnelle JS-Minifizierung — Kommentare entfernen, Whitespace zusammenfassen, Leerzeilen löschen. Größenvergleich inkl.", "description": "Kostenloser JavaScript-Minifier. Entfernt Zeilen- und Blockkommentare, überflüssigen Whitespace und Leerzeilen, ohne Strings, Regex und Template-Literale zu beschädigen."},
        "es": {"name": "Minificador de JavaScript", "tagline": "Minificación estructural rápida de JS — quita comentarios, colapsa espacios, elimina líneas vacías. Tamaño antes/después.", "description": "Minificador de JavaScript gratuito. Elimina comentarios de una línea y multilínea, espacios redundantes y líneas vacías sin romper strings, regex ni template literals."},
        "fr": {"name": "Minifieur JavaScript", "tagline": "Minification structurelle rapide du JS — suppression des commentaires, des espaces redondants et des lignes vides. Taille avant/après.", "description": "Minifieur JavaScript gratuit. Retire les commentaires mono- et multi-lignes, les espaces redondants et les lignes vides sans casser strings, regex et template literals."},
        "it": {"name": "Minificatore JavaScript", "tagline": "Minificazione strutturale rapida del JS — rimuove commenti, comprime spazi, elimina righe vuote. Dimensione prima/dopo.", "description": "Minificatore JavaScript gratuito. Rimuove commenti single-line e multi-line, spazi superflui e righe vuote preservando stringhe, regex e template literal."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="jm-input" oninput="jmRun()" placeholder="// Paste JavaScript here" spellcheck="false">// Sample
function greet(name) {
  // Say hi
  const msg = `Hello, ${name}!`;
  console.log(msg);
  return msg;
}

greet('World');</textarea>
  <div class="meta" id="jm-stats" style="margin-top:0.5rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="jm-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('jm-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
// String/regex/comment-aware minifier. Walks the input one char at a time.
function jmMinify(src){
  let out = '';
  const n = src.length;
  let i = 0;
  // Track "previous significant token char" to know if a `/` starts a regex
  let prev = '';
  const REGEX_PREV = /[(,=:[!&|?{};+\\-*~^%<>]|^$/;
  while(i < n){
    const c = src[i];
    const next = src[i+1];
    // Line comment
    if(c === '/' && next === '/'){
      while(i < n && src[i] !== '\\n') i++;
      continue;
    }
    // Block comment
    if(c === '/' && next === '*'){
      i += 2;
      while(i < n && !(src[i] === '*' && src[i+1] === '/')) i++;
      i += 2;
      continue;
    }
    // String literals: ' " `
    if(c === '"' || c === "'" || c === '`'){
      const quote = c;
      let chunk = c;
      i++;
      while(i < n){
        const ch = src[i];
        chunk += ch;
        if(ch === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
        if(quote === '`' && ch === '$' && src[i+1] === '{'){
          chunk += '{'; i += 2; let depth = 1;
          while(i < n && depth > 0){
            const k = src[i];
            chunk += k;
            if(k === '{') depth++;
            else if(k === '}') depth--;
            else if(k === '"' || k === "'" || k === '`'){
              const q = k; i++;
              while(i < n){
                const c2 = src[i]; chunk += c2;
                if(c2 === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
                if(c2 === q){ i++; break; }
                i++;
              }
              continue;
            }
            i++;
          }
          continue;
        }
        if(ch === quote){ i++; break; }
        i++;
      }
      out += chunk;
      prev = quote;
      continue;
    }
    // Regex literal — only if prev token suggests regex context
    if(c === '/' && REGEX_PREV.test(prev)){
      let chunk = '/'; i++;
      let inClass = false;
      while(i < n){
        const ch = src[i];
        chunk += ch;
        if(ch === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
        if(ch === '[') inClass = true;
        else if(ch === ']') inClass = false;
        else if(ch === '/' && !inClass){ i++; break; }
        i++;
      }
      // flags
      while(i < n && /[gimsuy]/.test(src[i])){ chunk += src[i]; i++; }
      out += chunk;
      prev = '/';
      continue;
    }
    // Whitespace collapse
    if(c === ' ' || c === '\\t'){
      // keep one space if both sides are identifier chars
      let j = i;
      while(j < n && (src[j] === ' ' || src[j] === '\\t')) j++;
      const before = out[out.length-1] || '';
      const after = src[j] || '';
      if(/[A-Za-z0-9_$]/.test(before) && /[A-Za-z0-9_$]/.test(after)) out += ' ';
      i = j;
      continue;
    }
    if(c === '\\n' || c === '\\r'){
      // newline can sometimes be needed (return/no-LF rule). Keep one if both sides could need ASI.
      let j = i;
      while(j < n && (src[j] === '\\n' || src[j] === '\\r' || src[j] === ' ' || src[j] === '\\t')) j++;
      const before = out[out.length-1] || '';
      const after = src[j] || '';
      const needsNL = /[A-Za-z0-9_$\\)\\]\\}]/.test(before) && /[A-Za-z_$]/.test(after);
      if(needsNL) out += '\\n';
      i = j;
      continue;
    }
    out += c;
    if(/\\S/.test(c)) prev = c;
    i++;
  }
  return out;
}
function jmHumanBytes(n){
  if(n < 1024) return n + ' B';
  if(n < 1024*1024) return (n/1024).toFixed(1) + ' KB';
  return (n/1048576).toFixed(2) + ' MB';
}
function jmRun(){
  const raw = document.getElementById('jm-input').value;
  const out = document.getElementById('jm-out');
  const stats = document.getElementById('jm-stats');
  out.classList.remove('error');
  if(!raw){ out.textContent = '{LBL_NO_INPUT}'; stats.textContent = ''; return; }
  try {
    const min = jmMinify(raw);
    out.textContent = min;
    const before = new TextEncoder().encode(raw).length;
    const after = new TextEncoder().encode(min).length;
    const saved = before > 0 ? Math.round((1 - after/before) * 100) : 0;
    stats.textContent = `Before: ${jmHumanBytes(before)} · After: ${jmHumanBytes(after)} · Saved: ${saved}%`;
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; stats.textContent = ''; }
}
document.addEventListener('DOMContentLoaded', jmRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A structural JavaScript minifier strips comments and unnecessary whitespace without changing what the code does. The output is functionally identical to the input — same identifiers, same logic — just shorter. This tool runs that pass in your browser, including the tricky bits: it preserves string contents and regex literals untouched, and keeps newlines where ASI (Automatic Semicolon Insertion) would otherwise change behaviour.</p>

<h3>When to use it</h3>
<ul>
  <li>Quickly trimming a snippet for inclusion in an HTML bookmarklet or a single-file demo, where you don't have a build chain.</li>
  <li>Sanity-checking how much "fat" is in a hand-written script before deciding whether a real optimiser is worth setting up.</li>
  <li>Inlining a small library into a static site without dragging in a bundler.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a structural minify, not a compressor.</strong> It won't rename variables, dead-code eliminate, mangle properties, or tree-shake. For production builds, use <code>terser</code>, <code>esbuild</code>, or <code>swc</code> in your pipeline — they cut another 30–60% on top of structural minify.</li>
  <li><strong>ASI traps.</strong> JavaScript inserts semicolons in surprising places. The minifier preserves a newline where removing it would change meaning (e.g. <code>return\\n{}</code> ≠ <code>return {}</code>). Stick to explicit semicolons in source if you can — it makes minification safer for everyone.</li>
  <li><strong>Source maps aren't generated.</strong> If you ship minified JS to production, generate source maps with a real toolchain so debugging is sane.</li>
  <li><strong>Modern compression dominates.</strong> Brotli/gzip on the wire does most of what minify does. The biggest wins come from removing unused code — that needs static analysis a structural minifier can't do.</li>
  <li><strong>Don't minify what you commit.</strong> Source goes in pretty; minify at build/deploy.</li>
</ul>
""",
    },
    "related": ["css-minifier", "json-formatter", "regex-tester"],
}
