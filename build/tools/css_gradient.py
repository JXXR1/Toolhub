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
        "ja": {"name": "CSS グラデーションジェネレーター", "tagline": "線形・放射状の CSS グラデーションをビジュアルに作成。カラーストップを編集して、貼り付けるだけの CSS をコピー。", "description": "無料の CSS グラデーションジェネレーター。任意の数のカラーストップで線形・放射状グラデーションを作成し、角度と形状を調整して、本番投入できる CSS をワンクリックでコピーできます。"},
        "nl": {"name": "CSS Gradient Generator", "tagline": "Bouw visueel lineaire en radiale CSS-gradients. Bewerk color stops, kopieer ready-to-paste CSS.", "description": "Gratis CSS gradient generator. Bouw lineaire of radiale gradients met zoveel color stops als je wilt, stel hoek en vorm in, kopieer production-ready CSS in één klik."},
        "tr": {"name": "CSS Gradient Oluşturucu", "tagline": "Lineer ve radial CSS gradient'larını görsel olarak kur. Renk durak noktalarını düzenle, yapıştırılmaya hazır CSS'i kopyala.", "description": "Ücretsiz CSS gradient oluşturucu. İstediğin kadar renk durak noktasıyla lineer veya radial gradient kur, açıyı ve şekli ayarla, üretime hazır CSS'i tek tıkla kopyala."},
        "id": {"name": "Pembangun CSS Gradient", "tagline": "Susun gradient linear dan radial CSS secara visual. Edit color stop, salin CSS siap-tempel.", "description": "Pembangun CSS gradient gratis. Buat gradient linear dan radial dengan stop warna yang dapat di-drag, kontrol sudut, dan pratinjau langsung. Salin CSS siap-tempel."},
        "vi": {"name": "CSS Gradient Builder", "tagline": "Soạn gradient linear và radial CSS một cách trực quan. Chỉnh sửa color stop, sao chép CSS sẵn-dùng.", "description": "Trình xây dựng CSS gradient miễn phí trực tuyến. Soạn linear hoặc radial gradient với nhiều color stop, sau đó sao chép CSS sẵn-dùng."},
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
    <button class="secondary" onclick="grAddStop()">+ {LBL_ADD}</button>
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
      <button onclick="grRemove(${i})" title="{LBL_REMOVE}" aria-label="{LBL_REMOVE}">×</button>
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
        "ja": """
<h2>用途</h2>
<p>CSS グラデーションは、画像アセットを使わずに背景・ボタン・ヒーローパネル・オーバーレイで滑らかな色の変化を描ける 1 行の CSS です。構文は強力ですが手書きには面倒で、角度、% でのストップ、繰り返しバリアント、線形と放射状の混在などを扱う必要があります。本ツールはビジュアルなビルダーで、CSS をリアルタイムにミラー表示します。ストップを所定位置にドラッグして、正確な <code>linear-gradient(...)</code> や <code>radial-gradient(...)</code> 文字列をコピーできます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ヒーローや CTA セクションの背景を、画像に焼き込まずに作りたいとき。</li>
  <li>ボタンやカードのホバーステートを「モダン」に見せつつ、画像アセットなしで作りたいとき。</li>
  <li>ブランドカラーのオーバーレイ（テキスト可読性のためにグラデーション + 低不透明度ベタ）を作るとき。</li>
  <li>装飾的なディバイダ、メッシュ風背景、アニメーション付き SVG 塗りを生成したいとき。</li>
</ul>

<h3>線形と放射状</h3>
<ul>
  <li><strong>線形（linear）</strong> — 指定した角度の直線に沿って色が遷移します（0° = 下から上、90° = 左から右、180° = 上から下）。</li>
  <li><strong>放射状（radial）</strong> — 中心点から円または楕円形に外側へ広がります。スポットライトやビネット効果に最適です。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong><code>background-color</code> ではなく <code>background</code> として使用してください。</strong> グラデーションは色ではなく画像です。<code>background-color</code> は無視されます。</li>
  <li><strong>ストップは順序通りに</strong>。予測可能な描画のため、本ツールは自動でソートしますが、CSS をコピー後に手で編集する場合は %値を単調に保ってください。</li>
  <li><strong>ハードストップ</strong>（同じ % に 2 つのストップ）は、フェードではなく境界線になります。ストライプやバンド効果に便利です。</li>
  <li><strong>大面積でのバンディング。</strong> 長くて低コントラストなグラデーションは、8-bit ディスプレイで段差が見えることがあります。微小な SVG ノイズオーバーレイ（<code>filter: url(#noise)</code>）を重ねるか、ストップを少しずらしてください。</li>
  <li><strong>パフォーマンス。</strong> グラデーションの描画自体は速いですが、<code>background-image</code> をアニメーションするとフレームごとに paint が走ります。代わりに上のレイヤーで <code>transform</code> をアニメーションしてください。</li>
  <li><strong>アクセシビリティ。</strong> グラデーション上にテキストを置く場合、平均ではなく、テキストが乗る最も<em>悪い</em>箇所のコントラスト比を確認してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>CSS-gradients zijn één regel CSS die soepele kleurovergangen tekent voor achtergronden, knoppen, hero-panelen en overlays — zonder enige image asset. De syntax is krachtig maar lastig met de hand te schrijven: hoeken, percentage-stops, repeating-varianten, lineair mixen met radiaal. Deze tool geeft je een visuele builder die de CSS realtime spiegelt, zodat je een stop op zijn plek kunt slepen en de exacte <code>linear-gradient(...)</code>- of <code>radial-gradient(...)</code>-string kunt kopiëren.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een hero- of call-to-action-sectie-achtergrond bouwen zonder die in een image te bakken.</li>
  <li>Button- of card-hover states maken die er "modern" uitzien zonder een image asset.</li>
  <li>Een brand-gekleurde overlay mocken (gradient + lage-opacity solid voor tekstleesbaarheid).</li>
  <li>Decoratieve dividers, mesh-style achtergronden of geanimeerde SVG-fills genereren.</li>
</ul>

<h3>Lineair vs radiaal</h3>
<ul>
  <li><strong>Lineair</strong> — kleuren overgaan langs een rechte lijn onder een gekozen hoek (0° = bottom-to-top, 90° = left-to-right, 180° = top-to-bottom).</li>
  <li><strong>Radiaal</strong> — kleuren spreiden vanuit een middelpunt naar buiten als cirkel of ellips. Top voor spotlight- of vignette-effecten.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Gebruik als <code>background</code>, niet <code>background-color</code>.</strong> Gradients zijn images, geen kleuren. <code>background-color</code> wordt genegeerd.</li>
  <li><strong>Stops moeten op volgorde staan</strong> voor voorspelbare rendering. De tool sorteert ze automatisch — als je CSS kopieert en met de hand bewerkt, houd de percentages monotoon.</li>
  <li><strong>Hard stops</strong> (twee stops op hetzelfde percentage) maken een scherpe grens in plaats van een fade — handig voor gestreepte of band-effecten.</li>
  <li><strong>Banding op grote oppervlakken.</strong> Lange, low-contrast gradients kunnen zichtbare "banden" tonen op 8-bit schermen. Voeg een kleine SVG noise-overlay toe (<code>filter: url(#noise)</code>) of verschuif de stops iets.</li>
  <li><strong>Performance.</strong> Browsers schilderen gradients snel, maar <code>background-image</code> animeren triggert paint op elke frame — animeer in plaats daarvan <code>transform</code> op een layer erboven.</li>
  <li><strong>Toegankelijkheid.</strong> Als tekst op een gradient zit, check de contrastratio tegen het <em>slechtste</em> punt langs de gradient waar de tekst verschijnt, niet het gemiddelde.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>CSS gradient'lar herhangi bir görsel varlık olmadan arka planlar, düğmeler, hero paneller ve overlay'ler için pürüzsüz renk geçişleri çizen tek satır CSS'tir. Sözdizimi güçlüdür ama elle yazılması zahmetlidir: açılar, yüzde durakları, tekrarlanan varyantlar, lineer ile radial karıştırma. Bu araç gerçek zamanlı CSS'i yansıtan görsel bir builder sunar, böylece bir durağı yerine sürükleyebilir ve tam <code>linear-gradient(...)</code> veya <code>radial-gradient(...)</code> string'ini kopyalayabilirsin.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir görsele yakmadan hero veya call-to-action bölüm arka planı kurma.</li>
  <li>Görsel varlık olmadan "modern" görünen düğme veya kart hover durumları oluşturma.</li>
  <li>Marka renkli overlay mockup'u (gradient + metin okunabilirliği için düşük opaklık solid).</li>
  <li>Dekoratif divider'lar, mesh stili arka planlar veya animated SVG fill'ler üretme.</li>
</ul>

<h3>Lineer - radial</h3>
<ul>
  <li><strong>Lineer</strong> — renkler seçilen açıda düz bir çizgi boyunca geçer (0° = aşağıdan yukarı, 90° = soldan sağa, 180° = yukarıdan aşağı).</li>
  <li><strong>Radial</strong> — renkler bir daire veya elips olarak merkez noktasından dışa yayılır. Spotlight veya vinyet efektleri için harika.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong><code>background</code> olarak kullan, <code>background-color</code> değil.</strong> Gradient'lar görsellerdir, renkler değil. <code>background-color</code> yok sayılır.</li>
  <li><strong>Duraklar sıralı olmalı</strong> öngörülebilir render için. Araç bunları otomatik sıralar — CSS'i kopyalayıp elle düzenliyorsan yüzdeleri monoton tut.</li>
  <li><strong>Sert duraklar</strong> (aynı yüzdede iki durak) fade yerine keskin sınır yapar — çizgili veya bant efektler için kullanışlı.</li>
  <li><strong>Büyük alanlarda banding.</strong> Uzun, düşük kontrastlı gradient'lar 8-bit ekranlarda görünür "bantlar" gösterebilir. Küçük bir SVG noise overlay ekle (<code>filter: url(#noise)</code>) veya durakları hafifçe kaydır.</li>
  <li><strong>Performans.</strong> Tarayıcılar gradient'ları hızlı boyar ama <code>background-image</code>'ı animate etmek her karede paint tetikler — yukarıdaki bir katmanda <code>transform</code>'u animate et.</li>
  <li><strong>Erişilebilirlik.</strong> Bir gradient üzerinde metin oturuyorsa, kontrast oranını gradient boyunca metnin göründüğü <em>en kötü</em> noktaya karşı kontrol et, ortalamasına değil.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>CSS gradient adalah satu baris CSS yang menggambar transisi warna mulus untuk background, tombol, panel hero, dan overlay tanpa aset gambar apa pun. Sintaksisnya kuat tapi ribet ditulis manual: angle, persen stop, varian repeating, mencampur linear dengan radial. Tool ini menyediakan builder visual yang mencerminkan CSS real-time, jadi kamu bisa men-drag stop ke posisinya dan menyalin string <code>linear-gradient(...)</code> atau <code>radial-gradient(...)</code> yang lengkap.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Membuat background section hero atau call-to-action tanpa membakar gambar.</li>
  <li>Membuat hover state tombol atau card yang tampak "modern" tanpa aset gambar.</li>
  <li>Mockup overlay warna brand (gradient + solid low-opacity untuk keterbacaan teks).</li>
  <li>Menghasilkan divider dekoratif, background gaya mesh, atau fill SVG animated.</li>
</ul>

<h3>Linear vs radial</h3>
<ul>
  <li><strong>Linear</strong> — warna bertransisi sepanjang garis lurus di angle yang dipilih (0° = bawah ke atas, 90° = kiri ke kanan, 180° = atas ke bawah).</li>
  <li><strong>Radial</strong> — warna menyebar keluar dari titik tengah sebagai lingkaran atau elips. Cocok untuk efek spotlight atau vignette.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Pakai sebagai <code>background</code>, bukan <code>background-color</code>.</strong> Gradient itu image, bukan warna. <code>background-color</code> akan diabaikan.</li>
  <li><strong>Stop harus urut</strong> untuk rendering yang predictable. Tool ini auto-sort — kalau kamu copy CSS dan edit manual, jaga persentasenya monotonic.</li>
  <li><strong>Hard stop</strong> (dua stop di persentase yang sama) menghasilkan batas tajam alih-alih fade — berguna untuk efek stripe atau band.</li>
  <li><strong>Banding di area besar.</strong> Gradient panjang dengan kontras rendah bisa menampilkan "band" yang terlihat di layar 8-bit. Tambahkan SVG noise overlay kecil (<code>filter: url(#noise)</code>) atau geser stop sedikit.</li>
  <li><strong>Performance.</strong> Browser meng-paint gradient dengan cepat, tapi meng-animate <code>background-image</code> memicu paint di tiap frame — animate <code>transform</code> di layer di atasnya sebagai gantinya.</li>
  <li><strong>Aksesibilitas.</strong> Kalau ada teks di atas gradient, cek rasio kontras terhadap titik <em>terburuk</em> sepanjang gradient di mana teks muncul, bukan rata-rata.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>CSS hỗ trợ gradient linear và radial dưới dạng hàm: <code>linear-gradient(to right, red, blue)</code> tạo ra một dải đỏ-sang-xanh từ trái sang phải. Cú pháp linh hoạt — bạn có thể đặt nhiều color stop, kiểm soát góc, và xếp lớp gradient — nhưng dễ gõ sai. Trình xây dựng này cho phép bạn chỉnh sửa color stop một cách trực quan và sao chép CSS hoàn thành.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Tạo background gradient mượt cho hero section hoặc card.</li>
  <li>Tạo "rainbow" hoặc gradient ý nghĩa với nhiều color stop chính xác.</li>
  <li>Thiết kế gradient radial cho hiệu ứng spotlight hoặc background trang trí.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Color stop có thể chồng lên nhau hoặc nhảy bậc.</strong> Hai stop ở cùng vị trí tạo ra một viền cứng — hữu ích để tạo các vùng ranh giới rõ ràng, nhầm lẫn khi bạn không có ý đó.</li>
  <li><strong>Hướng "to right" vs "90deg".</strong> Chúng tương đương trong CSS hiện đại. Trình duyệt cũ chỉ chấp nhận "to right".</li>
  <li><strong>Banding với gradient.</strong> Gradient từ đen đến xám đậm rất hay hiển thị các dải khi không gian màu 8-bit không đủ chính xác. Thêm một chút noise hoặc dùng OKLCH để giảm thiểu.</li>
  <li><strong>Gradient con không phải là image.</strong> Chúng được tính toán mỗi lần render. Một background-image với một file PNG có thể nhanh hơn cho gradient cực kỳ phức tạp.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "css-box-shadow"],
    "howto": {"flow": "generate",  "action": "generate","noun": "gradient"},
}
