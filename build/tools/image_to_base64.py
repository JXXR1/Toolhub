TOOL = {
    "slug": "image-to-base64",
    "category": "encoding",
    "icon": "🖼️",
    "tags": ["image", "base64", "data-uri", "convert", "embed"],
    "i18n": {
        "en": {
            "name": "Image to Base64",
            "tagline": "Convert any image to a Base64 data URI ready for inline use in HTML, CSS, or Markdown. Files stay in your browser.",
            "description": "Free online image to Base64 data URI encoder. Drop or pick an image and get a ready-to-paste data: URL for inline HTML, CSS background-image, or email.",
        },
        "de": {"name": "Bild zu Base64", "tagline": "Bilder in Base64-Data-URIs umwandeln, fertig zum Einfügen in HTML, CSS oder Markdown. Datei bleibt im Browser.", "description": "Kostenloser Bild-zu-Base64-Data-URI-Encoder. Bild auswählen und einsatzbereite data:-URL erhalten."},
        "es": {"name": "Imagen a Base64", "tagline": "Convierte cualquier imagen en un data URI Base64 para HTML, CSS o Markdown. El archivo nunca sale de tu navegador.", "description": "Codificador gratuito de imágenes a data URI Base64. Selecciona una imagen y obtén la URL data: lista para pegar."},
        "fr": {"name": "Image vers Base64", "tagline": "Convertissez n'importe quelle image en data URI Base64 pour HTML, CSS ou Markdown. Le fichier ne quitte pas votre navigateur.", "description": "Encodeur gratuit d'image en data URI Base64. Sélectionnez une image et obtenez l'URL data: prête à coller."},
        "it": {"name": "Immagine a Base64", "tagline": "Converti qualsiasi immagine in un data URI Base64 per HTML, CSS o Markdown. Il file non lascia il browser.", "description": "Encoder gratuito di immagini in data URI Base64. Seleziona un'immagine e ottieni l'URL data: pronta da incollare."},
        "pt": {"name": "Imagem para Base64", "tagline": "Converte qualquer imagem em um data URI Base64 pronto pra uso inline em HTML, CSS ou Markdown. O arquivo fica no seu browser.", "description": "Encoder grátis online de imagem para data URI Base64. Solte ou escolha uma imagem e receba uma URL data: pronta pra colar em HTML inline, background-image de CSS ou e-mail."},
        "pl": {"name": "Obrazek do Base64", "tagline": "Konwertuj dowolny obrazek na data URI Base64 gotowy do inline'owego użycia w HTML, CSS albo Markdown. Pliki zostają w przeglądarce.", "description": "Darmowy online encoder obrazków do data URI Base64. Upuść albo wybierz obrazek i dostań gotowy do wklejenia data: URL do inline HTML, CSS background-image albo maila."},
        "ja": {"name": "画像から Base64 へ", "tagline": "任意の画像を Base64 データ URI に変換し、HTML・CSS・Markdown へインライン挿入。ファイルはブラウザ内のみ。", "description": "オンライン無料の画像 → Base64 データ URI エンコーダー。画像をドロップまたは選択すると、HTML インライン・CSS の background-image・メール用に貼り付け可能な data: URL を得られます。"},
        "nl": {"name": "Afbeelding naar Base64", "tagline": "Converteer elke afbeelding naar een Base64-data-URI klaar voor inline gebruik in HTML, CSS of Markdown. Bestanden blijven in je browser.", "description": "Gratis online afbeelding-naar-Base64-data-URI encoder. Drop of kies een afbeelding en krijg een ready-to-paste data: URL voor inline HTML, CSS background-image of email."},
        "tr": {"name": "Görsel'den Base64'e", "tagline": "Herhangi bir görseli HTML, CSS veya Markdown'da inline kullanım için Base64 data URI'a dönüştür. Dosyalar tarayıcında kalır.", "description": "Ücretsiz online görselden Base64 data URI encoder. Bir görseli bırak veya seç, inline HTML, CSS background-image veya e-posta için yapıştırılmaya hazır data: URL al."},
        "id": {"name": "Gambar ke Base64", "tagline": "Konversi gambar apa pun ke Base64 data URI untuk penggunaan inline di HTML, CSS, atau Markdown. File tetap di browser-mu.", "description": "Konverter gambar ke Base64 gratis. Drop gambar apa pun dan dapatkan Base64 data URI siap pakai untuk disematkan di HTML, CSS, atau Markdown. File tetap di browser-mu — tanpa upload, tanpa pelacakan."},
        "vi": {"name": "Ảnh sang Base64", "tagline": "Chuyển bất kỳ ảnh nào thành Base64 data URI để dùng inline trong HTML, CSS hoặc Markdown. File ở lại trong trình duyệt của bạn.", "description": "Bộ chuyển ảnh sang Base64 miễn phí trực tuyến. Thả bất kỳ file ảnh nào và nhận data URI sẵn-dùng cho CSS, HTML hoặc Markdown. File không bao giờ rời khỏi trình duyệt của bạn."},
    },
    "body": """
<div class="tool-card">
  <label>Pick or drop an image</label>
  <input type="file" id="i2b-file" accept="image/*" oninput="i2bRun()" style="padding:0.5rem;background:var(--code-bg);border:1px dashed var(--border);border-radius:6px">
  <div class="meta" id="i2b-meta"></div>
</div>
<div class="tool-card">
  <label>Preview</label>
  <div id="i2b-prev" style="text-align:center;padding:1rem;background:var(--code-bg);border:1px solid var(--border);border-radius:6px;min-height:60px"><span style="color:var(--text-muted)">No image yet.</span></div>
</div>
<div class="tool-card">
  <label>Data URI</label>
  <div class="output-row">
    <pre class="output" id="i2b-out" style="max-height:240px;overflow:auto;font-size:0.78rem">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('i2b-out', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>Snippets</label>
  <div class="output-row"><pre class="output" id="i2b-html" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-html', this)">{LBL_COPY}</button></div>
  <div class="output-row" style="margin-top:0.5rem"><pre class="output" id="i2b-css" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-css', this)">{LBL_COPY}</button></div>
  <div class="output-row" style="margin-top:0.5rem"><pre class="output" id="i2b-md" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-md', this)">{LBL_COPY}</button></div>
</div>
""",
    "script": """
<script>
function i2bRun(){
  const f = document.getElementById('i2b-file').files[0];
  const out = document.getElementById('i2b-out');
  const meta = document.getElementById('i2b-meta');
  const prev = document.getElementById('i2b-prev');
  if (!f){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent=''; prev.innerHTML='<span style="color:var(--text-muted)">No image yet.</span>'; document.getElementById('i2b-html').textContent=''; document.getElementById('i2b-css').textContent=''; document.getElementById('i2b-md').textContent=''; return; }
  if (f.size > 5 * 1024 * 1024){ out.classList.add('error'); out.textContent = '✗ File larger than 5 MB. Inline data URIs that big are usually a bad idea — use a real image URL.'; return; }
  out.classList.remove('error');
  const r = new FileReader();
  r.onload = () => {
    const uri = r.result;
    out.textContent = uri;
    meta.textContent = f.name + ' · ' + f.type + ' · ' + (f.size/1024).toFixed(1) + ' KB → ' + (uri.length/1024).toFixed(1) + ' KB encoded';
    prev.innerHTML = '<img src="' + uri + '" style="max-width:100%;max-height:280px;border-radius:6px">';
    document.getElementById('i2b-html').textContent = '<img src="' + uri.slice(0, 60) + '…" alt="">';
    document.getElementById('i2b-css').textContent = 'background-image: url("' + uri.slice(0, 60) + '…");';
    document.getElementById('i2b-md').textContent = '![alt](' + uri.slice(0, 60) + '…)';
  };
  r.readAsDataURL(f);
}
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A <em>data URI</em> embeds the bytes of a file directly into a URL using Base64 — no separate request, no external file. This converter reads any image you drop on it and produces a <code>data:image/...;base64,...</code> string ready to paste into HTML, CSS, Markdown, or JSON. The file never leaves your browser; conversion happens via <code>FileReader.readAsDataURL</code>.</p>

<h3>When to use it</h3>
<ul>
  <li>Tiny icons (&lt; 4 KB) inline in CSS — saves an HTTP request and avoids a flash on first paint.</li>
  <li>Self-contained HTML emails, single-file demos, or offline-capable PWAs.</li>
  <li>Quick pastes into Markdown notes, Notion pages, or chat threads that need to travel with the image.</li>
  <li>Test fixtures and snapshot files where you want the asset committed alongside the test.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Size penalty.</strong> Base64 inflates payload by ~33%. Above ~4–8 KB the embedding cost outweighs the saved request, especially since data URIs cannot be cached separately by the browser.</li>
  <li><strong>No de-duplication across pages.</strong> Each page that embeds the URI ships the bytes again. For anything reused, keep it as a real URL so the browser caches it once.</li>
  <li><strong>Email clients vary.</strong> Most modern clients render data URIs, but Outlook on Windows historically blocks them in <code>&lt;img src&gt;</code>. CID attachments are still safer for mass email.</li>
  <li><strong>SVG ≠ raster.</strong> For SVG, embedding the markup directly (or url-encoding the SVG) is usually smaller than Base64.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um <em>data URI</em> embute os bytes de um arquivo direto numa URL usando Base64 — sem request separada, sem arquivo externo. Este conversor lê qualquer imagem que você soltar e gera uma string <code>data:image/...;base64,...</code> pronta pra colar em HTML, CSS, Markdown ou JSON. O arquivo nunca sai do seu browser; a conversão acontece via <code>FileReader.readAsDataURL</code>.</p>

<h3>Quando usar</h3>
<ul>
  <li>Ícones pequenos (&lt; 4 KB) inline em CSS — economiza uma request HTTP e evita um flash no primeiro paint.</li>
  <li>E-mails HTML autocontidos, demos em arquivo único ou PWAs offline-capable.</li>
  <li>Colagens rápidas em notas Markdown, páginas do Notion ou threads de chat que precisam viajar com a imagem.</li>
  <li>Fixtures de teste e arquivos de snapshot em que você quer o asset commitado junto com o teste.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Penalidade de tamanho.</strong> Base64 infla o payload em uns 33%. Acima de 4–8 KB, o custo de embutir supera a request economizada, especialmente porque data URIs não podem ser cacheados separadamente pelo browser.</li>
  <li><strong>Sem deduplicação entre páginas.</strong> Cada página que embute o URI envia os bytes de novo. Pra qualquer coisa reutilizada, mantenha como URL real pra que o browser cacheie uma vez.</li>
  <li><strong>Clientes de e-mail variam.</strong> Os clientes modernos renderizam data URIs, mas o Outlook no Windows historicamente bloqueia em <code>&lt;img src&gt;</code>. Anexos CID ainda são mais seguros pra envio em massa.</li>
  <li><strong>SVG ≠ raster.</strong> Pra SVG, embutir o markup direto (ou fazer url-encoding do SVG) costuma ficar menor que Base64.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p><em>Data URI</em> osadza bajty pliku bezpośrednio w URL-u używając Base64 — bez osobnego requesta, bez zewnętrznego pliku. Ten konwerter czyta dowolny obrazek, który upuścisz, i produkuje string <code>data:image/...;base64,...</code> gotowy do wklejenia w HTML, CSS, Markdown albo JSON. Plik nigdy nie opuszcza przeglądarki; konwersja idzie przez <code>FileReader.readAsDataURL</code>.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Maleńkie ikonki (&lt; 4 KB) inline w CSS — oszczędza request HTTP i unika flasha przy pierwszym paint.</li>
  <li>Samowystarczalne maile HTML, demo w jednym pliku albo PWA działające offline.</li>
  <li>Szybkie wklejki do notatek Markdown, stron Notion albo wątków na czacie, które muszą podróżować razem z obrazkiem.</li>
  <li>Fixture'y testowe i pliki snapshotów, gdzie chcesz, żeby asset był zacommitowany razem z testem.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Kara za rozmiar.</strong> Base64 nadyma payload o ~33%. Powyżej ~4–8 KB koszt osadzenia przewyższa zaoszczędzony request, zwłaszcza że data URI nie mogą być cache'owane osobno przez przeglądarkę.</li>
  <li><strong>Brak deduplikacji między stronami.</strong> Każda strona, która osadza URI, wysyła bajty od nowa. Dla czegokolwiek powtarzalnego trzymaj prawdziwy URL, żeby przeglądarka zacache'owała raz.</li>
  <li><strong>Klienty mailowe się różnią.</strong> Nowoczesne renderują data URI, ale Outlook na Windowsie historycznie blokuje je w <code>&lt;img src&gt;</code>. Załączniki CID nadal są bezpieczniejsze do mailingów masowych.</li>
  <li><strong>SVG ≠ raster.</strong> Dla SVG osadzenie markupu bezpośrednio (albo url-encoding SVG) jest zwykle mniejsze niż Base64.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p><em>Data URI</em> は Base64 を使ってファイルのバイト列を URL に直接埋め込む仕組みで、別リクエストや外部ファイルを使わずに済みます。本コンバーターはドロップした画像を読み込み、HTML、CSS、Markdown、JSON に貼り付けられる <code>data:image/...;base64,...</code> 文字列を生成します。ファイルはブラウザから外に出ず、変換は <code>FileReader.readAsDataURL</code> で行います。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>CSS にインライン化する小さなアイコン（4 KB 未満）。HTTP リクエストを節約し、初回ペイント時のフラッシュを避けられます。</li>
  <li>自己完結型の HTML メール、シングルファイルのデモ、オフライン対応の PWA。</li>
  <li>Markdown ノート、Notion ページ、画像と一緒に流通させたいチャットスレッドへの貼り付け。</li>
  <li>テストフィクスチャやスナップショットファイルで、アセットをテストと一緒にコミットしたい場合。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>サイズが膨らみます。</strong> Base64 はおよそ 33% ペイロードが増えます。4〜8 KB を超えると、リクエスト節約の利点を埋め込みコストが上回ります。data URI はブラウザに別個にキャッシュされない点も影響します。</li>
  <li><strong>ページ間で重複排除されません。</strong> URI を埋め込むページごとにバイト列が再送されます。再利用するアセットは実 URL のままにし、ブラウザに 1 度だけキャッシュさせてください。</li>
  <li><strong>メールクライアントの対応はまちまちです。</strong> 多くのモダンクライアントは data URI を表示しますが、Windows 版 Outlook は歴史的に <code>&lt;img src&gt;</code> でブロックしてきました。大量配信は CID 添付の方が安全です。</li>
  <li><strong>SVG はラスタとは別です。</strong> SVG はマークアップ直挿し（または URL エンコード）の方が Base64 より小さくなることが多いです。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een <em>data URI</em> embedt de bytes van een bestand direct in een URL met Base64 — geen apart request, geen extern bestand. Deze converter leest elke afbeelding die je erop drop't en produceert een <code>data:image/...;base64,...</code>-string klaar om in HTML, CSS, Markdown of JSON te plakken. Het bestand verlaat je browser nooit; conversie gebeurt via <code>FileReader.readAsDataURL</code>.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Kleine icons (&lt; 4 KB) inline in CSS — bespaart een HTTP-request en voorkomt een flash bij first paint.</li>
  <li>Zelfstandige HTML-emails, single-file demos of offline-capable PWA's.</li>
  <li>Snelle pastes in Markdown-notities, Notion-pagina's of chat-threads die met de afbeelding moeten reizen.</li>
  <li>Test fixtures en snapshot-bestanden waar je het asset committed wil hebben naast de test.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Size penalty.</strong> Base64 blaast payload op met ~33%. Boven ~4–8 KB weegt de embedding-cost zwaarder dan het bespaarde request, zeker omdat data URIs niet apart door de browser gecached kunnen worden.</li>
  <li><strong>Geen de-duplicatie over pagina's heen.</strong> Elke pagina die de URI embedt stuurt de bytes opnieuw mee. Voor alles dat hergebruikt wordt, houd het als echte URL zodat de browser het één keer cached.</li>
  <li><strong>Email-clients verschillen.</strong> De meeste moderne clients renderen data URIs, maar Outlook op Windows blokkeerde ze historisch in <code>&lt;img src&gt;</code>. CID-attachments zijn nog steeds veiliger voor mass email.</li>
  <li><strong>SVG ≠ raster.</strong> Voor SVG is de markup direct embedden (of de SVG url-encoderen) meestal kleiner dan Base64.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir <em>data URI</em> bir dosyanın byte'larını doğrudan bir URL'ye Base64 kullanarak gömer — ayrı istek yok, harici dosya yok. Bu dönüştürücü üzerine bıraktığın herhangi bir görseli okur ve HTML, CSS, Markdown veya JSON'a yapıştırmaya hazır bir <code>data:image/...;base64,...</code> string'i üretir. Dosya tarayıcını asla terk etmez; dönüşüm <code>FileReader.readAsDataURL</code> üzerinden olur.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>CSS'te küçük ikonlar (&lt; 4 KB) inline — bir HTTP isteğinden tasarruf eder ve ilk paint'te flash'tan kaçınır.</li>
  <li>Kendi kendine yeten HTML e-postalar, tek dosyalı demolar veya çevrimdışı yetenekli PWA'lar.</li>
  <li>Görselle birlikte gitmesi gereken Markdown notlarına, Notion sayfalarına veya sohbet thread'lerine hızlı yapıştırmalar.</li>
  <li>Test fixture'ları ve snapshot dosyaları — varlığı testle birlikte commit etmek istediğinde.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Boyut cezası.</strong> Base64 yükü ~%33 şişirir. ~4–8 KB üzerinde, gömme maliyeti tasarruf edilen isteği geçer, özellikle data URI'lar tarayıcı tarafından ayrı önbelleğe alınamadığı için.</li>
  <li><strong>Sayfalar arası deduplikasyon yok.</strong> URI'yi gömen her sayfa byte'ları yeniden gönderir. Yeniden kullanılan herhangi bir şey için tarayıcı bir kez önbelleğe alsın diye gerçek URL olarak tut.</li>
  <li><strong>E-posta istemcileri değişir.</strong> Çoğu modern istemci data URI'ları render eder, ancak Windows'ta Outlook tarihsel olarak bunları <code>&lt;img src&gt;</code> içinde engeller. CID ekleri toplu e-posta için hâlâ daha güvenlidir.</li>
  <li><strong>SVG ≠ raster.</strong> SVG için, markup'ı doğrudan gömme (veya SVG'yi url-encode etme) genellikle Base64'ten daha küçüktür.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Sebuah <em>data URI</em> menyematkan byte file langsung ke dalam URL menggunakan Base64 — tanpa request terpisah, tanpa file eksternal. Converter ini membaca image apa pun yang kamu drop dan menghasilkan string <code>data:image/...;base64,...</code> yang siap di-paste ke HTML, CSS, Markdown, atau JSON. File tidak pernah meninggalkan browser kamu; konversi terjadi via <code>FileReader.readAsDataURL</code>.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Icon kecil (&lt; 4 KB) inline di CSS — menghemat satu request HTTP dan menghindari flash di first paint.</li>
  <li>Email HTML mandiri, demo satu-file, atau PWA yang offline-capable.</li>
  <li>Paste cepat ke catatan Markdown, halaman Notion, atau thread chat yang harus ikut bersama gambarnya.</li>
  <li>Test fixture dan file snapshot ketika kamu ingin aset itu di-commit bersama test-nya.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Penalti ukuran.</strong> Base64 membengkakkan payload sekitar ~33%. Di atas ~4–8 KB, biaya embedding melebihi penghematan request, terutama karena data URI tidak bisa di-cache terpisah oleh browser.</li>
  <li><strong>Tidak ada deduplikasi antar halaman.</strong> Setiap halaman yang menyematkan URI itu mengirim byte-nya lagi. Untuk apa pun yang dipakai ulang, simpan sebagai URL asli supaya browser meng-cache-nya sekali.</li>
  <li><strong>Email client berbeda-beda.</strong> Kebanyakan client modern me-render data URI, tapi Outlook di Windows secara historis memblokirnya di <code>&lt;img src&gt;</code>. CID attachment masih lebih aman untuk mass email.</li>
  <li><strong>SVG ≠ raster.</strong> Untuk SVG, menyematkan markup langsung (atau url-encode SVG-nya) biasanya lebih kecil dibanding Base64.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Một data URI nhúng dữ liệu nhị phân trực tiếp vào CSS, HTML hoặc Markdown dưới dạng chuỗi base64. <code>background-image: url('data:image/png;base64,iVBORw...')</code> tải ảnh mà không cần fetch HTTP riêng. Hữu ích cho icon nhỏ trong CSS, ảnh inline trong email, hoặc ảnh thumbnail trong PDF được tạo. Tool này chuyển bất kỳ file ảnh nào thành một data URI sẵn sàng để paste.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Inline một icon nhỏ vào CSS để giảm số request HTTP.</li>
  <li>Nhúng một ảnh vào email HTML (mặc dù nhiều client email không bật cái này theo mặc định).</li>
  <li>Thử nhanh ảnh trong một CodeSandbox mà không upload nó.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Base64 thêm khoảng 33% kích thước.</strong> Một ảnh 10 KB trở thành ~13.4 KB chuỗi. Đối với ảnh nhỏ (&lt; 1 KB), tiết kiệm fetch worth it; đối với ảnh lớn hơn, dùng URL riêng và để trình duyệt cache.</li>
  <li><strong>Hỗ trợ email client thay đổi.</strong> Một số client (Outlook 2007–2013) không hỗ trợ data URI inline.</li>
  <li><strong>Đừng quá lớn.</strong> Một số trình duyệt và database có giới hạn về kích thước chuỗi data URI.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "qr-code-generator", "url-encoder"],
    "howto": {"flow": "transform", "action": "encode",  "noun": "image"},
}
