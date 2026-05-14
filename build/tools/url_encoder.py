TOOL = {
    "slug": "url-encoder",
    "category": "encoding",
    "icon": "🔗",
    "tags": ["url", "encode", "decode", "percent", "querystring"],
    "i18n": {
        "en": {
            "name": "URL Encoder / Decoder",
            "tagline": "Percent-encode strings for URLs or decode percent-encoded ones back to plain text.",
            "description": "Free online URL encoder and decoder. Encodes special characters as percent-escapes for URLs, query strings, and form data. Component-safe.",
        },
        "de": {"name": "URL Encoder / Decoder", "tagline": "Strings für URLs prozent-codieren oder zurück in Klartext decodieren.", "description": "Kostenloser URL Encoder und Decoder. Sonderzeichen für URLs, Query-Strings und Formulardaten escapen."},
        "es": {"name": "Codificador / Decodificador URL", "tagline": "Codifica cadenas para URLs (porcentaje) o decodifica de vuelta a texto plano.", "description": "Codificador y decodificador URL gratuito. Escapa caracteres especiales para URLs, query strings y datos de formulario."},
        "fr": {"name": "Encodeur / Décodeur URL", "tagline": "Encodez en pourcentage pour URLs ou décodez vers texte brut.", "description": "Encodeur et décodeur URL gratuit. Échappe les caractères spéciaux pour URLs, query strings et formulaires."},
        "it": {"name": "Encoder / Decoder URL", "tagline": "Codifica stringhe per URL (percent-encoding) o decodifica in testo semplice.", "description": "Encoder e decoder URL gratuito. Escape di caratteri speciali per URL, query string e dati form."},
        "pt": {"name": "Encoder / Decoder de URL", "tagline": "Faça percent-encoding de strings para URLs ou decodifique de volta para texto puro.", "description": "Encoder e decoder de URL online gratuito. Codifica caracteres especiais como percent-escapes para URLs, query strings e dados de formulário. Component-safe."},
        "pl": {"name": "Encoder / Decoder URL", "tagline": "Percent-encoduj stringi pod URL-e albo dekoduj zakodowane procentowo z powrotem na zwykły tekst.", "description": "Darmowy online encoder i decoder URL. Koduje znaki specjalne jako percent-escape pod URL-e, query stringi i form data. Component-safe."},
        "ja": {"name": "URL エンコーダー / デコーダー", "tagline": "URL 用に文字列を percent-encode、または percent-encoded をテキストにデコード。", "description": "オンライン無料の URL エンコーダー／デコーダー。URL、クエリ文字列、フォームデータ用に特殊文字を percent-escape にエンコードします。コンポーネントセーフ。"},
        "nl": {"name": "URL Encoder / Decoder", "tagline": "Percent-encode strings voor URLs of decodeer percent-encoded strings terug naar plain text.", "description": "Gratis online URL encoder en decoder. Encodet speciale tekens als percent-escapes voor URLs, query strings en form data. Component-safe."},
        "tr": {"name": "URL Encoder / Decoder", "tagline": "String'leri URL'ler için percent-encode et veya percent-encoded string'leri düz metne çöz.", "description": "Ücretsiz online URL encoder ve decoder. URL'ler, query string'ler ve form verisi için özel karakterleri percent-escape olarak kodlar. Component-safe."},
        "id": {"name": "URL Encoder / Decoder", "tagline": "Percent-encode string untuk URL atau decode string percent-encoded kembali ke teks biasa.", "description": "URL encoder dan decoder gratis. Percent-encode string apa pun untuk penggunaan aman di URL (path, query string, fragment) atau decode string percent-encoded kembali ke karakter aslinya. UTF-8 aman."},
        "vi": {"name": "URL Encoder / Decoder", "tagline": "Percent-encode chuỗi cho URL hoặc decode chuỗi percent-encoded trở lại văn bản thường.", "description": "URL encoder và decoder miễn phí trực tuyến. Percent-encode chuỗi để dùng an toàn trong query string và path, hoặc decode chuỗi percent-encoded trở lại văn bản thường. UTF-8 an toàn."},
        "hi": {"name": "URL Encoder / Decoder", "tagline": "URL के लिए strings को percent-encode करें या percent-encoded strings को वापस सादे टेक्स्ट में decode करें।", "description": "मुफ़्त ऑनलाइन URL encoder और decoder। URLs, query strings और form data के लिए विशेष अक्षरों को percent-escape के रूप में encode करें। Component-safe।"},
        "sk": {"name": 'URL Encoder / Decoder', "tagline": 'Percent-encode reťazce pre URL alebo dekóduj percent-encoded späť na obyčajný text.', "description": 'Bezplatný online URL encoder / decoder. Percent-encode reťazce na bezpečné použitie v URL alebo dekóduj percent-encoded reťazce späť na obyčajný text. UTF-8 safe.'},
        "cs": {"name": 'URL Encoder / Decoder', "tagline": 'Percent-encode řetězce pro URL nebo dekóduj percent-encoded zpět na obyčejný text.', "description": 'Zdarma online URL encoder / decoder. Percent-encode řetězce pro bezpečné použití v URL nebo dekóduj percent-encoded řetězce zpět na obyčejný text. UTF-8 safe.'},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="url-mode" onchange="urlRun()">
        <option value="enc">{LBL_ENCODE}</option>
        <option value="dec">{LBL_DECODE}</option>
      </select>
    </div>
    <div>
      <label>Scope</label>
      <select id="url-scope" onchange="urlRun()">
        <option value="component">Component (encodes /, ?, #, &amp;)</option>
        <option value="uri">Full URI (preserves /, ?, #, &amp;)</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="url-in" oninput="urlRun()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="url-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('url-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function urlRun(){
  const mode = document.getElementById('url-mode').value;
  const scope = document.getElementById('url-scope').value;
  const raw = document.getElementById('url-in').value;
  const out = document.getElementById('url-out');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    let res;
    if (mode === 'enc') res = scope === 'component' ? encodeURIComponent(raw) : encodeURI(raw);
    else                res = scope === 'component' ? decodeURIComponent(raw) : decodeURI(raw);
    out.textContent = res;
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; }
}
document.addEventListener('DOMContentLoaded', urlRun);
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('url-in');
  if (!input) return;
  input.value = e.detail.data;
  urlRun();
});
</script>
""",
    "help": {
        "en": """
