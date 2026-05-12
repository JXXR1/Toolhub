TOOL = {
    "slug": "lorem-ipsum",
    "category": "text",
    "icon": "¶",
    "tags": ["lorem", "ipsum", "placeholder", "filler", "dummy", "text"],
    "i18n": {
        "en": {
            "name": "Lorem Ipsum Generator",
            "tagline": "Generate paragraphs, sentences, words, or list items of placeholder Latin text. Configurable length and starting phrase.",
            "description": "Free Lorem Ipsum generator. Build paragraphs, sentences, words, or HTML lists for mockups and design comps. Optional classic 'Lorem ipsum dolor sit amet…' opener.",
        },
        "de": {"name": "Lorem-Ipsum-Generator", "tagline": "Erzeuge Absätze, Sätze, Wörter oder Listenpunkte mit Lorem-Ipsum-Platzhaltertext. Länge und Eröffnungsphrase wählbar.", "description": "Kostenloser Lorem-Ipsum-Generator. Absätze, Sätze, Wörter oder HTML-Listen für Mockups und Layouts."},
        "es": {"name": "Generador Lorem Ipsum", "tagline": "Genera párrafos, frases, palabras o elementos de lista en latín de relleno. Longitud y frase inicial configurables.", "description": "Generador de Lorem Ipsum gratuito. Párrafos, frases, palabras o listas HTML para maquetas y diseños."},
        "fr": {"name": "Générateur de Lorem Ipsum", "tagline": "Générez des paragraphes, phrases, mots ou éléments de liste en latin de remplissage. Longueur et phrase d'ouverture configurables.", "description": "Générateur de Lorem Ipsum gratuit. Paragraphes, phrases, mots ou listes HTML pour maquettes et designs."},
        "it": {"name": "Generatore di Lorem Ipsum", "tagline": "Genera paragrafi, frasi, parole o voci di elenco di testo segnaposto in latino. Lunghezza e frase iniziale configurabili.", "description": "Generatore di Lorem Ipsum gratuito. Paragrafi, frasi, parole o liste HTML per mockup e progetti grafici."},
        "pt": {"name": "Gerador de Lorem Ipsum", "tagline": "Gere parágrafos, frases, palavras ou itens de lista de texto placeholder em latim. Tamanho e frase inicial configuráveis.", "description": "Gerador de Lorem Ipsum gratuito. Crie parágrafos, frases, palavras ou listas HTML para mockups e composições de design. Abertura clássica 'Lorem ipsum dolor sit amet…' opcional."},
        "pl": {"name": "Generator Lorem Ipsum", "tagline": "Generuj akapity, zdania, słowa albo elementy listy tekstu placeholder po łacinie. Konfigurowalny rozmiar i fraza otwierająca.", "description": "Darmowy generator Lorem Ipsum. Buduj akapity, zdania, słowa albo listy HTML do mockupów i komp designerskich. Opcjonalna klasyczna otwarka 'Lorem ipsum dolor sit amet…'."},
        "ja": {"name": "Lorem Ipsum ジェネレーター", "tagline": "段落・文・単語・リスト項目の単位でラテン語のプレースホルダーテキストを生成。長さと冒頭フレーズを設定可能。", "description": "無料の Lorem Ipsum ジェネレーター。モックアップやデザインカンプ用に、段落・文・単語・HTML リストを生成できます。古典的な「Lorem ipsum dolor sit amet…」で始める設定もオプションで利用可能です。"},
        "nl": {"name": "Lorem Ipsum Generator", "tagline": "Genereer paragrafen, zinnen, woorden of list items van placeholder Latijnse tekst. Configureerbare lengte en startfrase.", "description": "Gratis Lorem Ipsum-generator. Bouw paragrafen, zinnen, woorden of HTML-lijsten voor mockups en design comps. Optionele klassieke 'Lorem ipsum dolor sit amet…'-opener."},
        "tr": {"name": "Lorem Ipsum Üretici", "tagline": "Placeholder Latince metnin paragraflarını, cümlelerini, kelimelerini veya liste öğelerini üret. Ayarlanabilir uzunluk ve başlangıç ibaresi.", "description": "Ücretsiz Lorem Ipsum üretici. Mockup ve tasarım kompozisyonları için paragraflar, cümleler, kelimeler veya HTML listeleri kur. Opsiyonel klasik 'Lorem ipsum dolor sit amet…' başlangıcı."},
        "id": {"name": "Lorem Ipsum Generator", "tagline": "Hasilkan paragraf, kalimat, kata, atau item list dengan teks placeholder Latin. Panjang dan frasa awal dapat dikustomisasi.", "description": "Generator Lorem Ipsum gratis. Hasilkan placeholder Latin klasik dengan panjang yang dapat dikonfigurasi — paragraf, kalimat, kata, atau item list. Mulai dengan frasa klasik 'Lorem ipsum dolor sit amet' atau acak."},
        "vi": {"name": "Lorem Ipsum Generator", "tagline": "Tạo đoạn văn, câu, từ hoặc mục danh sách của văn bản placeholder Latin. Tùy chỉnh độ dài và cụm từ mở đầu.", "description": "Trình tạo Lorem Ipsum miễn phí trực tuyến. Tạo đoạn, câu, từ hoặc mục danh sách của văn bản placeholder Latin cổ điển cho mockup, design và bản demo."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_TYPE}</label>
      <select id="li-type" onchange="liRun()">
        <option value="paragraphs">Paragraphs</option>
        <option value="sentences">Sentences</option>
        <option value="words">Words</option>
        <option value="list">List items (HTML)</option>
      </select>
    </div>
    <div>
      <label>{LBL_COUNT}</label>
      <input type="number" id="li-count" value="3" min="1" max="100" oninput="liRun()">
    </div>
  </div>
  <div style="margin-top:1rem;display:flex;gap:1rem;flex-wrap:wrap">
    <label><input type="checkbox" id="li-classic" checked onchange="liRun()"> Start with classic "Lorem ipsum…"</label>
    <label><input type="checkbox" id="li-html" onchange="liRun()"> Wrap output in HTML tags</label>
  </div>
  <div class="button-row" style="margin-top:1rem">
    <button onclick="liRun()">{LBL_GENERATE}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="li-out" style="white-space:pre-wrap">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('li-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
const LI_WORDS = ("lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum at vero eos accusamus iusto odio dignissimos ducimus blanditiis praesentium voluptatum deleniti atque corrupti quos quas molestias excepturi occaecati cupiditate similique placeat facere possimus assumenda repellendus temporibus autem quibusdam saepe eveniet voluptates repudiandae recusandae itaque earum rerum hic tenetur sapiente delectus reiciendis maiores doloribus asperiores").split(' ');
const LI_CLASSIC = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
function liRand(min, max){ return Math.floor(Math.random() * (max - min + 1)) + min; }
function liWord(){ return LI_WORDS[Math.floor(Math.random()*LI_WORDS.length)]; }
function liSentence(){
  const len = liRand(8, 16);
  const w = [];
  for(let i = 0; i < len; i++) w.push(liWord());
  // Sprinkle a comma
  if(len > 8) w[Math.floor(len/2)] += ',';
  w[0] = w[0][0].toUpperCase() + w[0].slice(1);
  return w.join(' ') + '.';
}
function liParagraph(){
  const n = liRand(3, 6);
  const s = [];
  for(let i = 0; i < n; i++) s.push(liSentence());
  return s.join(' ');
}
function liRun(){
  const type = document.getElementById('li-type').value;
  const count = parseInt(document.getElementById('li-count').value, 10) || 1;
  const classic = document.getElementById('li-classic').checked;
  const html = document.getElementById('li-html').checked;
  const out = document.getElementById('li-out');
  let result = '';
  if(type === 'paragraphs'){
    const paras = [];
    for(let i = 0; i < count; i++){
      let p = liParagraph();
      if(i === 0 && classic) p = LI_CLASSIC + ' ' + p.split('. ').slice(1).join('. ');
      paras.push(p);
    }
    result = html ? paras.map(p => '<p>' + p + '</p>').join('\\n') : paras.join('\\n\\n');
  } else if(type === 'sentences'){
    const s = [];
    for(let i = 0; i < count; i++){
      let sent = liSentence();
      if(i === 0 && classic) sent = LI_CLASSIC;
      s.push(sent);
    }
    result = s.join(' ');
  } else if(type === 'words'){
    const w = [];
    if(classic) w.push(...['Lorem','ipsum','dolor','sit','amet']);
    while(w.length < count) w.push(liWord());
    result = w.slice(0, count).join(' ');
  } else if(type === 'list'){
    const items = [];
    for(let i = 0; i < count; i++){
      const len = liRand(3, 8);
      const w = [];
      for(let j = 0; j < len; j++) w.push(liWord());
      w[0] = w[0][0].toUpperCase() + w[0].slice(1);
      items.push('  <li>' + w.join(' ') + '</li>');
    }
    result = '<ul>\\n' + items.join('\\n') + '\\n</ul>';
  }
  out.textContent = result;
}
document.addEventListener('DOMContentLoaded', liRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Lorem ipsum is scrambled Latin derived from Cicero's <em>De Finibus Bonorum et Malorum</em> (45 BC), in use as filler since the 1500s because its character frequencies and word lengths roughly match real prose without being readable enough to distract. Designers use it so the brain processes blocks of text as <em>shape</em> rather than <em>meaning</em> — exactly what you want when judging typography, layout, or page rhythm.</p>

<h3>When to use it</h3>
<ul>
  <li><strong>Mockups</strong> — placeholder for "the words don't matter, the layout does".</li>
  <li><strong>Design comps</strong> — testing wrapping, line lengths, font fallbacks at multiple sizes.</li>
  <li><strong>CMS / template testing</strong> — populating fields before real copy lands.</li>
  <li><strong>Capacity planning</strong> — sanity-checking how a card / preview / search result handles long bodies.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't ship it to production.</strong> Lorem ipsum has been published live more than once because nobody swapped it for the real copy.</li>
  <li><strong>Real copy is shorter or longer than placeholder.</strong> Real headlines are punchier. Real body copy varies wildly. A layout that looks balanced with lorem ipsum can fall apart with the actual content; verify with real text before sign-off.</li>
  <li><strong>Internationalisation reveals what lorem hides.</strong> Designs tested only with Latin filler often break with German compounds or Arabic right-to-left layouts. Test with multilingual placeholders for i18n-aware designs.</li>
  <li><strong>Convention matters.</strong> The first paragraph traditionally starts "Lorem ipsum dolor sit amet…" — designers recognise that as placeholder. Turning it off can mean someone misses the swap.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Lorem ipsum é latim embaralhado derivado de <em>De Finibus Bonorum et Malorum</em> de Cícero (45 a.C.), usado como texto de preenchimento desde os anos 1500 porque a frequência de caracteres e o tamanho das palavras lembram prosa real sem ser legível o bastante para distrair. Designers usam para que o cérebro processe blocos de texto como <em>forma</em> em vez de <em>significado</em> — exatamente o que você quer ao avaliar tipografia, layout ou ritmo de página.</p>

<h3>Quando usar</h3>
<ul>
  <li><strong>Mockups</strong> — placeholder para "as palavras não importam, o layout sim".</li>
  <li><strong>Design comps</strong> — testar quebra de linha, comprimento de linha e font fallbacks em vários tamanhos.</li>
  <li><strong>Teste de CMS / template</strong> — preencher campos antes do texto real chegar.</li>
  <li><strong>Planejamento de capacidade</strong> — validar como um card / preview / resultado de busca lida com conteúdos longos.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não publique em produção.</strong> Lorem ipsum já foi publicado ao vivo mais de uma vez porque ninguém trocou pelo texto real.</li>
  <li><strong>Texto real é mais curto ou mais longo que o placeholder.</strong> Títulos reais são mais diretos. Corpo de texto real varia muito. Um layout que parece equilibrado com lorem ipsum pode desmoronar com o conteúdo de verdade; valide com texto real antes da aprovação.</li>
  <li><strong>Internacionalização revela o que o lorem esconde.</strong> Designs testados apenas com preenchimento latino quebram com palavras compostas em alemão ou layouts da direita para a esquerda em árabe. Teste com placeholders multilíngues em designs com i18n.</li>
  <li><strong>Convenção importa.</strong> O primeiro parágrafo tradicionalmente começa com "Lorem ipsum dolor sit amet…" — designers reconhecem isso como placeholder. Desativar pode fazer alguém esquecer de fazer a troca.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Lorem ipsum to zniekształcona łacina wywodząca się z <em>De Finibus Bonorum et Malorum</em> Cycerona (45 p.n.e.), używana jako wypełniacz od XVI wieku, bo częstotliwości znaków i długości słów z grubsza odpowiadają realnej prozie, ale tekst nie jest na tyle czytelny, żeby rozpraszać. Designerzy używają go po to, by mózg przetwarzał bloki tekstu jako <em>kształt</em>, a nie <em>treść</em> — dokładnie tego chcesz, oceniając typografię, układ albo rytm strony.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li><strong>Mockupy</strong> — placeholder do "słowa nie mają znaczenia, ważny jest layout".</li>
  <li><strong>Kompozycje designerskie</strong> — testowanie zawijania, długości linii, font fallbacków przy różnych rozmiarach.</li>
  <li><strong>Test CMS / szablonów</strong> — wypełnianie pól zanim wpadnie prawdziwa treść.</li>
  <li><strong>Planowanie pojemności</strong> — sanity check, jak karta / preview / wynik wyszukiwania radzi sobie z długimi treściami.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie wysyłaj go na produkcję.</strong> Lorem ipsum był publikowany live więcej niż raz, bo nikt nie zamienił go na prawdziwą treść.</li>
  <li><strong>Prawdziwa treść jest krótsza albo dłuższa od placeholdera.</strong> Prawdziwe nagłówki są bardziej dosadne. Prawdziwy korpus tekstu szaleje. Layout, który wygląda zrównoważenie z lorem ipsum, może się rozsypać przy faktycznej treści; weryfikuj na prawdziwym tekście przed sign-offem.</li>
  <li><strong>Internacjonalizacja ujawnia to, co lorem ukrywa.</strong> Designy testowane tylko z łacińskim wypełniaczem często padają przy niemieckich złożeniach albo arabskich layoutach right-to-left. Testuj wielojęzycznymi placeholderami w designach świadomych i18n.</li>
  <li><strong>Konwencja ma znaczenie.</strong> Pierwszy akapit tradycyjnie zaczyna się "Lorem ipsum dolor sit amet…" — designerzy rozpoznają to jako placeholder. Wyłączenie tego może oznaczać, że ktoś przeoczy podmianę.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>Lorem ipsum はキケロの『善と悪の究極について』（紀元前 45 年）に由来する崩したラテン語で、1500 年代から穴埋め用テキストとして使われてきました。文字の出現頻度や単語長が実文に近い一方、読めるほどではないため意識を散らしません。デザイナーは脳がテキスト塊を<em>意味</em>ではなく<em>かたち</em>として処理できるように、これを使います。タイポグラフィやレイアウト、ページのリズムを評価するのにちょうどよい性質です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li><strong>モックアップ</strong> — 「言葉は重要ではなく、レイアウトが重要」の場面に。</li>
  <li><strong>デザインカンプ</strong> — 折り返し、行長、フォントフォールバックを各サイズで検証。</li>
  <li><strong>CMS / テンプレートのテスト</strong> — 実コピーが届くまでフィールドを埋めるため。</li>
  <li><strong>キャパシティの検証</strong> — カード／プレビュー／検索結果が長文で破綻しないかの確認。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>本番に出さないこと。</strong> 「実コピーに差し替える」のを忘れて Lorem ipsum がそのまま公開された事例は何度も起きています。</li>
  <li><strong>実コピーはプレースホルダーより短かったり長かったりします。</strong> 実際の見出しはもっと簡潔、本文は大きくばらつきます。lorem ipsum で整って見えるレイアウトは、実コンテンツで崩れることがあります。サインオフ前に実テキストで検証してください。</li>
  <li><strong>国際化は lorem が隠していたものを露わにします。</strong> ラテン語の穴埋めだけでテストしたデザインは、ドイツ語の複合語やアラビア語の右から左のレイアウトで破綻しがちです。i18n を意識する場合は多言語のプレースホルダーで検証してください。</li>
  <li><strong>慣習も大事です。</strong> 最初の段落は伝統的に「Lorem ipsum dolor sit amet…」で始まり、デザイナーはこれをプレースホルダーと認識します。これを外すと差し替え漏れに気づきにくくなります。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Lorem ipsum is gescrambled Latijn afgeleid van Cicero's <em>De Finibus Bonorum et Malorum</em> (45 v.C.), in gebruik als filler sinds de jaren 1500 omdat de karakterfrequenties en woordlengtes ruwweg matchen met echte tekst zonder leesbaar genoeg te zijn om af te leiden. Designers gebruiken het zodat het brein blokken tekst als <em>vorm</em> verwerkt in plaats van <em>betekenis</em> — precies wat je wil bij het beoordelen van typografie, layout of paginaritme.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li><strong>Mockups</strong> — placeholder voor "de woorden doen er niet toe, de layout wel".</li>
  <li><strong>Design comps</strong> — testen van wrapping, regellengtes, font-fallbacks op meerdere groottes.</li>
  <li><strong>CMS / template testing</strong> — velden vullen voor de echte copy aankomt.</li>
  <li><strong>Capacity planning</strong> — sanity check op hoe een card / preview / search-result lange bodies afhandelt.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Niet naar productie shippen.</strong> Lorem ipsum is meer dan eens live gegaan omdat niemand het voor de echte copy heeft omgewisseld.</li>
  <li><strong>Echte copy is korter of langer dan placeholder.</strong> Echte headlines zijn punchier. Echte body-copy varieert wild. Een layout die met lorem ipsum gebalanceerd lijkt, kan met de daadwerkelijke content uit elkaar vallen; verifieer met echte tekst voor sign-off.</li>
  <li><strong>Internationalisatie onthult wat lorem verbergt.</strong> Designs die alleen met Latijnse filler getest zijn, breken vaak met Duitse samenstellingen of Arabische right-to-left layouts. Test met multilingual placeholders voor i18n-aware designs.</li>
  <li><strong>Conventie doet ertoe.</strong> De eerste paragraaf begint traditioneel met "Lorem ipsum dolor sit amet…" — designers herkennen dat als placeholder. Het uitschakelen kan betekenen dat iemand de swap mist.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Lorem ipsum, Cicero'nun <em>De Finibus Bonorum et Malorum</em>'undan (MÖ 45) türetilen karıştırılmış Latince'dir, karakter frekansları ve kelime uzunlukları gerçek nesirle kabaca eşleştiği ama dikkat dağıtacak kadar okunabilir olmadığı için 1500'lerden beri filler olarak kullanılır. Tasarımcılar beynin metin bloklarını <em>anlam</em> yerine <em>şekil</em> olarak işlemesi için kullanır — tipografiyi, layout'u veya sayfa ritmini değerlendirirken tam olarak istediğin şey.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li><strong>Mockup'lar</strong> — "kelimeler önemli değil, layout önemli" için placeholder.</li>
  <li><strong>Tasarım comp'ları</strong> — birden fazla boyutta wrapping, satır uzunlukları, font fallback'lerini test etme.</li>
  <li><strong>CMS / template testi</strong> — gerçek kopya gelmeden önce alanları doldurma.</li>
  <li><strong>Kapasite planlaması</strong> — bir kartın / önizlemenin / arama sonucunun uzun gövdeleri nasıl ele aldığının sanity check'i.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Production'a gönderme.</strong> Lorem ipsum birden fazla kez canlı yayınlandı çünkü kimse gerçek kopya ile değiştirmedi.</li>
  <li><strong>Gerçek kopya placeholder'dan daha kısa veya uzundur.</strong> Gerçek başlıklar daha sıkıdır. Gerçek gövde kopyası vahşice değişir. Lorem ipsum ile dengeli görünen bir layout gerçek içerikle dağılabilir; sign-off'tan önce gerçek metinle doğrula.</li>
  <li><strong>Internationalisation lorem'in gizlediğini ortaya çıkarır.</strong> Sadece Latince filler ile test edilen tasarımlar sıklıkla Almanca bileşik kelimeler veya Arapça sağdan sola düzenlerle bozulur.</li>
  <li><strong>Gelenek önemlidir.</strong> İlk paragraf geleneksel olarak "Lorem ipsum dolor sit amet…" ile başlar — tasarımcılar bunu placeholder olarak tanır. Kapatmak değişimi birinin kaçırması anlamına gelebilir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Lorem ipsum adalah bahasa Latin yang diacak, berasal dari <em>De Finibus Bonorum et Malorum</em> Cicero (45 SM), digunakan sebagai filler sejak tahun 1500-an karena frekuensi karakter dan panjang katanya kurang lebih mirip prosa asli tanpa cukup mudah dibaca untuk mengalihkan perhatian. Designer memakainya supaya otak memproses blok teks sebagai <em>bentuk</em> alih-alih <em>arti</em> — persis yang kamu inginkan saat menilai tipografi, layout, atau ritme halaman.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li><strong>Mockup</strong> — placeholder untuk "kata-katanya tidak penting, layout-nya yang penting".</li>
  <li><strong>Design comp</strong> — menguji wrapping, panjang baris, font fallback di berbagai ukuran.</li>
  <li><strong>Testing CMS / template</strong> — mengisi field sebelum copy asli datang.</li>
  <li><strong>Capacity planning</strong> — sanity check bagaimana sebuah card / preview / search result menangani body yang panjang.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Jangan dirilis ke production.</strong> Lorem ipsum sudah pernah dipublikasikan live lebih dari sekali karena tidak ada yang menggantinya dengan copy asli.</li>
  <li><strong>Copy asli lebih pendek atau lebih panjang dari placeholder.</strong> Headline asli lebih punchy. Body copy asli sangat bervariasi. Layout yang terlihat seimbang dengan lorem ipsum bisa berantakan dengan konten sebenarnya; verifikasi dengan teks asli sebelum sign-off.</li>
  <li><strong>Internasionalisasi mengungkap apa yang disembunyikan lorem.</strong> Design yang hanya diuji dengan filler Latin sering rusak dengan kata majemuk Jerman atau layout right-to-left Arab. Uji dengan placeholder multibahasa untuk design yang sadar i18n.</li>
  <li><strong>Konvensi itu penting.</strong> Paragraf pertama secara tradisional dimulai dengan "Lorem ipsum dolor sit amet…" — designer mengenalinya sebagai placeholder. Mematikannya bisa berarti seseorang melewatkan pertukarannya.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Lorem ipsum là văn bản placeholder kinh điển — pseudo-Latin được dùng để fill mockup mà không phân tâm. Tool này tạo bất kỳ số đoạn văn, câu, từ hoặc mục list nào với phong cách Lorem ipsum cổ điển — sẵn sàng để paste vào design hoặc layout test.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Fill mockup hoặc wireframe với văn bản trông tự nhiên.</li>
  <li>Test layout với độ dài văn bản khác nhau (1 từ vs 1 đoạn dài).</li>
  <li>Tạo dữ liệu trông realistic cho seed database.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Lorem không có nghĩa.</strong> Đó là tính năng — designer và client nhìn vào layout, không phải content. Đừng dịch nó hoặc cố gắng hiểu nó.</li>
  <li><strong>Đừng ship Lorem ipsum.</strong> Đã có nhiều site sản xuất nổi tiếng release với placeholder content. Có lint rule cho điều đó nếu bạn lo lắng.</li>
  <li><strong>Lorem rất "đặc". </strong> Văn bản thực sự thường có khoảng trắng và hệ thống dấu câu khác — Lorem có thể che giấu vấn đề về typography.</li>
</ul>
""",
    },
    "related": ["word-counter", "case-converter", "markdown-to-html"],
    "howto": {"flow": "generate",  "action": "generate","noun": "text"},
}
