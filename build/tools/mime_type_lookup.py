TOOL = {
    "slug": "mime-type-lookup",
    "category": "developer",
    "icon": "📎",
    "tags": ["mime", "type", "extension", "content-type", "file", "media"],
    "i18n": {
        "en": {
            "name": "MIME Type Lookup",
            "tagline": "Search MIME types by extension or by type. ~120 common types — image, video, audio, application, text, font.",
            "description": "Free MIME type lookup tool. Search by file extension (.pdf, .png, .json) or by MIME type (image/jpeg, application/pdf) across roughly 120 common Internet media types.",
        },
        "de": {"name": "MIME-Typ-Suche", "tagline": "Suche MIME-Typen nach Erweiterung oder Typ. ~120 gängige Typen — Bild, Video, Audio, application, text, font.", "description": "Kostenlose MIME-Typ-Suche. Suche nach Dateierweiterung (.pdf, .png, .json) oder MIME-Typ (image/jpeg, application/pdf) in rund 120 gängigen Medien-Typen."},
        "es": {"name": "Búsqueda de Tipos MIME", "tagline": "Busca tipos MIME por extensión o por tipo. ~120 tipos habituales — imagen, vídeo, audio, application, text, font.", "description": "Herramienta gratuita de búsqueda MIME. Busca por extensión (.pdf, .png, .json) o tipo MIME (image/jpeg, application/pdf) entre unos 120 tipos comunes."},
        "fr": {"name": "Recherche Type MIME", "tagline": "Cherchez les types MIME par extension ou par type. ~120 types courants — image, vidéo, audio, application, text, font.", "description": "Outil gratuit de recherche MIME. Cherchez par extension (.pdf, .png, .json) ou type MIME (image/jpeg, application/pdf) parmi environ 120 types courants."},
        "it": {"name": "Ricerca Tipi MIME", "tagline": "Cerca tipi MIME per estensione o per tipo. ~120 tipi comuni — immagini, video, audio, application, text, font.", "description": "Strumento gratuito di ricerca MIME. Cerca per estensione (.pdf, .png, .json) o tipo MIME (image/jpeg, application/pdf) fra circa 120 tipi comuni."},
        "pt": {"name": "Consulta de MIME Types", "tagline": "Busque MIME types por extensão ou por tipo. ~120 tipos comuns — image, video, audio, application, text, font.", "description": "Ferramenta gratuita de consulta de MIME types. Busque por extensão de arquivo (.pdf, .png, .json) ou por MIME type (image/jpeg, application/pdf) entre cerca de 120 Internet media types comuns."},
        "pl": {"name": "Wyszukiwarka MIME Types", "tagline": "Wyszukuj MIME types po rozszerzeniu albo po typie. ~120 typowych — image, video, audio, application, text, font.", "description": "Darmowe narzędzie do wyszukiwania MIME types. Szukaj po rozszerzeniu pliku (.pdf, .png, .json) albo po MIME type (image/jpeg, application/pdf) wśród około 120 typowych Internet media types."},
        "ja": {"name": "MIME タイプ検索", "tagline": "拡張子やタイプから MIME タイプを検索。image・video・audio・application・text・font の約 120 種を収録。", "description": "無料の MIME タイプ検索ツール。ファイル拡張子（.pdf、.png、.json）や MIME タイプ（image/jpeg、application/pdf）から、よく使われる約 120 種のインターネットメディアタイプを検索できます。"},
        "nl": {"name": "MIME Type Lookup", "tagline": "Zoek MIME types op extensie of type. ~120 gangbare types — image, video, audio, application, text, font.", "description": "Gratis MIME-type-lookup tool. Zoek op bestandsextensie (.pdf, .png, .json) of op MIME-type (image/jpeg, application/pdf) over ruwweg 120 gangbare Internet media types."},
    },
    "body": """
<div class="tool-card">
  <label>Filter</label>
  <input type="text" id="mt-q" oninput="mtRun()" placeholder="Type an extension or a MIME type — '.pdf', 'png', 'image/', 'video', 'json'…" autocomplete="off" spellcheck="false">
  <div class="meta" id="mt-count" style="margin-top:0.4rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="mt-out"></div>
</div>
""",
    "script": """
<style>
.mt-list{display:grid;gap:0.4rem}
.mt-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.7rem;padding:0.55rem 0.8rem;border:1px solid var(--border);background:var(--bg-elev);border-radius:6px;align-items:center;font-family:ui-monospace,monospace;font-size:0.85rem}
.mt-mime{font-weight:600;color:var(--text)}
.mt-ext{color:var(--accent)}
.mt-desc{color:var(--text-muted);font-size:0.8rem;font-family:-apple-system,sans-serif}
.mt-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0}
@media (max-width:700px){.mt-row{grid-template-columns:1fr}}
</style>
<script>
const MIME_TYPES = [
  ['text/plain', '.txt', 'Plain text'],
  ['text/html', '.html .htm', 'HyperText Markup Language'],
  ['text/css', '.css', 'Cascading Style Sheets'],
  ['text/csv', '.csv', 'Comma-separated values'],
  ['text/javascript', '.js .mjs', 'JavaScript (text/javascript is preferred over application/javascript per RFC 9239)'],
  ['text/markdown', '.md .markdown', 'Markdown source'],
  ['text/calendar', '.ics', 'iCalendar event'],
  ['text/vcard', '.vcf', 'vCard contact'],
  ['text/xml', '.xml', 'XML (text/xml; prefer application/xml for new code)'],
  ['text/tab-separated-values', '.tsv', 'Tab-separated values'],
  ['text/yaml', '.yaml .yml', 'YAML (de facto — no IANA registration)'],
  ['application/json', '.json', 'JSON document'],
  ['application/ld+json', '.jsonld', 'JSON-LD linked-data'],
  ['application/xml', '.xml', 'XML document'],
  ['application/xhtml+xml', '.xhtml', 'XHTML'],
  ['application/javascript', '.js', 'JavaScript (legacy — use text/javascript)'],
  ['application/wasm', '.wasm', 'WebAssembly module'],
  ['application/pdf', '.pdf', 'Portable Document Format'],
  ['application/zip', '.zip', 'ZIP archive'],
  ['application/gzip', '.gz', 'gzip compressed'],
  ['application/x-bzip2', '.bz2', 'bzip2 compressed'],
  ['application/x-7z-compressed', '.7z', '7-Zip archive'],
  ['application/x-tar', '.tar', 'TAR archive'],
  ['application/x-rar-compressed', '.rar', 'RAR archive'],
  ['application/zstd', '.zst', 'Zstandard compressed'],
  ['application/octet-stream', '.bin', 'Generic binary — fallback when type is unknown'],
  ['application/sql', '.sql', 'SQL script'],
  ['application/rtf', '.rtf', 'Rich Text Format'],
  ['application/msword', '.doc', 'Microsoft Word 97-2003'],
  ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx', 'Microsoft Word (OOXML)'],
  ['application/vnd.ms-excel', '.xls', 'Microsoft Excel 97-2003'],
  ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx', 'Microsoft Excel (OOXML)'],
  ['application/vnd.ms-powerpoint', '.ppt', 'Microsoft PowerPoint 97-2003'],
  ['application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx', 'Microsoft PowerPoint (OOXML)'],
  ['application/vnd.oasis.opendocument.text', '.odt', 'OpenDocument Text'],
  ['application/vnd.oasis.opendocument.spreadsheet', '.ods', 'OpenDocument Spreadsheet'],
  ['application/vnd.oasis.opendocument.presentation', '.odp', 'OpenDocument Presentation'],
  ['application/epub+zip', '.epub', 'EPUB e-book'],
  ['application/vnd.android.package-archive', '.apk', 'Android package'],
  ['application/x-msdownload', '.exe .dll', 'Windows executable'],
  ['application/x-shockwave-flash', '.swf', 'Adobe Flash (deprecated)'],
  ['application/x-httpd-php', '.php', 'PHP script'],
  ['application/x-www-form-urlencoded', '', 'URL-encoded form data (HTTP body)'],
  ['multipart/form-data', '', 'Multipart form upload (HTTP body)'],
  ['multipart/byteranges', '', 'HTTP partial-content with multiple ranges'],
  ['application/manifest+json', '.webmanifest', 'Web App Manifest'],
  ['application/atom+xml', '.atom', 'Atom syndication feed'],
  ['application/rss+xml', '.rss', 'RSS feed'],
  ['image/jpeg', '.jpg .jpeg', 'JPEG image'],
  ['image/png', '.png', 'PNG image'],
  ['image/gif', '.gif', 'GIF image'],
  ['image/webp', '.webp', 'WebP image'],
  ['image/avif', '.avif', 'AVIF image (AV1-based)'],
  ['image/heic', '.heic', 'HEIC image (iOS default)'],
  ['image/heif', '.heif', 'HEIF image'],
  ['image/svg+xml', '.svg', 'Scalable Vector Graphics'],
  ['image/x-icon', '.ico', 'Windows icon — also commonly served as image/vnd.microsoft.icon'],
  ['image/vnd.microsoft.icon', '.ico', 'Windows icon (IANA registered)'],
  ['image/bmp', '.bmp', 'Windows Bitmap'],
  ['image/tiff', '.tif .tiff', 'TIFF image'],
  ['image/apng', '.apng', 'Animated PNG'],
  ['image/jxl', '.jxl', 'JPEG XL'],
  ['video/mp4', '.mp4 .m4v', 'MP4 video (H.264/H.265)'],
  ['video/webm', '.webm', 'WebM video (VP8/VP9/AV1)'],
  ['video/ogg', '.ogv', 'Ogg video (Theora)'],
  ['video/quicktime', '.mov', 'QuickTime video'],
  ['video/x-msvideo', '.avi', 'AVI video'],
  ['video/x-matroska', '.mkv', 'Matroska video'],
  ['video/3gpp', '.3gp', '3GPP mobile video'],
  ['video/mpeg', '.mpg .mpeg', 'MPEG-1/MPEG-2 video'],
  ['application/vnd.apple.mpegurl', '.m3u8', 'HLS playlist (HTTP Live Streaming)'],
  ['application/dash+xml', '.mpd', 'MPEG-DASH manifest'],
  ['audio/mpeg', '.mp3', 'MP3 audio'],
  ['audio/mp4', '.m4a', 'AAC audio in MP4 container'],
  ['audio/aac', '.aac', 'AAC audio (raw stream)'],
  ['audio/ogg', '.ogg .oga', 'Ogg Vorbis / Opus audio'],
  ['audio/opus', '.opus', 'Opus audio'],
  ['audio/webm', '.weba', 'WebM audio'],
  ['audio/flac', '.flac', 'FLAC lossless audio'],
  ['audio/wav', '.wav', 'WAV / RIFF audio'],
  ['audio/x-aiff', '.aiff .aif', 'AIFF audio'],
  ['audio/midi', '.mid .midi', 'MIDI sequence'],
  ['font/woff', '.woff', 'WOFF web font'],
  ['font/woff2', '.woff2', 'WOFF2 web font'],
  ['font/ttf', '.ttf', 'TrueType font'],
  ['font/otf', '.otf', 'OpenType font'],
  ['font/collection', '.ttc', 'TrueType collection'],
  ['application/vnd.ms-fontobject', '.eot', 'Embedded OpenType (legacy IE)'],
  ['model/gltf+json', '.gltf', 'glTF JSON 3D model'],
  ['model/gltf-binary', '.glb', 'glTF binary 3D model'],
  ['model/obj', '.obj', 'Wavefront OBJ 3D model'],
  ['model/stl', '.stl', 'STL 3D model'],
  ['application/vnd.google-earth.kml+xml', '.kml', 'Google Earth KML'],
  ['application/vnd.google-earth.kmz', '.kmz', 'Google Earth KMZ archive'],
  ['application/geo+json', '.geojson', 'GeoJSON'],
  ['application/x-protobuf', '', 'Protocol Buffers binary (de facto)'],
  ['application/grpc', '', 'gRPC payload'],
  ['application/cbor', '.cbor', 'Concise Binary Object Representation (RFC 8949)'],
  ['application/msgpack', '', 'MessagePack (de facto)'],
  ['application/x-yaml', '.yaml .yml', 'YAML (de facto)'],
  ['application/toml', '.toml', 'TOML config'],
  ['application/x-pkcs12', '.p12 .pfx', 'PKCS #12 certificate bundle'],
  ['application/pkcs7-mime', '.p7m', 'PKCS #7 / S/MIME'],
  ['application/x-pem-file', '.pem', 'PEM-encoded certificate or key'],
  ['application/jwt', '', 'JSON Web Token'],
  ['application/problem+json', '', 'Problem Details for HTTP APIs (RFC 7807)'],
  ['application/vnd.api+json', '', 'JSON:API'],
  ['application/hal+json', '', 'HAL — Hypertext Application Language'],
  ['application/x-ndjson', '.ndjson', 'Newline-delimited JSON'],
  ['application/x-jsonlines', '.jsonl', 'JSON Lines (de facto)'],
  ['text/event-stream', '', 'Server-Sent Events stream'],
  ['application/octet-stream', '.dat', 'Generic binary'],
  ['application/x-iso9660-image', '.iso', 'ISO 9660 disk image'],
  ['application/x-bittorrent', '.torrent', 'BitTorrent metadata'],
  ['application/vnd.debian.binary-package', '.deb', 'Debian package'],
  ['application/x-rpm', '.rpm', 'RPM package'],
  ['application/vnd.docker.image.rootfs.diff.tar.gzip', '', 'Docker image layer'],
  ['application/dicom', '.dcm', 'Medical imaging — DICOM'],
  ['application/x-x509-ca-cert', '.crt .cer', 'X.509 certificate (DER)'],
  ['image/x-portable-pixmap', '.ppm', 'Portable Pixmap']
];
function mtRun(){
  const q = (document.getElementById('mt-q').value || '').toLowerCase().trim();
  const out = document.getElementById('mt-out');
  const cnt = document.getElementById('mt-count');
  const matches = MIME_TYPES.filter(([m, ext, desc]) => {
    if(!q) return true;
    return m.toLowerCase().includes(q) || ext.toLowerCase().includes(q) || desc.toLowerCase().includes(q);
  });
  cnt.textContent = matches.length + ' / ' + MIME_TYPES.length + ' types';
  if(matches.length === 0){ out.innerHTML = '<div class="mt-empty">No matches.</div>'; return; }
  out.innerHTML = '<div class="mt-list">' + matches.map(([m, ext, desc]) =>
    `<div class="mt-row"><div class="mt-mime">${m}</div><div class="mt-ext">${ext || '—'}</div><div class="mt-desc">${desc}</div></div>`
  ).join('') + '</div>';
}
document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(mtRun));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A MIME type (now called an Internet media type) is a two-part label like <code>image/png</code> or <code>application/json</code> that tells a server, browser, or library how to interpret a chunk of bytes. It's what goes in HTTP <code>Content-Type</code> headers, what Multipart message parts declare, and what <code>file --mime</code> reports. The IANA registry has thousands of entries; this tool covers roughly 120 you'll actually meet in web work.</p>

<h3>When to use it</h3>
<ul>
  <li>Setting <code>Content-Type</code> on an API response and wanting the right one for <code>.docx</code>, <code>.heic</code>, or <code>.webmanifest</code>.</li>
  <li>Configuring an upload field's <code>accept</code> attribute or a S3-bucket allow-list.</li>
  <li>Reading a hex dump or a tcpdump and looking up what <code>application/grpc-web</code> actually is.</li>
  <li>Building a static-file server or CDN config and needing extension-to-mime mapping.</li>
  <li>Settling whether to use <code>text/xml</code> or <code>application/xml</code> (use the latter for new code per RFC 7303).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Extension does not equal MIME type.</strong> <code>.json</code> usually maps to <code>application/json</code>, but a server can serve it as <code>text/plain</code> and browsers will obey the header. Always set the header explicitly.</li>
  <li><strong>JavaScript is messy.</strong> RFC 9239 says <code>text/javascript</code> is the preferred type. <code>application/javascript</code>, <code>application/ecmascript</code>, and others are obsolete but still seen.</li>
  <li><strong>OOXML types are very long.</strong> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code> for <code>.docx</code>. Don't try to remember them — copy them.</li>
  <li><strong><code>application/octet-stream</code> means "I don't know".</strong> If you control the type, use a real one — browsers may force-download octet-stream content even when it's renderable.</li>
  <li><strong>Charset matters for text types.</strong> <code>Content-Type: text/html; charset=utf-8</code> — without it, browsers guess and sometimes guess wrong (mojibake).</li>
  <li><strong>Magic-byte sniffing differs from the declared type.</strong> Browsers may second-guess <code>Content-Type</code> based on file contents (<code>X-Content-Type-Options: nosniff</code> disables this — set it for security).</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um MIME type (hoje chamado de Internet media type) é um rótulo em duas partes como <code>image/png</code> ou <code>application/json</code> que diz a um servidor, browser ou biblioteca como interpretar uma sequência de bytes. É o que vai no header HTTP <code>Content-Type</code>, o que partes Multipart declaram e o que <code>file --mime</code> reporta. O registry da IANA tem milhares de entradas; esta ferramenta cobre cerca de 120 que você realmente encontra em trabalho com web.</p>

<h3>Quando usar</h3>
<ul>
  <li>Definir <code>Content-Type</code> numa resposta de API e querer o correto para <code>.docx</code>, <code>.heic</code> ou <code>.webmanifest</code>.</li>
  <li>Configurar o atributo <code>accept</code> de um campo de upload ou uma allow-list de bucket S3.</li>
  <li>Lendo um hex dump ou um tcpdump e procurando o que <code>application/grpc-web</code> realmente é.</li>
  <li>Montar um servidor de arquivos estáticos ou config de CDN e precisar do mapeamento extensão para MIME type.</li>
  <li>Decidir entre usar <code>text/xml</code> ou <code>application/xml</code> (use o último para código novo, conforme RFC 7303).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Extensão não é igual a MIME type.</strong> <code>.json</code> normalmente mapeia para <code>application/json</code>, mas um servidor pode servir como <code>text/plain</code> e os browsers vão obedecer ao header. Sempre defina o header explicitamente.</li>
  <li><strong>JavaScript é uma bagunça.</strong> RFC 9239 diz que <code>text/javascript</code> é o tipo preferido. <code>application/javascript</code>, <code>application/ecmascript</code> e outros são obsoletos mas ainda aparecem.</li>
  <li><strong>MIME types OOXML são bem longos.</strong> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code> para <code>.docx</code>. Não tente decorar — copie.</li>
  <li><strong><code>application/octet-stream</code> significa "não sei".</strong> Se você controla o tipo, use um real — browsers podem forçar download de conteúdo octet-stream mesmo quando ele é renderizável.</li>
  <li><strong>Charset importa para tipos de texto.</strong> <code>Content-Type: text/html; charset=utf-8</code> — sem isso, o browser adivinha e às vezes erra (mojibake).</li>
  <li><strong>Magic-byte sniffing difere do tipo declarado.</strong> Browsers podem questionar o <code>Content-Type</code> com base no conteúdo do arquivo (<code>X-Content-Type-Options: nosniff</code> desativa isso — defina por segurança).</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Ein MIME-Typ (offiziell "Internet media type") ist ein zweiteiliges Label wie <code>image/png</code>, das angibt, wie Bytes interpretiert werden sollen. Es steht in HTTP-<code>Content-Type</code>-Headern und in Multipart-Teilen. Dieses Tool deckt rund 120 gängige Typen ab.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Den korrekten <code>Content-Type</code> für <code>.docx</code>, <code>.heic</code>, <code>.webmanifest</code> setzen.</li>
<li><code>accept</code>-Attribut eines Upload-Feldes oder eine S3-Allowlist konfigurieren.</li>
<li>Bei einem Hex-Dump oder tcpdump nachschlagen, was z.B. <code>application/grpc-web</code> ist.</li>
<li>Statischen Dateiserver / CDN konfigurieren — Mapping Erweiterung→MIME.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Erweiterung ≠ MIME-Typ.</strong> Browser folgen dem Header, nicht der Endung — Header explizit setzen.</li>
<li><strong>JavaScript ist chaotisch.</strong> RFC 9239 bevorzugt <code>text/javascript</code>.</li>
<li><strong>OOXML-Typen sind sehr lang.</strong> Nicht auswendig lernen — kopieren.</li>
<li><strong><code>application/octet-stream</code> = "unbekannt".</strong> Wenn möglich konkreten Typ angeben.</li>
<li><strong>Charset zählt.</strong> Ohne <code>; charset=utf-8</code> rät der Browser — und liegt manchmal falsch.</li>
<li><strong>MIME-Sniffing umgeht den Header.</strong> Mit <code>X-Content-Type-Options: nosniff</code> deaktivieren.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Un tipo MIME (oficialmente "Internet media type") es una etiqueta de dos partes como <code>image/png</code> que indica cómo interpretar unos bytes. Aparece en cabeceras HTTP <code>Content-Type</code> y en partes Multipart. Esta herramienta cubre unos 120 tipos comunes.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Establecer el <code>Content-Type</code> correcto para <code>.docx</code>, <code>.heic</code>, <code>.webmanifest</code>.</li>
<li>Configurar el atributo <code>accept</code> de un upload o una allow-list de S3.</li>
<li>Buscar qué es <code>application/grpc-web</code> al ver un dump.</li>
<li>Configurar un servidor estático o CDN — mapeo extensión→MIME.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Extensión ≠ tipo MIME.</strong> Los navegadores siguen la cabecera, no la extensión — establece la cabecera explícitamente.</li>
<li><strong>JavaScript es un lío.</strong> RFC 9239 prefiere <code>text/javascript</code>.</li>
<li><strong>Los tipos OOXML son larguísimos.</strong> No los memorices — cópialos.</li>
<li><strong><code>application/octet-stream</code> = "desconocido".</strong> Usa un tipo real cuando lo conozcas.</li>
<li><strong>El charset importa.</strong> Sin <code>; charset=utf-8</code> el navegador adivina y a veces falla.</li>
<li><strong>El sniffing MIME ignora la cabecera.</strong> Desactívalo con <code>X-Content-Type-Options: nosniff</code>.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Un type MIME (officiellement "type de média Internet") est un libellé en deux parties comme <code>image/png</code> indiquant comment interpréter des octets. Il figure dans les en-têtes HTTP <code>Content-Type</code> et dans les parties Multipart. Cet outil couvre environ 120 types courants.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Définir le bon <code>Content-Type</code> pour <code>.docx</code>, <code>.heic</code>, <code>.webmanifest</code>.</li>
<li>Configurer l'attribut <code>accept</code> d'un upload ou une allow-list S3.</li>
<li>Chercher ce qu'est <code>application/grpc-web</code> dans un dump.</li>
<li>Configurer un serveur statique ou CDN — mapping extension→MIME.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Extension ≠ type MIME.</strong> Les navigateurs suivent l'en-tête — fixez-le explicitement.</li>
<li><strong>JavaScript est embrouillé.</strong> RFC 9239 préfère <code>text/javascript</code>.</li>
<li><strong>Les types OOXML sont très longs.</strong> Ne les mémorisez pas — copiez-les.</li>
<li><strong><code>application/octet-stream</code> = "inconnu".</strong> Utilisez un type réel si possible.</li>
<li><strong>Le charset compte.</strong> Sans <code>; charset=utf-8</code>, le navigateur devine et se trompe parfois.</li>
<li><strong>Le sniffing MIME ignore l'en-tête.</strong> Désactivez avec <code>X-Content-Type-Options: nosniff</code>.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Un tipo MIME (ufficialmente "Internet media type") è un'etichetta in due parti come <code>image/png</code> che indica come interpretare dei byte. Appare nelle intestazioni HTTP <code>Content-Type</code> e nelle parti Multipart. Questo strumento copre circa 120 tipi comuni.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Impostare il <code>Content-Type</code> corretto per <code>.docx</code>, <code>.heic</code>, <code>.webmanifest</code>.</li>
<li>Configurare l'attributo <code>accept</code> di un upload o una allow-list S3.</li>
<li>Cercare cos'è <code>application/grpc-web</code> in un dump.</li>
<li>Configurare un server statico o un CDN — mapping estensione→MIME.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Estensione ≠ tipo MIME.</strong> I browser seguono l'header — impostalo esplicitamente.</li>
<li><strong>JavaScript è caotico.</strong> RFC 9239 preferisce <code>text/javascript</code>.</li>
<li><strong>I tipi OOXML sono molto lunghi.</strong> Non memorizzarli — copiali.</li>
<li><strong><code>application/octet-stream</code> = "sconosciuto".</strong> Usa un tipo reale quando possibile.</li>
<li><strong>Il charset conta.</strong> Senza <code>; charset=utf-8</code> il browser indovina e a volte sbaglia.</li>
<li><strong>Lo sniffing MIME ignora l'header.</strong> Disattivalo con <code>X-Content-Type-Options: nosniff</code>.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>MIME type (obecnie nazywany Internet media type) to dwuczęściowa etykieta typu <code>image/png</code> albo <code>application/json</code>, która mówi serwerowi, przeglądarce albo bibliotece, jak interpretować kawałek bajtów. To, co idzie w nagłówkach HTTP <code>Content-Type</code>, co deklarują części Multipart wiadomości i co raportuje <code>file --mime</code>. Rejestr IANA ma tysiące wpisów; to narzędzie pokrywa około 120, na które faktycznie natkniesz się w pracy webowej.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Ustawianie <code>Content-Type</code> na odpowiedzi API i potrzeba właściwego dla <code>.docx</code>, <code>.heic</code> albo <code>.webmanifest</code>.</li>
  <li>Konfiguracja atrybutu <code>accept</code> w polu uploadu albo allow-listy bucketu S3.</li>
  <li>Czytanie hex dumpa albo tcpdumpa i sprawdzanie, czym właściwie jest <code>application/grpc-web</code>.</li>
  <li>Budowa serwera plików statycznych albo configa CDN i potrzeba mapowania rozszerzenie→MIME.</li>
  <li>Rozstrzyganie, czy używać <code>text/xml</code> czy <code>application/xml</code> (w nowym kodzie tego drugiego, wg RFC 7303).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Rozszerzenie nie równa się MIME type.</strong> <code>.json</code> zwykle mapuje się na <code>application/json</code>, ale serwer może serwować jako <code>text/plain</code> i przeglądarki posłuchają nagłówka. Zawsze ustawiaj nagłówek jawnie.</li>
  <li><strong>JavaScript jest bałaganiarski.</strong> RFC 9239 mówi, że <code>text/javascript</code> jest preferowanym typem. <code>application/javascript</code>, <code>application/ecmascript</code> i inne są przestarzałe, ale nadal widywane.</li>
  <li><strong>Typy OOXML są bardzo długie.</strong> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code> dla <code>.docx</code>. Nie próbuj zapamiętywać — kopiuj.</li>
  <li><strong><code>application/octet-stream</code> znaczy "nie wiem".</strong> Jeśli kontrolujesz typ, użyj prawdziwego — przeglądarki mogą wymusić download contentu octet-stream, nawet jeśli da się go wyrenderować.</li>
  <li><strong>Charset ma znaczenie dla typów tekstowych.</strong> <code>Content-Type: text/html; charset=utf-8</code> — bez tego przeglądarki zgadują i czasem zgadują źle (mojibake).</li>
  <li><strong>Magic-byte sniffing różni się od deklarowanego typu.</strong> Przeglądarki mogą zakwestionować <code>Content-Type</code> na bazie zawartości pliku (<code>X-Content-Type-Options: nosniff</code> to wyłącza — ustaw dla bezpieczeństwa).</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>MIME タイプ（現在は Internet media type）は、<code>image/png</code> や <code>application/json</code> のような 2 部構成のラベルで、サーバー、ブラウザ、ライブラリにバイト列の解釈方法を伝えます。HTTP の <code>Content-Type</code> ヘッダ、Multipart メッセージのパート、<code>file --mime</code> の出力に現れます。IANA のレジストリには数千件あり、本ツールはウェブで実際に出会う約 120 種を収録しています。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>API レスポンスに <code>Content-Type</code> を設定するとき、<code>.docx</code>、<code>.heic</code>、<code>.webmanifest</code> 用の正しいタイプが知りたい。</li>
  <li>アップロードフィールドの <code>accept</code> 属性や、S3 バケットの許可リストを設定するとき。</li>
  <li>hex ダンプや tcpdump で <code>application/grpc-web</code> が何かを調べたいとき。</li>
  <li>静的ファイルサーバーや CDN の設定で、拡張子→MIME のマッピングを作りたいとき。</li>
  <li><code>text/xml</code> と <code>application/xml</code> のどちらを使うか決めたいとき（新規コードでは RFC 7303 に従い後者を推奨）。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>拡張子は MIME タイプと等価ではありません。</strong> <code>.json</code> は通常 <code>application/json</code> にマップされますが、サーバーが <code>text/plain</code> として配信すれば、ブラウザはヘッダに従います。常にヘッダを明示してください。</li>
  <li><strong>JavaScript は混乱しがちです。</strong> RFC 9239 では <code>text/javascript</code> が推奨です。<code>application/javascript</code>、<code>application/ecmascript</code> などは廃止予定ですが、まだ目にします。</li>
  <li><strong>OOXML タイプは非常に長いです。</strong> <code>.docx</code> は <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code>。覚えようとせず、コピーしましょう。</li>
  <li><strong><code>application/octet-stream</code> は「分からない」の意味です。</strong> タイプを制御できるなら本物のタイプを使ってください。レンダリング可能なコンテンツでも、ブラウザがダウンロード扱いにすることがあります。</li>
  <li><strong>テキスト系では charset が重要です。</strong> <code>Content-Type: text/html; charset=utf-8</code>。これがないとブラウザは推測し、時々間違えて文字化けします。</li>
  <li><strong>マジックバイトのスニッフィングが宣言型と違うことがあります。</strong> ブラウザは <code>Content-Type</code> をファイル内容で再判定することがあります。<code>X-Content-Type-Options: nosniff</code> でこれを無効化できます。セキュリティのため設定を推奨します。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een MIME-type (nu Internet media type genoemd) is een tweedelig label als <code>image/png</code> of <code>application/json</code> dat een server, browser of library vertelt hoe een blok bytes te interpreteren. Het is wat in HTTP <code>Content-Type</code>-headers staat, wat Multipart-message-parts declareren, en wat <code>file --mime</code> rapporteert. De IANA-registry heeft duizenden entries; deze tool dekt ruwweg 120 die je in webwerk daadwerkelijk tegenkomt.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li><code>Content-Type</code> instellen op een API-response en de juiste willen voor <code>.docx</code>, <code>.heic</code> of <code>.webmanifest</code>.</li>
  <li>Het <code>accept</code>-attribuut van een upload-veld configureren of een S3-bucket allow-list.</li>
  <li>Een hex-dump of tcpdump lezen en opzoeken wat <code>application/grpc-web</code> eigenlijk is.</li>
  <li>Een statische-file-server of CDN-config bouwen en extension-to-mime mapping nodig hebben.</li>
  <li>Beslechten of <code>text/xml</code> of <code>application/xml</code> te gebruiken (gebruik de laatste voor nieuwe code volgens RFC 7303).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Extensie is niet gelijk aan MIME-type.</strong> <code>.json</code> mapt meestal naar <code>application/json</code>, maar een server kan het als <code>text/plain</code> serveren en browsers gehoorzamen de header. Stel de header altijd expliciet in.</li>
  <li><strong>JavaScript is rommelig.</strong> RFC 9239 zegt <code>text/javascript</code> is het preferred type. <code>application/javascript</code>, <code>application/ecmascript</code> en andere zijn obsolete maar nog te zien.</li>
  <li><strong>OOXML-types zijn heel lang.</strong> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code> voor <code>.docx</code>. Probeer ze niet te onthouden — kopieer ze.</li>
  <li><strong><code>application/octet-stream</code> betekent "ik weet het niet".</strong> Als je het type controleert, gebruik een echte — browsers kunnen octet-stream content force-downloaden zelfs als die renderbaar is.</li>
  <li><strong>Charset doet ertoe voor text-types.</strong> <code>Content-Type: text/html; charset=utf-8</code> — zonder gokt de browser en gokt soms verkeerd (mojibake).</li>
  <li><strong>Magic-byte sniffing verschilt van het gedeclareerde type.</strong> Browsers kunnen <code>Content-Type</code> tweede-raden op basis van file-contents (<code>X-Content-Type-Options: nosniff</code> schakelt dit uit — zet het voor security).</li>
</ul>
""",
    },
    "related": ["http-status-codes", "image-to-base64", "url-encoder"],
}
