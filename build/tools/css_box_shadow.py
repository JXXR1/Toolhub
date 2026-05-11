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
        "pt": {"name": "Gerador de Box Shadow CSS", "tagline": "Crie sombras CSS de uma ou várias camadas visualmente. Ajuste offset, blur, spread, cor e copie o CSS.", "description": "Gerador gratuito de box-shadow CSS. Empilhe várias sombras, alterne inset, ajuste blur e spread, copie CSS pronto para produção em um clique."},
        "pl": {"name": "Generator CSS Box Shadow", "tagline": "Buduj jedno- lub wielowarstwowe cienie CSS wizualnie. Dostosuj offset, blur, spread, kolor i kopiuj CSS.", "description": "Darmowy generator box-shadow CSS. Stackuj wiele cieni dla realistycznej elewacji, włączaj inset, dostrajaj blur i spread, kopiuj produkcyjny CSS jednym kliknięciem."},
        "ja": {"name": "CSS box-shadow ジェネレーター", "tagline": "1 層または多層の CSS box-shadow をビジュアルに作成。オフセット・ぼかし・広がり・色を調整し、CSS をコピー。", "description": "無料の CSS box-shadow ジェネレーター。複数のシャドウを重ねてリアルな立体感を表現でき、inset の切り替え、blur と spread の微調整、本番投入できる CSS のワンクリックコピーに対応します。"},
        "nl": {"name": "CSS Box-Shadow Generator", "tagline": "Bouw visueel single- of multi-layer CSS box shadows. Stel offset, blur, spread en kleur in en kopieer CSS.", "description": "Gratis CSS box-shadow generator. Stack meerdere shadows voor realistische elevation, toggle inset, fine-tune blur en spread en kopieer production-ready CSS in één klik."},
        "tr": {"name": "CSS Box Shadow Oluşturucu", "tagline": "Tek veya çok katmanlı CSS box shadow'ları görsel olarak kur. Offset, blur, spread, renk ayarla ve CSS'i kopyala.", "description": "Ücretsiz CSS box-shadow oluşturucu. Gerçekçi yükseklik için birden fazla gölgeyi üst üste bin, inset'i aç/kapa, blur ve spread'i ince ayarla ve üretime hazır CSS'i tek tıkla kopyala."},
    },
    "body": """
<div class="tool-card">
  <label>Shadow layers</label>
  <div id="bs-layers" class="bs-layers"></div>
  <div class="button-row" style="margin-top:0.6rem">
    <button class="secondary" onclick="bsAddLayer()">+ {LBL_ADD}</button>
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
        <button class="secondary" onclick="bsRemove(${i})" ${bsLayers.length<=1?'disabled':''}>{LBL_REMOVE}</button>
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
        "pt": """
<h2>Para que serve?</h2>
<p>A propriedade CSS <code>box-shadow</code> é o cavalo de batalha para adicionar profundidade — sombras em cards, destaques em botões, anéis de foco, brilhos, efeitos neon, até 3D falso. A sintaxe (<code>x y blur spread cor</code>, opcional <code>inset</code>, várias sombras separadas por vírgula) é fácil de ler mas chata de ajustar no escuro. Esta ferramenta dá sliders para cada valor com preview ao vivo, além de presets que combinam com elevações comuns de design system.</p>

<h3>Quando usar</h3>
<ul>
  <li>Desenhar elevação de card ou modal que não pareça "barata e dura".</li>
  <li>Construir um estilo de focus-ring para acessibilidade (ex.: glow de outline 2px).</li>
  <li>Criar um efeito neon ou glow para um CTA principal.</li>
  <li>Replicar tokens de elevação Material Design ou estilo Apple para um design system.</li>
  <li>Fazer profundidade "inset" falsa para efeito de botão pressionado ou recesso de card.</li>
</ul>

