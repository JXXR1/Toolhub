TOOL = {
    "slug": "ascii-table",
    "category": "developer",
    "icon": "🔤",
    "tags": ["ascii", "table", "character", "encoding", "hex", "binary", "control", "html"],
    "i18n": {
        "en": {
            "name": "ASCII Table",
            "tagline": "Full ASCII reference 0–127 with decimal, hex, binary, character, and HTML entity. Filterable.",
            "description": "Free ASCII table reference. All 128 standard ASCII codes with decimal, hex, octal, binary, character, HTML entity, and a description for control characters. Filter as you type.",
        },
        "de": {"name": "ASCII-Tabelle", "tagline": "Vollständige ASCII-Referenz 0–127 mit Dezimal, Hex, Binär, Zeichen und HTML-Entität. Filterbar.", "description": "Kostenlose ASCII-Tabelle. Alle 128 ASCII-Codes mit Dezimal, Hex, Oktal, Binär, Zeichen, HTML-Entität und Beschreibung für Steuerzeichen. Filter beim Tippen."},
        "es": {"name": "Tabla ASCII", "tagline": "Referencia completa ASCII 0–127 con decimal, hex, binario, carácter y entidad HTML. Filtrable.", "description": "Tabla ASCII gratuita. Los 128 códigos ASCII con decimal, hex, octal, binario, carácter, entidad HTML y descripción de los caracteres de control. Filtra al escribir."},
        "fr": {"name": "Table ASCII", "tagline": "Référence ASCII complète 0–127 avec décimal, hex, binaire, caractère et entité HTML. Filtrable.", "description": "Table ASCII gratuite. Les 128 codes ASCII avec décimal, hex, octal, binaire, caractère, entité HTML et description des caractères de contrôle. Filtrage au fil de la frappe."},
        "it": {"name": "Tabella ASCII", "tagline": "Riferimento ASCII completo 0–127 con decimale, hex, binario, carattere ed entità HTML. Filtrabile.", "description": "Tabella ASCII gratuita. Tutti i 128 codici ASCII con decimale, hex, ottale, binario, carattere, entità HTML e descrizione dei caratteri di controllo. Filtra mentre digiti."},
    },
    "body": """
<div class="tool-card">
  <label>Filter</label>
  <input type="text" id="ascii-q" oninput="asciiRun()" placeholder="Type to filter — try 'tab', 'newline', '0x41', '65', 'A'…" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.4rem">
    <label style="display:inline-flex;gap:0.4rem;align-items:center;color:var(--text-muted);font-size:0.85rem"><input type="checkbox" id="ascii-ctrl" checked onchange="asciiRun()" style="width:auto"> Show control characters (0–31, 127)</label>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ascii-out" class="output" style="padding:0;overflow:auto"></div>
</div>
""",
    "script": """
<style>
.ascii-table{width:100%;border-collapse:collapse;font-family:ui-monospace,monospace;font-size:0.85rem}
.ascii-table th{position:sticky;top:0;background:var(--surface);color:var(--text-muted);font-weight:600;font-size:0.78rem;text-align:left;padding:0.5rem 0.7rem;border-bottom:1px solid var(--border)}
.ascii-table td{padding:0.4rem 0.7rem;border-bottom:1px solid var(--border);vertical-align:top}
.ascii-table tr:hover{background:var(--card-hover)}
.ascii-ch{font-weight:600;color:var(--accent)}
.ascii-desc{color:var(--text-muted);font-size:0.78rem}
.ascii-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0}
</style>
<script>
const ASCII_NAMES = {
  0:['NUL','Null'],1:['SOH','Start of Heading'],2:['STX','Start of Text'],3:['ETX','End of Text'],
  4:['EOT','End of Transmission'],5:['ENQ','Enquiry'],6:['ACK','Acknowledge'],7:['BEL','Bell'],
  8:['BS','Backspace'],9:['HT','Tab (horizontal)'],10:['LF','Line Feed (newline)'],11:['VT','Vertical Tab'],
  12:['FF','Form Feed'],13:['CR','Carriage Return'],14:['SO','Shift Out'],15:['SI','Shift In'],
  16:['DLE','Data Link Escape'],17:['DC1','Device Control 1 (XON)'],18:['DC2','Device Control 2'],
  19:['DC3','Device Control 3 (XOFF)'],20:['DC4','Device Control 4'],21:['NAK','Negative Acknowledge'],
  22:['SYN','Synchronous Idle'],23:['ETB','End of Transmission Block'],24:['CAN','Cancel'],
  25:['EM','End of Medium'],26:['SUB','Substitute'],27:['ESC','Escape'],28:['FS','File Separator'],
  29:['GS','Group Separator'],30:['RS','Record Separator'],31:['US','Unit Separator'],
  32:['SP','Space'],127:['DEL','Delete']
};
function asciiHtmlEntity(n){
  // Named entities for the few that have one
  const named = {34:'&amp;quot;',38:'&amp;amp;',39:'&amp;apos;',60:'&amp;lt;',62:'&amp;gt;',160:'&amp;nbsp;'};
  if(named[n]) return named[n];
  return '&amp;#' + n + ';';
}
function asciiBin(n){ return n.toString(2).padStart(7,'0'); }
function asciiHex(n){ return '0x' + n.toString(16).toUpperCase().padStart(2,'0'); }
function asciiOct(n){ return n.toString(8).padStart(3,'0'); }
function asciiCh(n){
  if(n < 32 || n === 127) return ASCII_NAMES[n][0];
  if(n === 32) return '(space)';
  return String.fromCharCode(n);
}
function asciiMatch(n, q){
  if(!q) return true;
  q = q.toLowerCase().trim();
  const ch = asciiCh(n).toLowerCase();
  const dec = String(n);
  const hex = asciiHex(n).toLowerCase();
  const bin = asciiBin(n);
  const oct = asciiOct(n);
  const named = ASCII_NAMES[n];
  const name = named ? (named[0] + ' ' + named[1]).toLowerCase() : '';
  return ch.includes(q) || dec === q || hex.includes(q) || hex.replace('0x','').includes(q.replace('0x','')) || bin.includes(q) || oct === q || name.includes(q);
}
function asciiRun(){
  const q = document.getElementById('ascii-q').value;
  const showCtrl = document.getElementById('ascii-ctrl').checked;
  const rows = [];
  for(let n=0;n<128;n++){
    const isCtrl = (n < 32 || n === 127);
    if(isCtrl && !showCtrl) continue;
    if(!asciiMatch(n, q)) continue;
    const named = ASCII_NAMES[n];
    const desc = named ? `<span class="ascii-desc">${named[0]} — ${named[1]}</span>` : '';
    const chDisplay = isCtrl ? `<span class="ascii-desc">${named[0]}</span>` : (n === 32 ? '<span class="ascii-desc">(space)</span>' : `<span class="ascii-ch">${String.fromCharCode(n).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}</span>`);
    rows.push(`<tr><td>${n}</td><td>${asciiHex(n)}</td><td>${asciiOct(n)}</td><td>${asciiBin(n)}</td><td>${chDisplay}</td><td><code>${asciiHtmlEntity(n)}</code></td><td>${desc}</td></tr>`);
  }
  const out = document.getElementById('ascii-out');
  if(rows.length === 0){
    out.innerHTML = '<div class="ascii-empty">No matches.</div>';
    return;
  }
  out.innerHTML = `<table class="ascii-table">
    <thead><tr><th>Dec</th><th>Hex</th><th>Oct</th><th>Bin</th><th>Char</th><th>HTML</th><th>Description</th></tr></thead>
    <tbody>${rows.join('')}</tbody></table>`;
}
document.addEventListener('DOMContentLoaded', asciiRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>ASCII (American Standard Code for Information Interchange) is the 128-character coding system that maps the digits, letters, punctuation, and a handful of control codes onto the integers 0–127. It's the foundation every modern text encoding (UTF-8, Latin-1, Windows-1252) extends, so knowing the values is occasionally vital — diagnosing a stray byte in a binary file, building a regex for "any printable", reading a hex dump, or remembering whether 0x0A or 0x0D is a newline.</p>

<h3>When to use it</h3>
<ul>
  <li>Reading a hex dump and trying to figure out what those bytes <em>say</em>.</li>
  <li>Writing a parser and needing the boundary values: <code>0x20</code> (space), <code>0x7E</code> (tilde) — the printable range.</li>
  <li>Debugging a CSV that broke because something contained <code>0x09</code> (Tab) or <code>0x1F</code> (Unit Separator).</li>
  <li>Crafting an HTML entity for a tricky character — <code>&amp;#65;</code> = <code>A</code>.</li>
  <li>Settling an argument about whether <code>\\r</code> is 0x0D (yes — Carriage Return) and <code>\\n</code> is 0x0A (yes — Line Feed).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>ASCII is 7-bit, not 8-bit.</strong> Codes 128–255 are <em>not</em> ASCII — they belong to whatever 8-bit encoding (Latin-1, CP-1252, …) the document declares, or are the lead bytes of a UTF-8 sequence.</li>
  <li><strong>Newlines differ by platform.</strong> Unix/macOS use <code>LF</code> (0x0A) only; legacy Mac Classic used <code>CR</code> (0x0D); Windows uses <code>CRLF</code>. Files that mix them break naïve line counting.</li>
  <li><strong>Control characters can be invisible saboteurs.</strong> A copy/paste from a terminal or PDF can pick up <code>0x1F</code>, <code>0x07</code> (BEL — actually beeps the terminal), or zero-width Unicode characters that <em>aren't</em> ASCII at all. If text "looks fine" but compares unequal, dump it to bytes.</li>
  <li><strong>HTML entities aren't always needed.</strong> In modern UTF-8 documents, <code>&amp;#65;</code> and the literal <code>A</code> are equivalent. Only escape characters that have syntactic meaning in HTML: <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, and <code>"</code> in attributes.</li>
  <li><strong>NUL (<code>0x00</code>) terminates strings in C.</strong> Don't embed it in C-string buffers without thinking — many APIs will silently truncate at the first NUL.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>ASCII ist das 128-Zeichen-Kodierungssystem, das Ziffern, Buchstaben, Satzzeichen und einige Steuerzeichen auf die Zahlen 0–127 abbildet. Es ist die Grundlage moderner Textkodierungen (UTF-8, Latin-1) — manchmal ist es wichtig, einzelne Bytes in einem Hex-Dump zu identifizieren oder zu wissen, ob 0x0A oder 0x0D ein Zeilenumbruch ist.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Beim Lesen eines Hex-Dumps, um Bytes als Text zu interpretieren.</li>
<li>Beim Schreiben eines Parsers, um Grenzwerte zu kennen.</li>
<li>Beim Debuggen einer CSV, die durch ein Tab oder ein Steuerzeichen kaputt ging.</li>
<li>Um eine HTML-Entität für ein bestimmtes Zeichen nachzuschlagen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>ASCII ist 7-Bit.</strong> Codes 128–255 sind kein ASCII — sie gehören zu Latin-1, CP-1252 oder UTF-8-Folgebytes.</li>
<li><strong>Zeilenumbrüche unterscheiden sich.</strong> Unix verwendet LF (0x0A), Windows CRLF, das alte Mac CR.</li>
<li><strong>Steuerzeichen sind unsichtbar.</strong> Eingefügter Text kann unsichtbare Zeichen enthalten, die Vergleiche fehlschlagen lassen.</li>
<li><strong>HTML-Entitäten sind selten nötig.</strong> In UTF-8-Dokumenten reicht das wörtliche Zeichen — escapen Sie nur <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>.</li>
<li><strong>NUL beendet C-Strings.</strong> Vorsicht beim Einbetten in C-Buffer.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>ASCII es el sistema de codificación de 128 caracteres que asigna dígitos, letras, signos de puntuación y caracteres de control a los enteros 0–127. Es la base sobre la que se construyen las codificaciones modernas (UTF-8, Latin-1) — y conocer los valores ayuda a diagnosticar un byte en un volcado hexadecimal o recordar qué código corresponde al salto de línea.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Leer un volcado hex e identificar los bytes como texto.</li>
<li>Escribir un parser que necesita los límites del rango imprimible.</li>
<li>Depurar un CSV roto por un tabulador o un carácter de control.</li>
<li>Buscar la entidad HTML para un carácter concreto.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>ASCII es de 7 bits.</strong> Los códigos 128–255 no son ASCII — pertenecen a Latin-1, CP-1252 o son bytes de continuación UTF-8.</li>
<li><strong>Los saltos de línea varían según la plataforma.</strong> Unix usa LF, Windows CRLF, el Mac clásico CR.</li>
<li><strong>Los caracteres de control son invisibles.</strong> Texto pegado puede traer caracteres invisibles que rompen comparaciones.</li>
<li><strong>Las entidades HTML rara vez son necesarias.</strong> En UTF-8 basta con el carácter literal — solo escapa <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>.</li>
<li><strong>NUL termina cadenas en C.</strong> No lo incluyas sin cuidado en buffers de C.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>ASCII est le système de codage à 128 caractères qui mappe les chiffres, lettres, ponctuations et caractères de contrôle sur les entiers 0–127. C'est le socle des encodages modernes (UTF-8, Latin-1) — utile pour décoder un dump hexadécimal ou se rappeler que 0x0A est un saut de ligne.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Lire un dump hex et identifier les octets comme du texte.</li>
<li>Écrire un parseur qui dépend des bornes des caractères imprimables.</li>
<li>Déboguer un CSV cassé par une tabulation ou un caractère de contrôle.</li>
<li>Trouver l'entité HTML pour un caractère donné.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>ASCII fait 7 bits.</strong> Les codes 128–255 ne sont pas ASCII — ils relèvent de Latin-1, CP-1252 ou d'octets de continuation UTF-8.</li>
<li><strong>Les sauts de ligne diffèrent.</strong> Unix utilise LF, Windows CRLF, l'ancien Mac CR.</li>
<li><strong>Les caractères de contrôle sont invisibles.</strong> Du texte collé peut contenir des caractères invisibles qui font échouer les comparaisons.</li>
<li><strong>Les entités HTML sont rarement nécessaires.</strong> En UTF-8, le caractère littéral suffit — n'échappez que <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>.</li>
<li><strong>NUL termine les chaînes C.</strong> À éviter dans des buffers C sans précaution.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>ASCII è il sistema di codifica a 128 caratteri che mappa cifre, lettere, segni di punteggiatura e caratteri di controllo sugli interi 0–127. È la base delle codifiche moderne (UTF-8, Latin-1) — utile per decodificare un dump esadecimale o ricordare quale codice corrisponde al ritorno a capo.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Leggere un dump hex e identificare i byte come testo.</li>
<li>Scrivere un parser che dipende dai limiti dei caratteri stampabili.</li>
<li>Eseguire il debug di un CSV rotto da un tab o da un carattere di controllo.</li>
<li>Cercare l'entità HTML per un carattere specifico.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>ASCII è a 7 bit.</strong> I codici 128–255 non sono ASCII — appartengono a Latin-1, CP-1252 o sono byte di continuazione UTF-8.</li>
<li><strong>I ritorni a capo variano.</strong> Unix usa LF, Windows CRLF, il vecchio Mac CR.</li>
<li><strong>I caratteri di controllo sono invisibili.</strong> Il testo incollato può contenere caratteri invisibili che falliscono i confronti.</li>
<li><strong>Le entità HTML servono raramente.</strong> In UTF-8 basta il carattere letterale — escape solo <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>.</li>
<li><strong>NUL termina le stringhe C.</strong> Da evitare nei buffer C senza attenzione.</li>
</ul>
""",
    },
    "related": ["unicode-inspector", "html-encoder", "url-encoder"],
}
