TOOL = {
    "slug": "percentage-calculator",
    "category": "math",
    "icon": "%",
    "tags": ["percentage", "percent", "calculate", "discount", "increase", "decrease", "tip", "tax"],
    "i18n": {
        "en": {
            "name": "Percentage Calculator",
            "tagline": "Five percentage calculators in one: of, what %, increase/decrease, change, and tip/tax.",
            "description": "Free online percentage calculator. Compute X% of Y, what % is X of Y, percentage change, percentage increase/decrease, and tip or tax amounts.",
        },
        "de": {"name": "Prozentrechner", "tagline": "Fünf Prozent-Rechner in einem: von, wie viel %, Zunahme/Abnahme, Änderung und Trinkgeld/Steuer.", "description": "Kostenloser Prozentrechner. X % von Y, wie viel % ist X von Y, Prozentänderung, Zunahme/Abnahme sowie Trinkgeld- oder Steuerberechnung."},
        "es": {"name": "Calculadora de Porcentajes", "tagline": "Cinco calculadoras de porcentaje en una: de, qué %, aumento/descuento, variación y propina/impuesto.", "description": "Calculadora de porcentajes gratuita en línea. X% de Y, qué % es X de Y, variación porcentual, aumento/descuento y propina o impuesto."},
        "fr": {"name": "Calculateur de Pourcentage", "tagline": "Cinq calculateurs de pourcentage en un : de, quel %, hausse/baisse, variation et pourboire/taxe.", "description": "Calculateur de pourcentage gratuit en ligne. X% de Y, quel % est X de Y, variation, hausse/baisse et pourboire ou taxe."},
        "it": {"name": "Calcolatore di Percentuale", "tagline": "Cinque calcolatori di percentuale in uno: di, quale %, aumento/sconto, variazione e mancia/IVA.", "description": "Calcolatore di percentuale gratuito online. X% di Y, quale % è X di Y, variazione, aumento/sconto e mancia o IVA."},
        "pt": {"name": "Calculadora de Porcentagem", "tagline": "Cinco calculadoras de porcentagem em uma: de, qual %, aumento/desconto, variação e gorjeta/imposto.", "description": "Calculadora de porcentagem gratuita online. Calcule X% de Y, qual % X é de Y, variação percentual, aumento/desconto percentual e valores de gorjeta ou imposto."},
        "pl": {"name": "Kalkulator Procentów", "tagline": "Pięć kalkulatorów procentów w jednym: ile %, ile to %, zmiana, wzrost/spadek i napiwek/podatek.", "description": "Darmowy online kalkulator procentów. Policz X% z Y, ile % X stanowi Y, zmianę procentową, procentowy wzrost/spadek oraz wartość napiwku albo podatku."},
        "ja": {"name": "パーセンテージ計算機", "tagline": "5 つの百分率計算をひとつに：%、何%、増加／減少、変化、チップ／税。", "description": "オンライン無料のパーセンテージ計算機。Y の X%、X は Y の何 %、パーセンテージ変化、増加／減少、チップや税の金額を計算できます。"},
        "nl": {"name": "Percentage-calculator", "tagline": "Vijf percentage-calculators in één: of, hoeveel %, increase/decrease, change en tip/tax.", "description": "Gratis online percentage-calculator. Bereken X% van Y, welk % is X van Y, percentage-wijziging, percentage-verhoging/-verlaging en tip- of belastingbedragen."},
        "tr": {"name": "Yüzde Hesaplayıcı", "tagline": "Tek araçta beş yüzde hesaplayıcı: of, what %, artış/azalış, değişim ve tip/vergi.", "description": "Ücretsiz online yüzde hesaplayıcı. Y'nin X%'si, X Y'nin yüzde kaçı, yüzde değişim, yüzde artış/azalış ve tip veya vergi tutarlarını hesapla."},
        "id": {"name": "Kalkulator Persentase", "tagline": "Lima kalkulator persentase dalam satu tool: of, what %, increase/decrease, change, dan tip/tax.", "description": "Kalkulator persentase gratis. Lima kalkulator dalam satu: X% dari Y, Y berapa persen dari Z, kenaikan/penurunan, persen perubahan antara dua nilai, dan kalkulator tip/pajak."},
        "vi": {"name": "Máy tính Phần trăm", "tagline": "Năm máy tính phần trăm trong một công cụ: của, bao nhiêu %, tăng/giảm, thay đổi và tip/thuế.", "description": "Máy tính phần trăm miễn phí trực tuyến. Năm chế độ trong một công cụ: X% của Y, X là bao nhiêu phần trăm của Y, tăng/giảm theo phần trăm, phần trăm thay đổi giữa hai giá trị, và tip/thuế."},
    },
    "body": """
<div class="tool-card">
  <label>Calculation</label>
  <select id="pc-mode" onchange="pcSwitch()">
    <option value="of">What is X% of Y</option>
    <option value="is">X is what % of Y</option>
    <option value="change">% change from X to Y</option>
    <option value="inc">Increase X by Y%</option>
    <option value="dec">Decrease X by Y%</option>
    <option value="tip">Tip / Tax: X plus Y%</option>
  </select>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label id="pc-l1">X</label>
      <input type="number" id="pc-a" step="any" oninput="pcRun()" value="20">
    </div>
    <div>
      <label id="pc-l2">Y</label>
      <input type="number" id="pc-b" step="any" oninput="pcRun()" value="150">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="pc-out" class="output" style="font-size:1.1rem">{LBL_NO_INPUT}</div>
  <div id="pc-formula" class="meta" style="margin-top:0.6rem;font-family:ui-monospace,monospace"></div>
</div>
""",
    "script": """
<script>
function pcFmt(n){if(!isFinite(n))return '∞';const r=Math.round(n*1e6)/1e6;return Number.isInteger(r)?r.toString():r.toString().replace(/(\\.\\d*?)0+$/,'$1').replace(/\\.$/,'')}
function pcSwitch(){
  const m = document.getElementById('pc-mode').value;
  const l1 = document.getElementById('pc-l1'), l2 = document.getElementById('pc-l2');
  const labels = {
    of:    ['Percentage (X%)', 'Of (Y)'],
    is:    ['Part (X)',         'Of total (Y)'],
    change:['From (X)',         'To (Y)'],
    inc:   ['Starting value (X)', 'Increase by (Y%)'],
    dec:   ['Starting value (X)', 'Decrease by (Y%)'],
    tip:   ['Bill amount (X)',    'Tip / tax (Y%)'],
  }[m];
  l1.textContent = labels[0];
  l2.textContent = labels[1];
  pcRun();
}
function pcRun(){
  const m = document.getElementById('pc-mode').value;
  const a = parseFloat(document.getElementById('pc-a').value);
  const b = parseFloat(document.getElementById('pc-b').value);
  const out = document.getElementById('pc-out');
  const fml = document.getElementById('pc-formula');
  if(isNaN(a) || isNaN(b)){ out.textContent = '{LBL_NO_INPUT}'; fml.textContent = ''; return; }
  let res = '', formula = '';
  switch(m){
    case 'of':     { const v = (a/100)*b; res = `${pcFmt(a)}% of ${pcFmt(b)} = ${pcFmt(v)}`; formula = `(${pcFmt(a)} ÷ 100) × ${pcFmt(b)} = ${pcFmt(v)}`; break; }
    case 'is':     { const v = b===0 ? Infinity : (a/b)*100; res = `${pcFmt(a)} is ${pcFmt(v)}% of ${pcFmt(b)}`; formula = `(${pcFmt(a)} ÷ ${pcFmt(b)}) × 100 = ${pcFmt(v)}%`; break; }
    case 'change': { const v = a===0 ? Infinity : ((b-a)/Math.abs(a))*100; res = `Change: ${pcFmt(v)}% (${v>=0?'increase':'decrease'})`; formula = `((${pcFmt(b)} − ${pcFmt(a)}) ÷ |${pcFmt(a)}|) × 100 = ${pcFmt(v)}%`; break; }
    case 'inc':    { const v = a + (a*b/100); res = `${pcFmt(a)} increased by ${pcFmt(b)}% = ${pcFmt(v)}`; formula = `${pcFmt(a)} × (1 + ${pcFmt(b)}/100) = ${pcFmt(v)}`; break; }
    case 'dec':    { const v = a - (a*b/100); res = `${pcFmt(a)} decreased by ${pcFmt(b)}% = ${pcFmt(v)}`; formula = `${pcFmt(a)} × (1 − ${pcFmt(b)}/100) = ${pcFmt(v)}`; break; }
    case 'tip':    { const tip = a*b/100; const total = a+tip; res = `Tip/Tax: ${pcFmt(tip)} · Total: ${pcFmt(total)}`; formula = `${pcFmt(a)} × ${pcFmt(b)}/100 = ${pcFmt(tip)} · ${pcFmt(a)} + ${pcFmt(tip)} = ${pcFmt(total)}`; break; }
  }
  out.textContent = res;
  fml.textContent = formula;
}
document.addEventListener('DOMContentLoaded', pcSwitch);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Six different "percentage" calculations come up daily and are easy to mix up: how much is X% of Y? What percent is X out of Y? What's the change between two values? Apply a markup or discount? Tip or tax? Each is a slightly different formula, and getting them confused leads to wrong invoices, wrong discounts, and embarrassing reviews. This tool runs all six side by side with the formula spelled out, so you can pick the right one and double-check the maths.</p>

<h3>What each mode does</h3>
<ul>
  <li><strong>What is X% of Y</strong> — for discounts, commissions, percentage of a total. <em>20% of 150 → 30</em>.</li>
  <li><strong>X is what % of Y</strong> — for "score / max" style ratios. <em>30 of 150 → 20%</em>.</li>
  <li><strong>% change</strong> — signed: positive is an increase, negative is a decrease. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Increase / Decrease</strong> — applies a percentage adjustment to a starting value.</li>
  <li><strong>Tip / Tax</strong> — convenience for adding a percentage on top of a bill.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Percentage change isn't symmetric.</strong> Going 100 → 125 is +25%; going 125 → 100 is −20%, not −25%. The denominator is the starting value, which differs in each direction.</li>
  <li><strong>Stacking percentages compounds.</strong> A 20% increase followed by a 20% decrease doesn't return you to the start (1.20 × 0.80 = 0.96, a net 4% loss). For sequential markups/discounts, calculate each step.</li>
  <li><strong>Tip on pre-tax vs post-tax.</strong> Convention varies by country and venue. The tool computes the percentage of the value you enter — pick which value you actually want as the base.</li>
  <li><strong>Rounding.</strong> Output is rounded to 6 decimals then trimmed; if you need legal/accounting precision (banker's rounding, currency-specific rules), do that step in your domain layer, not here.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Seis cálculos diferentes de "porcentagem" aparecem todo dia e são fáceis de confundir: quanto é X% de Y? Que porcentagem X é de Y? Qual a variação entre dois valores? Aplicar um markup ou desconto? Gorjeta ou imposto? Cada um é uma fórmula um pouco diferente, e confundi-las leva a notas fiscais erradas, descontos errados e reviews vergonhosos. Esta ferramenta roda os seis lado a lado com a fórmula explicitada, para você escolher o certo e conferir a conta.</p>

<h3>O que cada modo faz</h3>
<ul>
  <li><strong>Quanto é X% de Y</strong> — para descontos, comissões, porcentagem de um total. <em>20% de 150 → 30</em>.</li>
  <li><strong>X é qual % de Y</strong> — para razões do tipo "nota / máximo". <em>30 de 150 → 20%</em>.</li>
  <li><strong>Variação %</strong> — com sinal: positivo é aumento, negativo é redução. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Aumentar / Diminuir</strong> — aplica um ajuste percentual a um valor inicial.</li>
  <li><strong>Gorjeta / Imposto</strong> — atalho para somar uma porcentagem em cima de uma conta.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Variação percentual não é simétrica.</strong> Ir de 100 → 125 é +25%; ir de 125 → 100 é −20%, não −25%. O denominador é o valor inicial, que muda em cada direção.</li>
  <li><strong>Empilhar porcentagens compõe.</strong> Um aumento de 20% seguido de uma redução de 20% não te leva de volta ao início (1.20 × 0.80 = 0.96, perda líquida de 4%). Para markups/descontos sequenciais, calcule cada passo.</li>
  <li><strong>Gorjeta sobre valor antes ou depois do imposto.</strong> A convenção varia por país e estabelecimento. A ferramenta calcula a porcentagem do valor que você digita — escolha qual valor você de fato quer como base.</li>
  <li><strong>Arredondamento.</strong> A saída é arredondada para 6 casas decimais e depois aparada; se você precisa de precisão legal/contábil (banker's rounding, regras específicas de moeda), faça esse passo na sua camada de domínio, não aqui.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Sześć różnych obliczeń "procentowych" pojawia się codziennie i łatwo je pomylić: ile to X% z Y? Jaki procent X stanowi Y? Jaka zmiana między dwiema wartościami? Doliczyć narzut albo rabat? Napiwek albo podatek? Każde to trochę inny wzór, a pomylenie ich prowadzi do błędnych faktur, błędnych rabatów i krępujących recenzji. To narzędzie liczy wszystkie sześć obok siebie z wyłożonym wzorem, żebyś mógł wybrać właściwe i sprawdzić rachunek.</p>

<h3>Co robi każdy tryb</h3>
<ul>
  <li><strong>Ile to X% z Y</strong> — do rabatów, prowizji, procentu sumy. <em>20% z 150 → 30</em>.</li>
  <li><strong>Ile X stanowi Y</strong> — do współczynników typu "wynik / max". <em>30 ze 150 → 20%</em>.</li>
  <li><strong>Zmiana %</strong> — ze znakiem: dodatnia to wzrost, ujemna spadek. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Wzrost / Spadek</strong> — aplikuje korektę procentową do wartości startowej.</li>
  <li><strong>Napiwek / Podatek</strong> — wygodny sposób na doliczenie procentu do rachunku.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Zmiana procentowa nie jest symetryczna.</strong> Pójście 100 → 125 to +25%; pójście 125 → 100 to −20%, nie −25%. Mianownikiem jest wartość startowa, która różni się w każdym kierunku.</li>
  <li><strong>Stackowanie procentów się składa.</strong> 20% wzrost, a po nim 20% spadek nie wraca cię do startu (1.20 × 0.80 = 0.96, netto strata 4%). Dla sekwencyjnych narzutów/rabatów licz każdy krok.</li>
  <li><strong>Napiwek od kwoty przed czy po podatku.</strong> Konwencja różni się krajem i lokalem. Narzędzie liczy procent od wartości, którą wpisujesz — wybierz, którą wartość faktycznie chcesz jako bazę.</li>
  <li><strong>Zaokrąglanie.</strong> Wyjście jest zaokrąglane do 6 miejsc po przecinku i przycinane; jeśli potrzebujesz precyzji prawnej/księgowej (banker's rounding, walutowe reguły), zrób to w warstwie domeny, nie tutaj.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>日常的によく出てくる「パーセンテージ」計算は 6 種類あり、どれも混同しがちです。Y の X% は？ X は Y の何 %？ 2 値の変化率は？ 値上げ・値引きの適用は？ チップや税は？ それぞれ式が微妙に違い、混同すると請求書の誤り、誤った割引、恥ずかしいレビューにつながります。本ツールは 6 つを並べて式を明示するため、適切な計算を選び、結果を見直しできます。</p>

<h3>各モードの動作</h3>
<ul>
  <li><strong>Y の X% は</strong> — 値引き、コミッション、合計の何%。<em>150 の 20% → 30</em>。</li>
  <li><strong>X は Y の何 %</strong> — 「得点／満点」型の比率。<em>150 のうち 30 → 20%</em>。</li>
  <li><strong>% 変化</strong> — 符号付き：正なら増加、負なら減少。<em>100 → 125 = +25%</em>。</li>
  <li><strong>増加 / 減少</strong> — 開始値に対してパーセンテージで補正します。</li>
  <li><strong>チップ / 税</strong> — 請求金額に上乗せするパーセンテージの便利機能。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>パーセンテージ変化は対称ではありません。</strong> 100 → 125 は +25% ですが、125 → 100 は −20% であって −25% ではありません。分母が「開始値」で、向きによって変わるからです。</li>
  <li><strong>パーセンテージは合成されます。</strong> 20% 上げて 20% 下げても元には戻りません（1.20 × 0.80 = 0.96、4% の純減）。連続した値上げ・値引きはステップごとに計算してください。</li>
  <li><strong>税抜き／税込みのチップ。</strong> 慣習は国や店によって異なります。本ツールは入力した値に対する % を計算しますので、基準としたい値を選んで入力してください。</li>
  <li><strong>丸め。</strong> 出力は小数 6 桁で丸めて末尾を整理します。法務／会計上の正確さ（銀行家丸め、通貨別ルール）が必要な場合は、本ツールではなくドメイン層で処理してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Zes verschillende "percentage"-berekeningen komen dagelijks voor en zijn makkelijk te verwarren: hoeveel is X% van Y? Welk percentage is X uit Y? Wat is de verandering tussen twee waarden? Een opslag of korting toepassen? Tip of belasting? Elk is een lichtjes andere formule, en ze verwarren leidt tot foute facturen, foute kortingen en gênante reviews. Deze tool draait alle zes side by side met de formule uitgespeld, zodat je de juiste kunt kiezen en de rekensom kunt dubbelchecken.</p>

<h3>Wat elke mode doet</h3>
<ul>
  <li><strong>Wat is X% van Y</strong> — voor kortingen, commissies, percentage van een totaal. <em>20% van 150 → 30</em>.</li>
  <li><strong>X is welk % van Y</strong> — voor "score / max"-stijl ratio's. <em>30 van 150 → 20%</em>.</li>
  <li><strong>% verandering</strong> — signed: positief is een toename, negatief is een afname. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Verhoging / Verlaging</strong> — past een percentage-aanpassing toe op een startwaarde.</li>
  <li><strong>Tip / Tax</strong> — gemak voor een percentage op een rekening opbouwen.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Percentage-wijziging is niet symmetrisch.</strong> 100 → 125 is +25%; 125 → 100 is −20%, geen −25%. De noemer is de startwaarde, die in elke richting verschilt.</li>
  <li><strong>Percentages stacken compounded.</strong> Een 20%-toename gevolgd door een 20%-afname brengt je niet terug naar het begin (1.20 × 0.80 = 0.96, een netto 4%-verlies). Voor sequentiële markups/discounts bereken je elke stap.</li>
  <li><strong>Fooi op pre-tax vs post-tax.</strong> Conventie varieert per land en venue. De tool berekent het percentage van de waarde die je invoert — kies welke waarde je daadwerkelijk wil als basis.</li>
  <li><strong>Afronding.</strong> Output is afgerond op 6 decimalen en daarna getrimd; als je legal/accounting-precisie nodig hebt (banker's rounding, currency-specifieke regels), doe die stap in je domain-laag, niet hier.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Günlük olarak karşılaşılan ve karıştırması kolay altı farklı "yüzde" hesaplaması: Y'nin X%'si ne kadar? X, Y'nin yüzde kaçı? İki değer arasındaki değişim nedir? Bir markup veya indirim uygulansın mı? Tip veya vergi? Her biri biraz farklı bir formüldür ve karıştırmak yanlış faturalar, yanlış indirimler ve utanç verici incelemelere yol açar. Bu araç altısını yan yana, formülü açıkça gösterilerek çalıştırır, böylece doğru olanı seçip matematiği iki kez kontrol edebilirsin.</p>

<h3>Her mod ne yapar</h3>
<ul>
  <li><strong>Y'nin X%'si ne</strong> — indirimler, komisyonlar, bir totalin yüzdesi için. <em>150'nin 20%'si → 30</em>.</li>
  <li><strong>X, Y'nin yüzde kaçı</strong> — "skor / max" tarzı oranlar için. <em>150'nin 30'u → 20%</em>.</li>
  <li><strong>% değişim</strong> — işaretli: pozitif artış, negatif azalış. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Artış / Azalış</strong> — başlangıç değerine bir yüzde ayarlaması uygular.</li>
  <li><strong>Tip / Vergi</strong> — bir hesabın üzerine yüzde eklemek için kolaylık.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Yüzde değişim simetrik değildir.</strong> 100 → 125 gitmek +25%; 125 → 100 gitmek −20%, −25% değil. Payda başlangıç değeridir ve her yönde farklıdır.</li>
  <li><strong>Yüzdeleri üst üste koymak bileşik etki yapar.</strong> %20 artış ve ardından %20 azalış seni başlangıca döndürmez (1,20 × 0,80 = 0,96, net %4 kayıp). Sıralı markup'lar/indirimler için her adımı hesapla.</li>
  <li><strong>Vergi öncesi - vergi sonrası tip.</strong> Konvansiyon ülke ve mekana göre değişir. Araç girdiğin değerin yüzdesini hesaplar — temel olarak hangi değeri istediğini seç.</li>
  <li><strong>Yuvarlama.</strong> Çıktı 6 ondalığa yuvarlanır ve sonra kırpılır; yasal/muhasebe hassasiyeti gerekiyorsa (banker's yuvarlama, para birimine özgü kurallar), bu adımı burada değil domain katmanında yap.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Enam perhitungan "persentase" yang berbeda muncul setiap hari dan mudah tertukar: berapa X% dari Y? X adalah berapa persen dari Y? Berapa perubahan antara dua nilai? Terapkan markup atau diskon? Tip atau pajak? Masing-masing adalah formula yang sedikit berbeda, dan tertukar menyebabkan invoice salah, diskon salah, dan review memalukan. Tool ini menjalankan keenamnya berdampingan dengan formula yang dijabarkan, sehingga kamu bisa pilih yang tepat dan double-check perhitungannya.</p>

<h3>Apa yang dilakukan tiap mode</h3>
<ul>
  <li><strong>Berapa X% dari Y</strong> — untuk diskon, komisi, persentase dari total. <em>20% dari 150 → 30</em>.</li>
  <li><strong>X adalah berapa % dari Y</strong> — untuk rasio gaya "score / max". <em>30 dari 150 → 20%</em>.</li>
  <li><strong>% perubahan</strong> — bertanda: positif berarti naik, negatif berarti turun. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Increase / Decrease</strong> — menerapkan penyesuaian persentase ke nilai awal.</li>
  <li><strong>Tip / Tax</strong> — kemudahan untuk menambahkan persentase di atas tagihan.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Perubahan persentase tidak simetris.</strong> Dari 100 → 125 adalah +25%; dari 125 → 100 adalah −20%, bukan −25%. Penyebutnya adalah nilai awal, yang berbeda di setiap arah.</li>
  <li><strong>Menumpuk persentase itu compound.</strong> Kenaikan 20% diikuti penurunan 20% tidak mengembalikan kamu ke awal (1,20 × 0,80 = 0,96, net kerugian 4%). Untuk markup/diskon sekuensial, hitung setiap langkah.</li>
  <li><strong>Tip pre-tax vs post-tax.</strong> Konvensi berbeda menurut negara dan tempat. Tool menghitung persentase dari nilai yang kamu masukkan — pilih nilai mana yang benar-benar kamu mau sebagai base.</li>
  <li><strong>Rounding.</strong> Output dibulatkan ke 6 desimal lalu dipangkas; jika kamu butuh presisi legal/akuntansi (banker's rounding, aturan spesifik mata uang), lakukan langkah itu di domain layer kamu, bukan di sini.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Mọi người sai trong toán phần trăm rất nhiều — đặc biệt khi câu hỏi đảo ngược ("X là bao nhiêu phần trăm của Y" vs "X% của Y là gì"). Tool này có năm calculator phổ biến trong một: của, bao nhiêu %, tăng/giảm, thay đổi, và tip/thuế. Mỗi cái xử lý một câu hỏi phổ biến mà người ta tự hỏi.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>"Giảm giá 30% trên $89 là bao nhiêu?" → của: 30% của 89 = $26.70 (bạn trả $62.30).</li>
  <li>"Tôi đạt 47/60 — đó là điểm gì?" → bao nhiêu %: 47 là 78% của 60.</li>
  <li>"Tăng 15% mỗi năm trong 5 năm — kết quả?" → tăng/giảm xếp chồng.</li>
  <li>"Tip 18% cho hóa đơn $42 chia 3 người" → tip/thuế.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Phần trăm không đảo ngược.</strong> Tăng 20% rồi giảm 20% không phải là cùng giá trị — bạn ở 96%.</li>
  <li><strong>"X% off" so với "X% off, then sales tax"</strong> rất khác. Thuế thường áp lên giá sau giảm.</li>
  <li><strong>Phần trăm số trên 100.</strong> Có thể có ý nghĩa (tăng 150%), nhưng kiểm tra bạn đang đo từ baseline đúng.</li>
</ul>
""",
    },
    "related": ["number-base-converter", "timestamp-converter", "json-formatter"],
    "howto": {"flow": "calculate", "action": "format",  "noun": "percentage"},
}