<h3>O que cada valor faz</h3>
<ul>
  <li><strong>Offset X / Y</strong> — direção em que a sombra cai (Y positivo = para baixo). Para sensação de "luz vinda de cima", use Y > 0 e X pequeno ou zero.</li>
  <li><strong>Blur</strong> — quão suave é a borda. 0 = nítido; maior = desvanece mais suave.</li>
  <li><strong>Spread</strong> — quanto a sombra é maior (ou menor, se negativo) que o próprio box.</li>
  <li><strong>Cor e alpha</strong> — geralmente um preto com alpha parcial ou cor da marca. Preto puro <code>#000</code> fica pesado demais; tente <code>#0003</code> a <code>#0002</code> para profundidade natural.</li>
  <li><strong>Inset</strong> — inverte a sombra para dentro, como um recesso.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Uma sombra grande sozinha parece artificial.</strong> Elevação real é duas ou três camadas empilhadas: uma sombra apertada, escura e próxima, mais uma larga, suave e distante. O preset "Material elevation" mostra o padrão.</li>
  <li><strong>Preto puro é pesado demais.</strong> Use ~10–25% de alpha em preto, ou tinja a sombra com a cor complementar da superfície para dar calor.</li>
  <li><strong>Sombras renderizam fora do box.</strong> Se o container tem <code>overflow: hidden</code>, a sombra é cortada. Use um wrapper ou mova o <code>overflow</code> para um filho.</li>
  <li><strong>Sombra em fundo transparente.</strong> Se o box não tem <code>background</code>, a sombra aparece através do próprio box — geralmente surpreendente.</li>
  <li><strong>Performance:</strong> blur muito grande em muitos elementos pode pesar em mobile de baixo desempenho. Teste num device real antes de enviar glows chiques.</li>
  <li><strong>Dark mode.</strong> Sombras escuras sobre escuro praticamente somem; considere uma borda interna brilhante ou uma sombra com tom claro em temas escuros.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>CSS-owy <code>box-shadow</code> to koń roboczy do dodawania głębi — drop shadows na kartach, podświetlenia przycisków, focus ringi, glow, efekty neonowe, nawet udawane 3D. Składnia (<code>x y blur spread kolor</code>, opcjonalnie <code>inset</code>, kilka cieni rozdzielonych przecinkami) jest łatwa do czytania, ale upierdliwa do tweakowania na ślepo. To narzędzie daje suwaki do każdej wartości i podgląd na żywo, plus presety pasujące do typowych elewacji w design systemach.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Projektowanie elewacji karty albo modala, która nie wygląda "tanio i ostro".</li>
  <li>Zbudowanie stylu focus ring dla dostępności (np. 2px outline glow).</li>
  <li>Stworzenie efektu neon albo glow dla głównego CTA.</li>
  <li>Replikacja tokenów elewacji Material Design albo w stylu Apple do design systemu.</li>
  <li>Sztuczna głębia "inset" dla efektu wciśniętego przycisku albo wgłębienia karty.</li>
</ul>

<h3>Co robi każda wartość</h3>
<ul>
  <li><strong>Offset X / Y</strong> — kierunek, w którym pada cień (Y dodatni = w dół). Dla efektu "światło z góry" używaj Y > 0 i małego albo zerowego X.</li>
  <li><strong>Blur</strong> — jak miękka jest krawędź. 0 = ostra; większy = łagodniejsze rozmycie.</li>
  <li><strong>Spread</strong> — o ile cień jest większy (albo mniejszy, jeśli ujemny) od samego boxa.</li>
  <li><strong>Kolor i alpha</strong> — zwykle czarny z częściowym alpha albo kolor marki. Czysty <code>#000</code> wygląda zbyt ciężko; spróbuj <code>#0003</code> do <code>#0002</code> dla naturalnej głębi.</li>
  <li><strong>Inset</strong> — odwraca cień do środka, jak wgłębienie.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Jeden duży cień wygląda sztucznie.</strong> Prawdziwa elewacja to dwie lub trzy nałożone warstwy: ciasny, ciemny, blisko + szeroki, miękki, daleko. Preset "Material elevation" pokazuje schemat.</li>
  <li><strong>Czysta czerń jest za ciężka.</strong> Używaj ~10–25% alpha czerni, albo podbarw cień kolorem dopełniającym powierzchnię, żeby dodać ciepła.</li>
  <li><strong>Cienie renderują się poza boxem.</strong> Jeśli kontener ma <code>overflow: hidden</code>, cień jest obcinany. Użyj wrappera albo przenieś <code>overflow</code> na dziecko.</li>
  <li><strong>Cień na przezroczystym tle.</strong> Jeśli box nie ma <code>background</code>, cień przebija przez sam box — zwykle zaskakuje.</li>
  <li><strong>Wydajność:</strong> bardzo duży blur na wielu elementach potrafi obciążyć słabsze mobilki. Testuj na realnym sprzęcie przed wypuszczeniem fancy glowów.</li>
  <li><strong>Dark mode.</strong> Subtelne ciemne cienie na ciemnym tle prawie znikają; rozważ jasny inner border albo cień z jasnym podtonem w ciemnych motywach.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>CSS の <code>box-shadow</code> プロパティは、奥行きを表現する万能ツールです。カードのドロップシャドウ、ボタンのハイライト、フォーカスリング、グロー、ネオン効果、簡易的な 3D まで、これ一つでこなせます。構文（<code>x y blur spread color</code>、オプションの <code>inset</code>、カンマ区切りで複数）は読みやすい一方、目視で調整するのは面倒です。本ツールは各値のスライダーとライブプレビューに加え、よくあるデザインシステムのエレベーションに合うプリセットを提供します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>カードやモーダルのエレベーションを「安っぽく」「硬く」見えないように設計したいとき。</li>
  <li>アクセシビリティ向けのフォーカスリング（例：2px のアウトライングロー）を作るとき。</li>
  <li>ヒーローの CTA にネオン／グロー効果を作るとき。</li>
  <li>Material Design や Apple 風のエレベーショントークンをデザインシステム用に再現するとき。</li>
  <li>押下されたボタンや凹んだカードを表現する偽の "inset" 奥行きを作るとき。</li>
