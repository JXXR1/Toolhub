TOOL = {
    "slug": "color-picker",
    "category": "design",
    "icon": "🎨",
    "tags": ["color", "picker", "hex", "rgb", "hsl", "hsv", "cmyk", "palette"],
    "i18n": {
        "en": {
            "name": "Color Picker",
            "tagline": "Pick a color and instantly see it in HEX, RGB, RGBA, HSL, HSLA, HSV, and CMYK. Adjust opacity and copy any value.",
            "description": "Free online color picker. Convert between HEX, RGB(A), HSL(A), HSV, and CMYK with live preview, opacity slider, and copy buttons.",
        },
        "de": {"name": "Farbwähler", "tagline": "Farbe wählen und sofort als HEX, RGB, RGBA, HSL, HSLA, HSV und CMYK sehen. Deckkraft anpassen und kopieren.", "description": "Kostenloser Farbwähler online. HEX, RGB(A), HSL(A), HSV und CMYK mit Live-Vorschau und Deckkraft-Regler."},
        "es": {"name": "Selector de Color", "tagline": "Elige un color y míralo en HEX, RGB, RGBA, HSL, HSLA, HSV y CMYK. Ajusta la opacidad y copia.", "description": "Selector de color en línea gratuito. HEX, RGB(A), HSL(A), HSV y CMYK con vista previa y opacidad."},
        "fr": {"name": "Sélecteur de Couleur", "tagline": "Choisissez une couleur et voyez-la en HEX, RGB, RGBA, HSL, HSLA, HSV et CMJN. Ajustez l'opacité et copiez.", "description": "Sélecteur de couleur en ligne gratuit. HEX, RGB(A), HSL(A), HSV et CMJN avec aperçu et curseur d'opacité."},
        "it": {"name": "Selettore Colore", "tagline": "Scegli un colore e vedilo in HEX, RGB, RGBA, HSL, HSLA, HSV e CMYK. Regola l'opacità e copia.", "description": "Selettore colore online gratuito. HEX, RGB(A), HSL(A), HSV e CMYK con anteprima live e cursore opacità."},
    },
    "body": """
<div class="tool-card">
  <div class="cp-grid">
    <div class="cp-swatch" id="cp-swatch"></div>
    <div class="cp-controls">
      <label>Pick a color</label>
      <input type="color" id="cp-input" value="#3b82f6" oninput="cpRun()">
      <label style="margin-top:0.8rem">Opacity: <span id="cp-alpha-display">100%</span></label>
      <input type="range" id="cp-alpha" min="0" max="100" value="100" oninput="cpRun()">
      <label style="margin-top:0.8rem">Or paste any value</label>
      <input type="text" id="cp-paste" placeholder="#ff8800 · rgb(255,136,0) · hsl(32 100% 50%)" oninput="cpFromText()">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="cp-out" class="cp-vals"></div>
</div>
""",
    "script": """
<style>
.cp-grid{display:grid;grid-template-columns:160px 1fr;gap:1rem;align-items:start}
.cp-swatch{height:160px;border-radius:10px;border:1px solid var(--border);background:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%,#ccc),linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%,#ccc);background-size:20px 20px;background-position:0 0,10px 10px;position:relative;overflow:hidden}
.cp-swatch::after{content:'';position:absolute;inset:0;background:var(--cp-color,#3b82f6)}
.cp-controls input[type=color]{width:100%;height:48px;border:1px solid var(--border);border-radius:8px;background:var(--bg-elev);cursor:pointer;padding:0.2rem}
.cp-vals{display:grid;gap:0.5rem}
.cp-row{display:grid;grid-template-columns:80px 1fr auto;gap:0.6rem;align-items:center;padding:0.5rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-family:ui-monospace,monospace;font-size:0.88rem}
.cp-row .lbl{color:var(--text-muted);font-size:0.78rem}
.cp-row button{padding:0.3rem 0.65rem;font-size:0.78rem}
@media(max-width:600px){.cp-grid{grid-template-columns:1fr}.cp-swatch{height:100px}.cp-row{grid-template-columns:1fr;gap:0.25rem}.cp-row button{justify-self:start}}
</style>
<script>
function cpHexToRgb(h){h=h.replace('#','');if(h.length===3)h=h.split('').map(c=>c+c).join('');return{r:parseInt(h.slice(0,2),16),g:parseInt(h.slice(2,4),16),b:parseInt(h.slice(4,6),16)}}
function cpRgbToHex(r,g,b){return '#'+[r,g,b].map(x=>x.toString(16).padStart(2,'0')).join('').toUpperCase()}
function cpRgbToHsl(r,g,b){r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);let h=0,s=0,l=(mx+mn)/2;if(mx!==mn){const d=mx-mn;s=l>0.5?d/(2-mx-mn):d/(mx+mn);if(mx===r)h=(g-b)/d+(g<b?6:0);else if(mx===g)h=(b-r)/d+2;else h=(r-g)/d+4;h*=60}return{h:Math.round(h),s:Math.round(s*100),l:Math.round(l*100)}}
function cpRgbToHsv(r,g,b){r/=255;g/=255;b/=255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b),d=mx-mn;let h=0;const s=mx===0?0:d/mx,v=mx;if(d!==0){if(mx===r)h=(g-b)/d+(g<b?6:0);else if(mx===g)h=(b-r)/d+2;else h=(r-g)/d+4;h*=60}return{h:Math.round(h),s:Math.round(s*100),v:Math.round(v*100)}}
function cpRgbToCmyk(r,g,b){const R=r/255,G=g/255,B=b/255;const K=1-Math.max(R,G,B);if(K===1)return{c:0,m:0,y:0,k:100};const C=(1-R-K)/(1-K),M=(1-G-K)/(1-K),Y=(1-B-K)/(1-K);return{c:Math.round(C*100),m:Math.round(M*100),y:Math.round(Y*100),k:Math.round(K*100)}}
function cpParse(text){
  text = text.trim();
  if(!text) return null;
  if(text[0]==='#' || /^[0-9a-f]{3}([0-9a-f]{3})?$/i.test(text)) {
    const h = text[0]==='#'?text:'#'+text;
    if(/^#[0-9a-f]{3}([0-9a-f]{3})?$/i.test(h)) return {...cpHexToRgb(h), a:1};
  }
  let m = text.match(/rgba?\\(\\s*(\\d+)[\\s,]+(\\d+)[\\s,]+(\\d+)(?:[\\s,/]+([\\d.]+%?))?\\s*\\)/i);
  if(m){const a=m[4]?(m[4].endsWith('%')?parseFloat(m[4])/100:parseFloat(m[4])):1;return{r:+m[1],g:+m[2],b:+m[3],a}}
  m = text.match(/hsla?\\(\\s*(\\d+(?:\\.\\d+)?)(?:deg)?[\\s,]+(\\d+(?:\\.\\d+)?)%?[\\s,]+(\\d+(?:\\.\\d+)?)%?(?:[\\s,/]+([\\d.]+%?))?\\s*\\)/i);
  if(m){const a=m[4]?(m[4].endsWith('%')?parseFloat(m[4])/100:parseFloat(m[4])):1;const rgb=cpHslToRgb(+m[1],+m[2],+m[3]);return{...rgb,a}}
  return null;
}
function cpHslToRgb(h,s,l){s/=100;l/=100;const c=(1-Math.abs(2*l-1))*s,x=c*(1-Math.abs((h/60)%2-1)),m=l-c/2;let r=0,g=0,b=0;if(h<60){r=c;g=x}else if(h<120){r=x;g=c}else if(h<180){g=c;b=x}else if(h<240){g=x;b=c}else if(h<300){r=x;b=c}else{r=c;b=x}return{r:Math.round((r+m)*255),g:Math.round((g+m)*255),b:Math.round((b+m)*255)}}
function cpRow(label, value){return `<div class="cp-row"><div class="lbl">${label}</div><div>${value}</div><button class="secondary" onclick="cpCopy(this,'${value.replace(/'/g,"\\\\'")}')">{LBL_COPY}</button></div>`}
function cpCopy(btn,text){navigator.clipboard.writeText(text);const old=btn.textContent;btn.textContent='✓';setTimeout(()=>btn.textContent=old,900)}
function cpRun(){
  const hex = document.getElementById('cp-input').value;
  const a = parseInt(document.getElementById('cp-alpha').value,10)/100;
  document.getElementById('cp-alpha-display').textContent = Math.round(a*100)+'%';
  const {r,g,b} = cpHexToRgb(hex);
  cpRender(r,g,b,a);
}
function cpFromText(){
  const t = document.getElementById('cp-paste').value;
  const c = cpParse(t);
  if(!c) return;
  document.getElementById('cp-input').value = cpRgbToHex(c.r,c.g,c.b);
  document.getElementById('cp-alpha').value = Math.round((c.a||1)*100);
  document.getElementById('cp-alpha-display').textContent = Math.round((c.a||1)*100)+'%';
  cpRender(c.r,c.g,c.b,c.a||1);
}
function cpRender(r,g,b,a){
  const sw = document.getElementById('cp-swatch');
  sw.style.setProperty('--cp-color', `rgba(${r},${g},${b},${a})`);
  const hsl = cpRgbToHsl(r,g,b);
  const hsv = cpRgbToHsv(r,g,b);
  const cmyk = cpRgbToCmyk(r,g,b);
  const out = [
    cpRow('HEX',  cpRgbToHex(r,g,b)),
    cpRow('HEX8', cpRgbToHex(r,g,b)+Math.round(a*255).toString(16).padStart(2,'0').toUpperCase()),
    cpRow('RGB',  `rgb(${r}, ${g}, ${b})`),
    cpRow('RGBA', `rgba(${r}, ${g}, ${b}, ${a.toFixed(2)})`),
    cpRow('HSL',  `hsl(${hsl.h}, ${hsl.s}%, ${hsl.l}%)`),
    cpRow('HSLA', `hsla(${hsl.h}, ${hsl.s}%, ${hsl.l}%, ${a.toFixed(2)})`),
    cpRow('HSV',  `hsv(${hsv.h}, ${hsv.s}%, ${hsv.v}%)`),
    cpRow('CMYK', `cmyk(${cmyk.c}%, ${cmyk.m}%, ${cmyk.y}%, ${cmyk.k}%)`),
  ].join('');
  document.getElementById('cp-out').innerHTML = out;
}
document.addEventListener('DOMContentLoaded', cpRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Pick a colour — or paste any HEX / <code>rgb()</code> / <code>hsl()</code> value — and instantly see it in every common notation: HEX (3- and 8-digit with alpha), RGB(A), HSL(A), HSV, and CMYK. Useful when you've got a value in one space and need it in another, when matching a brand colour across CSS / design tools / print, or when adjusting opacity without re-eyeballing the result.</p>

<h3>When to use each space</h3>
<ul>
  <li><strong>HEX / RGB</strong> — CSS, design tools, email templates. Universally supported.</li>
  <li><strong>HSL</strong> — readable palettes. Tweak hue, saturation, or lightness independently without the colour drifting on the other axes.</li>
  <li><strong>HSV</strong> — design software (Photoshop, Figma) for shading; matches the way most colour pickers think about "this colour, lighter".</li>
  <li><strong>CMYK</strong> — print-ready output. Approximate only: screens are RGB and printers don't all share one colour profile.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Alpha encoding differs by space.</strong> CSS supports <code>rgba()</code>, <code>hsla()</code>, and 8-digit HEX (<code>#RRGGBBAA</code>). Older email templates and some design tools don't grok <code>#RRGGBBAA</code> — fall back to <code>rgba()</code>.</li>
  <li><strong>HSL hue is in degrees.</strong> 0 = red, 120 = green, 240 = blue. CSS accepts <code>turn</code>, <code>rad</code>, <code>grad</code> too but the output here is degrees.</li>
  <li><strong>CMYK conversion is naive.</strong> Real print needs an ICC profile (sRGB → CMYK with rendering intent). This tool's output is fine for brand-deck mockups, not for press-ready files.</li>
  <li><strong>OKLCH and OKLAB</strong> (modern perceptually-uniform spaces) aren't shown here — they're newer and not yet broadly supported. Stick to HSL/HSV for design system tooling for now.</li>
</ul>
""",
    },
    "related": ["css-minifier", "image-to-base64", "qr-code-generator"],
}
