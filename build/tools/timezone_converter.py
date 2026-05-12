TOOL = {
    "slug": "timezone-converter",
    "category": "data",
    "icon": "🌍",
    "tags": ["timezone", "tz", "convert", "utc", "date", "time", "iana"],
    "i18n": {
        "en": {
            "name": "Time Zone Converter",
            "tagline": "Convert a date and time between IANA time zones. See offsets, DST status, and weekday for both ends.",
            "description": "Free online time zone converter. Convert between any IANA time zones with DST awareness. Pick from common zones or any of the ~400+ supported by your browser.",
        },
        "de": {
            "name": "Zeitzonen-Konverter",
            "tagline": "Konvertiere Datum und Uhrzeit zwischen IANA-Zeitzonen. Mit Offsets, Sommerzeit und Wochentag.",
            "description": "Kostenloser Zeitzonen-Konverter. Konvertiert zwischen IANA-Zeitzonen inklusive Sommerzeit. Wähle aus gängigen oder den über 400 vom Browser unterstützten Zonen.",
        },
        "es": {
            "name": "Conversor de Zonas Horarias",
            "tagline": "Convierte fecha y hora entre zonas horarias IANA. Muestra offsets, horario de verano y día de la semana.",
            "description": "Conversor gratuito de zonas horarias. Convierte entre zonas IANA con conciencia del horario de verano. Selecciona de zonas comunes o de las 400+ del navegador.",
        },
        "fr": {
            "name": "Convertisseur de Fuseaux",
            "tagline": "Convertissez date et heure entre fuseaux horaires IANA. Affiche décalages, heure d'été et jour de la semaine.",
            "description": "Convertisseur de fuseaux horaires gratuit. Conversion entre fuseaux IANA avec gestion de l'heure d'été. Choisissez parmi les zones communes ou les 400+ supportées par votre navigateur.",
        },
        "it": {
            "name": "Convertitore Fusi Orari",
            "tagline": "Converti data e ora tra fusi orari IANA. Mostra offset, ora legale e giorno della settimana.",
            "description": "Convertitore di fusi orari gratuito. Conversione tra fusi IANA con consapevolezza dell'ora legale. Seleziona tra i fusi comuni o gli oltre 400 supportati dal browser.",
        },
        "pt": {
            "name": "Conversor de Fuso Horário",
            "tagline": "Converta uma data e hora entre fusos horários IANA. Veja offsets, status de horário de verão e dia da semana dos dois lados.",
            "description": "Conversor gratuito de fuso horário. Converta entre quaisquer fusos IANA com suporte a horário de verão. Escolha entre fusos comuns ou qualquer um dos 400+ suportados pelo seu navegador.",
        },
        "pl": {
            "name": "Konwerter Stref Czasowych",
            "tagline": "Konwertuj datę i godzinę między strefami czasowymi IANA. Zobacz offsety, status DST i dzień tygodnia po obu stronach.",
            "description": "Darmowy online konwerter stref czasowych. Konwertuj między dowolnymi strefami IANA ze świadomością DST. Wybierz spośród typowych stref albo dowolnej z 400+ obsługiwanych przez przeglądarkę.",
        },
        "ja": {
            "name": "タイムゾーン変換",
            "tagline": "IANA タイムゾーン間で日時を変換。両端のオフセット、DST の有無、曜日も表示。",
            "description": "オンライン無料のタイムゾーン変換ツール。任意の IANA タイムゾーン間で DST を考慮しながら変換できます。よく使うゾーンから、ブラウザがサポートする 400 以上のゾーンまで選択可能です。",
        },
        "nl": {"name": "Tijdzone-converter", "tagline": "Converteer een datum en tijd tussen IANA-tijdzones. Zie offsets, DST-status en weekdag voor beide kanten.", "description": "Gratis online tijdzone-converter. Converteer tussen elke IANA-tijdzone met DST-awareness. Kies uit veelgebruikte zones of een van de ~400+ die je browser ondersteunt."},
        "tr": {"name": "Saat Dilimi Dönüştürücü", "tagline": "Bir tarih ve saati IANA saat dilimleri arasında dönüştür. Her iki uç için offset, DST durumu ve haftanın gününü gör.", "description": "Ücretsiz online saat dilimi dönüştürücü. DST farkındalığıyla herhangi bir IANA saat dilimleri arasında dönüştür. Yaygın dilimlerden veya tarayıcının desteklediği ~400+ taneden birini seç."},
        "id": {"name": "Konverter Zona Waktu", "tagline": "Konversi tanggal dan waktu antara zona waktu IANA. Lihat offset, status DST, dan hari dalam minggu untuk kedua ujung.", "description": "Konverter zona waktu gratis. Konversi waktu apa pun antara zona waktu IANA (Asia/Jakarta, America/New_York, Europe/London, dll). Menampilkan offset UTC, status DST, dan hari dalam minggu untuk zona sumber dan zona target."},
        "vi": {"name": "Chuyển đổi Múi giờ", "tagline": "Chuyển ngày-giờ giữa các múi giờ IANA. Xem offset, trạng thái DST và thứ trong tuần cho cả hai đầu.", "description": "Bộ chuyển múi giờ miễn phí trực tuyến. Chuyển bất kỳ ngày-giờ nào giữa các múi giờ IANA, hiển thị UTC offset, trạng thái DST và thứ trong tuần cho cả múi giờ nguồn và đích."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Date &amp; time (in source zone)</label>
      <input type="datetime-local" id="tz-when" oninput="tzRun()" step="1">
    </div>
    <div>
      <label>{LBL_FROM} (source zone)</label>
      <select id="tz-from" onchange="tzRun()"></select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>{LBL_TO} (target zone)</label>
      <select id="tz-to" onchange="tzRun()"></select>
    </div>
    <div>
      <label>&nbsp;</label>
      <button class="secondary" onclick="tzNow()" style="width:100%">{LBL_NOW}</button>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <pre class="output" id="tz-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
const TZ_COMMON = [
  'UTC','Europe/London','Europe/Paris','Europe/Berlin','Europe/Bratislava','Europe/Madrid','Europe/Rome','Europe/Athens','Europe/Moscow',
  'Africa/Cairo','Africa/Lagos','Africa/Johannesburg',
  'Asia/Dubai','Asia/Karachi','Asia/Kolkata','Asia/Bangkok','Asia/Singapore','Asia/Shanghai','Asia/Tokyo','Asia/Seoul',
  'Australia/Perth','Australia/Sydney','Pacific/Auckland',
  'America/New_York','America/Toronto','America/Chicago','America/Denver','America/Los_Angeles','America/Anchorage','America/Sao_Paulo','America/Mexico_City'
];

function tzPopulate(){
  const local = Intl.DateTimeFormat().resolvedOptions().timeZone;
  let all = TZ_COMMON.slice();
  if (Intl.supportedValuesOf){
    try { all = Intl.supportedValuesOf('timeZone'); } catch(e){}
  }
  if (!all.includes(local)) all = [local, ...all];
  for (const sel of [document.getElementById('tz-from'), document.getElementById('tz-to')]){
    sel.innerHTML = all.map(z => `<option value="${z}">${z}</option>`).join('');
  }
  document.getElementById('tz-from').value = local;
  document.getElementById('tz-to').value = 'UTC';
}

function tzNow(){
  const d = new Date();
  const local = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.getElementById('tz-from').value = local;
  // Format current local date for datetime-local input
  const pad = n => String(n).padStart(2,'0');
  document.getElementById('tz-when').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tzRun();
}

function tzGetOffsetMinutes(date, tz){
  // Get the minutes offset of `date` (an instant) in `tz`, vs UTC
  const dtf = new Intl.DateTimeFormat('en-US', {
    timeZone: tz, hour12: false,
    year:'numeric', month:'2-digit', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit'
  });
  const parts = Object.fromEntries(dtf.formatToParts(date).filter(p=>p.type!=='literal').map(p=>[p.type,p.value]));
  const asLocal = Date.UTC(parts.year, parts.month-1, parts.day, parts.hour==='24'?0:parts.hour, parts.minute, parts.second);
  return Math.round((asLocal - date.getTime()) / 60000);
}

function tzFormatOffset(min){
  const sign = min < 0 ? '-' : '+';
  const a = Math.abs(min);
  return sign + String(Math.floor(a/60)).padStart(2,'0') + ':' + String(a%60).padStart(2,'0');
}

function tzRun(){
  const whenStr = document.getElementById('tz-when').value;
  const from = document.getElementById('tz-from').value;
  const to = document.getElementById('tz-to').value;
  const out = document.getElementById('tz-out');
  out.classList.remove('error');
  if (!whenStr || !from || !to){ out.textContent = '{LBL_NO_INPUT}'; return; }
  // Parse the wall-clock time as if it's in the source zone.
  // Strategy: build a Date from the wall-clock as if UTC, then shift by the source-zone offset.
  const m = whenStr.match(/^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2})(?::(\\d{2}))?/);
  if (!m){ out.classList.add('error'); out.textContent = 'Invalid date'; return; }
  const utcMs = Date.UTC(+m[1], +m[2]-1, +m[3], +m[4], +m[5], +(m[6]||0));
  const probe = new Date(utcMs);
  const fromOff = tzGetOffsetMinutes(probe, from);
  // The actual instant: utcMs minus the source zone offset gives the true UTC instant for the wall-clock time
  const instant = new Date(utcMs - fromOff * 60000);
  const toFmt = new Intl.DateTimeFormat(undefined, {
    timeZone: to, weekday:'short', year:'numeric', month:'short', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit', timeZoneName:'short', hour12: false
  });
  const fromFmt = new Intl.DateTimeFormat(undefined, {
    timeZone: from, weekday:'short', year:'numeric', month:'short', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit', timeZoneName:'short', hour12: false
  });
  const toOff = tzGetOffsetMinutes(instant, to);
  out.textContent =
    'Source:  ' + fromFmt.format(instant) + '\\n' +
    '         (' + from + ', UTC' + tzFormatOffset(fromOff) + ')\\n\\n' +
    'Target:  ' + toFmt.format(instant) + '\\n' +
    '         (' + to + ', UTC' + tzFormatOffset(toOff) + ')\\n\\n' +
    'Diff:    ' + Math.abs(toOff - fromOff) + ' min (' + ((toOff-fromOff)/60).toFixed(2) + ' h)\\n' +
    'UTC:     ' + instant.toISOString().replace('T',' ').slice(0,19) + 'Z\\n' +
    'Unix:    ' + Math.floor(instant.getTime()/1000);
}
document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(() => { tzPopulate(); tzNow(); }));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Time zones are deceptively annoying. A meeting at "9am" means different absolute moments in London, Bratislava, and New York — and the offset between any two of them changes twice a year because of daylight saving, on different dates. This tool takes a wall-clock time in one IANA zone and tells you the exact equivalent in another, with current offsets, the UTC instant, and the day-of-week for both ends.</p>

