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
    },
    "related": ["unit-converter", "number-base-converter", "percentage-calculator"],
}
