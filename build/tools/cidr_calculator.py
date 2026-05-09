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
        "pt": {"name": "Calculadora CIDR / Subnet", "tagline": "Calcule subnets IPv4 a partir da notação CIDR. Network, broadcast, máscara, faixa de hosts e visão binária.", "description": "Calculadora gratuita de CIDR / subnet IPv4. Informe qualquer CIDR (ex.: 10.0.0.0/16) e veja o endereço de rede, broadcast, máscara de subnet, faixa de hosts, total de endereços e representação binária."},
        "pl": {"name": "Kalkulator CIDR / Subnet", "tagline": "Liczy podsieci IPv4 z notacji CIDR. Sieć, broadcast, maska, zakres hostów i widok binarny.", "description": "Darmowy kalkulator CIDR / podsieci IPv4. Wpisz dowolny CIDR (np. 10.0.0.0/16) i zobacz adres sieci, broadcast, maskę podsieci, zakres hostów, łączną liczbę adresów i reprezentację binarną."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>A notação CIDR (Classless Inter-Domain Routing) empacota um endereço IPv4 e o tamanho da sua subnet em uma única string: <code>192.168.1.0/24</code> significa "o endereço 192.168.1.0 com prefixo de rede de 24 bits" — a mesma rede que a antiga máscara <code>255.255.255.0</code>, mas escrita em 12 caracteres em vez de 30. Esta ferramenta decodifica qualquer CIDR nos valores legíveis para humanos: quais endereços estão <em>dentro</em> da subnet, o broadcast, a máscara em formato pontuado e a faixa de hosts que você de fato pode atribuir aos dispositivos.</p>

<h3>Quando usar</h3>
<ul>
  <li>Projetar uma VLAN ou VPC e descobrir quantos hosts um /22 vs /23 comporta (1.022 vs 510).</li>
  <li>Ler uma regra de firewall como <code>allow 10.42.0.0/16</code> e confirmar a faixa exata que ela cobre.</li>
  <li>Dividir um /24 em subnets menores e checar que os limites não se sobrepõem.</li>
  <li>Conferir uma regra de security group de cloud antes de fazer deploy.</li>
  <li>Traduzir entre CIDR e uma máscara pontuada legada <code>255.x.x.x</code> em configs de roteador.</li>
</ul>

<h3>Cola rápida de CIDR</h3>
<ul>
  <li><strong>/32</strong> — 1 endereço (uma rota de host único).</li>
  <li><strong>/30</strong> — 4 endereços, 2 utilizáveis (links ponto a ponto).</li>
  <li><strong>/29</strong> — 8 endereços, 6 utilizáveis (subnet de pequeno escritório).</li>
  <li><strong>/24</strong> — 256 endereços, 254 utilizáveis (clássico Class C / LAN típica).</li>
  <li><strong>/16</strong> — 65.536 endereços (rede típica de site ou VPC).</li>
  <li><strong>/8</strong> — 16,7M endereços (toda uma organização).</li>
  <li><strong>/0</strong> — todos os endereços IPv4 (a rota padrão).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>"Utilizáveis" exclui network e broadcast.</strong> Um /24 tem 256 endereços mas apenas 254 utilizáveis para hosts — o primeiro (.0) é a rede, o último (.255) é o broadcast.</li>
  <li><strong>/31 e /32 são especiais.</strong> /31 é usado para links ponto a ponto pela RFC 3021 — ambos os endereços são utilizáveis. /32 é um host único (usado em entradas de roteamento).</li>
  <li><strong>A parte do endereço não precisa ser o endereço de rede.</strong> <code>10.5.7.42/24</code> ainda significa o mesmo /24 que <code>10.5.7.0/24</code> — o que conta é o tamanho do prefixo. A ferramenta normaliza para o endereço de rede na saída.</li>
  <li><strong>Não confunda classe com CIDR.</strong> Classes A/B/C são um conceito legado (pré-1993). Um /24 pode cair dentro de uma faixa "classe A" e tudo bem.</li>
  <li><strong>Faixas privadas RFC 1918:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Qualquer coisa fora disso é roteável publicamente (ou reservada).</li>
  <li><strong>Esta ferramenta é apenas IPv4.</strong> CIDR IPv6 é estruturalmente parecido mas o prefixo pode ir até /128 e o espaço de endereços é muito maior; não é tratado aqui.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Notacja CIDR (Classless Inter-Domain Routing) pakuje adres IPv4 i rozmiar jego podsieci w jeden ciąg: <code>192.168.1.0/24</code> oznacza "adres 192.168.1.0 z 24-bitowym prefiksem sieci" — tę samą sieć co stara maska <code>255.255.255.0</code>, tylko zapisana w 12 znakach zamiast 30. To narzędzie dekoduje dowolny CIDR do wartości czytelnych dla człowieka: które adresy są <em>w</em> podsieci, broadcast, maska w formie kropkowej i zakres hostów, który faktycznie możesz przypisać urządzeniom.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Projektujesz VLAN albo VPC i sprawdzasz, ile hostów zmieści /22 vs /23 (1022 vs 510).</li>
  <li>Czytasz regułę firewalla typu <code>allow 10.42.0.0/16</code> i chcesz potwierdzić dokładny zakres, jaki obejmuje.</li>
  <li>Dzielisz /24 na mniejsze podsieci i sprawdzasz, czy granice się nie nakładają.</li>
  <li>Sanity check reguły security group w chmurze przed deployem.</li>
  <li>Tłumaczysz między CIDR a starą maską kropkową <code>255.x.x.x</code> w configu routera.</li>
</ul>

<h3>Szybka ściąga CIDR</h3>
<ul>
  <li><strong>/32</strong> — 1 adres (pojedyncza trasa hosta).</li>
  <li><strong>/30</strong> — 4 adresy, 2 użyteczne (linki point-to-point).</li>
  <li><strong>/29</strong> — 8 adresów, 6 użytecznych (mała podsieć biurowa).</li>
  <li><strong>/24</strong> — 256 adresów, 254 użyteczne (klasyczna klasa C / typowy LAN).</li>
  <li><strong>/16</strong> — 65 536 adresów (typowa sieć oddziału lub VPC).</li>
  <li><strong>/8</strong> — 16,7 mln adresów (cała organizacja).</li>
  <li><strong>/0</strong> — wszystkie adresy IPv4 (default route).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>"Użyteczne" nie obejmuje sieci i broadcastu.</strong> /24 ma 256 adresów, ale tylko 254 użyteczne dla hostów — pierwszy (.0) to sieć, ostatni (.255) to broadcast.</li>
  <li><strong>/31 i /32 są specjalne.</strong> /31 jest używany dla linków point-to-point wg RFC 3021 — oba adresy są użyteczne. /32 to pojedynczy host (używany w wpisach routingu).</li>
  <li><strong>Część adresowa nie musi być adresem sieci.</strong> <code>10.5.7.42/24</code> nadal oznacza tę samą /24 co <code>10.5.7.0/24</code> — liczy się długość prefiksu. Narzędzie normalizuje to do adresu sieci na wyjściu.</li>
  <li><strong>Nie myl klasy z CIDR.</strong> Klasy A/B/C to koncept legacy (sprzed 1993). /24 może wpaść w zakres "klasy A" i to jest OK.</li>
  <li><strong>Prywatne zakresy RFC 1918:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Wszystko poza nimi jest publicznie routowalne (albo zarezerwowane).</li>
  <li><strong>To narzędzie obsługuje tylko IPv4.</strong> CIDR IPv6 jest strukturalnie podobny, ale prefiks może iść aż do /128 i przestrzeń adresowa jest znacznie większa; tu nie jest obsługiwane.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "regex-tester", "json-formatter"],
}
