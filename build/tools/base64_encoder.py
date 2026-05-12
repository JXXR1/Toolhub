TOOL = {
    "slug": "base64-encoder",
    "category": "encoding",
    "icon": "🔄",
    "tags": ["base64", "encode", "decode", "data-uri"],
    "i18n": {
        "en": {
            "name": "Base64 Encoder / Decoder",
            "tagline": "Encode text to Base64 or decode Base64 back to text. UTF-8 safe and base64url variant supported.",
            "description": "Free online Base64 encoder and decoder. UTF-8 safe with optional base64url variant for URLs and JWTs. Runs in your browser.",
        },
        "de": {"name": "Base64 Encoder / Decoder", "tagline": "Text in Base64 codieren oder Base64 in Text decodieren. UTF-8-sicher und base64url-Variante.", "description": "Kostenloser Base64 Encoder und Decoder. UTF-8-sicher mit optionaler base64url-Variante für URLs und JWTs."},
        "es": {"name": "Codificador / Decodificador Base64", "tagline": "Codifica texto a Base64 o decodifica Base64 a texto. Compatible con UTF-8 y variante base64url.", "description": "Codificador y decodificador Base64 gratuito. Compatible con UTF-8 y variante base64url para URLs y JWTs."},
        "fr": {"name": "Encodeur / Décodeur Base64", "tagline": "Encodez du texte en Base64 ou décodez du Base64 en texte. UTF-8 et variante base64url supportées.", "description": "Encodeur et décodeur Base64 gratuit. Compatible UTF-8 avec variante base64url pour URLs et JWTs."},
        "it": {"name": "Encoder / Decoder Base64", "tagline": "Codifica testo in Base64 o decodifica Base64 in testo. UTF-8 sicuro con variante base64url.", "description": "Encoder e decoder Base64 gratuito. UTF-8 sicuro con variante base64url per URL e JWT."},
        "pt": {"name": "Codificador / Decodificador Base64", "tagline": "Codifique texto em Base64 ou decodifique Base64 de volta em texto. Seguro em UTF-8 e suporta a variante base64url.", "description": "Codificador e decodificador Base64 online gratuito. Seguro em UTF-8 com variante base64url opcional para URLs e JWTs. Roda no seu navegador."},
        "pl": {"name": "Encoder / Decoder Base64", "tagline": "Koduj tekst do Base64 albo dekoduj Base64 z powrotem na tekst. Bezpieczny dla UTF-8, wariant base64url.", "description": "Darmowy encoder i decoder Base64 online. Bezpieczny dla UTF-8 z opcjonalnym wariantem base64url dla URL-i i JWT. Działa w przeglądarce."},
        "ja": {"name": "Base64 エンコーダー / デコーダー", "tagline": "テキストを Base64 にエンコード、または Base64 をテキストにデコード。UTF-8 対応で base64url バリアントもサポート。", "description": "オンライン無料の Base64 エンコーダー・デコーダー。UTF-8 安全で、URL や JWT 向けの base64url バリアントにも対応。すべてブラウザ内で処理されます。"},
        "nl": {"name": "Base64 Encoder / Decoder", "tagline": "Codeer tekst naar Base64 of decodeer Base64 terug naar tekst. UTF-8 safe met base64url-variant.", "description": "Gratis online Base64 encoder en decoder. UTF-8 safe met optionele base64url-variant voor URLs en JWTs. Draait in je browser."},
        "tr": {"name": "Base64 Encoder / Decoder", "tagline": "Metni Base64'e kodla veya Base64'ü metne çöz. UTF-8 güvenli, base64url varyantı destekli.", "description": "Ücretsiz online Base64 encoder ve decoder. UTF-8 güvenli, URL ve JWT'ler için opsiyonel base64url varyantı. Tarayıcıda çalışır."},
        "id": {"name": "Base64 Encoder / Decoder", "tagline": "Encode teks ke Base64 atau decode Base64 kembali ke teks. Aman untuk UTF-8 dengan dukungan varian base64url.", "description": "Encoder dan decoder Base64 online gratis. Aman untuk UTF-8 dengan varian base64url opsional untuk URL dan JWT. Berjalan di browser-mu."},
        "vi": {"name": "Base64 Encoder / Decoder", "tagline": "Encode văn bản thành Base64 hoặc decode Base64 về văn bản. An toàn UTF-8 và hỗ trợ biến thể base64url.", "description": "Base64 encoder và decoder trực tuyến miễn phí. An toàn UTF-8 với biến thể base64url tùy chọn cho URL và JWT. Chạy trong trình duyệt của bạn."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="b64-mode" onchange="b64Run()">
        <option value="enc">{LBL_ENCODE} (text → base64)</option>
        <option value="dec">{LBL_DECODE} (base64 → text)</option>
      </select>
    </div>
    <div>
      <label>Variant</label>
      <select id="b64-variant" onchange="b64Run()">
        <option value="std">Standard</option>
        <option value="url">base64url (URL/JWT-safe)</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="b64-in" oninput="b64Run()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="b64-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('b64-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="b64-meta"></div>
</div>
""",
    "script": """
<script>
function b64Encode(s, urlSafe){
  const bytes = new TextEncoder().encode(s);
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  let out = btoa(bin);
  if (urlSafe) out = out.replace(/\\+/g,'-').replace(/\\//g,'_').replace(/=+$/,'');
  return out;
}
function b64Decode(s, urlSafe){
  let t = s.replace(/\\s+/g,'');
  if (urlSafe) t = t.replace(/-/g,'+').replace(/_/g,'/');
  while (t.length % 4) t += '=';
  const bin = atob(t);
  const bytes = new Uint8Array(bin.length);
  for (let i=0; i<bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder('utf-8', {fatal: true}).decode(bytes);
}
function b64Run(){
  const mode = document.getElementById('b64-mode').value;
  const variant = document.getElementById('b64-variant').value;
  const raw = document.getElementById('b64-in').value;
  const out = document.getElementById('b64-out');
  const meta = document.getElementById('b64-meta');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent = ''; return; }
  try {
    const result = (mode === 'enc') ? b64Encode(raw, variant === 'url') : b64Decode(raw, variant === 'url');
    out.textContent = result;
    meta.textContent = result.length + ' chars';
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + (e.message || e); meta.textContent = ''; }
}
document.addEventListener('DOMContentLoaded', b64Run);
</script>
""",
    "help": {
        "en": """
<h2>What Base64 actually does</h2>
<p>Base64 turns arbitrary bytes into 64 ASCII characters (A–Z, a–z, 0–9 plus two extras). Three input bytes become four output characters, so the result is roughly 33% larger than the input. It's an <em>encoding</em>, not encryption — anyone can decode it.</p>

<h3>When to use Base64</h3>
<ul>
  <li>Embedding small binary data inside text-only formats: data URIs, JSON values, environment variables, YAML strings.</li>
  <li>Encoding binary tokens (signatures, keys, hashes) for inclusion in URLs, headers, or cookies.</li>
  <li>Email attachments and SMIME — historic but still alive.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) uses <code>+</code>, <code>/</code>, <code>=</code>. Fine in email, JSON values, most XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) uses <code>-</code>, <code>_</code>, and typically drops trailing <code>=</code> padding. Used in JWTs, OAuth tokens, and anywhere the value lives in a URL where <code>+</code>/<code>/</code>/<code>=</code> would need extra escaping.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't confuse it with encryption.</strong> Base64 is reversible by anyone. If the data is sensitive, encrypt it first.</li>
  <li><strong>UTF-8 round-trips correctly here</strong> — non-ASCII (é, 你好, 🚀) goes through <code>TextEncoder</code>/<code>TextDecoder</code>, not <code>btoa</code>/<code>atob</code> directly. Naive <code>btoa(str)</code> in JavaScript breaks on non-Latin characters.</li>
  <li><strong>Padding</strong> — standard Base64 always ends with 0/1/2 <code>=</code> characters depending on input length. base64url often omits them. Decoders that require padding will reject unpadded input; this tool re-adds it on decode if missing.</li>
  <li><strong>Whitespace inside encoded strings</strong> — the decoder here strips spaces and line breaks (common from copy-paste), but some libraries don't, so re-encode if you're piping to one of those.</li>
</ul>
""",
        "pt": """
<h2>O que o Base64 faz de verdade</h2>
<p>Base64 transforma bytes arbitrários em 64 caracteres ASCII (A–Z, a–z, 0–9 mais dois extras). Três bytes de entrada viram quatro caracteres de saída, então o resultado fica cerca de 33% maior que a entrada. É um <em>encoding</em>, não criptografia — qualquer um consegue decodificar.</p>

<h3>Quando usar Base64</h3>
<ul>
  <li>Embutir pequenos dados binários dentro de formatos só-texto: data URIs, valores JSON, variáveis de ambiente, strings YAML.</li>
  <li>Codificar tokens binários (assinaturas, chaves, hashes) para incluir em URLs, headers ou cookies.</li>
  <li>Anexos de e-mail e SMIME — histórico mas ainda em uso.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) usa <code>+</code>, <code>/</code>, <code>=</code>. Funciona bem em e-mail, valores JSON, na maioria dos XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) usa <code>-</code>, <code>_</code> e tipicamente descarta o padding <code>=</code> no final. Usado em JWTs, tokens OAuth e em qualquer lugar onde o valor mora numa URL e <code>+</code>/<code>/</code>/<code>=</code> precisariam de escape extra.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não confunda com criptografia.</strong> Base64 é reversível por qualquer um. Se o dado é sensível, criptografe primeiro.</li>
  <li><strong>UTF-8 faz round-trip corretamente aqui</strong> — caracteres não-ASCII (é, 你好, 🚀) passam por <code>TextEncoder</code>/<code>TextDecoder</code>, e não direto por <code>btoa</code>/<code>atob</code>. <code>btoa(str)</code> ingênuo em JavaScript quebra com caracteres não-latinos.</li>
  <li><strong>Padding</strong> — Base64 standard sempre termina com 0/1/2 caracteres <code>=</code> dependendo do tamanho da entrada. base64url frequentemente os omite. Decoders que exigem padding rejeitam entrada sem padding; esta ferramenta readiciona o padding no decode se estiver faltando.</li>
  <li><strong>Whitespace dentro de strings codificadas</strong> — o decoder aqui remove espaços e quebras de linha (comuns em copiar/colar), mas algumas bibliotecas não fazem isso, então recodifique se você for jogar o resultado numa delas.</li>
</ul>
""",
        "pl": """
<h2>Co Base64 właściwie robi</h2>
<p>Base64 zamienia dowolne bajty w 64 znaki ASCII (A–Z, a–z, 0–9 plus dwa dodatkowe). Trzy bajty wejścia stają się czterema znakami wyjścia, więc wynik jest mniej więcej 33% większy od wejścia. To <em>kodowanie</em>, nie szyfrowanie — każdy może to zdekodować.</p>

<h3>Kiedy używać Base64</h3>
<ul>
  <li>Wstawianie małych binarnych danych w formaty tekstowe: data URI, wartości JSON, zmienne środowiskowe, stringi YAML.</li>
  <li>Kodowanie binarnych tokenów (sygnatury, klucze, hashe) do umieszczenia w URL-ach, headerach albo cookies.</li>
  <li>Załączniki maili i SMIME — historyczne, ale wciąż żywe.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) używa <code>+</code>, <code>/</code>, <code>=</code>. OK w mailu, wartościach JSON, większości XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) używa <code>-</code>, <code>_</code> i zwykle pomija końcowy padding <code>=</code>. Używany w JWT, tokenach OAuth i wszędzie tam, gdzie wartość siedzi w URL-u, gdzie <code>+</code>/<code>/</code>/<code>=</code> wymagałyby dodatkowego escape'owania.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie myl tego z szyfrowaniem.</strong> Base64 jest odwracalny przez każdego. Jeśli dane są wrażliwe — najpierw je zaszyfruj.</li>
  <li><strong>UTF-8 robi tu poprawny round-trip</strong> — znaki spoza ASCII (é, 你好, 🚀) idą przez <code>TextEncoder</code>/<code>TextDecoder</code>, nie bezpośrednio przez <code>btoa</code>/<code>atob</code>. Naiwne <code>btoa(str)</code> w JavaScripcie wywala się na znakach niełacińskich.</li>
  <li><strong>Padding</strong> — standardowy Base64 zawsze kończy się 0/1/2 znakami <code>=</code> w zależności od długości wejścia. base64url często go pomija. Dekodery wymagające paddingu odrzucają dane bez paddingu; to narzędzie sam dokleja go przy dekodowaniu, jeśli go brakuje.</li>
  <li><strong>Białe znaki w środku zakodowanego stringa</strong> — ten dekoder usuwa spacje i końce linii (typowe po copy-paste), ale niektóre biblioteki tego nie robią, więc przekoduj zanim wrzucisz to do takiej.</li>
