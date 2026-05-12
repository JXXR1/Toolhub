TOOL = {
    "slug": "credit-card-validator",
    "category": "validation",
    "icon": "💳",
    "tags": ["credit card", "validate", "luhn", "visa", "mastercard", "amex", "discover"],
    "i18n": {
        "en": {
            "name": "Credit Card Validator",
            "tagline": "Validate a card number with the Luhn check and detect the card brand. Runs locally — your number is never transmitted.",
            "description": "Free online credit card validator. Luhn (mod-10) checksum, brand detection (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay), and length verification. 100% client-side.",
        },
        "de": {"name": "Kreditkarten-Validator", "tagline": "Prüfe Kartennummern per Luhn-Algorithmus und erkenne die Kartenmarke. Läuft lokal — die Nummer wird nie übertragen.", "description": "Kostenloser Kreditkarten-Validator. Luhn-Prüfsumme, Markenerkennung (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) und Längenprüfung. 100% im Browser."},
        "es": {"name": "Validador de Tarjeta de Crédito", "tagline": "Valida un número de tarjeta con Luhn y detecta la marca. Funciona localmente — el número nunca se envía.", "description": "Validador de tarjeta de crédito gratuito. Suma de comprobación Luhn, detección de marca (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) y longitud. 100% en el navegador."},
        "fr": {"name": "Validateur de Carte Bancaire", "tagline": "Validez un numéro de carte avec Luhn et détectez la marque. Fonctionne localement — le numéro n'est jamais envoyé.", "description": "Validateur de carte bancaire gratuit. Somme de contrôle Luhn, détection de marque (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) et longueur. 100% dans le navigateur."},
        "it": {"name": "Validatore Carta di Credito", "tagline": "Valida un numero di carta con Luhn e rileva la marca. Funziona localmente — il numero non viene mai inviato.", "description": "Validatore di carta di credito gratuito. Checksum Luhn, rilevamento marca (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) e lunghezza. 100% nel browser."},
        "pt": {"name": "Validador de Cartão de Crédito", "tagline": "Valide um número de cartão com a verificação de Luhn e detecte a bandeira. Roda localmente — seu número nunca é transmitido.", "description": "Validador de cartão de crédito online gratuito. Checksum de Luhn (mod-10), detecção de bandeira (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) e verificação de tamanho. 100% client-side."},
        "pl": {"name": "Walidator Karty Kredytowej", "tagline": "Sprawdź numer karty algorytmem Luhna i wykryj wystawcę. Działa lokalnie — twój numer nigdy nie jest wysyłany.", "description": "Darmowy walidator kart kredytowych online. Checksum Luhna (mod-10), wykrywanie wystawcy (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) i sprawdzanie długości. 100% po stronie klienta."},
        "ja": {"name": "クレジットカード検証ツール", "tagline": "Luhn チェックでカード番号を検証し、ブランドを検出。ローカル動作で、番号は送信されません。", "description": "オンライン無料のクレジットカード検証ツール。Luhn (mod-10) チェックサム、ブランド検出（Visa、Mastercard、Amex、Discover、JCB、Diners、UnionPay）、桁数検証を行います。100% クライアントサイドで動作します。"},
        "nl": {"name": "Creditcard-validator", "tagline": "Valideer een kaartnummer met de Luhn-check en detecteer het kaartmerk. Draait lokaal — je nummer wordt nooit verzonden.", "description": "Gratis online creditcard-validator. Luhn (mod-10) checksum, brand-detectie (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) en lengtecontrole. 100% client-side."},
        "tr": {"name": "Kredi Kartı Doğrulayıcı", "tagline": "Kart numarasını Luhn kontrolü ile doğrula ve kart markasını tespit et. Yerel çalışır — numaran asla iletilmez.", "description": "Ücretsiz online kredi kartı doğrulayıcı. Luhn (mod-10) checksum, marka tespiti (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) ve uzunluk doğrulaması. %100 istemci tarafında çalışır."},
        "id": {"name": "Validator Kartu Kredit", "tagline": "Validasi nomor kartu dengan cek Luhn dan deteksi brand kartu. Berjalan lokal — nomormu tidak pernah dikirim.", "description": "Validator kartu kredit gratis. Cek nomor kartu dengan algoritma Luhn dan deteksi brand (Visa, Mastercard, Amex, Discover, JCB, Diners). Berjalan sepenuhnya di browser-mu — tanpa pelacakan, tanpa upload."},
        "vi": {"name": "Xác thực Thẻ Tín dụng", "tagline": "Xác thực số thẻ bằng kiểm tra Luhn và phát hiện brand. Chạy cục bộ — số thẻ của bạn không bao giờ được gửi đi.", "description": "Xác thực số thẻ tín dụng miễn phí trực tuyến. Kiểm tra Luhn checksum và phát hiện brand thẻ (Visa, Mastercard, Amex, Discover, JCB và các loại khác). Toàn bộ kiểm tra chạy trong trình duyệt của bạn — số thẻ không bao giờ được gửi đi."},
    },
    "body": """
<div class="tool-card">
  <label>Card number</label>
  <input type="text" id="cv-input" oninput="cvRun()" placeholder="4242 4242 4242 4242" inputmode="numeric" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">Spaces and hyphens are ignored. Number is never sent — validation is entirely in your browser.</div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="cv-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.cv-result{display:grid;gap:0.55rem}
.cv-row{display:grid;grid-template-columns:120px 1fr;gap:0.6rem;align-items:center;padding:0.5rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-size:0.9rem}
.cv-row .lbl{color:var(--text-muted);font-size:0.78rem;font-family:ui-monospace,monospace}
.cv-pass{color:#10b981;font-weight:600}
.cv-fail{color:#ef4444;font-weight:600}
</style>
<script>
const CV_BRANDS = [
  {name:'Visa',          regex:/^4/,                                             lengths:[13,16,19], cvv:3},
  {name:'Mastercard',    regex:/^(5[1-5]|2[2-7])/,                               lengths:[16],       cvv:3},
  {name:'American Express', regex:/^3[47]/,                                       lengths:[15],       cvv:4},
  {name:'Discover',      regex:/^(6011|65|64[4-9]|622(12[6-9]|1[3-9]\\d|[2-8]\\d{2}|9([01]\\d|2[0-5])))/, lengths:[16,19], cvv:3},
  {name:'JCB',           regex:/^35(2[89]|[3-8])/,                               lengths:[16,19],    cvv:3},
  {name:'Diners Club',   regex:/^3(?:0[0-5]|[68])/,                              lengths:[14,16,19], cvv:3},
  {name:'UnionPay',      regex:/^62/,                                             lengths:[16,17,18,19], cvv:3},
  {name:'Maestro',       regex:/^(5018|5020|5038|6304|6759|676[1-3])/,           lengths:[12,13,14,15,16,17,18,19], cvv:3},
];
function cvDetectBrand(num){
  for(const b of CV_BRANDS) if(b.regex.test(num)) return b;
  return null;
}
function cvLuhn(num){
  let sum=0, alt=false;
  for(let i=num.length-1;i>=0;i--){
    let n = parseInt(num[i],10);
    if(isNaN(n)) return false;
    if(alt){n*=2; if(n>9) n-=9}
    sum += n;
    alt = !alt;
  }
  return sum % 10 === 0;
}
function cvRun(){
  const raw = document.getElementById('cv-input').value;
  const num = raw.replace(/[\\s\\-]/g,'');
  const out = document.getElementById('cv-out');
  out.classList.remove('error');
  if(!num){ out.textContent = '{LBL_NO_INPUT}'; out.className = 'output'; return; }
  if(!/^\\d+$/.test(num)){ out.classList.add('error'); out.textContent = 'Card number must contain only digits.'; return; }
  const brand = cvDetectBrand(num);
  const lenOk = brand ? brand.lengths.includes(num.length) : (num.length>=12 && num.length<=19);
  const luhnOk = cvLuhn(num);
  const valid = lenOk && luhnOk;
  out.className = 'output';
  out.innerHTML = `<div class="cv-result">
    <div class="cv-row"><div class="lbl">Brand</div><div>${brand ? brand.name : '<span class="cv-fail">Unknown</span>'}</div></div>
    <div class="cv-row"><div class="lbl">Length</div><div>${num.length} digits ${lenOk?'<span class="cv-pass">✓</span>':'<span class="cv-fail">✗ expected '+(brand?brand.lengths.join('/'):'12–19')+'</span>'}</div></div>
    <div class="cv-row"><div class="lbl">Luhn check</div><div>${luhnOk?'<span class="cv-pass">✓ Pass</span>':'<span class="cv-fail">✗ Fail</span>'}</div></div>
    <div class="cv-row"><div class="lbl">CVV</div><div>${brand?brand.cvv+' digits':'3–4 digits'}</div></div>
    <div class="cv-row"><div class="lbl">Verdict</div><div>${valid?'<span class="cv-pass">✓ Number is structurally valid</span>':'<span class="cv-fail">✗ Number is not valid</span>'}</div></div>
  </div>`;
}
document.addEventListener('DOMContentLoaded', cvRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Card numbers carry a built-in checksum (the Luhn / mod-10 algorithm) and start with prefixes that identify the issuing brand. Together those let you catch typos and identify the brand before sending a number to a payment processor. This tool runs both checks 100% in your browser — the number you paste never leaves the page. It's developer-grade structural validation, not a fraud-check or live-card lookup.</p>

<h3>When to use it</h3>
<ul>
  <li>Validating that a test card number you've copied is well-formed (test cards from <a href="https://docs.stripe.com/testing" rel="noopener">Stripe's docs</a> or similar all pass Luhn).</li>
  <li>Sanity-checking input fields in a form — does the number satisfy the basic structure before round-tripping to a payments API that'd otherwise charge for the lookup?</li>
  <li>Auditing a card number that "looks wrong" to see whether it's a typo (Luhn fails) or a brand mismatch (length wrong for the prefix).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>"Structurally valid" doesn't mean "issued" or "active".</strong> Real validation requires a payment processor — which costs money or places a hold. This tool catches typos, not closed accounts.</li>
  <li><strong>Don't paste real card numbers anywhere</strong> — including this tool. The browser doesn't transmit them, but a screen-recorder, browser extension, or open dev-tools panel can. Use a known test number instead.</li>
  <li><strong>Some 16-digit numbers aren't cards.</strong> Loyalty cards, gift cards, and some prepaid SKUs reuse the format; Luhn pass + brand match doesn't guarantee a payment instrument.</li>
  <li><strong>Co-branded cards.</strong> Cards issued under one brand may show another's logo. The brand detection here uses the canonical issuer prefix, not the printed logo.</li>
</ul>

<h3>Test numbers (safe to paste)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Números de cartão carregam um checksum embutido (o algoritmo de Luhn / mod-10) e começam com prefixos que identificam a bandeira emissora. Juntos, isso permite pegar erros de digitação e identificar a bandeira antes de enviar um número a um gateway de pagamento. Esta ferramenta roda os dois checks 100% no seu navegador — o número que você cola nunca sai da página. É validação estrutural de nível de desenvolvedor, não checagem de fraude nem consulta de cartão ao vivo.</p>

<h3>Quando usar</h3>
<ul>
  <li>Validar que um número de cartão de teste que você copiou está bem-formado (cartões de teste da <a href="https://docs.stripe.com/testing" rel="noopener">documentação da Stripe</a> ou similares passam todos no Luhn).</li>
  <li>Conferir campos de input num formulário — o número satisfaz a estrutura básica antes de fazer round-trip a uma API de pagamentos que cobraria pela consulta?</li>
  <li>Auditar um número de cartão que "parece errado" para ver se é erro de digitação (Luhn falha) ou bandeira incompatível (tamanho errado para o prefixo).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>"Estruturalmente válido" não significa "emitido" ou "ativo".</strong> Validação real exige um gateway de pagamento — o que custa dinheiro ou faz uma autorização. Esta ferramenta pega erros de digitação, não contas encerradas.</li>
  <li><strong>Não cole números de cartão reais em lugar nenhum</strong> — incluindo esta ferramenta. O navegador não transmite, mas um gravador de tela, extensão de navegador ou painel de dev-tools aberto pode capturar. Use um número de teste conhecido.</li>
  <li><strong>Alguns números de 16 dígitos não são cartões.</strong> Cartões fidelidade, gift cards e alguns SKUs pré-pagos reutilizam o formato; passar no Luhn + bater bandeira não garante que seja um meio de pagamento.</li>
  <li><strong>Cartões co-branded.</strong> Cartões emitidos sob uma bandeira podem exibir o logo de outra. A detecção de bandeira aqui usa o prefixo canônico do emissor, não o logo impresso.</li>
</ul>

<h3>Números de teste (seguros para colar)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Numery kart noszą wbudowaną sumę kontrolną (algorytm Luhna / mod-10) i zaczynają się od prefiksów identyfikujących wystawcę. Razem to pozwala wyłapać literówki i rozpoznać wystawcę zanim wyślesz numer do procesora płatności. To narzędzie liczy oba sprawdzenia 100% w twojej przeglądarce — wklejony numer nigdy nie opuszcza strony. To deweloperska walidacja strukturalna, nie weryfikacja anty-fraudowa ani sprawdzenie aktywności karty.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Walidacja, czy testowy numer karty, który skopiowałeś, jest poprawnie zbudowany (karty testowe z <a href="https://docs.stripe.com/testing" rel="noopener">dokumentacji Stripe'a</a> i podobnych przechodzą Luhna).</li>
  <li>Sanity check pól w formularzu — czy numer spełnia podstawową strukturę, zanim odbije się o API płatności, które kasowałoby za sprawdzenie?</li>
  <li>Audyt numeru, który "wygląda źle", żeby zobaczyć, czy to literówka (Luhn nie przechodzi) czy niezgodność wystawcy (zła długość dla prefiksu).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>"Strukturalnie poprawny" nie znaczy "wydany" ani "aktywny".</strong> Prawdziwa walidacja wymaga procesora płatności — co kosztuje albo blokuje środki. To narzędzie łapie literówki, nie zamknięte konta.</li>
  <li><strong>Nie wklejaj nigdzie prawdziwych numerów kart</strong> — w tym tu. Przeglądarka ich nie wysyła, ale screen recorder, rozszerzenie albo otwarte dev-toolsy mogą podejrzeć. Użyj znanego numeru testowego.</li>
  <li><strong>Niektóre 16-cyfrowe numery to nie karty.</strong> Karty lojalnościowe, gift cardy i pewne pre-paid SKU używają tego samego formatu; przejście Luhna + zgodny wystawca nie gwarantuje, że to instrument płatniczy.</li>
  <li><strong>Karty co-branded.</strong> Karty wydane pod jedną marką mogą mieć logo innej. Wykrywanie wystawcy używa tu kanonicznego prefiksu, nie nadrukowanego logo.</li>
</ul>

<h3>Numery testowe (bezpieczne do wklejenia)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "ja": """
<h2>用途</h2>
<p>カード番号には組み込みのチェックサム（Luhn / mod-10 アルゴリズム）があり、先頭桁の接頭辞は発行ブランドを示します。これらを使うと、決済プロセッサに番号を送る前にタイプミスを検出し、ブランドを判定できます。本ツールはこの 2 つのチェックを 100% ブラウザ内で実行します。貼り付けた番号はページから外に出ません。これは開発者向けの構造的検証であり、不正検知や有効カードの照会ではありません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>コピーしたテストカード番号が形式的に正しいか確認する（<a href="https://docs.stripe.com/testing" rel="noopener">Stripe のドキュメント</a>などのテストカードはすべて Luhn を通ります）。</li>
  <li>フォームの入力値のサニティチェック — 課金される決済 API に投げる前に、番号が基本構造を満たしているか確認したいとき。</li>
  <li>「何か変だ」と感じる番号の監査 — タイプミス（Luhn が失敗）か、ブランド不一致（接頭辞に対する桁数の誤り）かを切り分けたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>「構造的に有効」は「発行済み」「有効」と同じではありません。</strong> 本物の検証には決済プロセッサが必要で、コストや与信枠の確保が伴います。本ツールはタイプミスを捕まえますが、解約済みアカウントは判定できません。</li>
  <li><strong>本物のカード番号はどこにも貼り付けないこと</strong> — 本ツールも例外ではありません。ブラウザは送信しませんが、画面録画ツール、ブラウザ拡張、開いた DevTools パネルなどから漏洩する可能性があります。既知のテスト番号を使ってください。</li>
  <li><strong>16 桁の番号がすべてクレカとは限りません。</strong> ポイントカード、ギフトカード、一部のプリペイド SKU も同じ形式を再利用しています。Luhn 通過 + ブランド一致でも、決済可能な手段である保証はありません。</li>
  <li><strong>コブランドカード。</strong> あるブランドで発行されたカードに別ブランドのロゴが印字されていることがあります。本ツールのブランド検出は印字ロゴではなく、発行元のカノニカル接頭辞に基づきます。</li>
</ul>

<h3>テスト用番号（貼り付けても安全）</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Kaartnummers dragen een ingebouwde checksum (het Luhn / mod-10 algoritme) en beginnen met prefixes die het uitgevende merk identificeren. Samen laten die je typo's vangen en het merk identificeren voor je een nummer naar een payment processor stuurt. Deze tool draait beide checks 100% in je browser — het nummer dat je plakt verlaat de pagina nooit. Het is developer-grade structurele validatie, geen fraud-check of live-card lookup.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Valideren dat een test-kaartnummer dat je hebt gekopieerd well-formed is (test-kaarten uit <a href="https://docs.stripe.com/testing" rel="noopener">Stripe's docs</a> of vergelijkbaar passeren allemaal Luhn).</li>
  <li>Sanity check op input-velden in een formulier — voldoet het nummer aan de basisstructuur voor je het round-trippt naar een payments-API die anders kosten in rekening brengt voor de lookup?</li>
  <li>Een kaartnummer audit doen dat "verkeerd lijkt" om te zien of het een typo is (Luhn faalt) of een brand-mismatch (lengte klopt niet bij de prefix).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>"Structureel geldig" betekent niet "uitgegeven" of "actief".</strong> Echte validatie vereist een payment processor — wat kost of een autorisatie plaatst. Deze tool vangt typo's, geen gesloten rekeningen.</li>
  <li><strong>Plak nergens echte kaartnummers</strong> — ook niet in deze tool. De browser stuurt ze niet door, maar een screen-recorder, browser-extensie of geopend dev-tools panel kan dat wel. Gebruik in plaats daarvan een bekend testnummer.</li>
  <li><strong>Sommige 16-cijferige nummers zijn geen kaarten.</strong> Loyalty cards, cadeaukaarten en sommige prepaid SKU's hergebruiken het formaat; Luhn-pass + brand-match garandeert geen betalingsinstrument.</li>
  <li><strong>Co-branded kaarten.</strong> Kaarten uitgegeven onder één merk tonen mogelijk het logo van een ander merk. De brand-detectie hier gebruikt de canonieke issuer-prefix, niet het gedrukte logo.</li>
