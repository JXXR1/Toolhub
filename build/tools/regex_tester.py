TOOL = {
    "slug": "regex-tester",
    "category": "developer",
    "icon": ".*",
    "tags": ["regex", "regular expression", "test", "match", "replace", "javascript"],
    "i18n": {
        "en": {
            "name": "Regex Tester",
            "tagline": "Test JavaScript regular expressions live. See matches, capture groups, and apply replacements as you type.",
            "description": "Free online JavaScript regex tester with live highlighting, capture groups, and replace mode. PCRE-compatible flags (g/i/m/s/u/y).",
        },
        "de": {
            "name": "Regex-Tester",
            "tagline": "JavaScript-Regex live testen. Treffer, Gruppen und Ersetzungen werden beim Tippen angezeigt.",
            "description": "Kostenloser JavaScript-Regex-Tester mit Live-Hervorhebung, Erfassungsgruppen und Ersetzungsmodus. PCRE-kompatible Flags.",
        },
        "es": {
            "name": "Probador de Regex",
            "tagline": "Prueba expresiones regulares de JavaScript en vivo. Coincidencias, grupos y reemplazos al instante.",
            "description": "Probador de regex JavaScript gratuito con resaltado en vivo, grupos de captura y modo reemplazo. Flags compatibles con PCRE.",
        },
        "fr": {
            "name": "Testeur Regex",
            "tagline": "Testez les expressions régulières JavaScript en direct. Correspondances, groupes de capture et remplacement instantanés.",
            "description": "Testeur regex JavaScript gratuit avec coloration en direct, groupes de capture et mode remplacement. Drapeaux compatibles PCRE.",
        },
        "it": {
            "name": "Tester Regex",
            "tagline": "Testa espressioni regolari JavaScript in tempo reale. Corrispondenze, gruppi di cattura e sostituzioni istantanee.",
            "description": "Tester regex JavaScript gratuito con evidenziazione live, gruppi di cattura e modalità sostituzione. Flag compatibili PCRE.",
        },
    },
    "body": """
<div class="tool-card">
  <label>Pattern</label>
  <div style="display:flex;gap:0.5rem;align-items:center">
    <span style="color:var(--text-muted);font-family:ui-monospace,monospace">/</span>
    <input type="text" id="re-pattern" placeholder="\\b(\\w+)@(\\w+\\.\\w+)\\b" oninput="reRun()" style="flex:1">
    <span style="color:var(--text-muted);font-family:ui-monospace,monospace">/</span>
    <input type="text" id="re-flags" value="g" oninput="reRun()" style="width:90px" placeholder="gimsuy">
  </div>
  <div class="meta" style="margin-top:0.5rem">Flags: <code>g</code> global · <code>i</code> case-insensitive · <code>m</code> multi-line · <code>s</code> dotAll · <code>u</code> unicode · <code>y</code> sticky</div>
</div>
<div class="tool-card">
  <label>Test string</label>
  <textarea id="re-input" oninput="reRun()" placeholder="Reach me at hello@example.com or admin@toolhub.software" spellcheck="false">Reach me at hello@example.com or admin@toolhub.software</textarea>
</div>
<div class="tool-card">
  <label>Highlighted matches</label>
  <pre class="output" id="re-highlight" style="word-break:break-word;white-space:pre-wrap"></pre>
  <div class="meta" id="re-meta"></div>
</div>
<div class="tool-card">
  <label>Capture groups</label>
  <div id="re-groups" class="output" style="font-size:0.88rem">{LBL_NO_INPUT}</div>
</div>
<div class="tool-card">
  <label>Replace</label>
  <input type="text" id="re-replace" placeholder="<a href=&quot;mailto:$&amp;&quot;>$&amp;</a>" oninput="reRun()">
  <div class="meta" style="margin-top:0.5rem">Use <code>$1</code>, <code>$2</code> for groups · <code>$&amp;</code> for the whole match · <code>$$</code> for literal $</div>
  <pre class="output" id="re-replaced" style="margin-top:0.75rem;word-break:break-word;white-space:pre-wrap">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function reEsc(s){ return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function reRun(){
  const pat = document.getElementById('re-pattern').value;
  const flags = document.getElementById('re-flags').value;
  const input = document.getElementById('re-input').value;
  const replaceWith = document.getElementById('re-replace').value;
  const hi = document.getElementById('re-highlight');
  const groupsEl = document.getElementById('re-groups');
  const meta = document.getElementById('re-meta');
  const repl = document.getElementById('re-replaced');
  if (!pat){ hi.textContent = ''; meta.textContent = ''; groupsEl.textContent = '{LBL_NO_INPUT}'; repl.textContent = ''; return; }
  let regex;
  try { regex = new RegExp(pat, flags); }
  catch(e){ hi.classList.add('error'); hi.textContent = '✗ ' + e.message; meta.textContent = ''; groupsEl.textContent = ''; repl.textContent = ''; return; }
  hi.classList.remove('error');
  // Highlight matches
  let out = '';
  let last = 0;
  let count = 0;
  const groups = [];
  const useGlobal = regex.global;
  if (useGlobal){
    let m;
    while ((m = regex.exec(input)) !== null){
      out += reEsc(input.slice(last, m.index));
      out += '<mark style="background:var(--accent);color:#fff;padding:0 2px;border-radius:2px">' + reEsc(m[0] || '') + '</mark>';
      last = m.index + (m[0]?.length || 0);
      count++;
      groups.push({index: m.index, match: m[0], groups: m.slice(1)});
      if (m[0] === '') { regex.lastIndex++; if (regex.lastIndex > input.length) break; }
      if (count > 10000) break;
    }
    out += reEsc(input.slice(last));
  } else {
    const m = regex.exec(input);
    if (m){
      out = reEsc(input.slice(0, m.index)) + '<mark style="background:var(--accent);color:#fff;padding:0 2px;border-radius:2px">' + reEsc(m[0]) + '</mark>' + reEsc(input.slice(m.index + m[0].length));
      count = 1;
      groups.push({index: m.index, match: m[0], groups: m.slice(1)});
    } else {
      out = reEsc(input);
    }
  }
  hi.innerHTML = out || '<span style="color:var(--text-muted)">(no matches)</span>';
  meta.textContent = count + ' match' + (count === 1 ? '' : 'es');
  // Capture groups
  if (groups.length === 0){
    groupsEl.textContent = '(no matches)';
  } else {
    groupsEl.innerHTML = groups.slice(0, 50).map((g, i) =>
      'Match ' + (i+1) + ' at index ' + g.index + ':\\n' +
      '  full: ' + reEsc(g.match) +
      (g.groups.length ? '\\n' + g.groups.map((cg, j) => '  $' + (j+1) + ': ' + reEsc(cg ?? '<undefined>')).join('\\n') : '')
    ).join('\\n\\n');
  }
  // Replace
  if (replaceWith !== ''){
    try {
      const replaced = input.replace(new RegExp(pat, flags), replaceWith);
      repl.textContent = replaced;
    } catch(e){ repl.textContent = '✗ ' + e.message; }
  } else {
    repl.textContent = '(enter a replacement above)';
  }
}
document.addEventListener('DOMContentLoaded', reRun);
</script>
""",
    "help": {
        "en": """
<h2>How it works</h2>
<p>Uses the JavaScript engine's native <code>RegExp</code> — same flavour as Node.js and the browser. Patterns and inputs never leave your device.</p>
<h3>Common patterns</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — email-ish</li>
  <li><code>^\\s*$</code> — empty/whitespace-only line (with <code>m</code> flag)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — named capture groups</li>
  <li><code>(?:.*)</code> — non-capturing group</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>
<h3>JavaScript regex gotchas</h3>
<ul>
  <li>JavaScript regex differs from PCRE — no <code>\\K</code>, no recursive patterns, lookbehind only since ES2018.</li>
  <li>Without <code>g</code> flag you get the first match only.</li>
  <li><code>$&amp;</code> is the whole match; <code>$1</code>, <code>$2</code>, ... are groups; <code>$$</code> is a literal $.</li>
</ul>
""",
    },
    "related": ["json-formatter", "text-diff", "case-converter"],
}
