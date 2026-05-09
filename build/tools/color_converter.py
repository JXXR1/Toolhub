TOOL = {
    "slug": "color-converter",
    "category": "design",
    "icon": "🎨",
    "tags": ["color", "hex", "rgb", "hsl", "oklch", "convert", "css"],
    "i18n": {
        "en": {
            "name": "Color Converter",
            "tagline": "Convert any color between hex, RGB, HSL, and OKLCH. Live preview, copy in one click.",
            "description": "Free online color converter. Translate between hex (#3498db), rgb(), hsl(), and the modern oklch() format. Live swatch preview, copy any value in one click.",
        },
        "de": {"name": "Farbkonverter", "tagline": "Konvertiere Farben zwischen Hex, RGB, HSL und OKLCH. Live-Vorschau, mit einem Klick kopieren.", "description": "Kostenloser Online-Farbkonverter. Übersetze zwischen Hex, rgb(), hsl() und dem modernen oklch()-Format. Live-Vorschau, mit einem Klick kopieren."},
        "es": {"name": "Conversor de Color", "tagline": "Convierte cualquier color entre hex, RGB, HSL y OKLCH. Vista previa en vivo, copiar con un clic.", "description": "Conversor de colores gratuito en línea. Convierte entre hex, rgb(), hsl() y el moderno formato oklch(). Vista previa en vivo, copiar con un clic."},
        "fr": {"name": "Convertisseur de Couleur", "tagline": "Convertissez toute couleur entre hex, RGB, HSL et OKLCH. Aperçu en direct, copier en un clic.", "description": "Convertisseur de couleur gratuit en ligne. Conversion entre hex, rgb(), hsl() et le format moderne oklch(). Aperçu en direct, copie en un clic."},
        "it": {"name": "Convertitore di Colori", "tagline": "Converti qualsiasi colore tra hex, RGB, HSL e OKLCH. Anteprima live, copia con un clic.", "description": "Convertitore di colori gratuito online. Conversione tra hex, rgb(), hsl() e il moderno formato oklch(). Anteprima live, copia con un clic."},
    },
    "body": """
<div class="tool-card">
  <div class="cc-grid">
    <div>
      <label>Hex</label>
      <input type="text" id="cc-hex" oninput="ccFromHex()" placeholder="#3498db" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>RGB</label>
      <input type="text" id="cc-rgb" oninput="ccFromRgb()" placeholder="rgb(52, 152, 219)" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>HSL</label>
      <input type="text" id="cc-hsl" oninput="ccFromHsl()" placeholder="hsl(204, 70%, 53%)" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>OKLCH</label>
      <input type="text" id="cc-oklch" oninput="ccFromOklch()" placeholder="oklch(0.65 0.13 240)" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>Picker</label>
      <input type="color" id="cc-pick" oninput="ccFromPicker()" value="#3498db" style="width:100%;height:42px;padding:2px">
    </div>
    <div>
      <label>{LBL_RESULT}</label>
      <div id="cc-swatch" class="cc-swatch"></div>
    </div>
  </div>
  <div class="meta" id="cc-meta" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<style>
.cc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0.7rem}
.cc-swatch{height:42px;border:1px solid var(--border);border-radius:8px;background:#3498db}
</style>
<script>
function ccClamp(n,lo,hi){return Math.min(hi,Math.max(lo,n))}
function ccHexToRgb(h){
  h = h.trim().replace(/^#/,'');
  if(h.length===3) h = h.split('').map(c=>c+c).join('');
  if(!/^[0-9a-fA-F]{6}$/.test(h)) return null;
  return [parseInt(h.slice(0,2),16), parseInt(h.slice(2,4),16), parseInt(h.slice(4,6),16)];
}
function ccRgbToHex(r,g,b){
  const h = n => ccClamp(Math.round(n),0,255).toString(16).padStart(2,'0');
  return '#' + h(r) + h(g) + h(b);
}
function ccRgbToHsl(r,g,b){
  r/=255; g/=255; b/=255;
  const mx = Math.max(r,g,b), mn = Math.min(r,g,b), d = mx-mn;
  let h=0, s=0, l=(mx+mn)/2;
  if(d){
    s = d / (1 - Math.abs(2*l - 1));
    switch(mx){
      case r: h = ((g-b)/d) % 6; break;
      case g: h = (b-r)/d + 2; break;
      default: h = (r-g)/d + 4;
    }
    h *= 60; if(h<0) h += 360;
  }
  return [h, s*100, l*100];
}
function ccHslToRgb(h,s,l){
  h = ((h%360)+360)%360; s/=100; l/=100;
  const c = (1 - Math.abs(2*l - 1)) * s;
  const x = c * (1 - Math.abs(((h/60) % 2) - 1));
  const m = l - c/2;
  let r=0,g=0,b=0;
  if(h<60){r=c;g=x} else if(h<120){r=x;g=c} else if(h<180){g=c;b=x} else if(h<240){g=x;b=c} else if(h<300){r=x;b=c} else {r=c;b=x}
  return [(r+m)*255, (g+m)*255, (b+m)*255];
}
// sRGB <-> linear
function ccSrgbToLinear(c){c/=255; return c <= 0.04045 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4)}
function ccLinearToSrgb(c){const v = c <= 0.0031308 ? c*12.92 : 1.055*Math.pow(c, 1/2.4) - 0.055; return ccClamp(Math.round(v*255),0,255)}
// linear sRGB -> Oklab (per Björn Ottosson)
function ccLinearToOklab(r,g,b){
  const l = 0.4122214708*r + 0.5363325363*g + 0.0514459929*b;
  const m = 0.2119034982*r + 0.6806995451*g + 0.1073969566*b;
  const s = 0.0883024619*r + 0.2817188376*g + 0.6299787005*b;
  const l_ = Math.cbrt(l), m_ = Math.cbrt(m), s_ = Math.cbrt(s);
  return [
    0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_,
    1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_,
    0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_
  ];
}
function ccOklabToLinear(L,a,b){
  const l_ = L + 0.3963377774*a + 0.2158037573*b;
  const m_ = L - 0.1055613458*a - 0.0638541728*b;
  const s_ = L - 0.0894841775*a - 1.2914855480*b;
  const l = l_*l_*l_, m = m_*m_*m_, s = s_*s_*s_;
  return [
    +4.0767416621*l - 3.3077115913*m + 0.2309699292*s,
    -1.2684380046*l + 2.6097574011*m - 0.3413193965*s,
    -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
  ];
}
function ccRgbToOklch(r,g,b){
  const [lr,lg,lb] = [ccSrgbToLinear(r), ccSrgbToLinear(g), ccSrgbToLinear(b)];
  const [L,a,bb] = ccLinearToOklab(lr,lg,lb);
  const C = Math.hypot(a,bb);
  let h = Math.atan2(bb,a) * 180 / Math.PI; if(h<0) h += 360;
  return [L, C, h];
}
function ccOklchToRgb(L,C,h){
  const a = C * Math.cos(h*Math.PI/180);
  const b = C * Math.sin(h*Math.PI/180);
  const [lr,lg,lb] = ccOklabToLinear(L,a,b);
  return [ccLinearToSrgb(lr), ccLinearToSrgb(lg), ccLinearToSrgb(lb)];
}
let ccCurrent = [52,152,219];
function ccUpdate(rgb, except){
  ccCurrent = rgb;
  const [r,g,b] = rgb;
  const hex = ccRgbToHex(r,g,b);
  const [hh,sl,ll] = ccRgbToHsl(r,g,b);
  const [oL,oC,oH] = ccRgbToOklch(r,g,b);
  if(except!=='hex')  document.getElementById('cc-hex').value = hex;
  if(except!=='rgb')  document.getElementById('cc-rgb').value = `rgb(${Math.round(r)}, ${Math.round(g)}, ${Math.round(b)})`;
  if(except!=='hsl')  document.getElementById('cc-hsl').value = `hsl(${hh.toFixed(0)}, ${sl.toFixed(0)}%, ${ll.toFixed(0)}%)`;
  if(except!=='oklch') document.getElementById('cc-oklch').value = `oklch(${oL.toFixed(3)} ${oC.toFixed(3)} ${oH.toFixed(1)})`;
  if(except!=='pick') document.getElementById('cc-pick').value = hex;
  document.getElementById('cc-swatch').style.background = hex;
  document.getElementById('cc-meta').textContent =
    `Click any field to edit · sRGB ${Math.round(r)},${Math.round(g)},${Math.round(b)} · perceptual L=${oL.toFixed(2)}`;
}
function ccFromHex(){
  const v = document.getElementById('cc-hex').value;
  const rgb = ccHexToRgb(v); if(rgb) ccUpdate(rgb, 'hex');
}
function ccFromRgb(){
  const m = document.getElementById('cc-rgb').value.match(/(\\d+(?:\\.\\d+)?)\\s*,\\s*(\\d+(?:\\.\\d+)?)\\s*,\\s*(\\d+(?:\\.\\d+)?)/);
  if(m) ccUpdate([+m[1],+m[2],+m[3]], 'rgb');
}
function ccFromHsl(){
  const m = document.getElementById('cc-hsl').value.match(/(-?\\d+(?:\\.\\d+)?)\\s*,?\\s*(\\d+(?:\\.\\d+)?)\\s*%?\\s*,?\\s*(\\d+(?:\\.\\d+)?)\\s*%?/);
  if(m) ccUpdate(ccHslToRgb(+m[1],+m[2],+m[3]), 'hsl');
}
function ccFromOklch(){
  const m = document.getElementById('cc-oklch').value.match(/(\\d*\\.?\\d+)%?\\s+(\\d*\\.?\\d+)\\s+(-?\\d*\\.?\\d+)/);
  if(m){
    let L = +m[1]; if(m[1].includes('.')===false && L > 1) L /= 100; // accept 65 as 0.65
    if(L > 1) L /= 100;
    ccUpdate(ccOklchToRgb(L, +m[2], +m[3]), 'oklch');
  }
}
function ccFromPicker(){
  const rgb = ccHexToRgb(document.getElementById('cc-pick').value);
  if(rgb) ccUpdate(rgb, 'pick');
}
document.addEventListener('DOMContentLoaded', () => ccUpdate([52,152,219]));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Designers and front-end developers shuffle colors between formats constantly — Figma gives you hex, the design tokens spec wants OKLCH, your CSS uses HSL, and the image you grabbed is in RGB. This tool keeps every notation in sync: edit one, the others update live. Includes the modern <code>oklch()</code> format added in CSS Color Module 4 (and supported in all major browsers since 2023), which produces perceptually uniform colors that are far easier to reason about than HSL.</p>

<h3>When to use it</h3>
<ul>
  <li>Translating a brand hex code into <code>rgb()</code> with alpha for a CSS overlay.</li>
  <li>Converting between HSL and OKLCH while migrating a design system to perceptual color.</li>
  <li>Reading a pasted <code>rgb(52, 152, 219)</code> from a screenshot tool back into a hex code for your stylesheet.</li>
  <li>Sanity-checking an OKLCH chroma value (anything above ~0.4 is likely outside the sRGB gamut).</li>
</ul>

<h3>Format quick reference</h3>
<ul>
  <li><strong>Hex</strong> — <code>#RRGGBB</code> (or 3-digit shorthand <code>#RGB</code>). Universal, no alpha unless 8-digit (<code>#RRGGBBAA</code>).</li>
  <li><strong>RGB</strong> — <code>rgb(0–255, 0–255, 0–255)</code>. The actual sRGB channel values your screen receives.</li>
  <li><strong>HSL</strong> — hue (0–360°), saturation (0–100%), lightness (0–100%). Easy to reason about colour families, but lightness is non-perceptual: HSL 50% green looks brighter than HSL 50% blue.</li>
  <li><strong>OKLCH</strong> — perceptual lightness (0–1), chroma (0–~0.4 in sRGB), hue (0–360°). Two colours with the same L look equally bright; ideal for design systems and accessibility.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>OKLCH lightness uses 0–1, not 0–100.</strong> CSS accepts both (<code>0.65</code> or <code>65%</code>); this tool accepts either form.</li>
  <li><strong>Some OKLCH values fall outside sRGB</strong> (e.g. high chroma for blue). The tool clamps to displayable sRGB on conversion — the result is approximate, not exact.</li>
  <li><strong>HSL is not the same as HSV.</strong> HSV's "value" is the brightest channel; HSL's "lightness" is the midpoint of the brightest and darkest. They give different numbers for the same colour.</li>
  <li><strong>Round-tripping isn't always lossless.</strong> hex → hsl → hex can shift a single integer due to rounding. For exact reproduction, store hex.</li>
  <li><strong>Hex and RGB are sRGB by default,</strong> not Display P3 or Rec. 2020. If your design tool is in a wide-gamut profile, the same hex looks different.</li>
</ul>
""",
    },
    "related": ["color-picker", "wcag-contrast", "css-gradient"],
}