<h3>When to use it</h3>
<ul>
  <li>Scheduling a call across continents — confirming what "3pm CET" is in your colleague's zone.</li>
  <li>Reading a log timestamp recorded in UTC and translating it to local time for a user-facing report.</li>
  <li>Checking whether a deploy window or maintenance slot crosses a DST boundary.</li>
  <li>Sanity-checking that a cron expression in <code>America/New_York</code> fires at the moment you expect from your own zone.</li>
  <li>Working out the day-of-week change when crossing the international date line.</li>
</ul>

<h3>Why IANA zones (not "GMT+2")</h3>
<p>An IANA zone like <code>Europe/Bratislava</code> or <code>America/New_York</code> encodes the historical and ongoing rules for that location — DST start and end dates, time-zone changes (Russia abolished DST in 2014; Türkiye dropped DST in 2016), even Samoa skipping a whole day in 2011. A bare offset like "GMT+2" tells you nothing about whether DST applies, what the rule was last year, or what it'll be next year. Browsers ship the IANA database (via ICU/CLDR) and update it automatically, so the conversion stays correct over time.</p>

<h3>Common gotchas</h3>
<ul>
  <li><strong>DST transitions create ambiguous and missing times.</strong> When a clock falls back, 02:30 happens twice; when it springs forward, 02:30 doesn't exist at all. The tool picks the standard-time interpretation by default; if you need the other side, shift by an hour either way.</li>
  <li><strong>Offsets aren't constants.</strong> "CET" is UTC+1 in winter and UTC+2 in summer (CEST). The output always shows the actual offset for the date you entered, so trust the displayed offset over the abbreviation.</li>
  <li><strong>Country abbreviations are not zones.</strong> "EST" is ambiguous (US vs Australian); "IST" can mean Indian, Irish, or Israeli. Always pick the IANA zone, not the abbreviation.</li>
  <li><strong>Historical accuracy</strong> is good for the modern era but breaks down for very old dates. Pre-1970 timestamps may use approximated offsets in some browsers.</li>
  <li><strong>Storing dates: always use UTC.</strong> Convert at display time. The UTC line in the output gives you the canonical value to write to your database.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Fusos horários são surpreendentemente irritantes. Uma reunião às "9h" significa momentos absolutos diferentes em São Paulo, Lisboa e Nova York — e o offset entre quaisquer dois deles muda duas vezes por ano por causa do horário de verão, em datas diferentes. Esta ferramenta pega uma hora de relógio em um fuso IANA e diz o equivalente exato em outro, com offsets atuais, o instante UTC e o dia da semana dos dois lados.</p>

