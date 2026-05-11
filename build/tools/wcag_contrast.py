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
        "pt": {"name": "Verificador de Contraste WCAG", "tagline": "Verifique a razão de contraste entre duas cores. Veredito pass/fail para WCAG AA e AAA em qualquer tamanho de texto.", "description": "Verificador de contraste WCAG gratuito. Escolha as cores de foreground e background, obtenha a razão (1:1 a 21:1) e o veredito pass/fail para WCAG 2.1 AA e AAA — para texto normal, texto grande e componentes de UI."},
        "pl": {"name": "Sprawdzacz Kontrastu WCAG", "tagline": "Sprawdź współczynnik kontrastu między dwoma kolorami. Werdykt pass/fail dla WCAG AA i AAA przy każdym rozmiarze tekstu.", "description": "Darmowy sprawdzacz kontrastu WCAG. Wybierz kolor tekstu i tła, dostań współczynnik (1:1 do 21:1) i werdykt pass/fail dla WCAG 2.1 AA i AAA — dla normalnego tekstu, dużego tekstu i komponentów UI."},
        "ja": {"name": "WCAG コントラストチェッカー", "tagline": "2 色のコントラスト比をチェック。各テキストサイズの WCAG AA／AAA で合否を判定。", "description": "無料の WCAG コントラスト比チェッカー。前景色と背景色を選ぶと比率（1:1〜21:1）と、WCAG 2.1 AA／AAA の合否（通常テキスト、大きい文字、UI コンポーネント別）を判定します。"},
        "nl": {"name": "WCAG Contrast Checker", "tagline": "Check de contrastratio tussen twee kleuren. Pass/fail-verdict voor WCAG AA en AAA op elke tekstgrootte.", "description": "Gratis WCAG contrastratio-checker. Kies foreground- en background-kleuren, krijg de ratio (1:1 tot 21:1) en pass/fail-verdicts voor WCAG 2.1 AA en AAA — voor normale tekst, grote tekst en UI-componenten."},
        "tr": {"name": "WCAG Kontrast Denetleyici", "tagline": "İki renk arasındaki kontrast oranını kontrol et. Her metin boyutu için WCAG AA ve AAA'da geçer/kalır yargısı.", "description": "Ücretsiz WCAG kontrast oranı denetleyici. Ön plan ve arka plan renklerini seç, oranı (1:1 ile 21:1) ve WCAG 2.1 AA ve AAA için geçer/kalır yargılarını al — normal metin, büyük metin ve UI bileşenleri için."},
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
    <button class="secondary" onclick="wcSwap()">{LBL_SWAP}</button>
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
        "pt": """
<h2>Para que serve?</h2>
<p>WCAG (Web Content Accessibility Guidelines) define uma razão mínima de contraste entre o texto e seu fundo para que pessoas com baixa visão, daltonismo ou em condições de reflexo ainda consigam ler. Esta ferramenta calcula essa razão (1:1 = idêntico, 21:1 = preto puro sobre branco puro) e diz se seu par de cores passa no WCAG 2.1 nível AA ou AAA, separadamente para texto normal, texto grande e componentes de UI. A matemática segue exatamente a fórmula de luminância da W3C.</p>

<h3>Quando usar</h3>
<ul>
  <li>Verificando se a cor da sua marca em um card branco atende aos padrões de acessibilidade.</li>
  <li>Escolhendo a cor do texto de um botão que passe no AA contra um fundo na cor da marca.</li>
  <li>Auditando um design system token por token antes de subir para produção.</li>
  <li>Justificando uma mudança de cor para um stakeholder com um veredito concreto pass/fail.</li>
  <li>Testando o que seus usuários com preferências de contraste reduzido vão realmente ver.</li>
</ul>

<h3>Os limites</h3>
<ul>
  <li><strong>Texto normal</strong> (abaixo de 18pt / 14pt bold): <strong>4,5:1</strong> para AA, <strong>7:1</strong> para AAA.</li>
  <li><strong>Texto grande</strong> (≥18pt ou ≥14pt bold): <strong>3:1</strong> para AA, <strong>4,5:1</strong> para AAA.</li>
  <li><strong>Componentes de UI &amp; gráficos</strong> (ícones, focus rings, bordas de form, elementos de gráfico que transmitem informação): <strong>3:1</strong> para AA (WCAG 2.1 §1.4.11). Sem nível AAA.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>"Texto grande" é maior do que você pensa.</strong> 18pt é mais ou menos 24px. 14pt bold é mais ou menos 19px bold. Texto de corpo a 16px <em>não</em> é texto grande — ele precisa do limite de 4,5:1.</li>
  <li><strong>Texto claro sobre uma foto cheia de detalhes vai falhar.</strong> A razão de contraste é entre pixels específicos — sobreponha um gradiente escuro ou use um painel sólido para dar ao texto um fundo controlado.</li>
  <li><strong>Anti-aliasing suaviza o contraste.</strong> 4,5:1 é o piso, não o objetivo. Leitura confortável geralmente quer 7:1 ou mais, especialmente para texto de corpo.</li>
  <li><strong>Estados de hover e focus contam.</strong> Se seu botão passa no AA em repouso mas falha no hover, isso é um bug real de acessibilidade.</li>
  <li><strong>WCAG 2.1 vs APCA.</strong> O novo APCA (Accessible Perceptual Contrast Algorithm), proposto para o WCAG 3, dá números diferentes e provavelmente melhores — mas o WCAG 2.1 é o padrão legal que a maioria das jurisdições ainda referencia. Use os números desta ferramenta para atender EN 301 549, ADA ou claims de conformidade AA.</li>
  <li><strong>Não compense com transparência.</strong> Um foreground com 50% de alpha sobre um fundo conhecido tem um contraste efetivo diferente — calcule contra a cor real renderizada, não a original.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>WCAG (Web Content Accessibility Guidelines) definiuje minimalny współczynnik kontrastu między tekstem a jego tłem, żeby osoby z słabym wzrokiem, daltonizmem albo w warunkach odblasku nadal mogły go przeczytać. To narzędzie liczy ten współczynnik (1:1 = identyczne, 21:1 = czysta czerń na czystej bieli) i mówi, czy twoja para kolorów przechodzi WCAG 2.1 Level AA albo AAA, osobno dla normalnego tekstu, dużego tekstu i komponentów UI. Matematyka idzie ściśle za wzorem luminancji W3C.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Sprawdzanie, czy kolor twojej marki na białej karcie spełnia standardy dostępności.</li>
  <li>Wybieranie koloru tekstu przycisku, który przejdzie AA na tle w kolorze marki.</li>
  <li>Audyt design systemu token po tokenie przed wypuszczeniem.</li>
  <li>Uzasadnienie zmiany koloru przed stakeholderem konkretnym werdyktem pass/fail.</li>
  <li>Testowanie, co użytkownicy z preferencjami obniżonego kontrastu faktycznie zobaczą.</li>
</ul>

<h3>Progi</h3>
<ul>
  <li><strong>Tekst normalny</strong> (poniżej 18pt / 14pt bold): <strong>4,5:1</strong> dla AA, <strong>7:1</strong> dla AAA.</li>
  <li><strong>Tekst duży</strong> (≥18pt albo ≥14pt bold): <strong>3:1</strong> dla AA, <strong>4,5:1</strong> dla AAA.</li>
  <li><strong>Komponenty UI &amp; grafika</strong> (ikony, focus ringi, ramki formularzy, elementy wykresu niosące informację): <strong>3:1</strong> dla AA (WCAG 2.1 §1.4.11). Brak poziomu AAA.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>"Duży tekst" jest większy, niż myślisz.</strong> 18pt to mniej więcej 24px. 14pt bold to mniej więcej 19px bold. Body copy w 16px to <em>nie</em> duży tekst — potrzebuje progu 4,5:1.</li>
  <li><strong>Jasny tekst na zatłoczonym zdjęciu padnie.</strong> Współczynnik kontrastu jest między konkretnymi pikselami — nałóż ciemny gradient albo użyj solidnego panelu, żeby dać tekstowi kontrolowane tło.</li>
  <li><strong>Anti-aliasing osłabia kontrast.</strong> 4,5:1 to dno, nie cel. Wygodne czytanie zwykle chce 7:1 albo lepiej, zwłaszcza dla body copy.</li>
  <li><strong>Stany hover i focus się liczą.</strong> Jeśli twój przycisk przechodzi AA w spoczynku, ale pada na hover, to prawdziwy bug dostępności.</li>
  <li><strong>WCAG 2.1 vs APCA.</strong> Nowy APCA (Accessible Perceptual Contrast Algorithm), proponowany do WCAG 3, daje inne i prawdopodobnie lepsze liczby — ale WCAG 2.1 jest standardem prawnym, do którego nadal odnosi się większość jurysdykcji. Używaj liczb tego narzędzia przy spełnianiu EN 301 549, ADA albo claimów zgodności AA.</li>
  <li><strong>Nie kombinuj z przezroczystością.</strong> Foreground z 50% alpha na znanym tle ma inny efektywny kontrast — licz przeciwko faktycznie wyrenderowanemu kolorowi, nie oryginałowi.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>WCAG（ウェブアクセシビリティガイドライン）は、ロービジョン、色覚特性、ギラつく光環境のユーザーでもテキストを読めるよう、テキストと背景の最低コントラスト比を定義しています。本ツールは比率（1:1 = 同色、21:1 = 純黒×純白）を計算し、WCAG 2.1 の AA／AAA に通るかを通常テキスト、大きい文字、UI コンポーネントごとに判定します。計算は W3C の輝度公式に厳密に従います。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>白カードに乗せたブランドカラーがアクセシビリティを満たすか確認したいとき。</li>
  <li>ブランドカラー背景のボタンに対して、AA を満たす文字色を選びたいとき。</li>
  <li>デザインシステムのトークンを 1 つずつ監査して出荷前に揃えたいとき。</li>
  <li>具体的な合否を提示してステークホルダーに色変更を提案したいとき。</li>
  <li>低コントラスト設定のユーザーに実際にどう見えるか確認したいとき。</li>
</ul>

<h3>閾値</h3>
<ul>
  <li><strong>通常テキスト</strong>（18pt 未満／14pt 太字未満）：AA は <strong>4.5:1</strong>、AAA は <strong>7:1</strong>。</li>
  <li><strong>大きい文字</strong>（18pt 以上または 14pt 太字以上）：AA は <strong>3:1</strong>、AAA は <strong>4.5:1</strong>。</li>
  <li><strong>UI コンポーネントとグラフィック</strong>（アイコン、フォーカスリング、フォーム枠、情報を伝えるグラフ要素）：AA は <strong>3:1</strong>（WCAG 2.1 §1.4.11）。AAA 規定はありません。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>「大きい文字」は思ったより大きいです。</strong> 18pt はおよそ 24px、14pt 太字はおよそ 19px 太字。16px の本文は<em>大きい文字ではありません</em>。4.5:1 の閾値が必要です。</li>
  <li><strong>賑やかな写真の上の明るい文字は失格しがち。</strong> コントラスト比は具体的なピクセル間で決まるため、暗いグラデーションを重ねるか、無地パネルで背景を整えてください。</li>
  <li><strong>アンチエイリアシングはコントラストを弱めます。</strong> 4.5:1 は床であって目標ではありません。本文では 7:1 以上を狙うと読みやすくなります。</li>
  <li><strong>ホバーとフォーカスも対象です。</strong> 静止状態で AA を通り、ホバー状態で落ちるなら、それは現実のアクセシビリティバグです。</li>
  <li><strong>WCAG 2.1 と APCA。</strong> WCAG 3 へ提案中の APCA は別の（おそらく改善された）数値を出しますが、ほとんどの法令で参照されるのは依然として WCAG 2.1 です。EN 301 549、ADA、AA 適合主張で使うのは本ツールの数値です。</li>
  <li><strong>透明度で誤魔化さないこと。</strong> 既知の背景に乗せたアルファ 50% の前景は実効コントラストが変わります。元の色ではなく、実際にレンダリングされる色で計算してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>WCAG (Web Content Accessibility Guidelines) definieert een minimum contrastratio tussen tekst en achtergrond zodat mensen met laag zicht, kleurenblindheid of bij tegenlicht het nog kunnen lezen. Deze tool berekent die ratio (1:1 = identiek, 21:1 = puur zwart op puur wit) en vertelt je of je kleurenpaar WCAG 2.1 Level AA of AAA haalt, apart voor normale tekst, grote tekst en UI-componenten. De rekensom volgt de W3C luminance-formule exact.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Checken of je brand-kleur op een witte card voldoet aan toegankelijkheidsnormen.</li>
  <li>Een button-tekstkleur kiezen die AA haalt tegen een brand-gekleurde achtergrond.</li>
  <li>Een design system token voor token auditen voor shipping.</li>
  <li>Een kleur-wijzigingsverzoek rechtvaardigen aan een stakeholder met een concreet pass/fail-verdict.</li>
  <li>Testen wat je users met reduced-contrast voorkeuren daadwerkelijk zullen zien.</li>
</ul>

<h3>De drempels</h3>
<ul>
  <li><strong>Normale tekst</strong> (onder 18pt / 14pt bold): <strong>4.5:1</strong> voor AA, <strong>7:1</strong> voor AAA.</li>
  <li><strong>Grote tekst</strong> (≥18pt of ≥14pt bold): <strong>3:1</strong> voor AA, <strong>4.5:1</strong> voor AAA.</li>
  <li><strong>UI-componenten &amp; graphics</strong> (icons, focus rings, form-borders, chart-elementen die info overdragen): <strong>3:1</strong> voor AA (WCAG 2.1 §1.4.11). Geen AAA-niveau.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>"Grote tekst" is groter dan je denkt.</strong> 18pt is ruwweg 24px. 14pt bold is ruwweg 19px bold. Body copy op 16px is <em>geen</em> grote tekst — het heeft de 4.5:1 drempel nodig.</li>
  <li><strong>Lichte tekst op een drukke foto zal falen.</strong> De contrastratio is tussen specifieke pixels — overlay een donker gradient of gebruik een solid panel om de tekst een gecontroleerde achtergrond te geven.</li>
  <li><strong>Anti-aliasing verzacht contrast.</strong> 4.5:1 is de vloer, geen doel. Comfortabel lezen wil meestal 7:1 of beter, vooral voor body copy.</li>
  <li><strong>Hover- en focus-states tellen.</strong> Als je button AA haalt at rest maar faalt op hover, is dat een echte accessibility-bug.</li>
  <li><strong>WCAG 2.1 vs APCA.</strong> De nieuwe APCA (Accessible Perceptual Contrast Algorithm), voorgesteld voor WCAG 3, geeft andere en arguably betere getallen — maar WCAG 2.1 is de wettelijke standaard waar de meeste jurisdicties nog naar verwijzen. Gebruik de getallen van deze tool bij EN 301 549, ADA of AA-conformance claims.</li>
  <li><strong>Pad niet met transparency.</strong> Een 50%-alpha foreground over een bekende achtergrond heeft een andere effectieve contrast — bereken tegen de daadwerkelijk gerenderde kleur, niet het origineel.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>WCAG (Web İçerik Erişilebilirlik Yönergeleri), düşük görüşlü, renk körü veya parlama koşullarındaki insanların hâlâ okuyabilmesi için metin ile arka planı arasında minimum bir kontrast oranı tanımlar. Bu araç bu oranı hesaplar (1:1 = aynı, 21:1 = saf siyah üzeri saf beyaz) ve renk çiftinin WCAG 2.1 Seviye AA veya AAA'yı geçip geçmediğini, normal metin, büyük metin ve UI bileşenleri için ayrı ayrı söyler. Matematik W3C luminance formülünü tam olarak izler.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Beyaz bir kart üzerindeki marka renginin erişilebilirlik standartlarını karşılayıp karşılamadığını kontrol etme.</li>
  <li>Marka renkli bir arka plana karşı AA'yı geçen bir düğme metin rengi seçme.</li>
  <li>Bir tasarım sistemini token by token denetleme — gönderim öncesi.</li>
  <li>Somut bir geçer/kalır yargısıyla bir paydaşa bir renk-değiştirme isteğini gerekçelendirme.</li>
  <li>Azaltılmış kontrast tercihleri olan kullanıcılarının gerçekte ne göreceğini test etme.</li>
</ul>

<h3>Eşikler</h3>
<ul>
  <li><strong>Normal metin</strong> (18pt / 14pt bold altında): AA için <strong>4.5:1</strong>, AAA için <strong>7:1</strong>.</li>
  <li><strong>Büyük metin</strong> (≥18pt veya ≥14pt bold): AA için <strong>3:1</strong>, AAA için <strong>4.5:1</strong>.</li>
  <li><strong>UI bileşenleri &amp; grafikler</strong> (ikonlar, focus ring, form kenarlıkları, bilgi taşıyan grafik elementleri): AA için <strong>3:1</strong> (WCAG 2.1 §1.4.11). AAA tier yok.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>"Büyük metin" düşündüğünden daha büyüktür.</strong> 18pt kabaca 24px'tir. 14pt bold kabaca 19px bold'dur. 16px'teki gövde kopyası büyük metin <em>değildir</em> — 4.5:1 eşiğine ihtiyacı var.</li>
  <li><strong>Yoğun bir fotoğraf üzerindeki açık metin başarısız olacaktır.</strong> Kontrast oranı belirli pikseller arasındadır — metni kontrollü bir arka plan vermek için koyu bir gradient veya solid bir panel yerleştir.</li>
  <li><strong>Anti-aliasing kontrastı yumuşatır.</strong> 4.5:1 zemindir, hedef değildir. Rahat okuma genellikle 7:1 veya daha iyisini ister, özellikle gövde kopyası için.</li>
  <li><strong>Hover ve focus durumları sayılır.</strong> Düğmen rest'te AA'yı geçer ama hover'da başarısız olursa, bu gerçek bir erişilebilirlik hatasıdır.</li>
  <li><strong>WCAG 2.1 vs APCA.</strong> WCAG 3 için önerilen yeni APCA (Erişilebilir Algısal Kontrast Algoritması) farklı ve tartışmasız daha iyi sayılar verir — ama WCAG 2.1 çoğu yargı yetkisinin hâlâ atıfta bulunduğu yasal standarttır.</li>
  <li><strong>Şeffaflıkla pad etme.</strong> Bilinen bir arka plan üzerinde %50 alfalı bir ön plan farklı bir etkili kontrasta sahiptir — orijinaline değil, gerçek render edilen renge karşı hesapla.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "css-gradient"],
    "howto": {"flow": "calculate", "action": "format",  "noun": "color pair"},
}
