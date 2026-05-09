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
    },
    "related": ["lorem-ipsum", "case-converter", "text-diff"],
}
