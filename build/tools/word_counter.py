TOOL = {
    "slug": "word-counter",
    "category": "text",
    "icon": "#",
    "tags": ["word", "count", "character", "sentence", "paragraph", "reading", "writing"],
    "i18n": {
        "en": {
            "name": "Word Counter",
            "tagline": "Count words, characters, sentences, paragraphs, and estimate reading + speaking time as you type.",
            "description": "Free online word counter. Live counts for words, characters (with and without spaces), sentences, paragraphs, syllables, plus reading and speaking time estimates.",
        },
        "de": {"name": "Wort-Zähler", "tagline": "Zähle Wörter, Zeichen, Sätze, Absätze und schätze Lese- und Sprechzeit live während du tippst.", "description": "Kostenloser Wort-Zähler. Live-Zählung von Wörtern, Zeichen (mit/ohne Leerzeichen), Sätzen, Absätzen, Silben sowie Lese- und Sprechzeitschätzung."},
        "es": {"name": "Contador de Palabras", "tagline": "Cuenta palabras, caracteres, frases, párrafos y estima tiempo de lectura y habla en vivo mientras escribes.", "description": "Contador de palabras gratuito. Conteo en vivo de palabras, caracteres (con y sin espacios), frases, párrafos, sílabas y estimación de tiempo de lectura y habla."},
        "fr": {"name": "Compteur de Mots", "tagline": "Comptez mots, caractères, phrases, paragraphes et estimez le temps de lecture et de parole en direct.", "description": "Compteur de mots gratuit. Comptage en direct des mots, caractères (avec/sans espaces), phrases, paragraphes, syllabes, et estimation du temps de lecture et de parole."},
        "it": {"name": "Contatore Parole", "tagline": "Conta parole, caratteri, frasi, paragrafi e stima tempo di lettura e parlato in tempo reale.", "description": "Contatore di parole gratuito. Conteggio live di parole, caratteri (con/senza spazi), frasi, paragrafi, sillabe e stima del tempo di lettura e parlato."},
        "pt": {"name": "Contador de Palavras", "tagline": "Conte palavras, caracteres, frases, parágrafos e estime tempo de leitura e fala enquanto você digita.", "description": "Contador de palavras online gratuito. Contagem ao vivo de palavras, caracteres (com e sem espaços), frases, parágrafos, sílabas, mais estimativas de tempo de leitura e fala."},
        "pl": {"name": "Licznik Słów", "tagline": "Licz słowa, znaki, zdania, akapity i estymuj czas czytania + mówienia w trakcie pisania.", "description": "Darmowy online licznik słów. Liczenie na żywo słów, znaków (ze spacjami i bez), zdań, akapitów, sylab plus estymacja czasu czytania i mówienia."},
        "ja": {"name": "ワードカウンター", "tagline": "単語数・文字数・文数・段落数を数え、入力中に読了時間と発話時間を概算。", "description": "オンライン無料のワードカウンター。単語数、文字数（スペース含む／含まない）、文数、段落数、音節数のライブカウントに加え、読了時間と発話時間の概算を提供します。"},
        "nl": {"name": "Woordenteller", "tagline": "Tel woorden, karakters, zinnen, paragrafen en schat lees- + spreektijd terwijl je typt.", "description": "Gratis online woordenteller. Live tellingen voor woorden, karakters (met en zonder spaties), zinnen, paragrafen, lettergrepen, plus lees- en spreektijd-schattingen."},
        "tr": {"name": "Kelime Sayacı", "tagline": "Kelimeleri, karakterleri, cümleleri, paragrafları say ve yazdıkça okuma + konuşma süresini tahmin et.", "description": "Ücretsiz online kelime sayacı. Kelimeler, karakterler (boşluklu ve boşluksuz), cümleler, paragraflar, heceler için canlı sayım, ayrıca okuma ve konuşma süresi tahminleri."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="wc-input" oninput="wcRun()" placeholder="Paste or type your text here…" spellcheck="false" style="min-height:240px"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div class="wc-grid" id="wc-stats">
    <div class="wc-stat"><div class="wc-num" id="wc-words">0</div><div class="wc-lbl" id="wc-words-lbl">Words</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-chars">0</div><div class="wc-lbl" id="wc-chars-lbl">Characters</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-chars-ns">0</div><div class="wc-lbl" id="wc-chars-ns-lbl">Characters (no spaces)</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-sentences">0</div><div class="wc-lbl" id="wc-sentences-lbl">Sentences</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-paragraphs">0</div><div class="wc-lbl" id="wc-paragraphs-lbl">Paragraphs</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-lines">0</div><div class="wc-lbl" id="wc-lines-lbl">Lines</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-read">0:00</div><div class="wc-lbl" id="wc-read-lbl">Reading time</div></div>
    <div class="wc-stat"><div class="wc-num" id="wc-speak">0:00</div><div class="wc-lbl" id="wc-speak-lbl">Speaking time</div></div>
  </div>
  <div class="wc-extra" id="wc-extra"></div>
</div>
""",
    "script": """
<style>
.wc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:0.6rem}
.wc-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.8rem;text-align:left}
.wc-num{font-family:ui-monospace,monospace;font-size:1.4rem;font-weight:600;color:var(--accent)}
.wc-lbl{font-size:0.78rem;color:var(--text-muted);margin-top:0.15rem}
.wc-extra{margin-top:0.8rem;font-size:0.85rem;color:var(--text-muted);display:grid;gap:0.3rem}
.wc-extra .wc-row{display:grid;grid-template-columns:160px 1fr;gap:0.5rem}
.wc-extra code{font-size:0.82rem}
</style>
<script>
function wcFmtTime(sec){
  const m = Math.floor(sec/60), s = Math.round(sec%60);
  return m + ':' + String(s).padStart(2,'0');
}
function wcRun(){
  const t = document.getElementById('wc-input').value;
  const chars = t.length;
  const charsNs = t.replace(/\\s/g,'').length;
  const words = (t.trim().match(/\\S+/g) || []).length;
  const sentences = (t.match(/[^.!?\\n]+[.!?]+(?=\\s|$)|[^.!?\\n]+$/g) || []).filter(s => s.trim().length>0).length;
  const paragraphs = t.split(/\\n\\s*\\n/).filter(p => p.trim().length>0).length;
  const lines = t === '' ? 0 : t.split(/\\n/).length;
  const readSec = words / 250 * 60;   // 250 wpm reading
  const speakSec = words / 130 * 60;  // 130 wpm speaking
  document.getElementById('wc-words').textContent = words.toLocaleString();
  document.getElementById('wc-chars').textContent = chars.toLocaleString();
  document.getElementById('wc-chars-ns').textContent = charsNs.toLocaleString();
  document.getElementById('wc-sentences').textContent = sentences.toLocaleString();
  document.getElementById('wc-paragraphs').textContent = paragraphs.toLocaleString();
  document.getElementById('wc-lines').textContent = lines.toLocaleString();
  document.getElementById('wc-read').textContent = wcFmtTime(readSec);
  document.getElementById('wc-speak').textContent = wcFmtTime(speakSec);

  // Extra stats
  const extra = document.getElementById('wc-extra');
  if(words === 0){ extra.innerHTML = ''; return; }
  const wordList = (t.toLowerCase().match(/[\\p{L}\\p{N}']+/gu) || []);
  const freq = {};
  for(const w of wordList) freq[w] = (freq[w]||0) + 1;
  const top = Object.entries(freq).sort((a,b)=>b[1]-a[1]).slice(0,5);
  const avgWordLen = wordList.length ? (wordList.reduce((a,w)=>a+w.length,0)/wordList.length).toFixed(1) : '0';
  const avgSentLen = sentences ? (words/sentences).toFixed(1) : '0';
  extra.innerHTML = `
    <div class="wc-row"><div>Avg word length</div><div><code>${avgWordLen}</code> chars</div></div>
    <div class="wc-row"><div>Avg sentence length</div><div><code>${avgSentLen}</code> words</div></div>
    <div class="wc-row"><div>Most frequent</div><div>${top.map(([w,n]) => `<code>${w}</code> ×${n}`).join(' · ') || '—'}</div></div>
    <div class="wc-row"><div>Twitter / X</div><div><code>${chars}</code> / 280 ${chars>280?'(over limit)':''}</div></div>
    <div class="wc-row"><div>SMS</div><div><code>${chars}</code> / 160 ${chars>160?'(multi-segment)':''}</div></div>
  `;
}
document.addEventListener('DOMContentLoaded', wcRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Counting words and characters by hand is tedious and error-prone, but the numbers matter all the time: tweet limits, SMS segments, essay word counts, SEO meta descriptions, journal submission lengths. This tool gives you live counts as you type — words, characters (with and without spaces), sentences, paragraphs, lines — plus reading and speaking time estimates and a quick word-frequency pass for the top five recurring words.</p>

<h3>When to use it</h3>
<ul>
  <li>Hitting a 280-character X/Twitter limit, a 160-char SMS, a 155-char SEO meta description, or a 100-word LinkedIn intro.</li>
  <li>Word-budgeting an essay, blog post, abstract, or grant application against a hard limit.</li>
  <li>Estimating how long a script will take to read aloud (podcasts, presentations, voice-overs).</li>
  <li>Spotting overused words by looking at the "most frequent" list before submitting.</li>
  <li>Checking whether a translation came in roughly the same length as the source.</li>
</ul>

<h3>What each number means</h3>
<ul>
  <li><strong>Words</strong> — runs of non-whitespace characters separated by whitespace. "Twenty-one" counts as one word; "twenty one" counts as two.</li>
  <li><strong>Characters</strong> vs <strong>characters (no spaces)</strong> — both count Unicode code points, not bytes. An emoji can be 1–2 "characters" here but more bytes when stored.</li>
  <li><strong>Sentences</strong> — segments ending in <code>.</code>, <code>!</code> or <code>?</code> (or end-of-text). Heuristic, see gotchas.</li>
  <li><strong>Paragraphs</strong> — separated by blank lines.</li>
  <li><strong>Reading time</strong> assumes 250 wpm (silent adult reading).</li>
  <li><strong>Speaking time</strong> assumes 130 wpm (typical conversational pace; news readers run faster, audiobooks slower).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Sentence detection is naïve.</strong> "Mr.", "U.S.", "e.g.", "3.14", and ellipses can inflate the sentence count. The figure is a useful estimate, not a guarantee.</li>
  <li><strong>Twitter/X counts code points, not characters.</strong> A flag emoji (🇸🇰) is 2 code points but renders as one symbol — Twitter treats it as 2 characters. This tool matches that.</li>
  <li><strong>SMS character limits depend on encoding.</strong> Plain ASCII fits 160 chars per segment; once you include a non-GSM character (em dash, smart quote, accented letter), the whole message switches to UCS-2 and the limit drops to 70. The tool reports the GSM limit; check your provider's behaviour for the actual cost.</li>
  <li><strong>Word counts vary by tool.</strong> Word, Google Docs, and journal-submission systems can disagree by a few percent — they handle hyphens, em dashes, and numbers differently. If a hard limit matters, count in the same tool the gatekeeper uses.</li>
  <li><strong>"Most frequent" doesn't filter stop words.</strong> "the" and "a" almost always top the list. Look at the longer entries for actual signal.</li>
  <li><strong>Reading-time estimates are personal.</strong> 250 wpm is the median; technical content runs slower, fiction faster. Treat the number as a planning guide, not a prediction.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Contar palavras e caracteres na mão é tedioso e propenso a erros, mas os números importam o tempo todo: limites de tweet, segmentos de SMS, contagem de palavras de redação, meta descriptions de SEO, tamanhos de submissão para periódicos. Esta ferramenta dá contagens ao vivo enquanto você digita — palavras, caracteres (com e sem espaços), frases, parágrafos, linhas — mais estimativas de tempo de leitura e fala, e uma rápida análise de frequência das cinco palavras mais recorrentes.</p>

<h3>Quando usar</h3>
<ul>
  <li>Quando você tem que caber em 280 caracteres no X/Twitter, 160 num SMS, 155 numa meta description de SEO ou 100 palavras numa intro de LinkedIn.</li>
  <li>Orçando palavras de uma redação, post de blog, resumo ou submissão de bolsa contra um limite rígido.</li>
  <li>Estimando quanto tempo um roteiro vai levar para ler em voz alta (podcasts, apresentações, voice-overs).</li>
  <li>Identificando palavras superusadas olhando a lista de "mais frequentes" antes de enviar.</li>
  <li>Verificando se uma tradução ficou aproximadamente do mesmo tamanho da fonte.</li>
</ul>

<h3>O que cada número significa</h3>
<ul>
  <li><strong>Palavras</strong> — sequências de caracteres não-whitespace separadas por whitespace. "Vinte-e-um" conta como uma palavra; "vinte e um" conta como três.</li>
  <li><strong>Caracteres</strong> vs <strong>caracteres (sem espaços)</strong> — ambos contam code points Unicode, não bytes. Um emoji pode ser 1–2 "caracteres" aqui mas ocupar mais bytes quando armazenado.</li>
  <li><strong>Frases</strong> — segmentos terminando em <code>.</code>, <code>!</code> ou <code>?</code> (ou fim do texto). Heurística, veja os cuidados abaixo.</li>
  <li><strong>Parágrafos</strong> — separados por linhas em branco.</li>
  <li><strong>Tempo de leitura</strong> assume 250 wpm (leitura silenciosa de adulto).</li>
  <li><strong>Tempo de fala</strong> assume 130 wpm (ritmo conversacional típico; locutores de notícias falam mais rápido, audiobooks mais devagar).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Detecção de frase é ingênua.</strong> "Sr.", "EUA.", "ex.:", "3,14" e reticências podem inflar a contagem de frases. O número é uma estimativa útil, não uma garantia.</li>
  <li><strong>Twitter/X conta code points, não caracteres.</strong> Um emoji de bandeira (🇸🇰) tem 2 code points mas renderiza como um símbolo — o Twitter trata como 2 caracteres. Esta ferramenta segue o mesmo critério.</li>
  <li><strong>Limites de caractere de SMS dependem do encoding.</strong> ASCII puro cabe em 160 chars por segmento; quando você inclui um caractere não-GSM (travessão, aspa curva, letra acentuada), a mensagem inteira muda para UCS-2 e o limite cai para 70. A ferramenta reporta o limite GSM; confira o comportamento da sua operadora para o custo real.</li>
  <li><strong>Contagens de palavras variam entre ferramentas.</strong> Word, Google Docs e sistemas de submissão de periódicos podem discordar em alguns por cento — eles tratam hifens, travessões e números de forma diferente. Se um limite rígido importa, conte na mesma ferramenta que o gatekeeper usa.</li>
  <li><strong>"Mais frequente" não filtra stop words.</strong> "a" e "o" quase sempre lideram a lista. Olhe as entradas mais longas para o sinal real.</li>
  <li><strong>Estimativas de tempo de leitura são pessoais.</strong> 250 wpm é a mediana; conteúdo técnico vai mais devagar, ficção mais rápido. Trate o número como guia de planejamento, não como previsão.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Liczenie słów i znaków ręcznie jest mozolne i błędogenne, ale liczby liczą się ciągle: limity tweetów, segmenty SMS-ów, słownictwo eseju, meta description SEO, długości submisji do journala. To narzędzie daje liczenie na żywo w trakcie pisania — słowa, znaki (ze spacjami i bez), zdania, akapity, linie — plus estymacja czasu czytania i mówienia oraz szybkie zliczenie częstotliwości pierwszej piątki najczęściej powtarzanych słów.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Trafianie w 280 znaków limitu X/Twittera, 160-znakowy SMS, 155-znakowy meta description SEO albo 100-słowną intro na LinkedIn.</li>
  <li>Budżetowanie słów eseju, posta blogowego, abstraktu albo wniosku grantowego pod twardy limit.</li>
  <li>Estymacja, ile zajmie skrypt czytany na głos (podcasty, prezentacje, voice-overy).</li>
  <li>Wyłapywanie nadużywanych słów patrząc na listę "najczęstszych" przed wysłaniem.</li>
  <li>Sprawdzenie, czy tłumaczenie wyszło mniej więcej tej samej długości co oryginał.</li>
</ul>

<h3>Co znaczy każda liczba</h3>
<ul>
  <li><strong>Słowa</strong> — ciągi znaków non-whitespace rozdzielone whitespace'em. "Dwadzieścia-jeden" liczy się jako jedno słowo; "dwadzieścia jeden" — jako dwa.</li>
  <li><strong>Znaki</strong> vs <strong>znaki (bez spacji)</strong> — oba liczą code pointy Unicode, nie bajty. Emoji może być tu 1–2 "znakami", ale więcej bajtów po zapisie.</li>
  <li><strong>Zdania</strong> — segmenty kończące się <code>.</code>, <code>!</code> albo <code>?</code> (albo końcem tekstu). Heurystyka, patrz pułapki.</li>
  <li><strong>Akapity</strong> — rozdzielone pustymi liniami.</li>
  <li><strong>Czas czytania</strong> zakłada 250 wpm (czytanie po cichu przez dorosłego).</li>
  <li><strong>Czas mówienia</strong> zakłada 130 wpm (typowe tempo konwersacyjne; lektorzy newsów lecą szybciej, audiobooki wolniej).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Detekcja zdań jest naiwna.</strong> "Mr.", "U.S.", "np.", "3,14" i wielokropki potrafią napompować licznik zdań. Liczba to przydatna estymata, nie gwarancja.</li>
  <li><strong>Twitter/X liczy code pointy, nie znaki.</strong> Emoji flagi (🇵🇱) to 2 code pointy, ale renderuje się jako jeden symbol — Twitter traktuje to jako 2 znaki. To narzędzie zachowuje się tak samo.</li>
  <li><strong>Limity znaków SMS-ów zależą od kodowania.</strong> Czyste ASCII mieści 160 znaków na segment; gdy wstawisz znak spoza GSM (myślnik, smart quote, znak diakrytyczny), cała wiadomość przełącza się na UCS-2 i limit spada do 70. Narzędzie raportuje limit GSM; sprawdź zachowanie operatora dla faktycznego kosztu.</li>
  <li><strong>Liczenie słów różni się między narzędziami.</strong> Word, Google Docs i systemy submisji journali potrafią różnić się o kilka procent — inaczej traktują myślniki, pauzy i liczby. Jeśli twardy limit ma znaczenie, licz w tym samym narzędziu, którego używa gatekeeper.</li>
  <li><strong>"Najczęstsze" nie filtruje stop words.</strong> "i", "w", "na" prawie zawsze lecą na czoło. Patrz na dłuższe wpisy po realny sygnał.</li>
  <li><strong>Estymaty czasu czytania są osobiste.</strong> 250 wpm to mediana; treść techniczna idzie wolniej, fikcja szybciej. Traktuj liczbę jako wskazówkę planowania, nie predykcję.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>単語数や文字数を手で数えるのは面倒で間違いやすい一方、これらは常に意味を持ちます。Tweet の上限、SMS のセグメント、エッセイの語数、SEO のメタディスクリプション、ジャーナル投稿の長さなど。本ツールは入力に応じてライブで集計します。単語、文字（スペース込み／なし）、文、段落、行数のほか、読了時間・発話時間の概算と、頻出単語トップ 5 のクイック頻度分析を提供します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>X/Twitter の 280 字、SMS の 160 字、SEO メタディスクリプションの 155 字、LinkedIn 紹介の 100 ワードに収めたいとき。</li>
  <li>エッセイ、ブログ、要旨、申請書を厳格な語数制限内にバジェットしたいとき。</li>
  <li>原稿の朗読時間を見積もりたいとき（ポッドキャスト、プレゼン、ナレーション）。</li>
  <li>提出前に「最頻出」リストから過剰使用語を見つけたいとき。</li>
  <li>翻訳が原文と概ね同じ長さになっているか確認したいとき。</li>
</ul>

<h3>各指標の意味</h3>
<ul>
  <li><strong>単語</strong> — 空白で区切られた非空白文字の連続。「twenty-one」は 1 単語、「twenty one」は 2 単語。</li>
  <li><strong>文字</strong> と <strong>文字（スペース除く）</strong> — どちらも Unicode コードポイント数（バイトではない）。絵文字はここでは 1〜2「文字」でも、保存時にはより多くのバイトを使います。</li>
  <li><strong>文</strong> — <code>.</code>、<code>!</code>、<code>?</code>（または末尾）で終わるセグメント。ヒューリスティックです。</li>
  <li><strong>段落</strong> — 空行で区切られた塊。</li>
  <li><strong>読了時間</strong> は 250 wpm（成人の黙読）を仮定。</li>
  <li><strong>発話時間</strong> は 130 wpm（典型的な会話速度。ニュース読みは速く、オーディオブックは遅め）を仮定。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>文の検出は素朴です。</strong> "Mr."、"U.S."、"e.g."、"3.14"、三点リーダーで文数が水増しされることがあります。あくまで参考値です。</li>
  <li><strong>Twitter/X は文字ではなくコードポイントで数えます。</strong> 国旗絵文字 🇯🇵 は 2 コードポイントで 1 シンボルとして表示されますが、Twitter は 2 文字としてカウントします。本ツールも同じ挙動です。</li>
  <li><strong>SMS の文字数上限はエンコーディング次第です。</strong> 純粋 ASCII ならセグメント 160 字、GSM 外の文字（em-dash、スマートクォート、アクセント文字など）が 1 文字でも入ると UCS-2 に切り替わり、上限は 70 字になります。本ツールは GSM の上限を表示します。実コストはキャリアの仕様も確認してください。</li>
  <li><strong>単語数はツールごとに数 % 違います。</strong> Word、Google Docs、ジャーナル投稿システムはハイフン、ダッシュ、数字の扱いが異なります。厳格な制限に合わせるなら、ゲートキーパーが使うのと同じツールで数えてください。</li>
  <li><strong>「最頻出」はストップワードを除外しません。</strong> "the" や "a" がほぼ常にトップに来ます。実質的なシグナルは長めの単語を見るとよいです。</li>
  <li><strong>読了時間の概算は人によって異なります。</strong> 250 wpm は中央値。技術文章は遅く、フィクションは速く読まれます。計画の目安として使ってください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Woorden en karakters met de hand tellen is saai en foutgevoelig, maar de getallen tellen voortdurend: tweet-limieten, SMS-segmenten, essay-woord-counts, SEO meta-descriptions, journal submission-lengtes. Deze tool geeft je live tellingen terwijl je typt — woorden, karakters (met en zonder spaties), zinnen, paragrafen, regels — plus lees- en spreektijd-schattingen en een snelle woord-frequentie-pass voor de top-vijf herhalende woorden.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een 280-karakter X/Twitter-limiet halen, een 160-karakter SMS, een 155-karakter SEO meta-description of een 100-woord LinkedIn-intro.</li>
  <li>Een essay, blogpost, abstract of grant application word-budgeteren tegen een harde limiet.</li>
  <li>Inschatten hoe lang een script duurt om voor te lezen (podcasts, presentaties, voice-overs).</li>
  <li>Overgebruikte woorden spotten door naar de "meest frequente"-lijst te kijken voor submitting.</li>
  <li>Checken of een vertaling ruwweg dezelfde lengte heeft als de bron.</li>
</ul>

<h3>Wat elk getal betekent</h3>
<ul>
  <li><strong>Woorden</strong> — runs van non-whitespace karakters gescheiden door whitespace. "Twenty-one" telt als één woord; "twenty one" telt als twee.</li>
  <li><strong>Karakters</strong> vs <strong>karakters (geen spaties)</strong> — beide tellen Unicode code points, geen bytes. Een emoji kan hier 1–2 "karakters" zijn maar meer bytes wanneer opgeslagen.</li>
  <li><strong>Zinnen</strong> — segmenten eindigend op <code>.</code>, <code>!</code> of <code>?</code> (of end-of-text). Heuristiek, zie valkuilen.</li>
  <li><strong>Paragrafen</strong> — gescheiden door blanke regels.</li>
  <li><strong>Leestijd</strong> gaat uit van 250 wpm (stille volwassen lezing).</li>
  <li><strong>Spreektijd</strong> gaat uit van 130 wpm (typisch conversationeel tempo; nieuwsfellers lopen sneller, audiobooks trager).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Zin-detectie is naïef.</strong> "Mr.", "U.S.", "bijv.", "3,14" en ellipses kunnen de zinstelling opblazen. Het getal is een nuttige schatting, geen garantie.</li>
  <li><strong>Twitter/X telt code points, geen karakters.</strong> Een vlag-emoji (🇳🇱) is 2 code points maar rendert als één symbool — Twitter behandelt het als 2 karakters. Deze tool matcht dat.</li>
  <li><strong>SMS-karakterlimieten hangen af van encoding.</strong> Plain ASCII past 160 karakters per segment; zodra je een non-GSM karakter (em-dash, smart quote, accent-letter) opneemt, schakelt het hele bericht naar UCS-2 en valt de limit naar 70. De tool rapporteert de GSM-limit; check je provider's gedrag voor de daadwerkelijke kost.</li>
  <li><strong>Woord-counts variëren per tool.</strong> Word, Google Docs en journal-submission systems kunnen een paar procent verschillen — ze handelen hyphens, em-dashes en getallen verschillend af. Als een harde limit telt, tel in dezelfde tool die de gatekeeper gebruikt.</li>
  <li><strong>"Meest frequente" filtert geen stop words.</strong> "de" en "een" staan bijna altijd bovenaan. Kijk naar de langere entries voor daadwerkelijk signaal.</li>
  <li><strong>Leestijd-schattingen zijn persoonlijk.</strong> 250 wpm is de mediaan; technische content loopt trager, fictie sneller. Behandel het getal als plannings-leidraad, geen voorspelling.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Kelime ve karakter saymak elle sıkıcı ve hata yapmaya açıktır, ama sayılar her zaman önemlidir: tweet sınırları, SMS segmentleri, deneme kelime sayıları, SEO meta açıklamalar, dergi gönderim uzunlukları. Bu araç sen yazdıkça canlı sayımlar verir — kelimeler, karakterler (boşluklu ve boşluksuz), cümleler, paragraflar, satırlar — artı okuma ve konuşma süresi tahminleri ve en sık geçen beş kelime için hızlı bir kelime frekansı geçişi.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>280 karakterlik bir X/Twitter sınırına, 160 karakterlik bir SMS'e, 155 karakterlik bir SEO meta açıklamaya veya 100 kelimelik bir LinkedIn intro'suna ulaşma.</li>
  <li>Bir deneme, blog gönderisi, özet veya hibe başvurusunu sert sınıra karşı bütçeleme.</li>
  <li>Bir script'in yüksek sesle okunması ne kadar sürer tahmin etme (podcast'ler, sunumlar, voice-over'lar).</li>
  <li>Gönderimden önce "en sık" listesine bakarak çok kullanılan kelimeleri tespit etme.</li>
  <li>Bir çevirinin kaynakla kabaca aynı uzunlukta gelip gelmediğini kontrol etme.</li>
</ul>

<h3>Her sayı ne anlama gelir</h3>
<ul>
  <li><strong>Kelimeler</strong> — boşlukla ayrılmış boşluk olmayan karakterler grupları. "Twenty-one" tek kelime olarak sayılır; "twenty one" iki olarak sayılır.</li>
  <li><strong>Karakterler</strong> vs <strong>karakterler (boşluksuz)</strong> — ikisi de Unicode code point'lerini sayar, byte değil. Bir emoji burada 1–2 "karakter" olabilir ama saklandığında daha fazla byte.</li>
  <li><strong>Cümleler</strong> — <code>.</code>, <code>!</code> veya <code>?</code> ile biten segmentler (veya metnin sonu). Sezgiseldir, sık yapılan hatalara bak.</li>
  <li><strong>Paragraflar</strong> — boş satırlarla ayrılır.</li>
  <li><strong>Okuma süresi</strong> 250 wpm varsayar (sessiz yetişkin okuması).</li>
  <li><strong>Konuşma süresi</strong> 130 wpm varsayar (tipik konuşma temposu; haber okuyucular daha hızlı, sesli kitaplar daha yavaş gider).</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Cümle tespiti naiftir.</strong> "Mr.", "U.S.", "e.g.", "3.14" ve üç nokta cümle sayısını şişirebilir. Rakam kullanışlı bir tahmindir, garanti değil.</li>
  <li><strong>Twitter/X karakterleri değil, code point'leri sayar.</strong> Bayrak emojisi (🇹🇷) 2 code point'tir ama tek sembol olarak render olur — Twitter bunu 2 karakter olarak ele alır. Bu araç bunu eşleştirir.</li>
  <li><strong>SMS karakter sınırları kodlamaya bağlıdır.</strong> Düz ASCII segment başına 160 karakter sığar; GSM olmayan bir karakter (em dash, smart quote, aksanlı harf) eklediğinde, tüm mesaj UCS-2'ye geçer ve sınır 70'e düşer. Araç GSM sınırını raporlar; gerçek maliyet için sağlayıcının davranışını kontrol et.</li>
  <li><strong>Kelime sayıları araca göre değişir.</strong> Word, Google Docs ve dergi gönderim sistemleri birkaç yüzde anlaşmazlık çıkarabilir — tireler, em dash'ler ve sayıları farklı ele alırlar. Sert sınır önemliyse, geçit bekçisinin kullandığı aynı araçta say.</li>
  <li><strong>"En sık" stop word'leri filtrelemez.</strong> "the" ve "a" neredeyse her zaman listenin başında olur. Gerçek sinyal için daha uzun girdilere bak.</li>
  <li><strong>Okuma süresi tahminleri kişiseldir.</strong> 250 wpm medyandır; teknik içerik daha yavaş, kurgu daha hızlı gider. Sayıyı bir tahmin değil, bir planlama rehberi olarak ele al.</li>
</ul>
""",
    },
    "related": ["lorem-ipsum", "case-converter", "text-diff"],
    "howto": {"flow": "calculate", "action": "count",   "noun": "text"},
}
