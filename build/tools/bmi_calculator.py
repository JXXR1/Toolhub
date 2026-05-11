TOOL = {
    "slug": "bmi-calculator",
    "category": "math",
    "icon": "⚖️",
    "tags": ["bmi", "body mass index", "health", "weight", "height", "metric", "imperial"],
    "i18n": {
        "en": {
            "name": "BMI Calculator",
            "tagline": "Body Mass Index from height and weight. Metric or imperial. Shows the WHO category — not medical advice.",
            "description": "Free Body Mass Index calculator. Enter height and weight in metric (cm + kg) or imperial (feet/inches + pounds) and see the BMI value plus the WHO classification (underweight, normal, overweight, obese). Educational only — not medical advice.",
        },
        "de": {"name": "BMI-Rechner", "tagline": "Body-Mass-Index aus Größe und Gewicht. Metrisch oder imperial. WHO-Kategorie wird angezeigt — keine medizinische Beratung.", "description": "Kostenloser Body-Mass-Index-Rechner. Größe und Gewicht in metrisch (cm + kg) oder imperial (Fuß/Zoll + Pfund) eingeben und BMI-Wert sowie WHO-Klassifikation sehen. Nur zur Information — keine medizinische Beratung."},
        "es": {"name": "Calculadora de IMC", "tagline": "Índice de Masa Corporal a partir de altura y peso. Métrico o imperial. Categoría OMS — no es consejo médico.", "description": "Calculadora gratuita de IMC. Introduce altura y peso en métrico (cm + kg) o imperial (pies/pulgadas + libras) y obtén el IMC y la clasificación de la OMS. Solo educativo — no es consejo médico."},
        "fr": {"name": "Calculateur d'IMC", "tagline": "Indice de Masse Corporelle à partir de la taille et du poids. Métrique ou impérial. Catégorie OMS — pas un avis médical.", "description": "Calculateur d'IMC gratuit. Saisissez la taille et le poids en métrique (cm + kg) ou impérial (pieds/pouces + livres) et obtenez l'IMC plus la classification OMS. À titre informatif — pas un avis médical."},
        "it": {"name": "Calcolatore BMI", "tagline": "Indice di Massa Corporea da altezza e peso. Metrico o imperiale. Categoria OMS — non è un consiglio medico.", "description": "Calcolatore BMI gratuito. Inserisci altezza e peso in metrico (cm + kg) o imperiale (piedi/pollici + libbre) e ottieni il BMI e la classificazione OMS. Solo informativo — non un consiglio medico."},
        "pt": {"name": "Calculadora de IMC", "tagline": "Índice de Massa Corporal a partir de altura e peso. Métrico ou imperial. Mostra a categoria da OMS — não é orientação médica.", "description": "Calculadora gratuita de Índice de Massa Corporal. Informe altura e peso em métrico (cm + kg) ou imperial (pés/polegadas + libras) e veja o valor de IMC mais a classificação da OMS (abaixo do peso, normal, sobrepeso, obesidade). Apenas educacional — não é orientação médica."},
        "pl": {"name": "Kalkulator BMI", "tagline": "Wskaźnik masy ciała z wzrostu i wagi. Metryczny lub imperialny. Pokazuje kategorię WHO — nie jest poradą medyczną.", "description": "Darmowy kalkulator BMI (Body Mass Index). Wpisz wzrost i wagę w jednostkach metrycznych (cm + kg) albo imperialnych (stopy/cale + funty) i zobacz wartość BMI oraz klasyfikację WHO (niedowaga, prawidłowa, nadwaga, otyłość). Tylko cele edukacyjne — nie jest poradą medyczną."},
        "ja": {"name": "BMI 計算機", "tagline": "身長と体重から BMI を計算。メートル法・ヤード・ポンド法対応。WHO 区分を表示 — 医療助言ではありません。", "description": "無料の BMI（体格指数）計算ツール。身長と体重をメートル法（cm + kg）またはヤード・ポンド法（フィート/インチ + ポンド）で入力すると、BMI 値と WHO 分類（低体重・標準・肥満気味・肥満）が表示されます。教育目的のみで、医療助言ではありません。"},
        "nl": {"name": "BMI-calculator", "tagline": "Body Mass Index uit lengte en gewicht. Metrisch of imperiaal. Toont de WHO-categorie — geen medisch advies.", "description": "Gratis Body Mass Index-calculator. Voer lengte en gewicht in metrisch (cm + kg) of imperiaal (feet/inches + pounds) in en zie de BMI-waarde plus de WHO-classificatie (ondergewicht, normaal, overgewicht, obesitas). Alleen educatief — geen medisch advies."},
        "tr": {"name": "BMI Hesaplayıcı", "tagline": "Boy ve kilodan vücut kitle indeksi. Metrik veya imperial. DSÖ kategorisini gösterir — tıbbi tavsiye değildir.", "description": "Ücretsiz vücut kitle indeksi hesaplayıcı. Boy ve kiloyu metrik (cm + kg) veya imperial (feet/inç + pound) gir; BMI değeri ve DSÖ sınıflandırmasını (zayıf, normal, fazla kilolu, obez) gör. Sadece bilgilendirme amaçlıdır — tıbbi tavsiye değildir."},
    },
    "body": """
<div class="tool-card">
  <label>Units</label>
  <select id="bmi-units" onchange="bmiSwitch()">
    <option value="metric">Metric — cm and kg</option>
    <option value="imperial">Imperial — feet/inches and pounds</option>
  </select>
</div>
<div class="tool-card" id="bmi-metric">
  <div class="row-2col">
    <div>
      <label>Height (cm)</label>
      <input type="number" id="bmi-cm" step="0.1" min="50" max="280" value="175" oninput="bmiRun()">
    </div>
    <div>
      <label>Weight (kg)</label>
      <input type="number" id="bmi-kg" step="0.1" min="10" max="400" value="70" oninput="bmiRun()">
    </div>
  </div>
</div>
<div class="tool-card" id="bmi-imperial" style="display:none">
  <div class="row-2col">
    <div>
      <label>Height (feet)</label>
      <input type="number" id="bmi-ft" step="1" min="1" max="8" value="5" oninput="bmiRun()">
    </div>
    <div>
      <label>Height (inches)</label>
      <input type="number" id="bmi-in" step="0.1" min="0" max="11.9" value="9" oninput="bmiRun()">
    </div>
  </div>
  <div style="margin-top:0.7rem">
    <label>Weight (pounds)</label>
    <input type="number" id="bmi-lb" step="0.1" min="20" max="900" value="155" oninput="bmiRun()">
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="bmi-out" class="output"></div>
</div>
""",
    "script": """
<style>
.bmi-num{font-family:ui-monospace,monospace;font-size:2.4rem;font-weight:700;color:var(--accent);text-align:center;margin:0.2rem 0}
.bmi-cat{text-align:center;font-size:1.05rem;font-weight:600;padding:0.4rem 0.8rem;border-radius:6px;display:inline-block;margin:0 auto;display:block;width:fit-content}
.bmi-c-under{background:rgba(88,166,255,0.15);color:#58a6ff;border:1px solid rgba(88,166,255,0.4)}
.bmi-c-normal{background:rgba(63,185,80,0.15);color:#3fb950;border:1px solid rgba(63,185,80,0.4)}
.bmi-c-over{background:rgba(247,147,30,0.15);color:#f7931e;border:1px solid rgba(247,147,30,0.4)}
.bmi-c-obese{background:rgba(248,81,73,0.15);color:#f85149;border:1px solid rgba(248,81,73,0.4)}
.bmi-bar{margin-top:1rem;height:14px;border-radius:7px;background:linear-gradient(to right,#58a6ff 0%,#58a6ff 18.5%,#3fb950 18.5%,#3fb950 25%,#f7931e 25%,#f7931e 30%,#f85149 30%,#f85149 100%);position:relative}
.bmi-marker{position:absolute;top:-4px;width:4px;height:22px;background:var(--text);border-radius:2px}
.bmi-scale{display:grid;grid-template-columns:repeat(4,1fr);font-size:0.72rem;color:var(--text-muted);margin-top:0.3rem;font-family:ui-monospace,monospace}
.bmi-scale span:nth-child(2),.bmi-scale span:nth-child(3),.bmi-scale span:nth-child(4){text-align:center}
.bmi-scale span:last-child{text-align:right}
.bmi-disclaimer{margin-top:0.8rem;font-size:0.78rem;color:var(--text-muted);text-align:center;font-style:italic}
.bmi-extras{margin-top:0.7rem;font-size:0.85rem;color:var(--text-muted);text-align:center;font-family:ui-monospace,monospace}
</style>
<script>
function bmiSwitch(){
  const u = document.getElementById('bmi-units').value;
  document.getElementById('bmi-metric').style.display = u === 'metric' ? '' : 'none';
  document.getElementById('bmi-imperial').style.display = u === 'imperial' ? '' : 'none';
  bmiRun();
}
function bmiCat(b){
  if(b < 18.5) return ['Underweight', 'bmi-c-under'];
  if(b < 25) return ['Normal weight', 'bmi-c-normal'];
  if(b < 30) return ['Overweight', 'bmi-c-over'];
  if(b < 35) return ['Obese (Class I)', 'bmi-c-obese'];
  if(b < 40) return ['Obese (Class II)', 'bmi-c-obese'];
  return ['Obese (Class III)', 'bmi-c-obese'];
}
function bmiRun(){
  const u = document.getElementById('bmi-units').value;
  let m, kg;
  if(u === 'metric'){
    const cm = parseFloat(document.getElementById('bmi-cm').value);
    kg = parseFloat(document.getElementById('bmi-kg').value);
    if(!isFinite(cm) || cm <= 0 || !isFinite(kg) || kg <= 0){ document.getElementById('bmi-out').textContent = '{LBL_NO_INPUT}'; return; }
    m = cm / 100;
  } else {
    const ft = parseFloat(document.getElementById('bmi-ft').value) || 0;
    const inch = parseFloat(document.getElementById('bmi-in').value) || 0;
    const lb = parseFloat(document.getElementById('bmi-lb').value);
    if(ft <= 0 && inch <= 0){ document.getElementById('bmi-out').textContent = '{LBL_NO_INPUT}'; return; }
    if(!isFinite(lb) || lb <= 0){ document.getElementById('bmi-out').textContent = '{LBL_NO_INPUT}'; return; }
    m = (ft * 12 + inch) * 0.0254;
    kg = lb * 0.45359237;
  }
  if(m <= 0){ document.getElementById('bmi-out').textContent = '{LBL_NO_INPUT}'; return; }
  const bmi = kg / (m * m);
  const [cat, cls] = bmiCat(bmi);
  // Marker on 0–40 scale
  const pct = Math.max(0, Math.min(100, (bmi / 40) * 100));
  // Healthy range in current units
  const lowKg = 18.5 * m * m;
  const highKg = 24.9 * m * m;
  let rangeStr;
  if(u === 'metric'){
    rangeStr = `Healthy weight range: ${lowKg.toFixed(1)} – ${highKg.toFixed(1)} kg`;
  } else {
    rangeStr = `Healthy weight range: ${(lowKg/0.45359237).toFixed(1)} – ${(highKg/0.45359237).toFixed(1)} lb`;
  }
  document.getElementById('bmi-out').innerHTML = `
    <div class="bmi-num">${bmi.toFixed(1)}</div>
    <div class="bmi-cat ${cls}">${cat}</div>
    <div class="bmi-bar"><div class="bmi-marker" style="left:calc(${pct}% - 2px)"></div></div>
    <div class="bmi-scale"><span>0</span><span>18.5</span><span>25</span><span>30</span></div>
    <div class="bmi-extras">${rangeStr}</div>
    <div class="bmi-disclaimer">BMI is a population-level screening figure. It does not account for muscle mass, body composition, age, ethnicity, or pregnancy. Speak to a clinician for a real assessment.</div>
  `;
}
document.addEventListener('DOMContentLoaded', bmiRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Body Mass Index (BMI) is a single number — weight in kilograms divided by the square of height in metres — used by the World Health Organization and many health systems as a quick screen for body-weight categories. It's not diagnostic; it's a flag. The classic adult thresholds are: under 18.5 underweight, 18.5–24.9 normal, 25–29.9 overweight, 30 and over obese (split into Class I/II/III at 35 and 40). This tool computes the value and the category from height and weight in metric or imperial.</p>

<h3>How it's calculated</h3>
<ul>
  <li><strong>Metric:</strong> BMI = kg ÷ (m × m). 70 kg at 1.75 m → 70 / 3.0625 = 22.9.</li>
  <li><strong>Imperial:</strong> BMI = (lb × 703) ÷ (in × in). The tool converts to metric internally for accuracy.</li>
  <li>The WHO categories are the same regardless of unit system — BMI itself is unitless.</li>
</ul>

<h3>When to use it</h3>
<ul>
  <li>Quick self-check or to fill in a form that asks for it (insurance, fitness apps, gym intake).</li>
  <li>Comparing a value across populations or studies.</li>
  <li>Tracking direction of change over time (rising, stable, falling) — the trend is more useful than any single reading.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>BMI does not measure body composition.</strong> Muscle weighs more than fat, so a fit, muscular person can score "overweight" while having low body-fat. Conversely, a low-muscle person can score "normal" while being unhealthy ("skinny fat").</li>
  <li><strong>It's an adult metric.</strong> For children and adolescents (under 18) use the age- and sex-specific BMI percentile charts instead.</li>
  <li><strong>Pregnancy isn't supported.</strong> BMI doesn't apply during pregnancy; talk to your healthcare provider.</li>
  <li><strong>Ethnicity matters.</strong> Several health bodies (NHS, WHO Asia-Pacific guidance) use lower thresholds (overweight ≥23, obese ≥27.5) for South Asian, Chinese, and other groups, because cardiovascular risk rises at lower BMIs.</li>
  <li><strong>Tall vs short people.</strong> The squared-height formula systematically over-classifies tall people as "underweight" and short people as "overweight" — alternative formulas (Trefethen's BMI uses height^2.5) try to correct for this.</li>
  <li><strong>Not medical advice.</strong> If you're concerned about your weight, talk to a clinician. They have the rest of the picture (waist circumference, blood pressure, blood-work, lifestyle) that a single number doesn't.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Der Body-Mass-Index (BMI) ist eine einzige Zahl — Gewicht (kg) geteilt durch das Quadrat der Größe (m) — die WHO und viele Gesundheitssysteme als Screening verwenden. Adulte Schwellen: unter 18,5 untergewichtig, 18,5–24,9 normal, 25–29,9 übergewichtig, ab 30 adipös. Dieses Tool berechnet Wert und Kategorie aus Größe und Gewicht in metrisch oder imperial.</p>
<h3>Wie wird er berechnet</h3>
<ul>
<li><strong>Metrisch:</strong> BMI = kg ÷ (m × m). 70 kg bei 1,75 m → 22,9.</li>
<li><strong>Imperial:</strong> Wird intern zur Genauigkeit in metrisch umgerechnet.</li>
<li>Die WHO-Kategorien sind systemunabhängig — BMI ist einheitenlos.</li>
</ul>
<h3>Wann verwenden</h3>
<ul>
<li>Schneller Selbst-Check oder Formular-Eingabe.</li>
<li>Vergleich zwischen Studien.</li>
<li>Trend über die Zeit — wichtiger als ein Einzelwert.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>BMI misst keine Körperzusammensetzung.</strong> Muskulöse Personen scoren "übergewichtig", muskelarme "normal".</li>
<li><strong>Nur für Erwachsene.</strong> Bei Kindern Perzentilen-Tabellen verwenden.</li>
<li><strong>Keine Schwangerschaft.</strong> BMI ist während der Schwangerschaft nicht aussagekräftig.</li>
<li><strong>Ethnizität zählt.</strong> WHO Asia-Pacific verwendet niedrigere Schwellen für Süd-/Ostasien.</li>
<li><strong>Große vs kleine Personen.</strong> Die Quadrat-Formel überschätzt große, unterschätzt kleine.</li>
<li><strong>Keine medizinische Beratung.</strong> Im Zweifel Hausarzt/Hausärztin.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>El Índice de Masa Corporal (IMC) es un único número — peso (kg) dividido por el cuadrado de la altura (m) — que la OMS y muchos sistemas sanitarios usan como cribado. Umbrales adultos: menos de 18,5 bajo peso, 18,5–24,9 normal, 25–29,9 sobrepeso, ≥30 obesidad. Esta herramienta calcula valor y categoría desde altura y peso en métrico o imperial.</p>
<h3>Cómo se calcula</h3>
<ul>
<li><strong>Métrico:</strong> IMC = kg ÷ (m × m). 70 kg a 1,75 m → 22,9.</li>
<li><strong>Imperial:</strong> Se convierte a métrico internamente.</li>
<li>Las categorías OMS son independientes del sistema.</li>
</ul>
<h3>Cuándo usarlo</h3>
<ul>
<li>Auto-chequeo rápido o un formulario que lo pida.</li>
<li>Comparar entre estudios.</li>
<li>Seguir la tendencia en el tiempo.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>El IMC no mide composición.</strong> Personas musculadas saldrán "sobrepeso", personas con poco músculo "normal".</li>
<li><strong>Solo adultos.</strong> Para niños usar percentiles por edad y sexo.</li>
<li><strong>Embarazo excluido.</strong> Consulta al profesional sanitario.</li>
<li><strong>La etnia importa.</strong> OMS Asia-Pacífico usa umbrales más bajos.</li>
<li><strong>Personas altas vs bajas.</strong> La fórmula sobreestima a las altas y subestima a las bajas.</li>
<li><strong>No es consejo médico.</strong> Acude a un profesional si te preocupa.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>L'Indice de Masse Corporelle (IMC) est un nombre unique — poids (kg) divisé par le carré de la taille (m) — utilisé par l'OMS comme dépistage. Seuils adultes : moins de 18,5 maigreur, 18,5–24,9 normal, 25–29,9 surpoids, ≥30 obésité. Cet outil calcule la valeur et la catégorie en métrique ou impérial.</p>
<h3>Comment c'est calculé</h3>
<ul>
<li><strong>Métrique :</strong> IMC = kg ÷ (m × m). 70 kg pour 1,75 m → 22,9.</li>
<li><strong>Impérial :</strong> Conversion interne en métrique pour la précision.</li>
<li>Les catégories OMS sont indépendantes du système d'unités.</li>
</ul>
<h3>Quand l'utiliser</h3>
<ul>
<li>Auto-contrôle rapide ou formulaire qui le demande.</li>
<li>Comparer entre études.</li>
<li>Suivre la tendance dans le temps.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>L'IMC ne mesure pas la composition corporelle.</strong> Les personnes musclées peuvent sortir "surpoids", celles avec peu de muscle "normal".</li>
<li><strong>Adulte uniquement.</strong> Pour les enfants, utiliser les percentiles par âge et sexe.</li>
<li><strong>Grossesse exclue.</strong> Consultez un professionnel de santé.</li>
<li><strong>L'origine compte.</strong> OMS Asie-Pacifique utilise des seuils plus bas.</li>
<li><strong>Grands vs petits.</strong> La formule au carré surestime les grands.</li>
<li><strong>Pas un avis médical.</strong> Voyez un professionnel si nécessaire.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>L'Indice di Massa Corporea (BMI) è un singolo numero — peso (kg) diviso per il quadrato dell'altezza (m) — usato dall'OMS come screening. Soglie per adulti: sotto 18,5 sottopeso, 18,5–24,9 normopeso, 25–29,9 sovrappeso, ≥30 obesità. Questo strumento calcola valore e categoria in metrico o imperiale.</p>
<h3>Come si calcola</h3>
<ul>
<li><strong>Metrico:</strong> BMI = kg ÷ (m × m). 70 kg a 1,75 m → 22,9.</li>
<li><strong>Imperiale:</strong> Conversione interna in metrico per precisione.</li>
<li>Le categorie OMS sono indipendenti dal sistema.</li>
</ul>
<h3>Quando usarlo</h3>
<ul>
<li>Autocontrollo rapido o modulo che lo richiede.</li>
<li>Confronto tra studi.</li>
<li>Tendenza nel tempo.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Il BMI non misura la composizione corporea.</strong> Persone muscolose risulteranno "sovrappeso".</li>
<li><strong>Solo adulti.</strong> Per i bambini usare i percentili per età e sesso.</li>
<li><strong>Gravidanza esclusa.</strong> Rivolgersi al professionista sanitario.</li>
<li><strong>L'etnia conta.</strong> OMS Asia-Pacifico usa soglie più basse.</li>
<li><strong>Alti vs bassi.</strong> La formula al quadrato sovrastima le persone alte.</li>
<li><strong>Non è un consiglio medico.</strong> Consulta un medico in caso di dubbi.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>O Índice de Massa Corporal (IMC) é um número único — peso em quilogramas dividido pelo quadrado da altura em metros — usado pela Organização Mundial da Saúde e por muitos sistemas de saúde como uma triagem rápida para categorias de peso corporal. Não é diagnóstico; é um sinalizador. Os limites clássicos para adultos são: abaixo de 18,5 baixo peso, 18,5–24,9 normal, 25–29,9 sobrepeso, 30 ou mais obesidade (dividida em Classe I/II/III em 35 e 40). Esta ferramenta calcula o valor e a categoria a partir da altura e do peso em métrico ou imperial.</p>

<h3>Como é calculado</h3>
<ul>
  <li><strong>Métrico:</strong> IMC = kg ÷ (m × m). 70 kg a 1,75 m → 70 / 3,0625 = 22,9.</li>
  <li><strong>Imperial:</strong> IMC = (lb × 703) ÷ (in × in). A ferramenta converte para métrico internamente para garantir precisão.</li>
  <li>As categorias da OMS são as mesmas independentemente do sistema de unidades — o IMC em si é adimensional.</li>
</ul>

<h3>Quando usar</h3>
<ul>
  <li>Autoavaliação rápida ou para preencher um formulário que pede o valor (seguro, apps de fitness, ficha de academia).</li>
  <li>Comparar um valor entre populações ou estudos.</li>
  <li>Acompanhar a direção da mudança ao longo do tempo (subindo, estável, caindo) — a tendência é mais útil que qualquer leitura isolada.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>O IMC não mede a composição corporal.</strong> Músculo pesa mais que gordura, então uma pessoa em forma e musculosa pode aparecer como "sobrepeso" tendo baixo percentual de gordura. Por outro lado, uma pessoa com pouca massa muscular pode aparecer como "normal" estando pouco saudável ("magro com gordura").</li>
  <li><strong>É uma métrica para adultos.</strong> Para crianças e adolescentes (menores de 18) use as curvas de percentil de IMC específicas por idade e sexo.</li>
  <li><strong>Gestação não é suportada.</strong> O IMC não se aplica durante a gravidez; converse com seu profissional de saúde.</li>
  <li><strong>Etnia importa.</strong> Vários órgãos de saúde (NHS, orientação da OMS Ásia-Pacífico) usam limites mais baixos (sobrepeso ≥23, obesidade ≥27,5) para populações sul-asiáticas, chinesas e outras, porque o risco cardiovascular sobe em IMCs mais baixos.</li>
  <li><strong>Pessoas altas vs baixas.</strong> A fórmula com altura ao quadrado sistematicamente classifica em excesso pessoas altas como "abaixo do peso" e pessoas baixas como "sobrepeso" — fórmulas alternativas (o BMI de Trefethen usa altura^2,5) tentam corrigir isso.</li>
  <li><strong>Não é orientação médica.</strong> Se você está preocupado com seu peso, fale com um profissional. Ele tem o resto do quadro (circunferência abdominal, pressão arterial, exames de sangue, estilo de vida) que um número isolado não tem.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Wskaźnik masy ciała (BMI) to pojedyncza liczba — waga w kilogramach podzielona przez kwadrat wzrostu w metrach — używana przez WHO i wiele systemów ochrony zdrowia jako szybki przesiew dla kategorii masy ciała. To nie diagnoza, tylko sygnał. Klasyczne progi dla dorosłych: poniżej 18,5 niedowaga, 18,5–24,9 prawidłowa, 25–29,9 nadwaga, 30 i więcej otyłość (z podziałem na klasy I/II/III przy 35 i 40). To narzędzie liczy wartość i kategorię z wzrostu i wagi w jednostkach metrycznych lub imperialnych.</p>

<h3>Jak to się liczy</h3>
<ul>
  <li><strong>Metrycznie:</strong> BMI = kg ÷ (m × m). 70 kg przy 1,75 m → 70 / 3,0625 = 22,9.</li>
  <li><strong>Imperialnie:</strong> BMI = (lb × 703) ÷ (in × in). Narzędzie konwertuje wewnętrznie do metrycznych dla dokładności.</li>
  <li>Kategorie WHO są takie same niezależnie od układu jednostek — samo BMI jest bezwymiarowe.</li>
</ul>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Szybki self-check albo wypełnienie formularza, który tego wymaga (ubezpieczenie, apki fitness, wpis na siłownię).</li>
  <li>Porównanie wartości między populacjami albo badaniami.</li>
  <li>Śledzenie kierunku zmiany w czasie (rośnie, stoi, spada) — trend jest użyteczniejszy niż pojedynczy odczyt.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>BMI nie mierzy składu ciała.</strong> Mięśnie ważą więcej niż tłuszcz, więc wysportowana, umięśniona osoba może mieć "nadwagę" przy niskim procencie tkanki tłuszczowej. Z drugiej strony osoba z małą masą mięśniową może wyjść "prawidłowo" będąc niezdrową ("skinny fat").</li>
  <li><strong>To metryka dla dorosłych.</strong> U dzieci i nastolatków (poniżej 18) używaj siatek centylowych BMI dopasowanych do wieku i płci.</li>
  <li><strong>Ciąża nie jest obsługiwana.</strong> BMI nie ma zastosowania w czasie ciąży; pogadaj ze swoim lekarzem.</li>
  <li><strong>Pochodzenie etniczne ma znaczenie.</strong> Kilka instytucji (NHS, wytyczne WHO Asia-Pacific) używa niższych progów (nadwaga ≥23, otyłość ≥27,5) dla populacji południowoazjatyckich, chińskich i innych, bo ryzyko sercowo-naczyniowe rośnie u nich przy niższym BMI.</li>
  <li><strong>Wysocy vs niscy.</strong> Wzór z kwadratem wzrostu systematycznie klasyfikuje wysokich jako "niedowaga", a niskich jako "nadwaga" — alternatywne wzory (BMI Trefethena używa wzrost^2,5) próbują to skorygować.</li>
  <li><strong>To nie porada medyczna.</strong> Jeśli martwisz się swoją wagą, pogadaj z lekarzem. Ma resztę obrazu (obwód talii, ciśnienie, badania krwi, styl życia), której pojedyncza liczba nie pokaże.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>BMI（Body Mass Index、体格指数）は、体重（kg）を身長（m）の 2 乗で割った 1 つの数値で、WHO や多くの保健機関が体重区分のスクリーニング指標として使用しています。診断ではなく、あくまで目安です。成人の代表的な閾値は次のとおりです：18.5 未満は低体重、18.5–24.9 は標準、25–29.9 は肥満気味（過体重）、30 以上は肥満（35・40 でクラス I/II/III に細分）。このツールは身長と体重から、メートル法またはヤード・ポンド法で BMI と区分を計算します。</p>

<h3>計算方法</h3>
<ul>
  <li><strong>メートル法：</strong> BMI = kg ÷ (m × m)。70 kg、1.75 m なら 70 / 3.0625 = 22.9。</li>
  <li><strong>ヤード・ポンド法：</strong> BMI = (lb × 703) ÷ (in × in)。本ツールは精度のため内部でメートル法に変換します。</li>
  <li>WHO の区分は単位系に依存しません。BMI 自体は無次元です。</li>
</ul>

<h3>使うべきタイミング</h3>
<ul>
  <li>簡易セルフチェックや、フォーム入力（保険、フィットネスアプリ、ジムの問診票）のとき。</li>
  <li>集団間や研究間で値を比較したいとき。</li>
  <li>時間経過での変化の方向（増加・横ばい・減少）を追うとき。単発の数値より傾向のほうが有用です。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>BMI は身体組成を測りません。</strong> 筋肉は脂肪より重いため、体脂肪が低くても筋肉質の人は「肥満気味」と判定されることがあります。逆に筋肉量が少ない人は「標準」でも実は不健康（いわゆる "skinny fat"）ということもあります。</li>
  <li><strong>これは成人向けの指標です。</strong> 18 歳未満の子どもや思春期の場合は、年齢・性別ごとの BMI パーセンタイル曲線を使ってください。</li>
  <li><strong>妊娠中は対象外です。</strong> 妊娠中は BMI は当てはまりません。担当医に相談してください。</li>
  <li><strong>人種・民族による違いがあります。</strong> NHS や WHO のアジア太平洋ガイドラインなど、いくつかの保健機関は南アジア、中国系、その他の集団に対して、より低い閾値（過体重 ≥23、肥満 ≥27.5）を採用しています。これらの集団では低い BMI でも心血管リスクが上がるためです。</li>
  <li><strong>身長が高い人と低い人。</strong> 身長の 2 乗を使う式は、構造的に背の高い人を「低体重」、背の低い人を「過体重」と過大に分類しがちです。代替式（Trefethen の BMI は身長^2.5 を使用）はこれを補正しようとします。</li>
  <li><strong>医療助言ではありません。</strong> 体重について不安がある場合は専門家に相談してください。ウエスト周囲径、血圧、血液検査、生活習慣など、単一の数値では分からない情報を併せて評価してくれます。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Body Mass Index (BMI) is één getal — gewicht in kilo's gedeeld door het kwadraat van de lengte in meters — dat door de Wereldgezondheidsorganisatie en veel gezondheidssystemen wordt gebruikt als snelle screening voor gewichtscategorieën. Het is geen diagnose; het is een signaal. De klassieke volwassen drempels zijn: onder 18,5 ondergewicht, 18,5–24,9 normaal, 25–29,9 overgewicht, 30 en hoger obesitas (klasse I/II/III bij 35 en 40). Deze tool berekent de waarde en de categorie uit lengte en gewicht in metrisch of imperiaal.</p>

<h3>Hoe het berekend wordt</h3>
<ul>
  <li><strong>Metrisch:</strong> BMI = kg ÷ (m × m). 70 kg bij 1,75 m → 70 / 3,0625 = 22,9.</li>
  <li><strong>Imperiaal:</strong> BMI = (lb × 703) ÷ (in × in). De tool converteert intern naar metrisch voor nauwkeurigheid.</li>
  <li>De WHO-categorieën zijn hetzelfde ongeacht het eenhedensysteem — BMI zelf is eenheidsloos.</li>
</ul>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Snelle self-check of een formulier invullen dat erom vraagt (verzekering, fitness apps, sportschool-intake).</li>
  <li>Een waarde vergelijken over populaties of studies heen.</li>
  <li>Trend over tijd volgen (stijgend, stabiel, dalend) — de trend is nuttiger dan een enkele meting.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>BMI meet geen lichaamssamenstelling.</strong> Spier weegt meer dan vet, dus een fitte, gespierde persoon kan "overgewicht" scoren met laag vetpercentage. Andersom kan iemand met weinig spiermassa "normaal" scoren terwijl die ongezond is ("skinny fat").</li>
  <li><strong>Het is een volwassen-metric.</strong> Voor kinderen en jongeren (onder 18) gebruik je in plaats daarvan de leeftijd- en geslachtspecifieke BMI-percentielcurven.</li>
  <li><strong>Zwangerschap wordt niet ondersteund.</strong> BMI geldt niet tijdens zwangerschap; overleg met je zorgverlener.</li>
  <li><strong>Etniciteit doet ertoe.</strong> Diverse gezondheidsinstanties (NHS, WHO Asia-Pacific-richtlijnen) hanteren lagere drempels (overgewicht ≥23, obesitas ≥27,5) voor Zuid-Aziatische, Chinese en andere groepen, omdat cardiovasculair risico bij lagere BMI stijgt.</li>
  <li><strong>Lange vs korte mensen.</strong> De gekwadrateerde-lengte formule classificeert lange mensen systematisch als "ondergewicht" en korte mensen als "overgewicht" — alternatieve formules (Trefethen's BMI gebruikt lengte^2.5) proberen dit te corrigeren.</li>
  <li><strong>Geen medisch advies.</strong> Als je je zorgen maakt over je gewicht, overleg met een arts. Die heeft de rest van het plaatje (buikomvang, bloeddruk, bloedwaarden, leefstijl) dat één getal niet biedt.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Vücut Kitle İndeksi (BMI), kilogram cinsinden ağırlığın metre cinsinden boyun karesine bölümü — Dünya Sağlık Örgütü ve birçok sağlık sisteminin vücut ağırlığı kategorileri için hızlı bir tarama olarak kullandığı tek bir sayıdır. Tanı koymaz; bir bayrak olarak çalışır. Klasik yetişkin eşikleri: 18,5 altı zayıf, 18,5–24,9 normal, 25–29,9 fazla kilolu, 30 ve üzeri obez (35 ve 40'ta Sınıf I/II/III'e ayrılır). Bu araç metrik veya imperial boy ve kilodan değeri ve kategoriyi hesaplar.</p>

<h3>Nasıl hesaplanır</h3>
<ul>
  <li><strong>Metrik:</strong> BMI = kg ÷ (m × m). 1,75 m'de 70 kg → 70 / 3,0625 = 22,9.</li>
  <li><strong>Imperial:</strong> BMI = (lb × 703) ÷ (in × in). Araç doğruluk için içsel olarak metriğe dönüştürür.</li>
  <li>DSÖ kategorileri birim sistemden bağımsız aynıdır — BMI'nin kendisi birimsizdir.</li>
</ul>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Hızlı öz kontrol veya isteyen bir form (sigorta, fitness uygulamaları, spor salonu girişi) doldurmak için.</li>
  <li>Bir değeri popülasyonlar veya çalışmalar arasında karşılaştırma.</li>
  <li>Zaman içinde değişim yönünü (artan, sabit, azalan) takip etme — eğilim, herhangi bir tek okumadan daha kullanışlıdır.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>BMI vücut kompozisyonunu ölçmez.</strong> Kas yağdan daha ağırdır, bu nedenle fit, kaslı biri düşük vücut yağ oranıyla "fazla kilolu" çıkabilir. Tersine, düşük kaslı biri sağlıksız olduğu halde "normal" çıkabilir ("zayıf yağlı").</li>
  <li><strong>Bu bir yetişkin metriğidir.</strong> 18 yaş altı çocuk ve ergenler için yaşa ve cinsiyete özgü BMI yüzdelik tabloları kullan.</li>
  <li><strong>Hamilelik desteklenmiyor.</strong> BMI hamilelik sırasında geçerli değildir; sağlık hizmeti sağlayıcına danış.</li>
  <li><strong>Etnik köken önemli.</strong> Birkaç sağlık kuruluşu (NHS, DSÖ Asya-Pasifik kılavuzu) Güney Asyalı, Çinli ve diğer gruplar için kardiyovasküler risk daha düşük BMI'lerde arttığı için daha düşük eşikler (fazla kilolu ≥23, obez ≥27,5) kullanır.</li>
  <li><strong>Uzun - kısa insanlar.</strong> Karesi alınmış boy formülü sistematik olarak uzun insanları "zayıf" ve kısa insanları "fazla kilolu" olarak fazla sınıflandırır.</li>
  <li><strong>Tıbbi tavsiye değildir.</strong> Kilonla ilgili endişen varsa, bir klinisyenle konuş. Tek bir sayının vermediği bel çevresi, kan basıncı, kan değerleri, yaşam tarzı gibi resmin geri kalanına sahipler.</li>
</ul>
""",
    },
    "related": ["unit-converter", "percentage-calculator", "tip-split-calculator"],
    "howto": {"flow": "calculate", "action": "format", "noun": "BMI"},
}
