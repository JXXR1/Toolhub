TOOL = {
    "slug": "cron-builder",
    "category": "developer",
    "icon": "⏱",
    "tags": ["cron", "schedule", "builder", "crontab", "next run"],
    "i18n": {
        "en": {
            "name": "Cron Expression Builder",
            "tagline": "Visually build a cron expression — minute, hour, day, month, weekday — and preview the next 5 fire times.",
            "description": "Free online cron expression builder. Pick fields with dropdowns and presets, get the cron string out, and see the next 5 fire times in your local timezone. Standard 5-field crontab.",
        },
        "de": {"name": "Cron-Ausdruck-Builder", "tagline": "Cron-Ausdruck visuell bauen — Minute, Stunde, Tag, Monat, Wochentag — und nächste 5 Auslösezeiten ansehen.", "description": "Kostenloser Cron-Ausdruck-Builder. Felder per Dropdown wählen, Cron-String erhalten, nächste 5 Ausführungen in deiner Zeitzone sehen. Standard 5-Felder-Crontab."},
        "es": {"name": "Constructor de Cron", "tagline": "Construye visualmente una expresión cron — minuto, hora, día, mes, día de semana — y previsualiza las próximas 5 ejecuciones.", "description": "Constructor de expresiones cron gratuito. Elige campos con desplegables, obtén el string cron y ve las próximas 5 ejecuciones en tu zona horaria. Crontab estándar de 5 campos."},
        "fr": {"name": "Constructeur Cron", "tagline": "Construisez visuellement une expression cron — minute, heure, jour, mois, jour-semaine — et prévisualisez les 5 prochaines exécutions.", "description": "Constructeur d'expression cron gratuit. Choisissez les champs via menus, récupérez la chaîne cron, voyez les 5 prochaines exécutions dans votre fuseau. Crontab standard 5 champs."},
        "it": {"name": "Costruttore Cron", "tagline": "Costruisci visivamente un'espressione cron — minuto, ora, giorno, mese, giorno-settimana — e anteprima delle prossime 5 esecuzioni.", "description": "Costruttore di espressioni cron gratuito. Scegli i campi con menu, ottieni la stringa cron e vedi le prossime 5 esecuzioni nel tuo fuso. Crontab standard a 5 campi."},
    },
    "body": """
<div class="tool-card">
  <label>Preset</label>
  <select id="cb-preset" onchange="cbPreset()">
    <option value="">— choose a preset or build below —</option>
    <option value="* * * * *">Every minute</option>
    <option value="*/5 * * * *">Every 5 minutes</option>
    <option value="*/15 * * * *">Every 15 minutes</option>
    <option value="0 * * * *">Every hour (top of hour)</option>
    <option value="0 0 * * *">Daily at midnight</option>
    <option value="0 9 * * *">Daily at 09:00</option>
    <option value="0 9 * * 1-5">Weekdays at 09:00</option>
    <option value="0 0 * * 0">Weekly Sunday midnight</option>
    <option value="0 0 1 * *">Monthly (1st at midnight)</option>
    <option value="0 0 1 1 *">Yearly (Jan 1 at midnight)</option>
  </select>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Minute (0–59)</label>
      <input type="text" id="cb-min" value="0" oninput="cbBuild()" placeholder="* | */5 | 0,30 | 0-29">
    </div>
    <div>
      <label>Hour (0–23)</label>
      <input type="text" id="cb-hour" value="9" oninput="cbBuild()" placeholder="* | */2 | 9-17">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Day of month (1–31)</label>
      <input type="text" id="cb-dom" value="*" oninput="cbBuild()" placeholder="* | 1 | 1,15">
    </div>
    <div>
      <label>Month (1–12)</label>
      <input type="text" id="cb-mon" value="*" oninput="cbBuild()" placeholder="* | */3 | 1-6">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Day of week (0=Sun – 6=Sat)</label>
      <input type="text" id="cb-dow" value="1-5" oninput="cbBuild()" placeholder="* | 1-5 | 0,6">
    </div>
    <div>
      <label>&nbsp;</label>
      <button class="secondary" onclick="cbReset()" style="width:100%">Reset to */5 every minute</button>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>Cron expression</label>
  <div class="output-row">
    <pre class="output" id="cb-expr" style="margin:0;flex:1;font-size:1.05rem">0 9 * * 1-5</pre>
    <button class="copy-btn secondary" onclick="copyOutput('cb-expr', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="cb-explain" style="margin-top:0.5rem"></div>
</div>
<div class="tool-card">
  <label>Next 5 fire times (local timezone)</label>
  <pre class="output" id="cb-next">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
const CB_RANGES = [[0,59],[0,23],[1,31],[1,12],[0,7]];

function cbPreset(){
  const v = document.getElementById('cb-preset').value;
  if(!v) return;
  const f = v.split(/\\s+/);
  document.getElementById('cb-min').value = f[0];
  document.getElementById('cb-hour').value = f[1];
  document.getElementById('cb-dom').value = f[2];
  document.getElementById('cb-mon').value = f[3];
  document.getElementById('cb-dow').value = f[4];
  cbBuild();
}
function cbReset(){
  document.getElementById('cb-min').value = '*/5';
  document.getElementById('cb-hour').value = '*';
  document.getElementById('cb-dom').value = '*';
  document.getElementById('cb-mon').value = '*';
  document.getElementById('cb-dow').value = '*';
  document.getElementById('cb-preset').value = '';
  cbBuild();
}

function cbExpand(field, idx){
  const [lo,hi] = CB_RANGES[idx];
  const out = new Set();
  field.split(',').forEach(part => {
    let step = 1;
    if (part.includes('/')){ const [a,b] = part.split('/'); step = parseInt(b,10); part = a; }
    let from = lo, to = hi;
    if (part === '*'){ /* keep */ }
    else if (part.includes('-')){ const [a,b] = part.split('-'); from = parseInt(a,10); to = parseInt(b,10); }
    else { from = to = parseInt(part,10); }
    if (isNaN(from) || isNaN(to) || from < lo || to > hi || from > to) throw new Error('Bad value: ' + part + ' (range ' + lo + '–' + hi + ')');
    if (isNaN(step) || step < 1) throw new Error('Bad step: ' + step);
    for (let v = from; v <= to; v += step) out.add(idx === 4 && v === 7 ? 0 : v);
  });
  return out;
}

function cbMatches(date, sets){
  return sets[0].has(date.getMinutes())
    && sets[1].has(date.getHours())
    && sets[2].has(date.getDate())
    && sets[3].has(date.getMonth() + 1)
    && sets[4].has(date.getDay());
}

function cbNext(expr, count){
  const fields = expr.trim().split(/\\s+/);
  if (fields.length !== 5) throw new Error('Expected 5 fields, got ' + fields.length);
  const sets = fields.map((f, i) => cbExpand(f, i));
  const now = new Date();
  let d = new Date(now.getFullYear(), now.getMonth(), now.getDate(), now.getHours(), now.getMinutes() + 1, 0, 0);
  const out = [];
  let safety = 0;
  while (out.length < count && safety < 600000){
    if (cbMatches(d, sets)) out.push(new Date(d));
    d.setMinutes(d.getMinutes() + 1);
    safety++;
  }
  if (safety >= 600000) throw new Error('No matches found in the next ~1 year');
  return out;
}

function cbExplain(expr){
  const f = expr.trim().split(/\\s+/);
  if(f.length !== 5) return '';
  const [m,h,dom,mon,dow] = f;
  let s = 'At ';
  if(m === '*') s += 'every minute';
  else if(m.startsWith('*/')) s += 'every ' + m.slice(2) + ' minutes';
  else s += 'minute ' + m;
  s += ', ';
  if(h === '*') s += 'every hour';
  else if(h.startsWith('*/')) s += 'every ' + h.slice(2) + ' hours';
  else s += 'hour ' + h;
  if(dow !== '*'){
    const names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    if(dow.includes('-')){
      const [a,b] = dow.split('-').map(x => parseInt(x,10));
      s += ', on ' + names[a] + '–' + names[b];
    } else if(dow.includes(',')){
      s += ', on ' + dow.split(',').map(x => names[parseInt(x,10) % 7]).join(',');
    } else if(!isNaN(parseInt(dow,10))){
      s += ', on ' + names[parseInt(dow,10) % 7];
    }
  }
  if(dom !== '*') s += ', on day ' + dom;
  if(mon !== '*'){
    const monNames = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    if(mon.includes('-')){ const [a,b] = mon.split('-').map(x=>parseInt(x,10)); s += ', in ' + monNames[a] + '–' + monNames[b]; }
    else if(!isNaN(parseInt(mon,10))) s += ', in ' + monNames[parseInt(mon,10)];
    else s += ', in month ' + mon;
  }
  return s + '.';
}

function cbBuild(){
  const expr = [
    document.getElementById('cb-min').value,
    document.getElementById('cb-hour').value,
    document.getElementById('cb-dom').value,
    document.getElementById('cb-mon').value,
    document.getElementById('cb-dow').value
  ].join(' ');
  document.getElementById('cb-expr').textContent = expr;
  document.getElementById('cb-expr').classList.remove('error');
  const next = document.getElementById('cb-next');
  const explain = document.getElementById('cb-explain');
  next.classList.remove('error');
  try {
    const dates = cbNext(expr, 5);
    next.textContent = dates.map((d,i) => (i+1) + '.  ' + d.toLocaleString(undefined,{weekday:'short',year:'numeric',month:'short',day:'2-digit',hour:'2-digit',minute:'2-digit'})).join('\\n');
    explain.textContent = cbExplain(expr);
  } catch(e){
    next.classList.add('error');
    next.textContent = '✗ ' + e.message;
    explain.textContent = '';
  }
}
document.addEventListener('DOMContentLoaded', cbBuild);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Cron syntax is famously dense — five fields, each accepting wildcards, ranges, lists, and steps. Writing one from scratch every time invites typos. This builder lets you start from a preset (every-5-minutes, weekdays-at-09:00, etc.) or type into individual fields, see the resulting cron string, get a plain-English summary, and confirm against the next five real fire times in your local timezone. The complement to this is the <a href="/cron-parser/">Cron Expression Parser</a>, which decodes an existing expression into the same preview.</p>

<h3>When to use it</h3>
<ul>
  <li>Setting up a new <code>crontab</code> entry, Kubernetes <code>CronJob</code>, GitHub Actions schedule, or AWS EventBridge rule.</li>
  <li>Translating a "run every weekday morning" requirement into a syntactically correct cron line.</li>
  <li>Sanity-checking that an expression you've drafted will actually run when you think it will, before deploying.</li>
  <li>Onboarding someone new to cron — let the dropdowns and the preview teach the syntax.</li>
</ul>

<h3>Field syntax cheat sheet</h3>
<ul>
  <li><code>*</code> — every value in the field's range.</li>
  <li><code>*/N</code> — every Nth (starting at the lower bound).</li>
  <li><code>A-B</code> — range, inclusive.</li>
  <li><code>A,B,C</code> — list of specific values.</li>
  <li><code>A-B/N</code> — every Nth within range A–B.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Day-of-month + day-of-week interact.</strong> Most cron implementations OR them when both are restricted: <code>* * 15 * 1</code> fires on the 15th OR a Monday, not "the 15th if it's a Monday".</li>
  <li><strong>Timezone is your browser's local zone here.</strong> Real cron daemons run in the server's timezone (often UTC). Confirm before pasting into a server.</li>
  <li><strong><code>*/N</code> isn't quite "every N".</strong> <code>*/15</code> in minutes = 0,15,30,45 — not 12,27,42,57. Use a list if you need a specific phase.</li>
  <li><strong>Step + range combos.</strong> <code>0-30/5</code> covers 0,5,10,15,20,25,30 only.</li>
  <li><strong>Some cron flavours add fields.</strong> Quartz cron has 6 or 7 fields (with seconds and year). systemd timers use a totally different format. This builder targets the standard 5-field crontab.</li>
  <li><strong>Friday-the-13th is hard to express in cron.</strong> Cron's day-of-month and day-of-week interact via OR, so combining them strictly requires a wrapper script.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Cron-Syntax ist dicht: fünf Felder, jeweils mit Wildcards, Ranges, Listen, Steps. Dieser Builder lässt dich mit einem Preset starten oder Felder einzeln tippen, zeigt den Cron-String, eine deutsche Erklärung und die nächsten fünf Auslösezeiten in deiner lokalen Zeitzone. Komplement: <a href="/cron-parser/">Cron-Parser</a>.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Neuer <code>crontab</code>-Eintrag, K8s <code>CronJob</code>, GitHub-Action, EventBridge.</li>
<li>"Jeden Wochentagmorgen" in Cron übersetzen.</li>
<li>Vor Deploy prüfen, ob der Ausdruck tatsächlich richtig läuft.</li>
<li>Cron-Einsteiger schulen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>DoM + DoW per OR verknüpft</strong>, nicht AND.</li>
<li><strong>Browser-Zeitzone hier</strong> — Server läuft meist in UTC.</li>
<li><strong><code>*/N</code> ist nicht exakt "alle N".</strong> Beginnt am Range-Anfang.</li>
<li><strong>Step+Range:</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30.</li>
<li><strong>Quartz/systemd haben anderes Format.</strong> Dieser Builder = 5-Felder-Crontab.</li>
<li><strong>Freitag-der-13.</strong> braucht Wrapper-Script.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>La sintaxis cron es densa: cinco campos con comodines, rangos, listas, pasos. Este constructor te permite empezar con un preset o escribir cada campo, muestra el string cron, una explicación en lenguaje natural y las próximas cinco ejecuciones en tu zona local. Complementa el <a href="/cron-parser/">Analizador de Cron</a>.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Configurar <code>crontab</code>, K8s <code>CronJob</code>, GitHub Actions, EventBridge.</li>
<li>Traducir "cada mañana laborable" a cron correcto.</li>
<li>Comprobar antes de desplegar que se ejecutará cuando esperas.</li>
<li>Enseñar cron a alguien nuevo.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>DoM + DoW se combinan con OR</strong>, no AND.</li>
<li><strong>Zona horaria del navegador aquí</strong> — el servidor suele estar en UTC.</li>
<li><strong><code>*/N</code> no es exactamente "cada N".</strong> Empieza en el límite inferior.</li>
<li><strong>Step+Rango:</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30.</li>
<li><strong>Quartz/systemd tienen formato distinto.</strong> Este constructor = crontab 5 campos.</li>
<li><strong>Viernes 13</strong> necesita script wrapper.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>La syntaxe cron est dense : cinq champs avec jokers, plages, listes, pas. Ce constructeur permet de partir d'un préréglage ou de taper chaque champ, affiche la chaîne cron, une explication en langage naturel et les cinq prochaines exécutions en heure locale. Complète l'<a href="/cron-parser/">Analyseur Cron</a>.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Configurer <code>crontab</code>, K8s <code>CronJob</code>, GitHub Actions, EventBridge.</li>
<li>Traduire « chaque matin de semaine » en cron correct.</li>
<li>Vérifier avant déploiement que ça s'exécutera quand prévu.</li>
<li>Initier quelqu'un à cron.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>DoM + DoW combinés avec OR</strong>, pas AND.</li>
<li><strong>Fuseau du navigateur ici</strong> — le serveur tourne souvent en UTC.</li>
<li><strong><code>*/N</code> n'est pas exactement « tous les N ».</strong> Commence au début de plage.</li>
<li><strong>Pas+Plage :</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30.</li>
<li><strong>Quartz/systemd ont un autre format.</strong> Ce constructeur = crontab 5 champs.</li>
<li><strong>Vendredi 13</strong> nécessite un script wrapper.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>La sintassi cron è densa: cinque campi con jolly, intervalli, liste, passi. Questo costruttore consente di partire da un preset o scrivere ogni campo, mostra la stringa cron, una spiegazione in linguaggio naturale e le prossime cinque esecuzioni in ora locale. Complementa l'<a href="/cron-parser/">Analizzatore Cron</a>.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Configurare <code>crontab</code>, K8s <code>CronJob</code>, GitHub Actions, EventBridge.</li>
<li>Tradurre "ogni mattina feriale" in cron corretto.</li>
<li>Verificare prima del deploy che eseguirà quando atteso.</li>
<li>Insegnare cron a qualcuno di nuovo.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>DoM + DoW combinati con OR</strong>, non AND.</li>
<li><strong>Fuso del browser qui</strong> — il server di solito è in UTC.</li>
<li><strong><code>*/N</code> non è esattamente "ogni N".</strong> Parte dal limite inferiore.</li>
<li><strong>Step+Range:</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30.</li>
<li><strong>Quartz/systemd hanno formato diverso.</strong> Questo costruttore = crontab 5 campi.</li>
<li><strong>Venerdì 13</strong> richiede script wrapper.</li>
</ul>
""",
    },
    "related": ["cron-parser", "timestamp-converter", "timezone-converter", "date-calculator"],
}
