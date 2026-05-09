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
    },
    "related": ["word-counter", "case-converter", "markdown-to-html"],
}