<h3>Quando usar</h3>
<ul>
  <li>Agendar uma call entre continentes — confirmar o que "15h CET" é no fuso do seu colega.</li>
  <li>Ler um timestamp de log gravado em UTC e traduzir para hora local em um relatório voltado ao usuário.</li>
  <li>Verificar se uma janela de deploy ou slot de manutenção cruza a transição do horário de verão.</li>
  <li>Conferir se uma expressão cron em <code>America/New_York</code> dispara no momento que você espera no seu próprio fuso.</li>
  <li>Descobrir a mudança de dia da semana ao cruzar a linha internacional de mudança de data.</li>
</ul>

<h3>Por que fusos IANA (não "GMT+2")</h3>
<p>Um fuso IANA como <code>America/Sao_Paulo</code> ou <code>America/New_York</code> codifica as regras históricas e atuais daquele lugar — datas de início e fim do horário de verão, mudanças de fuso (a Rússia aboliu o horário de verão em 2014; a Turquia largou em 2016), até Samoa pulando um dia inteiro em 2011. Um offset puro como "GMT+2" não te diz nada sobre se o horário de verão se aplica, qual era a regra ano passado ou qual será no próximo ano. Os navegadores trazem a base IANA (via ICU/CLDR) e atualizam automaticamente, então a conversão se mantém correta ao longo do tempo.</p>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Transições de horário de verão criam horas ambíguas e inexistentes.</strong> Quando o relógio atrasa, 02:30 acontece duas vezes; quando adianta, 02:30 não existe. A ferramenta escolhe a interpretação de horário padrão por padrão; se você precisa do outro lado, desloque uma hora para qualquer direção.</li>
  <li><strong>Offsets não são constantes.</strong> "CET" é UTC+1 no inverno e UTC+2 no verão (CEST). A saída sempre mostra o offset real para a data que você inseriu, então confie no offset exibido em vez da abreviação.</li>
  <li><strong>Abreviações de país não são fusos.</strong> "EST" é ambíguo (EUA vs Austrália); "IST" pode ser indiano, irlandês ou israelense. Sempre escolha o fuso IANA, não a abreviação.</li>
  <li><strong>A precisão histórica</strong> é boa para a era moderna, mas começa a falhar em datas muito antigas. Timestamps anteriores a 1970 podem usar offsets aproximados em alguns navegadores.</li>
  <li><strong>Armazenando datas: sempre use UTC.</strong> Converta na hora de exibir. A linha UTC na saída te dá o valor canônico para gravar no seu banco.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Strefy czasowe są zwodniczo upierdliwe. Spotkanie o "9:00" znaczy różne absolutne momenty w Warszawie, Londynie i Nowym Jorku — a offset między dowolną parą zmienia się dwa razy w roku przez DST, w różnych terminach. To narzędzie bierze czas ścienny w jednej strefie IANA i mówi ci dokładny ekwiwalent w innej, z aktualnymi offsetami, instantem UTC i dniem tygodnia po obu stronach.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Planowanie calla między kontynentami — potwierdzenie, czym jest "15:00 CET" w strefie kolegi.</li>
  <li>Czytanie timestampu z loga zapisanego w UTC i tłumaczenie go na czas lokalny do raportu user-facing.</li>
  <li>Sprawdzenie, czy okno deploya albo slot maintenance przekracza granicę DST.</li>
  <li>Sanity check, czy wyrażenie crona w <code>America/New_York</code> odpala w momencie, którego się spodziewasz w swojej strefie.</li>
  <li>Wyliczenie zmiany dnia tygodnia przy przekraczaniu international date line.</li>