</ul>
""",
        "ja": """
<h2>Base64 が実際にやっていること</h2>
<p>Base64 は任意のバイト列を 64 個の ASCII 文字（A–Z、a–z、0–9 と 2 文字の追加文字）に変換します。入力 3 バイトが出力 4 文字になるため、結果は入力よりおよそ 33% 大きくなります。これは<em>エンコーディング</em>であり、暗号化ではありません。誰でもデコード可能です。</p>

<h3>Base64 を使うべきタイミング</h3>
<ul>
  <li>テキスト形式の中に小さなバイナリデータを埋め込みたいとき：data URI、JSON 値、環境変数、YAML 文字列など。</li>
  <li>バイナリトークン（署名、鍵、ハッシュ）を URL、ヘッダー、Cookie に含めたいとき。</li>
  <li>メール添付や SMIME — 古いですが今も使われています。</li>
</ul>

<h3>Standard と base64url</h3>
<ul>
  <li><strong>Standard</strong>（<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>）は <code>+</code>、<code>/</code>、<code>=</code> を使います。メール、JSON 値、ほとんどの XML で問題ありません。</li>
  <li><strong>base64url</strong>（<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>）は <code>-</code>、<code>_</code> を使い、通常は末尾の <code>=</code> パディングを省略します。JWT、OAuth トークン、URL に値が入る場面で <code>+</code>/<code>/</code>/<code>=</code> の追加エスケープを避けたいときに使われます。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>暗号化と混同しないこと。</strong> Base64 は誰でも復元できます。機密データならまず暗号化してください。</li>
  <li><strong>UTF-8 はここで正しくラウンドトリップします</strong> — 非 ASCII 文字（é、你好、🚀）は <code>TextEncoder</code>/<code>TextDecoder</code> を経由し、<code>btoa</code>/<code>atob</code> を直接使うわけではありません。JavaScript で素朴に <code>btoa(str)</code> を呼ぶと非ラテン文字で壊れます。</li>
  <li><strong>パディング</strong> — 標準 Base64 は入力長に応じて 0/1/2 個の <code>=</code> で終わります。base64url では省略されることが多いです。パディングを必須とするデコーダーは省略形を拒否しますが、このツールはデコード時に不足分を補います。</li>
  <li><strong>エンコード文字列内の空白</strong> — このデコーダーはスペースや改行を取り除きます（コピペ時によく混入します）。一部のライブラリはこれを行わないため、そのようなライブラリに渡す場合は再エンコードしてください。</li>
