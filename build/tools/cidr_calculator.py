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
        "ja": {"name": "CIDR / サブネット計算機", "tagline": "CIDR 表記から IPv4 サブネットを計算。ネットワーク、ブロードキャスト、マスク、ホスト範囲、バイナリ表示。", "description": "無料の IPv4 CIDR / サブネット計算ツール。任意の CIDR（例：10.0.0.0/16）を入力すると、ネットワークアドレス、ブロードキャスト、サブネットマスク、ホスト範囲、総アドレス数、バイナリ表現が確認できます。"},
        "nl": {"name": "CIDR Subnet-calculator", "tagline": "Bereken IPv4-subnetten uit CIDR-notatie. Netwerk, broadcast, mask, hostbereik en binaire weergave.", "description": "Gratis IPv4 CIDR / subnet-calculator. Voer een CIDR in (bijv. 10.0.0.0/16) en zie het netwerkadres, broadcast, subnet mask, hostbereik, totaal aantal adressen en binaire representatie."},
        "tr": {"name": "CIDR Subnet Hesaplayıcı", "tagline": "CIDR notasyonundan IPv4 alt ağlarını hesapla. Network, broadcast, mask, host aralığı ve ikilik görünüm.", "description": "Ücretsiz IPv4 CIDR / subnet hesaplayıcı. Herhangi bir CIDR gir (örn. 10.0.0.0/16) ve network adresi, broadcast, subnet mask, host aralığı, toplam adres sayısı ve ikilik gösterimi gör."},
        "id": {"name": "Kalkulator CIDR Subnet", "tagline": "Hitung subnet IPv4 dari notasi CIDR. Network, broadcast, mask, rentang host, dan tampilan biner.", "description": "Kalkulator CIDR / subnet IPv4 gratis. Masukkan CIDR apa pun (misal 10.0.0.0/16) dan lihat alamat network, broadcast, subnet mask, rentang host, total alamat, dan representasi biner."},
        "vi": {"name": "Máy tính CIDR Subnet", "tagline": "Tính subnet IPv4 từ notation CIDR. Network, broadcast, mask, dải host và biểu diễn nhị phân.", "description": "Máy tính CIDR / subnet IPv4 miễn phí. Nhập bất kỳ CIDR nào (ví dụ 10.0.0.0/16) và xem network address, broadcast, subnet mask, dải host, tổng số địa chỉ và biểu diễn nhị phân."},
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
        "ja": """
<h2>用途</h2>
<p>CIDR（Classless Inter-Domain Routing）表記は、IPv4 アドレスとそのサブネットサイズを 1 つの文字列にまとめます。<code>192.168.1.0/24</code> は「アドレス 192.168.1.0 とネットワークプレフィックス 24 ビット」を意味し、従来の <code>255.255.255.0</code> マスクと同じネットワークを 30 文字ではなく 12 文字で表現できます。このツールは任意の CIDR を、人間が理解しやすい値にデコードします。サブネットに<em>含まれる</em>アドレス、ブロードキャスト、ドット表記のマスク、そして実際にデバイスに割り当てられるホスト範囲です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>VLAN や VPC を設計し、/22 と /23 で何台のホストを収容できるかを確認するとき（1022 対 510）。</li>
  <li><code>allow 10.42.0.0/16</code> のようなファイアウォールルールを読んで、カバーする範囲を正確に把握したいとき。</li>
  <li>/24 を小さなサブネットに分割し、境界が重ならないか確認するとき。</li>
  <li>クラウドのセキュリティグループルールをデプロイ前にサニティチェックするとき。</li>
  <li>ルーター設定で、CIDR と従来の <code>255.x.x.x</code> ドット表記マスクを相互に変換するとき。</li>
</ul>

<h3>CIDR クイックチートシート</h3>
<ul>
  <li><strong>/32</strong> — 1 アドレス（単一ホストルート）。</li>
  <li><strong>/30</strong> — 4 アドレス、使用可能 2（ポイント・ツー・ポイントリンク）。</li>
  <li><strong>/29</strong> — 8 アドレス、使用可能 6（小規模オフィスのサブネット）。</li>
  <li><strong>/24</strong> — 256 アドレス、使用可能 254（典型的なクラス C / 一般的な LAN）。</li>
  <li><strong>/16</strong> — 65,536 アドレス（拠点ネットワークや VPC によくあるサイズ）。</li>
  <li><strong>/8</strong> — 1,670 万アドレス（組織全体規模）。</li>
  <li><strong>/0</strong> — すべての IPv4 アドレス（デフォルトルート）。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>「使用可能」にはネットワークとブロードキャストは含まれません。</strong> /24 は 256 アドレスありますが、ホスト用に使えるのは 254 だけです。最初（.0）はネットワーク、最後（.255）はブロードキャストです。</li>
  <li><strong>/31 と /32 は特別です。</strong> /31 は RFC 3021 によりポイント・ツー・ポイントリンクで使われ、両方のアドレスが使用可能です。/32 は単一ホストで、ルーティングエントリで使われます。</li>
  <li><strong>アドレス部分はネットワークアドレスである必要はありません。</strong> <code>10.5.7.42/24</code> は <code>10.5.7.0/24</code> と同じ /24 を意味します。重要なのはプレフィックス長です。このツールは出力時にネットワークアドレスへ正規化します。</li>
  <li><strong>クラスと CIDR を混同しないこと。</strong> クラス A/B/C は 1993 年以前の古い概念です。/24 が「クラス A」の範囲に含まれていても問題ありません。</li>
  <li><strong>RFC 1918 のプライベート範囲：</strong> <code>10.0.0.0/8</code>、<code>172.16.0.0/12</code>、<code>192.168.0.0/16</code>。これら以外はパブリックにルーティング可能（または予約済み）です。</li>
  <li><strong>このツールは IPv4 専用です。</strong> IPv6 CIDR は構造的には似ていますが、プレフィックスは /128 まで可能でアドレス空間も格段に大きく、ここでは扱いません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>CIDR (Classless Inter-Domain Routing)-notatie pakt een IPv4-adres en de subnetgrootte in één string: <code>192.168.1.0/24</code> betekent "het adres 192.168.1.0 met een 24-bit netwerk-prefix" — hetzelfde netwerk als het oudere <code>255.255.255.0</code> mask, maar geschreven in 12 tekens in plaats van 30. Deze tool decodeert elke CIDR in de menselijk leesbare waarden: welke adressen <em>in</em> het subnet zitten, het broadcast, het mask in dotted-vorm en het hostbereik dat je daadwerkelijk aan apparaten kunt toewijzen.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een VLAN of VPC ontwerpen en uitzoeken hoeveel hosts een /22 vs /23 herbergt (1022 vs 510).</li>
  <li>Een firewallregel lezen als <code>allow 10.42.0.0/16</code> en het exacte bereik bevestigen dat die afdekt.</li>
  <li>Een /24 opsplitsen in kleinere subnets en checken dat de grenzen niet overlappen.</li>
  <li>Sanity check op een cloud security-group rule voor je deployt.</li>
  <li>Vertalen tussen CIDR en een legacy <code>255.x.x.x</code> dotted mask in routerconfigs.</li>
</ul>

<h3>Korte CIDR-spiekbrief</h3>
<ul>
  <li><strong>/32</strong> — 1 adres (een enkele host-route).</li>
  <li><strong>/30</strong> — 4 adressen, 2 bruikbaar (point-to-point links).</li>
  <li><strong>/29</strong> — 8 adressen, 6 bruikbaar (klein kantoor-subnet).</li>
  <li><strong>/24</strong> — 256 adressen, 254 bruikbaar (klassieke Class C / typisch LAN).</li>
  <li><strong>/16</strong> — 65.536 adressen (typisch site-netwerk of VPC).</li>
  <li><strong>/8</strong> — 16,7M adressen (hele organisatie).</li>
  <li><strong>/0</strong> — elk IPv4-adres (de default route).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>"Bruikbaar" sluit netwerk en broadcast uit.</strong> Een /24 heeft 256 adressen maar maar 254 bruikbaar voor hosts — de eerste (.0) is het netwerk, de laatste (.255) is de broadcast.</li>
  <li><strong>/31 en /32 zijn speciaal.</strong> /31 wordt gebruikt voor point-to-point links volgens RFC 3021 — beide adressen zijn bruikbaar. /32 is een enkele host (gebruikt in routingentries).</li>
  <li><strong>Het adresdeel hoeft niet het netwerkadres te zijn.</strong> <code>10.5.7.42/24</code> betekent nog steeds dezelfde /24 als <code>10.5.7.0/24</code> — wat telt is de prefixlengte. De tool normaliseert in zijn output naar het netwerkadres.</li>
  <li><strong>Verwar class niet met CIDR.</strong> Klassen A/B/C zijn een legacy-concept (van vóór 1993). Een /24 kan binnen een "class A"-bereik vallen en dat is prima.</li>
  <li><strong>RFC 1918 private ranges:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Al het andere is publiek routeerbaar (of gereserveerd).</li>
  <li><strong>Deze tool is alleen IPv4.</strong> IPv6 CIDR is structureel vergelijkbaar maar de prefix kan tot /128 gaan en de adresruimte is veel groter; hier niet ondersteund.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>CIDR (Classless Inter-Domain Routing) notasyonu bir IPv4 adresini ve subnet boyutunu tek bir string'e paketler: <code>192.168.1.0/24</code> "24-bit network prefix ile 192.168.1.0 adresi" anlamına gelir — eski <code>255.255.255.0</code> mask ile aynı ağ, ama 30 yerine 12 karakterde yazılır. Bu araç herhangi bir CIDR'yi insan tarafından anlamlı değerlere çözer: subnet <em>içindeki</em> adresler, broadcast, noktalı biçimde mask ve cihazlara gerçekten atayabileceğin host aralığı.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir VLAN veya VPC tasarlarken ve /22 ile /23'ün kaç host tutacağını (1022 - 510) hesaplarken.</li>
  <li><code>allow 10.42.0.0/16</code> gibi bir firewall kuralı okurken ve tam olarak hangi aralığı kapsadığını doğrularken.</li>
  <li>Bir /24'ü daha küçük subnet'lere bölüp sınırların çakışmadığını kontrol ederken.</li>
  <li>Deploy etmeden önce bir cloud security-group kuralının sanity check'i.</li>
  <li>Router config'lerinde CIDR ile eski <code>255.x.x.x</code> noktalı mask arasında çeviri yapma.</li>
</ul>

<h3>Hızlı CIDR çetel</h3>
<ul>
  <li><strong>/32</strong> — 1 adres (tek host route).</li>
  <li><strong>/30</strong> — 4 adres, 2 kullanılabilir (point-to-point linkler).</li>
  <li><strong>/29</strong> — 8 adres, 6 kullanılabilir (küçük ofis subnet'i).</li>
  <li><strong>/24</strong> — 256 adres, 254 kullanılabilir (klasik Class C / tipik LAN).</li>
  <li><strong>/16</strong> — 65.536 adres (tipik site ağı veya VPC).</li>
  <li><strong>/8</strong> — 16,7M adres (tüm bir kurum).</li>
  <li><strong>/0</strong> — her IPv4 adresi (default route).</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>"Kullanılabilir" network ve broadcast'i hariç tutar.</strong> Bir /24'te 256 adres vardır ama host'lar için sadece 254 kullanılabilir — ilki (.0) network'tür, sonuncu (.255) broadcast'tir.</li>
  <li><strong>/31 ve /32 özeldir.</strong> /31 RFC 3021'e göre point-to-point linkler için kullanılır — her iki adres de kullanılabilir. /32 tek bir host'tur (routing girdilerinde kullanılır).</li>
  <li><strong>Adres kısmının network adresi olması gerekmez.</strong> <code>10.5.7.42/24</code> hâlâ <code>10.5.7.0/24</code> ile aynı /24 demektir — önemli olan prefix uzunluğudur. Araç çıktıda network adresine normalize eder.</li>
  <li><strong>Class ve CIDR'yi karıştırma.</strong> A/B/C sınıfları eski (1993 öncesi) bir kavramdır. Bir /24 "class A" aralığına düşebilir ve bu sorun değildir.</li>
  <li><strong>RFC 1918 özel aralıkları:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Başka her şey kamuya açık şekilde routable'dır (veya rezervedir).</li>
  <li><strong>Bu araç sadece IPv4'tür.</strong> IPv6 CIDR yapısal olarak benzer ama prefix /128'e kadar çıkabilir ve adres alanı çok daha büyüktür; burada işlenmez.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Notasi CIDR (Classless Inter-Domain Routing) mengemas alamat IPv4 dan ukuran subnet-nya menjadi satu string: <code>192.168.1.0/24</code> berarti "alamat 192.168.1.0 dengan prefix network 24-bit" — network yang sama dengan mask lama <code>255.255.255.0</code>, tapi ditulis dalam 12 karakter, bukan 30. Tool ini mendekode CIDR apa pun menjadi nilai-nilai yang bermakna: alamat mana yang <em>di dalam</em> subnet, broadcast, mask dalam bentuk titik, dan rentang host yang benar-benar bisa kamu tetapkan ke perangkat.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mendesain VLAN atau VPC dan menghitung berapa host yang ditampung /22 vs /23 (1022 vs 510).</li>
  <li>Membaca aturan firewall seperti <code>allow 10.42.0.0/16</code> dan memastikan rentang persisnya.</li>
  <li>Memecah /24 menjadi subnet lebih kecil dan memeriksa batas tidak tumpang tindih.</li>
  <li>Sanity check aturan security group cloud sebelum deploy.</li>
  <li>Menerjemahkan antara CIDR dan mask titik <code>255.x.x.x</code> lama di config router.</li>
</ul>

<h3>Cheat sheet CIDR</h3>
<ul>
  <li><strong>/32</strong> — 1 alamat (rute host tunggal).</li>
  <li><strong>/30</strong> — 4 alamat, 2 dapat dipakai (link point-to-point).</li>
  <li><strong>/29</strong> — 8 alamat, 6 dapat dipakai (subnet kantor kecil).</li>
  <li><strong>/24</strong> — 256 alamat, 254 dapat dipakai (Class C klasik / LAN tipikal).</li>
  <li><strong>/16</strong> — 65.536 alamat (network site tipikal atau VPC).</li>
  <li><strong>/8</strong> — 16,7M alamat (seluruh organisasi).</li>
  <li><strong>/0</strong> — semua alamat IPv4 (default route).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>"Dapat dipakai" tidak termasuk network dan broadcast.</strong> /24 punya 256 alamat tapi hanya 254 untuk host — yang pertama (.0) adalah network, yang terakhir (.255) adalah broadcast.</li>
  <li><strong>/31 dan /32 itu khusus.</strong> /31 dipakai untuk link point-to-point per RFC 3021 — kedua alamat dapat dipakai. /32 adalah host tunggal (dipakai di entry routing).</li>
  <li><strong>Bagian alamat tidak harus alamat network.</strong> <code>10.5.7.42/24</code> tetap berarti /24 yang sama dengan <code>10.5.7.0/24</code> — yang dihitung adalah panjang prefix. Tool ini menormalisasi ke alamat network di output-nya.</li>
  <li><strong>Jangan campur class dengan CIDR.</strong> Class A/B/C adalah konsep legacy (sebelum 1993).</li>
  <li><strong>Rentang private RFC 1918:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Selain itu routable secara publik (atau direservasi).</li>
  <li><strong>Tool ini hanya IPv4.</strong> CIDR IPv6 secara struktural mirip tapi prefix bisa sampai /128 dan ruang alamat jauh lebih besar; tidak ditangani di sini.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Notation CIDR (Classless Inter-Domain Routing) đóng gói một địa chỉ IPv4 và kích thước subnet của nó thành một chuỗi duy nhất: <code>192.168.1.0/24</code> nghĩa là "địa chỉ 192.168.1.0 với prefix network 24-bit" — cùng một network như mask <code>255.255.255.0</code> cũ, nhưng viết bằng 12 ký tự thay vì 30. Công cụ này giải mã bất kỳ CIDR nào thành các giá trị có ý nghĩa: địa chỉ nào <em>thuộc</em> subnet, broadcast, mask dạng dot và dải host bạn thực sự có thể gán cho thiết bị.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Thiết kế VLAN hoặc VPC và tính xem /22 vs /23 chứa được bao nhiêu host (1022 vs 510).</li>
  <li>Đọc quy tắc firewall như <code>allow 10.42.0.0/16</code> và xác minh dải chính xác.</li>
  <li>Chia /24 thành các subnet nhỏ hơn và kiểm tra biên không chồng chéo.</li>
  <li>Sanity check quy tắc security group cloud trước khi deploy.</li>
  <li>Chuyển đổi giữa CIDR và mask dot <code>255.x.x.x</code> cũ trong cấu hình router.</li>
</ul>

<h3>Cheat sheet CIDR</h3>
<ul>
  <li><strong>/32</strong> — 1 địa chỉ (route host đơn).</li>
  <li><strong>/30</strong> — 4 địa chỉ, 2 có thể dùng (link point-to-point).</li>
  <li><strong>/29</strong> — 8 địa chỉ, 6 có thể dùng (subnet văn phòng nhỏ).</li>
  <li><strong>/24</strong> — 256 địa chỉ, 254 có thể dùng (Class C cổ điển / LAN điển hình).</li>
  <li><strong>/16</strong> — 65.536 địa chỉ (network site hoặc VPC điển hình).</li>
  <li><strong>/8</strong> — 16,7M địa chỉ (toàn tổ chức).</li>
  <li><strong>/0</strong> — toàn bộ địa chỉ IPv4 (default route).</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>"Có thể dùng" không bao gồm network và broadcast.</strong> /24 có 256 địa chỉ nhưng chỉ 254 cho host — địa chỉ đầu tiên (.0) là network, cuối cùng (.255) là broadcast.</li>
  <li><strong>/31 và /32 là đặc biệt.</strong> /31 được dùng cho link point-to-point theo RFC 3021 — cả hai địa chỉ đều có thể dùng. /32 là một host đơn (dùng trong entry routing).</li>
  <li><strong>Phần địa chỉ không phải lúc nào cũng là địa chỉ network.</strong> <code>10.5.7.42/24</code> vẫn nghĩa là cùng /24 như <code>10.5.7.0/24</code> — chỉ độ dài prefix mới quan trọng. Công cụ này chuẩn hóa thành địa chỉ network ở output.</li>
  <li><strong>Đừng trộn class với CIDR.</strong> Class A/B/C là khái niệm legacy (trước 1993).</li>
  <li><strong>Dải private RFC 1918:</strong> <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>. Mọi thứ khác đều có thể route công khai (hoặc dành riêng).</li>
  <li><strong>Công cụ này chỉ dành cho IPv4.</strong> CIDR IPv6 cấu trúc tương tự nhưng prefix có thể đi đến /128 và không gian địa chỉ lớn hơn nhiều; không được xử lý ở đây.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "regex-tester", "json-formatter"],
    "howto": {"flow": "calculate", "action": "format", "noun": "CIDR"},
}