</ul>

<h3>Dlaczego strefy IANA (nie "GMT+2")</h3>
<p>Strefa IANA typu <code>Europe/Warsaw</code> albo <code>America/New_York</code> koduje historyczne i bieżące reguły dla danej lokalizacji — daty rozpoczęcia i zakończenia DST, zmiany strefy (Rosja zniosła DST w 2014; Turcja porzuciła DST w 2016), nawet to, że Samoa pominęło cały dzień w 2011. Czysty offset typu "GMT+2" nic nie mówi o tym, czy DST się stosuje, jaka była reguła w zeszłym roku albo jaka będzie za rok. Przeglądarki dostarczają bazę IANA (przez ICU/CLDR) i aktualizują automatycznie, więc konwersja zostaje poprawna w czasie.</p>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Przejścia DST tworzą czasy dwuznaczne i nieistniejące.</strong> Gdy zegar się cofa, 02:30 dzieje się dwa razy; gdy się przesuwa do przodu, 02:30 nie istnieje wcale. Narzędzie domyślnie wybiera interpretację standard time; jeśli potrzebujesz drugiej strony, przesuń o godzinę w którąś stronę.</li>
  <li><strong>Offsety nie są stałe.</strong> "CET" to UTC+1 zimą i UTC+2 latem (CEST). Wyjście zawsze pokazuje faktyczny offset dla wpisanej daty — ufaj wyświetlanemu offsetowi, nie skrótowi.</li>
  <li><strong>Skróty krajów to nie strefy.</strong> "EST" jest dwuznaczne (US vs Australian); "IST" może znaczyć indyjską, irlandzką albo izraelską. Zawsze wybieraj strefę IANA, nie skrót.</li>
  <li><strong>Dokładność historyczna</strong> jest dobra dla nowoczesnej ery, ale rozjeżdża się dla bardzo starych dat. Timestampy sprzed 1970 mogą używać przybliżonych offsetów w niektórych przeglądarkach.</li>
  <li><strong>Zapisywanie dat: zawsze używaj UTC.</strong> Konwertuj przy wyświetlaniu. Linia UTC na wyjściu daje ci kanoniczną wartość do zapisu w bazie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>タイムゾーンは見た目より厄介です。「9:00」の会議は東京・ロンドン・ニューヨークでそれぞれ別の絶対時刻を意味し、しかも 2 つの間のオフセットは年に 2 回、しかも別々の日にサマータイムで変わります。本ツールはある IANA タイムゾーンの壁時計時刻を別のゾーンの正確な時刻に変換し、両端の現在オフセット、UTC 瞬時、曜日まで表示します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>大陸をまたぐ会議調整 — 「CET 15:00」が同僚のゾーンで何時かを確認したいとき。</li>
  <li>UTC で記録されたログタイムスタンプを、ユーザー向けレポート用にローカル時刻に変換したいとき。</li>
  <li>デプロイウィンドウやメンテ枠が DST 境界をまたいでいないか確認したいとき。</li>
  <li><code>America/New_York</code> の cron 式が、自分のゾーンで期待通りの時刻に発火するかサニティチェックしたいとき。</li>
  <li>国際日付変更線をまたぐときの曜日変化を計算したいとき。</li>
