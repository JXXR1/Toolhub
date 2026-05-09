TOOL = {
    "slug": "date-calculator",
    "category": "datetime",
    "icon": "📅",
    "tags": ["date", "calculator", "duration", "between", "add", "subtract", "age", "weekday"],
    "i18n": {
        "en": {
            "name": "Date Calculator",
            "tagline": "Days between two dates · add or subtract days/weeks/months/years from a date · age in years, months and days.",
            "description": "Free online date calculator. Compute the duration between two dates, add or subtract a span from any date, and work out exact age in years/months/days. All calculations run in your browser.",
        },
        "de": {"name": "Datumsrechner", "tagline": "Tage zwischen zwei Daten · Tage/Wochen/Monate/Jahre addieren oder subtrahieren · Alter in Jahren, Monaten und Tagen.", "description": "Kostenloser Datumsrechner. Berechne die Dauer zwischen zwei Daten, addiere oder subtrahiere Zeitspannen und ermittle das exakte Alter."},
        "es": {"name": "Calculadora de Fechas", "tagline": "Días entre dos fechas · suma o resta días/semanas/meses/años · edad exacta en años, meses y días.", "description": "Calculadora de fechas gratuita. Calcula la duración entre dos fechas, suma o resta un período y obtén la edad exacta en años/meses/días."},
        "fr": {"name": "Calculatrice de Dates", "tagline": "Jours entre deux dates · ajouter ou soustraire jours/semaines/mois/années · âge en années, mois et jours.", "description": "Calculatrice de dates gratuite. Calculez la durée entre deux dates, ajoutez ou soustrayez une période et obtenez l'âge exact."},
        "it": {"name": "Calcolatore di Date", "tagline": "Giorni tra due date · aggiungi o sottrai giorni/settimane/mesi/anni · età esatta in anni, mesi e giorni.", "description": "Calcolatore di date gratuito. Calcola la durata tra due date, aggiungi o sottrai un periodo e ottieni l'età esatta in anni/mesi/giorni."},
        "pt": {"name": "Calculadora de Datas", "tagline": "Dias entre duas datas · somar ou subtrair dias/semanas/meses/anos · idade em anos, meses e dias.", "description": "Calculadora de datas online gratuita. Calcule a duração entre duas datas, some ou subtraia um período e descubra a idade exata em anos/meses/dias. Tudo roda no seu browser."},
        "pl": {"name": "Kalkulator Dat", "tagline": "Dni między dwiema datami · dodaj/odejmij dni/tygodnie/miesiące/lata · wiek w latach, miesiącach i dniach.", "description": "Darmowy online kalkulator dat. Policz różnicę między dwiema datami, dodaj lub odejmij okres od dowolnej daty i wylicz dokładny wiek w latach/miesiącach/dniach. Wszystko liczy się w przeglądarce."},
    },
    "body": """
<div class="tool-card">
  <label>Mode</label>
  <select id="dc-mode" onchange="dcMode()">
    <option value="between">Duration between two dates</option>
    <option value="addsub">Add / subtract from a date</option>
    <option value="age">Age (years / months / days)</option>
  </select>
</div>

<div class="tool-card" id="dc-card-between">
  <div class="row-2col">
    <div>
      <label>{LBL_FROM}</label>
      <input type="date" id="dc-a" oninput="dcRun()">
    </div>
    <div>
      <label>{LBL_TO}</label>
      <input type="date" id="dc-b" oninput="dcRun()">
    </div>
  </div>
  <label style="margin-top:0.7rem"><input type="checkbox" id="dc-incl" onchange="dcRun()"> Include the end date in the count</label>
</div>

<div class="tool-card" id="dc-card-addsub" style="display:none">
  <div class="row-2col">
    <div>
      <label>Start date</label>
      <input type="date" id="dc-start" oninput="dcRun()">
    </div>
    <div>
      <label>Operation</label>
      <select id="dc-op" onchange="dcRun()">
        <option value="+">Add</option>
        <option value="-">Subtract</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.6rem">
    <div>
      <label>Years</label>
      <input type="number" id="dc-y" value="0" oninput="dcRun()">
    </div>
    <div>
      <label>Months</label>
      <input type="number" id="dc-m" value="0" oninput="dcRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.6rem">
    <div>
      <label>Weeks</label>
      <input type="number" id="dc-w" value="0" oninput="dcRun()">
    </div>
    <div>
      <label>Days</label>
      <input type="number" id="dc-d" value="0" oninput="dcRun()">
    </div>
  </div>
</div>

<div class="tool-card" id="dc-card-age" style="display:none">
  <div class="row-2col">
    <div>
      <label>Date of birth</label>
      <input type="date" id="dc-dob" oninput="dcRun()">
    </div>
    <div>
      <label>As of</label>
      <input type="date" id="dc-as" oninput="dcRun()">
    </div>
  </div>
</div>

<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="dc-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.dc-rows{display:grid;gap:0.5rem}
.dc-row{display:grid;grid-template-columns:170px 1fr;gap:0.6rem;align-items:center;padding:0.5rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-size:0.9rem}
.dc-row .lbl{font-size:0.78rem;color:var(--text-muted);font-family:ui-monospace,monospace}
.dc-row .val{font-family:ui-monospace,monospace}
.dc-pri{color:var(--accent);font-weight:600;font-size:1.05rem}
</style>
<script>
const DC_MS_DAY = 86400000;
function dcParse(id){
  const v = document.getElementById(id).value;
  if(!v) return null;
  // YYYY-MM-DD as UTC noon to dodge DST entirely
  const [y,m,d] = v.split('-').map(Number);
  return new Date(Date.UTC(y, m-1, d, 12));
}
function dcFmt(d){
  return d.toLocaleDateString(undefined, {weekday:'long', year:'numeric', month:'long', day:'numeric', timeZone:'UTC'});
}
function dcDateAdd(d, y, m, w, day){
  const nd = new Date(d);
  if(y) nd.setUTCFullYear(nd.getUTCFullYear() + y);
  if(m) nd.setUTCMonth(nd.getUTCMonth() + m);
  if(w || day) nd.setUTCDate(nd.getUTCDate() + (w*7) + day);
  return nd;
}
function dcWorkdays(a, b){
  // count Mon-Fri inclusive of both ends
  let from = new Date(a), to = new Date(b);
  if(from > to){ const t = from; from = to; to = t; }
  let n = 0;
  const cur = new Date(from);
  while(cur <= to){
    const dow = cur.getUTCDay();
    if(dow !== 0 && dow !== 6) n++;
    cur.setUTCDate(cur.getUTCDate() + 1);
  }
  return n;
}
function dcYmd(a, b){
  // exact years/months/days difference (a <= b)
  let y = b.getUTCFullYear() - a.getUTCFullYear();
  let m = b.getUTCMonth() - a.getUTCMonth();
  let d = b.getUTCDate() - a.getUTCDate();
  if(d < 0){
    m -= 1;
    const prev = new Date(Date.UTC(b.getUTCFullYear(), b.getUTCMonth(), 0));
    d += prev.getUTCDate();
  }
  if(m < 0){ y -= 1; m += 12; }
  return {y, m, d};
}
function dcMode(){
  const m = document.getElementById('dc-mode').value;
  document.getElementById('dc-card-between').style.display = m === 'between' ? '' : 'none';
  document.getElementById('dc-card-addsub').style.display = m === 'addsub' ? '' : 'none';
  document.getElementById('dc-card-age').style.display = m === 'age' ? '' : 'none';
  dcRun();
}
function dcRun(){
  const mode = document.getElementById('dc-mode').value;
  const out = document.getElementById('dc-out');
  out.classList.remove('error');
  if(mode === 'between'){
    const a = dcParse('dc-a'), b = dcParse('dc-b');
    if(!a || !b){ out.textContent = '{LBL_NO_INPUT}'; out.className='output'; return; }
    const incl = document.getElementById('dc-incl').checked ? 1 : 0;
    const from = a < b ? a : b, to = a < b ? b : a;
    const days = Math.round((to - from) / DC_MS_DAY) + incl;
    const ymd = dcYmd(from, to);
    const wd = dcWorkdays(from, to);
    out.className = 'output';
    out.innerHTML = `<div class="dc-rows">
      <div class="dc-row"><div class="lbl">Total days</div><div class="val dc-pri">${days.toLocaleString()} ${days===1?'day':'days'}</div></div>
      <div class="dc-row"><div class="lbl">Years/Months/Days</div><div class="val">${ymd.y}y ${ymd.m}m ${ymd.d}d</div></div>
      <div class="dc-row"><div class="lbl">Weeks &amp; days</div><div class="val">${Math.floor(days/7)}w ${days%7}d</div></div>
      <div class="dc-row"><div class="lbl">Workdays (Mon–Fri)</div><div class="val">${wd.toLocaleString()}</div></div>
      <div class="dc-row"><div class="lbl">Hours / Minutes / Seconds</div><div class="val">${(days*24).toLocaleString()}h · ${(days*1440).toLocaleString()}m · ${(days*86400).toLocaleString()}s</div></div>
      <div class="dc-row"><div class="lbl">From</div><div class="val">${dcFmt(from)}</div></div>
      <div class="dc-row"><div class="lbl">To</div><div class="val">${dcFmt(to)}</div></div>
    </div>`;
    return;
  }
  if(mode === 'addsub'){
    const start = dcParse('dc-start');
    if(!start){ out.textContent = '{LBL_NO_INPUT}'; out.className='output'; return; }
    const op = document.getElementById('dc-op').value === '-' ? -1 : 1;
    const y = (parseInt(document.getElementById('dc-y').value) || 0) * op;
    const m = (parseInt(document.getElementById('dc-m').value) || 0) * op;
    const w = (parseInt(document.getElementById('dc-w').value) || 0) * op;
    const d = (parseInt(document.getElementById('dc-d').value) || 0) * op;
    const result = dcDateAdd(start, y, m, w, d);
    const days = Math.round((result - start) / DC_MS_DAY);
    out.className = 'output';
    out.innerHTML = `<div class="dc-rows">
      <div class="dc-row"><div class="lbl">Result</div><div class="val dc-pri">${dcFmt(result)}</div></div>
      <div class="dc-row"><div class="lbl">ISO</div><div class="val">${result.toISOString().slice(0,10)}</div></div>
      <div class="dc-row"><div class="lbl">Net days</div><div class="val">${(days>=0?'+':'') + days.toLocaleString()}</div></div>
      <div class="dc-row"><div class="lbl">From</div><div class="val">${dcFmt(start)}</div></div>
    </div>`;
    return;
  }
  // age
  const dob = dcParse('dc-dob');
  let asOf = dcParse('dc-as');
  if(!dob){ out.textContent = '{LBL_NO_INPUT}'; out.className='output'; return; }
  if(!asOf){ asOf = new Date(); asOf = new Date(Date.UTC(asOf.getUTCFullYear(), asOf.getUTCMonth(), asOf.getUTCDate(), 12)); }
  if(dob > asOf){ out.classList.add('error'); out.textContent = '✗ Date of birth is after the "as of" date.'; return; }
  const ymd = dcYmd(dob, asOf);
  const days = Math.round((asOf - dob) / DC_MS_DAY);
  // next birthday
  let next = new Date(Date.UTC(asOf.getUTCFullYear(), dob.getUTCMonth(), dob.getUTCDate(), 12));
  if(next <= asOf) next = new Date(Date.UTC(asOf.getUTCFullYear()+1, dob.getUTCMonth(), dob.getUTCDate(), 12));
  const untilNext = Math.round((next - asOf) / DC_MS_DAY);
  out.className = 'output';
  out.innerHTML = `<div class="dc-rows">
    <div class="dc-row"><div class="lbl">Age</div><div class="val dc-pri">${ymd.y} years, ${ymd.m} months, ${ymd.d} days</div></div>
    <div class="dc-row"><div class="lbl">Total days</div><div class="val">${days.toLocaleString()}</div></div>
    <div class="dc-row"><div class="lbl">Total weeks</div><div class="val">${Math.floor(days/7).toLocaleString()}</div></div>
    <div class="dc-row"><div class="lbl">Total months (approx)</div><div class="val">${(ymd.y*12 + ymd.m).toLocaleString()}</div></div>
    <div class="dc-row"><div class="lbl">Born on a</div><div class="val">${dob.toLocaleDateString(undefined,{weekday:'long', timeZone:'UTC'})}</div></div>
    <div class="dc-row"><div class="lbl">Next birthday</div><div class="val">${dcFmt(next)} — in ${untilNext} ${untilNext===1?'day':'days'}</div></div>
  </div>`;
}
document.addEventListener('DOMContentLoaded', dcMode);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Three things people actually want from a date calculator: the gap between two dates ("how many days until launch?"), shifting a date by a span ("90 days after invoice date"), and a precise age ("years, months, and days from a date of birth"). This tool does all three, in your browser, anchored to UTC noon so DST and timezone shifts don't quietly wrong the answer when you travel.</p>

<h3>When to use it</h3>
<ul>
  <li>Calculating contract durations, project timelines, and deadlines.</li>
  <li>Working out exactly how many workdays (Mon–Fri) fall between two dates for invoicing or project estimation.</li>
  <li>Verifying age cut-offs (visa eligibility, school years, milestone birthdays).</li>
  <li>Adding "30 days net" or "90 day cooling-off" periods to a baseline date in a way that handles month-end correctly.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Inclusive vs exclusive end dates.</strong> "Days from Mon to Fri" is 4 if you count gaps, 5 if you count days. The toggle controls which convention; both are right depending on the question.</li>
  <li><strong>Add/subtract order matters.</strong> Years and months apply first, then weeks and days. Adding "1 month + 1 day" to Jan 30 gives Mar 1 (Feb 30 → Feb 28/29 → +1), not Mar 2 — which is the calendar-safe convention almost every datetime library uses.</li>
  <li><strong>Workdays don't include holidays.</strong> The calculation knows weekends but not bank holidays — adjust manually if it matters.</li>
  <li><strong>"Total months" is approximate</strong> in the age view (years × 12 + months) — it ignores the trailing days. The Y/M/D figure is exact.</li>
  <li><strong>UTC anchoring trades off with locale.</strong> A date in your local timezone might map to a slightly different UTC day. For most uses (deadlines, ages) UTC noon is the safer anchor; for to-the-minute timezone work use the timezone converter.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Três coisas que as pessoas realmente querem de uma calculadora de datas: a diferença entre duas datas ("quantos dias até o lançamento?"), deslocar uma data por um período ("90 dias depois da nota fiscal") e uma idade precisa ("anos, meses e dias a partir de uma data de nascimento"). Esta ferramenta faz as três, no seu browser, ancorada em UTC ao meio-dia para que horário de verão e mudanças de fuso não bagunçem a resposta quando você viaja.</p>

<h3>Quando usar</h3>
<ul>
  <li>Calcular durações de contratos, timelines de projetos e prazos.</li>
  <li>Descobrir exatamente quantos dias úteis (seg–sex) caem entre duas datas para faturamento ou estimativa de projeto.</li>
  <li>Verificar cortes de idade (elegibilidade de visto, anos escolares, aniversários marcantes).</li>
  <li>Adicionar períodos de "30 dias líquidos" ou "90 dias de carência" a uma data base, lidando corretamente com fim de mês.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Datas de fim inclusivas vs exclusivas.</strong> "Dias de seg até sex" é 4 se você conta intervalos, 5 se você conta dias. O toggle controla qual convenção; ambas estão certas, depende da pergunta.</li>
  <li><strong>A ordem de soma/subtração importa.</strong> Anos e meses são aplicados primeiro, depois semanas e dias. Adicionar "1 mês + 1 dia" a 30 de janeiro dá 1 de março (Fev 30 → Fev 28/29 → +1), não 2 de março — que é a convenção segura para calendário usada por quase toda lib de datetime.</li>
  <li><strong>Dias úteis não incluem feriados.</strong> O cálculo conhece fins de semana mas não feriados bancários — ajuste manualmente se importar.</li>
  <li><strong>"Total de meses" é aproximado</strong> na visão de idade (anos × 12 + meses) — ignora os dias finais. O número Y/M/D é exato.</li>
  <li><strong>Ancorar em UTC tem trade-off com locale.</strong> Uma data no seu fuso local pode mapear para um dia UTC ligeiramente diferente. Para a maioria dos usos (prazos, idades) UTC ao meio-dia é o ancoramento mais seguro; para trabalho de fuso ao minuto, use o conversor de fuso horário.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Trzy rzeczy, których ludzie naprawdę chcą od kalkulatora dat: różnica między dwiema datami ("ile dni do launchu?"), przesunięcie daty o okres ("90 dni po dacie faktury") i precyzyjny wiek ("lata, miesiące i dni od daty urodzenia"). To narzędzie robi wszystkie trzy, w przeglądarce, zakotwiczone w UTC w południe, żeby DST i przesunięcia stref nie wykrzywiały po cichu odpowiedzi, gdy podróżujesz.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Liczenie długości umów, timeline'ów projektów i deadline'ów.</li>
  <li>Sprawdzanie, ile dokładnie dni roboczych (pn–pt) wpada między dwie daty do fakturowania albo wyceny.</li>
  <li>Weryfikacja granic wieku (uprawnienia do wizy, lata szkolne, okrągłe urodziny).</li>
  <li>Dodawanie okresów "30 dni netto" albo "90 dni odstąpienia" do daty bazowej w sposób, który dobrze radzi sobie z końcami miesięcy.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Daty końcowe inkluzywne vs ekskluzywne.</strong> "Dni od pn do pt" to 4, jeśli liczysz odstępy, 5, jeśli liczysz dni. Toggle kontroluje, którą konwencję; obie są poprawne w zależności od pytania.</li>
  <li><strong>Kolejność dodawania/odejmowania ma znaczenie.</strong> Lata i miesiące najpierw, potem tygodnie i dni. Dodanie "1 miesiąc + 1 dzień" do 30 stycznia daje 1 marca (30 lutego → 28/29 lutego → +1), nie 2 marca — to bezpieczna konwencja kalendarzowa, której używa niemal każda biblioteka datetime.</li>
  <li><strong>Dni robocze nie obejmują świąt.</strong> Liczenie zna weekendy, ale nie święta państwowe — popraw ręcznie, jeśli to ważne.</li>
  <li><strong>"Łączne miesiące" są przybliżone</strong> w widoku wieku (lata × 12 + miesiące) — ignoruje końcowe dni. Liczba R/M/D jest dokładna.</li>
  <li><strong>Kotwiczenie w UTC ma trade-off z lokalizacją.</strong> Data w twojej strefie lokalnej może zmapować na nieco inny dzień UTC. W większości zastosowań (deadline'y, wiek) UTC w południe jest bezpieczniejsze; do pracy ze strefami z dokładnością do minut użyj konwertera stref czasowych.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "timezone-converter", "percentage-calculator"],
}
