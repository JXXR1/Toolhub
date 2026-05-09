TOOL = {
    "slug": "wcag-contrast",
    "category": "design",
    "icon": "◐",
    "tags": ["wcag", "contrast", "accessibility", "a11y", "color", "ratio"],
    "i18n": {
        "en": {
            "name": "WCAG Contrast Checker",
            "tagline": "Check the contrast ratio between two colors. Pass/fail verdict for WCAG AA and AAA at every text size.",
            "description": "Free WCAG contrast ratio checker. Pick foreground and background colors, get the ratio (1:1 to 21:1) and pass/fail verdicts for WCAG 2.1 AA and AAA — for normal text, large text, and UI components.",
        },
        "de": {"name": "WCAG-Kontrast-Prüfer", "tagline": "Prüfe das Kontrastverhältnis zwischen zwei Farben. Pass/fail nach WCAG AA und AAA für jede Textgröße.", "description": "Kostenloser WCAG-Kontrastprüfer. Wähle Vordergrund- und Hintergrundfarben, erhalte das Verhältnis (1:1 bis 21:1) und Pass/Fail nach WCAG 2.1 AA und AAA."},
        "es": {"name": "Verificador de Contraste WCAG", "tagline": "Comprueba el ratio de contraste entre dos colores. Veredicto pass/fail para WCAG AA y AAA en todos los tamaños.", "description": "Verificador gratuito de contraste WCAG. Elige colores de primer plano y fondo, obtén el ratio (1:1 a 21:1) y veredicto pass/fail según WCAG 2.1 AA y AAA."},
        "fr": {"name": "Vérificateur de Contraste WCAG", "tagline": "Vérifiez le ratio de contraste entre deux couleurs. Verdict pass/fail pour WCAG AA et AAA à toute taille.", "description": "Vérificateur gratuit de contraste WCAG. Choisissez les couleurs avant-plan et fond, obtenez le ratio (1:1 à 21:1) et verdict pass/fail selon WCAG 2.1 AA et AAA."},
        "it": {"name": "Verificatore Contrasto WCAG", "tagline": "Controlla il rapporto di contrasto tra due colori. Verdetto pass/fail per WCAG AA e AAA a ogni dimensione.", "description": "Verificatore gratuito di contrasto WCAG. Scegli colori di primo piano e sfondo, ottieni il rapporto (1:1 a 21:1) e verdetto pass/fail secondo WCAG 2.1 AA e AAA."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Foreground</label>
      <div class="wc-row">
        <input type="color" id="wc-fg-pick" value="#222222" oninput="wcSync('fg', this.value); wcRun()">
        <input type="text" id="wc-fg-hex" value="#222222" oninput="wcSync('fg-from-hex', this.value); wcRun()" style="font-family:ui-monospace,monospace">
      </div>
    </div>
    <div>
      <label>Background</label>
      <div class="wc-row">
        <input type="color" id="wc-bg-pick" value="#ffffff" oninput="wcSync('bg', this.value); wcRun()">
        <input type="text" id="wc-bg-hex" value="#ffffff" oninput="wcSync('bg-from-hex', this.value); wcRun()" style="font-family:ui-monospace,monospace">
      </div>
    </div>
  </div>
  <div class="button-row" style="margin-top:0.6rem">
    <button class="secondary" onclick="wcSwap()">Swap</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="wc-preview" class="wc-preview">
    <div class="wc-sample wc-large">Aa — Large text 24px / 18px bold</div>
    <div class="wc-sample wc-normal">Aa — Normal text 16px</div>
    <div class="wc-sample wc-small">Aa — Small text 12px</div>
  </div>
  <div id="wc-meta" class="wc-meta"></div>
</div>
""",
    "script": """
<style>
.wc-row{display:flex;gap:0.5rem;align-items:center}
.wc-row input[type=color]{width:48px;height:42px;padding:2px;flex:0 0 auto}
.wc-row input[type=text]{flex:1}
.wc-preview{border:1px solid var(--border);border-radius:8px;padding:1rem;display:flex;flex-direction:column;gap:0.6rem;background:#fff;color:#222}
.wc-sample{padding:0.5rem 0.75rem;border-radius:4px}
.wc-large{font-size:1.5rem;font-weight:600}
.wc-normal{font-size:1rem}
.wc-small{font-size:0.78rem}
.wc-meta{margin-top:0.6rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:0.6rem;font-size:0.9rem}
.wc-card{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.wc-ratio{font-family:ui-monospace,monospace;font-size:1.6rem;font-weight:600;color:var(--accent)}
.wc-row-result{display:flex;justify-content:space-between;font-size:0.85rem;margin-top:0.25rem}
.wc-pass{color:#10b981;font-weight:600}
.wc-fail{color:#ef4444;font-weight:600}
</style>
<script>
function wcHexToRgb(h){
  h = (h||'').trim().replace(/^#/,'');
  if(h.length===3) h = h.split('').map(c=>c+c).join('');
  if(!/^[0-9a-fA-F]{6}$/.test(h)) return null;
  return [parseInt(h.slice(0,2),16), parseInt(h.slice(2,4),16), parseInt(h.slice(4,6),16)];
}
function wcLum(r,g,b){
  const lin = c => { c/=255; return c<=0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4) };
  return 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b);
}
function wcRatio(fg, bg){
  const L1 = wcLum(...fg), L2 = wcLum(...bg);
  const hi = Math.max(L1,L2), lo = Math.min(L1,L2);
  return (hi + 0.05) / (lo + 0.05);
}
function wcSync(which, val){
  if(which==='fg'){ document.getElementById('wc-fg-hex').value = val }
  else if(which==='bg'){ document.getElementById('wc-bg-hex').value = val }
  else if(which==='fg-from-hex'){
    const rgb = wcHexToRgb(val);
    if(rgb) document.getElementById('wc-fg-pick').value = '#' + rgb.map(x=>x.toString(16).padStart(2,'0')).join('');
  } else if(which==='bg-from-hex'){
    const rgb = wcHexToRgb(val);
    if(rgb) document.getElementById('wc-bg-pick').value = '#' + rgb.map(x=>x.toString(16).padStart(2,'0')).join('');
  }
}
function wcSwap(){
  const a = document.getElementById('wc-fg-hex').value;
  const b = document.getElementById('wc-bg-hex').value;
  document.getElementById('wc-fg-hex').value = b; wcSync('fg-from-hex', b);
  document.getElementById('wc-bg-hex').value = a; wcSync('bg-from-hex', a);
  wcRun();
}
function wcVerdict(ratio, threshold){
  return ratio >= threshold ? `<span class="wc-pass">✓ Pass</span>` : `<span class="wc-fail">✗ Fail</span>`;
}
function wcRun(){
  const fg = wcHexToRgb(document.getElementById('wc-fg-hex').value);
  const bg = wcHexToRgb(document.getElementById('wc-bg-hex').value);
  const meta = document.getElementById('wc-meta');
  const preview = document.getElementById('wc-preview');
  if(!fg || !bg){ meta.innerHTML = '<div class="wc-card">Enter valid hex colors above.</div>'; return; }
  const fgHex = '#' + fg.map(x=>x.toString(16).padStart(2,'0')).join('');
  const bgHex = '#' + bg.map(x=>x.toString(16).padStart(2,'0')).join('');
  preview.style.background = bgHex;
  preview.style.color = fgHex;
  const r = wcRatio(fg, bg);
  meta.innerHTML = `
    <div class="wc-card"><div class="wc-ratio">${r.toFixed(2)}:1</div><div class="meta">Contrast ratio (1:1 to 21:1)</div></div>
    <div class="wc-card">
      <div><strong>Normal text</strong> (≥4.5 AA · ≥7 AAA)</div>
      <div class="wc-row-result"><span>AA</span>${wcVerdict(r, 4.5)}</div>
      <div class="wc-row-result"><span>AAA</span>${wcVerdict(r, 7.0)}</div>
    </div>
    <div class="wc-card">
      <div><strong>Large text</strong> (≥3 AA · ≥4.5 AAA)</div>
      <div class="wc-row-result"><span>AA</span>${wcVerdict(r, 3.0)}</div>
      <div class="wc-row-result"><span>AAA</span>${wcVerdict(r, 4.5)}</div>
    </div>
    <div class="wc-card">
      <div><strong>UI components</strong> (≥3 AA — WCAG 1.4.11)</div>
      <div class="wc-row-result"><span>AA</span>${wcVerdict(r, 3.0)}</div>
    </div>
  `;
}
document.addEventListener('DOMContentLoaded', wcRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>WCAG (Web Content Accessibility Guidelines) defines a minimum contrast ratio between text and its background so people with low vision, colour-blindness, or in glare conditions can still read it. This tool computes that ratio (1:1 = identical, 21:1 = pure black on pure white) and tells you whether your colour pair passes WCAG 2.1 Level AA or AAA, separately for normal text, large text, and UI components. The maths follows the W3C luminance formula exactly.</p>

<h3>When to use it</h3>
<ul>
  <li>Checking whether your brand colour on a white card meets accessibility standards.</li>
  <li>Picking a button text colour that passes AA against a brand-coloured background.</li>
  <li>Auditing a design system token by token before shipping.</li>
  <li>Justifying a colour-change request to a stakeholder with a concrete pass/fail verdict.</li>
  <li>Testing what your users with reduced contrast preferences will actually see.</li>
</ul>

<h3>The thresholds</h3>
<ul>
  <li><strong>Normal text</strong> (under 18pt / 14pt bold): <strong>4.5:1</strong> for AA, <strong>7:1</strong> for AAA.</li>
  <li><strong>Large text</strong> (≥18pt or ≥14pt bold): <strong>3:1</strong> for AA, <strong>4.5:1</strong> for AAA.</li>
  <li><strong>UI components &amp; graphics</strong> (icons, focus rings, form borders, chart elements that convey info): <strong>3:1</strong> for AA (WCAG 2.1 §1.4.11). No AAA tier.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>"Large text" is bigger than you think.</strong> 18pt is roughly 24px. 14pt bold is roughly 19px bold. Body copy at 16px is <em>not</em> large text — it needs the 4.5:1 threshold.</li>
  <li><strong>Light text on a busy photo will fail.</strong> The contrast ratio is between specific pixels — overlay a dark gradient or use a solid panel to give the text a controlled background.</li>
  <li><strong>Anti-aliasing softens contrast.</strong> 4.5:1 is the floor, not a goal. Comfortable reading usually wants 7:1 or better, especially for body copy.</li>
  <li><strong>Hover and focus states count.</strong> If your button passes AA at rest but fails on hover, that's a real accessibility bug.</li>
  <li><strong>WCAG 2.1 vs APCA.</strong> The new APCA (Accessible Perceptual Contrast Algorithm), proposed for WCAG 3, gives different and arguably better numbers — but WCAG 2.1 is the legal standard most jurisdictions still reference. Use this tool's numbers when meeting EN 301 549, ADA, or AA-conformance claims.</li>
  <li><strong>Don't pad with transparency.</strong> A 50% alpha foreground over a known background has a different effective contrast — compute against the actual rendered colour, not the original.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "css-gradient"],
}