</ul>

<h3>なぜ IANA ゾーンか（「GMT+2」ではなく）</h3>
<p><code>Asia/Tokyo</code> や <code>America/New_York</code> のような IANA ゾーンは、その地域の歴史的・現在のルール（DST の開始終了日、タイムゾーン変更：ロシアは 2014 年に DST 廃止、トルコは 2016 年に DST 廃止、サモアは 2011 年に丸 1 日スキップなど）を網羅しています。「GMT+2」のような単純なオフセットでは、DST の有無、昨年のルール、来年のルールは分かりません。ブラウザは ICU/CLDR 経由で IANA データベースを内蔵し、自動更新されるため、変換は時間が経っても正しいままです。</p>

<h3>よくある注意点</h3>
<ul>
  <li><strong>DST の切り替え時には曖昧な時刻と存在しない時刻が生まれます。</strong> 時計が戻る時には 02:30 が 2 回、進む時には 02:30 が存在しません。本ツールはデフォルトで標準時の解釈を選びます。逆側が必要なら 1 時間ずらしてください。</li>
  <li><strong>オフセットは定数ではありません。</strong> 「CET」は冬は UTC+1、夏は UTC+2（CEST）です。出力には入力した日時に対する実オフセットが表示されるため、略称ではなく表示中のオフセットを信用してください。</li>
  <li><strong>国の略称はゾーンではありません。</strong> 「EST」は米国とオーストラリアで意味が違い、「IST」はインド・アイルランド・イスラエルで違います。略称ではなく必ず IANA ゾーンを選んでください。</li>
  <li><strong>歴史的精度</strong> は近代以降は良好ですが、非常に古い日付では崩れることがあります。1970 年以前のタイムスタンプはブラウザによって近似オフセットが使われることがあります。</li>
  <li><strong>日時の保存は常に UTC で。</strong> 表示時にローカルへ変換します。出力の UTC 行が DB に書き込むべき正準値です。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Tijdzones zijn misleidend vervelend. Een meeting om "9 uur" betekent andere absolute momenten in Londen, Amsterdam en New York — en de offset tussen twee daarvan verandert twee keer per jaar door daylight saving, op verschillende datums. Deze tool neemt een wandkloktijd in één IANA-zone en vertelt je het exacte equivalent in een andere, met huidige offsets, het UTC-moment en de weekdag voor beide kanten.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een call inplannen over continenten — bevestigen wat "15u CET" is in de zone van je collega.</li>
  <li>Een log-timestamp lezen die in UTC is opgenomen en vertalen naar lokale tijd voor een user-facing report.</li>
  <li>Checken of een deploy-window of maintenance-slot een DST-grens kruist.</li>
  <li>Sanity check dat een cron-expressie in <code>America/New_York</code> vuurt op het moment dat je verwacht vanuit je eigen zone.</li>
  <li>De weekdag-verandering uitwerken bij het kruisen van de international date line.</li>