<h2>What URL encoding does</h2>
<p>URLs and HTTP headers are restricted to a small ASCII subset. Anything outside that set — including spaces, accented letters, emoji, and several reserved punctuation characters — has to be <em>percent-encoded</em>: replaced by <code>%</code> followed by two hex digits per byte. <code>café</code> becomes <code>caf%C3%A9</code> (UTF-8). Decoding reverses that.</p>

<h3>When to use which scope</h3>
<ul>
  <li><strong>Component</strong> — pick this for individual <em>values</em> you'll splice into a URL: query-string values, path segments, fragment text, header values. Encodes the structural characters <code>/ ? # &amp; = +</code> so they don't accidentally end up parsed as URL syntax.</li>
  <li><strong>Full URI</strong> — pick this for a whole URL you want to clean up. Preserves <code>/ ? # &amp; = +</code> as URL structure, only encodes <em>illegal</em> characters (spaces, non-ASCII, etc.).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't double-encode.</strong> Encoding an already-encoded string turns <code>%20</code> into <code>%2520</code>. If your input shows <code>%XX</code> sequences, decode first.</li>
  <li><strong>Spaces aren't always <code>%20</code>.</strong> In <em>application/x-www-form-urlencoded</em> bodies, spaces are <code>+</code>. This tool follows the JavaScript <code>encodeURIComponent</code> convention (always <code>%20</code>); decode handles both.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Modern browsers and <code>encodeURIComponent</code> always use UTF-8. Some older systems still produce Latin-1 percent-escapes — those won't round-trip cleanly here.</li>
  <li><strong>Reserved characters are case-insensitive in the percent-escape but case-sensitive in the decoded result</strong> — <code>%2F</code> and <code>%2f</code> both decode to <code>/</code>, but the original character's case is preserved.</li>
</ul>
""",
        "pt": """
