TOOL = {
    "slug": "qr-code-generator",
    "category": "media",
    "icon": "📱",
    "tags": ["qr", "code", "generate", "url", "wifi", "vcard", "svg", "png"],
    "i18n": {
        "en": {
            "name": "QR Code Generator",
            "tagline": "Generate QR codes for any text, URL, Wi-Fi, or vCard. Custom size, colors, and error correction. Export PNG or SVG.",
            "description": "Free online QR code generator. Custom size, foreground/background colors, error correction levels. Download as PNG or SVG. No watermarks.",
        },
        "de": {
            "name": "QR-Code-Generator",
            "tagline": "Erzeuge QR-Codes für Text, URLs, WLAN oder vCards. Größe, Farben und Fehlerkorrektur einstellbar. Export als PNG oder SVG.",
            "description": "Kostenloser QR-Code-Generator. Größe, Vorder-/Hintergrundfarbe und Fehlerkorrekturstufen. PNG oder SVG ohne Wasserzeichen.",
        },
        "es": {
            "name": "Generador de Códigos QR",
            "tagline": "Genera códigos QR para texto, URLs, Wi-Fi o vCards. Tamaño, colores y corrección de errores personalizables. Exporta PNG o SVG.",
            "description": "Generador de códigos QR gratuito en línea. Tamaño, colores y niveles de corrección de errores personalizables. PNG o SVG sin marcas de agua.",
        },
        "fr": {
            "name": "Générateur de Codes QR",
            "tagline": "Générez des codes QR pour du texte, URL, Wi-Fi ou vCard. Taille, couleurs et correction d'erreurs personnalisables. Export PNG ou SVG.",
            "description": "Générateur de codes QR gratuit en ligne. Taille, couleurs avant/arrière, niveaux de correction. PNG ou SVG sans filigrane.",
        },
        "it": {
            "name": "Generatore di Codici QR",
            "tagline": "Genera codici QR per testo, URL, Wi-Fi o vCard. Dimensione, colori e correzione errori personalizzabili. Esporta PNG o SVG.",
            "description": "Generatore di codici QR gratuito online. Dimensione, colori e livelli di correzione errori personalizzabili. PNG o SVG senza filigrane.",
        },
        "pt": {
            "name": "Gerador de QR Code",
            "tagline": "Gere QR codes para qualquer texto, URL, Wi-Fi ou vCard. Tamanho, cores e correção de erro personalizáveis. Exporte como PNG ou SVG.",
            "description": "Gerador de QR code gratuito online. Tamanho, cores de foreground/background e níveis de correção de erro personalizáveis. Baixe como PNG ou SVG. Sem marca d'água.",
        },
        "pl": {
            "name": "Generator Kodów QR",
            "tagline": "Generuj kody QR dla dowolnego tekstu, URL-a, Wi-Fi albo vCard. Konfigurowalny rozmiar, kolory i korekcja błędów. Eksportuj PNG albo SVG.",
            "description": "Darmowy online generator kodów QR. Konfigurowalny rozmiar, kolory foreground/background i poziomy korekcji błędów. Pobierz jako PNG albo SVG. Bez znaków wodnych.",
        },
        "ja": {
            "name": "QR コードジェネレーター",
            "tagline": "テキスト、URL、Wi-Fi、vCard などから QR コードを生成。サイズ・色・誤り訂正を指定可能。PNG／SVG で書き出し。",
            "description": "オンライン無料の QR コードジェネレーター。サイズ、前景／背景色、誤り訂正レベルをカスタマイズし、PNG または SVG でダウンロード可能。透かしはありません。",
        },
        "nl": {"name": "QR Code Generator", "tagline": "Genereer QR codes voor elke tekst, URL, Wi-Fi of vCard. Custom size, kleuren en error correction. Export PNG of SVG.", "description": "Gratis online QR code generator. Custom size, foreground/background-kleuren, error correction levels. Download als PNG of SVG. Geen watermerken."},
        "tr": {"name": "QR Kod Üretici", "tagline": "Herhangi bir metin, URL, Wi-Fi veya vCard için QR kod üret. Özel boyut, renkler ve hata düzeltme. PNG veya SVG olarak dışa aktar.", "description": "Ücretsiz online QR kod üretici. Özel boyut, ön plan/arka plan renkleri, hata düzeltme seviyeleri. PNG veya SVG olarak indir. Filigran yok."},
        "id": {"name": "Generator Kode QR", "tagline": "Hasilkan kode QR untuk teks, URL, Wi-Fi, atau vCard apa pun. Ukuran custom, warna, dan koreksi error. Export sebagai PNG atau SVG.", "description": "Generator kode QR online gratis. Hasilkan kode QR untuk URL, teks, Wi-Fi, vCard, email, telepon, dan SMS. Ukuran, warna, level error correction yang dapat dikonfigurasi. Export PNG atau SVG. Berjalan offline di browser-mu."},
        "vi": {"name": "Tạo Mã QR", "tagline": "Tạo mã QR cho bất kỳ văn bản, URL, Wi-Fi hoặc vCard nào. Kích thước tùy chỉnh, màu và mức sửa lỗi. Xuất dưới dạng PNG hoặc SVG.", "description": "Trình tạo mã QR miễn phí trực tuyến. Encode văn bản, URL, thông tin đăng nhập Wi-Fi hoặc vCard thành mã QR có thể xuất dưới dạng PNG hoặc SVG với màu và mức sửa lỗi tùy chỉnh."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="qr-input" placeholder="https://example.com" oninput="qrRender()">https://toolhub.software</textarea>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>Size (px)</label>
      <input type="number" id="qr-size" value="320" min="64" max="1024" step="32" oninput="qrRender()">
    </div>
    <div>
      <label>Error correction</label>
      <select id="qr-ec" onchange="qrRender()">
        <option value="L">L — 7%</option>
        <option value="M" selected>M — 15%</option>
        <option value="Q">Q — 25%</option>
        <option value="H">H — 30%</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>Foreground</label>
      <input type="color" id="qr-fg" value="#000000" oninput="qrRender()" style="height:42px;padding:4px">
    </div>
    <div>
      <label>Background</label>
      <input type="color" id="qr-bg" value="#ffffff" oninput="qrRender()" style="height:42px;padding:4px">
    </div>
  </div>
  <div class="button-row">
    <button onclick="qrDownloadPng()">PNG</button>
    <button onclick="qrDownloadSvg()">SVG</button>
    <button class="secondary" onclick="qrPreset('wifi')">Wi-Fi preset</button>
    <button class="secondary" onclick="qrPreset('mailto')">Email preset</button>
    <button class="secondary" onclick="qrPreset('tel')">Phone preset</button>
  </div>
</div>
<div class="tool-card" style="text-align:center">
  <div id="qr-canvas" style="display:inline-block"></div>
  <div class="meta" id="qr-meta"></div>
</div>
""",
    "script": """
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"></script>
<script>
function qrRender(){
  const text = document.getElementById('qr-input').value || ' ';
  const size = parseInt(document.getElementById('qr-size').value, 10) || 320;
  const ec = document.getElementById('qr-ec').value;
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  const wrap = document.getElementById('qr-canvas');
  wrap.innerHTML = '<canvas></canvas>';
  const canvas = wrap.querySelector('canvas');
  QRCode.toCanvas(canvas, text, {
    width: size,
    errorCorrectionLevel: ec,
    color: { dark: fg, light: bg },
    margin: 2,
  }, function(err){
    if (err){ document.getElementById('qr-meta').textContent = 'Error: ' + err.message; return; }
    document.getElementById('qr-meta').textContent = size + '×' + size + 'px · EC ' + ec + ' · ' + text.length + ' chars';
  });
}
function qrDownloadPng(){
  const canvas = document.querySelector('#qr-canvas canvas');
  if (!canvas) return;
  const a = document.createElement('a');
  a.download = 'qrcode.png';
  a.href = canvas.toDataURL('image/png');
  a.click();
}
function qrDownloadSvg(){
  const text = document.getElementById('qr-input').value || ' ';
  const ec = document.getElementById('qr-ec').value;
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  QRCode.toString(text, { type: 'svg', errorCorrectionLevel: ec, color: { dark: fg, light: bg }, margin: 2 }, function(err, svg){
    if (err) return;
    const blob = new Blob([svg], {type: 'image/svg+xml'});
    const a = document.createElement('a');
    a.download = 'qrcode.svg';
    a.href = URL.createObjectURL(blob);
    a.click();
  });
}
function qrPreset(kind){
  const inp = document.getElementById('qr-input');
  if (kind === 'wifi') inp.value = 'WIFI:T:WPA;S:NetworkName;P:password;;';
  if (kind === 'mailto') inp.value = 'mailto:hello@example.com?subject=Hello';
  if (kind === 'tel') inp.value = 'tel:+421900000000';
  qrRender();
}
document.addEventListener('DOMContentLoaded', () => { setTimeout(qrRender, 100); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>QR codes are tiny URLs that a phone camera can read in a fraction of a second. Encode a URL, a Wi-Fi network, an email draft, a phone number, or any short text — print it on a poster, a business card, or a menu, and anyone with a phone can act on it without typing. This generator runs entirely in your browser using the open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a> library. Your input text never leaves the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Sharing a URL on a slide, a poster, a business card, or a packaging insert.</li>
  <li>Letting guests join your Wi-Fi without typing the password (use the Wi-Fi preset).</li>
  <li>Putting "scan to pay / book / order" on signage in physical spaces.</li>
  <li>Encoding a vCard for instant contact-card import on the receiver's phone.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Error correction trades off with density.</strong> Higher levels (Q, H) survive scratches and overlaid logos; lower levels (L, M) keep the code small and faster to scan. Use <strong>H</strong> if you plan to overlay a logo, otherwise <strong>M</strong> is the sane default.</li>
  <li><strong>Contrast matters.</strong> Stylised QR codes with low foreground/background contrast often look pretty but scan poorly under bad light. Test by scanning from the printed/screen output before shipping.</li>
  <li><strong>Long content forces a denser code.</strong> If you must encode a 200-character URL, the resulting code is dense and harder to scan from far away. Shorten via a redirect first if size matters.</li>
  <li><strong>SVG vs PNG.</strong> SVG scales without quality loss — best for print or large displays. PNG is universally accepted but pixelates if scaled up; export at the size you'll use.</li>
  <li><strong>Wi-Fi preset format.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — modern iOS/Android scan and join automatically; very old phones may not support it.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>QR codes são URLs minúsculos que a câmera de um celular consegue ler em uma fração de segundo. Codifique uma URL, uma rede Wi-Fi, um rascunho de e-mail, um número de telefone ou qualquer texto curto — imprima num pôster, num cartão de visita ou num cardápio, e qualquer pessoa com um celular pode agir sem digitar. Este gerador roda inteiramente no seu navegador usando a biblioteca open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>. Seu texto de entrada nunca sai da página.</p>

<h3>Quando usar</h3>
<ul>
  <li>Compartilhar uma URL num slide, num pôster, num cartão de visita ou num inserto de embalagem.</li>
  <li>Deixar convidados entrarem no seu Wi-Fi sem digitar a senha (use o preset Wi-Fi).</li>
  <li>Colocar "scan to pay / book / order" em sinalização em espaços físicos.</li>
  <li>Codificar um vCard para importação instantânea de cartão de contato no celular do receptor.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Correção de erro tem trade-off com densidade.</strong> Níveis mais altos (Q, H) sobrevivem a arranhões e logos sobrepostos; níveis mais baixos (L, M) deixam o código menor e mais rápido de escanear. Use <strong>H</strong> se planeja sobrepor um logo, caso contrário <strong>M</strong> é o default sensato.</li>
  <li><strong>Contraste importa.</strong> QR codes estilizados com pouco contraste entre foreground e background ficam bonitos mas escaneiam mal sob luz ruim. Teste escaneando do output impresso/da tela antes de publicar.</li>
  <li><strong>Conteúdo longo força um código mais denso.</strong> Se você precisa codificar uma URL de 200 caracteres, o código resultante é denso e mais difícil de escanear de longe. Encurte com um redirect antes se o tamanho importar.</li>
  <li><strong>SVG vs PNG.</strong> SVG escala sem perda de qualidade — melhor para impressão ou displays grandes. PNG é universalmente aceito mas pixela se aumentar de escala; exporte no tamanho que vai usar.</li>
  <li><strong>Formato do preset Wi-Fi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;senha&gt;;;</code> — iOS/Android modernos escaneiam e conectam automaticamente; celulares muito antigos podem não suportar.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Kody QR to maleńkie URL-e, które kamera telefonu czyta w ułamku sekundy. Zakoduj URL, sieć Wi-Fi, wersję roboczą maila, numer telefonu albo dowolny krótki tekst — wydrukuj na plakacie, wizytówce albo karcie menu i każdy z telefonem może coś z tym zrobić bez wpisywania. Ten generator działa w całości w przeglądarce, używając open-source'owej biblioteki <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>. Twój tekst nie opuszcza strony.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Udostępnianie URL-a na slajdzie, plakacie, wizytówce albo wkładce do opakowania.</li>
  <li>Łatwe dołączenie gości do twojego Wi-Fi bez wpisywania hasła (preset Wi-Fi).</li>
  <li>"Skanuj, żeby zapłacić / zarezerwować / zamówić" na oznakowaniu w przestrzeniach fizycznych.</li>
  <li>Kodowanie vCarda do natychmiastowego importu kontaktu na telefonie odbiorcy.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Korekcja błędów ma trade-off z gęstością.</strong> Wyższe poziomy (Q, H) przeżyją zarysowania i nałożone logo; niższe (L, M) trzymają kod mały i szybszy do skanowania. Używaj <strong>H</strong>, jeśli planujesz nakładać logo, w przeciwnym razie <strong>M</strong> to sensowny default.</li>
  <li><strong>Kontrast ma znaczenie.</strong> Stylizowane kody QR z niskim kontrastem foreground/background często ładnie wyglądają, ale słabo skanują w gorszym świetle. Przetestuj skanując z wydruku/ekranu, zanim ruszy.</li>
  <li><strong>Długa zawartość wymusza gęstszy kod.</strong> Jeśli musisz zakodować 200-znakowy URL, wynikowy kod jest gęsty i trudniej go zeskanować z daleka. Skróć przez redirect, jeśli rozmiar ma znaczenie.</li>
  <li><strong>SVG vs PNG.</strong> SVG skaluje się bez utraty jakości — najlepsze do druku albo dużych ekranów. PNG jest powszechnie akceptowany, ale piksel się rozbiega przy powiększaniu; eksportuj w docelowym rozmiarze.</li>
  <li><strong>Format presetu Wi-Fi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;hasło&gt;;;</code> — nowoczesne iOS/Android skanują i łączą się automatycznie; bardzo stare telefony mogą nie wspierać.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>QR コードはスマホのカメラが瞬時に読み取れる小さな URL です。URL、Wi-Fi 設定、メール下書き、電話番号、その他短いテキストをエンコードしてポスター、名刺、メニューに印刷すれば、誰もがタイピングなしで操作できます。本ジェネレーターはオープンソースの <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a> ライブラリを使い、すべてブラウザ内で動作します。入力テキストはページから外に出ません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>スライド、ポスター、名刺、パッケージ封入物に URL を載せたいとき。</li>
  <li>ゲストにパスワードをタイピングさせずに Wi-Fi へ接続させたいとき（Wi-Fi プリセットを利用）。</li>
  <li>店舗のサイネージに「スキャンして支払い／予約／注文」を貼り付けたいとき。</li>
  <li>vCard をエンコードして、相手のスマホに連絡先カードを即インポートさせたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>誤り訂正は密度とのトレードオフです。</strong> Q、H など高めにすると傷やロゴ重ねに強くなりますが、コードは大きく密になります。L、M は小さくなり読み取りも速いです。ロゴを重ねるなら <strong>H</strong>、それ以外は <strong>M</strong> が無難です。</li>
  <li><strong>コントラストが重要です。</strong> 凝ったカラーリングで前景／背景のコントラストを下げると、見た目はおしゃれでも暗所での読み取りが落ちます。出力後に印刷物や画面で必ずスキャン確認してください。</li>
  <li><strong>長いコンテンツは密なコードを生みます。</strong> 200 文字の URL を入れると密度が上がり、遠距離では読み取りにくくなります。サイズが重要ならリダイレクト URL に短縮してから入れてください。</li>
  <li><strong>SVG と PNG。</strong> SVG は無劣化でスケールでき、印刷や大画面に最適です。PNG はどこでも使えますが拡大すると荒くなります。実際に使うサイズで書き出してください。</li>
  <li><strong>Wi-Fi プリセットの形式。</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — 最近の iOS/Android はスキャンで自動接続できます。古い端末では未対応の場合があります。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>QR codes zijn kleine URLs die een telefooncamera in een fractie van een seconde kan lezen. Encode een URL, een Wi-Fi-netwerk, een email-concept, een telefoonnummer of elke korte tekst — print het op een poster, een visitekaartje of een menu, en iedereen met een telefoon kan ernaar handelen zonder te typen. Deze generator draait volledig in je browser via de open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>-library. Je input-tekst verlaat de pagina nooit.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een URL delen op een slide, een poster, een visitekaartje of een verpakkingsinleg.</li>
  <li>Gasten je Wi-Fi laten joinen zonder het wachtwoord te typen (gebruik de Wi-Fi-preset).</li>
  <li>"Scan om te betalen / boeken / bestellen" op signage in fysieke ruimtes zetten.</li>
  <li>Een vCard encoderen voor instant contactkaart-import op de telefoon van de ontvanger.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Error correction wisselt af tegen density.</strong> Hogere levels (Q, H) overleven krassen en overlaid logo's; lagere levels (L, M) houden de code klein en sneller te scannen. Gebruik <strong>H</strong> als je een logo wil overlay-en, anders is <strong>M</strong> de verstandige default.</li>
  <li><strong>Contrast doet ertoe.</strong> Gestileerde QR-codes met laag foreground/background-contrast zien er vaak mooi uit maar scannen slecht onder slecht licht. Test door te scannen vanaf de printed/screen output voor shipping.</li>
  <li><strong>Lange content forceert een dichtere code.</strong> Als je een 200-karakter URL moet encoderen, is de resulterende code dicht en moeilijker van ver te scannen. Verkort via een redirect eerst als size telt.</li>
  <li><strong>SVG vs PNG.</strong> SVG schaalt zonder kwaliteitsverlies — best voor print of grote displays. PNG is universeel geaccepteerd maar pixelt als opgeschaald; export op de size die je zult gebruiken.</li>
  <li><strong>Wi-Fi-preset-formaat.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — moderne iOS/Android scannen en joinen automatisch; heel oude telefoons ondersteunen het misschien niet.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>QR kodları bir telefon kamerasının saniyenin bir kısmında okuyabileceği küçük URL'lerdir. Bir URL, bir Wi-Fi ağı, bir e-posta taslağı, bir telefon numarası veya herhangi bir kısa metni kodla — bir poster, kartvizit veya menüye bas, ve telefonu olan herkes yazmadan eyleme geçebilir. Bu üretici tamamen tarayıcında açık kaynaklı <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a> kütüphanesini kullanır. Giriş metnin sayfayı asla terk etmez.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir slayt, poster, kartvizit veya ambalaj eki üzerinde URL paylaşma.</li>
  <li>Misafirlerin parola yazmadan Wi-Fi'ne katılmasına izin verme (Wi-Fi preset'ini kullan).</li>
  <li>Fiziksel alanlardaki tabelalara "ödemek / rezervasyon / sipariş için tara" koyma.</li>
  <li>Alıcının telefonunda anında kişi kartı içe aktarımı için bir vCard kodlama.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Hata düzeltme yoğunlukla değiş tokuş yapar.</strong> Daha yüksek seviyeler (Q, H) çiziklere ve üzerine yerleştirilmiş logolara dayanır; daha düşük seviyeler (L, M) kodu küçük ve tarama için daha hızlı tutar. Logo yerleştirmeyi planlıyorsan <strong>H</strong> kullan, aksi takdirde <strong>M</strong> makul varsayılandır.</li>
  <li><strong>Kontrast önemlidir.</strong> Düşük ön plan/arka plan kontrastlı stilize QR kodları sıklıkla güzel görünür ama kötü ışıkta kötü taranır. Göndermeden önce basılı/ekran çıktısından tarayarak test et.</li>
  <li><strong>Uzun içerik daha yoğun bir kod zorlar.</strong> 200 karakterlik bir URL kodlamak zorundaysan, sonuç kod yoğundur ve uzaktan taranması daha zordur. Boyut önemliyse önce bir yönlendirme ile kısalt.</li>
  <li><strong>SVG - PNG.</strong> SVG kalite kaybı olmadan ölçeklenir — baskı veya büyük ekranlar için en iyisi. PNG evrensel olarak kabul edilir ama ölçeklendirildiğinde pikselleşir; kullanacağın boyutta dışa aktar.</li>
  <li><strong>Wi-Fi preset biçimi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;parola&gt;;;</code> — modern iOS/Android tarar ve otomatik katılır; çok eski telefonlar desteklemeyebilir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>QR code adalah URL mungil yang bisa dibaca kamera ponsel dalam sepersekian detik. Encode URL, jaringan Wi-Fi, draft email, nomor telepon, atau teks pendek apa pun — cetak di poster, kartu nama, atau menu, dan siapa pun dengan ponsel bisa beraksi tanpa mengetik. Generator ini berjalan sepenuhnya di browser kamu menggunakan library open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>. Teks input kamu tidak pernah meninggalkan halaman.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Berbagi URL di slide, poster, kartu nama, atau sisipan kemasan.</li>
  <li>Membiarkan tamu bergabung Wi-Fi kamu tanpa mengetik password (gunakan preset Wi-Fi).</li>
  <li>Memasang "scan to pay / book / order" di papan tanda di ruang fisik.</li>
  <li>Meng-encode vCard untuk import kartu kontak instan di ponsel penerima.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Error correction trade-off dengan density.</strong> Level lebih tinggi (Q, H) bertahan terhadap goresan dan logo yang ditumpuk; level lebih rendah (L, M) menjaga code tetap kecil dan lebih cepat di-scan. Gunakan <strong>H</strong> jika kamu berencana menumpuk logo, jika tidak <strong>M</strong> adalah default yang waras.</li>
  <li><strong>Kontras itu penting.</strong> QR code yang distilisasi dengan kontras foreground/background rendah sering terlihat cantik tapi sulit di-scan di cahaya buruk. Test dengan men-scan dari output cetakan/layar sebelum ship.</li>
  <li><strong>Konten panjang memaksa code lebih padat.</strong> Jika kamu harus encode URL 200 karakter, hasilnya padat dan lebih sulit di-scan dari jauh. Persingkat lewat redirect dulu jika ukuran penting.</li>
  <li><strong>SVG vs PNG.</strong> SVG scale tanpa kehilangan kualitas — terbaik untuk cetak atau display besar. PNG diterima universal tapi piksel jika di-scale ke atas; export di ukuran yang akan kamu pakai.</li>
  <li><strong>Format preset Wi-Fi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — iOS/Android modern men-scan dan join otomatis; ponsel sangat lama mungkin tidak mendukung.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>QR code mã hóa văn bản dưới dạng pattern đen-trắng có thể đọc bằng camera. Hữu ích cho mọi thứ từ URL ngắn đến vCard chứa thông tin liên hệ đến mật khẩu Wi-Fi mà khách có thể quét. Tool này tạo QR code cho văn bản, URL, Wi-Fi, hoặc vCard với màu và mức sửa lỗi tùy chỉnh; xuất dưới dạng PNG hoặc SVG.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Treo poster với URL đến trang đăng ký event.</li>
  <li>Chia sẻ mật khẩu Wi-Fi với khách mà không cần đọc to.</li>
  <li>In vCard QR code trên business card.</li>
  <li>Test login token một-lần qua QR code.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Mức sửa lỗi tăng kích thước.</strong> Cao hơn = QR phục hồi từ damage tốt hơn nhưng dày hơn. L (7%) cho điều kiện in tốt, H (30%) khi nó có thể được phủ logo.</li>
  <li><strong>Tương phản quan trọng.</strong> Đen trên trắng là an toàn nhất. Color reverse (trắng trên đen) thường ổn nhưng kiểm tra với phone.</li>
  <li><strong>Test trên phone trước khi in.</strong> Một số scanner cũ kén chọn — kiểm tra QR với app camera tiêu chuẩn iOS và Android trước khi đặt hàng 10.000 bản in.</li>
</ul>
""",
    },
    "related": ["url-encoder", "image-to-base64", "youtube-thumbnail"],
    "howto": {"flow": "generate",  "action": "generate","noun": "QR code"},
}