</ul>

<h3>Testnummers (veilig om te plakken)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Kart numaraları yerleşik bir checksum (Luhn / mod-10 algoritması) taşır ve veren markayı tanımlayan öneklerle başlar. Bu ikisi birlikte, bir numarayı ödeme işlemcisine göndermeden önce yazım hatalarını yakalamana ve markayı tanımlamana izin verir. Bu araç her iki kontrolü de %100 tarayıcında yapar — yapıştırdığın numara sayfayı asla terk etmez. Geliştirici seviyesi yapısal doğrulamadır, dolandırıcılık kontrolü veya canlı kart araması değildir.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Kopyaladığın bir test kart numarasının iyi biçimli olduğunu doğrulama (<a href="https://docs.stripe.com/testing" rel="noopener">Stripe docs</a> veya benzerinden test kartları hepsi Luhn'dan geçer).</li>
  <li>Bir formdaki giriş alanlarının sanity check'i — numara, aksi takdirde arama için ücret alan bir ödeme API'sine round-trip yapmadan önce temel yapıyı karşılıyor mu?</li>
  <li>"Yanlış görünen" bir kart numarasını denetleyip yazım hatası mı (Luhn başarısız) yoksa marka uyumsuzluğu mu (önek için uzunluk yanlış) olduğunu görme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>"Yapısal olarak geçerli" "verilmiş" veya "aktif" anlamına gelmez.</strong> Gerçek doğrulama bir ödeme işlemcisi gerektirir — bu para harcatır veya hold koyar. Bu araç yazım hatalarını yakalar, kapatılmış hesapları değil.</li>
  <li><strong>Gerçek kart numaralarını hiçbir yere yapıştırma</strong> — bu araç dahil. Tarayıcı iletmez ama ekran kaydedici, tarayıcı uzantısı veya açık dev-tools paneli yapabilir. Bilinen bir test numarası kullan.</li>
  <li><strong>Bazı 16 basamaklı numaralar kart değildir.</strong> Sadakat kartları, hediye kartları ve bazı prepaid SKU'lar biçimi tekrar kullanır; Luhn geçişi + marka eşleşmesi bir ödeme aracı garantilemez.</li>
  <li><strong>Co-branded kartlar.</strong> Bir marka altında verilen kartlar başka bir markanın logosunu gösterebilir. Buradaki marka tespiti basılı logoyu değil kanonik veren önekini kullanır.</li>
</ul>

<h3>Test numaraları (yapıştırılması güvenli)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Nomor kartu memiliki checksum bawaan (algoritma Luhn / mod-10) dan diawali prefix yang mengidentifikasi brand penerbit. Bersama-sama keduanya memungkinkan kamu menangkap typo dan mengidentifikasi brand sebelum mengirim nomor ke payment processor. Tool ini menjalankan kedua pemeriksaan 100% di browser-mu — nomor yang kamu tempel tidak pernah meninggalkan halaman. Ini validasi struktural untuk developer, bukan fraud-check atau lookup kartu live.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Memvalidasi bahwa nomor kartu test yang kamu salin well-formed (kartu test dari <a href="https://docs.stripe.com/testing" rel="noopener">dokumentasi Stripe</a> atau yang serupa semua lolos Luhn).</li>
  <li>Sanity check field input di form — apakah nomor memenuhi struktur dasar sebelum round-trip ke API pembayaran yang biasanya menarik biaya untuk lookup?</li>
  <li>Mengaudit nomor kartu yang "kelihatannya salah" untuk melihat apakah typo (Luhn gagal) atau brand mismatch (panjang salah untuk prefix-nya).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>"Valid secara struktural" tidak berarti "diterbitkan" atau "aktif".</strong> Validasi sungguhan butuh payment processor — yang berbiaya atau menempatkan hold. Tool ini menangkap typo, bukan akun yang ditutup.</li>
  <li><strong>Jangan tempel nomor kartu asli di mana pun</strong> — termasuk di tool ini. Browser tidak mengirimkannya, tapi screen-recorder, ekstensi browser, atau dev-tools terbuka bisa. Pakai nomor test yang dikenal.</li>
  <li><strong>Beberapa nomor 16 digit bukan kartu.</strong> Kartu loyalty, gift card, dan beberapa SKU prepaid memakai format yang sama; lolos Luhn + brand match tidak menjamin ini instrumen pembayaran.</li>
  <li><strong>Kartu co-branded.</strong> Kartu yang diterbitkan satu brand bisa menampilkan logo brand lain. Deteksi brand di sini memakai prefix penerbit kanonik, bukan logo cetaknya.</li>
</ul>

<h3>Nomor test (aman ditempel)</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Số thẻ tín dụng có một checksum tích hợp gọi là Luhn algorithm. Mọi nhà phát hành — Visa, Mastercard, Amex, Discover, JCB — phát hành số mà chữ số cuối làm cho toàn bộ chuỗi vượt qua Luhn. Sai số <em>do người gõ</em> hầu như luôn fail Luhn, nên kiểm tra ở phía client (trước khi gửi lên cổng thanh toán) bắt được hầu hết các lỗi gõ thông thường ngay tại nguồn.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Validation form checkout — bắt lỗi gõ trước khi gọi cổng thanh toán.</li>
  <li>Phát hiện brand từ tiền tố BIN — hữu ích để hiển thị logo nhà phát hành phù hợp.</li>
  <li>Sanity check một số test trong dataset trước khi import.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Vượt qua Luhn không có nghĩa là thẻ có thật.</strong> Bất kỳ ai cũng có thể tạo số "hợp lệ" về Luhn. Chỉ cổng thanh toán biết liệu thẻ có tồn tại và đã được duyệt hay không.</li>
  <li><strong>Đừng bao giờ lưu PAN không cần thiết.</strong> PCI DSS có quy tắc nghiêm ngặt về lưu trữ dữ liệu thẻ. Tốt nhất là dùng token hóa và không bao giờ chạm vào PAN ngoài cổng.</li>
  <li><strong>Phát hiện brand không thay thế kiểm tra của cổng.</strong> Tiền tố BIN có thể thay đổi và một số dải overlap; coi việc đoán brand là gợi ý UX, không phải sự thật.</li>
  <li><strong>Công cụ này chạy hoàn toàn cục bộ.</strong> Số bạn nhập không bao giờ rời khỏi trình duyệt — nhưng đừng dán PAN sản xuất vào bất kỳ tool ngẫu nhiên nào dù sao đi nữa. Dùng <a href="https://www.payments-cards.com/test-cards.html">số test</a> để demo.</li>
</ul>
""",
    },
    "related": ["email-validator", "hash-generator", "regex-tester"],
    "howto": {"flow": "transform", "action": "validate","noun": "card number"},
}