</ul>

<h3>Waarom IANA-zones (geen "GMT+2")</h3>
<p>Een IANA-zone als <code>Europe/Amsterdam</code> of <code>America/New_York</code> codeert de historische en doorlopende regels voor die locatie — DST start- en einddatums, tijdzone-wijzigingen (Rusland schafte DST af in 2014; Turkije liet DST vallen in 2016), zelfs Samoa dat in 2011 een hele dag oversloeg. Een kale offset als "GMT+2" vertelt je niets over of DST geldt, wat de regel vorig jaar was, of wat hij volgend jaar zal zijn. Browsers shippen de IANA-database (via ICU/CLDR) en updaten 'm automatisch, zodat de conversie correct blijft over tijd.</p>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>DST-transitions maken ambigue en ontbrekende tijden.</strong> Als een klok terugvalt, gebeurt 02:30 twee keer; als hij vooruitspringt, bestaat 02:30 helemaal niet. De tool kiest standaard de standard-time-interpretatie; als je de andere kant nodig hebt, schuif met een uur naar één kant.</li>
  <li><strong>Offsets zijn geen constanten.</strong> "CET" is UTC+1 in winter en UTC+2 in zomer (CEST). De output toont altijd de daadwerkelijke offset voor de datum die je hebt ingevoerd, dus vertrouw de getoonde offset boven de afkorting.</li>
  <li><strong>Land-afkortingen zijn geen zones.</strong> "EST" is ambigu (US vs Australisch); "IST" kan Indisch, Iers of Israëlisch betekenen. Kies altijd de IANA-zone, niet de afkorting.</li>
  <li><strong>Historische accuratesse</strong> is goed voor het moderne tijdperk maar breekt af voor heel oude datums. Pre-1970 timestamps kunnen in sommige browsers benaderde offsets gebruiken.</li>
  <li><strong>Datums opslaan: altijd UTC.</strong> Converteer op display-tijd. De UTC-regel in de output geeft je de canonieke waarde om naar je database te schrijven.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Saat dilimleri aldatıcı şekilde sinir bozucudur. "09:00"da bir toplantı Londra, Bratislava ve New York'ta farklı mutlak anlamlara gelir — ve aralarındaki ofset günyaylığı tasarrufu nedeniyle yılda iki kez farklı tarihlerde değişir. Bu araç bir IANA diliminde bir duvar saati zamanı alır ve mevcut ofsetler, UTC anı ve her iki uç için haftanın günü ile başka bir dilimdeki tam eşdeğerini söyler.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Kıtalar arası bir arama planlama — "15:00 CET"in meslektaşının diliminde ne olduğunu doğrulama.</li>
  <li>UTC'de kaydedilmiş bir log timestamp'ini okuma ve kullanıcı odaklı bir rapor için yerel saate çevirme.</li>
  <li>Bir deploy penceresi veya bakım slot'unun bir DST sınırını aşıp aşmadığını kontrol etme.</li>
  <li><code>America/New_York</code>'taki bir cron ifadesinin kendi diliminden beklediğin anda çalışacağının sanity check'i.</li>
  <li>Uluslararası tarih çizgisini geçerken haftanın günü değişikliğini hesaplama.</li>
