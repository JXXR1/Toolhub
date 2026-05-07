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
<h2>How it works</h2>
<p>This generator uses your browser's <code>crypto.getRandomValues</code> API — a cryptographically secure random source. Nothing is transmitted; the password never leaves your device.</p>
<h3>Random characters vs passphrases</h3>
<ul>
  <li><strong>Random characters</strong> give the most entropy per length — 20 mixed characters ≈ 130 bits.</li>
  <li><strong>Passphrases</strong> are easier to remember and type — four words ≈ 40 bits, six words ≈ 60 bits. Increase word count for higher-stakes accounts.</li>
  <li>"Exclude ambiguous" removes <code>0/O/1/l/I</code> for safer reading from screens.</li>
</ul>
<h3>How much entropy do I need?</h3>
<ul>
  <li>≥ 60 bits — fine for low-value accounts</li>
  <li>≥ 80 bits — good for most accounts</li>
  <li>≥ 100 bits — high-value (financial, master password, root credential)</li>
</ul>
""",
    },
    "related": ["uuid-generator", "hash-generator", "jwt-decoder"],
}