<h2>O que o URL encoding faz</h2>
<p>URLs e headers HTTP são restritos a um pequeno subconjunto do ASCII. Qualquer coisa fora desse conjunto — incluindo espaços, letras acentuadas, emoji e vários caracteres de pontuação reservados — precisa ser <em>percent-encoded</em>: substituída por <code>%</code> seguido de dois dígitos hex por byte. <code>café</code> vira <code>caf%C3%A9</code> (UTF-8). A decodificação reverte isso.</p>

<h3>Quando usar cada scope</h3>
<ul>
  <li><strong>Component</strong> — escolha esta opção para <em>valores</em> individuais que você vai inserir em uma URL: valores de query string, segmentos de path, texto de fragment, valores de header. Codifica os caracteres estruturais <code>/ ? # &amp; = +</code> para que não sejam interpretados acidentalmente como sintaxe de URL.</li>
  <li><strong>Full URI</strong> — escolha esta para uma URL inteira que você quer limpar. Preserva <code>/ ? # &amp; = +</code> como estrutura da URL, codificando apenas caracteres <em>ilegais</em> (espaços, não-ASCII, etc.).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não codifique duas vezes.</strong> Codificar uma string já codificada transforma <code>%20</code> em <code>%2520</code>. Se sua entrada já tem sequências <code>%XX</code>, decodifique primeiro.</li>
  <li><strong>Espaços nem sempre são <code>%20</code>.</strong> Em corpos <em>application/x-www-form-urlencoded</em>, espaços são <code>+</code>. Esta ferramenta segue a convenção do <code>encodeURIComponent</code> do JavaScript (sempre <code>%20</code>); a decodificação aceita os dois.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Browsers modernos e <code>encodeURIComponent</code> sempre usam UTF-8. Alguns sistemas antigos ainda produzem percent-escapes em Latin-1 — esses não fazem round-trip corretamente aqui.</li>
  <li><strong>Caracteres reservados são case-insensitive no percent-escape mas case-sensitive no resultado decodificado</strong> — <code>%2F</code> e <code>%2f</code> ambos decodificam para <code>/</code>, mas o case original do caractere é preservado.</li>
</ul>
""",
        "pl": """
<h2>Co robi URL encoding</h2>
<p>URL-e i nagłówki HTTP są ograniczone do małego podzbioru ASCII. Wszystko poza nim — w tym spacje, litery z diakrytykami, emoji i kilka zarezerwowanych znaków interpunkcyjnych — musi być <em>percent-encoded</em>: zastąpione <code>%</code> i dwiema cyframi hex na bajt. <code>café</code> staje się <code>caf%C3%A9</code> (UTF-8). Dekodowanie odwraca to.</p>

<h3>Kiedy którego scope użyć</h3>
<ul>
  <li><strong>Component</strong> — wybierz to dla pojedynczych <em>wartości</em>, które wkleisz do URL-a: wartości query stringa, segmenty path, tekst fragmentu, wartości nagłówków. Koduje znaki strukturalne <code>/ ? # &amp; = +</code>, żeby nie zostały przypadkowo sparsowane jako składnia URL-a.</li>
  <li><strong>Full URI</strong> — wybierz to dla całego URL-a, który chcesz uporządkować. Zachowuje <code>/ ? # &amp; = +</code> jako strukturę URL-a, koduje tylko znaki <em>nielegalne</em> (spacje, non-ASCII itd.).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie koduj podwójnie.</strong> Zakodowanie już zakodowanego stringa zamienia <code>%20</code> w <code>%2520</code>. Jeśli wejście pokazuje sekwencje <code>%XX</code>, najpierw zdekoduj.</li>
  <li><strong>Spacje nie zawsze to <code>%20</code>.</strong> W ciałach <em>application/x-www-form-urlencoded</em> spacje to <code>+</code>. To narzędzie idzie za konwencją JS-owego <code>encodeURIComponent</code> (zawsze <code>%20</code>); dekodowanie obsługuje obie.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Nowoczesne przeglądarki i <code>encodeURIComponent</code> zawsze używają UTF-8. Niektóre starsze systemy nadal produkują percent-escape w Latin-1 — te nie zrobią tu czystego round-tripu.</li>
  <li><strong>Znaki zarezerwowane są case-insensitive w percent-escape, ale case-sensitive w zdekodowanym wyniku</strong> — <code>%2F</code> i <code>%2f</code> oba dekodują do <code>/</code>, ale oryginalna wielkość znaku jest zachowana.</li>