</ul>
""",
        "nl": """
<h2>Wat Base64 eigenlijk doet</h2>
<p>Base64 zet willekeurige bytes om naar 64 ASCII-tekens (A–Z, a–z, 0–9 plus twee extra's). Drie input-bytes worden vier output-tekens, dus het resultaat is grofweg 33% groter dan de input. Het is een <em>encoding</em>, geen encryptie — iedereen kan het decoderen.</p>

<h3>Wanneer Base64 gebruiken</h3>
<ul>
  <li>Kleine binaire data inbedden in tekstformaten: data URIs, JSON-waarden, environment variables, YAML-strings.</li>
  <li>Binaire tokens coderen (handtekeningen, keys, hashes) om in URLs, headers of cookies te zetten.</li>
  <li>Email-bijlagen en S/MIME — historisch maar nog steeds in gebruik.</li>
</ul>

<h3>Standaard vs base64url</h3>
<ul>
  <li><strong>Standaard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) gebruikt <code>+</code>, <code>/</code>, <code>=</code>. Prima in email, JSON-waarden, de meeste XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) gebruikt <code>-</code>, <code>_</code>, en laat doorgaans de trailing <code>=</code> padding weg. Gebruikt in JWTs, OAuth-tokens en overal waar de waarde in een URL leeft, waar <code>+</code>/<code>/</code>/<code>=</code> extra escaping zouden vereisen.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Verwar het niet met encryptie.</strong> Base64 is door iedereen omkeerbaar. Als de data gevoelig is, versleutel het eerst.</li>
  <li><strong>UTF-8 round-trips hier correct</strong> — non-ASCII (é, 你好, 🚀) gaat door <code>TextEncoder</code>/<code>TextDecoder</code>, niet direct door <code>btoa</code>/<code>atob</code>. Naïeve <code>btoa(str)</code> in JavaScript breekt op niet-Latin tekens.</li>
  <li><strong>Padding</strong> — standaard Base64 eindigt altijd op 0/1/2 <code>=</code>-tekens afhankelijk van de input-lengte. base64url laat ze vaak weg. Decoders die padding vereisen weigeren input zonder padding; deze tool voegt het weer toe bij decoderen indien afwezig.</li>
  <li><strong>Whitespace in encoded strings</strong> — de decoder hier strijkt spaties en regeleinden eruit (komen vaak van copy-paste), maar sommige libraries niet, dus re-encode als je naar zo'n library doorstuurt.</li>
