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
    },
    "related": ["regex-tester", "credit-card-validator", "url-encoder"],
}
