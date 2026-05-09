TOOL = {
    "slug": "css-gradient",
    "category": "design",
    "icon": "🌈",
    "tags": ["css", "gradient", "linear", "radial", "design", "background"],
    "i18n": {
        "en": {
            "name": "CSS Gradient Generator",
            "tagline": "Build linear and radial CSS gradients visually. Edit color stops, copy ready-to-paste CSS.",
            "description": "Free CSS gradient generator. Build linear or radial gradients with as many color stops as you want, adjust angle and shape, copy production-ready CSS in one click.",
        },
        "de": {"name": "CSS-Gradient-Generator", "tagline": "Erstelle lineare und radiale CSS-Gradienten visuell. Farbstops bearbeiten, fertiges CSS kopieren.", "description": "Kostenloser CSS-Gradient-Generator. Erstelle lineare oder radiale Gradienten mit beliebig vielen Farbstops, kopiere produktionsreifes CSS mit einem Klick."},
        "es": {"name": "Generador de Gradiente CSS", "tagline": "Crea gradientes CSS lineales y radiales visualmente. Edita paradas de color, copia CSS listo para producción.", "description": "Generador gratuito de gradientes CSS. Crea gradientes lineales o radiales con tantas paradas como quieras, copia CSS listo en un clic."},
        "fr": {"name": "Générateur de Dégradé CSS", "tagline": "Créez des dégradés CSS linéaires et radiaux visuellement. Éditez les couleurs, copiez le CSS prêt à coller.", "description": "Générateur gratuit de dégradé CSS. Créez des dégradés linéaires ou radiaux avec autant d'arrêts que vous voulez, copiez le CSS en un clic."},
        "it": {"name": "Generatore di Gradienti CSS", "tagline": "Crea gradienti CSS lineari e radiali visualmente. Modifica i punti colore, copia CSS pronto.", "description": "Generatore gratuito di gradienti CSS. Crea gradienti lineari o radiali con quanti punti vuoi, copia CSS pronto in un clic."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_TYPE}</label>
      <select id="gr-type" onchange="grRun()">
        <option value="linear">Linear</option>
        <option value="radial">Radial</option>
      </select>
    </div>
    <div id="gr-angle-wrap">
      <label>Angle <span id="gr-angle-val" class="meta">90°</span></label>
      <input type="range" id="gr-angle" min="0" max="360" value="90" oninput="grAngleSync(); grRun()">
    </div>
    <div id="gr-shape-wrap" style="display:none">
      <label>Shape</label>
      <select id="gr-shape" onchange="grRun()">
        <option value="ellipse">Ellipse (default)</option>
        <option value="circle">Circle</option>
      </select>
    </div>
  </div>
  <label style="margin-top:0.7rem">Color stops</label>
  <div id="gr-stops" class="gr-stops"></div>
  <div class="button-row" style="margin-top:0.6rem">
    <button class="secondary" onclick="grAddStop()">+ Add stop</button>
    <button class="secondary" onclick="grPreset('sunset')">Sunset</button>
    <button class="secondary" onclick="grPreset('ocean')">Ocean</button>
    <button class="secondary" onclick="grPreset('candy')">Candy</button>
  </div>
</div>
<div class="tool-card">
  <label>Preview</label>
  <div id="gr-preview" class="gr-preview"></div>
</div>
<div class="tool-card">
  <label>CSS</label>
  <div class="output-row">
    <pre class="output" id="gr-css"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('gr-css', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<style>
.gr-stops{display:flex;flex-direction:column;gap:0.45rem;margin-top:0.4rem}
.gr-stop{display:grid;grid-template-columns:48px 1fr 80px 28px;gap:0.5rem;align-items:center}
.gr-stop input[type=color]{width:48px;height:36px;padding:2px}
.gr-stop input[type=range]{width:100%}
.gr-stop input[type=number]{width:100%;font-family:ui-monospace,monospace}
.gr-stop button{padding:0;width:28px;height:28px;background:transparent;border:1px solid var(--border);color:var(--text-muted);border-radius:6px;cursor:pointer}
.gr-preview{height:220px;border:1px solid var(--border);border-radius:8px}
</style>
<script>
let grStops = [
  {color:'#3498db', pos:0},
  {color:'#9b59b6', pos:100}
];
const GR_PRESETS = {
  sunset: [{color:'#ff7e5f',pos:0},{color:'#feb47b',pos:100}],
  ocean:  [{color:'#1e3c72',pos:0},{color:'#2a5298',pos:100}],
  candy:  [{color:'#fbc2eb',pos:0},{color:'#a6c1ee',pos:100}]
};
function grRender(){
  const wrap = document.getElementById('gr-stops');
  wrap.innerHTML = '';
  grStops.forEach((s,i) => {
    const row = document.createElement('div');
    row.className = 'gr-stop';
    row.innerHTML = `
      <input type="color" value="${s.color}" oninput="grStops[${i}].color = this.value; grRun()">
      <input type="range" min="0" max="100" value="${s.pos}" oninput="grStops[${i}].pos = +this.value; this.nextElementSibling.value = +this.value; grRun()">
      <input type="number" min="0" max="100" value="${s.pos}" oninput="grStops[${i}].pos = +this.value; this.previousElementSibling.value = +this.value; grRun()">
      <button onclick="grRemove(${i})" title="Remove">×</button>
    `;
    wrap.appendChild(row);
  });
}
function grAddStop(){
  const last = grStops[grStops.length-1].pos;
  grStops.push({color:'#ffffff', pos: Math.min(100, last+10)});
  grRender(); grRun();
}
function grRemove(i){
  if(grStops.length <= 2) return;
  grStops.splice(i,1);
  grRender(); grRun();
}
function grPreset(k){
  grStops = JSON.parse(JSON.stringify(GR_PRESETS[k]));
  grRender(); grRun();
}
function grAngleSync(){
  document.getElementById('gr-angle-val').textContent = document.getElementById('gr-angle').value + '°';
}
function grRun(){
  const type = document.getElementById('gr-type').value;
  document.getElementById('gr-angle-wrap').style.display = type === 'linear' ? '' : 'none';
  document.getElementById('gr-shape-wrap').style.display = type === 'radial' ? '' : 'none';
  const sorted = grStops.slice().sort((a,b) => a.pos - b.pos);
  const stopsCss = sorted.map(s => `${s.color} ${s.pos}%`).join(', ');
  let css;
  if(type === 'linear'){
    const a = document.getElementById('gr-angle').value;
    css = `linear-gradient(${a}deg, ${stopsCss})`;
  } else {
    const shape = document.getElementById('gr-shape').value;
    css = `radial-gradient(${shape} at center, ${stopsCss})`;
  }
  document.getElementById('gr-preview').style.background = css;
  document.getElementById('gr-css').textContent = `background: ${css};`;
}
document.addEventListener('DOMContentLoaded', () => { grRender(); grRun(); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>CSS gradients are a single line of CSS that draws smooth color transitions for backgrounds, buttons, hero panels, and overlays — without any image asset. The syntax is powerful but fiddly to write by hand: angles, percentage stops, repeating variants, mixing linear with radial. This tool gives you a visual builder that mirrors the CSS in real time, so you can drag a stop into place and copy the exact <code>linear-gradient(...)</code> or <code>radial-gradient(...)</code> string.</p>

<h3>When to use it</h3>
<ul>
  <li>Building a hero or call-to-action section background without burning into an image.</li>
  <li>Creating button or card hover states that look "modern" without an image asset.</li>
  <li>Mocking a brand-coloured overlay (gradient + low-opacity solid for text legibility).</li>
  <li>Generating decorative dividers, mesh-style backgrounds, or animated SVG fills.</li>
</ul>

<h3>Linear vs radial</h3>
<ul>
  <li><strong>Linear</strong> — colors transition along a straight line at a chosen angle (0° = bottom-to-top, 90° = left-to-right, 180° = top-to-bottom).</li>
  <li><strong>Radial</strong> — colors spread from a center point outward as a circle or ellipse. Great for spotlight or vignette effects.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Use as <code>background</code>, not <code>background-color</code>.</strong> Gradients are images, not colors. <code>background-color</code> is ignored.</li>
  <li><strong>Stops must be in order</strong> for predictable rendering. The tool sorts them automatically — if you copy CSS and edit by hand, keep the percentages monotonic.</li>
  <li><strong>Hard stops</strong> (two stops at the same percentage) make a sharp boundary instead of a fade — useful for striped or band effects.</li>
  <li><strong>Banding on big areas.</strong> Long, low-contrast gradients can show visible "bands" on 8-bit screens. Add a tiny SVG noise overlay (<code>filter: url(#noise)</code>) or move the stops slightly.</li>
  <li><strong>Performance.</strong> Browsers paint gradients quickly, but animating <code>background-image</code> triggers paint on every frame — animate <code>transform</code> on a layer above instead.</li>
  <li><strong>Accessibility.</strong> If text sits on a gradient, check the contrast ratio against the <em>worst</em> point along the gradient where the text appears, not the average.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "css-box-shadow"],
}
