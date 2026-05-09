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
    },
    "related": ["lorem-ipsum", "case-converter", "text-diff"],
}