</ul>
""",
        "tr": """
<h2>Base64 gerçekte ne yapar</h2>
<p>Base64, rastgele byte'ları 64 ASCII karaktere (A–Z, a–z, 0–9 artı iki ek) çevirir. Üç giriş byte'ı dört çıkış karakteri olur, yani sonuç girişten kabaca %33 daha büyüktür. Bu bir <em>kodlama</em>dır, şifreleme değil — herkes çözebilir.</p>

<h3>Base64'ü ne zaman kullanmalı</h3>
<ul>
  <li>Küçük ikilik verileri sadece metin biçimlerine gömerken: data URI'ler, JSON değerleri, ortam değişkenleri, YAML string'leri.</li>
  <li>İkilik token'ları (imzalar, anahtarlar, hash'ler) URL, header veya cookie'lere dahil etmek için kodlama.</li>
  <li>E-posta ekleri ve SMIME — tarihsel ama hâlâ canlı.</li>
</ul>

<h3>Standart - base64url</h3>
<ul>
  <li><strong>Standart</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) <code>+</code>, <code>/</code>, <code>=</code> kullanır. E-posta, JSON değerleri, çoğu XML'de uygundur.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) <code>-</code>, <code>_</code> kullanır ve genellikle sondaki <code>=</code> padding'ini düşürür. JWT'ler, OAuth token'ları ve değerin URL içinde yaşadığı yerlerde kullanılır.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Şifrelemeyle karıştırma.</strong> Base64 herkes tarafından geri çevrilebilir. Veri hassassa, önce şifrele.</li>
  <li><strong>UTF-8 burada doğru round-trip yapar</strong> — ASCII olmayan (é, 你好, 🚀) doğrudan <code>btoa</code>/<code>atob</code>'dan değil, <code>TextEncoder</code>/<code>TextDecoder</code>'dan geçer. JavaScript'te naif <code>btoa(str)</code> Latin olmayan karakterlerde bozulur.</li>
  <li><strong>Padding</strong> — standart Base64 giriş uzunluğuna bağlı olarak her zaman 0/1/2 <code>=</code> karakteriyle biter. base64url genellikle bunları atlar. Padding gerektiren decoder'lar padding'siz girişi reddeder; bu araç decode sırasında eksikse yeniden ekler.</li>
  <li><strong>Kodlanmış string içindeki boşluk</strong> — buradaki decoder boşluklar ve satır sonlarını temizler (kopyala-yapıştırdan yaygın), ancak bazı kütüphaneler temizlemez, bu nedenle birine pipe yapıyorsan yeniden kodla.</li>
