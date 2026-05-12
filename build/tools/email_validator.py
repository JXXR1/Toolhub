TOOL = {
    "slug": "email-validator",
    "category": "validation",
    "icon": "✉",
    "tags": ["email", "validate", "rfc", "syntax", "mx", "domain"],
    "i18n": {
        "en": {
            "name": "Email Validator",
            "tagline": "Check whether an email address is syntactically valid (RFC 5322 friendly), with breakdown of local part, domain, and common pitfalls.",
            "description": "Free online email validator. RFC 5322-aware syntax check, local-part and domain analysis, disposable-domain hint, and length verification.",
        },
        "de": {"name": "E-Mail-Validator", "tagline": "Prüfe, ob eine E-Mail-Adresse syntaktisch korrekt ist (RFC 5322), mit Aufschlüsselung von Local-Part und Domain.", "description": "Kostenloser E-Mail-Validator. RFC-5322-kompatible Syntaxprüfung, Local-Part- und Domain-Analyse, Hinweis auf Wegwerfdomains und Längenprüfung."},
        "es": {"name": "Validador de Email", "tagline": "Comprueba si una dirección de email es sintácticamente válida (RFC 5322), con desglose de la parte local y el dominio.", "description": "Validador de email en línea gratuito. Verificación sintáctica compatible con RFC 5322, análisis de parte local y dominio, aviso de dominios desechables."},
        "fr": {"name": "Validateur d'Email", "tagline": "Vérifiez si une adresse email est syntaxiquement valide (RFC 5322), avec analyse de la partie locale et du domaine.", "description": "Validateur d'email gratuit en ligne. Vérification syntaxique compatible RFC 5322, analyse de la partie locale et du domaine, alerte domaines jetables."},
        "it": {"name": "Validatore Email", "tagline": "Verifica se un indirizzo email è sintatticamente valido (RFC 5322), con analisi della parte locale e del dominio.", "description": "Validatore email online gratuito. Verifica sintattica conforme RFC 5322, analisi della parte locale e del dominio, segnalazione domini usa-e-getta."},
        "pt": {"name": "Validador de Email", "tagline": "Verifique se um endereço de email é sintaticamente válido (compatível com RFC 5322), com análise da parte local, domínio e armadilhas comuns.", "description": "Validador de email online gratuito. Checagem de sintaxe alinhada à RFC 5322, análise da parte local e do domínio, alerta de domínios descartáveis e verificação de comprimento."},
        "pl": {"name": "Walidator Email", "tagline": "Sprawdź, czy adres email jest poprawny składniowo (zgodny z RFC 5322), z rozbiciem na local part, domenę i typowe pułapki.", "description": "Darmowy online walidator emaili. Walidacja składni zgodna z RFC 5322, analiza local part i domeny, oznaczanie disposable domains i weryfikacja długości."},
        "ja": {"name": "メールアドレス検証ツール", "tagline": "メールアドレスが構文的に有効か（RFC 5322 準拠）を確認。ローカル部・ドメイン・よくある落とし穴も解析。", "description": "オンライン無料のメールアドレス検証ツール。RFC 5322 準拠の構文チェック、ローカル部とドメインの解析、使い捨てドメインの検出、長さ検証を行います。"},
        "nl": {"name": "Email-validator", "tagline": "Check of een emailadres syntactisch geldig is (RFC 5322-friendly), met breakdown van local part, domain en veelvoorkomende valkuilen.", "description": "Gratis online email-validator. RFC 5322-aware syntax check, analyse van local part en domain, disposable-domain hint en lengtecontrole."},
        "tr": {"name": "E-posta Doğrulayıcı", "tagline": "Bir e-posta adresinin sözdizimsel olarak geçerli olup olmadığını kontrol et (RFC 5322 uyumlu); local part, domain ve yaygın hataları ayrıştırır.", "description": "Ücretsiz online e-posta doğrulayıcı. RFC 5322 uyumlu sözdizimi kontrolü, local-part ve domain analizi, geçici domain ipucu ve uzunluk doğrulaması."},
        "id": {"name": "Validator Email", "tagline": "Cek apakah alamat email valid secara sintaks (RFC 5322-compliant); mengurai local part, domain, dan kesalahan umum.", "description": "Validator email gratis. Cek apakah alamat email valid secara sintaks per RFC 5322 dan urai local part, domain, dan TLD. Menandai typo umum (gmial.com, gmal.com) dan domain yang kemungkinan typo."},
        "vi": {"name": "Xác thực Email", "tagline": "Kiểm tra xem một địa chỉ email có hợp lệ về cú pháp không (tuân thủ RFC 5322); phân tích phần local, domain và các lỗi thường gặp.", "description": "Trình xác thực email miễn phí trực tuyến. Kiểm tra xem một địa chỉ có cú pháp hợp lệ theo RFC 5322 không, tách phần local và domain, và đánh dấu các vấn đề thường gặp như khoảng trắng, ký tự không hợp lệ hoặc TLD bị thiếu."},
    },
    "body": """
<div class="tool-card">
  <label>Email address</label>
  <input type="text" id="ev-input" oninput="evRun()" placeholder="hello@example.com" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">Or paste a list (one per line) below to bulk-check.</div>
  <textarea id="ev-bulk" oninput="evRun()" placeholder="Optional: bulk check, one address per line" spellcheck="false" style="margin-top:0.6rem"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ev-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.ev-result{display:grid;gap:0.5rem}
.ev-row{display:grid;grid-template-columns:140px 1fr;gap:0.6rem;align-items:center;padding:0.45rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-size:0.88rem}
.ev-row .lbl{color:var(--text-muted);font-size:0.78rem;font-family:ui-monospace,monospace}
.ev-pass{color:#10b981;font-weight:600}
.ev-fail{color:#ef4444;font-weight:600}
.ev-warn{color:#f59e0b;font-weight:600}
.ev-bulk-row{display:grid;grid-template-columns:1fr 90px;gap:0.5rem;padding:0.4rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;font-family:ui-monospace,monospace;font-size:0.85rem;margin-bottom:0.3rem;word-break:break-all}
</style>
<script>
const EV_DISPOSABLE = new Set(['mailinator.com','tempmail.com','10minutemail.com','guerrillamail.com','yopmail.com','throwawaymail.com','trashmail.com','maildrop.cc','sharklasers.com','dispostable.com','fakeinbox.com','getnada.com']);
const EV_LOCAL_RX = /^[A-Za-z0-9!#$%&'*+\\-/=?^_`{|}~]+(\\.[A-Za-z0-9!#$%&'*+\\-/=?^_`{|}~]+)*$/;
const EV_DOMAIN_LABEL_RX = /^[A-Za-z0-9](?:[A-Za-z0-9\\-]{0,61}[A-Za-z0-9])?$/;
function evCheck(addr){
  const r = {addr, valid:false, problems:[], warnings:[]};
  if(!addr) return r;
  if(addr.length > 254) r.problems.push('Total length over 254 chars (RFC 5321 limit)');
  const at = addr.lastIndexOf('@');
  if(at <= 0 || at === addr.length-1){ r.problems.push('Missing local part or domain (no @ separator)'); return r; }
  const local = addr.slice(0, at);
  const domain = addr.slice(at+1);
  r.local = local; r.domain = domain;
  if(local.length > 64) r.problems.push('Local part over 64 chars (RFC 5321 limit)');
  if(local.startsWith('.') || local.endsWith('.')) r.problems.push('Local part cannot start or end with a dot');
  if(local.includes('..')) r.problems.push('Local part contains consecutive dots');
  if(!EV_LOCAL_RX.test(local) && !(local.startsWith('"') && local.endsWith('"'))) r.problems.push('Local part has invalid characters');
  if(!domain.includes('.')) r.problems.push('Domain has no TLD (no dot)');
  const labels = domain.split('.');
  for(const lab of labels){
    if(!lab){ r.problems.push('Empty label in domain (consecutive dots?)'); continue; }
    if(lab.length > 63){ r.problems.push('Domain label "'+lab+'" over 63 chars'); continue; }
    if(!EV_DOMAIN_LABEL_RX.test(lab)) r.problems.push('Invalid domain label "'+lab+'"');
  }
  const tld = labels[labels.length-1] || '';
  if(tld.length < 2) r.problems.push('TLD too short');
  if(/^\\d+$/.test(tld)) r.problems.push('TLD cannot be all-numeric');
  if(EV_DISPOSABLE.has(domain.toLowerCase())) r.warnings.push('Disposable / throwaway domain');
  if(domain.toLowerCase()==='gmail.com' && local.includes('+')) r.warnings.push('Gmail "+" alias — routes to base address');
  r.valid = r.problems.length === 0;
  return r;
}
function evRow(label, val){return `<div class="ev-row"><div class="lbl">${label}</div><div>${val}</div></div>`}
function evRender(c){
  if(!c.local && !c.domain) return `<div class="ev-result">${evRow('Status','<span class="ev-fail">'+c.problems.join('; ')+'</span>')}</div>`;
  const verdict = c.valid ? '<span class="ev-pass">✓ Syntactically valid</span>' : '<span class="ev-fail">✗ Invalid</span>';
  let html = '<div class="ev-result">';
  html += evRow('Verdict', verdict);
  html += evRow('Local part', '<code>'+c.local+'</code>');
  html += evRow('Domain', '<code>'+c.domain+'</code>');
  if(c.problems.length) html += evRow('Problems', '<span class="ev-fail">'+c.problems.join('<br>')+'</span>');
  if(c.warnings.length) html += evRow('Notes', '<span class="ev-warn">'+c.warnings.join('<br>')+'</span>');
  html += '</div>';
  return html;
}
function evRun(){
  const single = document.getElementById('ev-input').value.trim();
  const bulk = document.getElementById('ev-bulk').value.trim();
  const out = document.getElementById('ev-out');
  out.classList.remove('error');
  if(!single && !bulk){ out.textContent = '{LBL_NO_INPUT}'; return; }
  if(single && !bulk){
    out.innerHTML = evRender(evCheck(single));
    return;
  }
  const list = (bulk || single).split(/\\r?\\n/).map(s=>s.trim()).filter(Boolean);
  let html = '';
  let pass = 0, fail = 0;
  for(const a of list){
    const c = evCheck(a);
    if(c.valid) pass++; else fail++;
    const cls = c.valid ? 'ev-pass' : 'ev-fail';
    html += `<div class="ev-bulk-row"><div>${a}</div><div class="${cls}">${c.valid?'✓ valid':'✗ invalid'}</div></div>`;
  }
  out.innerHTML = `<div class="meta" style="margin-bottom:0.6rem">${pass} valid · ${fail} invalid · ${list.length} total</div>` + html;
}
document.addEventListener('DOMContentLoaded', evRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Most "email validators" are a one-line regex that approves <code>not@an.email</code> and rejects <code>edge@case.io</code>. This tool runs the structural checks RFC 5321 / 5322 actually require — local part charset, dot rules, label lengths, TLD shape, hard length limits — plus a disposable-domain hint. It tells you whether an address is <em>well-formed</em>; it doesn't tell you whether the mailbox exists (that needs a server-side MX/SMTP probe).</p>

<h3>When to use it</h3>
<ul>
  <li>Pre-flighting a list of email addresses before piping it into a paid validation API or mass-mailer (catches typos for free, saves credits).</li>
  <li>Building a signup form that rejects obvious garbage at the field level.</li>
  <li>Auditing a CSV of contacts to find typos before importing.</li>
  <li>Checking whether an address that "looks weird" (international TLD, plus-addressing, sub-addressing) is actually allowed.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Syntactically valid ≠ deliverable.</strong> <code>does-not-exist@gmail.com</code> passes every structural check. Real verification needs the MX server's response. Use this as a first-line filter, not a confidence signal.</li>
  <li><strong>Plus addressing is allowed.</strong> <code>name+tag@gmail.com</code> is valid and routes to <code>name@gmail.com</code> — don't strip it; it's a feature.</li>
  <li><strong>Internationalised email (IDN).</strong> <code>用户@例.中国</code> is technically valid per RFC 6530 but not yet broadly supported by SMTP servers. This tool follows the conservative ASCII rules; loosen if you genuinely need IDN.</li>
  <li><strong>Disposable-domain detection is hint-only.</strong> The list is necessarily incomplete and any flagged domain might still be a real user.</li>
  <li><strong>Don't reject case differences.</strong> Local parts are technically case-sensitive per RFC 5321; in practice every modern provider treats them as case-insensitive. Don't lowercase in storage.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>A maioria dos "validadores de email" é uma regex de uma linha que aprova <code>not@an.email</code> e rejeita <code>edge@case.io</code>. Esta ferramenta roda as checagens estruturais que a RFC 5321 / 5322 realmente exigem — charset da parte local, regras de pontos, comprimentos de labels, formato de TLD, limites duros de tamanho — mais um alerta de domínio descartável. Diz se um endereço é <em>bem formado</em>; não diz se a caixa de email existe (isso requer um probe MX/SMTP no servidor).</p>

<h3>Quando usar</h3>
<ul>
  <li>Pré-checar uma lista de emails antes de jogar numa API paga de validação ou mass-mailer (pega erros de digitação de graça, economiza créditos).</li>
  <li>Construir um formulário de cadastro que rejeita lixo óbvio no nível do campo.</li>
  <li>Auditar um CSV de contatos para achar erros de digitação antes de importar.</li>
  <li>Verificar se um endereço que "parece estranho" (TLD internacional, plus-addressing, sub-addressing) é realmente permitido.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Sintaticamente válido ≠ entregável.</strong> <code>does-not-exist@gmail.com</code> passa em toda checagem estrutural. Verificação real precisa da resposta do servidor MX. Use isto como filtro de primeira linha, não como sinal de confiança.</li>
  <li><strong>Plus addressing é permitido.</strong> <code>nome+tag@gmail.com</code> é válido e roteia para <code>nome@gmail.com</code> — não retire; é uma feature.</li>
  <li><strong>Email internacionalizado (IDN).</strong> <code>用户@例.中国</code> é tecnicamente válido pela RFC 6530 mas ainda não é amplamente suportado por servidores SMTP. Esta ferramenta segue as regras conservadoras ASCII; afrouxe se realmente precisar de IDN.</li>
  <li><strong>Detecção de domínio descartável é só uma dica.</strong> A lista é necessariamente incompleta e qualquer domínio sinalizado pode ainda ser de um usuário real.</li>
  <li><strong>Não rejeite diferenças de caixa.</strong> Partes locais são tecnicamente case-sensitive pela RFC 5321; na prática todo provider moderno trata como case-insensitive. Não lowercase no storage.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Większość "walidatorów emaili" to jednoliniowy regex, który przepuszcza <code>not@an.email</code> i odrzuca <code>edge@case.io</code>. To narzędzie odpala strukturalne sprawdzenia, których faktycznie wymaga RFC 5321 / 5322 — charset local part, reguły kropek, długości labeli, kształt TLD, twarde limity długości — plus podpowiedź disposable domain. Mówi, czy adres jest <em>dobrze sformatowany</em>; nie mówi, czy skrzynka istnieje (do tego potrzeba serwerowego probe MX/SMTP).</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Pre-flight listy adresów email zanim przepchniesz ją przez płatne API walidacji albo mass-mailera (łapie literówki za darmo, oszczędza kredyty).</li>
  <li>Budowa formularza rejestracji odrzucającego oczywisty syf na poziomie pola.</li>
  <li>Audyt CSV-a kontaktów w poszukiwaniu literówek przed importem.</li>
  <li>Sprawdzenie, czy adres, który "wygląda dziwnie" (międzynarodowy TLD, plus-addressing, sub-addressing), faktycznie jest dozwolony.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Składniowo poprawny ≠ dostarczalny.</strong> <code>does-not-exist@gmail.com</code> przechodzi każde strukturalne sprawdzenie. Prawdziwa weryfikacja wymaga odpowiedzi serwera MX. Używaj tego jako filtra pierwszej linii, nie jako sygnału pewności.</li>
  <li><strong>Plus addressing jest dozwolony.</strong> <code>imie+tag@gmail.com</code> jest poprawny i routuje do <code>imie@gmail.com</code> — nie wycinaj go; to feature.</li>
  <li><strong>Międzynarodowy email (IDN).</strong> <code>用户@例.中国</code> jest technicznie poprawny wg RFC 6530, ale nadal nie jest powszechnie wspierany przez serwery SMTP. To narzędzie trzyma się konserwatywnych zasad ASCII; poluzuj, jeśli naprawdę potrzebujesz IDN.</li>
  <li><strong>Wykrywanie disposable domain to tylko podpowiedź.</strong> Lista jest siłą rzeczy niekompletna, a oznaczona domena może i tak być prawdziwym użytkownikiem.</li>
  <li><strong>Nie odrzucaj różnic wielkości liter.</strong> Local part jest technicznie case-sensitive wg RFC 5321; w praktyce każdy nowoczesny provider traktuje go case-insensitive. Nie zamieniaj na lowercase przy zapisie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>大半の「メール検証ツール」は <code>not@an.email</code> を通し、<code>edge@case.io</code> を弾く 1 行の正規表現にすぎません。本ツールは RFC 5321 / 5322 が実際に求める構造的チェック（ローカル部の文字種、ドット規則、ラベル長、TLD の形、絶対長制限）に加え、使い捨てドメインの検出も行います。アドレスが<em>整形式</em>かどうかは判定できますが、メールボックスが実在するかは別問題で、それにはサーバー側の MX/SMTP プローブが必要です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>有料の検証 API やメール一斉送信サービスに送る前に、リストを事前チェックしたい（タイポを無料で捕まえてクレジット節約）。</li>
  <li>サインアップフォームで明らかなゴミ入力をフィールド単位で弾きたい。</li>
  <li>連絡先 CSV をインポート前に監査して、タイポを発見したい。</li>
  <li>「変に見える」アドレス（国際 TLD、プラスアドレッシング、サブアドレッシング）が本当に有効なのかを確かめたい。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>構文的に有効 ≠ 配信可能。</strong> <code>does-not-exist@gmail.com</code> は構造チェックを全部通ります。本物の検証には MX サーバーの応答が必要です。本ツールはあくまで一次フィルターとして使い、配信可否の根拠にはしないでください。</li>
  <li><strong>プラスアドレッシングは有効です。</strong> <code>name+tag@gmail.com</code> は有効で、<code>name@gmail.com</code> にルーティングされます。剥がさないでください。これは仕様の機能です。</li>
  <li><strong>国際化メール（IDN）。</strong> <code>用户@例.中国</code> は RFC 6530 上は有効ですが、SMTP サーバーの対応はまだ広くありません。本ツールは保守的な ASCII ルールに従います。本当に IDN が必要な場合は緩めてください。</li>
  <li><strong>使い捨てドメイン検出はあくまでヒントです。</strong> リストは性質上不完全ですし、フラグが立ったドメインでも実在ユーザーである可能性があります。</li>
  <li><strong>大文字小文字の差で弾かないでください。</strong> RFC 5321 上はローカル部は case-sensitive ですが、実際のプロバイダはすべて case-insensitive に扱います。保存時に小文字化はしないでください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>De meeste "email-validators" zijn een one-line regex die <code>not@an.email</code> goedkeurt en <code>edge@case.io</code> afwijst. Deze tool draait de structurele checks die RFC 5321 / 5322 daadwerkelijk vereisen — local-part charset, dot-regels, label-lengtes, TLD-vorm, harde lengtelimieten — plus een disposable-domain hint. Hij vertelt je of een adres <em>well-formed</em> is; hij vertelt je niet of de mailbox bestaat (daarvoor is een server-side MX/SMTP-probe nodig).</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een lijst emailadressen pre-flighten voor je ze door een betaalde validation-API of mass-mailer pompt (vangt typo's gratis, spaart credits).</li>
  <li>Een signup-form bouwen die overduidelijke onzin op veldniveau afwijst.</li>
  <li>Een CSV met contacten auditen om typo's te vinden voor importeren.</li>
  <li>Checken of een adres dat "raar lijkt" (internationale TLD, plus-addressing, sub-addressing) eigenlijk toegestaan is.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Syntactisch geldig ≠ deliverable.</strong> <code>does-not-exist@gmail.com</code> passeert elke structurele check. Echte verificatie vereist de respons van de MX-server. Gebruik dit als eerste filter, niet als zekerheidssignaal.</li>
  <li><strong>Plus-addressing is toegestaan.</strong> <code>naam+tag@gmail.com</code> is geldig en routeert naar <code>naam@gmail.com</code> — strip het niet; het is een feature.</li>
  <li><strong>Internationalised email (IDN).</strong> <code>用户@例.中国</code> is technisch geldig volgens RFC 6530 maar nog niet breed ondersteund door SMTP-servers. Deze tool volgt de conservatieve ASCII-regels; versoepel als je echt IDN nodig hebt.</li>
  <li><strong>Disposable-domain detectie is hint-only.</strong> De lijst is per definitie incompleet en een gevlagde domain kan nog steeds een echte gebruiker zijn.</li>
  <li><strong>Wijs case-verschillen niet af.</strong> Local parts zijn technisch case-sensitive volgens RFC 5321; in de praktijk behandelt elke moderne provider ze als case-insensitive. Maak ze niet lowercase bij opslag.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Çoğu "e-posta doğrulayıcı" <code>not@an.email</code>'i onaylayan ve <code>edge@case.io</code>'yu reddeden tek satırlık bir regex'tir. Bu araç RFC 5321 / 5322'nin gerçekten gerektirdiği yapısal kontrolleri yapar — local part charset, nokta kuralları, etiket uzunlukları, TLD şekli, sert uzunluk sınırları — artı bir geçici domain ipucu. Adresin <em>iyi biçimli</em> olup olmadığını söyler; mailbox'ın var olup olmadığını söylemez (bu sunucu tarafı MX/SMTP probe gerektirir).</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Ücretli bir doğrulama API'sine veya mass-mailer'a göndermeden önce bir e-posta listesini önden kontrol etme (ücretsiz yazım hatalarını yakalar, kredilerden tasarruf eder).</li>
  <li>Alan seviyesinde bariz çöpü reddeden bir kayıt formu kurma.</li>
  <li>İçe aktarmadan önce yazım hatalarını bulmak için bir CSV kişi listesi denetleme.</li>
  <li>"Tuhaf görünen" bir adresin (uluslararası TLD, plus-addressing, sub-addressing) gerçekten izinli olup olmadığını kontrol etme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Sözdizimsel olarak geçerli ≠ teslim edilebilir.</strong> <code>does-not-exist@gmail.com</code> her yapısal kontrolü geçer. Gerçek doğrulama MX sunucusunun yanıtını gerektirir. Bunu güven sinyali değil, ilk hat filtre olarak kullan.</li>
  <li><strong>Plus addressing izinlidir.</strong> <code>name+tag@gmail.com</code> geçerlidir ve <code>name@gmail.com</code>'a yönlenir — temizleme; bir özelliktir.</li>
  <li><strong>Internationalised email (IDN).</strong> <code>用户@例.中国</code> teknik olarak RFC 6530'a göre geçerlidir ama SMTP sunucuları tarafından henüz geniş çapta desteklenmez. Bu araç muhafazakar ASCII kurallarını izler; gerçekten IDN gerekliyse gevşet.</li>
  <li><strong>Geçici domain tespiti sadece ipucu.</strong> Liste zorunlu olarak eksiktir ve işaretlenmiş herhangi bir domain hâlâ gerçek bir kullanıcı olabilir.</li>
  <li><strong>Case farklarını reddetme.</strong> Local part'lar RFC 5321'e göre teknik olarak case-sensitive'dir; pratikte her modern sağlayıcı case-insensitive ele alır. Depolamada küçük harfe çevirme.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Sebagian besar "email validator" hanyalah regex satu baris yang meloloskan <code>not@an.email</code> dan menolak <code>edge@case.io</code>. Tool ini menjalankan pengecekan struktural yang sebenarnya diwajibkan oleh RFC 5321 / 5322 — charset local part, aturan titik, panjang label, bentuk TLD, batas hard length — plus hint disposable domain. Tool ini memberitahu apakah sebuah alamat <em>well-formed</em>; tool ini tidak memberitahu apakah mailbox-nya ada (itu butuh probe MX/SMTP sisi server).</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Pre-flight daftar alamat email sebelum diumpankan ke API validasi berbayar atau mass-mailer (menangkap typo gratis, menghemat kredit).</li>
  <li>Membangun form signup yang menolak sampah yang jelas-jelas salah di level field.</li>
  <li>Audit CSV kontak untuk menemukan typo sebelum import.</li>
  <li>Mengecek apakah alamat yang "kelihatan aneh" (TLD internasional, plus-addressing, sub-addressing) sebenarnya diizinkan.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Valid secara sintaksis ≠ deliverable.</strong> <code>does-not-exist@gmail.com</code> lolos setiap pengecekan struktural. Verifikasi nyata butuh respons dari server MX. Pakai ini sebagai filter lini pertama, bukan sinyal kepercayaan.</li>
  <li><strong>Plus addressing diizinkan.</strong> <code>name+tag@gmail.com</code> valid dan di-route ke <code>name@gmail.com</code> — jangan strip; itu fitur.</li>
  <li><strong>Internationalised email (IDN).</strong> <code>用户@例.中国</code> secara teknis valid per RFC 6530 tapi belum didukung luas oleh server SMTP. Tool ini mengikuti aturan ASCII konservatif; longgarkan kalau kamu memang butuh IDN.</li>
  <li><strong>Deteksi disposable domain hanya hint.</strong> Daftarnya pasti tidak lengkap dan domain yang di-flag pun masih bisa jadi user sungguhan.</li>
  <li><strong>Jangan tolak perbedaan case.</strong> Local part secara teknis case-sensitive per RFC 5321; dalam praktiknya setiap provider modern memperlakukannya sebagai case-insensitive. Jangan lowercase saat disimpan.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>RFC 5322 định nghĩa cú pháp địa chỉ email — và quy tắc phức tạp một cách đáng ngạc nhiên (dấu cộng, dấu chấm và quote được phép trong phần local; tên miền IDN; bracketed IP). Tool này kiểm tra một địa chỉ theo cú pháp đó, tách phần local và domain, và đánh dấu các vấn đề thông thường mà người dùng vẫn gặp phải khi gõ địa chỉ của họ vào form.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Validation form đăng ký phía client trước khi gửi lên backend.</li>
  <li>Đánh dấu lỗi gõ trong danh sách email được nhập (ví dụ <code>@gmial.com</code>).</li>
  <li>Xác nhận một địa chỉ phức tạp (với +alias hoặc dấu chấm) hợp lệ.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Vượt qua cú pháp không có nghĩa là email tồn tại.</strong> Bạn cần một MX lookup để biết miền có nhận thư hay không, và việc gửi xác minh để biết tài khoản có tồn tại hay không.</li>
  <li><strong>Quote và escape trong phần local thực sự hợp lệ.</strong> <code>"john.doe"@example.com</code> theo kỹ thuật là hợp lệ. Trong thực tế, hầu hết các dịch vụ không chấp nhận chúng.</li>
  <li><strong>Tên miền IDN.</strong> <code>user@münchen.de</code> hợp lệ — nhưng nhiều validator regex cổ điển từ chối nó. Tool này chấp nhận chúng.</li>
  <li><strong>Đừng over-validate.</strong> Form đăng ký nên chấp nhận rộng rãi (thậm chí có rủi ro chấp nhận một số địa chỉ không gửi được) — gửi email xác minh, sau đó dọn các địa chỉ không phản hồi.</li>
</ul>
""",
    },
    "related": ["regex-tester", "credit-card-validator", "url-encoder"],
    "howto": {"flow": "transform", "action": "validate","noun": "email"},
}
