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
        "pt": {"name": "Gerador de Gradiente CSS", "tagline": "Crie gradientes CSS lineares e radiais visualmente. Edite paradas de cor, copie CSS pronto para colar.", "description": "Gerador gratuito de gradiente CSS. Crie gradientes lineares ou radiais com quantas paradas quiser, copie CSS pronto para produção em um clique."},
        "pl": {"name": "Generator Gradientów CSS", "tagline": "Buduj liniowe i radialne gradienty CSS wizualnie. Edytuj color stopy, kopiuj CSS gotowy do wklejenia.", "description": "Darmowy generator gradientów CSS. Buduj linear lub radial gradienty z dowolną liczbą color stopów, dostosuj kąt i kształt, kopiuj produkcyjny CSS jednym kliknięciem."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>Gradientes CSS são uma única linha de CSS que desenha transições suaves de cor para fundos, botões, painéis hero e overlays — sem precisar de imagem. A sintaxe é poderosa mas trabalhosa de escrever na mão: ângulos, paradas em porcentagem, variantes repeating, misturar linear com radial. Esta ferramenta dá um construtor visual que espelha o CSS em tempo real, então você arrasta uma parada para o lugar e copia a string exata <code>linear-gradient(...)</code> ou <code>radial-gradient(...)</code>.</p>

<h3>Quando usar</h3>
<ul>
  <li>Criar fundo de uma seção hero ou call-to-action sem queimar numa imagem.</li>
  <li>Construir estados hover de botão ou card que pareçam "modernos" sem asset de imagem.</li>
  <li>Mockar um overlay com cor de marca (gradiente + sólido com baixa opacidade para legibilidade do texto).</li>
  <li>Gerar divisores decorativos, fundos estilo mesh ou preenchimentos SVG animados.</li>
</ul>

<h3>Linear vs radial</h3>
<ul>
  <li><strong>Linear</strong> — cores transitam ao longo de uma linha reta num ângulo escolhido (0° = de baixo para cima, 90° = da esquerda para direita, 180° = de cima para baixo).</li>
  <li><strong>Radial</strong> — cores se espalham de um ponto central para fora em forma de círculo ou elipse. Ótimo para efeitos de spotlight ou vinheta.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Use como <code>background</code>, não como <code>background-color</code>.</strong> Gradientes são imagens, não cores. <code>background-color</code> é ignorado.</li>
  <li><strong>Paradas precisam estar em ordem</strong> para renderização previsível. A ferramenta ordena automaticamente — se copiar o CSS e editar na mão, mantenha as porcentagens monotônicas.</li>
  <li><strong>Hard stops</strong> (duas paradas na mesma porcentagem) criam um limite nítido em vez de um fade — útil para efeitos de listras ou faixas.</li>
  <li><strong>Banding em áreas grandes.</strong> Gradientes longos e de baixo contraste podem mostrar "faixas" visíveis em telas de 8 bits. Adicione um overlay SVG sutil de noise (<code>filter: url(#noise)</code>) ou mova as paradas levemente.</li>
  <li><strong>Performance.</strong> Browsers pintam gradientes rápido, mas animar <code>background-image</code> dispara paint a cada frame — anime <code>transform</code> numa camada acima.</li>
  <li><strong>Acessibilidade.</strong> Se texto fica sobre um gradiente, verifique a razão de contraste no <em>pior</em> ponto do gradiente onde o texto aparece, não na média.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Gradienty CSS to jedna linia CSS, która rysuje płynne przejścia kolorów dla teł, przycisków, hero panelów i overlayów — bez żadnego pliku obrazu. Składnia jest potężna, ale upierdliwa do pisania ręcznie: kąty, color stopy w procentach, warianty repeating, mieszanie linear z radial. To narzędzie daje wizualny builder, który odzwierciedla CSS w czasie rzeczywistym, więc możesz przeciągnąć stop na miejsce i skopiować dokładny string <code>linear-gradient(...)</code> albo <code>radial-gradient(...)</code>.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Tło sekcji hero albo CTA bez wypalania w obrazek.</li>
  <li>Stany hover na przyciskach albo kartach, które wyglądają "nowocześnie" bez assetu graficznego.</li>
  <li>Mockowanie overlaya w kolorach marki (gradient + półprzezroczysty solid dla czytelności tekstu).</li>
  <li>Ozdobne dividery, tła w stylu mesh albo animowane wypełnienia SVG.</li>
</ul>

<h3>Linear vs radial</h3>
<ul>
  <li><strong>Linear</strong> — kolory przechodzą wzdłuż prostej linii pod wybranym kątem (0° = z dołu do góry, 90° = z lewej do prawej, 180° = z góry do dołu).</li>
  <li><strong>Radial</strong> — kolory rozchodzą się z punktu centralnego na zewnątrz w kształcie koła albo elipsy. Świetne do efektów spotlight albo winiety.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Używaj jako <code>background</code>, nie <code>background-color</code>.</strong> Gradienty są obrazami, nie kolorami. <code>background-color</code> jest ignorowane.</li>
  <li><strong>Stopy muszą być w kolejności</strong> dla przewidywalnego renderowania. Narzędzie sortuje je automatycznie — jeśli kopiujesz CSS i edytujesz ręcznie, trzymaj procenty monotoniczne.</li>
  <li><strong>Hard stops</strong> (dwa stopy w tym samym procencie) tworzą ostrą granicę zamiast przejścia — przydatne do efektów paskowych albo bandowych.</li>
  <li><strong>Banding na dużych powierzchniach.</strong> Długie, niskokontrastowe gradienty mogą pokazywać widoczne "pasy" na 8-bitowych ekranach. Dodaj subtelny overlay SVG noise (<code>filter: url(#noise)</code>) albo lekko przesuń stopy.</li>
  <li><strong>Wydajność.</strong> Przeglądarki malują gradienty szybko, ale animowanie <code>background-image</code> wywołuje paint co klatkę — animuj <code>transform</code> na warstwie nad, zamiast tego.</li>
  <li><strong>Dostępność.</strong> Jeśli tekst leży na gradiencie, sprawdź współczynnik kontrastu w <em>najgorszym</em> punkcie gradientu, gdzie tekst się pojawia, nie średnią.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "css-box-shadow"],
}