</ul>

<h3>各値の意味</h3>
<ul>
  <li><strong>X / Y オフセット</strong> — 影が落ちる方向（Y が正なら下方向）。「上から光」の雰囲気には Y > 0 と X 小さめ（または 0）が合います。</li>
  <li><strong>Blur</strong> — エッジの柔らかさ。0 = シャープ、大きいほど柔らかいフェードに。</li>
  <li><strong>Spread</strong> — シャドウがボックス自体よりどれだけ大きい（または負なら小さい）か。</li>
  <li><strong>色とアルファ</strong> — 通常は半透明の黒、またはブランドカラー。純粋な <code>#000</code> は重すぎるので、自然な奥行きには <code>#0002</code>〜<code>#0003</code> あたりが有効です。</li>
  <li><strong>Inset</strong> — シャドウを内側に反転させ、凹みのように見せます。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>大きなシャドウ 1 枚は不自然に見えます。</strong> 本物のエレベーションは、近くて濃く絞ったシャドウと、遠くて柔らかく広いシャドウを 2〜3 枚重ねます。「Material elevation」プリセットがその典型です。</li>
  <li><strong>純黒は重すぎます。</strong> 黒のアルファ 10–25% 程度を使うか、表面の補色で温かみを足すといい感じになります。</li>
  <li><strong>シャドウはボックスの外側に描画されます。</strong> コンテナに <code>overflow: hidden</code> があるとクリップされます。ラッパーを使うか、<code>overflow</code> を子要素に移してください。</li>
  <li><strong>背景が透明なボックスのシャドウ。</strong> ボックスに <code>background</code> がないと、シャドウがボックスを透過して見えてしまいます（だいたい意図しない結果）。</li>
  <li><strong>パフォーマンス：</strong> 大きな blur を多数の要素に適用すると、低スペックモバイルで重くなることがあります。派手なグローを出す前に実機で確認しましょう。</li>
  <li><strong>ダークモード。</strong> 暗背景に微妙な暗いシャドウはほとんど見えません。明るいインナーボーダーや、明色寄りのシャドウを検討してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>De CSS <code>box-shadow</code>-property is de werkpaard om diepte toe te voegen — drop shadows op cards, button-highlights, focus rings, glows, neon-effecten, zelfs nep-3D. De syntax (<code>x y blur spread color</code>, optionele <code>inset</code>, meerdere shadows komma-gescheiden) is makkelijk te lezen maar omslachtig om blind te tweaken. Deze tool geeft je sliders voor elke waarde plus een live preview, plus presets die overeenkomen met de gangbare design-system elevations.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Card- of modal-elevation ontwerpen die er niet "goedkoop en hard" uitziet.</li>
  <li>Een focus-ring-stijl bouwen voor toegankelijkheid (bijv. een 2px outline-glow).</li>
  <li>Een neon- of glow-effect maken voor een hero-CTA.</li>
  <li>Material Design- of Apple-stijl elevation tokens repliceren voor een design system.</li>
  <li>Nep-"inset" diepte maken voor een ingedrukt-knop-effect of een card-recess.</li>
</ul>

