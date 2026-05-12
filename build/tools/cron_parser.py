TOOL = {
    "slug": "cron-parser",
    "category": "developer",
    "icon": "🕒",
    "tags": ["cron", "schedule", "crontab", "next run", "expression"],
    "i18n": {
        "en": {
            "name": "Cron Expression Parser",
            "tagline": "Parse cron expressions and see the next 10 fire times. Standard 5-field crontab.",
            "description": "Free online cron expression parser. Validates 5-field crontab syntax and lists the next 10 scheduled fire times in your local timezone.",
        },
        "de": {
            "name": "Cron-Ausdruck-Parser",
            "tagline": "Cron-Ausdrücke parsen und die nächsten 10 Auslösezeiten anzeigen. Standard 5-Felder-Crontab.",
            "description": "Kostenloser Cron-Ausdruck-Parser. Validiert die 5-Felder-Crontab-Syntax und listet die nächsten 10 Ausführungszeitpunkte in deiner Zeitzone.",
        },
        "es": {
            "name": "Analizador de Cron",
            "tagline": "Analiza expresiones cron y ve las próximas 10 ejecuciones. Crontab estándar de 5 campos.",
            "description": "Analizador de expresiones cron gratuito. Valida la sintaxis crontab de 5 campos y muestra las próximas 10 ejecuciones en tu zona horaria.",
        },
        "fr": {
            "name": "Analyseur Cron",
            "tagline": "Analysez les expressions cron et voyez les 10 prochaines exécutions. Crontab standard à 5 champs.",
            "description": "Analyseur d'expressions cron gratuit. Valide la syntaxe crontab à 5 champs et affiche les 10 prochaines exécutions dans votre fuseau horaire.",
        },
        "it": {
            "name": "Analizzatore Cron",
            "tagline": "Analizza espressioni cron e vedi le prossime 10 esecuzioni. Crontab standard a 5 campi.",
            "description": "Analizzatore di espressioni cron gratuito. Valida la sintassi crontab a 5 campi e mostra le prossime 10 esecuzioni nel tuo fuso orario.",
        },
        "pt": {
            "name": "Parser de Expressões Cron",
            "tagline": "Faça o parse de expressões cron e veja os próximos 10 horários de execução. Crontab padrão de 5 campos.",
            "description": "Parser online gratuito de expressões cron. Valida a sintaxe crontab de 5 campos e lista os próximos 10 horários de execução agendados no seu fuso local.",
        },
        "pl": {
            "name": "Parser Wyrażeń Cron",
            "tagline": "Sparsuj wyrażenia cron i zobacz 10 najbliższych odpaleń. Standardowy 5-polowy crontab.",
            "description": "Darmowy online parser wyrażeń cron. Waliduje składnię 5-polowego crontaba i listuje 10 najbliższych zaplanowanych odpaleń w twojej lokalnej strefie czasowej.",
        },
        "ja": {
            "name": "cron 式パーサー",
            "tagline": "cron 式をパースし、次の 10 回の発火時刻を表示。標準 5 フィールドの crontab。",
            "description": "オンライン無料の cron 式パーサー。5 フィールドの crontab 構文を検証し、ローカルタイムゾーンで次の 10 回の予定実行時刻を一覧表示します。",
        },
        "nl": {"name": "Cron Expression Parser", "tagline": "Parse cron-expressies en zie de volgende 10 fire times. Standaard 5-veld crontab.", "description": "Gratis online cron expression parser. Valideert 5-veld crontab-syntax en lijst de volgende 10 geplande fire times in je lokale tijdzone."},
        "tr": {"name": "Cron İfadesi Parser", "tagline": "Cron ifadelerini parse et ve sonraki 10 çalışma zamanını gör. Standart 5 alanlı crontab.", "description": "Ücretsiz online cron ifadesi parser. 5 alanlı crontab sözdizimini doğrular ve yerel saat diliminde planlanan sonraki 10 çalışma zamanını listeler."},
        "id": {"name": "Cron Expression Parser", "tagline": "Parse ekspresi cron dan lihat 10 waktu run berikutnya. Crontab 5-field standar.", "description": "Parser ekspresi cron gratis. Tempel ekspresi cron apa pun dan lihat 10 waktu eksekusi berikutnya dengan zona waktu yang dapat dipilih. Mendukung crontab 5-field standar dengan steps, ranges, dan list."},
        "vi": {"name": "Cron Expression Parser", "tagline": "Phân tích biểu thức cron và xem 10 lần chạy kế tiếp. Crontab 5-trường chuẩn.", "description": "Cron parser miễn phí trực tuyến. Dán biểu thức crontab 5-trường chuẩn và xem 10 lần chạy kế tiếp được tính theo múi giờ của bạn."},
    },
    "body": """
<div class="tool-card">
  <label>Cron expression (5 fields: minute hour day-of-month month day-of-week)</label>
  <input type="text" id="cron-in" oninput="cronRun()" placeholder="*/5 * * * *" value="0 9 * * 1-5" style="font-family:ui-monospace,monospace">
  <div class="button-row">
    <button class="secondary" onclick="cronSet('*/5 * * * *')">every 5 min</button>
    <button class="secondary" onclick="cronSet('0 * * * *')">hourly</button>
    <button class="secondary" onclick="cronSet('0 9 * * 1-5')">weekdays 9am</button>
    <button class="secondary" onclick="cronSet('0 0 1 * *')">1st of month</button>
    <button class="secondary" onclick="cronSet('0 2 * * 0')">Sunday 2am</button>
  </div>
  <div class="meta" id="cron-explain"></div>
</div>
<div class="tool-card">
  <label>Next 10 fire times (local timezone)</label>
  <pre class="output" id="cron-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
const FIELD_RANGES = [[0,59],[0,23],[1,31],[1,12],[0,7]]; // last 0 and 7 = Sunday
const FIELD_NAMES = ['minute','hour','day-of-month','month','day-of-week'];

function cronExpand(field, idx){
  const [lo,hi] = FIELD_RANGES[idx];
  const out = new Set();
  field.split(',').forEach(part => {
    let step = 1;
    if (part.includes('/')){ const [a,b] = part.split('/'); step = parseInt(b,10); part = a; }
    let from = lo, to = hi;
    if (part === '*'){ /* keep range */ }
    else if (part.includes('-')){ const [a,b] = part.split('-'); from = parseInt(a,10); to = parseInt(b,10); }
    else { from = to = parseInt(part,10); }
    if (isNaN(from) || isNaN(to) || from < lo || to > hi || from > to) throw new Error('Invalid value: ' + part + ' (expected ' + lo + '-' + hi + ')');
    if (isNaN(step) || step < 1) throw new Error('Invalid step: ' + step);
    for (let v = from; v <= to; v += step) out.add(idx === 4 && v === 7 ? 0 : v);
  });
  return out;
}

function cronMatches(date, sets){
  return sets[0].has(date.getMinutes())
      && sets[1].has(date.getHours())
      && sets[2].has(date.getDate())
      && sets[3].has(date.getMonth() + 1)
      && sets[4].has(date.getDay());
}

function cronNext(expr, count){
  const fields = expr.trim().split(/\\s+/);
  if (fields.length !== 5) throw new Error('Expected 5 space-separated fields, got ' + fields.length);
  const sets = fields.map((f, i) => cronExpand(f, i));
  const now = new Date();
  const start = new Date(now.getFullYear(), now.getMonth(), now.getDate(), now.getHours(), now.getMinutes() + 1, 0, 0);
  const out = [];
  let d = new Date(start);
  let safety = 0;
  while (out.length < count && safety < 600000){
    if (cronMatches(d, sets)) out.push(new Date(d));
    d.setMinutes(d.getMinutes() + 1);
    safety++;
  }
  if (safety >= 600000) throw new Error('Search exhausted (no matches in next ~1 year)');
  return out;
}

function cronExplain(expr){
  // Very brief human-readable summary
  const parts = expr.trim().split(/\\s+/);
  if (parts.length !== 5) return '';
  const m = parts[0], h = parts[1], dom = parts[2], mon = parts[3], dow = parts[4];
  let s = 'At ';
  if (m === '*') s += 'every minute';
  else if (m.startsWith('*/')) s += 'every ' + m.slice(2) + ' minutes';
  else s += 'minute ' + m;
  s += ', ';
  if (h === '*') s += 'every hour';
  else if (h.startsWith('*/')) s += 'every ' + h.slice(2) + ' hours';
  else s += 'hour ' + h;
  if (dow !== '*'){
    const names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    if (dow.includes('-')){
      const [a,b] = dow.split('-').map(x => parseInt(x,10));
      s += ', on ' + names[a] + '-' + names[b];
    } else if (!isNaN(parseInt(dow,10))){
      s += ', on ' + names[parseInt(dow,10) % 7];
    }
  }
  if (dom !== '*'){
    s += ', on day ' + dom + ' of the month';
  }
  if (mon !== '*'){
    s += ', in month ' + mon;
  }
  return s + '.';
}

function cronRun(){
  const expr = document.getElementById('cron-in').value;
  const out = document.getElementById('cron-out');
  const exp = document.getElementById('cron-explain');
  out.classList.remove('error');
  if (!expr.trim()){ out.textContent = '{LBL_NO_INPUT}'; exp.textContent = ''; return; }
  try {
    const dates = cronNext(expr, 10);
    out.textContent = dates.map((d,i) => (i+1).toString().padStart(2,' ') + '.  ' + d.toLocaleString(undefined,{weekday:'short', year:'numeric', month:'short', day:'2-digit', hour:'2-digit', minute:'2-digit'})).join('\\n');
    exp.textContent = cronExplain(expr);
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + e.message;
    exp.textContent = '';
  }
}
function cronSet(s){ document.getElementById('cron-in').value = s; cronRun(); }
document.addEventListener('DOMContentLoaded', cronRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Cron expressions are powerful and easy to mis-write. <code>0 0 * * 1-5</code> looks like a weekday-at-midnight schedule and is. <code>*/15 0-9 * * *</code> looks like every fifteen minutes during business hours and is. <code>0 0 1 */3 *</code> looks like quarterly... if you remembered <code>*/3</code> means "every third month". This tool lets you paste an expression, see what it actually means in plain English, and preview the next 10 fire times so you can confirm before deploying.</p>

<h3>When to use it</h3>
<ul>
  <li>Sanity-checking a cron line in <code>crontab -e</code> before saving.</li>
  <li>Translating a Kubernetes <code>CronJob</code> schedule string into "what time will this actually run?".</li>
  <li>Designing a new schedule — start with English ("every weekday morning") and iterate the expression until the preview matches.</li>
  <li>Debugging a job that "didn't run when I expected" — paste the schedule, look at the next 10 times, see whether reality is the surprise or the expression is.</li>
</ul>

<h3>Cron field reference</h3>
<table>
  <tr><th>Field</th><th>Range</th><th>Wildcards</th></tr>
  <tr><td>Minute</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Hour</td><td>0-23</td><td>same</td></tr>
  <tr><td>Day of month</td><td>1-31</td><td>same</td></tr>
  <tr><td>Month</td><td>1-12</td><td>same</td></tr>
  <tr><td>Day of week</td><td>0-6 (0 = Sunday, 7 also = Sunday)</td><td>same</td></tr>
</table>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Day-of-month + day-of-week interact.</strong> If both are restricted (e.g. <code>15 * * * 1</code> meaning "the 15th OR a Monday"), most cron implementations OR them. This tool follows that convention.</li>
  <li><strong><code>*/N</code> isn't quite "every N".</strong> It's "every N starting from the lower bound", so <code>*/15</code> in minute = 0,15,30,45 (not 12,27,42,57). To start later, use a list: <code>5,20,35,50</code>.</li>
  <li><strong>Step + range combos.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. The step applies inside the range only.</li>
  <li><strong>Timezone is browser-local here.</strong> Real cron daemons run in server time (often UTC). A schedule that looks fine in your browser may fire at a different wall-clock time on the server. Confirm timezone before pasting.</li>
  <li><strong>Some cron flavours add fields.</strong> Quartz cron has 6 or 7 fields (with seconds and year). systemd timers use a different format entirely. This tool parses standard 5-field crontab.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Expressões cron são poderosas e fáceis de escrever errado. <code>0 0 * * 1-5</code> parece um agendamento de meia-noite em dias úteis e é. <code>*/15 0-9 * * *</code> parece a cada quinze minutos durante o horário comercial e é. <code>0 0 1 */3 *</code> parece trimestral... se você lembrou que <code>*/3</code> significa "a cada terceiro mês". Esta ferramenta deixa você colar uma expressão, ver o que ela de fato significa em português claro e prever os próximos 10 horários de execução para confirmar antes do deploy.</p>

<h3>Quando usar</h3>
<ul>
  <li>Conferir uma linha cron em <code>crontab -e</code> antes de salvar.</li>
  <li>Traduzir uma string de agendamento de <code>CronJob</code> do Kubernetes em "que horas isso vai rodar de verdade?".</li>
  <li>Projetar um novo agendamento — comece em português ("toda manhã de dia útil") e itere a expressão até o preview bater.</li>
  <li>Debugar um job que "não rodou quando eu esperava" — cole o schedule, olhe os próximos 10 horários e veja se a surpresa é a realidade ou a expressão.</li>
</ul>

<h3>Referência dos campos cron</h3>
<table>
  <tr><th>Campo</th><th>Range</th><th>Wildcards</th></tr>
  <tr><td>Minuto</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Hora</td><td>0-23</td><td>idem</td></tr>
  <tr><td>Dia do mês</td><td>1-31</td><td>idem</td></tr>
  <tr><td>Mês</td><td>1-12</td><td>idem</td></tr>
  <tr><td>Dia da semana</td><td>0-6 (0 = domingo, 7 também = domingo)</td><td>idem</td></tr>
</table>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Dia do mês + dia da semana interagem.</strong> Se ambos estão restritos (ex.: <code>15 * * * 1</code> significando "o dia 15 OU uma segunda-feira"), a maioria das implementações de cron faz OR. Esta ferramenta segue essa convenção.</li>
  <li><strong><code>*/N</code> não é exatamente "a cada N".</strong> É "a cada N começando do limite inferior", então <code>*/15</code> em minuto = 0,15,30,45 (não 12,27,42,57). Para começar depois, use uma lista: <code>5,20,35,50</code>.</li>
  <li><strong>Combinações step + range.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. O step se aplica só dentro do range.</li>
  <li><strong>O fuso horário aqui é o local do navegador.</strong> Daemons cron reais rodam no horário do servidor (frequentemente UTC). Um agendamento que parece certo no seu navegador pode disparar num horário diferente no servidor. Confirme o fuso antes de colar.</li>
  <li><strong>Alguns dialetos de cron adicionam campos.</strong> O cron do Quartz tem 6 ou 7 campos (com segundos e ano). Timers do systemd usam um formato totalmente diferente. Esta ferramenta faz o parse do crontab padrão de 5 campos.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Wyrażenia cron są potężne i łatwo je źle napisać. <code>0 0 * * 1-5</code> wygląda jak harmonogram "o północy w dni robocze" — i tym jest. <code>*/15 0-9 * * *</code> wygląda jak "co 15 minut w godzinach pracy" — i tym jest. <code>0 0 1 */3 *</code> wygląda jak "kwartalnie"... jeśli pamiętałeś, że <code>*/3</code> znaczy "co trzeci miesiąc". To narzędzie pozwala wkleić wyrażenie, zobaczyć, co ono naprawdę znaczy po polsku, i podejrzeć 10 najbliższych odpaleń, żebyś mógł zweryfikować przed deployem.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Sanity check linii crona w <code>crontab -e</code> przed zapisem.</li>
  <li>Tłumaczenie schedule'a z <code>CronJob</code> w Kubernetesie na "o której to faktycznie odpali?".</li>
  <li>Projektowanie nowego harmonogramu — zacznij od polskiego ("rano w każdy dzień roboczy") i iteruj wyrażenie, aż podgląd się zgodzi.</li>
  <li>Debug joba, który "nie odpalił, kiedy się spodziewałem" — wklej schedule, spójrz na 10 najbliższych odpaleń i zobacz, czy zaskoczeniem jest rzeczywistość, czy wyrażenie.</li>
</ul>

<h3>Referencja pól crona</h3>
<table>
  <tr><th>Pole</th><th>Zakres</th><th>Wildcardy</th></tr>
  <tr><td>Minuta</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Godzina</td><td>0-23</td><td>tak samo</td></tr>
  <tr><td>Dzień miesiąca</td><td>1-31</td><td>tak samo</td></tr>
  <tr><td>Miesiąc</td><td>1-12</td><td>tak samo</td></tr>
  <tr><td>Dzień tygodnia</td><td>0-6 (0 = niedziela, 7 też = niedziela)</td><td>tak samo</td></tr>
</table>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Day-of-month i day-of-week wchodzą w interakcję.</strong> Jeśli oba są ograniczone (np. <code>15 * * * 1</code> znaczy "15. dzień LUB poniedziałek"), większość implementacji crona robi OR. To narzędzie trzyma się tej konwencji.</li>
  <li><strong><code>*/N</code> nie znaczy dokładnie "co N".</strong> To "co N zaczynając od dolnej granicy", więc <code>*/15</code> w minutach = 0,15,30,45 (nie 12,27,42,57). Żeby zacząć później, użyj listy: <code>5,20,35,50</code>.</li>
  <li><strong>Kombinacje step + range.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. Krok działa tylko wewnątrz zakresu.</li>
  <li><strong>Strefa czasowa to tu lokalna strefa przeglądarki.</strong> Prawdziwe demony cron działają w czasie serwera (często UTC). Schedule, który wygląda OK w przeglądarce, może odpalić o innej godzinie ściennej na serwerze. Zweryfikuj strefę przed wklejeniem.</li>
  <li><strong>Niektóre dialekty crona dodają pola.</strong> Quartz cron ma 6 albo 7 pól (z sekundami i rokiem). Timery systemd używają zupełnie innego formatu. To narzędzie parsuje standardowy 5-polowy crontab.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>cron 式は強力ですが、書き間違いも起こしやすい構文です。<code>0 0 * * 1-5</code> は「平日の真夜中」に見えますし、実際にそうです。<code>*/15 0-9 * * *</code> は「営業時間中の 15 分ごと」に見えますし、実際にそうです。<code>0 0 1 */3 *</code> は四半期ごとに見えますが、それは <code>*/3</code> が「3 か月ごと」を意味することを覚えていればの話です。本ツールは式を貼り付けると、その実際の意味を平易な言葉で示し、次の 10 回の発火時刻をプレビューしてデプロイ前に確認できるようにします。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li><code>crontab -e</code> で書いた cron 行を保存前にサニティチェックしたいとき。</li>
  <li>Kubernetes の <code>CronJob</code> のスケジュール文字列を「実際に何時に走るか？」に翻訳したいとき。</li>
  <li>新しいスケジュールの設計 — 「平日の朝」のような言葉から始めて、プレビューが一致するまで式を反復するとき。</li>
  <li>「思った時刻に実行されなかった」ジョブのデバッグ — スケジュールを貼り、次の 10 回を見比べて、現実と式のどちらが意外なのかを切り分けます。</li>
</ul>

<h3>cron フィールドリファレンス</h3>
<table>
  <tr><th>フィールド</th><th>範囲</th><th>ワイルドカード</th></tr>
  <tr><td>分</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>時</td><td>0-23</td><td>同じ</td></tr>
  <tr><td>日</td><td>1-31</td><td>同じ</td></tr>
  <tr><td>月</td><td>1-12</td><td>同じ</td></tr>
  <tr><td>曜日</td><td>0-6（0 = 日曜、7 も日曜）</td><td>同じ</td></tr>
</table>

<h3>よくある注意点</h3>
<ul>
  <li><strong>day-of-month と day-of-week は相互作用します。</strong> 両方が制限されている場合（例：<code>15 * * * 1</code> は「15 日 OR 月曜」）、多くの cron 実装は OR で結合します。本ツールもこれに従います。</li>
  <li><strong><code>*/N</code> は「N ごと」とは少し異なります。</strong> 「下限から N 刻み」なので、分の <code>*/15</code> は 0,15,30,45 になります（12,27,42,57 ではありません）。後ろから始めたい場合はリストを使ってください：<code>5,20,35,50</code>。</li>
  <li><strong>step + range の組み合わせ。</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30。step は範囲内のみに適用されます。</li>
  <li><strong>タイムゾーンはブラウザのローカルです。</strong> 実際の cron デーモンはサーバー時間（多くは UTC）で動きます。ブラウザでは正しく見えても、サーバーでは別の壁時計時刻に発火することがあります。貼り付ける前に確認してください。</li>
  <li><strong>cron の方言にはフィールドが多いものがあります。</strong> Quartz cron は秒と年を含む 6〜7 フィールド、systemd タイマーは全く別の形式です。本ツールは標準 5 フィールドの crontab を解析します。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Cron-expressies zijn krachtig en makkelijk verkeerd te schrijven. <code>0 0 * * 1-5</code> lijkt op een weekdag-om-middernacht schedule en is dat ook. <code>*/15 0-9 * * *</code> lijkt elke vijftien minuten tijdens kantooruren en is dat ook. <code>0 0 1 */3 *</code> lijkt op kwartaals... als je je herinnert dat <code>*/3</code> "elke derde maand" betekent. Met deze tool kun je een expressie plakken, zien wat-ie echt betekent in gewoon Nederlands, en de volgende 10 fire times previewen zodat je kunt bevestigen voor je deployt.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Sanity check op een cron-regel in <code>crontab -e</code> voor opslaan.</li>
  <li>Een Kubernetes <code>CronJob</code> schedule-string vertalen naar "hoe laat draait dit eigenlijk?".</li>
  <li>Een nieuwe schedule ontwerpen — start met Nederlands ("elke werkdag-ochtend") en itereer de expressie tot de preview matcht.</li>
  <li>Een job debuggen die "niet draaide toen ik dacht" — plak de schedule, kijk naar de volgende 10 tijden, zie of de realiteit de verrassing is of de expressie.</li>
</ul>

<h3>Cron-veld referentie</h3>
<table>
  <tr><th>Veld</th><th>Range</th><th>Wildcards</th></tr>
  <tr><td>Minuut</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Uur</td><td>0-23</td><td>idem</td></tr>
  <tr><td>Day of month</td><td>1-31</td><td>idem</td></tr>
  <tr><td>Maand</td><td>1-12</td><td>idem</td></tr>
  <tr><td>Day of week</td><td>0-6 (0 = zondag, 7 ook = zondag)</td><td>idem</td></tr>
</table>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Day-of-month + day-of-week interacteren.</strong> Als beide beperkt zijn (bijv. <code>15 * * * 1</code> oftewel "de 15e OF een maandag"), OR'en de meeste cron-implementaties ze. Deze tool volgt die conventie.</li>
  <li><strong><code>*/N</code> is niet helemaal "elke N".</strong> Het is "elke N startend bij de ondergrens", dus <code>*/15</code> in minuut = 0,15,30,45 (niet 12,27,42,57). Om later te beginnen, gebruik een lijst: <code>5,20,35,50</code>.</li>
  <li><strong>Step + range combinaties.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. De step werkt alleen binnen de range.</li>
  <li><strong>Tijdzone is hier browser-lokaal.</strong> Echte cron-daemons draaien in servertijd (vaak UTC). Een schedule die in je browser prima lijkt, kan op de server op een andere wandkloktijd vuren. Bevestig de tijdzone voor je plakt.</li>
  <li><strong>Sommige cron-varianten voegen velden toe.</strong> Quartz cron heeft 6 of 7 velden (met seconden en jaar). systemd timers gebruiken een heel ander formaat. Deze tool parset standaard 5-veld crontab.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Cron ifadeleri güçlüdür ve yanlış yazılması kolaydır. <code>0 0 * * 1-5</code> hafta içi gece yarısı zaman çizelgesi gibi görünür ve öyledir. <code>*/15 0-9 * * *</code> mesai saatlerinde her on beş dakikada gibi görünür ve öyledir. <code>0 0 1 */3 *</code> üç ayda bir gibi görünür... <code>*/3</code>'ün "her üçüncü ay" anlamına geldiğini hatırladıysan. Bu araç bir ifade yapıştırmana, gerçekten ne anlama geldiğini sade dilde görmene ve deploy etmeden önce doğrulamak için sonraki 10 çalışma zamanını önizlemene izin verir.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Kaydetmeden önce <code>crontab -e</code>'deki bir cron satırının sanity check'i.</li>
  <li>Kubernetes <code>CronJob</code> zaman çizelgesi string'ini "bu gerçekten ne zaman çalışacak?" diye çevirme.</li>
  <li>Yeni bir zaman çizelgesi tasarlama — İngilizce ile başla ("her hafta içi sabah") ve önizleme eşleşene kadar ifadeyi yinele.</li>
  <li>"Beklediğim zaman çalışmadı" diye debug'lanan bir iş — zaman çizelgesini yapıştır, sonraki 10 zamana bak, sürprizin gerçeklik mi yoksa ifade mi olduğunu gör.</li>
</ul>

<h3>Cron alan referansı</h3>
<table>
  <tr><th>Alan</th><th>Aralık</th><th>Joker</th></tr>
  <tr><td>Dakika</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Saat</td><td>0-23</td><td>aynı</td></tr>
  <tr><td>Ayın günü</td><td>1-31</td><td>aynı</td></tr>
  <tr><td>Ay</td><td>1-12</td><td>aynı</td></tr>
  <tr><td>Haftanın günü</td><td>0-6 (0 = Pazar, 7 de = Pazar)</td><td>aynı</td></tr>
</table>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Day-of-month + day-of-week etkileşir.</strong> Her ikisi de kısıtlanmışsa (örn. <code>15 * * * 1</code> "15'inde VEYA Pazartesi" anlamında), çoğu cron uygulaması bunları OR'lar. Bu araç bu geleneği izler.</li>
  <li><strong><code>*/N</code> tam olarak "her N" değildir.</strong> "Alt sınırdan başlayarak her N"dir, bu yüzden dakikada <code>*/15</code> = 0,15,30,45 (12,27,42,57 değil). Sonra başlatmak için liste kullan: <code>5,20,35,50</code>.</li>
  <li><strong>Adım + aralık kombinasyonları.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. Adım sadece aralık içinde geçerlidir.</li>
  <li><strong>Saat dilimi burada tarayıcının yerel dilimidir.</strong> Gerçek cron daemon'ları sunucu zamanında (genellikle UTC) çalışır. Tarayıcında iyi görünen bir zaman çizelgesi sunucuda farklı saatte çalışabilir.</li>
  <li><strong>Bazı cron lehçeleri alan ekler.</strong> Quartz cron 6 veya 7 alana sahiptir (saniyeler ve yıl ile). systemd timer'lar tamamen farklı bir biçim kullanır. Bu araç standart 5 alanlı crontab'ı parse eder.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Ekspresi cron itu kuat dan mudah salah tulis. <code>0 0 * * 1-5</code> kelihatan seperti schedule tengah malam di hari kerja, dan memang begitu. <code>*/15 0-9 * * *</code> kelihatan seperti setiap lima belas menit di jam kerja, dan memang begitu. <code>0 0 1 */3 *</code> kelihatan seperti tiap kuartal... kalau kamu ingat bahwa <code>*/3</code> berarti "tiap bulan ketiga". Tool ini memungkinkan kamu menempel ekspresi, melihat artinya dalam bahasa sederhana, dan mempreview 10 waktu run berikutnya untuk memvalidasinya sebelum deploy.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Sanity check baris cron di <code>crontab -e</code> sebelum disimpan.</li>
  <li>Menerjemahkan schedule string Kubernetes <code>CronJob</code> ke "kapan sebenarnya ini akan jalan?"</li>
  <li>Mendesain schedule baru — mulai dengan kalimat bahasa Inggris ("setiap pagi hari kerja") dan iterasi ekspresinya sampai preview cocok.</li>
  <li>Mendebug job yang "tidak jalan saat seharusnya" — tempel schedule-nya, lihat 10 waktu berikutnya, lihat apakah kejutannya berasal dari kenyataan atau dari ekspresi.</li>
</ul>

<h3>Referensi field cron</h3>
<table>
  <tr><th>Field</th><th>Range</th><th>Wildcard</th></tr>
  <tr><td>Menit</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Jam</td><td>0-23</td><td>sama</td></tr>
  <tr><td>Day of month</td><td>1-31</td><td>sama</td></tr>
  <tr><td>Bulan</td><td>1-12</td><td>sama</td></tr>
  <tr><td>Day of week</td><td>0-6 (0 = Minggu, 7 juga = Minggu)</td><td>sama</td></tr>
</table>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Day-of-month + day-of-week berinteraksi.</strong> Kalau keduanya dibatasi (mis. <code>15 * * * 1</code> berarti "tanggal 15 ATAU hari Senin"), kebanyakan implementasi cron meng-OR keduanya. Tool ini mengikuti konvensi tersebut.</li>
  <li><strong><code>*/N</code> bukan persis "setiap N".</strong> Ini "setiap N mulai dari batas bawah", jadi <code>*/15</code> di menit = 0,15,30,45 (bukan 12,27,42,57). Untuk mulai belakangan, pakai list: <code>5,20,35,50</code>.</li>
  <li><strong>Kombinasi step + range.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. Step hanya berlaku dalam range.</li>
  <li><strong>Timezone di sini adalah zona lokal browser.</strong> Daemon cron sungguhan jalan di server time (sering UTC). Schedule yang tampak baik di browser-mu bisa jalan di waktu wall-clock berbeda di server.</li>
  <li><strong>Beberapa dialek cron menambah field.</strong> Quartz cron punya 6 atau 7 field (dengan detik dan tahun). systemd timer pakai format yang sama sekali berbeda. Tool ini mem-parse crontab standar 5-field.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Một biểu thức cron như <code>0 2 * * 1-5</code> không cho bạn biết khi nào nó sẽ chạy tiếp theo — chỉ là khi nào nó <em>khớp</em>. Để biết các lần chạy thực tế bạn cần kết hợp cú pháp với một múi giờ và lịch dương lịch. Tool này phân tích bất kỳ biểu thức crontab 5-trường tiêu chuẩn nào và liệt kê 10 lần khớp tiếp theo bắt đầu từ "bây giờ".</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Xác nhận cron job mới sẽ kích hoạt khi bạn nghĩ — đặc biệt khi giáp ranh DST.</li>
  <li>Diễn giải cron không quen thuộc trong codebase được kế thừa.</li>
  <li>Cảnh báo trên oncall rotation gặp một cron bí ẩn và bạn cần biết "tôi có bao nhiêu thời gian trước lần chạy tiếp theo?"</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Lần chạy tiếp theo phụ thuộc vào múi giờ.</strong> Cron không có múi giờ tích hợp; máy chủ điều hành nó quyết định. Tool này hiển thị lần chạy trong múi giờ trình duyệt cục bộ của bạn — kiểm tra cài đặt của runner.</li>
  <li><strong>Phương ngữ năm trường.</strong> Cron POSIX là 5 trường (phút giờ ngày tháng dow). Spring/Quartz/AWS thêm trường giây hoặc năm. Đảm bảo phương ngữ bạn dán khớp.</li>
  <li><strong>Trường tháng và ngày-trong-tuần OR.</strong> Khi cả hai được hạn chế, cron POSIX khớp <em>hoặc</em> — không phải cả hai. Vì vậy <code>0 0 1 * 0</code> chạy vào ngày 1 của mỗi tháng <em>và</em> mỗi Chủ Nhật.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "timezone-converter", "date-calculator"],
    "howto": {"flow": "transform", "action": "convert", "noun": "cron expression"},
}
