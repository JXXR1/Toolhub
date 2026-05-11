TOOL = {
    "slug": "timestamp-converter",
    "category": "developer",
    "icon": "🕐",
    "tags": ["timestamp", "unix", "epoch", "date", "convert", "iso8601"],
    "i18n": {
        "en": {
            "name": "Unix Timestamp Converter",
            "tagline": "Convert between Unix timestamps and human-readable dates. Seconds and milliseconds, UTC and local.",
            "description": "Free online Unix timestamp converter. Convert between epoch seconds, milliseconds, ISO 8601, and human-readable dates in UTC or local time.",
        },
        "de": {"name": "Unix-Zeitstempel-Konverter", "tagline": "Konvertiere zwischen Unix-Zeitstempeln und lesbarem Datum. Sekunden und Millisekunden, UTC und lokal.", "description": "Kostenloser Unix-Zeitstempel-Konverter. Konvertiere zwischen Epoch-Sekunden, Millisekunden, ISO 8601 und lesbarem Datum."},
        "es": {"name": "Conversor de Timestamp Unix", "tagline": "Convierte entre timestamps Unix y fechas legibles. Segundos y milisegundos, UTC y local.", "description": "Conversor gratuito de timestamps Unix. Convierte entre segundos epoch, milisegundos, ISO 8601 y fechas legibles."},
        "fr": {"name": "Convertisseur Timestamp Unix", "tagline": "Convertissez entre timestamps Unix et dates lisibles. Secondes et millisecondes, UTC et local.", "description": "Convertisseur de timestamp Unix gratuit. Conversion entre secondes epoch, millisecondes, ISO 8601 et dates lisibles."},
        "it": {"name": "Convertitore Timestamp Unix", "tagline": "Converti tra timestamp Unix e date leggibili. Secondi e millisecondi, UTC e locale.", "description": "Convertitore gratuito di timestamp Unix. Conversione tra secondi epoch, millisecondi, ISO 8601 e date leggibili."},
        "pt": {"name": "Conversor de Timestamp Unix", "tagline": "Converta entre timestamps Unix e datas legíveis. Segundos e milissegundos, UTC e local.", "description": "Conversor gratuito de timestamp Unix. Converta entre segundos epoch, milissegundos, ISO 8601 e datas legíveis em UTC ou hora local."},
        "pl": {"name": "Konwerter Unix Timestamp", "tagline": "Konwertuj między Unix timestampami a datami czytelnymi dla człowieka. Sekundy i milisekundy, UTC i lokalna.", "description": "Darmowy online konwerter Unix timestampów. Konwertuj między epoch w sekundach, milisekundach, ISO 8601 i datami czytelnymi dla człowieka w UTC albo czasie lokalnym."},
        "ja": {"name": "Unix タイムスタンプ変換", "tagline": "Unix タイムスタンプと人間可読な日時を相互変換。秒・ミリ秒、UTC・ローカルに対応。", "description": "オンライン無料の Unix タイムスタンプ変換ツール。エポック秒、ミリ秒、ISO 8601、UTC およびローカル時刻の人間可読な日時間で変換できます。"},
        "nl": {"name": "Unix Timestamp Converter", "tagline": "Converteer tussen Unix-timestamps en menselijk leesbare datums. Seconds en milliseconds, UTC en lokaal.", "description": "Gratis online Unix timestamp converter. Converteer tussen epoch seconds, milliseconds, ISO 8601 en menselijk leesbare datums in UTC of lokale tijd."},
        "tr": {"name": "Unix Timestamp Dönüştürücü", "tagline": "Unix timestamp'leri ile insan tarafından okunabilir tarihler arasında dönüştür. Saniyeler ve milisaniyeler, UTC ve yerel.", "description": "Ücretsiz online Unix timestamp dönüştürücü. Epoch saniyeleri, milisaniyeler, ISO 8601 ve UTC veya yerel saatte insan tarafından okunabilir tarihler arasında dönüştür."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Unix timestamp</label>
      <input type="text" id="ts-num" oninput="tsFromNum()" placeholder="1704067200 or 1704067200000" style="font-family:ui-monospace,monospace">
      <div class="meta">Auto-detects seconds vs milliseconds</div>
    </div>
    <div>
      <label>Date &amp; time</label>
      <input type="datetime-local" id="ts-date" step="1" oninput="tsFromDate()">
      <div class="meta">Local timezone</div>
    </div>
  </div>
  <div class="button-row">
    <button onclick="tsNow()">{LBL_NOW}</button>
    <button class="secondary" onclick="document.getElementById('ts-num').value=''; tsRender(null)">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>Result</label>
  <pre class="output" id="ts-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function tsRender(d){
  const out = document.getElementById('ts-out');
  if (!d){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const ms = d.getTime();
  const sec = Math.floor(ms / 1000);
  const iso = d.toISOString();
  const local = d.toLocaleString(undefined, { weekday:'long', year:'numeric', month:'short', day:'2-digit', hour:'2-digit', minute:'2-digit', second:'2-digit' });
  const utc = d.toUTCString();
  // Relative
  const now = Date.now();
  const diffMs = ms - now;
  const abs = Math.abs(diffMs);
  let rel;
  const sec_ = Math.floor(abs/1000), min = Math.floor(sec_/60), hr = Math.floor(min/60), day = Math.floor(hr/24), yr = Math.floor(day/365);
  if (yr) rel = yr + 'y ' + (day - yr*365) + 'd';
  else if (day) rel = day + 'd ' + (hr - day*24) + 'h';
  else if (hr) rel = hr + 'h ' + (min - hr*60) + 'm';
  else if (min) rel = min + 'm ' + (sec_ - min*60) + 's';
  else rel = sec_ + 's';
  rel += diffMs >= 0 ? ' from now' : ' ago';
  out.textContent =
    'Unix seconds:       ' + sec + '\\n' +
    'Unix milliseconds:  ' + ms + '\\n' +
    'ISO 8601 (UTC):     ' + iso + '\\n' +
    'UTC:                ' + utc + '\\n' +
    'Local:              ' + local + '\\n' +
    'Relative:           ' + rel;
}
function tsFromNum(){
  const v = document.getElementById('ts-num').value.trim();
  if (!v){ tsRender(null); return; }
  const n = Number(v);
  if (!isFinite(n)){ tsRender(null); return; }
  // Heuristic: <= 10 digits = seconds, else ms
  const ms = (Math.abs(n) >= 1e12) ? n : (Math.abs(n) >= 1e10 ? n : n * 1000);
  const d = new Date(ms);
  // Update date input
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
function tsFromDate(){
  const v = document.getElementById('ts-date').value;
  if (!v){ tsRender(null); return; }
  const d = new Date(v);
  if (isNaN(d.getTime())){ tsRender(null); return; }
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  tsRender(d);
}
function tsNow(){
  const d = new Date();
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
document.addEventListener('DOMContentLoaded', tsNow);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A Unix timestamp is a single integer — the number of seconds (or milliseconds) since 1970-01-01 00:00:00 UTC. They're everywhere: log files, API responses, JWT <code>iat</code>/<code>exp</code> claims, database <code>created_at</code> columns, cache headers. They're unambiguous and timezone-free, but not human-readable, so when something breaks at <code>1735689600</code>, you need to know whether that's 2pm or 4am, today or last year. This tool flips between the integer form and the readable form in both directions, with seconds/ms auto-detection and a relative-time hint.</p>

<h3>When to use it</h3>
<ul>
  <li>Decoding a <code>"timestamp": 1735689600</code> field from a log entry or API response.</li>
  <li>Checking when a JWT was issued or when it expires (<code>iat</code> / <code>exp</code> claims are seconds-since-epoch).</li>
  <li>Calculating a future timestamp for a <code>retry-after</code> header, scheduled job, or cache TTL.</li>
  <li>Sanity-checking whether a date stored in a database is in seconds, milliseconds, or microseconds.</li>
  <li>Converting "now" into the format your tool of the moment wants.</li>
</ul>

<h3>Seconds, milliseconds, microseconds</h3>
<ul>
  <li><strong>Seconds</strong> — the original Unix convention; ~10 digits today (e.g. <code>1735689600</code>). Used in C, Linux, JWT, most APIs, most database <code>integer</code> columns.</li>
  <li><strong>Milliseconds</strong> — JavaScript's <code>Date.now()</code>, Java <code>System.currentTimeMillis()</code>, Kafka, many JSON APIs. ~13 digits.</li>
  <li><strong>Microseconds (16 digits) / nanoseconds (19 digits)</strong> — Python <code>time.time_ns()</code>, Go <code>time.Now().UnixNano()</code>, some metrics systems. This tool doesn't auto-handle them — divide by 1,000 or 1,000,000 first.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>The Year 2038 problem.</strong> Signed 32-bit timestamps overflow at <code>2147483647</code> = <strong>03:14:07 UTC, 19 January 2038</strong>. Old C code, MySQL <code>TIMESTAMP</code> columns, and embedded systems can wrap to 1901. Modern systems use 64-bit and are fine until ~year 292,277,026,596.</li>
  <li><strong>Unix time skips leap seconds.</strong> A Unix day is exactly 86,400 seconds, even when UTC has 86,401. This is by design (it keeps arithmetic simple) but means you can't use Unix timestamps for sub-second-accurate astronomy or GPS.</li>
  <li><strong>Negative timestamps</strong> are valid and represent dates before 1970. Some libraries reject them — test before relying on it.</li>
  <li><strong>Auto-detection isn't foolproof.</strong> A 10-digit value <em>could</em> be a millisecond timestamp from 1970 — vanishingly unlikely in practice, but if you know which unit you have, don't rely on the heuristic.</li>
  <li><strong>Always store UTC.</strong> Timestamps are timezone-free; "local time" is for display only. The "Local" line in the output uses your browser's zone, but the underlying integer is always UTC.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um timestamp Unix é um único inteiro — o número de segundos (ou milissegundos) desde 1970-01-01 00:00:00 UTC. Eles estão em todo lugar: arquivos de log, respostas de API, claims <code>iat</code>/<code>exp</code> de JWT, colunas <code>created_at</code> em banco, headers de cache. São inequívocos e sem timezone, mas não são legíveis por humanos, então quando algo quebra em <code>1735689600</code>, você precisa saber se é 14h ou 4h da manhã, hoje ou ano passado. Esta ferramenta alterna entre a forma inteira e a forma legível nos dois sentidos, com auto-detecção de segundos/ms e uma dica de tempo relativo.</p>

<h3>Quando usar</h3>
<ul>
  <li>Decodificar um campo <code>"timestamp": 1735689600</code> de uma entrada de log ou resposta de API.</li>
  <li>Verificar quando um JWT foi emitido ou quando expira (claims <code>iat</code> / <code>exp</code> são segundos-desde-epoch).</li>
  <li>Calcular um timestamp futuro para um header <code>retry-after</code>, job agendado ou TTL de cache.</li>
  <li>Verificação de sanidade se uma data armazenada num banco está em segundos, milissegundos ou microssegundos.</li>
  <li>Converter "agora" no formato que sua ferramenta do momento espera.</li>
</ul>

<h3>Segundos, milissegundos, microssegundos</h3>
<ul>
  <li><strong>Segundos</strong> — a convenção Unix original; ~10 dígitos hoje (ex.: <code>1735689600</code>). Usado em C, Linux, JWT, na maioria das APIs e na maioria das colunas <code>integer</code> de banco.</li>
  <li><strong>Milissegundos</strong> — <code>Date.now()</code> do JavaScript, <code>System.currentTimeMillis()</code> do Java, Kafka, muitas APIs JSON. ~13 dígitos.</li>
  <li><strong>Microssegundos (16 dígitos) / nanossegundos (19 dígitos)</strong> — <code>time.time_ns()</code> do Python, <code>time.Now().UnixNano()</code> do Go, alguns sistemas de métricas. Esta ferramenta não trata automaticamente — divida por 1.000 ou 1.000.000 antes.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>O problema do ano 2038.</strong> Timestamps signed de 32 bits estouram em <code>2147483647</code> = <strong>03:14:07 UTC, 19 de janeiro de 2038</strong>. Código C antigo, colunas <code>TIMESTAMP</code> do MySQL e sistemas embarcados podem dar wrap para 1901. Sistemas modernos usam 64 bits e estão tranquilos até ~ano 292.277.026.596.</li>
  <li><strong>Tempo Unix pula leap seconds.</strong> Um dia Unix tem exatamente 86.400 segundos, mesmo quando UTC tem 86.401. Isso é por design (mantém a aritmética simples), mas significa que você não pode usar timestamps Unix para astronomia ou GPS com precisão de sub-segundo.</li>
  <li><strong>Timestamps negativos</strong> são válidos e representam datas anteriores a 1970. Algumas bibliotecas rejeitam — teste antes de confiar.</li>
  <li><strong>A auto-detecção não é à prova de balas.</strong> Um valor de 10 dígitos <em>poderia</em> ser um timestamp em milissegundos de 1970 — extremamente improvável na prática, mas se você sabe a unidade, não dependa da heurística.</li>
  <li><strong>Sempre armazene em UTC.</strong> Timestamps são sem timezone; "hora local" é só para exibição. A linha "Local" na saída usa o fuso do seu navegador, mas o inteiro subjacente é sempre UTC.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Unix timestamp to jeden integer — liczba sekund (albo milisekund) od 1970-01-01 00:00:00 UTC. Są wszędzie: w plikach logów, w odpowiedziach API, w claimsach <code>iat</code>/<code>exp</code> JWT, w kolumnach <code>created_at</code> baz danych, w nagłówkach cache. Są jednoznaczne i wolne od strefy czasowej, ale nieczytelne dla człowieka — więc gdy coś się sypie o <code>1735689600</code>, musisz wiedzieć, czy to 14:00 czy 4:00 rano, dziś czy w zeszłym roku. To narzędzie przerzuca między formą integerową a formą czytelną w obie strony, z auto-detekcją sekund/ms i podpowiedzią czasu względnego.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Dekodowanie pola <code>"timestamp": 1735689600</code> z wpisu w logu albo odpowiedzi API.</li>
  <li>Sprawdzenie, kiedy JWT został wystawiony albo kiedy wygasa (claimsy <code>iat</code> / <code>exp</code> to sekundy od epoch).</li>
  <li>Wyliczenie przyszłego timestampu do nagłówka <code>retry-after</code>, zaplanowanego joba albo TTL cache.</li>
  <li>Sanity check, czy data zapisana w bazie jest w sekundach, milisekundach, czy mikrosekundach.</li>
  <li>Konwersja "now" na format, którego oczekuje twoje aktualne narzędzie.</li>
</ul>

<h3>Sekundy, milisekundy, mikrosekundy</h3>
<ul>
  <li><strong>Sekundy</strong> — pierwotna konwencja Unixa; ~10 cyfr dziś (np. <code>1735689600</code>). Używane w C, Linuksie, JWT, większości API, większości kolumn <code>integer</code> w bazie.</li>
  <li><strong>Milisekundy</strong> — JS-owy <code>Date.now()</code>, javowy <code>System.currentTimeMillis()</code>, Kafka, wiele JSON-owych API. ~13 cyfr.</li>
  <li><strong>Mikrosekundy (16 cyfr) / nanosekundy (19 cyfr)</strong> — pythonowy <code>time.time_ns()</code>, golangowy <code>time.Now().UnixNano()</code>, niektóre systemy metryk. To narzędzie ich nie obsługuje automatycznie — najpierw podziel przez 1000 albo 1 000 000.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Problem roku 2038.</strong> Signed 32-bitowe timestampy przepełniają się przy <code>2147483647</code> = <strong>03:14:07 UTC, 19 stycznia 2038</strong>. Stary kod C, kolumny <code>TIMESTAMP</code> w MySQL i systemy embedded mogą zawinąć się do 1901. Nowoczesne systemy używają 64 bitów i są OK do ~roku 292 277 026 596.</li>
  <li><strong>Czas Unix pomija sekundy przestępne.</strong> Doba uniksowa ma dokładnie 86 400 sekund, nawet gdy UTC ma 86 401. Tak jest z założenia (uproszcza arytmetykę), ale znaczy, że nie użyjesz Unix timestampów do astronomii ani GPS-a z dokładnością subsekundową.</li>
  <li><strong>Ujemne timestampy</strong> są poprawne i reprezentują daty sprzed 1970. Niektóre biblioteki je odrzucają — przetestuj zanim na tym polegniesz.</li>
  <li><strong>Auto-detekcja nie jest niezawodna.</strong> 10-cyfrowa wartość <em>mogłaby</em> być milisekundowym timestampem z 1970 — w praktyce nieprawdopodobnie, ale jeśli wiesz, którą jednostkę masz, nie polegaj na heurystyce.</li>
  <li><strong>Zawsze zapisuj UTC.</strong> Timestampy są wolne od strefy; "czas lokalny" jest tylko do wyświetlania. Linia "Local" na wyjściu używa strefy twojej przeglądarki, ale integer pod spodem to zawsze UTC.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>Unix タイムスタンプは 1 つの整数で、1970-01-01 00:00:00 UTC からの秒数（またはミリ秒数）を表します。ログ、API レスポンス、JWT の <code>iat</code>/<code>exp</code>、DB の <code>created_at</code>、キャッシュヘッダなど至る所で使われます。曖昧さがなくタイムゾーン非依存ですが、人には読めないため、何かが <code>1735689600</code> で壊れたとき、それが今日の 14 時か早朝 4 時か、今年か昨年かを知る必要があります。本ツールは整数表現と可読表現を双方向に変換し、秒／ミリ秒の自動判定と相対時間の表示も行います。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ログや API レスポンスの <code>"timestamp": 1735689600</code> をデコードしたいとき。</li>
  <li>JWT の発行日時や有効期限を確認したいとき（<code>iat</code> / <code>exp</code> はエポック秒）。</li>
  <li><code>retry-after</code> ヘッダ、スケジュールジョブ、キャッシュ TTL のために未来のタイムスタンプを計算したいとき。</li>
  <li>DB に保存された値が秒なのかミリ秒なのかマイクロ秒なのかをサニティチェックしたいとき。</li>
  <li>「今」を、いま使っているツールが要求する形式に変換したいとき。</li>
</ul>

<h3>秒・ミリ秒・マイクロ秒</h3>
<ul>
  <li><strong>秒</strong> — Unix の本来の慣例。現在およそ 10 桁（例：<code>1735689600</code>）。C、Linux、JWT、多くの API、整数カラムでよく使われます。</li>
  <li><strong>ミリ秒</strong> — JavaScript の <code>Date.now()</code>、Java の <code>System.currentTimeMillis()</code>、Kafka、多くの JSON API。約 13 桁。</li>
  <li><strong>マイクロ秒（16 桁）／ナノ秒（19 桁）</strong> — Python の <code>time.time_ns()</code>、Go の <code>time.Now().UnixNano()</code>、一部のメトリクス基盤。本ツールは自動処理しません。先に 1,000 や 1,000,000 で割ってから入力してください。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>2038 年問題。</strong> 32 ビット符号付きタイムスタンプは <code>2147483647</code> = <strong>2038 年 1 月 19 日 03:14:07 UTC</strong> でオーバーフローします。古い C コード、MySQL の <code>TIMESTAMP</code> 型、組み込み機器は 1901 年に巻き戻ることがあります。現代のシステムは 64 ビットなので、約西暦 292,277,026,596 年まで問題ありません。</li>
  <li><strong>Unix 時刻は閏秒を飛ばします。</strong> Unix の 1 日は常に 86,400 秒ですが、UTC は 86,401 秒の日が稀にあります。これは設計上の選択（演算が単純になる）ですが、サブ秒精度の天文計算や GPS には Unix 時刻は使えません。</li>
  <li><strong>負のタイムスタンプ</strong> は有効で、1970 年以前を表します。一部ライブラリは拒否するため、依存する前に検証してください。</li>
  <li><strong>自動判定は完全ではありません。</strong> 10 桁の値は理論上は 1970 年のミリ秒タイムスタンプであり得ます（実用上は皆無）。単位が分かっているなら自動判定に頼らず明示してください。</li>
  <li><strong>常に UTC で保存しましょう。</strong> タイムスタンプにタイムゾーンはありません。「ローカル時刻」は表示専用です。出力の "Local" 行はブラウザのタイムゾーンを使いますが、整数自体は常に UTC です。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een Unix-timestamp is één integer — het aantal seconden (of milliseconden) sinds 1970-01-01 00:00:00 UTC. Ze zijn overal: log-files, API-responses, JWT <code>iat</code>/<code>exp</code> claims, database <code>created_at</code>-kolommen, cache-headers. Ze zijn ondubbelzinnig en tijdzone-vrij, maar niet menselijk leesbaar, dus als iets breekt op <code>1735689600</code>, wil je weten of dat 14u of 4u is, vandaag of vorig jaar. Deze tool flipt tussen de integer-vorm en de leesbare vorm in beide richtingen, met seconds/ms auto-detectie en een relative-time hint.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een <code>"timestamp": 1735689600</code> veld uit een log-entry of API-response decoderen.</li>
  <li>Checken wanneer een JWT is uitgegeven of wanneer hij verloopt (<code>iat</code> / <code>exp</code> claims zijn seconds-since-epoch).</li>
  <li>Een toekomstige timestamp berekenen voor een <code>retry-after</code>-header, scheduled job of cache TTL.</li>
  <li>Sanity check op of een datum in een database in seconden, milliseconden of microseconden is opgeslagen.</li>
  <li>"Nu" converteren naar het formaat dat je tool van het moment wil.</li>
</ul>

<h3>Seconds, milliseconds, microseconds</h3>
<ul>
  <li><strong>Seconds</strong> — de oorspronkelijke Unix-conventie; ~10 cijfers vandaag (bijv. <code>1735689600</code>). Gebruikt in C, Linux, JWT, de meeste API's, de meeste database <code>integer</code>-kolommen.</li>
  <li><strong>Milliseconds</strong> — JavaScript's <code>Date.now()</code>, Java <code>System.currentTimeMillis()</code>, Kafka, veel JSON-API's. ~13 cijfers.</li>
  <li><strong>Microseconds (16 cijfers) / nanoseconds (19 cijfers)</strong> — Python <code>time.time_ns()</code>, Go <code>time.Now().UnixNano()</code>, sommige metrics-systemen. Deze tool handelt ze niet auto af — deel eerst door 1.000 of 1.000.000.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Het Year 2038-probleem.</strong> Signed 32-bit timestamps overflowen op <code>2147483647</code> = <strong>03:14:07 UTC, 19 januari 2038</strong>. Oude C-code, MySQL <code>TIMESTAMP</code>-kolommen en embedded systems kunnen wrappen naar 1901. Moderne systemen gebruiken 64-bit en zijn prima tot ~jaar 292.277.026.596.</li>
  <li><strong>Unix-tijd slaat leap seconds over.</strong> Een Unix-dag is precies 86.400 seconden, ook als UTC 86.401 heeft. Dit is by design (het houdt rekenen simpel) maar betekent dat je Unix-timestamps niet kunt gebruiken voor sub-seconde nauwkeurige astronomie of GPS.</li>
  <li><strong>Negatieve timestamps</strong> zijn geldig en representeren datums voor 1970. Sommige libraries wijzen ze af — test voor je erop vertrouwt.</li>
  <li><strong>Auto-detectie is niet vlekkeloos.</strong> Een 10-cijferige waarde <em>kan</em> een millisecond-timestamp uit 1970 zijn — verdwijnend onwaarschijnlijk in de praktijk, maar als je weet welke unit je hebt, vertrouw niet op de heuristiek.</li>
  <li><strong>Sla altijd UTC op.</strong> Timestamps zijn tijdzone-vrij; "lokale tijd" is alleen voor display. De "Local"-regel in de output gebruikt je browser-zone, maar de onderliggende integer is altijd UTC.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir Unix timestamp tek bir tamsayıdır — 1970-01-01 00:00:00 UTC'den bu yana saniye (veya milisaniye) sayısı. Her yerdeler: log dosyaları, API yanıtları, JWT <code>iat</code>/<code>exp</code> claim'leri, veritabanı <code>created_at</code> sütunları, cache header'ları. Belirsiz ve saat dilimsizdirler, ama insan tarafından okunamaz, bu yüzden <code>1735689600</code>'da bir şey bozulduğunda, bunun 14:00 mı yoksa 04:00 mı, bugün mü yoksa geçen yıl mı olduğunu bilmen gerekir. Bu araç tamsayı formu ile okunabilir formu her iki yönde çevirir, saniye/ms otomatik tespiti ve göreceli zaman ipucuyla.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir log girdisinden veya API yanıtından <code>"timestamp": 1735689600</code> alanını çözme.</li>
  <li>Bir JWT'nin ne zaman verildiğini veya ne zaman süresinin dolduğunu kontrol etme (<code>iat</code> / <code>exp</code> claim'leri saniye-since-epoch'tur).</li>
  <li><code>retry-after</code> header, zamanlanmış iş veya cache TTL için gelecekteki bir timestamp hesaplama.</li>
  <li>Veritabanında saklanan bir tarihin saniye, milisaniye veya mikrosaniye cinsinden olup olmadığının sanity check'i.</li>
  <li>"Şimdi"yi anlık aracın istediği biçime dönüştürme.</li>
</ul>

<h3>Saniye, milisaniye, mikrosaniye</h3>
<ul>
  <li><strong>Saniye</strong> — orijinal Unix konvansiyonu; bugün ~10 basamak (örn. <code>1735689600</code>). C, Linux, JWT, çoğu API, çoğu veritabanı <code>integer</code> sütununda kullanılır.</li>
  <li><strong>Milisaniye</strong> — JavaScript'in <code>Date.now()</code>, Java <code>System.currentTimeMillis()</code>, Kafka, birçok JSON API. ~13 basamak.</li>
  <li><strong>Mikrosaniye (16 basamak) / nanosaniye (19 basamak)</strong> — Python <code>time.time_ns()</code>, Go <code>time.Now().UnixNano()</code>, bazı metrik sistemleri. Bu araç bunları otomatik işlemez — önce 1.000 veya 1.000.000'a böl.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Yıl 2038 problemi.</strong> İşaretli 32-bit timestamp'lar <code>2147483647</code> = <strong>03:14:07 UTC, 19 Ocak 2038</strong>'de taşar. Eski C kodu, MySQL <code>TIMESTAMP</code> sütunları ve gömülü sistemler 1901'e dönebilir. Modern sistemler 64-bit kullanır ve ~292,277,026,596 yılına kadar iyidir.</li>
  <li><strong>Unix zamanı leap saniyeleri atlar.</strong> Bir Unix günü tam olarak 86.400 saniyedir, UTC 86.401 olduğunda bile. Bu tasarım gereğidir (aritmetiği basit tutar) ama Unix timestamp'larını sub-saniye doğruluklu astronomi veya GPS için kullanamayacağın anlamına gelir.</li>
  <li><strong>Negatif timestamp'lar</strong> geçerlidir ve 1970'ten önceki tarihleri temsil eder. Bazı kütüphaneler bunları reddeder — güvenmeden önce test et.</li>
  <li><strong>Otomatik tespit kusursuz değildir.</strong> 10 basamaklı bir değer 1970'ten bir milisaniye timestamp'i <em>olabilir</em> — pratikte yok denecek kadar olası değildir, ama hangi birimin olduğunu biliyorsan, sezgisele güvenme.</li>
  <li><strong>Her zaman UTC sakla.</strong> Timestamp'lar saat dilimsizdir; "yerel saat" sadece gösterim içindir. Çıktıdaki "Yerel" satırı tarayıcının dilimini kullanır, ama temel tamsayı her zaman UTC'dir.</li>
</ul>
""",
    },
    "related": ["timezone-converter", "cron-parser", "date-calculator"],
    "howto": {"flow": "transform", "action": "convert", "noun": "timestamp"},
}
