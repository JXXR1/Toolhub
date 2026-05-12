TOOL = {
    "slug": "number-base-converter",
    "category": "developer",
    "icon": "0b",
    "tags": ["binary", "hex", "octal", "decimal", "base", "convert", "number"],
    "i18n": {
        "en": {
            "name": "Number Base Converter",
            "tagline": "Convert between binary, octal, decimal, hexadecimal, and any base from 2 to 36.",
            "description": "Free online number base converter. Convert between binary, octal, decimal, hex, and arbitrary bases 2-36. Handles negative numbers and large integers via BigInt.",
        },
        "de": {
            "name": "Zahlensystem-Konverter",
            "tagline": "Konvertiere zwischen binär, oktal, dezimal, hexadezimal und beliebigen Basen von 2 bis 36.",
            "description": "Kostenloser Zahlensystem-Konverter. Konvertiere zwischen binär, oktal, dezimal, hexadezimal und beliebiger Basis 2-36. Auch negative und große Zahlen via BigInt.",
        },
        "es": {
            "name": "Conversor de Bases Numéricas",
            "tagline": "Convierte entre binario, octal, decimal, hexadecimal y cualquier base de 2 a 36.",
            "description": "Conversor gratuito de bases numéricas. Convierte entre binario, octal, decimal, hexadecimal y cualquier base 2-36. Soporta negativos y enteros grandes con BigInt.",
        },
        "fr": {
            "name": "Convertisseur de Bases",
            "tagline": "Convertissez entre binaire, octal, décimal, hexadécimal et toute base de 2 à 36.",
            "description": "Convertisseur de bases numériques gratuit. Convertissez entre binaire, octal, décimal, hex et bases arbitraires 2-36. Gère les nombres négatifs et grands entiers via BigInt.",
        },
        "it": {
            "name": "Convertitore Basi Numeriche",
            "tagline": "Converti tra binario, ottale, decimale, esadecimale e qualsiasi base da 2 a 36.",
            "description": "Convertitore gratuito di basi numeriche. Converti tra binario, ottale, decimale, esadecimale e basi arbitrarie 2-36. Supporta negativi e interi grandi con BigInt.",
        },
        "pt": {
            "name": "Conversor de Bases Numéricas",
            "tagline": "Converta entre binary, octal, decimal, hexadecimal e qualquer base de 2 a 36.",
            "description": "Conversor de bases numéricas gratuito online. Converta entre binary, octal, decimal, hex e bases arbitrárias de 2 a 36. Lida com números negativos e inteiros grandes via BigInt.",
        },
        "pl": {
            "name": "Konwerter Systemów Liczbowych",
            "tagline": "Konwertuj między binarnym, oktalnym, dziesiętnym, szesnastkowym i dowolną bazą od 2 do 36.",
            "description": "Darmowy online konwerter systemów liczbowych. Konwertuj między binary, octal, decimal, hex i dowolną bazą 2-36. Obsługuje liczby ujemne i duże integery przez BigInt.",
        },
        "ja": {
            "name": "進数変換ツール",
            "tagline": "2 進・8 進・10 進・16 進、および 2〜36 の任意の基数を相互変換。",
            "description": "オンライン無料の進数変換ツール。2 進、8 進、10 進、16 進、そして 2〜36 の任意の基数を相互変換できます。負数や大きな整数も BigInt によって扱えます。",
        },
        "nl": {"name": "Getalstelsel-converter", "tagline": "Converteer tussen binair, octaal, decimaal, hexadecimaal en elk grondtal van 2 tot 36.", "description": "Gratis online converter voor getalstelsels. Converteer tussen binair, octaal, decimaal, hex en willekeurige grondtallen 2-36. Verwerkt negatieve getallen en grote integers via BigInt."},
        "tr": {"name": "Sayı Tabanı Dönüştürücü", "tagline": "İkilik, sekizlik, ondalık, onaltılık ve 2'den 36'ya kadar her taban arasında dönüştür.", "description": "Ücretsiz online sayı tabanı dönüştürücü. İkilik, sekizlik, ondalık, hex ve 2-36 arası rastgele tabanlar arasında dönüştür. BigInt üzerinden negatif sayıları ve büyük tamsayıları işler."},
        "id": {"name": "Konverter Basis Angka", "tagline": "Konversi antara biner, oktal, desimal, heksadesimal, dan basis 2 sampai 36.", "description": "Konverter basis angka gratis. Konversi antara biner (basis-2), oktal (basis-8), desimal (basis-10), heksadesimal (basis-16), dan basis arbitrer 2 sampai 36. Pengubah basis-N umum untuk programmer."},
        "vi": {"name": "Chuyển đổi Hệ cơ số", "tagline": "Chuyển giữa nhị phân, bát phân, thập phân, thập lục phân và các hệ cơ số 2 đến 36.", "description": "Bộ chuyển đổi hệ cơ số miễn phí trực tuyến. Chuyển bất kỳ số nào giữa nhị phân, bát phân, thập phân, thập lục phân và các hệ cơ số 2 đến 36. Bao gồm hỗ trợ số âm."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_INPUT}</label>
      <input type="text" id="nb-in" oninput="nbRun()" placeholder="42" value="42" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>{LBL_FROM} (base)</label>
      <select id="nb-from" onchange="nbRun()">
        <option value="2">2 — binary</option>
        <option value="8">8 — octal</option>
        <option value="10" selected>10 — decimal</option>
        <option value="16">16 — hexadecimal</option>
        <option value="36">36</option>
        <option value="other">Other (2-36)…</option>
      </select>
      <input type="number" id="nb-from-other" min="2" max="36" placeholder="custom base" oninput="nbRun()" style="display:none;margin-top:0.4rem">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>All bases</label>
  <table>
    <tr><th style="width:140px">Base</th><th>Value</th></tr>
    <tr><td>2 (binary)</td><td><code id="nb-bin">…</code></td></tr>
    <tr><td>8 (octal)</td><td><code id="nb-oct">…</code></td></tr>
    <tr><td>10 (decimal)</td><td><code id="nb-dec">…</code></td></tr>
    <tr><td>16 (hex)</td><td><code id="nb-hex">…</code></td></tr>
    <tr><td>32</td><td><code id="nb-32">…</code></td></tr>
    <tr><td>36</td><td><code id="nb-36">…</code></td></tr>
  </table>
  <div class="meta" id="nb-meta"></div>
</div>
""",
    "script": """
<script>
function nbValidate(s, base){
  // Accept optional leading minus, but BigInt with arbitrary base needs custom parsing
  if (!s) return null;
  s = s.trim();
  let neg = false;
  if (s.startsWith('-')){ neg = true; s = s.slice(1); }
  if (!s.length) return null;
  // Strip leading 0x/0o/0b/# prefix lenience for base 10 input — only when base hints
  if (base === 16 && (s.startsWith('0x') || s.startsWith('0X') || s.startsWith('#'))) s = s.replace(/^0x|^0X|^#/,'');
  if (base === 2 && (s.startsWith('0b') || s.startsWith('0B'))) s = s.slice(2);
  if (base === 8 && (s.startsWith('0o') || s.startsWith('0O'))) s = s.slice(2);
  s = s.replace(/_/g, ''); // allow digit grouping with underscores
  // Validate against alphabet
  const alpha = '0123456789abcdefghijklmnopqrstuvwxyz'.slice(0, base);
  for (const ch of s.toLowerCase()){
    if (!alpha.includes(ch)) throw new Error('Invalid digit `' + ch + '` for base ' + base);
  }
  let val = 0n;
  for (const ch of s.toLowerCase()) val = val * BigInt(base) + BigInt(alpha.indexOf(ch));
  return neg ? -val : val;
}

function nbToBase(big, base){
  if (big === 0n) return '0';
  const neg = big < 0n;
  let n = neg ? -big : big;
  const alpha = '0123456789abcdefghijklmnopqrstuvwxyz';
  let out = '';
  while (n > 0n){
    out = alpha[Number(n % BigInt(base))] + out;
    n = n / BigInt(base);
  }
  return (neg ? '-' : '') + out;
}

function nbRun(){
  const sel = document.getElementById('nb-from');
  const otherInput = document.getElementById('nb-from-other');
  otherInput.style.display = sel.value === 'other' ? 'block' : 'none';
  let base = sel.value === 'other' ? parseInt(otherInput.value, 10) : parseInt(sel.value, 10);
  const inp = document.getElementById('nb-in').value;
  const meta = document.getElementById('nb-meta');
  const ids = ['nb-bin','nb-oct','nb-dec','nb-hex','nb-32','nb-36'];
  if (!base || base < 2 || base > 36){ meta.textContent = 'Pick a base between 2 and 36'; return; }
  try {
    const big = nbValidate(inp, base);
    if (big === null){ ids.forEach(id => document.getElementById(id).textContent = '—'); meta.textContent = ''; return; }
    document.getElementById('nb-bin').textContent = nbToBase(big, 2);
    document.getElementById('nb-oct').textContent = nbToBase(big, 8);
    document.getElementById('nb-dec').textContent = big.toString();
    document.getElementById('nb-hex').textContent = nbToBase(big, 16).toUpperCase();
    document.getElementById('nb-32').textContent = nbToBase(big, 32);
    document.getElementById('nb-36').textContent = nbToBase(big, 36);
    const bits = big < 0n ? (-big).toString(2).length + 1 : big.toString(2).length;
    meta.textContent = bits + ' bits';
  } catch(e){
    meta.textContent = '✗ ' + e.message;
    ids.forEach(id => document.getElementById(id).textContent = '—');
  }
}
document.addEventListener('DOMContentLoaded', nbRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Numbers are the same number regardless of base — <code>255</code>, <code>0xff</code>, <code>0b11111111</code>, and <code>0o377</code> are identical. But which base you read or write in matters when you're translating between memory layouts, parsing colour codes, decoding bit fields, or just reading hex from a debugger. This tool converts between binary, octal, decimal, hexadecimal, and any base from 2 to 36, using BigInt under the hood so you don't lose precision on large numbers.</p>

<h3>When to use it</h3>
<ul>
  <li>Reading a hex value from a stack trace and figuring out what it is in decimal.</li>
  <li>Converting CSS colour <code>0xff8800</code> into an RGB triple, or vice versa.</li>
  <li>Inspecting a bitmask or flags integer in binary to see which bits are set.</li>
  <li>Translating between base-36 short IDs and decimal counters.</li>
</ul>

<h3>Recognised prefixes</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binary: <code>0b</code>, <code>0B</code></li>
  <li>Octal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore digit grouping: <code>1_000_000</code></li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Negative numbers are sign-prefixed, not two's complement.</strong> <code>-128</code> is shown as <code>-10000000</code> in binary, not <code>10000000</code>. Most languages display the same way for arbitrary-precision integers.</li>
  <li><strong>Big numbers don't lose precision here.</strong> JavaScript <code>Number</code> caps at 2<sup>53</sup>; this tool uses <code>BigInt</code>, so 64-bit integers, large hashes, and crypto values all round-trip exactly.</li>
  <li><strong>Don't confuse base with case.</strong> Base-16 letters can be upper or lower; the tool accepts both and emits uppercase. Base-32 / base-36 outputs are lowercase by convention.</li>
  <li><strong>Leading zeros are dropped.</strong> <code>0x000F</code> becomes <code>F</code>. If you need a fixed-width hex (e.g. for byte representations), pad in your code afterward.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Números são o mesmo número independentemente da base — <code>255</code>, <code>0xff</code>, <code>0b11111111</code> e <code>0o377</code> são idênticos. Mas em qual base você lê ou escreve faz diferença quando está traduzindo entre layouts de memória, fazendo parsing de códigos de cor, decodificando bit fields ou só lendo hex no debugger. Esta ferramenta converte entre binary, octal, decimal, hexadecimal e qualquer base de 2 a 36, usando BigInt por baixo dos panos para você não perder precisão em números grandes.</p>

<h3>Quando usar</h3>
<ul>
  <li>Lendo um valor em hex de uma stack trace e querendo saber o que é em decimal.</li>
  <li>Convertendo cor CSS <code>0xff8800</code> em uma tripla RGB, ou o contrário.</li>
  <li>Inspecionando um bitmask ou inteiro de flags em binary para ver quais bits estão setados.</li>
  <li>Traduzindo entre IDs curtos em base 36 e contadores em decimal.</li>
</ul>

<h3>Prefixos reconhecidos</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binary: <code>0b</code>, <code>0B</code></li>
  <li>Octal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore para agrupar dígitos: <code>1_000_000</code></li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Números negativos vêm com prefixo de sinal, não em complemento de dois.</strong> <code>-128</code> aparece como <code>-10000000</code> em binary, não <code>10000000</code>. A maioria das linguagens mostra do mesmo jeito para inteiros de precisão arbitrária.</li>
  <li><strong>Números grandes não perdem precisão aqui.</strong> O <code>Number</code> do JavaScript trava em 2<sup>53</sup>; esta ferramenta usa <code>BigInt</code>, então inteiros de 64 bits, hashes grandes e valores de crypto fazem round-trip exato.</li>
  <li><strong>Não confunda base com case.</strong> Letras de base 16 podem ser maiúsculas ou minúsculas; a ferramenta aceita ambas e emite em maiúsculas. Saídas em base 32 / base 36 são minúsculas por convenção.</li>
  <li><strong>Zeros à esquerda são descartados.</strong> <code>0x000F</code> vira <code>F</code>. Se precisar de hex de largura fixa (por exemplo, para representação de bytes), faça o padding depois no seu código.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Liczby są tą samą liczbą niezależnie od bazy — <code>255</code>, <code>0xff</code>, <code>0b11111111</code> i <code>0o377</code> to to samo. Ale w której bazie czytasz albo piszesz, ma znaczenie, gdy tłumaczysz między layoutami pamięci, parsujesz kody kolorów, dekodujesz bit fieldy albo po prostu czytasz hex z debuggera. To narzędzie konwertuje między binary, octal, decimal, hex i dowolną bazą od 2 do 36, używając BigInt pod spodem, żebyś nie tracił precyzji na dużych liczbach.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Czytanie wartości hex ze stack trace i sprawdzanie, ile to dziesiętnie.</li>
  <li>Konwersja koloru CSS <code>0xff8800</code> na trójkę RGB albo na odwrót.</li>
  <li>Inspekcja bitmaski albo flagowego integera w binary, żeby zobaczyć, które bity są ustawione.</li>
  <li>Tłumaczenie między krótkimi ID-kami w bazie 36 a dziesiętnymi licznikami.</li>
</ul>

<h3>Rozpoznawane prefiksy</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binary: <code>0b</code>, <code>0B</code></li>
  <li>Octal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore do grupowania cyfr: <code>1_000_000</code></li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Liczby ujemne mają prefiks znaku, nie są w uzupełnieniu do dwóch.</strong> <code>-128</code> jest pokazane jako <code>-10000000</code> w binary, nie <code>10000000</code>. Większość języków pokazuje tak samo dla integerów dowolnej precyzji.</li>
  <li><strong>Duże liczby nie tracą tu precyzji.</strong> JS-owy <code>Number</code> ma kres w 2<sup>53</sup>; to narzędzie używa <code>BigInt</code>, więc 64-bitowe integery, duże hashe i wartości kryptograficzne robią dokładny round-trip.</li>
  <li><strong>Nie myl bazy z wielkością liter.</strong> Litery base-16 mogą być wielkie albo małe; narzędzie akceptuje obie i emituje wielkie. Wyjścia base-32 / base-36 są małe z konwencji.</li>
  <li><strong>Wiodące zera są usuwane.</strong> <code>0x000F</code> staje się <code>F</code>. Jeśli potrzebujesz hex stałej szerokości (np. do reprezentacji bajtów), dopadduj potem w swoim kodzie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>数は基数によらず同じ数です。<code>255</code>、<code>0xff</code>、<code>0b11111111</code>、<code>0o377</code> はすべて等価です。とはいえ、メモリレイアウト間の翻訳、カラーコードのパース、ビットフィールドのデコード、デバッガでの hex の読み取りなど、どの基数で読み書きするかは重要です。本ツールは 2 進・8 進・10 進・16 進、および 2〜36 の任意の基数を相互変換します。内部で BigInt を使うため、大きな数値でも精度は失われません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>スタックトレースに出てきた hex 値を 10 進で確認したいとき。</li>
  <li>CSS の色 <code>0xff8800</code> を RGB トリプルに、あるいはその逆に変換したいとき。</li>
  <li>ビットマスクやフラグ整数を 2 進で見て、どのビットが立っているかを確認したいとき。</li>
  <li>base-36 の短い ID と 10 進カウンタの間で変換したいとき。</li>
</ul>

<h3>認識される接頭辞</h3>
<ul>
  <li>Hex: <code>0x</code>、<code>0X</code>、<code>#</code></li>
  <li>2 進: <code>0b</code>、<code>0B</code></li>
  <li>8 進: <code>0o</code>、<code>0O</code></li>
  <li>桁区切りのアンダースコア：<code>1_000_000</code></li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>負数は符号付き表示で、2 の補数ではありません。</strong> <code>-128</code> は 2 進で <code>-10000000</code> と表示されます（<code>10000000</code> ではありません）。任意精度整数を扱う言語の多くも同様です。</li>
  <li><strong>大きな数で精度を失いません。</strong> JavaScript の <code>Number</code> は 2<sup>53</sup> で頭打ちになりますが、本ツールは <code>BigInt</code> を使うため、64 bit 整数や大きなハッシュ、暗号値も正確にラウンドトリップします。</li>
  <li><strong>基数と大文字小文字を混同しないでください。</strong> 16 進の文字は大文字でも小文字でも受け付け、出力は大文字。32 進・36 進は慣例で小文字です。</li>
  <li><strong>先頭のゼロは落ちます。</strong> <code>0x000F</code> は <code>F</code> になります。固定幅の hex（バイト表現など）が必要なら、後続のコードでパディングしてください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Getallen zijn hetzelfde getal ongeacht het grondtal — <code>255</code>, <code>0xff</code>, <code>0b11111111</code> en <code>0o377</code> zijn identiek. Maar in welk grondtal je leest of schrijft doet ertoe als je vertaalt tussen memory layouts, kleurcodes parset, bit fields decodeert of gewoon hex uit een debugger leest. Deze tool converteert tussen binair, octaal, decimaal, hexadecimaal en elk grondtal van 2 tot 36, met BigInt onder de motorkap zodat je geen precisie verliest op grote getallen.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een hex-waarde uit een stack trace lezen en uitvogelen wat hij is in decimaal.</li>
  <li>CSS-kleur <code>0xff8800</code> converteren naar een RGB-tripel, of andersom.</li>
  <li>Een bitmask of flags-integer in binair inspecteren om te zien welke bits gezet zijn.</li>
  <li>Vertalen tussen base-36 korte IDs en decimale tellers.</li>
</ul>

<h3>Herkende prefixen</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binair: <code>0b</code>, <code>0B</code></li>
  <li>Octaal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore-groepering: <code>1_000_000</code></li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Negatieve getallen zijn sign-prefixed, geen two's complement.</strong> <code>-128</code> wordt als <code>-10000000</code> in binair getoond, niet <code>10000000</code>. De meeste talen tonen het op dezelfde manier voor arbitrary-precision integers.</li>
  <li><strong>Grote getallen verliezen hier geen precisie.</strong> JavaScript <code>Number</code> kapt af bij 2<sup>53</sup>; deze tool gebruikt <code>BigInt</code>, dus 64-bit integers, grote hashes en crypto-waarden round-trip allemaal exact.</li>
  <li><strong>Verwar grondtal niet met case.</strong> Base-16 letters kunnen upper- of lowercase zijn; de tool accepteert beide en geeft uppercase. Base-32 / base-36 outputs zijn per conventie lowercase.</li>
  <li><strong>Leading zeros worden gedropt.</strong> <code>0x000F</code> wordt <code>F</code>. Als je een fixed-width hex nodig hebt (bijv. voor byte-representaties), pad daarna in je code.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Sayılar tabandan bağımsız aynı sayıdır — <code>255</code>, <code>0xff</code>, <code>0b11111111</code> ve <code>0o377</code> aynıdır. Ama okuduğun veya yazdığın taban, bellek düzenleri arasında çeviri yaparken, renk kodlarını parse ederken, bit alanlarını çözerken veya sadece bir debugger'dan hex okurken önemlidir. Bu araç ikilik, sekizlik, ondalık, onaltılık ve 2'den 36'ya kadar herhangi bir taban arasında dönüşür, büyük sayılarda hassasiyet kaybetmemen için altta BigInt kullanır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir stack trace'ten hex değeri okuyup ondalıkta ne olduğunu bulma.</li>
  <li>CSS rengi <code>0xff8800</code>'ı bir RGB üçlüsüne veya tersine dönüştürme.</li>
  <li>Hangi bit'lerin set edildiğini görmek için ikilikte bir bitmask veya flag tamsayısını inceleme.</li>
  <li>Base-36 kısa ID'ler ile ondalık sayaçlar arasında çeviri yapma.</li>
</ul>

<h3>Tanınan önekler</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>İkilik: <code>0b</code>, <code>0B</code></li>
  <li>Sekizlik: <code>0o</code>, <code>0O</code></li>
  <li>Alt çizgi rakam gruplaması: <code>1_000_000</code></li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Negatif sayılar işaret önekli, two's complement değil.</strong> <code>-128</code> ikilikte <code>-10000000</code> olarak gösterilir, <code>10000000</code> değil. Çoğu dil keyfi-hassasiyet tamsayıları için aynı şekilde gösterir.</li>
  <li><strong>Burada büyük sayılar hassasiyet kaybetmez.</strong> JavaScript <code>Number</code> 2<sup>53</sup>'te tepe yapar; bu araç <code>BigInt</code> kullanır, bu nedenle 64-bit tamsayılar, büyük hash'ler ve kripto değerleri hepsi tam round-trip yapar.</li>
  <li><strong>Tabanla büyük/küçük harfi karıştırma.</strong> Base-16 harfler büyük veya küçük olabilir; araç ikisini de kabul eder ve büyük harf yayınlar. Base-32 / base-36 çıktıları konvansiyon gereği küçüktür.</li>
  <li><strong>Baştaki sıfırlar düşürülür.</strong> <code>0x000F</code> <code>F</code> olur. Sabit genişlikli hex (örn. byte temsilleri için) gerekiyorsa, kodunda sonradan pad et.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Angka tetap angka yang sama tanpa peduli base-nya — <code>255</code>, <code>0xff</code>, <code>0b11111111</code>, dan <code>0o377</code> identik. Tapi base mana yang kamu baca atau tulis itu penting saat kamu menerjemahkan antar layout memory, parsing color code, decode bit field, atau sekadar membaca hex di debugger. Tool ini mengkonversi antara binary, octal, decimal, hexadecimal, dan base apa pun dari 2 sampai 36, memakai BigInt di bawah supaya kamu tidak kehilangan presisi pada angka besar.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Membaca nilai hex dari stack trace dan ingin tahu nilainya dalam desimal.</li>
  <li>Mengkonversi warna CSS <code>0xff8800</code> ke triple RGB, atau sebaliknya.</li>
  <li>Memeriksa bitmask atau flags integer dalam binary untuk melihat bit mana yang di-set.</li>
  <li>Menerjemahkan antara short ID base-36 dan counter desimal.</li>
</ul>

<h3>Prefix yang dikenali</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binary: <code>0b</code>, <code>0B</code></li>
  <li>Octal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore digit grouping: <code>1_000_000</code></li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Angka negatif memakai sign-prefix, bukan two's complement.</strong> <code>-128</code> ditampilkan sebagai <code>-10000000</code> dalam binary, bukan <code>10000000</code>. Kebanyakan bahasa menampilkan dengan cara yang sama untuk integer arbitrary-precision.</li>
  <li><strong>Angka besar tidak kehilangan presisi di sini.</strong> <code>Number</code> JavaScript dibatasi pada 2<sup>53</sup>; tool ini memakai <code>BigInt</code>, jadi integer 64-bit, hash besar, dan nilai crypto semua round-trip dengan akurat.</li>
  <li><strong>Jangan campur base dengan case.</strong> Huruf base-16 bisa upper- atau lowercase; tool ini menerima keduanya dan menghasilkan uppercase. Output base-32 / base-36 adalah lowercase secara konvensi.</li>
  <li><strong>Leading zero dibuang.</strong> <code>0x000F</code> jadi <code>F</code>. Kalau kamu butuh hex dengan fixed-width (misal untuk representasi byte), pad di kode kamu setelahnya.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Cùng một con số có thể được viết theo nhiều hệ — thập phân (62), nhị phân (111110), thập lục phân (3E), bát phân (76). Lập trình viên thường cần chuyển giữa chúng để debug, đọc dump bộ nhớ, hoặc thiết lập bitmask. Tool này chuyển bất kỳ số nào giữa hệ 2 và 36 (sau đó các chữ số bao gồm A–Z).</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Convert địa chỉ bộ nhớ hex sang decimal khi đọc log.</li>
  <li>Tính bitmask trong binary, nhập nó vào C dưới dạng hex.</li>
  <li>Debug protocol cấp thấp với binary và hex offset.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Số âm cần convention.</strong> Two's complement là tiêu chuẩn cho integer máy tính, nhưng tool có thể hiển thị dấu trừ literal cho input người đọc.</li>
  <li><strong>Floating point khác.</strong> Tool này xử lý integer; chuyển đổi float thập lục phân (như IEEE 754) cần một tool riêng.</li>
  <li><strong>Hệ trên 36 cần ký hiệu đặc biệt.</strong> Base64 dùng nguyên tắc khác (giá trị 0–63 với A–Z, a–z, 0–9, +, /). Tool này dừng ở 36 (chữ số 0–9 + chữ cái A–Z).</li>
</ul>
""",
    },
    "related": ["base64-encoder", "hash-generator", "uuid-generator"],
    "howto": {"flow": "transform", "action": "convert", "noun": "number"},
}