</ul>
""",
        "id": """
<h2>Apa yang sebenarnya Base64 lakukan</h2>
<p>Base64 mengubah byte arbitrer menjadi 64 karakter ASCII (A–Z, a–z, 0–9 ditambah dua karakter ekstra). Tiga byte input menjadi empat karakter output, jadi hasilnya sekitar 33% lebih besar dari input. Ini adalah <em>encoding</em>, bukan enkripsi — siapa saja bisa decode-nya.</p>

<h3>Kapan menggunakan Base64</h3>
<ul>
  <li>Menanamkan data biner kecil di dalam format yang hanya teks: data URI, value JSON, environment variable, string YAML.</li>
  <li>Meng-encode token biner (signature, key, hash) untuk dimasukkan ke URL, header, atau cookie.</li>
  <li>Attachment email dan SMIME — historis tapi masih hidup.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) pakai <code>+</code>, <code>/</code>, <code>=</code>. Aman di email, value JSON, sebagian besar XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) pakai <code>-</code>, <code>_</code>, dan biasanya menghilangkan trailing padding <code>=</code>. Dipakai di JWT, OAuth token, dan di mana pun value-nya hidup di URL di mana <code>+</code>/<code>/</code>/<code>=</code> akan butuh escape tambahan.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Jangan keliru dengan enkripsi.</strong> Base64 reversible oleh siapa pun. Kalau datanya sensitif, enkripsi dulu.</li>
  <li><strong>UTF-8 round-trip dengan benar di sini</strong> — non-ASCII (é, 你好, 🚀) lewat <code>TextEncoder</code>/<code>TextDecoder</code>, bukan <code>btoa</code>/<code>atob</code> langsung. <code>btoa(str)</code> naif di JavaScript rusak pada karakter non-Latin.</li>
  <li><strong>Padding</strong> — Base64 standard selalu berakhir dengan 0/1/2 karakter <code>=</code> tergantung panjang input. base64url sering menghilangkannya. Decoder yang butuh padding akan menolak input tanpa padding; tool ini menambahkannya kembali saat decode kalau hilang.</li>
  <li><strong>Whitespace di dalam string yang sudah di-encode</strong> — decoder di sini menghapus spasi dan line break (umum dari copy-paste), tapi beberapa library tidak, jadi encode ulang kalau kamu menyalurkan ke library seperti itu.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Base64 mã hóa dữ liệu nhị phân tùy ý thành 64 ký tự ASCII an toàn (A–Z, a–z, 0–9, + và /) bằng cách nhóm các byte thành các đoạn 6 bit. Điều đó cho phép bạn chèn dữ liệu nhị phân vào các nơi chỉ chấp nhận văn bản: email, JSON, URL, HTML, cấu hình YAML. Việc encode thêm khoảng một phần ba kích thước nhưng làm cho payload tồn tại được qua bất kỳ giao thức text-only nào.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Nhúng ảnh hoặc font nhỏ vào CSS dưới dạng data URI.</li>
  <li>Đặt token đã encode (như JWT) vào header HTTP hoặc URL.</li>
  <li>Decode payload Base64 từ API hoặc log để xem nó thực sự chứa gì.</li>
  <li>Bọc PEM key (RSA, EC) và chứng chỉ X.509 — chúng là DER nhị phân được wrap bằng Base64.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>base64 không phải là mã hóa.</strong> Nó là encoding — bất kỳ ai cũng có thể decode nó. Đừng dùng nó để "bảo vệ" mật khẩu hay secret.</li>
  <li><strong>base64url khác với base64 chuẩn.</strong> JWT, OAuth và một số API dùng base64url, thay <code>+</code> bằng <code>-</code>, <code>/</code> bằng <code>_</code> và (thường) bỏ <code>=</code> padding. Decode lẫn nhau sẽ thất bại.</li>
  <li><strong>Padding quan trọng.</strong> Base64 chuẩn cần độ dài đầu vào là bội số của 4, được pad bằng <code>=</code>. Bỏ qua hoặc thêm padding có thể phá vỡ decoder ngặt nghèo.</li>
  <li><strong>UTF-8 trước, rồi mới base64.</strong> Khi encode chuỗi không-ASCII, chuyển sang byte UTF-8 trước. Mã hóa kép hoặc dùng encoding khác sẽ làm hỏng văn bản.</li>
</ul>
""",
    },
    "related": ["url-encoder", "html-encoder", "jwt-decoder", "image-to-base64"],
    "howto": {"flow": "transform", "action": "encode", "noun": "text"},
}
