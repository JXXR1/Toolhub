TOOL = {
    "slug": "hash-generator",
    "category": "security",
    "icon": "🔑",
    "tags": ["hash", "md5", "sha", "sha-256", "sha-512", "checksum"],
    "i18n": {
        "en": {
            "name": "Hash Generator",
            "tagline": "Hash text with SHA-1, SHA-256, SHA-384 or SHA-512 using your browser's WebCrypto. Computed locally — input never leaves the page.",
            "description": "Free online hash generator. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Hex output, copy-friendly. Runs entirely in your browser.",
        },
        "de": {"name": "Hash-Generator", "tagline": "Text mit SHA-1, SHA-256, SHA-384 oder SHA-512 hashen via WebCrypto. Lokal berechnet — Eingabe verlässt die Seite nicht.", "description": "Kostenloser Hash-Generator. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Hex-Ausgabe, läuft komplett im Browser."},
        "es": {"name": "Generador de Hash", "tagline": "Genera hashes SHA-1, SHA-256, SHA-384 o SHA-512 con WebCrypto del navegador. Calculado localmente — la entrada no se envía.", "description": "Generador de hash gratuito. SHA-1, SHA-256, SHA-384, SHA-512 vía WebCrypto. Salida en hexadecimal, todo en tu navegador."},
        "fr": {"name": "Générateur de Hash", "tagline": "Hachez du texte avec SHA-1, SHA-256, SHA-384 ou SHA-512 via WebCrypto. Calcul local — l'entrée ne quitte pas la page.", "description": "Générateur de hash gratuit. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Sortie hex, tout dans votre navigateur."},
        "it": {"name": "Generatore di Hash", "tagline": "Genera hash SHA-1, SHA-256, SHA-384 o SHA-512 con WebCrypto. Calcolato localmente — l'input non lascia la pagina.", "description": "Generatore di hash gratuito. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Output esadecimale, tutto nel browser."},
        "pt": {"name": "Gerador de Hash", "tagline": "Gere hash de texto com SHA-1, SHA-256, SHA-384 ou SHA-512 usando WebCrypto do browser. Calculado localmente — o input nunca sai da página.", "description": "Gerador de hash online gratuito. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Saída em hex, fácil de copiar. Roda inteiramente no seu browser."},
        "pl": {"name": "Generator Hashy", "tagline": "Hashuj tekst za pomocą SHA-1, SHA-256, SHA-384 lub SHA-512 używając WebCrypto przeglądarki. Liczone lokalnie — input nigdy nie opuszcza strony.", "description": "Darmowy online generator hashy. SHA-1, SHA-256, SHA-384, SHA-512 przez WebCrypto. Wyjście hex, łatwe do skopiowania. Działa w całości w przeglądarce."},
        "ja": {"name": "ハッシュ生成ツール", "tagline": "ブラウザの WebCrypto で SHA-1、SHA-256、SHA-384、SHA-512 のハッシュを生成。ローカル計算で、入力はページから外に出ません。", "description": "オンライン無料のハッシュ生成ツール。WebCrypto を用いて SHA-1、SHA-256、SHA-384、SHA-512 を計算します。hex 出力でコピーしやすく、すべてブラウザ内で動作します。"},
        "nl": {"name": "Hash Generator", "tagline": "Hash tekst met SHA-1, SHA-256, SHA-384 of SHA-512 via WebCrypto in je browser. Lokaal berekend — input verlaat de pagina nooit.", "description": "Gratis online hash generator. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Hex output, copy-friendly. Draait volledig in je browser."},
        "tr": {"name": "Hash Üretici", "tagline": "Metni tarayıcının WebCrypto'su ile SHA-1, SHA-256, SHA-384 veya SHA-512 hash'le. Yerel hesaplanır — giriş sayfayı asla terk etmez.", "description": "Ücretsiz online hash üretici. WebCrypto üzerinden SHA-1, SHA-256, SHA-384, SHA-512. Hex çıktı, kopyalanabilir. Tamamen tarayıcında çalışır."},
        "id": {"name": "Hash Generator", "tagline": "Hash teks dengan SHA-1, SHA-256, SHA-384, atau SHA-512 menggunakan WebCrypto browser. Dihitung lokal — input tidak pernah meninggalkan halaman.", "description": "Hash generator gratis. Hitung digest SHA-1, SHA-256, SHA-384, dan SHA-512 untuk teks atau file apa pun menggunakan WebCrypto browser. Semuanya berjalan lokal — input tidak pernah meninggalkan perangkatmu."},
        "vi": {"name": "Tạo Hash", "tagline": "Hash văn bản với SHA-1, SHA-256, SHA-384 hoặc SHA-512 bằng WebCrypto của trình duyệt. Tính cục bộ — đầu vào không bao giờ rời khỏi trang.", "description": "Trình tạo hash miễn phí trực tuyến hỗ trợ SHA-1, SHA-256, SHA-384 và SHA-512. Sử dụng API WebCrypto của trình duyệt — đầu vào của bạn không bao giờ rời khỏi thiết bị."},
        "hi": {"name": "Hash Generator", "tagline": "अपने browser के WebCrypto का उपयोग करके text को SHA-1, SHA-256, SHA-384 या SHA-512 से hash करें। Locally compute होता है — input page से बाहर नहीं जाता।", "description": "मुफ़्त ऑनलाइन hash generator। WebCrypto के माध्यम से SHA-1, SHA-256, SHA-384, SHA-512। Hex output, copy-friendly। पूरी तरह से आपके browser में चलता है।"},
        "sk": {"name": 'Hash generátor', "tagline": 'Zhashuj text pomocou SHA-1, SHA-256, SHA-384 alebo SHA-512 cez WebCrypto v prehliadači. Počíta sa lokálne — vstup nikdy neopustí stránku.', "description": 'Bezplatný online hash generátor. Vytvor SHA-1, SHA-256, SHA-384 alebo SHA-512 hash z textu pomocou WebCrypto API. Všetko beží lokálne v prehliadači — vstup nikdy nikam neodíde.'},
        "cs": {"name": 'Hash generátor', "tagline": 'Zahashuj text pomocí SHA-1, SHA-256, SHA-384 nebo SHA-512 přes WebCrypto v prohlížeči. Počítá se lokálně — vstup nikdy neopustí stránku.', "description": 'Zdarma online hash generátor. Vytvoř SHA-1, SHA-256, SHA-384 nebo SHA-512 hash z textu pomocí WebCrypto API. Vše běží lokálně v prohlížeči — vstup nikdy nikam neodejde.'},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="h-in" oninput="hRun()" placeholder="Hello, world!" spellcheck="false"></textarea>
  <div class="meta">Note: MD5 is not provided here — it is broken for security purposes. Use SHA-256 or higher for new applications.</div>
</div>
<div class="tool-card">
  <label>SHA-1 <span class="badge">160 bits</span> <span class="meta">— legacy, do not use for security</span></label>
  <div class="output-row"><code class="output" id="h-sha1">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha1', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-256 <span class="badge">256 bits</span> <span class="meta">— recommended default</span></label>
  <div class="output-row"><code class="output" id="h-sha256">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha256', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-384 <span class="badge">384 bits</span></label>
  <div class="output-row"><code class="output" id="h-sha384">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha384', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-512 <span class="badge">512 bits</span></label>
  <div class="output-row"><code class="output" id="h-sha512">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha512', this)">{LBL_COPY}</button></div>
</div>
""",
    "script": """
<script>
async function hOne(name, bytes){
  const buf = await crypto.subtle.digest(name, bytes);
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2,'0')).join('');
}
async function hRun(){
  const raw = document.getElementById('h-in').value;
  const ids = ['h-sha1','h-sha256','h-sha384','h-sha512'];
  if (!raw){ ids.forEach(id => document.getElementById(id).textContent = '{LBL_NO_INPUT}'); return; }
  const bytes = new TextEncoder().encode(raw);
  const [s1, s256, s384, s512] = await Promise.all([
    hOne('SHA-1', bytes), hOne('SHA-256', bytes), hOne('SHA-384', bytes), hOne('SHA-512', bytes)
  ]);
  document.getElementById('h-sha1').textContent = s1;
  document.getElementById('h-sha256').textContent = s256;
  document.getElementById('h-sha384').textContent = s384;
  document.getElementById('h-sha512').textContent = s512;
}
document.addEventListener('DOMContentLoaded', hRun);
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('h-in');
  if (!input) return;
  input.value = e.detail.data;
  hRun();
});
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A cryptographic hash takes any input and produces a fixed-length fingerprint. Two identical inputs always hash to the same digest; changing a single bit changes the digest entirely. Hashes underpin file-integrity checks, content-addressable storage, digital signatures, and password-hashing pipelines (where they're combined with a slow function like Argon2 or bcrypt).</p>
<p>All hashing here uses the browser's <code>crypto.subtle.digest</code> — the same primitives that power TLS. Your input never leaves the page.</p>

<h3>When to use which</h3>
<ul>
  <li><strong>SHA-256</strong> — sensible default for integrity checks, content addressing (Git, IPFS-style), HMAC keys, and signatures.</li>
  <li><strong>SHA-384 / SHA-512</strong> — useful when you need a wider digest (PBKDF2/HKDF tuning, larger HMAC keys, post-quantum-margin habits).</li>
  <li><strong>SHA-1</strong> — for compatibility only (Git object IDs, legacy CI checksums). Don't use for security boundaries — practical collision attacks have existed since 2017.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Hashing is not encryption.</strong> Hashes are one-way; you can't get the original back. If you need confidentiality, encrypt.</li>
  <li><strong>Don't hash passwords with raw SHA-256.</strong> Plain SHA is fast — that helps attackers brute-force. Use a slow KDF (Argon2id, bcrypt, scrypt) for password storage.</li>
  <li><strong>MD5 is intentionally absent.</strong> Broken since the early 2000s. Anywhere you "need" MD5, you also need to flag a security review.</li>
  <li><strong>Whitespace matters.</strong> A trailing newline produces a different hash than the same text without one. Compare hex output exactly.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um hash criptográfico pega qualquer entrada e produz uma impressão digital de tamanho fixo. Duas entradas idênticas sempre geram o mesmo digest; mudar um único bit muda o digest inteiro. Hashes sustentam checagens de integridade de arquivo, armazenamento content-addressable, assinaturas digitais e pipelines de hashing de senha (onde são combinados com uma função lenta como Argon2 ou bcrypt).</p>
<p>Todo o hashing aqui usa o <code>crypto.subtle.digest</code> do browser — as mesmas primitivas que sustentam o TLS. Seu input nunca sai da página.</p>

<h3>Quando usar qual</h3>
<ul>
  <li><strong>SHA-256</strong> — escolha sensata como padrão para checagens de integridade, content addressing (Git, estilo IPFS), chaves HMAC e assinaturas.</li>
  <li><strong>SHA-384 / SHA-512</strong> — útil quando você precisa de um digest mais largo (tuning de PBKDF2/HKDF, chaves HMAC maiores, hábitos de margem pós-quântica).</li>
  <li><strong>SHA-1</strong> — apenas para compatibilidade (IDs de objeto Git, checksums legados de CI). Não use em fronteiras de segurança — ataques práticos de colisão existem desde 2017.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Hash não é criptografia.</strong> Hashes são one-way; você não consegue o original de volta. Se precisa de confidencialidade, criptografe.</li>
  <li><strong>Não faça hash de senha com SHA-256 puro.</strong> SHA puro é rápido — isso ajuda atacantes a fazer brute-force. Use uma KDF lenta (Argon2id, bcrypt, scrypt) para armazenar senhas.</li>
  <li><strong>MD5 está intencionalmente ausente.</strong> Quebrado desde o início dos anos 2000. Onde quer que você "precise" de MD5, também precisa sinalizar uma revisão de segurança.</li>
  <li><strong>Espaço em branco importa.</strong> Uma quebra de linha no fim produz um hash diferente do mesmo texto sem ela. Compare a saída hex exatamente.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Kryptograficzny hash bierze dowolne wejście i produkuje odcisk palca o stałej długości. Dwa identyczne wejścia zawsze dają ten sam digest; zmiana jednego bitu zmienia digest całkowicie. Hashe leżą u podstaw weryfikacji integralności plików, content-addressable storage, podpisów cyfrowych i pipeline'ów do hashowania haseł (gdzie są łączone z wolną funkcją typu Argon2 albo bcrypt).</p>
<p>Całe hashowanie tutaj używa <code>crypto.subtle.digest</code> z przeglądarki — tych samych prymitywów, które napędzają TLS. Twój input nigdy nie opuszcza strony.</p>

<h3>Kiedy używać którego</h3>
<ul>
  <li><strong>SHA-256</strong> — sensowny default do weryfikacji integralności, content addressingu (Git, w stylu IPFS), kluczy HMAC i podpisów.</li>
  <li><strong>SHA-384 / SHA-512</strong> — przydatny, gdy potrzebujesz szerszego digestu (tuning PBKDF2/HKDF, większe klucze HMAC, post-quantum margines).</li>
  <li><strong>SHA-1</strong> — tylko do kompatybilności (Git object IDs, legacy checksum w CI). Nie używaj do granic bezpieczeństwa — praktyczne ataki kolizyjne istnieją od 2017.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Hashowanie to nie szyfrowanie.</strong> Hashe są jednokierunkowe; nie odzyskasz oryginału. Jeśli potrzebujesz poufności — szyfruj.</li>
  <li><strong>Nie hashuj haseł czystym SHA-256.</strong> Czysty SHA jest szybki — to pomaga atakującym brute-force'ować. Do przechowywania haseł użyj wolnego KDF (Argon2id, bcrypt, scrypt).</li>
  <li><strong>MD5 jest celowo nieobecny.</strong> Złamany od początku lat 2000. Wszędzie tam, gdzie "potrzebujesz" MD5, musisz też zgłosić review bezpieczeństwa.</li>
  <li><strong>Białe znaki mają znaczenie.</strong> Końcowy newline daje inny hash niż ten sam tekst bez niego. Porównuj wyjście hex dokładnie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>暗号学的ハッシュは、任意の入力を固定長のフィンガープリントに変換します。同じ入力からは常に同じダイジェストが得られ、1 ビットでも変えれば全く別のダイジェストになります。ハッシュはファイル整合性検査、コンテンツアドレッサブルストレージ、デジタル署名、パスワードハッシュ（Argon2 や bcrypt のような遅い関数と併用）など、多くの場面で基盤となっています。</p>
<p>本ツールは TLS と同じプリミティブであるブラウザの <code>crypto.subtle.digest</code> を使用します。入力はページから外に出ません。</p>

<h3>どれを使うか</h3>
<ul>
  <li><strong>SHA-256</strong> — 整合性検査、コンテンツアドレッシング（Git、IPFS 系）、HMAC キー、署名のデフォルトとして妥当。</li>
  <li><strong>SHA-384 / SHA-512</strong> — より広いダイジェストが必要な場合（PBKDF2/HKDF のチューニング、より大きな HMAC キー、ポスト量子のマージン）に有用。</li>
  <li><strong>SHA-1</strong> — 互換性目的のみ（Git のオブジェクト ID、レガシー CI のチェックサム）。セキュリティ境界には使用しないこと。2017 年以降、現実的な衝突攻撃が存在します。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>ハッシュは暗号化ではありません。</strong> ハッシュは一方向で、元には戻せません。機密性が必要なら暗号化を使ってください。</li>
  <li><strong>パスワードを生の SHA-256 でハッシュしないこと。</strong> 素の SHA は高速で、攻撃側のブルートフォースに有利です。パスワード保管には遅い KDF（Argon2id、bcrypt、scrypt）を使ってください。</li>
  <li><strong>MD5 は意図的に提供していません。</strong> 2000 年代初頭から破られています。「MD5 が必要」と思った場面では、まずセキュリティレビューを検討してください。</li>
  <li><strong>空白文字は重要です。</strong> 末尾の改行があるかないかでハッシュは変わります。hex 出力を厳密に比較してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een cryptografische hash neemt elke input en produceert een fingerprint van vaste lengte. Twee identieke inputs hashen altijd naar dezelfde digest; één bit veranderen verandert de digest volledig. Hashes onderbouwen file-integrity checks, content-addressable storage, digital signatures en password-hashing pipelines (waar ze met een trage functie als Argon2 of bcrypt worden gecombineerd).</p>
<p>Al het hashen hier gebruikt <code>crypto.subtle.digest</code> van de browser — dezelfde primitives die TLS aansturen. Je input verlaat de pagina nooit.</p>

<h3>Wanneer welke</h3>
<ul>
  <li><strong>SHA-256</strong> — verstandige default voor integrity checks, content addressing (Git, IPFS-style), HMAC-keys en signatures.</li>
  <li><strong>SHA-384 / SHA-512</strong> — nuttig als je een bredere digest nodig hebt (PBKDF2/HKDF-tuning, grotere HMAC-keys, post-quantum-marge-gewoontes).</li>
  <li><strong>SHA-1</strong> — alleen voor compatibiliteit (Git object IDs, legacy CI-checksums). Niet gebruiken voor security boundaries — praktische collision attacks bestaan sinds 2017.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Hashen is geen encryptie.</strong> Hashes zijn one-way; je krijgt het origineel niet terug. Als je vertrouwelijkheid nodig hebt, versleutel.</li>
  <li><strong>Hash wachtwoorden niet met raw SHA-256.</strong> Plain SHA is snel — dat helpt aanvallers brute-forcen. Gebruik een trage KDF (Argon2id, bcrypt, scrypt) voor wachtwoordopslag.</li>
  <li><strong>MD5 is opzettelijk afwezig.</strong> Gebroken sinds begin jaren 2000. Overal waar je MD5 "nodig" hebt, moet je ook een security review aanvragen.</li>
  <li><strong>Whitespace doet ertoe.</strong> Een trailing newline produceert een andere hash dan dezelfde tekst zonder. Vergelijk hex output exact.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir kriptografik hash herhangi bir girdi alır ve sabit uzunluklu bir parmak izi üretir. Aynı girdiler her zaman aynı digest'e hash'lenir; tek bir bit değiştirmek digest'i tamamen değiştirir. Hash'ler dosya bütünlüğü kontrolleri, içerik adreslenebilir depolama, dijital imzalar ve parola hash'leme pipeline'larının (Argon2 veya bcrypt gibi yavaş bir fonksiyonla birleştirildikleri) temelinde yatar.</p>
<p>Buradaki tüm hash'leme tarayıcının <code>crypto.subtle.digest</code>'ini kullanır — TLS'i çalıştıran aynı primitive'ler. Girişin sayfayı asla terk etmez.</p>

<h3>Hangisini ne zaman kullanmalı</h3>
<ul>
  <li><strong>SHA-256</strong> — bütünlük kontrolleri, içerik adresleme (Git, IPFS-tarzı), HMAC anahtarları ve imzalar için makul varsayılan.</li>
  <li><strong>SHA-384 / SHA-512</strong> — daha geniş bir digest gerektiğinde kullanışlıdır (PBKDF2/HKDF ince ayarı, daha büyük HMAC anahtarları, post-quantum-marjı alışkanlıkları).</li>
  <li><strong>SHA-1</strong> — yalnızca uyumluluk için (Git nesne ID'leri, eski CI checksum'ları). Güvenlik sınırları için kullanma — pratik çarpışma saldırıları 2017'den beri vardır.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Hash'leme şifreleme değildir.</strong> Hash'ler tek yönlüdür; orijinali geri alamazsın. Gizlilik gerekiyorsa, şifrele.</li>
  <li><strong>Parolaları ham SHA-256 ile hash'leme.</strong> Düz SHA hızlıdır — bu saldırganların brute-force yapmasına yardım eder. Parola depolama için yavaş bir KDF (Argon2id, bcrypt, scrypt) kullan.</li>
  <li><strong>MD5 kasıtlı olarak yok.</strong> 2000'lerin başından beri kırık. MD5'e "ihtiyaç duyduğun" her yerde bir güvenlik incelemesi de işaretlemen gerekir.</li>
  <li><strong>Boşluk önemlidir.</strong> Sondaki bir yeni satır, onsuz aynı metnin farklı bir hash'ini üretir. Hex çıktısını tam olarak karşılaştır.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Cryptographic hash mengambil input apa pun dan menghasilkan fingerprint dengan panjang tetap. Dua input yang identik selalu di-hash ke digest yang sama; mengubah satu bit saja mengubah digest sepenuhnya. Hash menjadi dasar dari pengecekan integritas file, content-addressable storage, digital signature, dan pipeline password hashing (di mana mereka digabungkan dengan fungsi lambat seperti Argon2 atau bcrypt).</p>
<p>Semua hashing di sini menggunakan <code>crypto.subtle.digest</code> dari browser — primitive yang sama dengan yang menggerakkan TLS. Input kamu tidak pernah meninggalkan halaman.</p>

<h3>Kapan pakai yang mana</h3>
<ul>
  <li><strong>SHA-256</strong> — default yang masuk akal untuk pengecekan integritas, content addressing (Git, gaya IPFS), HMAC key, dan signature.</li>
  <li><strong>SHA-384 / SHA-512</strong> — berguna saat kamu butuh digest yang lebih lebar (tuning PBKDF2/HKDF, HMAC key yang lebih besar, kebiasaan margin post-quantum).</li>
  <li><strong>SHA-1</strong> — hanya untuk kompatibilitas (Git object ID, checksum CI legacy). Jangan gunakan untuk batas keamanan — serangan collision praktis sudah ada sejak 2017.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Hashing bukan enkripsi.</strong> Hash itu one-way; kamu tidak bisa mendapatkan kembali yang asli. Kalau butuh kerahasiaan, enkripsi.</li>
  <li><strong>Jangan hash password dengan SHA-256 mentah.</strong> Plain SHA itu cepat — itu membantu attacker brute-force. Pakai KDF lambat (Argon2id, bcrypt, scrypt) untuk penyimpanan password.</li>
  <li><strong>MD5 sengaja tidak ada.</strong> Sudah broken sejak awal 2000-an. Di mana pun kamu "butuh" MD5, kamu juga butuh menandai security review.</li>
  <li><strong>Whitespace itu penting.</strong> Newline di akhir menghasilkan hash yang berbeda dari teks yang sama tanpa newline. Bandingkan output hex secara eksak.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Hàm hash mã hóa biến một input có độ dài bất kỳ thành một fingerprint có độ dài cố định. Cùng một input luôn cho cùng một hash; thay đổi nhỏ thay đổi toàn bộ hash; và việc đảo ngược từ hash về input là không khả thi về mặt tính toán (đối với hàm hash tốt). Tool này tính SHA-1, SHA-256, SHA-384 và SHA-512 bằng cách dùng WebCrypto của trình duyệt — không có gì rời khỏi thiết bị của bạn.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Xác minh tính toàn vẹn file: tính hash của download và so sánh với hash được công bố.</li>
  <li>Tạo cache key xác định từ content.</li>
  <li>Băm checksum để xác định các bản sao trong dataset.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>SHA-1 bị phá vỡ về mặt mã hóa.</strong> Va chạm đã được tìm thấy. Đừng dùng nó cho chữ ký mới — chỉ chấp nhận được cho kiểm tra tính toàn vẹn không phải bảo mật.</li>
  <li><strong>MD5 cũng bị phá vỡ.</strong> Vẫn ổn để dùng làm checksum không mật khẩu (kiểm tra một bản download bị hỏng) nhưng không dùng cho bảo mật.</li>
  <li><strong>Hash mật khẩu không phải hash chung.</strong> Cho mật khẩu, dùng bcrypt, scrypt, hoặc Argon2 — chúng cố ý chậm để chống brute force. SHA-256 quá nhanh.</li>
  <li><strong>Encoding quan trọng.</strong> Hash của <code>"hello"</code> có thể khác nhau tùy thuộc vào việc bạn coi nó là 5 byte ASCII hay 5 byte UTF-8 (chúng cùng trong trường hợp này, nhưng không khi có Unicode).</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>एक cryptographic hash किसी भी input को लेता है और एक fixed-length fingerprint produce करता है। दो identical inputs हमेशा same digest पर hash करते हैं; एक single bit बदलने से digest पूरी तरह बदल जाता है। Hashes file-integrity checks, content-addressable storage, digital signatures, और password-hashing pipelines (जहां वे Argon2 या bcrypt जैसे slow function के साथ combined हैं) को underpin करते हैं।</p>
<p>यहां सभी hashing browser के <code>crypto.subtle.digest</code> का उपयोग करती है — वही primitives जो TLS को power देते हैं। आपका input page से बाहर नहीं जाता।</p>

<h3>कब किसका उपयोग करें</h3>
<ul>
  <li><strong>SHA-256</strong> — integrity checks, content addressing (Git, IPFS-style), HMAC keys, और signatures के लिए समझदार default।</li>
  <li><strong>SHA-384 / SHA-512</strong> — उपयोगी जब आपको wider digest की आवश्यकता हो (PBKDF2/HKDF tuning, larger HMAC keys, post-quantum-margin habits)।</li>
  <li><strong>SHA-1</strong> — केवल compatibility के लिए (Git object IDs, legacy CI checksums)। Security boundaries के लिए उपयोग न करें — practical collision attacks 2017 से मौजूद हैं।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>Hashing encryption नहीं है।</strong> Hashes one-way हैं; आप original वापस नहीं पा सकते। यदि आपको confidentiality चाहिए, तो encrypt करें।</li>
  <li><strong>Passwords को raw SHA-256 से hash न करें।</strong> Plain SHA fast है — यह attackers को brute-force करने में मदद करता है। Password storage के लिए slow KDF (Argon2id, bcrypt, scrypt) का उपयोग करें।</li>
  <li><strong>MD5 जानबूझकर अनुपस्थित है।</strong> 2000 के दशक की शुरुआत से broken है। जहां भी आप MD5 की "जरूरत" समझते हैं, वहां security review भी flag करें।</li>
  <li><strong>Whitespace मायने रखता है।</strong> एक trailing newline बिना उसके वही text की तुलना में अलग hash produce करता है। Hex output को सटीक रूप से compare करें।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>Hash funkcia premení ľubovoľne dlhý vstup na fixed-size „odtlačok". Rovnaký vstup vždy dá rovnaký hash; akákoľvek zmena vstupu produkuje úplne iný hash. Tento nástroj počíta SHA-1, SHA-256, SHA-384 a SHA-512 cez WebCrypto API priamo v tvojom prehliadači — text nikdy neopustí stránku.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>Overenie integrity stiahnutého súboru (porovnaj SHA-256 s tým, čo je na stránke).</li>
  <li>Zhasovanie hesla pred poslaním? <strong>Nie — to robí backend s salt + bcrypt/argon2.</strong></li>
  <li>Cache key z obsahu (content-addressable storage).</li>
  <li>Sanity-check, že dva texty sú identické, bez ich porovnávania znak po znaku.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>MD5 a SHA-1 sú broken.</strong> Pre security použij SHA-256 alebo silnejšie. SHA-1 ešte občas pre git commit hash (rieši to SHA-256-aware git).</li>
  <li><strong>Hash hesla bez salt-u je zlý nápad.</strong> Useri majú slabé heslá a rainbow tables existujú. Použij bcrypt / argon2 / scrypt.</li>
  <li><strong>SHA-256 NIE JE šifrovanie.</strong> Nedá sa „dehashovať" — je jednosmerná. Šifrovanie je dvojsmerné.</li>
  <li><strong>UTF-8 encoding.</strong> Hash bajtov, nie znakov — uistite sa, že encoding je rovnaký na oboch koncoch.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>Hash funkce promění libovolně dlouhý vstup na fixed-size „otisk". Stejný vstup vždy dá stejný hash; jakákoli změna vstupu produkuje úplně jiný hash. Tenhle nástroj počítá SHA-1, SHA-256, SHA-384 a SHA-512 přes WebCrypto API přímo v tvém prohlížeči — text nikdy neopustí stránku.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>Ověření integrity stáhnutého souboru (porovnej SHA-256 s tím, co je na stránce).</li>
  <li>Hashování hesla před posláním? <strong>Ne — to dělá backend s salt + bcrypt/argon2.</strong></li>
  <li>Cache key z obsahu (content-addressable storage).</li>
  <li>Sanity-check, že dva texty jsou identické, bez jejich porovnávání znak po znaku.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>MD5 a SHA-1 jsou broken.</strong> Pro security použij SHA-256 nebo silnější. SHA-1 ještě občas pro git commit hash (řeší to SHA-256-aware git).</li>
  <li><strong>Hash hesla bez salt-u je špatný nápad.</strong> Uživatelé mají slabá hesla a rainbow tables existují. Použij bcrypt / argon2 / scrypt.</li>
  <li><strong>SHA-256 NENÍ šifrování.</strong> Nedá se „dehashovat" — je jednosměrná. Šifrování je obousměrné.</li>
  <li><strong>UTF-8 encoding.</strong> Hash bajtů, ne znaků — ujisti se, že encoding je stejný na obou koncích.</li>
</ul>
""",
    },
    "related": ["password-generator", "uuid-generator", "jwt-decoder"],
    "howto": {"flow": "transform", "action": "generate","noun": "text"},
}