<h3>Wat elke waarde doet</h3>
<ul>
  <li><strong>X / Y offset</strong> — richting waar de shadow valt (positieve Y = naar beneden). Voor een "licht van boven"-gevoel gebruik je Y > 0 en kleine of nul X.</li>
  <li><strong>Blur</strong> — hoe zacht de rand is. 0 = scherp; groter = zachtere fade.</li>
  <li><strong>Spread</strong> — hoeveel groter (of kleiner, bij negatief) de shadow is dan de box zelf.</li>
  <li><strong>Color &amp; alpha</strong> — meestal een partial-alpha zwart of brand-kleur. Puur <code>#000</code> ziet er te zwaar uit; probeer <code>#0003</code> tot <code>#0002</code> voor natuurlijke diepte.</li>
  <li><strong>Inset</strong> — keert de shadow naar binnen, als een recess.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Eén grote shadow lijkt kunstmatig.</strong> Echte elevation is twee of drie lagen gestapeld: een strakke, donkere, dichtbije shadow plus een brede, zachte, ver-uit. De "Material elevation"-preset toont het patroon.</li>
  <li><strong>Puur zwart is te zwaar.</strong> Gebruik ~10–25% alpha-zwart, of tint de shadow met de complementkleur van het oppervlak voor warmte.</li>
  <li><strong>Shadows renderen buiten de box.</strong> Als je container <code>overflow: hidden</code> heeft, wordt de shadow geclipt. Gebruik een wrapper of verplaats <code>overflow</code> naar een child.</li>
  <li><strong>Shadow op transparante achtergrond.</strong> Als de box geen <code>background</code> heeft, schijnt de shadow door de box zelf — meestal verrassend.</li>
  <li><strong>Performance:</strong> heel grote blur op veel elementen kan duur zijn op low-end mobile. Test op een echt device voor je fancy glows uitlevert.</li>
  <li><strong>Dark mode.</strong> Subtiele dark-on-dark shadows verdwijnen bijna; overweeg een heldere inner border of een licht-getinte shadow in donkere thema's.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>CSS <code>box-shadow</code> özelliği derinlik eklemek için iş atıdır — kartlarda drop shadow, düğme highlight, focus ring, glow, neon efektleri, hatta sahte 3D. Sözdizimi (<code>x y blur spread color</code>, isteğe bağlı <code>inset</code>, virgülle ayrılmış birden fazla gölge) okuması kolaydır ama körü körüne ayarlamak zahmetlidir. Bu araç her değer için kaydırıcılar ve canlı önizleme, artı yaygın tasarım sistemi yüksekliklerini eşleştiren preset'ler sunar.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>"Ucuz ve sert" görünmeyen kart veya modal yüksekliği tasarlama.</li>
  <li>Erişilebilirlik için focus-ring stili kurma (örn. 2px outline glow).</li>
  <li>Bir hero CTA için neon veya glow efekti hazırlama.</li>
  <li>Material Design veya Apple stili yükseklik token'larını bir tasarım sistemi için kopyalama.</li>
  <li>Basılı düğme efekti veya kart girintisi için sahte "inset" derinlik üretme.</li>
</ul>

<h3>Her değer ne yapar</h3>
<ul>
  <li><strong>X / Y offset</strong> — gölgenin düştüğü yön (pozitif Y = aşağı). "Yukarıdan ışık" hissi için Y > 0 ve küçük veya sıfır X kullan.</li>
  <li><strong>Blur</strong> — kenarın ne kadar yumuşak olduğu. 0 = keskin; daha büyük = daha yumuşak.</li>
  <li><strong>Spread</strong> — gölgenin kutudan ne kadar büyük (veya negatifse küçük) olduğu.</li>
  <li><strong>Renk &amp; alfa</strong> — genellikle kısmi alfalı siyah veya marka rengi. Saf <code>#000</code> çok ağır görünür; doğal derinlik için <code>#0003</code> ile <code>#0002</code> dene.</li>
  <li><strong>Inset</strong> — gölgeyi içe çevirir, girinti gibi.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Tek büyük gölge yapay görünür.</strong> Gerçek yükseklik iki veya üç katman üst üstedir: sıkı, koyu, yakın bir gölge artı geniş, yumuşak, uzak bir gölge. "Material elevation" preset'i bu deseni gösterir.</li>
  <li><strong>Saf siyah çok ağırdır.</strong> ~%10–25 alfa siyah kullan veya gölgeyi yüzeyin tamamlayıcısıyla renklendir.</li>
  <li><strong>Gölgeler kutu dışında render olur.</strong> Container'ın <code>overflow: hidden</code> varsa, gölge kırpılır. Bir wrapper kullan veya <code>overflow</code>'u bir child'a taşı.</li>
  <li><strong>Şeffaf arka planda gölge.</strong> Kutunun <code>background</code>'u yoksa, gölge kutunun kendisinden geçer — genellikle sürpriz.</li>
  <li><strong>Performans:</strong> Çok elemanda çok büyük blur düşük seviye mobilde maliyetli olabilir. Süslü glow'ları göndermeden önce gerçek cihazda test et.</li>
  <li><strong>Dark mode.</strong> Subtle koyu üzeri koyu gölgeler neredeyse kaybolur; karanlık temalarda parlak bir iç kenarlık veya açık tonlu bir gölge düşün.</li>
</ul>
""",
    },
    "related": ["css-gradient", "color-picker", "color-converter"],
    "howto": {"flow": "generate",  "action": "generate","noun": "shadow"},
}
