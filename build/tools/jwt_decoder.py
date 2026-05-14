TOOL = {
    "slug": "jwt-decoder",
    "category": "developer",
    "icon": "🔓",
    "tags": ["jwt", "json web token", "decode", "auth", "oauth", "openid"],
    "i18n": {
        "en": {
            "name": "JWT Decoder",
            "tagline": "Paste a JWT to decode its header and payload. All decoding runs in your browser — tokens never leave the page.",
            "description": "Free online JSON Web Token decoder. Decode header and payload, verify expiry timestamps, inspect signature. Works fully offline in your browser.",
        },
        "de": {
            "name": "JWT-Decoder",
            "tagline": "JWT einfügen, um Header und Payload zu dekodieren. Alles läuft im Browser — Tokens verlassen die Seite nicht.",
            "description": "Kostenloser JSON Web Token Decoder. Header und Payload dekodieren, Ablaufzeit prüfen, Signatur ansehen. Vollständig offline im Browser.",
        },
        "es": {
            "name": "Decodificador JWT",
            "tagline": "Pega un JWT para decodificar su header y payload. Todo se ejecuta en tu navegador — los tokens nunca se envían.",
            "description": "Decodificador JSON Web Token gratuito. Decodifica header y payload, verifica caducidad, inspecciona la firma. Funciona offline en tu navegador.",
        },
        "fr": {
            "name": "Décodeur JWT",
            "tagline": "Collez un JWT pour décoder son en-tête et son payload. Tout est traité localement — les tokens ne quittent pas la page.",
            "description": "Décodeur JSON Web Token gratuit. Décode en-tête et payload, vérifie l'expiration, inspecte la signature. Fonctionne hors-ligne dans votre navigateur.",
        },
        "it": {
            "name": "Decoder JWT",
            "tagline": "Incolla un JWT per decodificare header e payload. Tutto viene eseguito nel browser — i token non lasciano la pagina.",
            "description": "Decoder JSON Web Token gratuito. Decodifica header e payload, verifica scadenza, ispeziona la firma. Funziona offline nel browser.",
        },
        "pt": {
            "name": "Decoder JWT",
            "tagline": "Cole um JWT para decodificar header e payload. Tudo roda no seu browser — os tokens não saem da página.",
            "description": "Decoder de JSON Web Token grátis online. Decodifica header e payload, verifica timestamps de expiração, inspeciona a signature. Funciona totalmente offline no seu browser.",
        },
        "pl": {
            "name": "Decoder JWT",
            "tagline": "Wklej JWT, żeby zdekodować header i payload. Wszystko liczy się w przeglądarce — tokeny nie opuszczają strony.",
            "description": "Darmowy online decoder JSON Web Token. Dekoduje header i payload, weryfikuje timestamp wygaśnięcia, pokazuje signature. Działa w pełni offline w przeglądarce.",
        },
        "ja": {
            "name": "JWT デコーダー",
            "tagline": "JWT を貼り付けてヘッダーとペイロードをデコード。すべてブラウザ内で処理し、トークンはページから外に出ません。",
            "description": "オンライン無料の JSON Web Token デコーダー。ヘッダーとペイロードのデコード、有効期限のタイムスタンプ確認、署名の表示まで対応。完全にオフライン（ブラウザ内）で動作します。",
        },
        "nl": {"name": "JWT Decoder", "tagline": "Plak een JWT om header en payload te decoderen. Alle decodering draait in je browser — tokens verlaten de pagina nooit.", "description": "Gratis online JSON Web Token decoder. Decodeer header en payload, verifieer expiry-timestamps, inspecteer signature. Werkt volledig offline in je browser."},
        "tr": {"name": "JWT Decoder", "tagline": "JWT'yi yapıştır, header ve payload'ı çöz. Tüm decode tarayıcında çalışır — token'lar sayfayı asla terk etmez.", "description": "Ücretsiz online JSON Web Token decoder. Header ve payload'ı çöz, expiry timestamp'leri doğrula, imzayı incele. Tarayıcında tamamen çevrimdışı çalışır."},
        "id": {"name": "JWT Decoder", "tagline": "Tempel JWT, decode header dan payload. Semua decoding terjadi di browser-mu — token tidak pernah meninggalkan halaman.", "description": "JWT decoder gratis. Tempel JSON Web Token apa pun dan lihat header dan payload yang di-decode dengan format yang dapat dibaca. Semua decoding lokal — token tidak pernah dikirim ke server kami atau server mana pun."},
        "vi": {"name": "JWT Decoder", "tagline": "Dán một JWT, decode header và payload. Toàn bộ decode xảy ra trong trình duyệt — token không bao giờ rời khỏi trang.", "description": "JWT decoder miễn phí trực tuyến. Dán token và xem header, payload và claim được giải mã. Toàn bộ decode chạy trong trình duyệt — token không bao giờ rời khỏi thiết bị của bạn."},
        "hi": {"name": "JWT Decoder", "tagline": "एक JWT paste करें ताकि उसके header और payload को decode किया जा सके। सारा decoding आपके browser में चलता है — tokens कभी page नहीं छोड़ते।", "description": "मुफ़्त ऑनलाइन JSON Web Token decoder. Header और payload decode करें, expiry timestamps की पुष्टि करें, signature का निरीक्षण करें। आपके browser में पूरी तरह offline काम करता है।"},
        "sk": {"name": 'JWT Decoder', "tagline": 'Vlož JWT a dekóduj jeho header a payload. Celé dekódovanie beží v prehliadači — tokeny nikdy neopustia stránku.', "description": 'Bezplatný online JWT decoder. Vlož JSON Web Token a dekóduje jeho header a payload do čitateľnej JSON formy. Beží lokálne — token nikdy neopustí prehliadač.'},
        "cs": {"name": 'JWT Decoder', "tagline": 'Vlož JWT a dekóduj jeho header a payload. Celé dekódování běží v prohlížeči — tokeny nikdy neopustí stránku.', "description": 'Zdarma online JWT decoder. Vlož JSON Web Token a dekóduje jeho header a payload do čitelné JSON podoby. Běží lokálně — token nikdy neopustí prohlížeč.'},
    },
    "body": """
<div class="tool-card">
  <label>JWT</label>
  <textarea id="jwt-in" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." spellcheck="false" oninput="jwtDecode()"></textarea>
  <div class="meta" id="jwt-summary"></div>
</div>
<div class="tool-card">
  <label>Header</label>
  <pre class="output" id="jwt-header">{LBL_NO_INPUT}</pre>
</div>
<div class="tool-card">
  <label>Payload</label>
  <pre class="output" id="jwt-payload">{LBL_NO_INPUT}</pre>
</div>
<div class="tool-card">
  <label>Signature (base64url, not verified)</label>
  <pre class="output" id="jwt-sig">{LBL_NO_INPUT}</pre>
  <div class="meta">This tool decodes only — it does not verify the signature against a key. Treat decoded payload as untrusted until verified.</div>
</div>
""",
    "script": """
<script>
function b64urlDecode(s){
  s = s.replace(/-/g,'+').replace(/_/g,'/');
  while (s.length % 4) s += '=';
  try {
    const bin = atob(s);
    // utf-8 decode
    const bytes = new Uint8Array(bin.length);
    for (let i=0;i<bin.length;i++) bytes[i] = bin.charCodeAt(i);
    return new TextDecoder('utf-8').decode(bytes);
  } catch(e){ return null; }
}
function jwtPretty(s){
  try { return JSON.stringify(JSON.parse(s), null, 2); }
  catch(e){ return s; }
}
function jwtDecode(){
  const tok = document.getElementById('jwt-in').value.trim();
  const hdr = document.getElementById('jwt-header');
  const pld = document.getElementById('jwt-payload');
  const sig = document.getElementById('jwt-sig');
  const sum = document.getElementById('jwt-summary');
  hdr.classList.remove('error'); pld.classList.remove('error'); sig.classList.remove('error');
  if (!tok){ hdr.textContent='{LBL_NO_INPUT}'; pld.textContent='{LBL_NO_INPUT}'; sig.textContent='{LBL_NO_INPUT}'; sum.textContent=''; return; }
  const parts = tok.split('.');
  if (parts.length !== 3){
    hdr.classList.add('error');
    hdr.textContent = '✗ Invalid JWT — expected 3 dot-separated parts (header.payload.signature)';
    pld.textContent = ''; sig.textContent = ''; sum.textContent = parts.length + ' parts found';
    return;
  }
  const h = b64urlDecode(parts[0]);
  const p = b64urlDecode(parts[1]);
  if (h === null){ hdr.classList.add('error'); hdr.textContent = '✗ Header is not valid base64url'; }
  else hdr.textContent = jwtPretty(h);
  if (p === null){ pld.classList.add('error'); pld.textContent = '✗ Payload is not valid base64url'; }
  else pld.textContent = jwtPretty(p);
  sig.textContent = parts[2] || '(empty signature)';
  // Summary: alg + exp/iat status
  let parts2 = [];
  try {
    const hj = JSON.parse(h);
    if (hj.alg) parts2.push('alg: ' + hj.alg);
  } catch(e){}
  try {
    const pj = JSON.parse(p);
    const now = Math.floor(Date.now()/1000);
    if (pj.exp){
      const d = new Date(pj.exp*1000);
      parts2.push('exp: ' + d.toISOString().replace('T',' ').slice(0,19) + 'Z' + (pj.exp < now ? ' ⚠ EXPIRED' : ''));
    }
    if (pj.iat){
      const d = new Date(pj.iat*1000);
      parts2.push('iat: ' + d.toISOString().replace('T',' ').slice(0,19) + 'Z');
    }
    if (pj.iss) parts2.push('iss: ' + pj.iss);
    if (pj.sub) parts2.push('sub: ' + pj.sub);
  } catch(e){}
  sum.textContent = parts2.join(' · ');
}
document.addEventListener('DOMContentLoaded', jwtDecode);
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('jwt-in');
  if (!input) return;
  input.value = e.detail.data;
  jwtDecode();
});
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A JWT (JSON Web Token) is three base64url-encoded parts joined by dots: <code>header.payload.signature</code>. The header and payload are JSON objects you can inspect; the signature proves the token wasn't tampered with after issuance. This tool decodes the first two parts so you can see what's inside without the noise of base64 — useful when debugging auth flows, expired sessions, or "which user is this token for, exactly?".</p>

<h3>When to use it</h3>
<ul>
  <li>Debugging an OAuth / OpenID Connect login that's failing — paste the access or ID token, see what the IdP actually issued.</li>
  <li>Confirming token expiry: the tool decodes <code>exp</code> as a real date and flags it if it's in the past.</li>
  <li>Sanity-checking custom claims a backend is asserting (roles, permissions, tenant IDs).</li>
  <li>Reading a token your library "rejected as invalid" to see whether the issue is structural, expiry, or signature.</li>
</ul>

<h3>Common claims</h3>
<ul>
  <li><code>iss</code> — issuer (who created the token)</li>
  <li><code>sub</code> — subject (the user/account it represents)</li>
  <li><code>aud</code> — audience (who should accept it)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>A decoded JWT is NOT a verified JWT.</strong> The signature isn't checked here — that requires the issuer's public key (RSA/EC) or shared secret (HMAC). Decoded contents tell you what the token <em>says</em>, not whether you should trust it. Always verify on the server before honouring claims.</li>
  <li><strong>Don't paste production tokens into anywhere.</strong> Anyone with a live JWT can impersonate the user until <code>exp</code>. The browser doesn't transmit it from this tool, but extensions, screen-recordings, and dev tools can. Use a fresh token from a test environment if you need to share.</li>
  <li><strong><code>alg: none</code> tokens are a known attack class.</strong> If a header has <code>alg: none</code> and your library accepts it, attackers can forge tokens. Reject this on the server.</li>
  <li><strong>Time skew matters.</strong> A token's <code>exp</code> is checked against the verifier's clock. Servers with drift fail tokens that look valid here.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um JWT (JSON Web Token) são três partes em base64url ligadas por pontos: <code>header.payload.signature</code>. O header e o payload são objetos JSON que você pode inspecionar; a signature prova que o token não foi adulterado depois de emitido. Esta ferramenta decodifica as duas primeiras partes pra você ver o que está dentro sem o barulho do base64 — útil pra debugar fluxos de auth, sessões expiradas ou "pra qual usuário é esse token, exatamente?".</p>

<h3>Quando usar</h3>
<ul>
  <li>Debugar um login OAuth / OpenID Connect que está falhando — cole o access ou ID token e veja o que o IdP de fato emitiu.</li>
  <li>Confirmar a expiração do token: a ferramenta decodifica <code>exp</code> como uma data real e marca se já passou.</li>
  <li>Checar custom claims que um backend está afirmando (roles, permissões, tenant IDs).</li>
  <li>Ler um token que sua biblioteca "rejeitou como inválido" pra ver se o problema é estrutural, de expiração ou de signature.</li>
</ul>

<h3>Claims comuns</h3>
<ul>
  <li><code>iss</code> — issuer (quem criou o token)</li>
  <li><code>sub</code> — subject (o usuário/conta que ele representa)</li>
  <li><code>aud</code> — audience (quem deveria aceitá-lo)</li>
  <li><code>exp</code> — expiração (timestamp Unix)</li>
  <li><code>iat</code> — issued-at (timestamp Unix)</li>
  <li><code>nbf</code> — not-valid-before (timestamp Unix)</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Um JWT decodificado NÃO é um JWT verificado.</strong> A signature não é checada aqui — isso exige a chave pública do issuer (RSA/EC) ou o segredo compartilhado (HMAC). O conteúdo decodificado te diz o que o token <em>diz</em>, não se você deve confiar nele. Sempre verifique no servidor antes de honrar claims.</li>
  <li><strong>Não cole tokens de produção em qualquer lugar.</strong> Qualquer um com um JWT vivo pode se passar pelo usuário até o <code>exp</code>. O browser não transmite o token a partir desta ferramenta, mas extensões, gravações de tela e dev tools podem. Use um token novo de um ambiente de teste se precisar compartilhar.</li>
  <li><strong>Tokens com <code>alg: none</code> são uma classe conhecida de ataque.</strong> Se um header tem <code>alg: none</code> e sua biblioteca aceita, atacantes podem forjar tokens. Rejeite isso no servidor.</li>
  <li><strong>Time skew importa.</strong> O <code>exp</code> de um token é checado contra o relógio do verificador. Servidores com drift falham tokens que parecem válidos aqui.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>JWT (JSON Web Token) to trzy części w base64url połączone kropkami: <code>header.payload.signature</code>. Header i payload to obiekty JSON, które możesz obejrzeć; signature dowodzi, że token nie został zmajstrowany po wystawieniu. To narzędzie dekoduje pierwsze dwie części, żebyś mógł zobaczyć, co siedzi w środku, bez szumu base64 — przydaje się przy debugowaniu flow auth, wygasłych sesji albo "do którego użytkownika ten token właściwie należy?".</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Debug logowania OAuth / OpenID Connect, które się sypie — wklej access albo ID token, zobacz, co IdP faktycznie wystawił.</li>
  <li>Potwierdzenie wygaśnięcia tokenu: narzędzie dekoduje <code>exp</code> jako prawdziwą datę i flaguje, jeśli minął.</li>
  <li>Sanity check custom claims, które backend asseruje (role, uprawnienia, tenant ID).</li>
  <li>Czytanie tokenu, który twoja biblioteka "odrzuciła jako nieprawidłowy", żeby zobaczyć, czy problem jest strukturalny, w wygaśnięciu, czy w signature.</li>
</ul>

<h3>Typowe claimsy</h3>
<ul>
  <li><code>iss</code> — issuer (kto utworzył token)</li>
  <li><code>sub</code> — subject (użytkownik/konto, które reprezentuje)</li>
  <li><code>aud</code> — audience (kto powinien go akceptować)</li>
  <li><code>exp</code> — wygaśnięcie (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Zdekodowany JWT to NIE zweryfikowany JWT.</strong> Signature nie jest tu sprawdzana — to wymaga klucza publicznego issuera (RSA/EC) albo współdzielonego sekretu (HMAC). Zdekodowana zawartość mówi ci, co token <em>twierdzi</em>, nie czy powinieneś mu ufać. Zawsze weryfikuj na serwerze, zanim uznasz claimsy.</li>
  <li><strong>Nie wklejaj tokenów produkcyjnych nigdzie.</strong> Każdy z żywym JWT może podszyć się pod użytkownika do <code>exp</code>. Przeglądarka go z tego narzędzia nie wysyła, ale rozszerzenia, screen recordingi i dev tools mogą podejrzeć. Użyj świeżego tokenu z testowego środowiska, jeśli musisz się podzielić.</li>
  <li><strong>Tokeny z <code>alg: none</code> to znana klasa ataków.</strong> Jeśli header ma <code>alg: none</code> i twoja biblioteka to akceptuje, atakujący mogą podrabiać tokeny. Odrzucaj to na serwerze.</li>
  <li><strong>Time skew ma znaczenie.</strong> <code>exp</code> tokenu jest sprawdzane przeciw zegarowi weryfikatora. Serwery z driftem padają na tokenach, które tu wyglądają na poprawne.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>JWT（JSON Web Token）は、ドットでつながれた 3 つの base64url パート <code>header.payload.signature</code> から成ります。ヘッダーとペイロードは検査可能な JSON オブジェクトで、署名は発行後に改ざんされていないことを示します。本ツールは前 2 つをデコードして、base64 のノイズを除いた中身を確認できるようにします。認証フローのデバッグ、セッションの期限切れ調査、「このトークンは結局どのユーザーのもの？」を素早く確認するのに役立ちます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>失敗している OAuth / OpenID Connect ログインのデバッグ — アクセストークンや ID トークンを貼り付けて、IdP が実際に何を発行したかを確認するとき。</li>
  <li>有効期限の確認 — <code>exp</code> を実際の日時にデコードし、過去日であればフラグを立てます。</li>
  <li>バックエンドが主張するカスタムクレーム（ロール、権限、テナント ID）の妥当性確認。</li>
  <li>ライブラリが「無効」と判断したトークンを読んで、構造の問題か、期限切れか、署名の問題かを切り分けるとき。</li>
</ul>

<h3>主なクレーム</h3>
<ul>
  <li><code>iss</code> — issuer（トークンを作ったエンティティ）</li>
  <li><code>sub</code> — subject（対象のユーザー／アカウント）</li>
  <li><code>aud</code> — audience（受け取るべき相手）</li>
  <li><code>exp</code> — 有効期限（Unix タイムスタンプ）</li>
  <li><code>iat</code> — 発行日時（Unix タイムスタンプ）</li>
  <li><code>nbf</code> — 有効開始前（Unix タイムスタンプ）</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>デコード済み JWT は、検証済み JWT ではありません。</strong> 署名はここでは検証していません。検証には発行元の公開鍵（RSA/EC）または共有シークレット（HMAC）が必要です。デコードした内容は「トークンが何を主張しているか」しか教えません。クレームを信用する前に必ずサーバー側で検証してください。</li>
  <li><strong>本番のトークンを貼り付けないこと。</strong> 有効な JWT を持つ者は <code>exp</code> までユーザーになりすませます。本ツールはブラウザから外に送信しませんが、拡張機能、画面録画、開発者ツールから漏れる可能性はあります。共有が必要なら、テスト環境の新しいトークンを使ってください。</li>
  <li><strong><code>alg: none</code> のトークンは既知の攻撃クラスです。</strong> ヘッダに <code>alg: none</code> があり、ライブラリがそれを受け入れると、攻撃者がトークンを偽造できます。サーバー側で必ず拒否してください。</li>
  <li><strong>クロックスキューに注意。</strong> <code>exp</code> は検証側の時計と比較されます。時刻ずれのあるサーバーでは、ここで有効に見えるトークンが落ちることがあります。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een JWT (JSON Web Token) bestaat uit drie base64url-encoded delen verbonden door dots: <code>header.payload.signature</code>. De header en payload zijn JSON-objects die je kunt inspecteren; de signature bewijst dat het token na issuance niet is geknoeid. Deze tool decodeert de eerste twee delen zodat je kunt zien wat erin zit zonder de ruis van base64 — nuttig bij het debuggen van auth-flows, verlopen sessions of "voor welke user is dit token precies?".</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een OAuth / OpenID Connect login debuggen die faalt — plak het access of ID token, zie wat de IdP daadwerkelijk uitgaf.</li>
  <li>Token-expiry bevestigen: de tool decodeert <code>exp</code> als echte datum en vlagt het als het in het verleden ligt.</li>
  <li>Sanity check op custom claims die een backend asseert (roles, permissions, tenant IDs).</li>
  <li>Een token lezen dat je library "rejected as invalid" om te zien of het issue structureel, expiry of signature is.</li>
</ul>

<h3>Gebruikelijke claims</h3>
<ul>
  <li><code>iss</code> — issuer (wie het token maakte)</li>
  <li><code>sub</code> — subject (de user/account die het representeert)</li>
  <li><code>aud</code> — audience (wie het zou moeten accepteren)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Een decoded JWT is GEEN verified JWT.</strong> De signature wordt hier niet gecheckt — dat vereist de public key van de issuer (RSA/EC) of shared secret (HMAC). Decoded contents vertellen je wat het token <em>zegt</em>, niet of je het moet vertrouwen. Verifieer altijd op de server voor je claims honoreert.</li>
  <li><strong>Plak production-tokens nergens.</strong> Iedereen met een live JWT kan de user impersoneren tot <code>exp</code>. De browser stuurt het vanaf deze tool niet door, maar extensies, screen-recordings en dev tools kunnen dat wel. Gebruik een fresh token uit een test-omgeving als je moet delen.</li>
  <li><strong><code>alg: none</code> tokens zijn een bekende aanvalsklasse.</strong> Als een header <code>alg: none</code> heeft en je library accepteert het, kunnen aanvallers tokens forgen. Wijs dit af op de server.</li>
  <li><strong>Time skew doet ertoe.</strong> Een token's <code>exp</code> wordt gecheckt tegen de klok van de verifier. Servers met drift falen tokens die hier valide lijken.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir JWT (JSON Web Token) nokta ile birleştirilmiş üç base64url-kodlanmış parçadır: <code>header.payload.signature</code>. Header ve payload, inceleyebileceğin JSON nesneleridir; imza, token'ın verildikten sonra değiştirilmediğini kanıtlar. Bu araç ilk iki kısmı çözer, böylece base64 gürültüsü olmadan içinde ne olduğunu görebilirsin — auth akışları, süresi dolmuş oturumlar veya "tam olarak hangi kullanıcı için bu token?" debug ederken kullanışlıdır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Başarısız olan bir OAuth / OpenID Connect girişini debug etme — access veya ID token'ı yapıştır, IdP'nin gerçekte ne verdiğini gör.</li>
  <li>Token süresinin dolduğunu doğrulama: araç <code>exp</code>'i gerçek bir tarih olarak çözer ve geçmişteyse işaretler.</li>
  <li>Bir backend'in iddia ettiği özel claim'lerin (roller, izinler, tenant ID'ler) sanity check'i.</li>
  <li>Kütüphanenin "geçersiz olarak reddettiği" bir token'ı okuyarak sorunun yapısal mı, expiry mi yoksa imza mı olduğunu görme.</li>
</ul>

<h3>Yaygın claim'ler</h3>
<ul>
  <li><code>iss</code> — issuer (token'ı kim oluşturdu)</li>
  <li><code>sub</code> — subject (temsil ettiği kullanıcı/hesap)</li>
  <li><code>aud</code> — audience (kim kabul etmeli)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Decoded bir JWT doğrulanmış bir JWT DEĞİLDİR.</strong> İmza burada kontrol edilmez — bu, veren tarafın açık anahtarını (RSA/EC) veya paylaşılan secret'ı (HMAC) gerektirir. Çözülmüş içerik sana token'ın ne <em>dediğini</em> söyler, ona güvenip güvenmemen gerektiğini değil. Claim'leri onurlandırmadan önce sunucuda her zaman doğrula.</li>
  <li><strong>Production token'larını hiçbir yere yapıştırma.</strong> Canlı bir JWT olan herkes <code>exp</code>'e kadar kullanıcıyı taklit edebilir. Tarayıcı bu araçtan iletmez ama uzantılar, ekran kayıtları ve dev tools yapabilir. Paylaşman gerekiyorsa test ortamından taze bir token kullan.</li>
  <li><strong><code>alg: none</code> token'ları bilinen bir saldırı sınıfıdır.</strong> Bir header'da <code>alg: none</code> varsa ve kütüphanen kabul ediyorsa, saldırganlar token sahteleyebilir. Sunucuda reddet.</li>
  <li><strong>Zaman kayması önemlidir.</strong> Bir token'ın <code>exp</code>'i doğrulayıcının saatine karşı kontrol edilir. Kayan saatler burada geçerli görünen token'ları başarısız yapar.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Sebuah JWT (JSON Web Token) terdiri dari tiga bagian ter-encode base64url yang disambung dengan titik: <code>header.payload.signature</code>. Header dan payload adalah JSON object yang bisa kamu inspect; signature membuktikan token tidak diutak-atik setelah diterbitkan. Tool ini mendecode dua bagian pertama sehingga kamu bisa lihat isinya tanpa kebisingan base64 — berguna saat men-debug auth flow, session yang kadaluarsa, atau "token ini untuk user yang mana sebenarnya?".</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Men-debug login OAuth / OpenID Connect yang gagal — paste access atau ID token, lihat apa yang sebenarnya diterbitkan IdP.</li>
  <li>Mengkonfirmasi expiry token: tool ini mendecode <code>exp</code> sebagai tanggal asli dan menandainya jika sudah lewat.</li>
  <li>Sanity-check custom claim yang di-assert backend (role, permission, tenant ID).</li>
  <li>Membaca token yang "ditolak sebagai invalid" oleh library kamu untuk melihat apakah masalahnya struktural, expiry, atau signature.</li>
</ul>

<h3>Claim umum</h3>
<ul>
  <li><code>iss</code> — issuer (siapa yang membuat token)</li>
  <li><code>sub</code> — subject (user/account yang diwakili)</li>
  <li><code>aud</code> — audience (siapa yang seharusnya menerima)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>JWT yang di-decode BUKAN JWT yang sudah diverifikasi.</strong> Signature tidak dicek di sini — itu butuh public key issuer (RSA/EC) atau shared secret (HMAC). Konten yang sudah di-decode hanya memberitahu kamu apa yang token <em>katakan</em>, bukan apakah kamu harus mempercayainya. Selalu verifikasi di server sebelum menghormati claim.</li>
  <li><strong>Jangan paste token production di mana pun.</strong> Siapa pun yang punya JWT yang masih hidup bisa menyamar sebagai user sampai <code>exp</code>. Browser tidak mengirimnya keluar dari tool ini, tapi extension, screen-recording, dan dev tools bisa. Pakai token baru dari environment test jika kamu harus berbagi.</li>
  <li><strong>Token <code>alg: none</code> adalah kelas serangan yang dikenal.</strong> Kalau sebuah header punya <code>alg: none</code> dan library kamu menerimanya, attacker bisa memalsukan token. Tolak ini di server.</li>
  <li><strong>Time skew itu penting.</strong> <code>exp</code> sebuah token dicek terhadap jam verifier. Server yang drift akan menolak token yang di sini terlihat valid.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Một JWT (JSON Web Token) gồm ba phần được phân tách bằng dấu chấm: header.payload.signature — mỗi phần là base64url-encoded JSON (signature là binary). Tool này tách ba phần, decode JSON, và hiển thị header và payload với syntax highlighting. Signature được hiển thị nguyên trạng (không thể verify mà không có key).</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Debug auth flow và muốn xem claim trong token (sub, exp, scope, custom claim).</li>
  <li>Inspect provider token (Google, Auth0, Cognito) để xem cấu trúc của nó.</li>
  <li>Confirm token chưa hết hạn — claim <code>exp</code> là epoch seconds.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>JWT không phải mã hóa, chỉ là encode + sign.</strong> Bất kỳ ai cũng có thể đọc payload. Đừng bao giờ đặt secret hoặc PII vào claim.</li>
  <li><strong>Signature verification cần key.</strong> Tool này decode nhưng không verify. Để verify, bạn cần public key của issuer hoặc shared secret.</li>
  <li><strong>JWT không phải session.</strong> Token có claim hết hạn nhưng không thể revoke trừ khi backend của bạn maintain danh sách revocation. Đối với session, dùng cookie.</li>
  <li><strong>Token chạy hoàn toàn local trong tool này.</strong> Không có gì được upload — nhưng đừng paste token sản xuất vào tool ngẫu nhiên dù sao đi nữa.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>एक JWT (JSON Web Token) तीन base64url-encoded हिस्से हैं जो dots से जुड़े हैं: <code>header.payload.signature</code>. Header और payload JSON objects हैं जिनकी जाँच की जा सकती है; signature यह सिद्ध करता है कि issuance के बाद token में छेड़छाड़ नहीं हुई। यह टूल पहले दो हिस्सों को decode करता है ताकि आप base64 के शोर के बिना अंदर क्या है यह देख सकें — auth flows, expired sessions, या "यह token वास्तव में किस user के लिए है?" debug करते समय उपयोगी।</p>

<h3>कब इस्तेमाल करें</h3>
<ul>
  <li>एक OAuth / OpenID Connect login को debug करना जो fail हो रहा है — access या ID token paste करें, देखें IdP ने वास्तव में क्या जारी किया।</li>
  <li>Token expiry की पुष्टि करना: टूल <code>exp</code> को असली date के रूप में decode करता है और यदि वह अतीत में है तो flag लगाता है।</li>
  <li>Backend द्वारा assert किए जा रहे custom claims की जाँच करना (roles, permissions, tenant IDs)।</li>
  <li>एक token पढ़ना जिसे आपकी library ने "invalid" बताया है ताकि देखा जा सके कि समस्या structural है, expiry है, या signature की है।</li>
</ul>

<h3>आम claims</h3>
<ul>
  <li><code>iss</code> — issuer (किसने token बनाया)</li>
  <li><code>sub</code> — subject (वह user/account जिसे यह represent करता है)</li>
  <li><code>aud</code> — audience (किसे इसे accept करना चाहिए)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>एक decoded JWT verified JWT नहीं है।</strong> Signature यहाँ check नहीं की जाती — इसके लिए issuer की public key (RSA/EC) या shared secret (HMAC) चाहिए। Decoded contents आपको बताते हैं कि token <em>क्या कहता है</em>, यह नहीं कि आपको उस पर भरोसा करना चाहिए या नहीं। Claims को सम्मान देने से पहले हमेशा server पर verify करें।</li>
  <li><strong>Production tokens कहीं भी paste न करें।</strong> Live JWT वाला कोई भी व्यक्ति <code>exp</code> तक user की पहचान धारण कर सकता है। Browser इसे इस टूल से transmit नहीं करता, लेकिन extensions, screen-recordings, और dev tools कर सकते हैं। यदि आपको साझा करना है तो test environment से एक fresh token का उपयोग करें।</li>
  <li><strong><code>alg: none</code> tokens एक ज्ञात attack class हैं।</strong> यदि किसी header में <code>alg: none</code> है और आपकी library इसे accept करती है, तो हमलावर tokens forge कर सकते हैं। इसे server पर reject करें।</li>
  <li><strong>Time skew मायने रखता है।</strong> Token का <code>exp</code> verifier की घड़ी के विरुद्ध check किया जाता है। Drift वाले servers ऐसे tokens fail कर देते हैं जो यहाँ valid दिखते हैं।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>JWT (JSON Web Token) je trojica base64url-encoded častí oddelených bodkami: <code>header.payload.signature</code>. Tento nástroj rozdelí token, dekóduje header a payload a zobrazí ich ako čitateľný JSON. Beží lokálne — tvoj token nikdy neopustí prehliadač.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>Debug auth flow — chceš vidieť, čo presne backend posiela v JWT.</li>
  <li>Kontrola, kedy token expiruje (<code>exp</code> claim).</li>
  <li>Ladenie OIDC / OAuth identity flow.</li>
  <li>Audit, či token obsahuje žiadne PII, ktoré by tam nemali byť.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>JWT NIE je šifrovaný.</strong> Payload je len base64url-encoded JSON — ktokoľvek vie dekódovať. NIKDY do JWT nevkladaj heslá ani tajomstvá.</li>
  <li><strong>Tento decoder neoveruje podpis.</strong> Na to potrebuješ public key a knižnicu (jose, jsonwebtoken).</li>
  <li><strong>Algoritmus „none".</strong> Bezpečnostná diera v starých implementáciách — nikdy neakceptuj.</li>
  <li><strong>Expiry je v sekundách Unix epoch.</strong> Nie milisekundách. Pozri <code>exp</code> claim cez timestamp converter.</li>
  <li><strong>Token z URL.</strong> Base64url v URL: pozor na URL-encoded <code>%</code> escape pri kopírovaní.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>JWT (JSON Web Token) je trojice base64url-encoded částí oddělených tečkami: <code>header.payload.signature</code>. Tenhle nástroj rozdělí token, dekóduje header a payload a zobrazí je jako čitelný JSON. Běží lokálně — tvůj token nikdy neopustí prohlížeč.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>Debug auth flow — chceš vidět, co přesně backend posílá v JWT.</li>
  <li>Kontrola, kdy token expiruje (<code>exp</code> claim).</li>
  <li>Ladění OIDC / OAuth identity flow.</li>
  <li>Audit, jestli token neobsahuje žádné PII, které by tam být neměly.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>JWT NENÍ šifrovaný.</strong> Payload je jen base64url-encoded JSON — kdokoli umí dekódovat. NIKDY do JWT nevkládej hesla ani tajemství.</li>
  <li><strong>Tenhle decoder neověřuje podpis.</strong> Na to potřebuješ public key a knihovnu (jose, jsonwebtoken).</li>
  <li><strong>Algoritmus „none".</strong> Bezpečnostní díra ve starých implementacích — nikdy neakceptuj.</li>
  <li><strong>Expiry je v sekundách Unix epoch.</strong> Ne milisekundách. Podívej se na <code>exp</code> claim přes timestamp converter.</li>
  <li><strong>Token z URL.</strong> Base64url v URL: pozor na URL-encoded <code>%</code> escape při kopírování.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "json-formatter", "hash-generator"],
    "howto": {"flow": "transform", "action": "decode",  "noun": "JWT"},
}
