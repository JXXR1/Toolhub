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
        "pt": {"name": "Conversor de Cores", "tagline": "Converta qualquer cor entre hex, RGB, HSL e OKLCH. Preview ao vivo, copie com um clique.", "description": "Conversor de cores online gratuito. Traduza entre hex (#3498db), rgb(), hsl() e o formato moderno oklch(). Preview de amostra ao vivo, copie qualquer valor com um clique."},
        "pl": {"name": "Konwerter Kolorów", "tagline": "Konwertuj dowolny kolor między hex, RGB, HSL i OKLCH. Podgląd na żywo, kopia jednym kliknięciem.", "description": "Darmowy online konwerter kolorów. Tłumacz między hex (#3498db), rgb(), hsl() i nowoczesnym formatem oklch(). Podgląd próbki na żywo, kopiuj dowolną wartość jednym kliknięciem."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>Designers e desenvolvedores front-end ficam o tempo todo movendo cores entre formatos — o Figma te dá hex, a spec de design tokens quer OKLCH, seu CSS usa HSL, e a imagem que você capturou está em RGB. Esta ferramenta mantém todas as notações sincronizadas: edite uma, as outras atualizam ao vivo. Inclui o formato moderno <code>oklch()</code> adicionado no CSS Color Module 4 (e suportado em todos os navegadores principais desde 2023), que produz cores perceptualmente uniformes muito mais fáceis de raciocinar do que HSL.</p>

<h3>Quando usar</h3>
<ul>
  <li>Traduzir um código hex de marca para <code>rgb()</code> com alpha para um overlay CSS.</li>
  <li>Converter entre HSL e OKLCH ao migrar um design system para cor perceptual.</li>
  <li>Ler um <code>rgb(52, 152, 219)</code> colado de uma ferramenta de captura de tela de volta para um hex no seu stylesheet.</li>
  <li>Conferir um valor de chroma OKLCH (qualquer coisa acima de ~0,4 provavelmente está fora do gamut sRGB).</li>
</ul>

<h3>Referência rápida dos formatos</h3>
<ul>
  <li><strong>Hex</strong> — <code>#RRGGBB</code> (ou shorthand de 3 dígitos <code>#RGB</code>). Universal, sem alpha a menos que use 8 dígitos (<code>#RRGGBBAA</code>).</li>
  <li><strong>RGB</strong> — <code>rgb(0–255, 0–255, 0–255)</code>. Os valores reais de canal sRGB que sua tela recebe.</li>
  <li><strong>HSL</strong> — hue/matiz (0–360°), saturação (0–100%), lightness/luminosidade (0–100%). Fácil para raciocinar sobre famílias de cor, mas a lightness não é perceptual: verde com HSL 50% parece mais brilhante que azul com HSL 50%.</li>
  <li><strong>OKLCH</strong> — lightness perceptual (0–1), chroma (0–~0,4 em sRGB), hue (0–360°). Duas cores com o mesmo L parecem igualmente brilhantes; ideal para design systems e acessibilidade.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>A lightness do OKLCH usa 0–1, não 0–100.</strong> O CSS aceita ambos (<code>0.65</code> ou <code>65%</code>); esta ferramenta aceita as duas formas.</li>
  <li><strong>Alguns valores OKLCH ficam fora do sRGB</strong> (ex.: chroma alto para azul). A ferramenta faz clamp para sRGB exibível na conversão — o resultado é aproximado, não exato.</li>
  <li><strong>HSL não é o mesmo que HSV.</strong> O "value" do HSV é o canal mais brilhante; a "lightness" do HSL é o ponto médio entre o mais brilhante e o mais escuro. Eles dão números diferentes para a mesma cor.</li>
  <li><strong>Round-trip nem sempre é sem perdas.</strong> hex → hsl → hex pode mudar um único inteiro por causa do arredondamento. Para reprodução exata, armazene hex.</li>
  <li><strong>Hex e RGB são sRGB por padrão,</strong> não Display P3 nem Rec. 2020. Se sua ferramenta de design está num perfil de gamut amplo, o mesmo hex aparece diferente.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Designerzy i frontendowcy non-stop przerzucają kolory między formatami — Figma daje hex, spec design tokenów chce OKLCH, twój CSS używa HSL, a obrazek, który złapałeś, jest w RGB. To narzędzie utrzymuje wszystkie notacje w synchronizacji: edytuj jedną, reszta aktualizuje się na żywo. Zawiera nowoczesny format <code>oklch()</code> dodany w CSS Color Module 4 (i wspierany we wszystkich głównych przeglądarkach od 2023), który produkuje percepcyjnie jednolite kolory, znacznie łatwiejsze do zrozumienia niż HSL.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Tłumaczenie hexa marki na <code>rgb()</code> z alphą do CSS-owego overlaya.</li>
  <li>Konwersja między HSL a OKLCH przy migracji design systemu na percepcyjny model koloru.</li>
  <li>Czytanie wklejonego <code>rgb(52, 152, 219)</code> z narzędzia do screenshotów z powrotem na hex do stylesheeta.</li>
  <li>Sanity check wartości chromy OKLCH (cokolwiek powyżej ~0,4 prawdopodobnie wypada poza gamut sRGB).</li>
</ul>

<h3>Szybka ściąga formatów</h3>
<ul>
  <li><strong>Hex</strong> — <code>#RRGGBB</code> (albo skrót 3-cyfrowy <code>#RGB</code>). Uniwersalny, bez alphy chyba że 8-cyfrowy (<code>#RRGGBBAA</code>).</li>
  <li><strong>RGB</strong> — <code>rgb(0–255, 0–255, 0–255)</code>. Faktyczne wartości kanałów sRGB, które dostaje twój ekran.</li>
  <li><strong>HSL</strong> — hue (0–360°), saturation (0–100%), lightness (0–100%). Łatwy do myślenia o rodzinach kolorów, ale lightness nie jest percepcyjny: HSL 50% zielony wygląda jaśniej niż HSL 50% niebieski.</li>
  <li><strong>OKLCH</strong> — percepcyjna lightness (0–1), chroma (0–~0,4 w sRGB), hue (0–360°). Dwa kolory z tą samą L wyglądają tak samo jasno; idealne do design systemów i dostępności.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Lightness w OKLCH używa 0–1, nie 0–100.</strong> CSS akceptuje obie formy (<code>0.65</code> albo <code>65%</code>); to narzędzie też.</li>
  <li><strong>Niektóre wartości OKLCH wypadają poza sRGB</strong> (np. wysoka chroma dla niebieskiego). Narzędzie clampuje do wyświetlalnego sRGB przy konwersji — wynik jest przybliżony, nie dokładny.</li>
  <li><strong>HSL to nie to samo co HSV.</strong> "Value" w HSV to najjaśniejszy kanał; "lightness" w HSL to środek między najjaśniejszym a najciemniejszym. Dają różne liczby dla tego samego koloru.</li>
  <li><strong>Round-trip nie zawsze jest bezstratny.</strong> hex → hsl → hex może przesunąć jeden integer przez zaokrąglenie. Dla dokładnej reprodukcji trzymaj hex.</li>
  <li><strong>Hex i RGB są domyślnie w sRGB,</strong> nie Display P3 ani Rec. 2020. Jeśli twoje narzędzie projektowe jest w profilu wide-gamut, ten sam hex wygląda inaczej.</li>
</ul>
""",
    },
    "related": ["color-picker", "wcag-contrast", "css-gradient"],
}