</ul>
""",
        "ja": """
<h2>URL エンコードの仕組み</h2>
<p>URL や HTTP ヘッダはごく一部の ASCII しか許容しません。空白、アクセント文字、絵文字、いくつかの予約された記号を含めて、それ以外はすべて<em>パーセントエンコード</em>（バイトごとに <code>%</code> + 16 進 2 桁）が必要です。<code>café</code> は UTF-8 で <code>caf%C3%A9</code> になります。デコードはその逆です。</p>

<h3>スコープの使い分け</h3>
<ul>
  <li><strong>Component</strong> — URL に差し込む個別の<em>値</em>（クエリ値、パスセグメント、フラグメント、ヘッダ値）はこちらを選びます。<code>/ ? # &amp; = +</code> も含めて構造記号もエンコードし、URL 構文として誤解釈されないようにします。</li>
  <li><strong>Full URI</strong> — URL 全体を整えたいときに使います。<code>/ ? # &amp; = +</code> は URL 構造として保持し、不正文字（空白、非 ASCII など）だけをエンコードします。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>二重エンコードに注意。</strong> エンコード済みを再度エンコードすると <code>%20</code> が <code>%2520</code> になります。<code>%XX</code> が見えるならまずデコードしてください。</li>
  <li><strong>空白は常に <code>%20</code> ではありません。</strong> <em>application/x-www-form-urlencoded</em> ボディでは空白は <code>+</code> です。本ツールは JS の <code>encodeURIComponent</code> 慣習（常に <code>%20</code>）に従い、デコードはどちらも受け付けます。</li>
  <li><strong>UTF-8 と Latin-1。</strong> モダンブラウザや <code>encodeURIComponent</code> は常に UTF-8。古いシステムが Latin-1 percent-escape を生成する場合、ここでは綺麗にラウンドトリップしないことがあります。</li>
  <li><strong>予約文字の percent-escape は大小無視ですが、デコード結果は大小区別あり。</strong> <code>%2F</code> も <code>%2f</code> も <code>/</code> にデコードされますが、元の文字の大小は保持されます。</li>
</ul>
""",
        "nl": """
<h2>Wat URL-encoding doet</h2>
<p>URLs en HTTP-headers zijn beperkt tot een kleine ASCII-subset. Alles buiten die set — inclusief spaties, accenten, emoji en diverse reserved leestekens — moet <em>percent-encoded</em> worden: vervangen door <code>%</code> gevolgd door twee hex-cijfers per byte. <code>café</code> wordt <code>caf%C3%A9</code> (UTF-8). Decoderen keert dat om.</p>

<h3>Wanneer welke scope</h3>
<ul>
  <li><strong>Component</strong> — kies dit voor individuele <em>values</em> die je in een URL plakt: query-string values, path segments, fragment text, header values. Encodet de structurele karakters <code>/ ? # &amp; = +</code> zodat ze niet per ongeluk als URL-syntax geparseerd worden.</li>
  <li><strong>Full URI</strong> — kies dit voor een hele URL die je wil opschonen. Behoudt <code>/ ? # &amp; = +</code> als URL-structuur, encodet alleen <em>illegale</em> karakters (spaties, non-ASCII, etc.).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Encode niet dubbel.</strong> Een al-encoded string encoderen verandert <code>%20</code> in <code>%2520</code>. Als je input <code>%XX</code>-sequences toont, decodeer eerst.</li>
  <li><strong>Spaties zijn niet altijd <code>%20</code>.</strong> In <em>application/x-www-form-urlencoded</em>-bodies zijn spaties <code>+</code>. Deze tool volgt de JavaScript <code>encodeURIComponent</code>-conventie (altijd <code>%20</code>); decode handelt beide af.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Moderne browsers en <code>encodeURIComponent</code> gebruiken altijd UTF-8. Sommige oudere systemen produceren nog Latin-1 percent-escapes — die round-trippen hier niet schoon.</li>
  <li><strong>Reserved karakters zijn case-insensitive in de percent-escape maar case-sensitive in het decoded resultaat</strong> — <code>%2F</code> en <code>%2f</code> decoderen beide naar <code>/</code>, maar de case van het oorspronkelijke karakter blijft behouden.</li>