</ul>

<h3>Neden IANA dilimleri (GMT+2 değil)</h3>
<p><code>Europe/Bratislava</code> veya <code>America/New_York</code> gibi bir IANA dilimi o konumun tarihsel ve devam eden kurallarını kodlar — DST başlangıç ve bitiş tarihleri, saat dilimi değişiklikleri (Rusya 2014'te DST'yi kaldırdı; Türkiye 2016'da DST'yi düşürdü), hatta Samoa'nın 2011'de bütün bir günü atlaması. "GMT+2" gibi çıplak bir ofset sana DST'nin geçerli olup olmadığını, geçen yıl kuralın ne olduğunu veya gelecek yıl ne olacağını söylemez. Tarayıcılar IANA veritabanını (ICU/CLDR aracılığıyla) gönderir ve otomatik olarak günceller, böylece dönüşüm zamanla doğru kalır.</p>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>DST geçişleri belirsiz ve eksik zamanlar yaratır.</strong> Saat geri düştüğünde, 02:30 iki kez olur; ileri sıçradığında, 02:30 hiç olmaz. Araç varsayılan olarak standart zaman yorumunu seçer.</li>
  <li><strong>Ofsetler sabit değildir.</strong> "CET" kışın UTC+1 ve yazın UTC+2'dir (CEST). Çıktı her zaman girdiğin tarih için gerçek ofseti gösterir, bu yüzden kısaltma yerine gösterilen ofsete güven.</li>
  <li><strong>Ülke kısaltmaları dilim değildir.</strong> "EST" belirsizdir (ABD vs Avustralya); "IST" Hint, İrlanda veya İsrail anlamına gelebilir. Her zaman IANA dilimini seç, kısaltmayı değil.</li>
  <li><strong>Tarihsel doğruluk</strong> modern çağ için iyidir ama çok eski tarihler için bozulur. 1970 öncesi timestamp'lar bazı tarayıcılarda yaklaştırılmış ofsetler kullanabilir.</li>
  <li><strong>Tarihleri saklarken: her zaman UTC kullan.</strong> Gösterim zamanında çevir. Çıktıdaki UTC satırı veritabanına yazılacak kanonik değeri sana verir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Timezone itu menyebalkan secara mengejutkan. Sebuah meeting jam "9 pagi" berarti momen absolut yang berbeda di Jakarta, London, dan New York — dan offset antara dua zona berubah dua kali setahun karena daylight saving, di tanggal yang berbeda. Tool ini mengambil waktu wall-clock di satu IANA timezone dan memberitahu ekuivalen persisnya di timezone lain, dengan offset terkini, momen UTC, dan hari dalam minggu untuk kedua sisi.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Menjadwalkan call lintas benua — memastikan "15:00 CET" itu jam berapa di zona kolega kamu.</li>
  <li>Membaca timestamp log yang dicatat di UTC dan menerjemahkan ke local time untuk laporan yang dilihat user.</li>
  <li>Mengecek apakah deploy window atau slot maintenance melintasi batas DST.</li>
  <li>Sanity check bahwa cron expression di <code>America/New_York</code> akan jalan di momen yang kamu harapkan dari zone-mu sendiri.</li>
  <li>Menghitung perubahan hari ketika melintasi international date line.</li>
