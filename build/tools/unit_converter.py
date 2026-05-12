TOOL = {
    "slug": "unit-converter",
    "category": "math",
    "icon": "📐",
    "tags": ["unit", "convert", "length", "weight", "temperature", "volume", "area", "metric", "imperial"],
    "i18n": {
        "en": {
            "name": "Unit Converter",
            "tagline": "Convert between metric and imperial units of length, weight, temperature, volume, and area.",
            "description": "Free online unit converter. Convert length (mm, cm, m, km, in, ft, yd, mi), weight (g, kg, lb, oz), temperature (C, F, K), volume (mL, L, gal, fl oz), and area (m², ft², acre, ha).",
        },
        "de": {"name": "Einheitenrechner", "tagline": "Konvertiere zwischen metrischen und imperialen Einheiten für Länge, Gewicht, Temperatur, Volumen und Fläche.", "description": "Kostenloser Einheitenrechner. Konvertiere Länge, Gewicht, Temperatur, Volumen und Fläche zwischen metrischen und imperialen Einheiten."},
        "es": {"name": "Conversor de Unidades", "tagline": "Convierte entre unidades métricas e imperiales de longitud, peso, temperatura, volumen y área.", "description": "Conversor gratuito de unidades. Convierte longitud, peso, temperatura, volumen y área entre unidades métricas e imperiales."},
        "fr": {"name": "Convertisseur d'Unités", "tagline": "Convertissez entre unités métriques et impériales de longueur, poids, température, volume et surface.", "description": "Convertisseur d'unités gratuit. Conversion entre unités métriques et impériales de longueur, poids, température, volume et surface."},
        "it": {"name": "Convertitore di Unità", "tagline": "Converti tra unità metriche e imperiali di lunghezza, peso, temperatura, volume e area.", "description": "Convertitore di unità gratuito. Conversione tra unità metriche e imperiali di lunghezza, peso, temperatura, volume e area."},
        "pt": {"name": "Conversor de Unidades", "tagline": "Converta entre unidades métricas e imperiais de comprimento, peso, temperatura, volume e área.", "description": "Conversor de unidades online gratuito. Converta comprimento (mm, cm, m, km, in, ft, yd, mi), peso (g, kg, lb, oz), temperatura (C, F, K), volume (mL, L, gal, fl oz) e área (m², ft², acre, ha)."},
        "pl": {"name": "Konwerter Jednostek", "tagline": "Konwertuj między metrycznymi i imperialnymi jednostkami długości, wagi, temperatury, objętości i powierzchni.", "description": "Darmowy online konwerter jednostek. Konwertuj długość (mm, cm, m, km, in, ft, yd, mi), wagę (g, kg, lb, oz), temperaturę (C, F, K), objętość (mL, L, gal, fl oz) i powierzchnię (m², ft², acre, ha)."},
        "ja": {"name": "単位変換ツール", "tagline": "メートル法とヤード・ポンド法の長さ、重さ、温度、体積、面積を相互変換。", "description": "オンライン無料の単位変換ツール。長さ（mm、cm、m、km、in、ft、yd、mi）、重さ（g、kg、lb、oz）、温度（C、F、K）、体積（mL、L、gal、fl oz）、面積（m²、ft²、acre、ha）を相互変換できます。"},
        "nl": {"name": "Unit Converter", "tagline": "Converteer tussen metrische en imperiale eenheden van lengte, gewicht, temperatuur, volume en oppervlakte.", "description": "Gratis online unit-converter. Converteer lengte (mm, cm, m, km, in, ft, yd, mi), gewicht (g, kg, lb, oz), temperatuur (C, F, K), volume (mL, L, gal, fl oz) en oppervlakte (m², ft², acre, ha)."},
        "tr": {"name": "Birim Dönüştürücü", "tagline": "Uzunluk, ağırlık, sıcaklık, hacim ve alan için metrik ve imperial birimler arasında dönüştür.", "description": "Ücretsiz online birim dönüştürücü. Uzunluk (mm, cm, m, km, in, ft, yd, mi), ağırlık (g, kg, lb, oz), sıcaklık (C, F, K), hacim (mL, L, gal, fl oz) ve alan (m², ft², acre, ha) dönüşümleri."},
        "id": {"name": "Konverter Satuan", "tagline": "Konversi antara satuan metrik dan imperial untuk panjang, berat, suhu, volume, dan luas.", "description": "Konverter satuan gratis. Konversi antara satuan metrik dan imperial untuk panjang (mm, cm, m, km, in, ft, yd, mi), berat (g, kg, oz, lb), suhu (°C, °F, K), volume, dan luas."},
        "vi": {"name": "Chuyển đổi Đơn vị", "tagline": "Chuyển giữa đơn vị mét và imperial cho chiều dài, trọng lượng, nhiệt độ, thể tích và diện tích.", "description": "Bộ chuyển đổi đơn vị miễn phí trực tuyến giữa hệ mét và imperial cho chiều dài, trọng lượng, nhiệt độ, thể tích và diện tích. Xử lý các đơn vị thường dùng (mét/feet, kg/lb, °C/°F, lít/gallon, m²/ft²) với độ chính xác đầy đủ."},
    },
    "body": """
<div class="tool-card">
  <label>Category</label>
  <select id="uc-cat" onchange="ucCatChanged(); ucRun()">
    <option value="length">Length</option>
    <option value="weight">Weight</option>
    <option value="temperature">Temperature</option>
    <option value="volume">Volume</option>
    <option value="area">Area</option>
    <option value="time">Time</option>
    <option value="speed">Speed</option>
  </select>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>{LBL_FROM}</label>
      <div class="uc-row">
        <input type="number" id="uc-in" value="1" oninput="ucRun()" step="any" style="font-family:ui-monospace,monospace">
        <select id="uc-from" onchange="ucRun()"></select>
      </div>
    </div>
    <div>
      <label>{LBL_TO}</label>
      <div class="uc-row">
        <input type="text" id="uc-out" readonly style="font-family:ui-monospace,monospace;background:var(--bg-elev)">
        <select id="uc-to" onchange="ucRun()"></select>
      </div>
    </div>
  </div>
  <div class="button-row" style="margin-top:0.6rem">
    <button class="secondary" onclick="ucSwap()">⇄ {LBL_SWAP}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <pre class="output" id="uc-summary">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<style>
.uc-row{display:flex;gap:0.5rem;align-items:center}
.uc-row input{flex:1}
.uc-row select{flex:0 0 130px}
</style>
<script>
// All units defined as a factor relative to a base. For temperature, use functions.
const UC = {
  length: {
    base: 'm',
    units: {
      mm:0.001, cm:0.01, m:1, km:1000,
      in:0.0254, ft:0.3048, yd:0.9144, mi:1609.344,
      'nautical mi':1852
    }
  },
  weight: {
    base: 'kg',
    units: {
      mg:0.000001, g:0.001, kg:1, t:1000,
      oz:0.028349523125, lb:0.45359237, st:6.35029318
    }
  },
  temperature: {
    base: 'K',
    fns: {
      C: { to: c => c + 273.15, from: k => k - 273.15 },
      F: { to: f => (f - 32) * 5/9 + 273.15, from: k => (k - 273.15) * 9/5 + 32 },
      K: { to: k => k, from: k => k }
    }
  },
  volume: {
    base: 'L',
    units: {
      mL:0.001, L:1, m3:1000,
      'tsp (US)':0.00492892, 'tbsp (US)':0.0147868, 'fl oz (US)':0.0295735,
      cup:0.236588, 'pint (US)':0.473176, 'quart (US)':0.946353, 'gal (US)':3.78541,
      'gal (UK)':4.54609, 'pint (UK)':0.568261
    }
  },
  area: {
    base: 'm2',
    units: {
      mm2:0.000001, cm2:0.0001, m2:1, ha:10000, km2:1000000,
      in2:0.00064516, ft2:0.092903, yd2:0.836127, acre:4046.8564, mi2:2589988.11
    }
  },
  time: {
    base: 's',
    units: {
      ms:0.001, s:1, min:60, h:3600, day:86400, week:604800,
      month:2629800,  // average
      year:31557600
    }
  },
  speed: {
    base: 'm/s',
    units: {
      'm/s':1, 'km/h':1/3.6, 'mph':0.44704, 'ft/s':0.3048, 'knot':0.514444
    }
  }
};
function ucPopulate(){
  const cat = document.getElementById('uc-cat').value;
  const def = UC[cat];
  const labels = def.units ? Object.keys(def.units) : Object.keys(def.fns);
  for(const id of ['uc-from','uc-to']){
    const sel = document.getElementById(id);
    sel.innerHTML = labels.map(l => `<option value="${l}">${l}</option>`).join('');
  }
}
function ucCatChanged(){
  const cat = document.getElementById('uc-cat').value;
  ucPopulate();
  if(cat === 'temperature'){
    document.getElementById('uc-from').value = 'C';
    document.getElementById('uc-to').value = 'F';
  } else if(cat === 'length'){
    document.getElementById('uc-from').value = 'm';
    document.getElementById('uc-to').value = 'ft';
  } else if(cat === 'weight'){
    document.getElementById('uc-from').value = 'kg';
    document.getElementById('uc-to').value = 'lb';
  } else if(cat === 'volume'){
    document.getElementById('uc-from').value = 'L';
    document.getElementById('uc-to').value = 'gal (US)';
  } else if(cat === 'area'){
    document.getElementById('uc-from').value = 'm2';
    document.getElementById('uc-to').value = 'ft2';
  } else if(cat === 'time'){
    document.getElementById('uc-from').value = 'h';
    document.getElementById('uc-to').value = 'min';
  } else if(cat === 'speed'){
    document.getElementById('uc-from').value = 'km/h';
    document.getElementById('uc-to').value = 'mph';
  }
}
function ucConvert(val, from, to){
  const cat = document.getElementById('uc-cat').value;
  const def = UC[cat];
  if(def.fns){
    const baseVal = def.fns[from].to(val);
    return def.fns[to].from(baseVal);
  } else {
    return val * def.units[from] / def.units[to];
  }
}
function ucFmt(n){
  if(!isFinite(n)) return '—';
  const a = Math.abs(n);
  if(a !== 0 && (a >= 1e6 || a < 1e-3)) return n.toExponential(4);
  return Number(n.toFixed(6)).toString();
}
function ucSwap(){
  const f = document.getElementById('uc-from'), t = document.getElementById('uc-to');
  [f.value, t.value] = [t.value, f.value];
  ucRun();
}
function ucRun(){
  const v = parseFloat(document.getElementById('uc-in').value);
  if(isNaN(v)){ document.getElementById('uc-out').value = ''; document.getElementById('uc-summary').textContent = '{LBL_NO_INPUT}'; return; }
  const f = document.getElementById('uc-from').value;
  const t = document.getElementById('uc-to').value;
  const r = ucConvert(v, f, t);
  document.getElementById('uc-out').value = ucFmt(r);
  // Show a few common targets too
  const cat = document.getElementById('uc-cat').value;
  const def = UC[cat];
  const labels = def.units ? Object.keys(def.units) : Object.keys(def.fns);
  const lines = labels.map(l => `  ${ucFmt(ucConvert(v, f, l)).padStart(15)} ${l}`);
  document.getElementById('uc-summary').textContent = `${ucFmt(v)} ${f} =\\n${lines.join('\\n')}`;
}
document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(() => { ucCatChanged(); ucRun(); }));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Most of the world is metric, the US is imperial, the UK is half-and-half, recipes are in cups when they should be in grams, and somewhere in the middle a kid's school project asks for "5 yards in centimetres". This tool runs the conversions for length, weight, temperature, volume, area, time, and speed using high-precision definitions — and spreads the result across every unit in the category at once, so you don't have to convert twice.</p>

<h3>When to use it</h3>
<ul>
  <li>Reading a recipe in cups when you cook in grams (or vice versa).</li>
  <li>Translating a flight distance in nautical miles into kilometres.</li>
  <li>Converting an outdoor-temperature forecast from °C to °F before travel.</li>
  <li>Sizing a piece of furniture: 72 inches wide → will it fit through a 1.9 m doorway?</li>
  <li>Reading scientific paper measurements in SI when you think in imperial.</li>
</ul>

<h3>What's accurate, and what isn't</h3>
<ul>
  <li><strong>Length, weight, temperature, area, speed</strong> use the SI definitions and the international yard-and-pound agreement (1959), so they're precise to the precision your input has.</li>
  <li><strong>Volume</strong> can be fiddly: a US "gallon" (3.785 L) and a UK "imperial gallon" (4.546 L) are different. The tool labels which is which.</li>
  <li><strong>Cup / tablespoon / teaspoon</strong> default to US measure here. UK and Australian cups are slightly different (250 mL in AU, 240 mL in US).</li>
  <li><strong>"Month" and "year"</strong> in the time category use averages (30.44 days / 365.25 days). Don't use this for legal or accounting calculations where exact months matter — use a date calculator instead.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Temperature is not a ratio.</strong> 0°C is not "no temperature" — it's a reference point. Doubling Celsius doesn't double the heat. The conversion uses the additive offsets (273.15 to/from Kelvin, 32 between C and F) which is why the tool uses functions for temperature, not multipliers.</li>
  <li><strong>US vs UK fluid ounces are different.</strong> 1 US fl oz = 29.57 mL, 1 UK fl oz = 28.41 mL. Always check which standard a recipe uses.</li>
  <li><strong>"Tonne" vs "ton".</strong> Metric tonne = 1000 kg. US short ton = 907 kg. UK long ton = 1016 kg. The tool's "t" is the metric tonne.</li>
  <li><strong>Mass vs weight.</strong> Strictly, kg is mass and pounds are mass too (despite the colloquial "I weigh 70 kg"). The tool treats them as a mass-to-mass conversion. For force (newtons, pound-force), you need a different category.</li>
  <li><strong>Round at the end, not the middle.</strong> Don't convert m → ft, round, then ft → in — accumulate errors. Go straight to the target unit.</li>
  <li><strong>Stones &amp; pounds.</strong> A British weight: 1 stone = 14 lb. The tool has stone (st) but you'll need to do the lb portion separately for "11 st 4 lb"-style entries.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>A maior parte do mundo usa o sistema métrico, os EUA usam o imperial, o Reino Unido mistura os dois, receitas vêm em xícaras quando deveriam estar em gramas, e em algum momento o trabalho escolar do seu filho pede "5 jardas em centímetros". Esta ferramenta faz as conversões para comprimento, peso, temperatura, volume, área, tempo e velocidade usando definições de alta precisão — e mostra o resultado em todas as unidades da categoria de uma vez, para você não ter que converter duas vezes.</p>

<h3>Quando usar</h3>
<ul>
  <li>Lendo uma receita em xícaras quando você cozinha em gramas (ou vice-versa).</li>
  <li>Convertendo a distância de um voo em milhas náuticas para quilômetros.</li>
  <li>Convertendo uma previsão de temperatura externa de °C para °F antes de viajar.</li>
  <li>Medindo um móvel: 72 polegadas de largura → cabe numa porta de 1,9 m?</li>
  <li>Lendo medidas em SI de um artigo científico quando você pensa em imperial.</li>
</ul>

<h3>O que é preciso e o que não é</h3>
<ul>
  <li><strong>Comprimento, peso, temperatura, área, velocidade</strong> usam as definições do SI e o acordo internacional de jarda e libra (1959), então são precisos até a precisão da sua entrada.</li>
  <li><strong>Volume</strong> pode ser complicado: um "gallon" americano (3,785 L) e um "imperial gallon" britânico (4,546 L) são diferentes. A ferramenta indica qual é qual.</li>
  <li><strong>Cup / tablespoon / teaspoon</strong> usam por padrão a medida americana aqui. Xícaras britânicas e australianas são ligeiramente diferentes (250 mL na AU, 240 mL nos EUA).</li>
  <li><strong>"Mês" e "ano"</strong> na categoria tempo usam médias (30,44 dias / 365,25 dias). Não use isto para cálculos jurídicos ou contábeis em que meses exatos importam — use uma calculadora de datas.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Temperatura não é uma razão.</strong> 0°C não é "ausência de temperatura" — é um ponto de referência. Dobrar Celsius não dobra o calor. A conversão usa os deslocamentos aditivos (273,15 de/para Kelvin, 32 entre C e F) — por isso a ferramenta usa funções para temperatura, e não multiplicadores.</li>
  <li><strong>Fluid ounces dos EUA e do Reino Unido são diferentes.</strong> 1 US fl oz = 29,57 mL, 1 UK fl oz = 28,41 mL. Sempre verifique qual padrão a receita usa.</li>
  <li><strong>"Tonne" vs "ton".</strong> Tonelada métrica = 1000 kg. Short ton (EUA) = 907 kg. Long ton (UK) = 1016 kg. O "t" da ferramenta é a tonelada métrica.</li>
  <li><strong>Massa vs peso.</strong> Estritamente, kg é massa e libras também são massa (apesar do coloquial "eu peso 70 kg"). A ferramenta trata como conversão de massa para massa. Para força (newtons, pound-force), você precisa de outra categoria.</li>
  <li><strong>Arredonde no fim, não no meio.</strong> Não converta m → ft, arredonde, e depois ft → in — você acumula erros. Vá direto para a unidade alvo.</li>
  <li><strong>Stones &amp; pounds.</strong> Uma medida britânica de peso: 1 stone = 14 lb. A ferramenta tem stone (st), mas você terá que fazer a parte das lb separadamente para entradas no estilo "11 st 4 lb".</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Większość świata jest metryczna, USA jest imperialne, UK jest pół na pół, przepisy są w cupach, kiedy powinny być w gramach, a gdzieś pomiędzy szkolny projekt dziecka pyta o "5 yardów w centymetrach". To narzędzie liczy konwersje długości, wagi, temperatury, objętości, powierzchni, czasu i prędkości używając wysokiej precyzji definicji — i rozkłada wynik na każdą jednostkę kategorii naraz, żebyś nie musiał konwertować dwa razy.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Czytanie przepisu w cupach, gdy gotujesz w gramach (albo na odwrót).</li>
  <li>Tłumaczenie odległości lotu w milach morskich na kilometry.</li>
  <li>Konwersja prognozy temperatury z °C na °F przed podróżą.</li>
  <li>Wymiarowanie mebla: 72 cale szerokości → zmieści się w drzwiach 1,9 m?</li>
  <li>Czytanie pomiarów z papera naukowego w SI, gdy myślisz w imperialnym.</li>
</ul>

<h3>Co jest dokładne, a co nie</h3>
<ul>
  <li><strong>Długość, waga, temperatura, powierzchnia, prędkość</strong> używają definicji SI i międzynarodowego porozumienia yard-and-pound (1959), więc są dokładne do precyzji twojego wejścia.</li>
  <li><strong>Objętość</strong> bywa upierdliwa: amerykański "gallon" (3,785 L) i brytyjski "imperial gallon" (4,546 L) to różne rzeczy. Narzędzie podaje, który jest który.</li>
  <li><strong>Cup / tablespoon / teaspoon</strong> domyślnie są tu w mierze amerykańskiej. Brytyjskie i australijskie cupy są lekko inne (250 mL w AU, 240 mL w US).</li>
  <li><strong>"Miesiąc" i "rok"</strong> w kategorii czasu używają średnich (30,44 dnia / 365,25 dnia). Nie używaj tego do prawnych albo księgowych obliczeń, gdzie liczą się dokładne miesiące — użyj kalkulatora dat.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Temperatura nie jest stosunkiem.</strong> 0°C to nie "brak temperatury" — to punkt odniesienia. Podwojenie Celsjuszy nie podwaja ciepła. Konwersja używa addytywnych przesunięć (273,15 do/z Kelvinów, 32 między C a F) — dlatego narzędzie używa funkcji do temperatury, nie mnożników.</li>
  <li><strong>US i UK fluid ounces są różne.</strong> 1 US fl oz = 29,57 mL, 1 UK fl oz = 28,41 mL. Zawsze sprawdzaj, którego standardu używa przepis.</li>
  <li><strong>"Tonne" vs "ton".</strong> Tona metryczna = 1000 kg. US short ton = 907 kg. UK long ton = 1016 kg. "t" w narzędziu to tona metryczna.</li>
  <li><strong>Masa vs waga.</strong> Ściśle, kg to masa, a funty to też masa (mimo potocznego "ważę 70 kg"). Narzędzie traktuje to jako konwersję masa-do-masy. Do siły (newtony, pound-force) potrzeba innej kategorii.</li>
  <li><strong>Zaokrąglaj na końcu, nie w środku.</strong> Nie konwertuj m → ft, zaokrąglaj, potem ft → in — kumulujesz błędy. Idź wprost do docelowej jednostki.</li>
  <li><strong>Stones &amp; pounds.</strong> Brytyjska waga: 1 stone = 14 lb. Narzędzie ma stone (st), ale część w lb musisz zrobić osobno dla wpisów typu "11 st 4 lb".</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>世界の多くはメートル法、米国はヤード・ポンド法、英国は半々、レシピはグラムで欲しいのにカップで書かれていて、子どもの宿題には「5 ヤードを cm で」と出ます。本ツールは長さ、重さ、温度、体積、面積、時間、速度の変換を高精度の定義に基づいて計算し、同一カテゴリ内のすべての単位を一度に表示するため、二度手間の変換が不要です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>レシピがカップ表記なのに、自分はグラムで料理するとき（あるいはその逆）。</li>
  <li>飛行距離の海里をキロメートルに変換したいとき。</li>
  <li>旅行前に屋外気温の予報を °C ↔ °F で見たいとき。</li>
  <li>家具の寸法を比較：72 インチ幅は 1.9 m のドアを通れるか？</li>
  <li>ヤード・ポンドで考えがちな人が論文の SI 単位を読みたいとき。</li>
</ul>

<h3>精度の高いところと注意点</h3>
<ul>
  <li><strong>長さ、重さ、温度、面積、速度</strong> は SI 定義と 1959 年の international yard-and-pound に基づいており、入力精度に従って正確です。</li>
  <li><strong>体積</strong> は厄介。米ガロン（3.785 L）と英 imperial gallon（4.546 L）は別物です。本ツールはどちらかを明示します。</li>
  <li><strong>カップ／テーブルスプーン／ティースプーン</strong> はここでは米計量がデフォルト。英・豪のカップは少し違います（豪 250 mL、米 240 mL）。</li>
  <li><strong>「月」「年」</strong>（時間カテゴリ）は平均値（30.44 日／365.25 日）を用います。法務・会計で正確な月数が必要な場合は、本ツールではなく日付計算を使ってください。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>温度は比率ではありません。</strong> 0°C は「温度なし」ではなく基準点に過ぎず、°C を倍にしても熱量は倍になりません。Kelvin との 273.15 のオフセット、C↔F の 32 のオフセットが加算的に必要なため、温度には倍率ではなく関数を使います。</li>
  <li><strong>米／英の fluid ounce は別物です。</strong> 1 米 fl oz = 29.57 mL、1 英 fl oz = 28.41 mL。レシピがどちらの規格か必ず確認しましょう。</li>
  <li><strong>「tonne」と「ton」。</strong> メトリックトン = 1000 kg、米 short ton = 907 kg、英 long ton = 1016 kg。本ツールの「t」はメトリックトンです。</li>
  <li><strong>質量と重量。</strong> 厳密には kg もポンドも質量です（口語では「体重 70 kg」と言いますが）。本ツールは質量↔質量の変換として扱います。力（ニュートン、pound-force）には別カテゴリが必要です。</li>
  <li><strong>丸めは最後に、途中ではしない。</strong> m → ft で丸めて、さらに ft → in と進めると誤差が積み重なります。直接ターゲット単位に変換してください。</li>
  <li><strong>ストーンとポンド。</strong> 英国の重量で 1 stone = 14 lb。本ツールは stone（st）を持ちますが、「11 st 4 lb」のような表記の lb 部分は別途処理してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Het grootste deel van de wereld is metrisch, de VS is imperiaal, het VK is half-en-half, recepten zijn in cups als ze in grammen hadden moeten zijn, en ergens daartussen vraagt een schoolwerkstuk om "5 yards in centimeters". Deze tool draait de conversies voor lengte, gewicht, temperatuur, volume, oppervlakte, tijd en snelheid met high-precision definities — en spreidt het resultaat tegelijk over elke unit in de categorie, zodat je niet twee keer hoeft te converteren.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een recept in cups lezen als je in grammen kookt (of andersom).</li>
  <li>Een vluchtafstand in nautische mijlen vertalen naar kilometers.</li>
  <li>Een buitentemperatuur-forecast converteren van °C naar °F voor reizen.</li>
  <li>Een meubelstuk meten: 72 inches breed → past het door een deuropening van 1,9 m?</li>
  <li>Wetenschappelijke paper-metingen in SI lezen als je in imperiaal denkt.</li>
</ul>

<h3>Wat accuraat is, en wat niet</h3>
<ul>
  <li><strong>Lengte, gewicht, temperatuur, oppervlakte, snelheid</strong> gebruiken de SI-definities en het international yard-and-pound agreement (1959), dus ze zijn precies tot de precisie die je input heeft.</li>
  <li><strong>Volume</strong> kan gepriegel zijn: een US "gallon" (3,785 L) en een UK "imperial gallon" (4,546 L) zijn verschillend. De tool labelt welke welke is.</li>
  <li><strong>Cup / tablespoon / teaspoon</strong> defaulten hier op US-maat. UK en Australische cups zijn lichtjes anders (250 mL in AU, 240 mL in US).</li>
  <li><strong>"Maand" en "jaar"</strong> in de tijd-categorie gebruiken gemiddelden (30,44 dagen / 365,25 dagen). Gebruik dit niet voor legal- of accounting-berekeningen waar exacte maanden tellen — gebruik in plaats daarvan een datum-calculator.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Temperatuur is geen ratio.</strong> 0°C is geen "geen temperatuur" — het is een referentiepunt. Celsius verdubbelen verdubbelt de hitte niet. De conversie gebruikt de additieve offsets (273,15 naar/van Kelvin, 32 tussen C en F) wat de reden is dat de tool functies gebruikt voor temperatuur, geen multipliers.</li>
  <li><strong>US vs UK fluid ounces zijn verschillend.</strong> 1 US fl oz = 29,57 mL, 1 UK fl oz = 28,41 mL. Check altijd welke standaard een recept gebruikt.</li>
  <li><strong>"Tonne" vs "ton".</strong> Metrische tonne = 1000 kg. US short ton = 907 kg. UK long ton = 1016 kg. De "t" van de tool is de metrische tonne.</li>
  <li><strong>Mass vs weight.</strong> Strikt is kg massa en pounds ook massa (ondanks het spreektalige "ik weeg 70 kg"). De tool behandelt ze als een mass-to-mass conversie. Voor force (newtons, pound-force) heb je een andere categorie nodig.</li>
  <li><strong>Rond af op het einde, niet in het midden.</strong> Niet m → ft, afronden, dan ft → in — fouten stapelen op. Ga rechtstreeks naar de doel-unit.</li>
  <li><strong>Stones &amp; pounds.</strong> Een Brits gewicht: 1 stone = 14 lb. De tool heeft stone (st) maar je moet het lb-gedeelte apart doen voor "11 st 4 lb"-stijl entries.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Dünyanın çoğu metriktir, ABD imperialdir, İngiltere yarı-yarıdır, tarifler gram olması gerektiğinde cup'tadır ve ortada bir yerde bir çocuğun okul projesi "5 yard santimetrede" ister. Bu araç yüksek hassasiyetli tanımlar kullanarak uzunluk, ağırlık, sıcaklık, hacim, alan, zaman ve hız için dönüşümleri çalıştırır — ve sonucu kategorideki her birim üzerine bir kerede yayar, böylece iki kez dönüştürmen gerekmez.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Gram cinsinden pişirdiğinde cup'ta bir tarif okuma (veya tersi).</li>
  <li>Bir uçuş mesafesini deniz mili cinsinden kilometreye çevirme.</li>
  <li>Seyahatten önce dış mekan sıcaklık tahmini °C'den °F'a dönüştürme.</li>
  <li>Bir mobilya parçasını boyutlandırma: 72 inç genişlik → 1,9 m kapıdan geçer mi?</li>
  <li>Imperial düşündüğünde SI'da bilimsel makale ölçümlerini okuma.</li>
</ul>

<h3>Ne doğru, ne değil</h3>
<ul>
  <li><strong>Uzunluk, ağırlık, sıcaklık, alan, hız</strong> SI tanımlarını ve uluslararası yard-and-pound anlaşmasını (1959) kullanır, böylece girdinin sahip olduğu hassasiyete kesindirler.</li>
  <li><strong>Hacim</strong> zahmetli olabilir: ABD "galon" (3,785 L) ve İngiliz "imperial galon" (4,546 L) farklıdır. Araç hangisinin hangisi olduğunu etiketler.</li>
  <li><strong>Cup / yemek kaşığı / çay kaşığı</strong> burada varsayılan olarak ABD ölçüsüdür. İngiliz ve Avustralya cup'ları biraz farklıdır (AU'da 250 mL, ABD'de 240 mL).</li>
  <li><strong>Zaman kategorisinde "ay" ve "yıl"</strong> ortalamalar kullanır (30,44 gün / 365,25 gün). Bunu kesin ayların önemli olduğu yasal veya muhasebe hesaplamaları için kullanma — bunun yerine bir tarih hesaplayıcı kullan.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Sıcaklık bir oran değildir.</strong> 0°C "sıcaklık yok" demek değildir — bir referans noktasıdır. Celsius'u ikiye katlamak ısıyı ikiye katlamaz. Dönüşüm aditif ofsetleri kullanır (Kelvin'e/dan 273,15, C ile F arasında 32) bu yüzden araç sıcaklık için çarpanlar değil fonksiyonlar kullanır.</li>
  <li><strong>ABD ve İngiliz fluid ons'ları farklıdır.</strong> 1 ABD fl oz = 29,57 mL, 1 İngiliz fl oz = 28,41 mL. Bir tarifin hangi standardı kullandığını her zaman kontrol et.</li>
  <li><strong>"Tonne" ve "ton".</strong> Metrik tonne = 1000 kg. ABD kısa ton = 907 kg. İngiliz uzun ton = 1016 kg. Aracın "t"si metrik tonne'dur.</li>
  <li><strong>Kütle - ağırlık.</strong> Kesin olarak, kg kütledir ve pound da kütledir (günlük "70 kg ağırlığım var"a rağmen). Araç bunları kütle-kütle dönüşümü olarak ele alır. Kuvvet (newton, pound-force) için farklı bir kategoriye ihtiyacın var.</li>
  <li><strong>Sonda yuvarla, ortada değil.</strong> m → ft'a çevirme, yuvarlama, sonra ft → in'e çevirme — hatalar birikir. Hedef birime doğru git.</li>
  <li><strong>Stone &amp; pound.</strong> Bir İngiliz ağırlığı: 1 stone = 14 lb. Aracın stone (st) vardır ama "11 st 4 lb" tarzı girişler için lb kısmını ayrı yapman gerekir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Sebagian besar dunia pakai metrik, AS pakai imperial, UK setengah-setengah, resep masakan pakai cup padahal seharusnya gram, dan di suatu tempat di tengah project sekolah anak meminta "5 yard dalam sentimeter". Tool ini menjalankan konversi untuk panjang, berat, suhu, volume, area, waktu, dan kecepatan memakai definisi presisi tinggi — dan menyebar hasilnya ke setiap unit dalam kategori sekaligus, jadi kamu tidak perlu mengkonversi dua kali.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Membaca resep dalam cup ketika kamu memasak dalam gram (atau sebaliknya).</li>
  <li>Menerjemahkan jarak penerbangan dalam nautical mile ke kilometer.</li>
  <li>Mengkonversi prakiraan suhu outdoor dari °C ke °F sebelum bepergian.</li>
  <li>Mengukur sepotong furniture: lebar 72 inci → apakah muat lewat pintu 1,9 m?</li>
  <li>Membaca pengukuran paper ilmiah dalam SI ketika kamu berpikir dalam imperial.</li>
</ul>

<h3>Apa yang akurat, dan apa yang tidak</h3>
<ul>
  <li><strong>Panjang, berat, suhu, area, kecepatan</strong> pakai definisi SI dan international yard-and-pound agreement (1959), jadi presisinya sesuai presisi input kamu.</li>
  <li><strong>Volume</strong> bisa rumit: "gallon" AS (3,785 L) dan "imperial gallon" UK (4,546 L) itu berbeda. Tool memberi label mana yang mana.</li>
  <li><strong>Cup / tablespoon / teaspoon</strong> di sini default ke ukuran AS. Cup UK dan Australia sedikit berbeda (250 mL di AU, 240 mL di US).</li>
  <li><strong>"Bulan" dan "tahun"</strong> di kategori waktu pakai rata-rata (30,44 hari / 365,25 hari). Jangan pakai ini untuk perhitungan legal atau akuntansi di mana bulan eksak penting — pakai date calculator saja.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Suhu bukan rasio.</strong> 0°C bukan "tidak ada suhu" — itu titik referensi. Menggandakan Celsius tidak menggandakan panas. Konversi pakai offset aditif (273,15 ke/dari Kelvin, 32 antara C dan F) — itu sebabnya tool memakai fungsi untuk suhu, bukan multiplier.</li>
  <li><strong>Fluid ounce AS vs UK berbeda.</strong> 1 US fl oz = 29,57 mL, 1 UK fl oz = 28,41 mL. Selalu cek standar mana yang dipakai resep.</li>
  <li><strong>"Tonne" vs "ton".</strong> Metric tonne = 1000 kg. US short ton = 907 kg. UK long ton = 1016 kg. "t" di tool adalah metric tonne.</li>
  <li><strong>Massa vs berat.</strong> Secara ketat, kg itu massa dan pound juga massa (meski sehari-hari "berat saya 70 kg"). Tool memperlakukannya sebagai konversi mass-to-mass. Untuk gaya (newton, pound-force), kamu butuh kategori berbeda.</li>
  <li><strong>Bulatkan di akhir, bukan di tengah.</strong> Jangan konversi m → ft, bulatkan, lalu ft → in — error akan akumulasi. Langsung ke unit target.</li>
  <li><strong>Stone &amp; pound.</strong> Berat Inggris: 1 stone = 14 lb. Tool punya stone (st) tapi kamu perlu melakukan bagian lb secara terpisah untuk entry gaya "11 st 4 lb".</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Đa số thế giới đo theo hệ mét; Mỹ, Liberia và Myanmar dùng hệ imperial. Khi đọc tài liệu, công thức nấu ăn hoặc dữ liệu từ nguồn không quen thuộc, bạn cần chuyển đổi. Tool này chuyển giữa các đơn vị thông thường trong sáu trục: chiều dài, trọng lượng, nhiệt độ, thể tích, diện tích.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Đọc tài liệu API quốc tế với mét và bạn cần feet.</li>
  <li>Công thức nấu ăn ngoại quốc với gram và bạn nghĩ theo cup.</li>
  <li>Mua đất hoặc nhà với hectare ở một nước và acre ở nước khác.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Nhiệt độ không phải scale tuyến tính qua zero.</strong> 0°C ≠ 0°F. 0K (Kelvin) là không tuyệt đối, -273.15°C.</li>
  <li><strong>Imperial fluid ounce ≠ US fluid ounce.</strong> UK pint là 568 mL; US pint là 473 mL. Đáng nhớ khi pha cocktail từ công thức.</li>
  <li><strong>Mass vs weight.</strong> Kilogram là đơn vị khối lượng; pound đo lực ở Trái đất bình thường. Trên Mặt trăng, kilogram cùng, pound khác.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "timezone-converter", "percentage-calculator"],
    "howto": {"flow": "calculate", "action": "convert", "noun": "unit"},
}