</ul>
""",
        "tr": """
<h2>URL kodlama ne yapar</h2>
<p>URL'ler ve HTTP header'ları küçük bir ASCII alt kümesiyle sınırlıdır. Bu setin dışındaki her şey — boşluklar, aksanlı harfler, emoji ve birkaç rezerve noktalama karakteri dahil — <em>percent-encoded</em> olmalıdır: byte başına iki hex basamak izleyen <code>%</code> ile değiştirilir. <code>café</code> <code>caf%C3%A9</code> olur (UTF-8). Çözme bunu tersine çevirir.</p>

<h3>Hangi kapsamı ne zaman kullanmalı</h3>
<ul>
  <li><strong>Component</strong> — bir URL'ye ekleyeceğin bireysel <em>değerler</em> için bunu seç: query string değerleri, path segmentleri, fragment metni, header değerleri. Yapısal karakterleri <code>/ ? # &amp; = +</code> kodlar, böylece yanlışlıkla URL sözdizimi olarak parse edilmezler.</li>
  <li><strong>Full URI</strong> — temizlemek istediğin tüm bir URL için bunu seç. <code>/ ? # &amp; = +</code>'ı URL yapısı olarak korur, yalnızca <em>yasadışı</em> karakterleri (boşluklar, ASCII olmayan, vb.) kodlar.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Çift kodlama yapma.</strong> Zaten kodlanmış bir string'i kodlamak <code>%20</code>'yi <code>%2520</code>'ye çevirir. Girişinde <code>%XX</code> dizileri görüyorsan, önce çöz.</li>
  <li><strong>Boşluklar her zaman <code>%20</code> değildir.</strong> <em>application/x-www-form-urlencoded</em> gövdelerinde, boşluklar <code>+</code>'tır. Bu araç JavaScript <code>encodeURIComponent</code> konvansiyonunu izler (her zaman <code>%20</code>); çözme her ikisini de işler.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Modern tarayıcılar ve <code>encodeURIComponent</code> her zaman UTF-8 kullanır. Bazı eski sistemler hâlâ Latin-1 percent-escape'leri üretir — bunlar burada temiz round-trip yapmaz.</li>
  <li><strong>Rezerve karakterler percent-escape'te büyük/küçük harfe duyarsızdır ama çözülmüş sonuçta büyük/küçük harfe duyarlıdır</strong> — <code>%2F</code> ve <code>%2f</code> ikisi de <code>/</code>'a çözülür, ama orijinal karakterin case'i korunur.</li>
</ul>
""",
        "id": """
<h2>Apa yang dilakukan URL encoding</h2>
<p>URL dan HTTP header dibatasi pada subset ASCII yang kecil. Apa pun di luar set itu — termasuk spasi, huruf beraksen, emoji, dan beberapa karakter punctuation reserved — harus di-<em>percent-encoded</em>: diganti dengan <code>%</code> diikuti dua digit hex per byte. <code>café</code> menjadi <code>caf%C3%A9</code> (UTF-8). Decoding membalikkan itu.</p>

