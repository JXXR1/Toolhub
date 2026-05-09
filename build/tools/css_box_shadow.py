TOOL = {
    "slug": "css-box-shadow",
    "category": "design",
    "icon": "▣",
    "tags": ["css", "shadow", "box-shadow", "design", "depth", "elevation"],
    "i18n": {
        "en": {
            "name": "CSS Box Shadow Generator",
            "tagline": "Build single or multi-layer CSS box shadows visually. Adjust offset, blur, spread, color, and copy CSS.",
            "description": "Free CSS box-shadow generator. Stack multiple shadows for realistic elevation, toggle inset, fine-tune blur and spread, and copy production-ready CSS in one click.",
        },
        "de": {"name": "CSS Box-Shadow-Generator", "tagline": "Erstelle einzel- oder mehrlagige CSS-Box-Shadows visuell. Offset, Blur, Spread, Farbe einstellen und CSS kopieren.", "description": "Kostenloser CSS Box-Shadow-Generator. Stapele mehrere Shadows, schalte inset, feinjustiere Blur und Spread, kopiere CSS mit einem Klick."},
        "es": {"name": "Generador de Box Shadow CSS", "tagline": "Crea sombras CSS de una o varias capas visualmente. Ajusta offset, blur, spread, color y copia el CSS.", "description": "Generador gratuito de box-shadow CSS. Apila varias sombras, alterna inset, afina blur y spread, copia CSS listo en un clic."},
        "fr": {"name": "Générateur Box Shadow CSS", "tagline": "Créez des ombres CSS simples ou multi-couches visuellement. Réglez offset, blur, spread, couleur, copiez le CSS.", "description": "Générateur gratuit de box-shadow CSS. Empilez plusieurs ombres, basculez inset, affinez blur et spread, copiez le CSS en un clic."},
        "it": {"name": "Generatore Box Shadow CSS", "tagline": "Crea ombre CSS singole o multi-livello visualmente. Regola offset, blur, spread, colore e copia il CSS.", "description": "Generatore gratuito di box-shadow CSS. Sovrapponi più ombre, alterna inset, regola blur e spread, copia CSS pronto in un clic."},
    },
    "body": """
<div class="tool-card">
  <label>Shadow layers</label>
  <div id="bs-layers" class="bs-layers"></div>
  <div class="button-row" style="margin-top:0.6rem">
    <button class="secondary" onclick="bsAddLayer()">+ Add layer</button>
    <button class="secondary" onclick="bsPreset('soft')">Soft</button>
    <button class="secondary" onclick="bsPreset('elevation')">Material elevation</button>
    <button class="secondary" onclick="bsPreset('glow')">Glow</button>
  </div>
</div>
<div class="tool-card">
  <label>Preview</label>
  <div class="bs-preview-wrap">
    <div id="bs-preview" class="bs-box">Sample</div>
  </div>
</div>
<div class="tool-card">
  <label>CSS</label>
  <div class="output-row">
    <pre class="output" id="bs-css"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('bs-css', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<style>
.bs-layers{display:flex;flex-direction:column;gap:0.6rem;margin-top:0.4rem}
.bs-layer{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem}
.bs-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:0.5rem;align-items:center}
.bs-row label{font-size:0.78rem;color:var(--text-muted)}
.bs-row input[type=number]{width:100%;font-family:ui-monospace,monospace}
.bs-row input[type=color]{width:100%;height:32px;padding:2px}
.bs-actions{display:flex;justify-content:space-between;align-items:center;margin-top:0.4rem;font-size:0.85rem}
.bs-preview-wrap{display:flex;justify-content:center;align-items:center;padding:3rem 1rem;background:var(--bg);border:1px solid var(--border);border-radius:8px}
.bs-box{width:160px;height:120px;background:#fff;color:#222;display:flex;align-items:center;justify-content:center;font-weight:600;border-radius:8px}
</style>
<script>
let bsLayers = [
  {x:0, y:4, blur:8, spread:0, color:'#00000033', inset:false}
];
const BS_PRESETS = {
  soft: [{x:0,y:1,blur:3,spread:0,color:'#0000001a',inset:false},{x:0,y:1,blur:2,spread:0,color:'#0000000f',inset:false}],
  elevation: [{x:0,y:3,blur:6,spread:0,color:'#00000026',inset:false},{x:0,y:1,blur:18,spread:0,color:'#00000026',inset:false}],
  glow: [{x:0,y:0,blur:24,spread:4,color:'#3498dbaa',inset:false}]
};
function bsRender(){
  const wrap = document.getElementById('bs-layers');
  wrap.innerHTML = '';
  bsLayers.forEach((L,i) => {
    const card = document.createElement('div');
    card.className = 'bs-layer';
    card.innerHTML = `
      <div class="bs-row">
        <div><label>X (px)</label><input type="number" value="${L.x}" oninput="bsLayers[${i}].x = +this.value; bsRun()"></div>
        <div><label>Y (px)</label><input type="number" value="${L.y}" oninput="bsLayers[${i}].y = +this.value; bsRun()"></div>
        <div><label>Blur (px)</label><input type="number" min="0" value="${L.blur}" oninput="bsLayers[${i}].blur = +this.value; bsRun()"></div>
        <div><label>Spread (px)</label><input type="number" value="${L.spread}" oninput="bsLayers[${i}].spread = +this.value; bsRun()"></div>
        <div><label>Color</label><input type="color" value="${L.color.slice(0,7)}" oninput="bsLayers[${i}].color = this.value + (bsLayers[${i}].color.length===9 ? bsLayers[${i}].color.slice(7) : ''); bsRun()"></div>
        <div><label>Alpha</label><input type="range" min="0" max="255" value="${L.color.length===9 ? parseInt(L.color.slice(7),16) : 255}" oninput="bsLayers[${i}].color = bsLayers[${i}].color.slice(0,7) + (+this.value).toString(16).padStart(2,'0'); bsRun()"></div>
      </div>
      <div class="bs-actions">
        <label><input type="checkbox" ${L.inset?'checked':''} onchange="bsLayers[${i}].inset = this.checked; bsRun()"> inset</label>
        <button class="secondary" onclick="bsRemove(${i})" ${bsLayers.length<=1?'disabled':''}>Remove</button>
      </div>
    `;
    wrap.appendChild(card);
  });
}
function bsAddLayer(){
  bsLayers.push({x:0, y:8, blur:16, spread:0, color:'#00000022', inset:false});
  bsRender(); bsRun();
}
function bsRemove(i){
  if(bsLayers.length<=1) return;
  bsLayers.splice(i,1);
  bsRender(); bsRun();
}
function bsPreset(k){
  bsLayers = JSON.parse(JSON.stringify(BS_PRESETS[k]));
  bsRender(); bsRun();
}
function bsRun(){
  const css = bsLayers.map(L => `${L.inset?'inset ':''}${L.x}px ${L.y}px ${L.blur}px ${L.spread}px ${L.color}`).join(', ');
  document.getElementById('bs-preview').style.boxShadow = css;
  document.getElementById('bs-css').textContent = `box-shadow: ${css};`;
}
document.addEventListener('DOMContentLoaded', () => { bsRender(); bsRun(); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>The CSS <code>box-shadow</code> property is the workhorse for adding depth — drop shadows on cards, button highlights, focus rings, glows, neon effects, even fake 3D. The syntax (<code>x y blur spread color</code>, optional <code>inset</code>, multiple shadows comma-separated) is easy to read but tedious to tweak blind. This tool gives you sliders for every value and a live preview, plus presets that match common design-system elevations.</p>

<h3>When to use it</h3>
<ul>
  <li>Designing card or modal elevation that doesn't look "cheap and harsh".</li>
  <li>Building a focus-ring style for accessibility (e.g. a 2px outline glow).</li>
  <li>Crafting a neon or glow effect for a hero CTA.</li>
  <li>Replicating Material Design or Apple-style elevation tokens for a design system.</li>
  <li>Making fake "inset" depth for a pressed-button effect or a card recess.</li>
</ul>

<h3>What each value does</h3>
<ul>
  <li><strong>X / Y offset</strong> — direction the shadow falls (positive Y = down). For a "light from above" feel, use Y > 0 and small or zero X.</li>
  <li><strong>Blur</strong> — how soft the edge is. 0 = sharp; larger = softer fade.</li>
  <li><strong>Spread</strong> — how much bigger (or smaller, if negative) the shadow is than the box itself.</li>
  <li><strong>Color &amp; alpha</strong> — usually a partial-alpha black or brand color. Pure <code>#000</code> looks too heavy; try <code>#0003</code> to <code>#0002</code> for natural depth.</li>
  <li><strong>Inset</strong> — flips the shadow inward, like a recess.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>One big shadow looks artificial.</strong> Real elevation is two or three layers stacked: a tight, dark, close-in shadow plus a wide, soft, far-out one. The "Material elevation" preset shows the pattern.</li>
  <li><strong>Pure black is too heavy.</strong> Use ~10–25% alpha black, or tint the shadow with the surface's complement for warmth.</li>
  <li><strong>Shadows render outside the box.</strong> If your container has <code>overflow: hidden</code>, the shadow is clipped. Use a wrapper or move <code>overflow</code> to a child.</li>
  <li><strong>Shadow on transparent background.</strong> If the box has no <code>background</code>, the shadow shows through the box itself — usually surprising.</li>
  <li><strong>Performance:</strong> very large blur on lots of elements can be expensive on low-end mobile. Test on a real device before shipping fancy glows.</li>
  <li><strong>Dark mode.</strong> Subtle dark-on-dark shadows almost disappear; consider a bright inner border or a light-tinted shadow in dark themes.</li>
</ul>
""",
    },
    "related": ["css-gradient", "color-picker", "color-converter"],
}
