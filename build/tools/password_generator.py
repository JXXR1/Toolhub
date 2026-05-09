TOOL = {
    "slug": "password-generator",
    "category": "security",
    "icon": "🔐",
    "tags": ["password", "secure", "random", "generate", "passphrase"],
    "i18n": {
        "en": {
            "name": "Password Generator",
            "tagline": "Strong random passwords or memorable passphrases. Generated locally — never sent anywhere.",
            "description": "Free secure password generator. Custom character rules, passphrase mode, and batch generation. Runs entirely in your browser.",
        },
        "de": {
            "name": "Passwort-Generator",
            "tagline": "Sichere Zufallspasswörter oder einprägsame Passphrasen. Lokal erzeugt – wird nie übertragen.",
            "description": "Kostenloser sicherer Passwort-Generator. Eigene Zeichenregeln, Passphrasen-Modus und Mehrfacherzeugung. Läuft komplett im Browser.",
        },
        "es": {
            "name": "Generador de Contraseñas",
            "tagline": "Contraseñas aleatorias seguras o frases-contraseña memorables. Se generan localmente, nunca se envían.",
            "description": "Generador de contraseñas seguro y gratuito. Reglas de caracteres, modo frase-contraseña y generación por lotes. Funciona en tu navegador.",
        },
        "fr": {
            "name": "Générateur de Mots de Passe",
            "tagline": "Mots de passe aléatoires solides ou phrases secrètes mémorables. Générés localement — jamais envoyés.",
            "description": "Générateur de mots de passe sécurisé et gratuit. Règles personnalisables, mode phrase secrète et génération par lot. Tout dans votre navigateur.",
        },
        "it": {
            "name": "Generatore di Password",
            "tagline": "Password casuali robuste o passphrase memorabili. Generate localmente, mai inviate altrove.",
            "description": "Generatore di password sicuro e gratuito. Regole personalizzabili, modalità passphrase e generazione in batch. Tutto nel browser.",
        },
        "pt": {
            "name": "Gerador de Senhas",
            "tagline": "Senhas aleatórias fortes ou passphrases memorizáveis. Geradas localmente — nunca enviadas para lugar nenhum.",
            "description": "Gerador de senhas seguro e gratuito. Regras de caracteres personalizadas, modo passphrase e geração em lote. Roda inteiramente no seu navegador.",
        },
        "pl": {
            "name": "Generator Haseł",
            "tagline": "Mocne losowe hasła albo łatwe do zapamiętania passphrase'y. Generowane lokalnie — nigdzie nie wysyłane.",
            "description": "Darmowy bezpieczny generator haseł. Konfigurowalne reguły znaków, tryb passphrase i generowanie batch. Działa w całości w przeglądarce.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_TYPE}</label>
      <select id="pw-mode" onchange="pwToggleMode()">
        <option value="chars">Random characters</option>
        <option value="phrase">Passphrase (words)</option>
      </select>
    </div>
    <div>
      <label>{LBL_COUNT} (1-50)</label>
      <input type="number" id="pw-count" value="1" min="1" max="50">
    </div>
  </div>
  <div id="pw-chars-opts">
    <div class="row-2col" style="margin-top:1rem">
      <div>
        <label>{LBL_LENGTH}: <span id="pw-len-display">20</span></label>
        <input type="range" id="pw-length" min="6" max="128" value="20" oninput="document.getElementById('pw-len-display').textContent=this.value">
      </div>
      <div style="display:flex;flex-direction:column;gap:0.4rem;font-size:0.9rem">
        <label><input type="checkbox" id="pw-lower" checked> a-z lowercase</label>
        <label><input type="checkbox" id="pw-upper" checked> A-Z uppercase</label>
        <label><input type="checkbox" id="pw-digit" checked> 0-9 digits</label>
        <label><input type="checkbox" id="pw-symbol" checked> Symbols !@#$…</label>
        <label><input type="checkbox" id="pw-noambig"> Exclude ambiguous (0/O/1/l/I)</label>
      </div>
    </div>
  </div>
  <div id="pw-phrase-opts" style="display:none;margin-top:1rem">
    <div class="row-2col">
      <div>
        <label>Words per phrase</label>
        <input type="number" id="pw-words" value="4" min="2" max="12">
      </div>
      <div>
        <label>Separator</label>
        <select id="pw-sep">
          <option value="-">- (hyphen)</option>
          <option value=".">. (period)</option>
          <option value="_">_ (underscore)</option>
          <option value=" ">space</option>
        </select>
      </div>
    </div>
  </div>
  <div class="button-row">
    <button onclick="pwGenerate()">{LBL_GENERATE}</button>
    <button class="secondary" onclick="pwCopy()">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <pre class="output" id="pw-out">{LBL_NO_INPUT}</pre>
  <div class="meta" id="pw-meta"></div>
</div>
""",
    "script": """
<script>
const PW_WORDS = ["able","acid","aged","also","area","army","away","baby","back","ball","band","bank","base","bath","bear","beat","been","beer","bell","belt","best","bike","bird","blow","blue","boat","body","bomb","bond","bone","book","boom","born","boss","both","bowl","bulk","burn","bush","busy","call","calm","came","camp","card","care","case","cash","cast","cell","chat","chip","city","club","coal","coat","code","cold","come","cook","cool","cope","copy","core","cost","crew","crop","dark","data","date","dawn","days","dead","deal","dean","dear","debt","deep","deny","desk","dial","dice","diet","disc","disk","does","done","door","dose","down","draw","drew","drop","drug","dual","duke","dust","duty","each","earn","ease","east","easy","edge","else","even","ever","evil","exit","face","fact","fail","fair","fall","farm","fast","fate","fear","feed","feel","feet","fell","felt","file","fill","film","find","fine","fire","firm","fish","five","flag","flat","flow","food","foot","fork","form","fort","four","free","from","fuel","full","fund","gain","game","gate","gave","gear","gene","gift","girl","give","glad","goal","goes","gold","golf","gone","good","gray","grew","grey","grow","gulf","hair","half","hall","hand","hang","hard","harm","hate","have","head","hear","heat","held","hell","help","here","hero","high","hill","hint","hire","hold","hole","holy","home","hope","host","hour","huge","hunt","hurt","idea","into","iron","item","jack","jane","java","jean","jess","jest","jets","john","join","jose","jude","jump","june","jury","just","keen","keep","kept","kick","kind","king","knee","knew","know","lack","lady","laid","lake","land","lane","last","late","lava","lawn","laws","lead","leaf","lean","leap","left","lend","less","life","lift","like","line","link","lion","list","live","load","loan","lock","lost","loud","love","luck","made","mail","main","make","male","many","mark","mass","matt","mean","meat","meet","menu","mere","mike","mile","milk","mill","mind","mine","miss","mode","mood","moon","more","most","move","much","must","name","navy","near","neck","need","news","next","nice","nine","none","nose","note","ohio","once","only","onto","open","oral","over","pace","pack","page","paid","pain","pair","palm","park","part","pass","past","path","peak","pick","pink","pipe","plan","play","plot","plug","plus","poll","pool","poor","port","post","pull","pure","push","race","rage","rail","rain","rank","rare","rate","read","real","rear","rely","rent","rest","rice","rich","ride","ring","rise","risk","road","rock","role","roll","roof","room","root","rose","rule","rush","ruth","safe","said","sake","sale","salt","same","sand","save","seal","seat","seed","seek","seem","seen","self","sell","send","sent","sept","sets","sext","shed","ship","shoe","shop","shot","show","shut","sick","side","sign","silk","sing","sink","site","size","skin","slip","slow","snap","snow","soft","soil","sold","sole","some","song","soon","sort","soul","soup","spot","star","stay","step","stir","stop","such","suit","sure","take","tale","talk","tall","tank","tape","task","team","tech","tell","tend","term","test","text","than","that","them","then","they","thin","this","thus","tide","tied","time","tiny","told","toll","tone","tony","took","tool","tops","tore","torn","tour","town","tree","trip","true","tube","tune","turn","twin","type","ugly","unit","upon","used","user","uses","vary","vast","very","vice","view","vote","wage","wait","wake","walk","wall","want","ward","warm","warn","wash","wave","ways","weak","wear","week","well","went","were","west","what","when","whom","wide","wife","wild","will","wind","wine","wing","wire","wise","wish","with","wood","word","wore","work","worn","yard","yeah","year","your","zero","zone"];

function pwToggleMode(){
  const m = document.getElementById('pw-mode').value;
  document.getElementById('pw-chars-opts').style.display = m === 'chars' ? 'block' : 'none';
  document.getElementById('pw-phrase-opts').style.display = m === 'phrase' ? 'block' : 'none';
}

function pwRandInt(max){
  const u = new Uint32Array(1);
  crypto.getRandomValues(u);
  return u[0] % max;
}

function pwGenChars(){
  let pool = '';
  if (document.getElementById('pw-lower').checked) pool += 'abcdefghijklmnopqrstuvwxyz';
  if (document.getElementById('pw-upper').checked) pool += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  if (document.getElementById('pw-digit').checked) pool += '0123456789';
  if (document.getElementById('pw-symbol').checked) pool += '!@#$%^&*()-_=+[]{};:,.<>?/~';
  if (document.getElementById('pw-noambig').checked) pool = pool.replace(/[0O1lI]/g, '');
  if (!pool) return 'Pick at least one character set.';
  const len = parseInt(document.getElementById('pw-length').value, 10);
  const out = new Array(len);
  const rand = new Uint32Array(len);
  crypto.getRandomValues(rand);
  for (let i = 0; i < len; i++) out[i] = pool[rand[i] % pool.length];
  return out.join('');
}

function pwGenPhrase(){
  const n = parseInt(document.getElementById('pw-words').value, 10);
  const sep = document.getElementById('pw-sep').value;
  const words = [];
  for (let i = 0; i < n; i++) words.push(PW_WORDS[pwRandInt(PW_WORDS.length)]);
  return words.join(sep);
}

function pwEntropy(s, mode){
  if (mode === 'phrase'){
    const n = parseInt(document.getElementById('pw-words').value, 10);
    return Math.round(n * Math.log2(PW_WORDS.length));
  }
  let pool = 0;
  if (document.getElementById('pw-lower').checked) pool += 26;
  if (document.getElementById('pw-upper').checked) pool += 26;
  if (document.getElementById('pw-digit').checked) pool += 10;
  if (document.getElementById('pw-symbol').checked) pool += 27;
  if (!pool) return 0;
  return Math.round(s.length * Math.log2(pool));
}

function pwGenerate(){
  const mode = document.getElementById('pw-mode').value;
  const count = parseInt(document.getElementById('pw-count').value, 10) || 1;
  const lines = [];
  let example = '';
  for (let i = 0; i < count; i++){
    const p = mode === 'phrase' ? pwGenPhrase() : pwGenChars();
    if (i === 0) example = p;
    lines.push(p);
  }
  document.getElementById('pw-out').textContent = lines.join('\\n');
  const bits = pwEntropy(example, mode);
  let strength = 'weak';
  if (bits >= 60) strength = 'fair';
  if (bits >= 80) strength = 'strong';
  if (bits >= 100) strength = 'very strong';
  document.getElementById('pw-meta').textContent = '~' + bits + ' bits of entropy · ' + strength;
}

function pwCopy(){
  const text = document.getElementById('pw-out').textContent;
  if (!text || text === '{LBL_NO_INPUT}') return;
  navigator.clipboard.writeText(text);
}

document.addEventListener('DOMContentLoaded', pwGenerate);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A good password is one an attacker can't guess and you don't have to remember (because it's stored in your password manager). This generator produces strong random passwords or memorable passphrases entirely in your browser, using <code>crypto.getRandomValues</code> — the same cryptographically secure random source TLS uses. Nothing is transmitted; the password never leaves your device.</p>

<h3>When to use it</h3>
<ul>
  <li>Creating a unique password for any new account that goes into a password manager.</li>
  <li>Generating a master password or a recovery passphrase you'll commit to memory — passphrase mode is easier to type and remember.</li>
  <li>Producing a non-human secret for a CI variable, API token, or Wi-Fi network.</li>
  <li>Bulk-generating passwords for a fresh user batch (set count up to 50).</li>
</ul>

<h3>Random characters vs passphrases</h3>
<ul>
  <li><strong>Random characters</strong> — most entropy per length. 20 mixed characters ≈ 130 bits. Right for things you paste, not type.</li>
  <li><strong>Passphrases</strong> — easier to type and remember. Four words ≈ 40 bits, six words ≈ 60 bits. Right for master passwords, device unlock, and anything you'll enter manually often.</li>
  <li>"Exclude ambiguous" drops <code>0/O/1/l/I</code> for safer reading from screens or hand-written notes.</li>
</ul>

<h3>How much entropy do I need?</h3>
<ul>
  <li>≥ 60 bits — fine for low-value accounts</li>
  <li>≥ 80 bits — good for most accounts</li>
  <li>≥ 100 bits — high-value (financial, master password, root credential)</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't reuse passwords.</strong> The single biggest security upgrade you can make is one unique password per site, stored in a manager. Generator strength is wasted if the same password lives on five sites.</li>
  <li><strong>Don't write generated passwords down without protection.</strong> Use a password manager (1Password, Bitwarden, KeePass) — not a Notes app, not a text file, not an email draft.</li>
  <li><strong>Long &gt; complex.</strong> A 24-character password using only lowercase letters has more entropy than a 10-character one with every symbol class. Length wins.</li>
  <li><strong>Site-specific rules can break copy-paste.</strong> Some sites ban specific symbols or cap length at 16. Annoying but real — generate, then trim/swap to fit if needed (and then store the actual stored password in your manager).</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Uma boa senha é uma que o atacante não consegue adivinhar e que você não precisa lembrar (porque ela está guardada no seu password manager). Este gerador produz senhas aleatórias fortes ou passphrases memorizáveis inteiramente no seu navegador, usando <code>crypto.getRandomValues</code> — a mesma fonte aleatória criptograficamente segura que o TLS usa. Nada é transmitido; a senha nunca sai do seu dispositivo.</p>

<h3>Quando usar</h3>
<ul>
  <li>Criar uma senha única para qualquer conta nova que vá para um password manager.</li>
  <li>Gerar uma master password ou uma passphrase de recuperação que você vai memorizar — o modo passphrase é mais fácil de digitar e lembrar.</li>
  <li>Produzir um segredo não-humano para uma variável de CI, API token ou rede Wi-Fi.</li>
  <li>Gerar senhas em lote para um batch novo de usuários (count até 50).</li>
</ul>

<h3>Caracteres aleatórios vs passphrases</h3>
<ul>
  <li><strong>Caracteres aleatórios</strong> — entropia máxima por comprimento. 20 caracteres misturados ≈ 130 bits. Bom para coisas que você cola, não digita.</li>
  <li><strong>Passphrases</strong> — mais fáceis de digitar e lembrar. Quatro palavras ≈ 40 bits, seis palavras ≈ 60 bits. Bom para master passwords, desbloqueio de dispositivo e qualquer coisa que você vá digitar manualmente com frequência.</li>
  <li>"Excluir ambíguos" remove <code>0/O/1/l/I</code> para leitura mais segura em telas ou anotações à mão.</li>
</ul>

<h3>De quanta entropia eu preciso?</h3>
<ul>
  <li>≥ 60 bits — ok para contas de baixo valor</li>
  <li>≥ 80 bits — bom para a maioria das contas</li>
  <li>≥ 100 bits — alto valor (financeiro, master password, credencial de root)</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não reutilize senhas.</strong> O maior upgrade de segurança que você pode fazer é uma senha única por site, guardada num manager. A força do gerador é desperdiçada se a mesma senha está em cinco sites.</li>
  <li><strong>Não anote senhas geradas sem proteção.</strong> Use um password manager (1Password, Bitwarden, KeePass) — não um app de Notas, não um arquivo de texto, não um rascunho de e-mail.</li>
  <li><strong>Longa &gt; complexa.</strong> Uma senha de 24 caracteres só com letras minúsculas tem mais entropia que uma de 10 com todas as classes de símbolos. Comprimento ganha.</li>
  <li><strong>Regras específicas do site podem quebrar copy-paste.</strong> Alguns sites proíbem símbolos específicos ou limitam o tamanho em 16. Chato mas real — gere, depois corte/troque para encaixar se precisar (e aí guarde a senha real no seu manager).</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Dobre hasło to takie, którego atakujący nie zgadnie i którego ty nie musisz pamiętać (bo jest w menedżerze haseł). Ten generator produkuje mocne losowe hasła albo łatwe do zapamiętania passphrase'y w całości w twojej przeglądarce, używając <code>crypto.getRandomValues</code> — tego samego kryptograficznie bezpiecznego źródła losowości, którego używa TLS. Nic nie jest wysyłane; hasło nigdy nie opuszcza twojego urządzenia.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Tworzenie unikalnego hasła do każdego nowego konta, które wpada do menedżera haseł.</li>
  <li>Generowanie master password albo recovery passphrase, którą zapamiętasz — tryb passphrase jest łatwiejszy do wpisania i zapamiętania.</li>
  <li>Produkowanie nieludzkiego sekretu do zmiennej CI, tokenu API albo sieci Wi-Fi.</li>
  <li>Hurtowe generowanie haseł dla nowej paczki użytkowników (count do 50).</li>
</ul>

<h3>Losowe znaki vs passphrase</h3>
<ul>
  <li><strong>Losowe znaki</strong> — najwięcej entropii na długość. 20 mieszanych znaków ≈ 130 bitów. Dobre do rzeczy, które wklejasz, nie wpisujesz.</li>
  <li><strong>Passphrase'y</strong> — łatwiejsze do wpisania i zapamiętania. Cztery słowa ≈ 40 bitów, sześć słów ≈ 60 bitów. Dobre do master password, odblokowania urządzenia i wszystkiego, co wpisujesz ręcznie często.</li>
  <li>"Wyklucz dwuznaczne" wycina <code>0/O/1/l/I</code> dla bezpieczniejszego czytania z ekranu albo odręcznych notatek.</li>
</ul>

<h3>Ile entropii potrzebuję?</h3>
<ul>
  <li>≥ 60 bitów — OK do kont o niskiej wartości</li>
  <li>≥ 80 bitów — dobre do większości kont</li>
  <li>≥ 100 bitów — wysoka wartość (finanse, master password, root credential)</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie używaj tych samych haseł.</strong> Największy upgrade bezpieczeństwa to jedno unikalne hasło na stronę, trzymane w menedżerze. Siła generatora idzie w piach, jeśli to samo hasło żyje na pięciu stronach.</li>
  <li><strong>Nie zapisuj wygenerowanych haseł bez ochrony.</strong> Używaj menedżera haseł (1Password, Bitwarden, KeePass) — nie aplikacji Notatki, nie pliku tekstowego, nie kopii roboczej maila.</li>
  <li><strong>Długie &gt; skomplikowane.</strong> 24-znakowe hasło tylko z małych liter ma więcej entropii niż 10-znakowe ze wszystkimi klasami symboli. Długość wygrywa.</li>
  <li><strong>Reguły konkretnych stron potrafią zepsuć copy-paste.</strong> Niektóre serwisy zakazują konkretnych symboli albo ograniczają długość do 16. Upierdliwe, ale realne — wygeneruj, potem przytnij/podmień, żeby zmieścić (a faktyczne zapisane hasło wrzuć do menedżera).</li>
</ul>
""",
    },
    "related": ["uuid-generator", "hash-generator", "jwt-decoder"],
}