<h3>Kapan pakai scope mana</h3>
<ul>
  <li><strong>Component</strong> — pilih ini untuk <em>value</em> individual yang akan kamu sisipkan ke URL: nilai query-string, segment path, teks fragment, nilai header. Meng-encode karakter struktural <code>/ ? # &amp; = +</code> supaya tidak terparse sebagai sintaks URL secara tidak sengaja.</li>
  <li><strong>Full URI</strong> — pilih ini untuk seluruh URL yang ingin kamu bersihkan. Mempertahankan <code>/ ? # &amp; = +</code> sebagai struktur URL, hanya meng-encode karakter <em>ilegal</em> (spasi, non-ASCII, dll).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Jangan double-encode.</strong> Meng-encode string yang sudah di-encode mengubah <code>%20</code> jadi <code>%2520</code>. Jika input kamu menampilkan sequence <code>%XX</code>, decode dulu.</li>
  <li><strong>Spasi tidak selalu <code>%20</code>.</strong> Di body <em>application/x-www-form-urlencoded</em>, spasi adalah <code>+</code>. Tool ini mengikuti konvensi <code>encodeURIComponent</code> JavaScript (selalu <code>%20</code>); decode meng-handle keduanya.</li>
  <li><strong>UTF-8 vs Latin-1.</strong> Browser modern dan <code>encodeURIComponent</code> selalu pakai UTF-8. Beberapa sistem lama masih menghasilkan percent-escape Latin-1 — itu tidak akan round-trip dengan bersih di sini.</li>
  <li><strong>Karakter reserved itu case-insensitive di percent-escape tapi case-sensitive di hasil decoded</strong> — <code>%2F</code> dan <code>%2f</code> keduanya di-decode jadi <code>/</code>, tapi case karakter asli dipertahankan.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>URL có cú pháp đặc biệt — <code>/</code>, <code>?</code>, <code>&amp;</code>, <code>#</code>, space đều có ý nghĩa. Để chèn ký tự đó như văn bản trong path hoặc query string, bạn phải percent-encode chúng: space thành <code>%20</code>, <code>?</code> thành <code>%3F</code>, etc. Tool này thực hiện encoding và decoding theo cả hai chiều — UTF-8 safe.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Xây dựng URL với param chứa space hoặc ký tự đặc biệt.</li>
  <li>Decode URL từ log để xem param thực.</li>
  <li>Encode tên file để dùng trong URL (đặc biệt với ký tự không-ASCII).</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>encodeURIComponent vs encodeURI.</strong> Trong JavaScript, dùng <code>encodeURIComponent</code> cho component (giá trị param); <code>encodeURI</code> giữ delimiter URL không-encoded.</li>
  <li><strong>+ vs %20 cho space.</strong> Trong query string, cả hai thường được chấp nhận; <code>%20</code> ổn định hơn vì <code>+</code> chỉ là space trong query string, không phải trong path.</li>
  <li><strong>Encode kép gây ra "%2520" — kép-encode <code>%</code>.</strong> Nếu bạn thấy điều đó, decode hai lần để hiểu cái gì có ở đó.</li>
</ul>
""",
        "hi": """
<h2>URL encoding क्या करता है</h2>
<p>URL और HTTP headers एक छोटे ASCII subset तक सीमित हैं। उस set के बाहर कुछ भी — spaces, उच्चारण-चिह्न वाले अक्षर, emoji और कई reserved विराम-चिह्न सहित — को <em>percent-encoded</em> होना चाहिए: प्रति byte <code>%</code> के बाद दो hex digits द्वारा प्रतिस्थापित। <code>café</code> <code>caf%C3%A9</code> (UTF-8) बन जाता है। Decoding इसे उलट देता है।</p>

