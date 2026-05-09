TOOL = {
    "slug": "cidr-calculator",
    "category": "developer",
    "icon": "🌐",
    "tags": ["cidr", "subnet", "ipv4", "network", "mask", "ip", "calculator"],
    "i18n": {
        "en": {
            "name": "CIDR Subnet Calculator",
            "tagline": "Compute IPv4 subnets from CIDR notation. Network, broadcast, mask, host range, and binary view.",
            "description": "Free IPv4 CIDR / subnet calculator. Enter any CIDR (e.g. 10.0.0.0/16) and see the network address, broadcast, subnet mask, host range, total addresses, and binary representation.",
        },
        "de": {"name": "CIDR-Subnetz-Rechner", "tagline": "Berechne IPv4-Subnetze aus CIDR-Notation. Netz, Broadcast, Maske, Host-Bereich und Binärdarstellung.", "description": "Kostenloser IPv4 CIDR / Subnetz-Rechner. Gib einen CIDR ein (z.B. 10.0.0.0/16) und sieh Netzadresse, Broadcast, Subnetzmaske, Host-Bereich, Gesamtadressen und Binärdarstellung."},
        "es": {"name": "Calculadora CIDR / Subred", "tagline": "Calcula subredes IPv4 desde notación CIDR. Red, broadcast, máscara, rango de hosts y vista binaria.", "description": "Calculadora gratuita IPv4 CIDR / subred. Introduce un CIDR (p.ej. 10.0.0.0/16) y obtén dirección de red, broadcast, máscara, rango de hosts y representación binaria."},
        "fr": {"name": "Calculateur CIDR / Sous-réseau", "tagline": "Calculez les sous-réseaux IPv4 depuis la notation CIDR. Réseau, broadcast, masque, plage d'hôtes, vue binaire.", "description": "Calculateur gratuit IPv4 CIDR / sous-réseau. Entrez un CIDR (ex: 10.0.0.0/16) et obtenez adresse réseau, broadcast, masque, plage d'hôtes et représentation binaire."},
        "it": {"name": "Calcolatore CIDR / Subnet", "tagline": "Calcola subnet IPv4 dalla notazione CIDR. Rete, broadcast, maschera, intervallo host, vista binaria.", "description": "Calcolatore gratuito IPv4 CIDR / subnet. Inserisci un CIDR (es. 10.0.0.0/16) e ottieni indirizzo di rete, broadcast, maschera, intervallo host e rappresentazione binaria."},
    },
    "body": """
<div class="tool-card">
  <label>CIDR notation</label>
  <input type="text" id="cidr-in" oninput="cidrRun()" placeholder="192.168.1.0/24" value="192.168.1.0/24" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
  <div class="meta" style="margin-top:0.4rem">Example: <code>10.0.0.0/16</code>, <code>172.16.5.0/24</code>, <code>203.0.113.42/29</code></div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <pre class="output" id="cidr-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function cidrParse(s){
  s = (s||'').trim();
  const m = s.match(/^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\/(\\d{1,2})$/);
  if(!m) return null;
  const oct = [+m[1],+m[2],+m[3],+m[4]];
  const pfx = +m[5];
  if(oct.some(n => n<0 || n>255)) return null;
  if(pfx < 0 || pfx > 32) return null;
  return {oct, pfx};
}
function cidrToInt(oct){ return ((oct[0]<<24) | (oct[1]<<16) | (oct[2]<<8) | oct[3]) >>> 0 }
function intToCidr(n){ return [(n>>>24)&0xff, (n>>>16)&0xff, (n>>>8)&0xff, n&0xff].join('.') }
function intToBin(n){
  const b = (n>>>0).toString(2).padStart(32,'0');
  return b.match(/.{8}/g).join('.');
}
function cidrClass(o){
  if(o[0] >= 224) return 'D / E (multicast / experimental)';
  if(o[0] >= 192) return 'C';
  if(o[0] >= 128) return 'B';
  return 'A';
}
function cidrPrivate(n){
  // 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
  if((n & 0xff000000) === 0x0a000000) return true;
  if((n & 0xfff00000) === 0xac100000) return true;
  if((n & 0xffff0000) === 0xc0a80000) return true;
  return false;
}
function cidrRun(){
  const out = document.getElementById('cidr-out');
  out.classList.remove('error');
  const p = cidrParse(document.getElementById('cidr-in').value);
  if(!p){ out.classList.add('error'); out.textContent = '✗ Invalid CIDR — expected e.g. 192.168.1.0/24'; return; }
  const ip = cidrToInt(p.oct);
  const mask = p.pfx === 0 ? 0 : (0xffffffff << (32 - p.pfx)) >>> 0;
  const wildcard = (~mask) >>> 0;
  const network = (ip & mask) >>> 0;
  const broadcast = (network | wildcard) >>> 0;
  const total = Math.pow(2, 32 - p.pfx);
  let firstHost, lastHost, usable;
  if(p.pfx >= 31){
    firstHost = network;
    lastHost = broadcast;
    usable = p.pfx === 32 ? 1 : 2;
  } else {
    firstHost = (network + 1) >>> 0;
    lastHost = (broadcast - 1) >>> 0;
    usable = total - 2;
  }
  const lines = [
    `CIDR:           ${intToCidr(ip)}/${p.pfx}`,
    `Network:        ${intToCidr(network)}`,
    `Broadcast:      ${intToCidr(broadcast)}`,
    `Subnet mask:    ${intToCidr(mask)}`,
    `Wildcard mask:  ${intToCidr(wildcard)}`,
    ``,
    `First host:     ${intToCidr(firstHost)}`,
    `Last host:      ${intToCidr(lastHost)}`,
    `Usable hosts:   ${usable.toLocaleString()}`,
    `Total addrs:    ${total.toLocaleString()}`,
    ``,
    `Class:          ${cidrClass(p.oct)}`,
    `Private RFC1918: ${cidrPrivate(network) ? 'yes' : 'no'}`,
    ``,
    `Binary:`,
    `  IP:    ${intToBin(ip)}`,
    `  Mask:  ${intToBin(mask)}`,
    `  Net:   ${intToBin(network)}`,
  ];
  out.textContent = lines.join('\\n');
}
document.addEventListener('DOMContentLoaded', cidrRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>CIDR (Classless Inter-Domain Routing) notation packs an IPv4 address and its subnet size into one string: <code>192.168.1.0/24</code> means "the address 192.168.1.0 with a 24-bit network prefix" — the same network as the older <code>255.255.255.0</code> mask, but written in 12 characters instead of 30. This tool decodes any CIDR into the human-meaningful values: which addresses are <em>in</em> the subnet, the broadcast, the mask in dotted form, and the host range you can actually assign to devices.</p>

<h3>When to use it</h3>
<ul>
  <li>Designing a VLAN or VPC and figuring out how many hosts a /22 vs /23 will hold (1022 vs 510).</li>
  <li>Reading a firewall rule like <code>allow 10.42.0.0/16</code> and confirming the exact range it covers.</li>
  <li>Splitting a /24 into smaller subnets and checking the boundaries don't overlap.</li>
  <li>Sanity-checking a cloud security-group rule before deploying.</li>
  <li>Translating between CIDR and a legacy <code>255.x.x.x</code> dotted mask in router configs.</li>
</ul>

<h3>Quick CIDR cheat sheet</h3>
<ul>
  <li><strong>/32</strong> — 1 address (a single host route).</li>
  <li><strong>/30</strong> — 4 addresses, 2 usable (point-to-point links).</li>
  <li><strong>/29</strong> — 8 addresses, 6 usable (small office subnet).</li>
  <li><strong>/24</strong> — 256 addresses, 254 usable (classic Class C / typical LAN).</li>
  <li><strong>/16</strong> — 65,536 addresses (typical site network or VPC).</li>
  <li><strong>/8</strong> — 16.7M addresses (whole-of-organisation).</li>
  <li><strong>/0</strong> — every IPv4 address (the default route).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>"Usable" excludes network and broadcast.</strong> A /24 has 256 addresses but only 254 usable for hosts — the first (.0) is the network, the last (.255) is the broadcast.</li>
  <li><strong>/31 and /32 are special.</strong> /31 is used for point-to-point links per RFC 3021 — both addresses are usable. /32 is a single host (used in routing entries).</li>
  <li><strong>The address part doesn't have to be the network address.</strong> <code>10.5.7.42/24</code> still means the same /24 as <code>10.5.7.0/24</code> — the prefix length is what counts. The tool normalises to the network address in its output.</li>
  <li><strong>Don't confuse class with CIDR.</strong> Classes A/B/C are a legacy concept (pre-1993). A /24 might fall inside a "class A" range and that's fine.</li>
  <li><strong>RFC 1918 private ranges:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Anything else is publicly-routable (or reserved).</li>
  <li><strong>This tool is IPv4 only.</strong> IPv6 CIDR is structurally similar but the prefix can go up to /128 and the address space is much bigger; not handled here.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "regex-tester", "json-formatter"],
}