</ul>

<h3>Kenapa pakai IANA zone (bukan "GMT+2")</h3>
<p>IANA zone seperti <code>Europe/Bratislava</code> atau <code>America/New_York</code> meng-encode aturan historis dan yang sedang berlaku untuk lokasi tersebut — tanggal mulai dan akhir DST, perubahan timezone (Rusia menghapus DST tahun 2014; Türkiye menghapus DST tahun 2016), bahkan Samoa yang melewatkan satu hari penuh tahun 2011. Offset polos seperti "GMT+2" tidak memberitahu apa pun tentang apakah DST berlaku, apa aturannya tahun lalu, atau bagaimana tahun depan. Browser membawa database IANA (via ICU/CLDR) dan meng-update otomatis, sehingga konversi tetap benar dari waktu ke waktu.</p>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Transisi DST menciptakan waktu ambigu dan waktu yang hilang.</strong> Ketika jam mundur, 02:30 terjadi dua kali; ketika maju, 02:30 tidak pernah ada. Tool memilih interpretasi standard-time secara default; jika kamu butuh sisi lain, geser satu jam ke arah yang sesuai.</li>
  <li><strong>Offset bukan konstanta.</strong> "CET" itu UTC+1 di musim dingin dan UTC+2 di musim panas (CEST). Output selalu menampilkan offset aktual untuk tanggal yang kamu masukkan, jadi percaya pada offset yang ditampilkan, bukan singkatannya.</li>
  <li><strong>Singkatan negara bukan zona.</strong> "EST" ambigu (US vs Australia); "IST" bisa berarti India, Irlandia, atau Israel. Selalu pilih IANA zone, bukan singkatan.</li>
  <li><strong>Akurasi historis</strong> bagus untuk era modern tapi rusak untuk tanggal yang sangat lama. Timestamp pra-1970 mungkin pakai offset perkiraan di beberapa browser.</li>
  <li><strong>Menyimpan tanggal: selalu pakai UTC.</strong> Konversi saat display. Baris UTC di output memberi kamu nilai kanonik untuk ditulis ke database.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>"3pm London thứ Năm là mấy giờ ở Tokyo?" Câu trả lời phụ thuộc vào DST và quy ước múi giờ địa phương. Tool này dùng database múi giờ IANA tích hợp của trình duyệt để chuyển bất kỳ ngày-giờ nào giữa các múi giờ, hiển thị UTC offset, trạng thái DST và thứ trong tuần cho cả hai đầu.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Lên lịch họp với đồng nghiệp ở múi giờ khác.</li>
  <li>Hiểu log có timestamp UTC trong khi system của bạn ở múi giờ địa phương.</li>
  <li>Đặt cron job UTC trong khi nghĩ theo múi giờ địa phương.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>DST làm gấp đôi và bỏ qua giờ.</strong> Vào "spring forward", một giờ không tồn tại; "fall back", một giờ xảy ra hai lần. Lưu trữ ở UTC và convert chỉ ở display để tránh xung đột.</li>
  <li><strong>Tên múi giờ thay đổi.</strong> "GMT" không cập nhật DST; "BST" làm. "EST" không cập nhật DST; "EDT" làm. Để tránh lẫn lộn, dùng tên IANA (<code>Europe/London</code>, <code>America/New_York</code>) khi có thể.</li>
  <li><strong>Chính phủ thay đổi quy tắc.</strong> Múi giờ là chính trị. Brazil, Mexico và một số bang Mỹ đã thay đổi quy tắc DST gần đây — đảm bảo OS của bạn cập nhật.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "date-calculator", "cron-parser"],
    "howto": {"flow": "transform", "action": "convert", "noun": "time"},
}
