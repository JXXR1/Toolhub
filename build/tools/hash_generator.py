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
    },
    "related": ["password-generator", "uuid-generator", "jwt-decoder"],
}
