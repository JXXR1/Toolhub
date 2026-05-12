TOOL = {
    "slug": "file-size-converter",
    "category": "math",
    "icon": "📦",
    "tags": ["file size", "convert", "byte", "kilobyte", "megabyte", "gigabyte", "kib", "mib", "binary", "decimal"],
    "i18n": {
        "en": {
            "name": "File Size Converter",
            "tagline": "Convert between bytes, KB, MB, GB, TB and the binary KiB, MiB, GiB, TiB. Decimal vs binary clearly distinguished.",
            "description": "Free file size unit converter. Convert any byte count between decimal units (B, KB, MB, GB, TB, PB) and IEC binary units (KiB, MiB, GiB, TiB, PiB). See both at once, with the exact distinction.",
        },
        "de": {"name": "Dateigrößen-Umrechner", "tagline": "Konvertiere zwischen Bytes, KB, MB, GB, TB und den binären KiB, MiB, GiB, TiB. Dezimal vs binär klar getrennt.", "description": "Kostenloser Dateigrößen-Umrechner. Konvertiere jeden Byte-Wert zwischen dezimalen Einheiten (B, KB, MB, GB, TB) und binären IEC-Einheiten (KiB, MiB, GiB, TiB). Beide nebeneinander."},
        "es": {"name": "Conversor de Tamaño de Archivo", "tagline": "Convierte entre bytes, KB, MB, GB, TB y los binarios KiB, MiB, GiB, TiB. Decimal vs binario claros.", "description": "Conversor gratuito de tamaño de archivo. Convierte cualquier valor en bytes entre unidades decimales (B, KB, MB, GB, TB) y unidades binarias IEC (KiB, MiB, GiB, TiB)."},
        "fr": {"name": "Convertisseur de Taille de Fichier", "tagline": "Convertissez entre octets, Ko, Mo, Go, To et les binaires Kio, Mio, Gio, Tio. Décimal vs binaire clarifié.", "description": "Convertisseur gratuit de taille de fichier. Convertissez n'importe quel nombre d'octets entre unités décimales (B, KB, MB, GB, TB) et unités binaires IEC (KiB, MiB, GiB, TiB)."},
        "it": {"name": "Convertitore Dimensione File", "tagline": "Converti tra byte, KB, MB, GB, TB e i binari KiB, MiB, GiB, TiB. Decimale vs binario chiari.", "description": "Convertitore gratuito di dimensioni file. Converti qualsiasi quantità di byte tra unità decimali (B, KB, MB, GB, TB) e unità binarie IEC (KiB, MiB, GiB, TiB)."},
        "pt": {"name": "Conversor de Tamanho de Arquivo", "tagline": "Converta entre bytes, KB, MB, GB, TB e os binários KiB, MiB, GiB, TiB. Decimal vs binário bem distinguidos.", "description": "Conversor gratuito de unidades de tamanho de arquivo. Converta qualquer quantidade de bytes entre unidades decimais (B, KB, MB, GB, TB, PB) e unidades binárias IEC (KiB, MiB, GiB, TiB, PiB). Veja os dois lado a lado, com a distinção exata."},
        "pl": {"name": "Konwerter Rozmiaru Plików", "tagline": "Konwertuj między bajtami, KB, MB, GB, TB a binarnymi KiB, MiB, GiB, TiB. Decimal vs binary jasno rozdzielone.", "description": "Darmowy konwerter jednostek rozmiaru pliku. Przelicz dowolną liczbę bajtów między jednostkami dziesiętnymi (B, KB, MB, GB, TB, PB) i binarnymi IEC (KiB, MiB, GiB, TiB, PiB). Zobacz obie naraz, z dokładnym rozróżnieniem."},
        "ja": {"name": "ファイルサイズコンバーター", "tagline": "バイト、KB、MB、GB、TB と、バイナリ系の KiB、MiB、GiB、TiB を相互変換。10 進と 2 進を明確に区別。", "description": "無料のファイルサイズ単位変換ツール。任意のバイト値を、10 進系単位（B、KB、MB、GB、TB、PB）と IEC バイナリ単位（KiB、MiB、GiB、TiB、PiB）の間で変換し、両方を同時に表示します。違いを正確に把握できます。"},
        "nl": {"name": "Bestandsgrootte-converter", "tagline": "Converteer tussen bytes, KB, MB, GB, TB en de binaire KiB, MiB, GiB, TiB. Decimaal vs binair duidelijk gescheiden.", "description": "Gratis converter voor bestandsgrootte-units. Converteer elk aantal bytes tussen decimale units (B, KB, MB, GB, TB, PB) en IEC binaire units (KiB, MiB, GiB, TiB, PiB). Zie beide tegelijk, met het exacte onderscheid."},
        "tr": {"name": "Dosya Boyutu Dönüştürücü", "tagline": "byte, KB, MB, GB, TB ve ikilik KiB, MiB, GiB, TiB arasında dönüştür. Ondalık - ikilik ayrımı net.", "description": "Ücretsiz dosya boyutu birim dönüştürücü. Herhangi bir byte sayısını ondalık birimler (B, KB, MB, GB, TB, PB) ile IEC ikilik birimleri (KiB, MiB, GiB, TiB, PiB) arasında çevir. İkisini birden, kesin ayrımıyla gör."},
        "id": {"name": "Konverter Ukuran File", "tagline": "Konversi antara byte, KB, MB, GB, TB dan biner KiB, MiB, GiB, TiB. Pemisahan desimal vs biner yang jelas.", "description": "Konverter ukuran file gratis. Konversi antara satuan desimal (KB, MB, GB, TB) dan biner (KiB, MiB, GiB, TiB) dengan pemisahan yang jelas. Menjelaskan perbedaan 1000 vs 1024 yang membingungkan banyak orang."},
        "vi": {"name": "Chuyển đổi Kích thước File", "tagline": "Chuyển giữa byte, KB, MB, GB, TB và KiB nhị phân, MiB, GiB, TiB. Phân tách thập phân vs nhị phân rõ ràng.", "description": "Bộ chuyển kích thước file miễn phí trực tuyến giữa byte, KB, MB, GB, TB và KiB nhị phân, MiB, GiB, TiB. Phân biệt đơn vị thập phân (1000) và nhị phân (1024) một cách rõ ràng."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Value</label>
      <input type="number" id="fs-val" step="any" oninput="fsRun()" value="1" autocomplete="off">
    </div>
    <div>
      <label>From</label>
      <select id="fs-unit" onchange="fsRun()">
        <option value="B">B — bytes</option>
        <option value="KB">KB — kilobytes (decimal, 1000)</option>
        <option value="MB" selected>MB — megabytes (decimal, 1000²)</option>
        <option value="GB">GB — gigabytes (decimal, 1000³)</option>
        <option value="TB">TB — terabytes (decimal, 1000⁴)</option>
        <option value="PB">PB — petabytes (decimal, 1000⁵)</option>
        <option value="KiB">KiB — kibibytes (binary, 1024)</option>
        <option value="MiB">MiB — mebibytes (binary, 1024²)</option>
        <option value="GiB">GiB — gibibytes (binary, 1024³)</option>
        <option value="TiB">TiB — tebibytes (binary, 1024⁴)</option>
        <option value="PiB">PiB — pebibytes (binary, 1024⁵)</option>
        <option value="bit">bit — single bit (1/8 of a byte)</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="fs-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.fs-grid{display:grid;grid-template-columns:1fr 1fr;gap:0.7rem;font-family:ui-monospace,monospace;font-size:0.88rem}
.fs-col{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.fs-col h4{font-size:0.78rem;color:var(--text-muted);font-weight:600;margin:0 0 0.4rem;letter-spacing:0.04em;text-transform:uppercase}
.fs-row{display:grid;grid-template-columns:auto 1fr;gap:0.6rem;padding:0.2rem 0;border-bottom:1px dashed var(--border)}
.fs-row:last-child{border:none}
.fs-row .fs-u{color:var(--text-muted);min-width:3.4rem}
.fs-row .fs-v{color:var(--text);text-align:right;word-break:break-all}
.fs-bytes{margin-top:0.7rem;padding:0.6rem 0.8rem;border:1px solid var(--accent);border-radius:6px;color:var(--accent);font-family:ui-monospace,monospace;font-size:0.85rem}
@media (max-width:700px){.fs-grid{grid-template-columns:1fr}}
</style>
<script>
const FS_FACTORS = {
  bit: 1/8,
  B: 1,
  KB: 1e3, MB: 1e6, GB: 1e9, TB: 1e12, PB: 1e15,
  KiB: 1024, MiB: 1024**2, GiB: 1024**3, TiB: 1024**4, PiB: 1024**5
};
function fsFmt(n){
  if(!isFinite(n)) return '∞';
  if(n === 0) return '0';
  const abs = Math.abs(n);
  if(abs >= 1e15 || (abs > 0 && abs < 1e-4)) return n.toExponential(6);
  // Up to 6 significant decimals, trim trailing zeros
  let s = n.toFixed(6);
  if(s.includes('.')) s = s.replace(/0+$/,'').replace(/\\.$/,'');
  return s;
}
function fsRun(){
  const v = parseFloat(document.getElementById('fs-val').value);
  const u = document.getElementById('fs-unit').value;
  const out = document.getElementById('fs-out');
  if(!isFinite(v)){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const bytes = v * FS_FACTORS[u];
  const dec = ['B','KB','MB','GB','TB','PB'];
  const bin = ['B','KiB','MiB','GiB','TiB','PiB'];
  const decRows = dec.map(unit => `<div class="fs-row"><span class="fs-u">${unit}</span><span class="fs-v">${fsFmt(bytes/FS_FACTORS[unit])}</span></div>`).join('');
  const binRows = bin.map(unit => `<div class="fs-row"><span class="fs-u">${unit}</span><span class="fs-v">${fsFmt(bytes/FS_FACTORS[unit])}</span></div>`).join('');
  out.innerHTML = `
    <div class="fs-grid">
      <div class="fs-col"><h4>Decimal (SI · powers of 1000)</h4>${decRows}</div>
      <div class="fs-col"><h4>Binary (IEC · powers of 1024)</h4>${binRows}</div>
    </div>
    <div class="fs-bytes">= ${fsFmt(bytes)} bytes  ·  ${fsFmt(bytes*8)} bits</div>
  `;
}
document.addEventListener('DOMContentLoaded', fsRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>"How big is 4 GB?" depends on who's asking. Hard-drive manufacturers, network engineers, and SI-following standards mean 4,000,000,000 bytes (powers of 1000). Operating systems, RAM modules, and most file managers historically meant 4,294,967,296 bytes (powers of 1024). The two numbers are 7% apart at the gigabyte scale and 10% apart at the terabyte scale — enough to feel cheated when a "1 TB" drive shows up as "931 GiB" on your computer. This tool converts between both systems so you always know which you're looking at.</p>

<h3>The two systems</h3>
<ul>
  <li><strong>SI / decimal</strong> — KB, MB, GB, TB. <code>1 KB = 1,000 bytes</code>. Used by storage manufacturers, network speeds (Mbps, Gbps), and the SI standard since 1960.</li>
  <li><strong>IEC / binary</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1,024 bytes</code>. The IEC introduced these in 1998 to disambiguate. Linux <code>du</code> with <code>-h</code> uses these, as does macOS Finder for memory.</li>
</ul>

<h3>When to use it</h3>
<ul>
  <li>Sizing a backup, an upload, or a Docker image and matching what a tool reports.</li>
  <li>Converting "150 Mbps" download speed to MB/s (divide by 8 — bits to bytes).</li>
  <li>Estimating cloud-storage cost when one provider quotes GB and another quotes GiB.</li>
  <li>Figuring out how much "1 GB" of email actually is on disk.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Hard drives use decimal.</strong> A "1 TB" drive holds 1,000,000,000,000 bytes ≈ 931 GiB. The OS isn't lying — the marketing is using the smaller unit.</li>
  <li><strong>RAM uses binary.</strong> "8 GB RAM" is almost always 8 GiB (8,589,934,592 bytes). RAM is built in powers of two.</li>
  <li><strong>Network speed is in bits, not bytes.</strong> 100 Mbps = 100 megabits per second = 12.5 MB/s peak. Your "100 Mbit fiber" doesn't download a 100 MB file in one second.</li>
  <li><strong>Some tools are inconsistent.</strong> macOS Finder switched from binary (with KB labels) to decimal in 10.6, then mostly stayed there. Windows Explorer still uses binary with KB labels — confusing but unchanged.</li>
  <li><strong>Browsers' <code>Content-Length</code> is bytes.</strong> Always exact, no SI/IEC ambiguity.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>"Quão grande são 4 GB?" depende de quem está perguntando. Fabricantes de HD, engenheiros de rede e padrões SI significam 4.000.000.000 bytes (potências de 1000). Sistemas operacionais, módulos de RAM e a maioria dos gerenciadores de arquivos historicamente significam 4.294.967.296 bytes (potências de 1024). Os dois números diferem em 7% na escala de gigabyte e 10% na escala de terabyte — o suficiente para você se sentir enganado quando um HD de "1 TB" aparece como "931 GiB" no seu computador. Esta ferramenta converte entre os dois sistemas para você sempre saber qual está vendo.</p>

<h3>Os dois sistemas</h3>
<ul>
  <li><strong>SI / decimal</strong> — KB, MB, GB, TB. <code>1 KB = 1.000 bytes</code>. Usado por fabricantes de armazenamento, velocidades de rede (Mbps, Gbps) e o padrão SI desde 1960.</li>
  <li><strong>IEC / binário</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1.024 bytes</code>. A IEC introduziu essas unidades em 1998 para desambiguar. O <code>du</code> do Linux com <code>-h</code> usa essas, assim como o Finder do macOS para memória.</li>
</ul>

<h3>Quando usar</h3>
<ul>
  <li>Dimensionar um backup, um upload ou uma imagem Docker e bater com o que a ferramenta reporta.</li>
  <li>Converter velocidade de download de "150 Mbps" para MB/s (divida por 8 — bits para bytes).</li>
  <li>Estimar custo de cloud storage quando um provider cobra em GB e outro em GiB.</li>
  <li>Descobrir quanto "1 GB" de email realmente ocupa em disco.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>HDs usam decimal.</strong> Um drive de "1 TB" guarda 1.000.000.000.000 bytes ≈ 931 GiB. O SO não está mentindo — o marketing está usando a unidade menor.</li>
  <li><strong>RAM usa binário.</strong> "8 GB de RAM" é quase sempre 8 GiB (8.589.934.592 bytes). RAM é construída em potências de dois.</li>
  <li><strong>Velocidade de rede é em bits, não bytes.</strong> 100 Mbps = 100 megabits por segundo = 12,5 MB/s no pico. Sua "fibra de 100 Mbit" não baixa um arquivo de 100 MB em um segundo.</li>
  <li><strong>Algumas ferramentas são inconsistentes.</strong> O Finder do macOS migrou de binário (com labels KB) para decimal no 10.6 e ficou lá. O Windows Explorer ainda usa binário com labels KB — confuso mas inalterado.</li>
  <li><strong>O <code>Content-Length</code> dos browsers é em bytes.</strong> Sempre exato, sem ambiguidade SI/IEC.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>"Wie groß ist 4 GB?" hängt davon ab, wer fragt. Festplattenhersteller verstehen 4.000.000.000 Bytes (SI, Potenzen von 1000); Betriebssysteme verstehen 4.294.967.296 Bytes (IEC, Potenzen von 1024). Auf TB-Ebene unterscheiden sich beide um 10%. Dieses Tool konvertiert zwischen beiden Systemen.</p>
<h3>Die zwei Systeme</h3>
<ul>
<li><strong>SI / dezimal</strong> — KB, MB, GB, TB. 1 KB = 1.000 Bytes. Festplattenhersteller, Netzwerkgeschwindigkeiten.</li>
<li><strong>IEC / binär</strong> — KiB, MiB, GiB, TiB. 1 KiB = 1.024 Bytes. Linux <code>du -h</code>, Speichermodule.</li>
</ul>
<h3>Wann verwenden</h3>
<ul>
<li>Backup-, Upload- oder Docker-Image-Größe ermitteln.</li>
<li>"150 Mbps" in MB/s umrechnen (durch 8 teilen).</li>
<li>Cloud-Speicherkosten zwischen Anbietern vergleichen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Festplatten verwenden dezimal.</strong> "1 TB" = 1.000.000.000.000 Bytes ≈ 931 GiB.</li>
<li><strong>RAM verwendet binär.</strong> "8 GB RAM" ist fast immer 8 GiB.</li>
<li><strong>Netzwerk in Bits.</strong> 100 Mbps = 12,5 MB/s Spitze.</li>
<li><strong>Tools sind inkonsistent.</strong> Windows Explorer zeigt binär mit KB-Label.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>"¿Cuánto es 4 GB?" depende de quién pregunte. Los fabricantes de discos usan 4.000.000.000 bytes (SI, potencias de 1000); los sistemas operativos usan 4.294.967.296 bytes (IEC, potencias de 1024). A escala TB la diferencia es del 10%. Esta herramienta convierte entre ambos sistemas.</p>
<h3>Los dos sistemas</h3>
<ul>
<li><strong>SI / decimal</strong> — KB, MB, GB, TB. 1 KB = 1.000 bytes. Fabricantes de disco, velocidad de red.</li>
<li><strong>IEC / binario</strong> — KiB, MiB, GiB, TiB. 1 KiB = 1.024 bytes. Linux <code>du -h</code>, módulos de memoria.</li>
</ul>
<h3>Cuándo usarlo</h3>
<ul>
<li>Calcular el tamaño de una copia, una subida o una imagen Docker.</li>
<li>Convertir "150 Mbps" a MB/s (dividir entre 8).</li>
<li>Comparar costes de almacenamiento en nube entre proveedores.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Los discos usan decimal.</strong> "1 TB" = 1.000.000.000.000 bytes ≈ 931 GiB.</li>
<li><strong>La RAM usa binario.</strong> "8 GB RAM" es casi siempre 8 GiB.</li>
<li><strong>Red en bits.</strong> 100 Mbps = 12,5 MB/s pico.</li>
<li><strong>Herramientas inconsistentes.</strong> Windows Explorer muestra binario con etiqueta KB.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>"Combien fait 4 Go ?" dépend de qui pose la question. Les fabricants de disques entendent 4 000 000 000 octets (SI, puissances de 1000) ; les systèmes d'exploitation entendent 4 294 967 296 octets (IEC, puissances de 1024). À l'échelle To, la différence est de 10 %. Cet outil convertit entre les deux systèmes.</p>
<h3>Les deux systèmes</h3>
<ul>
<li><strong>SI / décimal</strong> — Ko, Mo, Go, To. 1 Ko = 1 000 octets. Fabricants de disques, débits réseau.</li>
<li><strong>IEC / binaire</strong> — Kio, Mio, Gio, Tio. 1 Kio = 1 024 octets. Linux <code>du -h</code>, modules mémoire.</li>
</ul>
<h3>Quand l'utiliser</h3>
<ul>
<li>Estimer la taille d'une sauvegarde, d'un upload ou d'une image Docker.</li>
<li>Convertir "150 Mbps" en Mo/s (diviser par 8).</li>
<li>Comparer les coûts de stockage cloud entre fournisseurs.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Les disques durs utilisent le décimal.</strong> "1 To" = 1 000 000 000 000 octets ≈ 931 Gio.</li>
<li><strong>La RAM utilise le binaire.</strong> "8 Go RAM" vaut presque toujours 8 Gio.</li>
<li><strong>Le réseau est en bits.</strong> 100 Mbps = 12,5 Mo/s en pointe.</li>
<li><strong>Outils incohérents.</strong> L'explorateur Windows affiche du binaire avec un label Ko.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>"Quanto è 4 GB?" dipende da chi chiede. I produttori di dischi intendono 4.000.000.000 byte (SI, potenze di 1000); i sistemi operativi intendono 4.294.967.296 byte (IEC, potenze di 1024). Al livello TB la differenza è del 10%. Questo strumento converte tra i due sistemi.</p>
<h3>I due sistemi</h3>
<ul>
<li><strong>SI / decimale</strong> — KB, MB, GB, TB. 1 KB = 1.000 byte. Produttori di dischi, velocità di rete.</li>
<li><strong>IEC / binario</strong> — KiB, MiB, GiB, TiB. 1 KiB = 1.024 byte. Linux <code>du -h</code>, moduli di memoria.</li>
</ul>
<h3>Quando usarlo</h3>
<ul>
<li>Dimensionare un backup, un upload o un'immagine Docker.</li>
<li>Convertire "150 Mbps" in MB/s (dividere per 8).</li>
<li>Confrontare costi di cloud storage tra provider.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>I dischi usano il decimale.</strong> "1 TB" = 1.000.000.000.000 byte ≈ 931 GiB.</li>
<li><strong>La RAM usa il binario.</strong> "8 GB RAM" è quasi sempre 8 GiB.</li>
<li><strong>La rete è in bit.</strong> 100 Mbps = 12,5 MB/s di picco.</li>
<li><strong>Strumenti incoerenti.</strong> Esplora risorse Windows mostra binario con etichetta KB.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>"Ile to jest 4 GB?" zależy od tego, kto pyta. Producenci dysków, inżynierowie sieciowi i standardy zgodne z SI rozumieją 4 000 000 000 bajtów (potęgi 1000). Systemy operacyjne, moduły RAM i większość menedżerów plików historycznie rozumie 4 294 967 296 bajtów (potęgi 1024). Te dwie liczby różnią się o 7% na poziomie gigabajta i 10% na poziomie terabajta — wystarczająco, żeby poczuć się oszukanym, gdy dysk "1 TB" pokazuje się jako "931 GiB" w komputerze. To narzędzie konwertuje między oboma systemami, żebyś zawsze wiedział, na co patrzysz.</p>

<h3>Dwa systemy</h3>
<ul>
  <li><strong>SI / dziesiętny</strong> — KB, MB, GB, TB. <code>1 KB = 1000 bajtów</code>. Używane przez producentów storage'u, prędkości sieciowe (Mbps, Gbps) i standard SI od 1960.</li>
  <li><strong>IEC / binarny</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1024 bajty</code>. IEC wprowadziło je w 1998, żeby ujednoznacznić. Linuksowy <code>du -h</code> ich używa, podobnie macOS Finder dla pamięci.</li>
</ul>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wymiarowanie backupu, uploadu albo Docker image i dopasowanie do tego, co raportuje narzędzie.</li>
  <li>Konwersja "150 Mbps" prędkości pobierania na MB/s (podziel przez 8 — bity na bajty).</li>
  <li>Estymacja kosztu storage'u w chmurze, gdy jeden provider liczy w GB, a drugi w GiB.</li>
  <li>Sprawdzenie, ile naprawdę zajmuje "1 GB" maila na dysku.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Dyski twarde używają systemu dziesiętnego.</strong> Dysk "1 TB" mieści 1 000 000 000 000 bajtów ≈ 931 GiB. OS nie kłamie — marketing używa mniejszej jednostki.</li>
  <li><strong>RAM używa binarnego.</strong> "8 GB RAM" to prawie zawsze 8 GiB (8 589 934 592 bajty). RAM jest budowany w potęgach dwójki.</li>
  <li><strong>Prędkość sieci jest w bitach, nie bajtach.</strong> 100 Mbps = 100 megabitów na sekundę = 12,5 MB/s w szczycie. Twoja "100 Mbit fiber" nie ściągnie pliku 100 MB w sekundę.</li>
  <li><strong>Niektóre narzędzia są niespójne.</strong> macOS Finder przeszedł z binarnego (z labelami KB) na dziesiętny w 10.6 i tam głównie został. Eksplorator Windows nadal używa binarnego z labelami KB — myląco, ale niezmiennie.</li>
  <li><strong><code>Content-Length</code> przeglądarek jest w bajtach.</strong> Zawsze dokładny, bez dwuznaczności SI/IEC.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>「4 GB ってどれくらい？」は、聞く相手で答えが変わります。HDD メーカー、ネットワーク技術者、SI に従う規格は 4,000,000,000 バイト（1000 のべき乗）を意味します。OS、RAM、多くのファイルマネージャは歴史的に 4,294,967,296 バイト（1024 のべき乗）を意味してきました。GB スケールで両者は約 7%、TB スケールで約 10% ずれます。「1 TB」のドライブが PC で「931 GiB」と表示されて損した気分になるのに十分な差です。本ツールは両系統を相互変換し、いま見ているのがどちらかを常に把握できるようにします。</p>

<h3>2 つの体系</h3>
<ul>
  <li><strong>SI / 10 進</strong> — KB、MB、GB、TB。<code>1 KB = 1,000 バイト</code>。ストレージメーカー、ネットワーク速度（Mbps、Gbps）、1960 年以来の SI 規格で使用されます。</li>
  <li><strong>IEC / 2 進</strong> — KiB、MiB、GiB、TiB。<code>1 KiB = 1,024 バイト</code>。IEC が 1998 年に曖昧さを解消するため導入。Linux の <code>du -h</code> やメモリ表示の macOS Finder などで採用されています。</li>
</ul>

<h3>使うべきタイミング</h3>
<ul>
  <li>バックアップ、アップロード、Docker イメージのサイズを見積もり、ツールの表示と突き合わせるとき。</li>
  <li>「150 Mbps」のダウンロード速度を MB/s に換算するとき（8 で割る — ビットからバイトへ）。</li>
  <li>あるクラウドプロバイダが GB、別のプロバイダが GiB を使う場合のコスト比較。</li>
  <li>「1 GB のメール」が実際にディスクで何バイト占めるかを把握したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>HDD は 10 進です。</strong> 「1 TB」ドライブは 1,000,000,000,000 バイト ≈ 931 GiB です。OS が嘘をついているのではなく、マーケティングが小さい単位を使っています。</li>
  <li><strong>RAM は 2 進です。</strong> 「8 GB RAM」はほぼ常に 8 GiB（8,589,934,592 バイト）です。RAM は 2 のべき乗で構成されます。</li>
  <li><strong>ネットワーク速度はビット単位です。</strong> 100 Mbps = 100 メガビット/秒 = 最大 12.5 MB/s。「100 Mbit 光」が 100 MB のファイルを 1 秒でダウンロードするわけではありません。</li>
  <li><strong>ツールの一貫性に乏しいことがあります。</strong> macOS Finder は 10.6 で 2 進（KB ラベル）から 10 進に切り替え、おおむね 10 進のままです。Windows Explorer は依然として 2 進を KB ラベルで表示しており、紛らわしいですが変わっていません。</li>
  <li><strong>ブラウザの <code>Content-Length</code> はバイトです。</strong> 常に厳密で、SI/IEC の曖昧さはありません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>"Hoe groot is 4 GB?" hangt af van wie het vraagt. Harde-schijf-fabrikanten, netwerkengineers en SI-volgende standaarden bedoelen 4.000.000.000 bytes (machten van 1000). Besturingssystemen, RAM-modules en de meeste filemanagers bedoelden historisch 4.294.967.296 bytes (machten van 1024). De twee getallen liggen 7% uit elkaar op gigabyte-schaal en 10% op terabyte-schaal — genoeg om je belazerd te voelen als een "1 TB"-schijf als "931 GiB" op je computer verschijnt. Deze tool converteert tussen beide systemen zodat je altijd weet welk je bekijkt.</p>

<h3>De twee systemen</h3>
<ul>
  <li><strong>SI / decimaal</strong> — KB, MB, GB, TB. <code>1 KB = 1.000 bytes</code>. Gebruikt door storage-fabrikanten, netwerksnelheden (Mbps, Gbps) en de SI-standaard sinds 1960.</li>
  <li><strong>IEC / binair</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1.024 bytes</code>. De IEC introduceerde deze in 1998 om te disambigueren. Linux <code>du</code> met <code>-h</code> gebruikt deze, net als macOS Finder voor memory.</li>
</ul>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een backup, upload of Docker image inschatten en matchen wat een tool rapporteert.</li>
  <li>"150 Mbps" downloadsnelheid converteren naar MB/s (deel door 8 — bits naar bytes).</li>
  <li>Cloud-storage kosten inschatten als de ene provider GB quoteert en de andere GiB.</li>
  <li>Uitvogelen hoeveel "1 GB" email eigenlijk is op disk.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Harde schijven gebruiken decimaal.</strong> Een "1 TB"-schijf bevat 1.000.000.000.000 bytes ≈ 931 GiB. De OS liegt niet — de marketing gebruikt de kleinere unit.</li>
  <li><strong>RAM gebruikt binair.</strong> "8 GB RAM" is bijna altijd 8 GiB (8.589.934.592 bytes). RAM wordt gebouwd in machten van twee.</li>
  <li><strong>Netwerksnelheid is in bits, geen bytes.</strong> 100 Mbps = 100 megabit per seconde = 12,5 MB/s piek. Je "100 Mbit glasvezel" downloadt geen 100 MB file in één seconde.</li>
  <li><strong>Sommige tools zijn inconsistent.</strong> macOS Finder schakelde in 10.6 van binair (met KB-labels) naar decimaal, en bleef daar grotendeels. Windows Explorer gebruikt nog steeds binair met KB-labels — verwarrend maar ongewijzigd.</li>
  <li><strong>Browsers' <code>Content-Length</code> is bytes.</strong> Altijd exact, geen SI/IEC-ambiguïteit.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>"4 GB ne kadar büyük?" kime sorduğuna bağlıdır. Sabit disk üreticileri, ağ mühendisleri ve SI standartlarını izleyenler 4.000.000.000 byte (1000'in kuvvetleri) anlamına gelir. İşletim sistemleri, RAM modülleri ve çoğu dosya yöneticisi tarihsel olarak 4.294.967.296 byte (1024'ün kuvvetleri) anlamına geliyordu. İki sayı gigabyte ölçeğinde %7, terabyte ölçeğinde %10 farklıdır — "1 TB"'lık bir sürücü bilgisayarında "931 GiB" olarak göründüğünde aldatılmış hissetmek için yeterli. Bu araç her iki sistem arasında dönüştürür, böylece her zaman hangisine baktığını bilirsin.</p>

<h3>İki sistem</h3>
<ul>
  <li><strong>SI / ondalık</strong> — KB, MB, GB, TB. <code>1 KB = 1.000 byte</code>. Depolama üreticileri, ağ hızları (Mbps, Gbps) ve 1960'tan beri SI standardı tarafından kullanılır.</li>
  <li><strong>IEC / ikilik</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1.024 byte</code>. IEC bunları belirsizliği gidermek için 1998'de tanıttı. Linux <code>du</code> <code>-h</code> ile bunları kullanır, bellek için macOS Finder de öyle.</li>
</ul>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Yedek, upload veya Docker imajını boyutlandırma ve bir aracın raporladığıyla eşleştirme.</li>
  <li>"150 Mbps" indirme hızını MB/s'ye dönüştürme (8'e böl — bit'ten byte'a).</li>
  <li>Bir sağlayıcı GB, diğeri GiB belirttiğinde bulut depolama maliyetini tahmin etme.</li>
  <li>"1 GB" e-postanın diskte aslında ne kadar olduğunu bulma.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Sabit diskler ondalık kullanır.</strong> "1 TB" sürücü 1.000.000.000.000 byte ≈ 931 GiB tutar. OS yalan söylemiyor — pazarlama daha küçük birim kullanıyor.</li>
  <li><strong>RAM ikilik kullanır.</strong> "8 GB RAM" neredeyse her zaman 8 GiB (8.589.934.592 byte)'dır. RAM ikinin kuvvetlerinde inşa edilir.</li>
  <li><strong>Ağ hızı bit'tir, byte değil.</strong> 100 Mbps = saniyede 100 megabit = tepe 12,5 MB/s. "100 Mbit fiber"in bir saniyede 100 MB dosya indirmez.</li>
  <li><strong>Bazı araçlar tutarsızdır.</strong> macOS Finder 10.6'da ikilikten (KB etiketleri ile) ondalığa geçti, sonra çoğunlukla orada kaldı. Windows Explorer hâlâ KB etiketleri ile ikilik kullanır — kafa karıştırıcı ama değişmemiş.</li>
  <li><strong>Tarayıcıların <code>Content-Length</code>'i byte'tır.</strong> Her zaman kesin, SI/IEC belirsizliği yok.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>"Seberapa besar 4 GB?" tergantung siapa yang bertanya. Pabrikan hard drive, network engineer, dan standar yang mengikuti SI berarti 4.000.000.000 byte (pangkat 1000). Operating system, modul RAM, dan kebanyakan file manager secara historis berarti 4.294.967.296 byte (pangkat 1024). Dua angka itu berbeda 7% di skala gigabyte dan 10% di skala terabyte — cukup untuk membuat kamu merasa tertipu ketika drive "1 TB" muncul sebagai "931 GiB" di komputer kamu. Tool ini mengkonversi antara kedua sistem sehingga kamu selalu tahu yang mana yang sedang kamu lihat.</p>

<h3>Dua sistem</h3>
<ul>
  <li><strong>SI / desimal</strong> — KB, MB, GB, TB. <code>1 KB = 1.000 byte</code>. Dipakai oleh pabrikan storage, kecepatan jaringan (Mbps, Gbps), dan standar SI sejak 1960.</li>
  <li><strong>IEC / biner</strong> — KiB, MiB, GiB, TiB. <code>1 KiB = 1.024 byte</code>. IEC memperkenalkan ini di 1998 untuk menghilangkan ambiguitas. Linux <code>du</code> dengan <code>-h</code> menggunakan ini, begitu juga macOS Finder untuk memory.</li>
</ul>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mengukur backup, upload, atau Docker image dan mencocokkan dengan apa yang dilaporkan tool.</li>
  <li>Mengkonversi kecepatan download "150 Mbps" menjadi MB/s (bagi 8 — bit ke byte).</li>
  <li>Mengestimasi biaya cloud storage saat satu provider mengutip GB dan yang lain mengutip GiB.</li>
  <li>Mencari tahu berapa "1 GB" email sebenarnya di disk.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Hard drive pakai desimal.</strong> Drive "1 TB" memuat 1.000.000.000.000 byte ≈ 931 GiB. OS tidak berbohong — marketing-nya yang pakai unit lebih kecil.</li>
  <li><strong>RAM pakai biner.</strong> "8 GB RAM" hampir selalu 8 GiB (8.589.934.592 byte). RAM dibangun dalam pangkat dua.</li>
  <li><strong>Kecepatan jaringan dalam bit, bukan byte.</strong> 100 Mbps = 100 megabit per detik = 12,5 MB/s puncak. "100 Mbit fiber" kamu tidak mendownload file 100 MB dalam satu detik.</li>
  <li><strong>Beberapa tool tidak konsisten.</strong> macOS Finder berganti dari biner (dengan label KB) ke desimal di 10.6, lalu sebagian besar tetap di sana. Windows Explorer masih pakai biner dengan label KB — membingungkan tapi tidak berubah.</li>
  <li><strong><code>Content-Length</code> browser itu byte.</strong> Selalu eksak, tidak ada ambiguitas SI/IEC.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>"1 KB là 1000 byte hay 1024 byte?" Câu trả lời là "có", tùy ngữ cảnh. SI và đa số tiếp thị nhà sản xuất ổ đĩa cứng dùng 1000; OS và hầu hết các tool dev dùng 1024 và gọi nó là kibibyte (KiB). Tool này chuyển đổi giữa cả hai hệ và làm rõ bạn đang nói về cái nào.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Định kích thước phân vùng đĩa khi nhà sản xuất nói "500 GB" và OS hiển thị 465 GiB.</li>
  <li>Tính budget tải xuống — quota 50 GB của ISP có nghĩa là gì trong giga-octet thực.</li>
  <li>Chuyển bytes dump của profiler thành KB/MB/GB con người đọc được.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>KB vs KiB.</strong> Đơn vị SI chính thức là kilobyte (KB) = 1000 byte. Đơn vị nhị phân là kibibyte (KiB) = 1024 byte. Hầu hết mọi người vẫn nói "KB" khi họ có ý nói KiB.</li>
  <li><strong>Tính theo decimal sai cho việc đếm byte.</strong> RAM, kích thước file và độ phân giải mạng đo theo lũy thừa của 2 — phải dùng đơn vị nhị phân.</li>
  <li><strong>Mạng dùng decimal.</strong> 100 Mbps internet có nghĩa là 100 mega<strong>bit</strong> mỗi giây = 12,5 MB/s decimal, không 12,5 MiB/s.</li>
</ul>
""",
    },
    "related": ["unit-converter", "number-base-converter", "percentage-calculator"],
    "howto": {"flow": "calculate", "action": "convert", "noun": "file size"},
}