<h3>किस scope का कब उपयोग करें</h3>
<ul>
  <li><strong>Component</strong> — व्यक्तिगत <em>values</em> के लिए इसे चुनें जिन्हें आप URL में जोड़ेंगे: query-string values, path segments, fragment text, header values। संरचनात्मक अक्षरों <code>/ ? # &amp; = +</code> को encode करता है ताकि वे गलती से URL syntax के रूप में parse न हो जाएं।</li>
  <li><strong>Full URI</strong> — किसी पूरे URL के लिए इसे चुनें जिसे आप साफ़ करना चाहते हैं। <code>/ ? # &amp; = +</code> को URL संरचना के रूप में सुरक्षित रखता है, केवल <em>अवैध</em> अक्षरों (spaces, non-ASCII, आदि) को encode करता है।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>दो बार encode न करें।</strong> पहले से encoded string को encode करना <code>%20</code> को <code>%2520</code> में बदल देता है। यदि आपका input <code>%XX</code> क्रम दिखाता है, तो पहले decode करें।</li>
  <li><strong>Spaces हमेशा <code>%20</code> नहीं होते।</strong> <em>application/x-www-form-urlencoded</em> bodies में, spaces <code>+</code> होते हैं। यह टूल JavaScript <code>encodeURIComponent</code> सम्मेलन का पालन करता है (हमेशा <code>%20</code>); decode दोनों को संभालता है।</li>
  <li><strong>UTF-8 बनाम Latin-1.</strong> आधुनिक browsers और <code>encodeURIComponent</code> हमेशा UTF-8 का उपयोग करते हैं। कुछ पुराने systems अभी भी Latin-1 percent-escapes उत्पन्न करते हैं — वे यहां स्वच्छ रूप से round-trip नहीं करेंगे।</li>
  <li><strong>Reserved अक्षर percent-escape में case-insensitive हैं लेकिन decoded परिणाम में case-sensitive हैं</strong> — <code>%2F</code> और <code>%2f</code> दोनों <code>/</code> में decode होते हैं, लेकिन मूल अक्षर का case सुरक्षित रहता है।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>URL môže obsahovať len ASCII a niektoré špeciálne znaky. Všetko ostatné — diakritika, medzery, ampersands — musí byť percent-encoded (<code>%20</code> pre medzeru, <code>%C3%A1</code> pre <code>á</code>). Tento nástroj percent-encoduje vstup alebo dekóduje percent-encoded reťazec späť.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>Príprava query parametra s diakritikou alebo špeciálnymi znakmi.</li>
  <li>Dekódovanie URL z log-u, kde je <code>%C3%A1</code> namiesto <code>á</code>.</li>
  <li>Encoding hodnoty pre Header alebo Cookie.</li>
  <li>Debug, prečo URL nefunguje (čo je tam zle escapované).</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>encodeURI vs. encodeURIComponent.</strong> JS má dve funkcie. <code>encodeURIComponent</code> escapuje viac (vrátane <code>&amp;</code>, <code>=</code>), použij pre hodnoty parametrov.</li>
  <li><strong>Medzera: <code>%20</code> alebo <code>+</code>.</strong> V query stringu <code>+</code> = medzera (form-encoding); v path-i len <code>%20</code>.</li>
  <li><strong>Double encoding.</strong> Ak encoduješ už encoded reťazec, dostaneš dvojito encoded — <code>%2520</code>.</li>
  <li><strong>UTF-8 bytes.</strong> Percent-encoding zakóduje UTF-8 bajty, nie codepointy. <code>á</code> = 2 bajty = <code>%C3%A1</code>.</li>
  <li><strong>Reserved characters.</strong> <code>:/?#[]@!$&amp;'()*+,;=</code> majú špeciálny význam — pri použití v hodnote ich treba encodovať.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>URL může obsahovat jen ASCII a některé speciální znaky. Všechno ostatní — diakritika, mezery, ampersands — musí být percent-encoded (<code>%20</code> pro mezeru, <code>%C3%A1</code> pro <code>á</code>). Tenhle nástroj percent-encoduje vstup nebo dekóduje percent-encoded řetězec zpět.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>Příprava query parametru s diakritikou nebo speciálními znaky.</li>
  <li>Dekódování URL z logu, kde je <code>%C3%A1</code> místo <code>á</code>.</li>
  <li>Encoding hodnoty pro Header nebo Cookie.</li>
  <li>Debug, proč URL nefunguje (co je tam špatně escapované).</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>encodeURI vs. encodeURIComponent.</strong> JS má dvě funkce. <code>encodeURIComponent</code> escapuje víc (včetně <code>&amp;</code>, <code>=</code>), použij pro hodnoty parametrů.</li>
  <li><strong>Mezera: <code>%20</code> nebo <code>+</code>.</strong> V query stringu <code>+</code> = mezera (form-encoding); v pathu jen <code>%20</code>.</li>
  <li><strong>Double encoding.</strong> Pokud encoduješ už encoded řetězec, dostaneš dvojitě encoded — <code>%2520</code>.</li>
  <li><strong>UTF-8 bytes.</strong> Percent-encoding zakóduje UTF-8 bajty, ne codepointy. <code>á</code> = 2 bajty = <code>%C3%A1</code>.</li>
  <li><strong>Reserved characters.</strong> <code>:/?#[]@!$&amp;'()*+,;=</code> mají speciální význam — při použití v hodnotě je třeba je encodovat.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "html-encoder", "qr-code-generator"],
    "howto": {"flow": "transform", "action": "encode",  "noun": "text"},
}
