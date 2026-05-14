TOOL = {
    "slug": "json-formatter",
    "category": "developer",
    "icon": "{ }",
    "tags": ["json", "format", "beautify", "validate", "minify"],
    "i18n": {
        "en": {
            "name": "JSON Formatter",
            "tagline": "Format, validate, and minify JSON instantly. Errors highlighted with line and column.",
            "description": "Free online JSON formatter and validator. Pretty-print, minify, and check JSON syntax with precise error messages.",
        },
        "de": {
            "name": "JSON-Formatter",
            "tagline": "JSON sofort formatieren, validieren und minimieren. Fehler werden mit Zeile und Spalte hervorgehoben.",
            "description": "Kostenloser Online-JSON-Formatter und Validator. JSON formatieren, minimieren und auf Syntax prüfen.",
        },
        "es": {
            "name": "Formateador JSON",
            "tagline": "Formatea, valida y minifica JSON al instante. Los errores se resaltan con línea y columna.",
            "description": "Formateador y validador JSON gratuito en línea. Formatea, minifica y verifica la sintaxis JSON.",
        },
        "fr": {
            "name": "Formateur JSON",
            "tagline": "Formatez, validez et minifiez du JSON instantanément. Les erreurs sont signalées avec ligne et colonne.",
            "description": "Formateur et validateur JSON gratuit en ligne. Embellissez, minifiez et vérifiez la syntaxe JSON.",
        },
        "it": {
            "name": "Formattatore JSON",
            "tagline": "Formatta, valida e minifica JSON all'istante. Gli errori sono evidenziati con riga e colonna.",
            "description": "Formattatore e validatore JSON gratuito online. Abbellisci, minifica e controlla la sintassi JSON.",
        },
        "pt": {
            "name": "Formatador JSON",
            "tagline": "Formata, valida e minifica JSON na hora. Erros destacados com linha e coluna.",
            "description": "Formatador e validador JSON grátis online. Pretty-print, minify e checagem da sintaxe JSON com mensagens de erro precisas.",
        },
        "pl": {
            "name": "Formatter JSON",
            "tagline": "Formatuj, waliduj i minifikuj JSON od ręki. Błędy podświetlone z numerem linii i kolumny.",
            "description": "Darmowy online formatter i walidator JSON. Pretty-print, minify i sprawdzanie składni JSON z precyzyjnymi komunikatami błędów.",
        },
        "ja": {
            "name": "JSON フォーマッター",
            "tagline": "JSON を即座に整形・検証・圧縮。エラー位置を行と列でハイライト。",
            "description": "オンライン無料の JSON フォーマッター・バリデーター。整形（pretty-print）、ミニファイ、構文検証を行い、正確なエラー位置を表示します。",
        },
        "nl": {"name": "JSON Formatter", "tagline": "Formatteer, valideer en minify JSON direct. Errors gehighlight met regel en kolom.", "description": "Gratis online JSON-formatter en -validator. Pretty-print, minify en check JSON-syntax met precieze foutmeldingen."},
        "tr": {"name": "JSON Formatter", "tagline": "JSON'u anında biçimlendir, doğrula ve küçült. Hatalar satır ve sütunla vurgulanır.", "description": "Ücretsiz online JSON formatter ve doğrulayıcı. JSON sözdizimini güzel yazdır, küçült ve hassas hata mesajlarıyla denetle."},
        "id": {"name": "JSON Formatter", "tagline": "Format, validasi, dan minify JSON secara instan. Error disorot dengan baris dan kolom.", "description": "JSON formatter dan validator online gratis. Beautify JSON berantakan dengan indentasi, atau minify-nya untuk transport. Error sintaks disorot dengan nomor baris dan kolom. Berjalan di browser-mu."},
        "vi": {"name": "JSON Formatter", "tagline": "Format, xác thực và minify JSON tức thì. Lỗi được làm nổi bật với dòng và cột.", "description": "JSON formatter và validator miễn phí trực tuyến. Làm đẹp JSON lộn xộn với indent, hoặc minify để truyền tải. Lỗi cú pháp được làm nổi bật với số dòng và cột. Chạy trong trình duyệt của bạn."},
        "hi": {"name": "JSON Formatter", "tagline": "JSON को तुरंत फ़ॉर्मैट करें, जांचें, और minify करें। Errors को line और column के साथ highlight किया जाता है।", "description": "मुफ़्त ऑनलाइन JSON formatter और validator. JSON syntax को pretty-print, minify, और सटीक error messages के साथ जांचें।"},
        "sk": {"name": 'JSON formátovač', "tagline": 'Naformátuj, over a minifikuj JSON okamžite. Chyby zvýraznené s riadkom a stĺpcom.', "description": 'Bezplatný online JSON formátovač a validátor. Naformátuje, validuje a minifikuje JSON okamžite. Chyby ukazuje s riadkom a stĺpcom. Beží v prehliadači.'},
        "cs": {"name": 'JSON formátovač', "tagline": 'Naformátuj, ověř a zminifikuj JSON okamžitě. Chyby zvýrazněné s řádkem a sloupcem.', "description": 'Zdarma online JSON formátovač a validátor. Naformátuje, validuje a minifikuje JSON okamžitě. Chyby ukazuje s řádkem a sloupcem. Běží v prohlížeči.'},
    },
    "body": """
<div class="tool-card">
  <label for="json-input">{LBL_INPUT}</label>
  <textarea id="json-input" placeholder='{{"hello": "world", "n": 42}}' spellcheck="false"></textarea>
  <div class="button-row">
    <button onclick="jfFormat(2)">{LBL_FORMAT}</button>
    <button class="secondary" onclick="jfFormat(4)">{LBL_FORMAT} (4)</button>
    <button class="secondary" onclick="jfMinify()">{LBL_MINIFY}</button>
    <button class="secondary" onclick="jfValidate()">{LBL_VALIDATE}</button>
    <button class="secondary" onclick="document.getElementById('json-input').value=''">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="json-output">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('json-output', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="json-meta"></div>
</div>
""",
    "script": """
<script>
function jfShowError(e, raw){
  const out = document.getElementById('json-output');
  out.classList.add('error');
  out.classList.remove('success');
  let msg = e.message || String(e);
  // Try to extract position
  const m = msg.match(/position (\\d+)/i);
  if (m){
    const pos = parseInt(m[1], 10);
    const before = raw.slice(0, pos);
    const line = (before.match(/\\n/g) || []).length + 1;
    const col = pos - (before.lastIndexOf('\\n') + 1) + 1;
    msg = msg.replace(/position \\d+/i, 'line ' + line + ', col ' + col);
  }
  out.textContent = '✗ ' + msg;
  document.getElementById('json-meta').textContent = '';
}
function jfShowOk(text, label){
  const out = document.getElementById('json-output');
  out.classList.remove('error');
  out.classList.add('success');
  out.textContent = text;
  document.getElementById('json-meta').textContent = label || '';
}
function jfFormat(indent){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj, null, indent);
    jfShowOk(out, out.length + ' chars · ' + (out.match(/\\n/g)||[]).length + ' lines');
  } catch(e){ jfShowError(e, raw); }
}
function jfMinify(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj);
    jfShowOk(out, out.length + ' chars (minified)');
  } catch(e){ jfShowError(e, raw); }
}
function jfValidate(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const t = Array.isArray(obj) ? 'array' : typeof obj;
    const sz = JSON.stringify(obj).length;
    jfShowOk('✓ Valid JSON', 'top-level: ' + t + ' · ' + sz + ' chars minified');
  } catch(e){ jfShowError(e, raw); }
}
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('json-input');
  if (!input) return;
  input.value = e.detail.data;
  jfFormat(2);
});
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>JSON travels minified — every byte counts when an API response is being shipped. But minified JSON is unreadable. This tool round-trips through the browser's native <code>JSON.parse</code> / <code>JSON.stringify</code> to produce indented, copy-able output, validate the structure, or strip whitespace back out. Nothing is uploaded; everything happens in the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Pasting a minified API response and getting back something a human can scan.</li>
  <li>Catching syntax errors — trailing commas, unquoted keys, smart quotes — with the exact line/column the parser tripped on.</li>
  <li>Stripping whitespace before pasting JSON into a context where size matters (URL params, env vars, config files).</li>
  <li>Confirming your hand-written JSON is valid before piping it into another tool.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>JSON ≠ JavaScript object literal.</strong> Keys must be in double quotes. Single quotes, unquoted keys, and trailing commas all fail. If you've got JS object literals, run them through a converter first.</li>
  <li><strong>Smart quotes from copy-paste.</strong> Word processors and chat apps love to "helpfully" replace <code>"</code> with <code>"</code> / <code>"</code>. Those aren't valid JSON delimiters.</li>
  <li><strong>JSON has no comments.</strong> If your "JSON" has <code>//</code> or <code>/* */</code>, it's actually JSONC (used by VS Code config) — strip those before parsing.</li>
  <li><strong>Numbers larger than 2⁵³.</strong> JavaScript can't represent integers above <code>9007199254740992</code> exactly. Twitter snowflake IDs and similar should be quoted as strings.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>O JSON viaja minificado — cada byte conta quando uma resposta de API está sendo enviada. Mas JSON minificado é ilegível. Esta ferramenta faz round-trip pelo <code>JSON.parse</code> / <code>JSON.stringify</code> nativo do browser pra produzir output indentado e copiável, validar a estrutura ou tirar o whitespace de novo. Nada é enviado; tudo acontece na página.</p>

<h3>Quando usar</h3>
<ul>
  <li>Colar uma resposta de API minificada e receber algo que um humano consegue ler.</li>
  <li>Pegar erros de sintaxe — vírgulas no final, chaves sem aspas, smart quotes — com linha/coluna exata onde o parser tropeçou.</li>
  <li>Tirar whitespace antes de colar JSON num contexto onde tamanho importa (params de URL, env vars, arquivos de config).</li>
  <li>Confirmar que seu JSON feito à mão é válido antes de mandar pra outra ferramenta.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>JSON ≠ object literal de JavaScript.</strong> Chaves precisam estar entre aspas duplas. Aspas simples, chaves sem aspas e vírgulas no final, tudo falha. Se você tem object literals de JS, passe por um conversor antes.</li>
  <li><strong>Smart quotes vindas de copy-paste.</strong> Editores de texto e apps de chat adoram "ajudar" trocando <code>"</code> por <code>"</code> / <code>"</code>. Esses não são delimitadores JSON válidos.</li>
  <li><strong>JSON não tem comentários.</strong> Se seu "JSON" tem <code>//</code> ou <code>/* */</code>, na verdade é JSONC (usado em config do VS Code) — remova antes de fazer parse.</li>
  <li><strong>Números maiores que 2⁵³.</strong> O JavaScript não consegue representar inteiros acima de <code>9007199254740992</code> com exatidão. IDs snowflake do Twitter e similares devem vir entre aspas como strings.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>JSON podróżuje zminifikowany — każdy bajt się liczy, gdy odpowiedź API leci po sieci. Ale zminifikowany JSON jest nieczytelny. To narzędzie robi round-trip przez natywny <code>JSON.parse</code> / <code>JSON.stringify</code> przeglądarki, żeby wyprodukować wcięte, kopiowalne wyjście, zwalidować strukturę albo wyciąć białe znaki z powrotem. Nic nie jest wysyłane; wszystko dzieje się na stronie.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wklejenie zminifikowanej odpowiedzi API i dostanie czegoś, co da się przeczytać po ludzku.</li>
  <li>Łapanie błędów składniowych — końcowych przecinków, kluczy bez cudzysłowu, smart quotes — z dokładnym numerem linii/kolumny, gdzie parser się wywalił.</li>
  <li>Wycinanie białych znaków przed wklejeniem JSON-a w kontekst, gdzie rozmiar ma znaczenie (parametry URL, zmienne środowiskowe, pliki configa).</li>
  <li>Potwierdzenie, że ręcznie pisany JSON jest poprawny, zanim wpuścisz go w inne narzędzie.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>JSON ≠ object literal w JavaScripcie.</strong> Klucze muszą być w podwójnych cudzysłowach. Pojedyncze cudzysłowy, klucze bez cudzysłowu i końcowe przecinki — wszystko padnie. Jeśli masz JS-owe object literale, najpierw przepuść je przez konwerter.</li>
  <li><strong>Smart quotes z copy-paste.</strong> Edytory tekstu i czaty uwielbiają "pomocnie" zamieniać <code>"</code> na <code>"</code> / <code>"</code>. To nie są poprawne delimitery JSON.</li>
  <li><strong>JSON nie ma komentarzy.</strong> Jeśli twój "JSON" ma <code>//</code> albo <code>/* */</code>, to faktycznie JSONC (używany w configu VS Code) — wytnij je przed parsem.</li>
  <li><strong>Liczby większe niż 2⁵³.</strong> JavaScript nie potrafi dokładnie reprezentować integerów powyżej <code>9007199254740992</code>. Snowflake'i z Twittera i podobne powinny być cytowane jako stringi.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>JSON は配信時にミニファイされて流れます。API レスポンスではバイトが命だからです。しかしミニファイされた JSON は人には読みづらいものです。本ツールはブラウザネイティブの <code>JSON.parse</code> / <code>JSON.stringify</code> を経由してラウンドトリップし、インデント付きでコピーしやすい出力を生成、構造を検証、または空白を再度除去できます。アップロードはなく、すべてページ内で完結します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ミニファイされた API レスポンスを貼り付けて、人が読める形に整形したいとき。</li>
  <li>末尾カンマ、引用符なしキー、スマートクォートといった構文エラーを、パーサが落ちた行・列付きで把握したいとき。</li>
  <li>サイズが重要な場面（URL パラメータ、環境変数、設定ファイル）に貼り付ける前に空白を取り除きたいとき。</li>
  <li>手書きの JSON を別ツールに渡す前に有効性を確認したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>JSON は JavaScript のオブジェクトリテラルとは別物です。</strong> キーは必ず二重引用符。シングルクォート、引用符なしのキー、末尾カンマはすべてエラーです。JS のオブジェクトリテラルがあるなら、まず JSON にコンバートしてください。</li>
  <li><strong>コピペで入るスマートクォート。</strong> ワープロやチャットアプリは「親切に」<code>"</code> を <code>“</code>／<code>”</code> に置き換えます。これらは JSON では有効な区切り文字ではありません。</li>
  <li><strong>JSON にコメントはありません。</strong> 「JSON」に <code>//</code> や <code>/* */</code> が含まれているなら、それは実は JSONC（VS Code 設定で使われる）です。パース前に取り除いてください。</li>
  <li><strong>2⁵³ を超える数値。</strong> JavaScript は <code>9007199254740992</code> を超える整数を厳密に表現できません。Twitter のスノーフレーク ID などは文字列で扱ってください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>JSON reist geminifieerd — elke byte telt als een API-response over de lijn gaat. Maar geminifieerd JSON is onleesbaar. Deze tool round-trip't door de native <code>JSON.parse</code> / <code>JSON.stringify</code> van de browser om geïndenteerde, kopieerbare output te produceren, de structuur te valideren of whitespace eruit te strippen. Niets wordt geüpload; alles gebeurt op de pagina.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een geminifieerde API-response plakken en iets terugkrijgen dat een mens kan scannen.</li>
  <li>Syntax-fouten vangen — trailing comma's, unquoted keys, smart quotes — met de exacte regel/kolom waar de parser struikelde.</li>
  <li>Whitespace strippen voor je JSON in een context plakt waar size telt (URL params, env vars, config files).</li>
  <li>Bevestigen dat je met-de-hand-geschreven JSON geldig is voor je het naar een andere tool stuurt.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>JSON ≠ JavaScript object literal.</strong> Keys moeten in dubbele aanhalingstekens. Single quotes, unquoted keys en trailing comma's falen allemaal. Als je JS object literals hebt, draai ze eerst door een converter.</li>
  <li><strong>Smart quotes uit copy-paste.</strong> Word processors en chat-apps vervangen <code>"</code> graag "behulpzaam" door <code>"</code> / <code>"</code>. Die zijn geen geldige JSON-delimiters.</li>
  <li><strong>JSON heeft geen comments.</strong> Als jouw "JSON" <code>//</code> of <code>/* */</code> heeft, is het eigenlijk JSONC (gebruikt in VS Code config) — strip die voor parsen.</li>
  <li><strong>Getallen groter dan 2⁵³.</strong> JavaScript kan integers boven <code>9007199254740992</code> niet exact representeren. Twitter snowflake-IDs en vergelijkbaar moeten als strings ge-quote'd worden.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>JSON minified seyahat eder — bir API yanıtı gönderilirken her byte sayılır. Ama minified JSON okunmaz. Bu araç tarayıcının yerel <code>JSON.parse</code> / <code>JSON.stringify</code> üzerinden round-trip yaparak indent edilmiş, kopyalanabilir çıktı üretir, yapıyı doğrular veya boşluğu geri temizler. Hiçbir şey upload edilmez; her şey sayfada olur.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Minified bir API yanıtı yapıştırma ve bir insanın tarayabileceği bir şey geri alma.</li>
  <li>Parser'ın tökezlediği tam satır/sütun ile sözdizimi hatalarını yakalama — sondaki virgüller, tırnaksız anahtarlar, smart quote'lar.</li>
  <li>Boyutun önemli olduğu bir bağlama (URL parametreleri, ortam değişkenleri, config dosyaları) JSON yapıştırmadan önce boşluğu temizleme.</li>
  <li>El yazımı JSON'unun başka bir araca pipe etmeden önce geçerli olduğunu doğrulama.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>JSON ≠ JavaScript nesne literal'i.</strong> Anahtarlar çift tırnak içinde olmalıdır. Tek tırnak, tırnaksız anahtarlar ve sondaki virgüller hepsi başarısız olur. JS nesne literal'ların varsa, önce bir dönüştürücüden geçir.</li>
  <li><strong>Kopyala-yapıştırdan smart quote'lar.</strong> Word ve sohbet uygulamaları <code>"</code>'yi <code>"</code> / <code>"</code> ile "yardımcı" şekilde değiştirmeyi sever. Bunlar geçerli JSON sınırlayıcılar değildir.</li>
  <li><strong>JSON'da yorum yoktur.</strong> "JSON"un <code>//</code> veya <code>/* */</code> içeriyorsa, aslında JSONC'tir (VS Code config tarafından kullanılır) — parse etmeden önce bunları temizle.</li>
  <li><strong>2⁵³'ten büyük sayılar.</strong> JavaScript <code>9007199254740992</code> üzerindeki tamsayıları tam olarak temsil edemez. Twitter snowflake ID'leri ve benzerleri string olarak tırnaklanmalıdır.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>JSON dikirim dalam bentuk minified — setiap byte penting saat response API melayang di kabel. Tapi JSON minified susah dibaca. Tool ini melakukan round-trip lewat <code>JSON.parse</code> / <code>JSON.stringify</code> bawaan browser untuk menghasilkan output yang ter-indent dan bisa di-copy, memvalidasi struktur, atau menghapus whitespace lagi. Tidak ada yang di-upload; semuanya terjadi di halaman.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mem-paste response API yang minified dan mendapatkan sesuatu yang bisa di-scan manusia.</li>
  <li>Menangkap syntax error — trailing comma, key tanpa quote, smart quote — dengan line/column persis tempat parser tersandung.</li>
  <li>Menghapus whitespace sebelum mem-paste JSON ke konteks yang sensitif ukuran (URL param, environment variable, file config).</li>
  <li>Memastikan JSON hand-written valid sebelum kamu menyalurkannya ke tool lain.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>JSON ≠ object literal JavaScript.</strong> Key harus pakai double quote. Single quote, key tanpa quote, dan trailing comma semua akan gagal. Kalau kamu punya object literal JS, lewatkan dulu ke converter.</li>
  <li><strong>Smart quote dari copy-paste.</strong> Word processor dan aplikasi chat suka "membantu" mengganti <code>"</code> jadi <code>"</code> / <code>"</code>. Itu bukan delimiter JSON yang valid.</li>
  <li><strong>JSON tidak punya comment.</strong> Kalau "JSON"-mu mengandung <code>//</code> atau <code>/* */</code>, sebenarnya itu JSONC (dipakai di config VS Code) — hapus dulu sebelum parse.</li>
  <li><strong>Angka di atas 2⁵³.</strong> JavaScript tidak bisa merepresentasikan integer di atas <code>9007199254740992</code> dengan tepat. ID snowflake Twitter dan semacamnya harus di-quote sebagai string.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>JSON được gửi dưới dạng minified — mỗi byte quan trọng khi response API bay qua dây. Nhưng JSON minified khó đọc. Tool này round-trip qua <code>JSON.parse</code> / <code>JSON.stringify</code> tích hợp của trình duyệt để xuất ra output được indent dễ copy, validate cấu trúc, hoặc bỏ whitespace lại. Không có gì được upload; mọi thứ xảy ra trên trang.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Paste một response API minified và lấy thứ gì đó có thể scan bằng con người.</li>
  <li>Bắt lỗi cú pháp — trailing comma, key không có quote, smart quote — với line/column chính xác nơi parser vấp.</li>
  <li>Strip whitespace trước khi paste JSON vào context nhạy cảm về kích thước (URL param, environment variable, file config).</li>
  <li>Đảm bảo JSON hand-written hợp lệ trước khi feed nó vào tool khác.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>JSON ≠ object literal JavaScript.</strong> Key phải có double quote. Single quote, key không có quote và trailing comma đều sẽ fail. Nếu bạn có JS object literal, chạy nó qua converter trước.</li>
  <li><strong>Smart quote từ copy-paste.</strong> Word processor và app chat thích "giúp" thay <code>"</code> bằng <code>"</code> / <code>"</code>. Đó không phải là delimiter JSON hợp lệ.</li>
  <li><strong>JSON không có comment.</strong> Nếu "JSON" của bạn chứa <code>//</code> hoặc <code>/* */</code>, đó thực sự là JSONC (dùng trong config VS Code) — strip chúng trước khi parse.</li>
  <li><strong>Số trên 2⁵³.</strong> JavaScript không thể biểu diễn integer trên <code>9007199254740992</code> chính xác. ID snowflake Twitter và tương tự phải được quote như string.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>JSON minified रूप में travel करता है — जब API response wire पर भेजा जा रहा हो तो हर byte मायने रखता है। लेकिन minified JSON पढ़ने योग्य नहीं होता। यह टूल browser के native <code>JSON.parse</code> / <code>JSON.stringify</code> के माध्यम से round-trip करता है ताकि indented, copy-योग्य output बनाया जा सके, संरचना को जांचा जा सके, या whitespace वापस हटाया जा सके। कुछ भी upload नहीं होता; सब कुछ page पर होता है।</p>

<h3>कब इस्तेमाल करें</h3>
<ul>
  <li>Minified API response को paste करना और कुछ ऐसा वापस पाना जिसे एक इंसान scan कर सके।</li>
  <li>Syntax errors पकड़ना — trailing commas, unquoted keys, smart quotes — सटीक line/column के साथ जहाँ parser फिसला।</li>
  <li>JSON को ऐसे context में paste करने से पहले whitespace हटाना जहाँ size मायने रखता है (URL params, env vars, config files)।</li>
  <li>दूसरे टूल में pipe करने से पहले यह पुष्टि करना कि आपका hand-written JSON valid है।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>JSON ≠ JavaScript object literal।</strong> Keys double quotes में होनी चाहिए। Single quotes, unquoted keys, और trailing commas सभी fail होते हैं। यदि आपके पास JS object literals हैं, तो पहले उन्हें एक converter से चलाएं।</li>
  <li><strong>Copy-paste से smart quotes।</strong> Word processors और chat apps "मदद" के नाम पर <code>"</code> को <code>"</code> / <code>"</code> से बदलना पसंद करते हैं। वे वैध JSON delimiters नहीं हैं।</li>
  <li><strong>JSON में comments नहीं होते।</strong> यदि आपके "JSON" में <code>//</code> या <code>/* */</code> है, तो वह वास्तव में JSONC है (VS Code config में उपयोग होता है) — parse करने से पहले उन्हें हटाएं।</li>
  <li><strong>2⁵³ से बड़ी संख्याएं।</strong> JavaScript <code>9007199254740992</code> से ऊपर के integers को सटीक रूप से represent नहीं कर सकता। Twitter snowflake IDs और इसी तरह की संख्याओं को strings के रूप में quote किया जाना चाहिए।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>JSON formátovač naformátuje JSON s konzistentným indentom (alebo ho minifikuje na jeden riadok), zároveň validuje syntax. Pri chybe ti ukáže presný riadok a stĺpec, aby si nehľadal čiarku navyše hodinu.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>API odpoveď, ktorú dostaneš ako jeden dlhý riadok, premeniť na čitateľnú.</li>
  <li>Validácia, či JSON, ktorý práve píšeš, parse-uje.</li>
  <li>Minify pred poslaním cez network (alebo do localStorage).</li>
  <li>Príprava pretty-printed JSON-u do dokumentácie.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Trailing comma.</strong> JSON nepovoľuje čiarku za posledným prvkom (na rozdiel od JS objektov).</li>
  <li><strong>Komentáre.</strong> Štandardný JSON ich nemá. Použij JSON5 alebo JSONC, ak ich nutne potrebuješ.</li>
  <li><strong>Single quotes.</strong> JSON keys aj string values musia byť v double quotes.</li>
  <li><strong>NaN / Infinity / undefined.</strong> Nie sú validné JSON — JS to dovoľuje, ale JSON.parse zlyhá.</li>
  <li><strong>Veľké čísla.</strong> JSON nedefinuje presnosť — 64-bit JS čísla strácajú presnosť cez 2^53.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>JSON formátovač naformátuje JSON s konzistentním indentem (nebo ho zminifikuje na jeden řádek), zároveň validuje syntaxi. Při chybě ti ukáže přesný řádek a sloupec, abys nehledal čárku navíc hodinu.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>API odpověď, kterou dostaneš jako jeden dlouhý řádek, proměnit na čitelnou.</li>
  <li>Validace, jestli JSON, který právě píšeš, parsuje.</li>
  <li>Minify před posláním přes network (nebo do localStorage).</li>
  <li>Příprava pretty-printed JSONu do dokumentace.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Trailing comma.</strong> JSON nepovoluje čárku za posledním prvkem (na rozdíl od JS objektů).</li>
  <li><strong>Komentáře.</strong> Standardní JSON je nemá. Použij JSON5 nebo JSONC, pokud je nutně potřebuješ.</li>
  <li><strong>Single quotes.</strong> JSON keys i string values musí být v double quotes.</li>
  <li><strong>NaN / Infinity / undefined.</strong> Nejsou validní JSON — JS to dovoluje, ale JSON.parse selže.</li>
  <li><strong>Velká čísla.</strong> JSON nedefinuje přesnost — 64-bit JS čísla ztrácí přesnost přes 2^53.</li>
</ul>
""",
    },
    "related": ["regex-tester", "yaml-json", "json-diff"],
    "howto": {"flow": "transform", "action": "format", "noun": "JSON"},
}
