# Static content pages — about, contact, for-schools, privacy,
# how-we-handle-your-data, affiliate-disclosure.
# Each page has:
#   slug    — URL segment (e.g. "about" => /about/ for EN, /<lang>/about/ for others)
#   schema  — schema.org @type for the JSON-LD WebPage variant (AboutPage, ContactPage, WebPage)
#   i18n[lang] = { title, h1, description, body (HTML) }
#
# Pages are pure static content. No body/script/help like tools — rendered via
# build/page_template.html, NOT build/template.html.

REPO_URL = "https://github.com/JXXR1/Toolhub"
REPO_ISSUES = "https://github.com/JXXR1/Toolhub/issues"
CONTACT_EMAIL = "JXXR1@users.noreply.github.com"
PDF_URL = "/how-we-handle-your-data.pdf"
LAST_UPDATED = "11 May 2026"


def _about_body(intro_what, intro_why, intro_who, intro_how, intro_oss, intro_no_ai,
                h_what, h_why, h_who, h_how, h_oss, h_no_ai):
    return f"""
<h2>{h_what}</h2>
<p>{intro_what}</p>

<h2>{h_why}</h2>
<p>{intro_why}</p>

<h2>{h_who}</h2>
<p>{intro_who}</p>

<h2>{h_how}</h2>
<p>{intro_how}</p>

<h2>{h_oss}</h2>
<p>{intro_oss}</p>

<h2>{h_no_ai}</h2>
<p>{intro_no_ai}</p>
""".strip()


PAGES = {
    "about": {
        "slug": "about",
        "schema": "AboutPage",
        "i18n": {
            "en": {
                "title": "About Toolhub",
                "h1": "About Toolhub",
                "description": "Toolhub is a small no-tracking utility site built by one person. Free developer tools that run entirely in your browser, no signup, no data collection.",
                "body": _about_body(
                    intro_what="Toolhub is a collection of free developer and everyday utility tools that run entirely in your browser. No signup, no account, no tracking, no server-side processing. Paste your data in, get the result, close the tab — nothing is stored or transmitted.",
                    intro_why="Most online utility sites are ad-laden parking pages or shovel your data through fourteen third-party trackers before you even click anything. Toolhub is the alternative: one page, one tool, runs locally, leaves you alone.",
                    intro_who=f'JXXR1, indie maintainer. No company, no funding round, no investors. Toolhub started as a side project to scratch a personal itch — a single page that did one tool well — and grew from there. Reachable via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="The site is static HTML hosted on GitHub Pages. Every tool runs as JavaScript in your browser — no API calls, no server-side compute, no data leaves your device unless explicitly noted (for example the YouTube Thumbnail tool fetches an image from YouTube's CDN; everything else is purely local).",
                    intro_oss=f'The full source is at <a href="{REPO_URL}">{REPO_URL}</a>. Contributions, bug reports, and tool ideas are welcome via GitHub Issues.',
                    intro_no_ai="Tool help blocks and translations are human-reviewed within reason, not pasted from an LLM. If you spot a translation that sounds robotic or wrong, open an issue — it's an easy fix and the kind of contribution that makes the site better for everyone.",
                    h_what="What Toolhub is",
                    h_why="Why",
                    h_who="Who",
                    h_how="How it works",
                    h_oss="Open source",
                    h_no_ai="No AI slop",
                ),
            },
            "de": {
                "title": "Über Toolhub",
                "h1": "Über Toolhub",
                "description": "Toolhub ist eine kleine, tracking-freie Utility-Seite, gebaut von einer Person. Kostenlose Entwickler-Tools, die komplett im Browser laufen — ohne Anmeldung, ohne Datensammlung.",
                "body": _about_body(
                    intro_what="Toolhub ist eine Sammlung kostenloser Entwickler- und Alltags-Tools, die komplett in deinem Browser laufen. Keine Anmeldung, kein Konto, kein Tracking, keine serverseitige Verarbeitung. Daten einfügen, Ergebnis bekommen, Tab schließen — nichts wird gespeichert oder übertragen.",
                    intro_why="Die meisten Utility-Seiten im Netz sind entweder mit Werbung vollgepflasterte Parking-Pages oder schicken deine Daten durch vierzehn Drittanbieter-Tracker, bevor du überhaupt klickst. Toolhub ist die Alternative: eine Seite, ein Tool, läuft lokal, lässt dich in Ruhe.",
                    intro_who=f'JXXR1, unabhängiger Maintainer. Keine Firma, keine Finanzierungsrunde, keine Investoren. Toolhub fing als Nebenprojekt an — eine einzige Seite, die ein Tool gut macht — und ist von dort gewachsen. Erreichbar über <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Die Seite ist statisches HTML, gehostet auf GitHub Pages. Jedes Tool läuft als JavaScript in deinem Browser — keine API-Aufrufe, keine serverseitige Berechnung, keine Daten verlassen dein Gerät, außer es ist explizit angemerkt (zum Beispiel lädt das YouTube-Thumbnail-Tool ein Bild von YouTubes CDN; alles andere ist rein lokal).",
                    intro_oss=f'Der komplette Quellcode liegt auf <a href="{REPO_URL}">{REPO_URL}</a>. Beiträge, Bug-Reports und Tool-Ideen sind über GitHub Issues willkommen.',
                    intro_no_ai="Hilfetexte und Übersetzungen sind nach Möglichkeit von Menschen geprüft, nicht aus einem LLM kopiert. Wenn dir eine Übersetzung robotisch oder falsch vorkommt, öffne ein Issue — das ist eine schnelle Korrektur und macht die Seite für alle besser.",
                    h_what="Was Toolhub ist",
                    h_why="Warum",
                    h_who="Wer",
                    h_how="Wie es funktioniert",
                    h_oss="Open Source",
                    h_no_ai="Kein KI-Schrott",
                ),
            },
            "es": {
                "title": "Acerca de Toolhub",
                "h1": "Acerca de Toolhub",
                "description": "Toolhub es un pequeño sitio de utilidades sin tracking, hecho por una sola persona. Herramientas gratis para desarrolladores que se ejecutan enteramente en tu navegador, sin registro y sin recolectar datos.",
                "body": _about_body(
                    intro_what="Toolhub es una colección de herramientas gratis para desarrolladores y uso diario que se ejecutan enteramente en tu navegador. Sin registro, sin cuenta, sin tracking, sin procesamiento en servidor. Pegas los datos, obtienes el resultado, cierras la pestaña — nada se almacena ni se transmite.",
                    intro_why="La mayoría de sitios de utilidades online son páginas llenas de anuncios o pasan tus datos por catorce trackers de terceros antes de que hagas un solo clic. Toolhub es la alternativa: una página, una herramienta, funciona en local, te deja en paz.",
                    intro_who=f'JXXR1, mantenedor independiente. Sin empresa, sin ronda de financiación, sin inversores. Toolhub empezó como un proyecto paralelo para resolver una necesidad personal — una sola página que hiciera bien una herramienta — y creció desde ahí. Contactable vía <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="El sitio es HTML estático alojado en GitHub Pages. Cada herramienta funciona como JavaScript en tu navegador — sin llamadas a APIs, sin cómputo en servidor, ningún dato sale de tu dispositivo a menos que se indique explícitamente (por ejemplo, la herramienta de YouTube Thumbnail descarga una imagen desde la CDN de YouTube; todo lo demás es puramente local).",
                    intro_oss=f'El código fuente completo está en <a href="{REPO_URL}">{REPO_URL}</a>. Contribuciones, reportes de bugs e ideas de herramientas son bienvenidas vía GitHub Issues.',
                    intro_no_ai="Los textos de ayuda y traducciones están revisados por personas dentro de lo razonable, no pegados de un LLM. Si ves una traducción que suena robótica o incorrecta, abre un issue — es un cambio fácil y de los que hacen mejor el sitio para todos.",
                    h_what="Qué es Toolhub",
                    h_why="Por qué",
                    h_who="Quién",
                    h_how="Cómo funciona",
                    h_oss="Open source",
                    h_no_ai="Nada de basura generada por IA",
                ),
            },
            "fr": {
                "title": "À propos de Toolhub",
                "h1": "À propos de Toolhub",
                "description": "Toolhub est un petit site d'utilitaires sans tracking, fait par une seule personne. Des outils dev gratuits qui tournent entièrement dans ton navigateur, sans inscription ni collecte de données.",
                "body": _about_body(
                    intro_what="Toolhub est une collection d'outils gratuits pour développeurs et usage quotidien qui tournent entièrement dans ton navigateur. Pas d'inscription, pas de compte, pas de tracking, pas de traitement côté serveur. Tu colles tes données, tu obtiens le résultat, tu fermes l'onglet — rien n'est stocké ni transmis.",
                    intro_why="La plupart des sites d'utilitaires en ligne sont des pages couvertes de pubs ou refilent tes données à quatorze trackers tiers avant même que tu cliques. Toolhub est l'alternative : une page, un outil, tourne en local, te laisse tranquille.",
                    intro_who=f'JXXR1, mainteneur indépendant. Pas de société, pas de levée de fonds, pas d\'investisseurs. Toolhub a commencé comme un side project pour résoudre un besoin perso — une seule page qui fait bien un outil — et a grandi à partir de là. Joignable via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Le site est du HTML statique hébergé sur GitHub Pages. Chaque outil tourne en JavaScript dans ton navigateur — pas d'appels API, pas de calcul serveur, aucune donnée ne quitte ton appareil sauf mention explicite (par exemple l'outil YouTube Thumbnail récupère une image depuis le CDN de YouTube ; tout le reste est purement local).",
                    intro_oss=f'Le code source complet est sur <a href="{REPO_URL}">{REPO_URL}</a>. Les contributions, rapports de bugs et idées d\'outils sont les bienvenus via GitHub Issues.',
                    intro_no_ai="Les textes d'aide et les traductions sont relus par des humains dans la mesure du raisonnable, pas collés depuis un LLM. Si tu vois une traduction qui sonne robotique ou fausse, ouvre une issue — c'est une correction facile et le genre de contribution qui rend le site meilleur pour tout le monde.",
                    h_what="Ce qu'est Toolhub",
                    h_why="Pourquoi",
                    h_who="Qui",
                    h_how="Comment ça marche",
                    h_oss="Open source",
                    h_no_ai="Pas de contenu IA bâclé",
                ),
            },
            "it": {
                "title": "Chi siamo — Toolhub",
                "h1": "Chi siamo",
                "description": "Toolhub è un piccolo sito di utility senza tracking, costruito da una sola persona. Strumenti per sviluppatori gratuiti che girano interamente nel tuo browser, senza registrazione e senza raccolta dati.",
                "body": _about_body(
                    intro_what="Toolhub è una raccolta di strumenti gratuiti per sviluppatori e uso quotidiano che girano interamente nel tuo browser. Niente registrazione, niente account, niente tracking, niente elaborazione server-side. Incolli i dati, ottieni il risultato, chiudi la tab — nulla viene salvato o trasmesso.",
                    intro_why="La maggior parte dei siti di utility online sono parking page piene di pubblicità o passano i tuoi dati attraverso quattordici tracker di terze parti prima ancora che tu clicchi qualcosa. Toolhub è l'alternativa: una pagina, uno strumento, gira in locale, ti lascia in pace.",
                    intro_who=f'JXXR1, maintainer indipendente. Niente azienda, niente round di finanziamento, niente investitori. Toolhub è nato come progetto secondario per risolvere una necessità personale — una singola pagina che facesse bene uno strumento — ed è cresciuto da lì. Contattabile via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Il sito è HTML statico ospitato su GitHub Pages. Ogni strumento gira come JavaScript nel tuo browser — niente chiamate API, niente calcoli server-side, nessun dato lascia il tuo dispositivo salvo dove esplicitamente indicato (per esempio lo strumento YouTube Thumbnail scarica un'immagine dalla CDN di YouTube; tutto il resto è puramente locale).",
                    intro_oss=f'Il codice sorgente completo è su <a href="{REPO_URL}">{REPO_URL}</a>. Contributi, segnalazioni di bug e idee per strumenti sono i benvenuti via GitHub Issues.',
                    intro_no_ai="I testi di aiuto e le traduzioni sono rivisti da persone per quanto possibile, non incollati da un LLM. Se vedi una traduzione che suona robotica o sbagliata, apri una issue — è una correzione facile e il tipo di contributo che rende il sito migliore per tutti.",
                    h_what="Cos'è Toolhub",
                    h_why="Perché",
                    h_who="Chi",
                    h_how="Come funziona",
                    h_oss="Open source",
                    h_no_ai="Niente robaccia da IA",
                ),
            },
            "pt": {
                "title": "Sobre o Toolhub",
                "h1": "Sobre o Toolhub",
                "description": "Toolhub é um site pequeno de utilitários sem tracking, feito por uma pessoa só. Ferramentas grátis para devs que rodam inteiramente no seu navegador, sem cadastro e sem coletar dados.",
                "body": _about_body(
                    intro_what="Toolhub é uma coleção de ferramentas grátis para devs e uso cotidiano que rodam inteiramente no seu navegador. Sem cadastro, sem conta, sem tracking, sem processamento no servidor. Você cola os dados, pega o resultado, fecha a aba — nada é guardado nem transmitido.",
                    intro_why="A maioria dos sites de utilitários online são páginas lotadas de anúncios ou passam seus dados por quatorze trackers de terceiros antes de você clicar em qualquer coisa. O Toolhub é a alternativa: uma página, uma ferramenta, roda local, deixa você em paz.",
                    intro_who=f'JXXR1, mantenedor independente. Sem empresa, sem rodada de investimento, sem investidores. O Toolhub começou como um side project para resolver uma necessidade pessoal — uma página só que fizesse bem uma ferramenta — e cresceu a partir daí. Pode falar comigo pelo <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="O site é HTML estático hospedado no GitHub Pages. Cada ferramenta roda como JavaScript no seu navegador — sem chamadas a API, sem cálculo no servidor, nenhum dado sai do seu dispositivo a não ser quando explicitamente indicado (por exemplo, a ferramenta YouTube Thumbnail baixa uma imagem da CDN do YouTube; o resto é puramente local).",
                    intro_oss=f'O código-fonte completo está em <a href="{REPO_URL}">{REPO_URL}</a>. Contribuições, relatos de bug e ideias de ferramentas são bem-vindos via GitHub Issues.',
                    intro_no_ai="Os textos de ajuda e as traduções são revisados por pessoas dentro do razoável, não colados de um LLM. Se você ver uma tradução que soa robótica ou errada, abra uma issue — é uma correção fácil e do tipo que melhora o site pra todo mundo.",
                    h_what="O que é o Toolhub",
                    h_why="Por quê",
                    h_who="Quem",
                    h_how="Como funciona",
                    h_oss="Open source",
                    h_no_ai="Nada de lixo gerado por IA",
                ),
            },
            "pl": {
                "title": "O Toolhub",
                "h1": "O Toolhub",
                "description": "Toolhub to mała strona z narzędziami bez trackingu, zbudowana przez jedną osobę. Darmowe narzędzia dla devów, które działają w całości w przeglądarce — bez rejestracji, bez zbierania danych.",
                "body": _about_body(
                    intro_what="Toolhub to zbiór darmowych narzędzi dla devów i codziennego użytku, które działają w całości w twojej przeglądarce. Bez rejestracji, bez konta, bez trackingu, bez przetwarzania po stronie serwera. Wklejasz dane, dostajesz wynik, zamykasz kartę — nic się nie zapisuje ani nie wysyła.",
                    intro_why="Większość stron z narzędziami online to albo parking pages oblepione reklamami, albo przepuszczają twoje dane przez czternaście trackerów stron trzecich, zanim w ogóle coś klikniesz. Toolhub to alternatywa: jedna strona, jedno narzędzie, działa lokalnie, zostawia cię w spokoju.",
                    intro_who=f'JXXR1, niezależny maintainer. Bez firmy, bez rundy finansowania, bez inwestorów. Toolhub zaczął się jako side project, żeby zaspokoić własną potrzebę — jedna strona, która porządnie robi jedno narzędzie — i rozrósł się od tego. Można się dobić przez <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Strona to statyczny HTML hostowany na GitHub Pages. Każde narzędzie działa jako JavaScript w twojej przeglądarce — bez wywołań API, bez obliczeń po stronie serwera, żadne dane nie opuszczają twojego urządzenia, chyba że jest to wyraźnie zaznaczone (na przykład narzędzie YouTube Thumbnail pobiera obraz z CDN YouTube'a; cała reszta jest czysto lokalna).",
                    intro_oss=f'Cały kod źródłowy jest na <a href="{REPO_URL}">{REPO_URL}</a>. Wkład, zgłoszenia bugów i pomysły na narzędzia są mile widziane przez GitHub Issues.',
                    intro_no_ai="Teksty pomocy i tłumaczenia są w miarę możliwości weryfikowane przez ludzi, nie wklejone z LLM-a. Jeśli widzisz tłumaczenie, które brzmi robotycznie albo źle — otwórz issue. To prosta poprawka i taki wkład, który robi stronę lepszą dla wszystkich.",
                    h_what="Czym jest Toolhub",
                    h_why="Dlaczego",
                    h_who="Kto",
                    h_how="Jak to działa",
                    h_oss="Open source",
                    h_no_ai="Bez AI-owej sieczki",
                ),
            },
            "ja": {
                "title": "Toolhub について",
                "h1": "Toolhub について",
                "description": "Toolhub は一人の開発者が作っている、トラッキングなしの小さなユーティリティサイトです。すべてブラウザ内で動く無料の開発者向けツール — 登録不要、データ収集なし。",
                "body": _about_body(
                    intro_what="Toolhub は、すべてブラウザ内で動作する無料の開発者向け・日常用ユーティリティツール集です。登録不要、アカウント不要、トラッキングなし、サーバー側処理もありません。データを貼り付けて、結果を取得して、タブを閉じる — 何も保存されず、送信もされません。",
                    intro_why="オンラインのユーティリティサイトの多くは広告だらけのパーキングページか、クリックする前にあなたのデータを十数個のサードパーティトラッカーに流しています。Toolhub はその代わりになるものです — 1ページ、1ツール、ローカルで動き、あなたをそっとしておきます。",
                    intro_who=f'JXXR1、独立した個人メンテナーです。会社も、資金調達ラウンドも、投資家もいません。Toolhub は個人的な必要を満たすためのサイドプロジェクトとして始まり — 1つのツールをきちんとこなす1ページのサイトとして — そこから育ってきました。連絡は <a href="{REPO_URL}">GitHub</a> からどうぞ。',
                    intro_how="サイトは GitHub Pages にホストされた静的 HTML です。各ツールはブラウザ内の JavaScript として動作します — API 呼び出しもサーバー側の計算もありません。明示的に注記されている場合を除き、データがあなたの端末を離れることはありません（例えば YouTube Thumbnail ツールは YouTube の CDN から画像を取得しますが、それ以外はすべて純粋にローカルで動作します）。",
                    intro_oss=f'ソースコード全体は <a href="{REPO_URL}">{REPO_URL}</a> にあります。コントリビューション、バグ報告、ツールのアイデアは GitHub Issues からどうぞ。',
                    intro_no_ai="ヘルプ文章や翻訳は、できる範囲で人の手でレビューしています。LLM から貼り付けただけのものではありません。ロボットっぽい、あるいは間違っている翻訳を見つけたら、Issue を開いてください — 簡単に直せますし、こうした貢献がサイトを皆にとって良いものにします。",
                    h_what="Toolhub とは",
                    h_why="なぜ作っているのか",
                    h_who="誰が作っているのか",
                    h_how="仕組み",
                    h_oss="オープンソース",
                    h_no_ai="AI のいい加減な出力は使いません",
                ),
            },
            "nl": {
                "title": "Over Toolhub",
                "h1": "Over Toolhub",
                "description": "Toolhub is een kleine tracking-vrije utility-site, gebouwd door één persoon. Gratis developer tools die volledig in je browser draaien, zonder account en zonder data-verzameling.",
                "body": _about_body(
                    intro_what="Toolhub is een verzameling gratis developer- en alledaagse tools die volledig in je browser draaien. Geen account, geen registratie, geen tracking, geen verwerking op de server. Je plakt je data, krijgt het resultaat, sluit het tabblad — niets wordt opgeslagen of verstuurd.",
                    intro_why="De meeste utility-sites online zijn parking pages volgeplakt met reclame, of duwen je data door veertien third-party trackers nog voor je iets aanklikt. Toolhub is het alternatief: één pagina, één tool, draait lokaal, laat je met rust.",
                    intro_who=f'JXXR1, onafhankelijke maintainer. Geen bedrijf, geen funding round, geen investeerders. Toolhub begon als een side project om een eigen behoefte op te lossen — één pagina die één tool goed deed — en is van daaruit gegroeid. Te bereiken via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="De site is statische HTML gehost op GitHub Pages. Elke tool draait als JavaScript in je browser — geen API calls, geen server-side compute, geen data verlaat je apparaat tenzij expliciet aangegeven (bijvoorbeeld de YouTube Thumbnail tool haalt een afbeelding op van YouTube's CDN; al het andere is puur lokaal).",
                    intro_oss=f'De volledige source staat op <a href="{REPO_URL}">{REPO_URL}</a>. Bijdragen, bug reports en tool-ideeën zijn welkom via GitHub Issues.',
                    intro_no_ai="Hulpteksten en vertalingen zijn binnen redelijke grenzen door mensen nagekeken, niet uit een LLM geplakt. Zie je een vertaling die robotachtig of fout klinkt, open een issue — het is een snelle fix en het soort bijdrage dat de site voor iedereen beter maakt.",
                    h_what="Wat Toolhub is",
                    h_why="Waarom",
                    h_who="Wie",
                    h_how="Hoe het werkt",
                    h_oss="Open source",
                    h_no_ai="Geen AI-rommel",
                ),
            },
        },
    },

    "contact": {
        "slug": "contact",
        "schema": "ContactPage",
        "i18n": {
            "en": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Reach the Toolhub maintainer via GitHub Issues for bug reports, feature requests and tool ideas, or by email for everything else.",
                "body": f"""
<p>Toolhub is a one-person side project. Best-effort response times, not commercial. There is no contact form — this site has no backend, by design.</p>

<h2>GitHub Issues</h2>
<p>For bug reports, feature requests, translation fixes, and new tool ideas, please open an issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues is preferred because it gives the discussion a permanent URL other people with the same question can find later.</p>

<h2>Email</h2>
<p>For things that don't fit GitHub Issues — press, partnership, security disclosure, takedown requests — email <code>{CONTACT_EMAIL}</code>.</p>

<h2>Response times</h2>
<p>I aim to read everything within a week, but Toolhub is built and maintained in spare time alongside a day job. If something is urgent (e.g. security), say so in the subject line.</p>
""".strip(),
            },
            "de": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Den Toolhub-Maintainer erreichst du über GitHub Issues für Bug-Reports, Feature-Wünsche und Tool-Ideen, oder per E-Mail für alles andere.",
                "body": f"""
<p>Toolhub ist ein Ein-Personen-Nebenprojekt. Best-Effort-Antwortzeiten, nichts Kommerzielles. Es gibt kein Kontaktformular — die Seite hat bewusst kein Backend.</p>

<h2>GitHub Issues</h2>
<p>Für Bug-Reports, Feature-Wünsche, Übersetzungs-Korrekturen und Ideen für neue Tools öffne bitte ein Issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues sind bevorzugt, weil sie der Diskussion eine permanente URL geben, die andere Leute mit derselben Frage später finden können.</p>

<h2>E-Mail</h2>
<p>Für Themen, die nicht in GitHub Issues passen — Presse, Kooperationen, Security-Disclosure, Takedown-Anfragen — schreibe an <code>{CONTACT_EMAIL}</code>.</p>

<h2>Antwortzeiten</h2>
<p>Ich versuche, alles innerhalb einer Woche zu lesen, aber Toolhub wird in der Freizeit neben einem Brotjob gebaut und gewartet. Wenn etwas dringend ist (z. B. Security), schreibe das in den Betreff.</p>
""".strip(),
            },
            "es": {
                "title": "Contacto",
                "h1": "Contacto",
                "description": "Contacta con el mantenedor de Toolhub vía GitHub Issues para reportes de bugs, peticiones de funcionalidades e ideas de herramientas, o por email para todo lo demás.",
                "body": f"""
<p>Toolhub es un proyecto paralelo de una sola persona. Tiempos de respuesta best-effort, no comerciales. No hay formulario de contacto — este sitio no tiene backend, por diseño.</p>

<h2>GitHub Issues</h2>
<p>Para reportes de bugs, peticiones de funcionalidades, correcciones de traducción e ideas de nuevas herramientas, por favor abre una issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues es la vía preferida porque le da a la discusión una URL permanente que otras personas con la misma pregunta pueden encontrar después.</p>

<h2>Email</h2>
<p>Para cosas que no encajan en GitHub Issues — prensa, partnerships, divulgación de seguridad, peticiones de retirada — escribe a <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tiempos de respuesta</h2>
<p>Intento leer todo en una semana, pero Toolhub se construye y mantiene en tiempo libre, además de un trabajo principal. Si algo es urgente (por ejemplo, seguridad), indícalo en el asunto.</p>
""".strip(),
            },
            "fr": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Contacte le mainteneur de Toolhub via GitHub Issues pour les bugs, demandes de fonctionnalités et idées d'outils, ou par email pour le reste.",
                "body": f"""
<p>Toolhub est un side project d'une seule personne. Délais de réponse en best-effort, rien de commercial. Il n'y a pas de formulaire de contact — ce site n'a pas de backend, c'est voulu.</p>

<h2>GitHub Issues</h2>
<p>Pour les rapports de bugs, demandes de fonctionnalités, corrections de traduction et idées de nouveaux outils, ouvre une issue :</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues est préféré parce que ça donne à la discussion une URL permanente que d'autres personnes avec la même question pourront retrouver plus tard.</p>

<h2>Email</h2>
<p>Pour les choses qui ne rentrent pas dans GitHub Issues — presse, partenariats, divulgation de sécurité, demandes de retrait — écris à <code>{CONTACT_EMAIL}</code>.</p>

<h2>Délais de réponse</h2>
<p>J'essaie de tout lire dans la semaine, mais Toolhub est construit et maintenu sur du temps libre, à côté d'un boulot principal. Si quelque chose est urgent (par exemple sécurité), mentionne-le dans le sujet.</p>
""".strip(),
            },
            "it": {
                "title": "Contatti",
                "h1": "Contatti",
                "description": "Contatta il maintainer di Toolhub via GitHub Issues per segnalazioni di bug, richieste di funzionalità e idee per strumenti, o via email per tutto il resto.",
                "body": f"""
<p>Toolhub è un side project di una sola persona. Tempi di risposta best-effort, non commerciali. Non c'è un form di contatto — il sito non ha backend, di proposito.</p>

<h2>GitHub Issues</h2>
<p>Per segnalazioni di bug, richieste di funzionalità, correzioni di traduzione e idee per nuovi strumenti, apri una issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues è preferito perché dà alla discussione un URL permanente che altre persone con la stessa domanda potranno trovare in futuro.</p>

<h2>Email</h2>
<p>Per cose che non rientrano in GitHub Issues — stampa, partnership, segnalazioni di sicurezza, richieste di rimozione — scrivi a <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tempi di risposta</h2>
<p>Cerco di leggere tutto entro una settimana, ma Toolhub viene costruito e mantenuto nel tempo libero, oltre a un lavoro principale. Se qualcosa è urgente (es. sicurezza), scrivilo nell'oggetto.</p>
""".strip(),
            },
            "pt": {
                "title": "Contato",
                "h1": "Contato",
                "description": "Fala com o mantenedor do Toolhub via GitHub Issues para bugs, pedidos de funcionalidade e ideias de ferramentas, ou por e-mail pro resto.",
                "body": f"""
<p>Toolhub é um side project de uma pessoa só. Tempos de resposta best-effort, não comerciais. Não tem formulário de contato — o site não tem backend, de propósito.</p>

<h2>GitHub Issues</h2>
<p>Para relatos de bug, pedidos de funcionalidade, correções de tradução e ideias de novas ferramentas, abra uma issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>O GitHub Issues é preferido porque dá pra discussão uma URL permanente que outras pessoas com a mesma dúvida vão poder achar depois.</p>

<h2>E-mail</h2>
<p>Pra coisas que não cabem em GitHub Issues — imprensa, parceria, disclosure de segurança, pedidos de takedown — mande um e-mail pra <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tempos de resposta</h2>
<p>Eu tento ler tudo dentro de uma semana, mas o Toolhub é construído e mantido no tempo livre, junto com um trabalho principal. Se for urgente (ex.: segurança), coloca isso no assunto.</p>
""".strip(),
            },
            "pl": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Skontaktuj się z maintainerem Toolhub przez GitHub Issues w sprawie bugów, propozycji funkcji i pomysłów na narzędzia, albo mailem do reszty spraw.",
                "body": f"""
<p>Toolhub to jednoosobowy side project. Czasy odpowiedzi best-effort, nie komercyjne. Nie ma formularza kontaktowego — strona z założenia nie ma backendu.</p>

<h2>GitHub Issues</h2>
<p>W sprawie zgłoszeń bugów, propozycji funkcji, poprawek tłumaczeń i pomysłów na nowe narzędzia — otwórz issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues są preferowane, bo dają dyskusji stały URL, który inni ludzie z tym samym pytaniem znajdą później.</p>

<h2>Mail</h2>
<p>W sprawach, które nie pasują do GitHub Issues — prasa, współpraca, zgłoszenia bezpieczeństwa, takedown — pisz na <code>{CONTACT_EMAIL}</code>.</p>

<h2>Czasy odpowiedzi</h2>
<p>Staram się czytać wszystko w ciągu tygodnia, ale Toolhub jest budowany i utrzymywany po godzinach, obok głównej pracy. Jeśli coś jest pilne (np. bezpieczeństwo), napisz to w temacie.</p>
""".strip(),
            },
            "ja": {
                "title": "お問い合わせ",
                "h1": "お問い合わせ",
                "description": "バグ報告・機能リクエスト・新ツールのアイデアは GitHub Issues、それ以外はメールで Toolhub のメンテナーへご連絡ください。",
                "body": f"""
<p>Toolhub は個人で運営するサイドプロジェクトです。返信はベストエフォートで、商用サポートではありません。お問い合わせフォームは用意していません — このサイトはあえてバックエンドを持たない設計です。</p>

<h2>GitHub Issues</h2>
<p>バグ報告、機能リクエスト、翻訳の修正、新しいツールのアイデアは Issue を立ててください：</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues を優先しているのは、同じ疑問を持つ他の方が後から見つけられる、恒久的な URL がやりとりに残るためです。</p>

<h2>メール</h2>
<p>GitHub Issues に向かない用件 — プレス、提携、セキュリティ脆弱性の通報、削除要請など — は <code>{CONTACT_EMAIL}</code> 宛にメールしてください。</p>

<h2>返信までの時間</h2>
<p>すべてに 1 週間以内に目を通すよう心がけていますが、Toolhub は本業の傍ら、空き時間で開発・運用しています。急ぎの場合（セキュリティなど）は、件名にその旨をご記入ください。</p>
""".strip(),
            },
            "nl": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Bereik de Toolhub-maintainer via GitHub Issues voor bug reports, feature requests en tool-ideeën, of per e-mail voor de rest.",
                "body": f"""
<p>Toolhub is een eenmans-side project. Best-effort responsetijden, niet commercieel. Er is geen contactformulier — deze site heeft bewust geen backend.</p>

<h2>GitHub Issues</h2>
<p>Voor bug reports, feature requests, vertaalcorrecties en ideeën voor nieuwe tools — open een issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues heeft de voorkeur omdat het de discussie een permanente URL geeft die andere mensen met dezelfde vraag later kunnen vinden.</p>

<h2>E-mail</h2>
<p>Voor zaken die niet bij GitHub Issues passen — pers, samenwerking, security disclosure, takedown-verzoeken — mail naar <code>{CONTACT_EMAIL}</code>.</p>

<h2>Responsetijden</h2>
<p>Ik probeer alles binnen een week te lezen, maar Toolhub wordt in vrije tijd naast een dagbaan gebouwd en onderhouden. Als iets urgent is (bijvoorbeeld security), zet dat dan in de subject line.</p>
""".strip(),
            },
        },
    },

    "for-schools": {
        "slug": "for-schools",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "Toolhub for Schools",
                "h1": "Toolhub for Schools",
                "description": "Privacy-first developer and utility tools for classrooms. No signup, no tracking, multilingual, self-hostable. Filter-friendly and safe to share with students.",
                "body": f"""
<h2>Toolhub for classrooms</h2>
<p>Toolhub is a set of small in-browser tools that students can use without creating an account, without being tracked, and without being redirected to ads or affiliate funnels. Every tool runs entirely in the browser, which means student input never leaves the school network — there is no backend to call.</p>
<p>If you teach in a primary, secondary or tertiary setting and need a quick utility (a regex tester, a colour converter, a Base64 encoder, a password generator for a security lesson), Toolhub is built to be safe to put on the projector and safe to send to a class.</p>

<h2>Curriculum tie-ins</h2>
<ul>
<li><strong>Computer science:</strong> the <a href="/regex-tester/">regex tester</a> for pattern matching, the <a href="/base64-encoder/">Base64 encoder</a> for data lessons, the <a href="/hash-generator/">hash generator</a> for talking about integrity, the <a href="/cidr-calculator/">CIDR calculator</a> for networking units.</li>
<li><strong>Design and digital media:</strong> the <a href="/color-converter/">colour converter</a> and <a href="/color-picker/">colour picker</a> for talking about colour models, the <a href="/wcag-contrast/">WCAG contrast checker</a> for accessibility.</li>
<li><strong>Security awareness:</strong> the <a href="/password-generator/">password generator</a> for talking about entropy and password strength, the <a href="/jwt-decoder/">JWT decoder</a> for showing what's actually inside a token.</li>
<li><strong>Maths and health:</strong> the <a href="/percentage-calculator/">percentage calculator</a>, <a href="/unit-converter/">unit converter</a>, and <a href="/bmi-calculator/">BMI calculator</a> (the BMI page carries its own "not medical advice" notice).</li>
</ul>

<h2>Languages supported</h2>
<p>Every tool is translated into nine languages so students can work in their first language:</p>
<ul>
<li>English</li>
<li>Deutsch (German)</li>
<li>Español (Spanish)</li>
<li>Français (French)</li>
<li>Italiano (Italian)</li>
<li>Português (Portuguese)</li>
<li>Polski (Polish)</li>
<li>日本語 (Japanese)</li>
<li>Nederlands (Dutch)</li>
</ul>

<h2>Self-hosted option</h2>
<p>If your school network blocks external sites or you'd rather have full control, the entire site is around 5 MB and works offline as a Progressive Web App. You can mirror it on a school intranet — it's a static folder of HTML, CSS and JavaScript with no build step required to serve, just put the files behind any web server.</p>
<p>The full source is at <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-friendly</h2>
<p>Toolhub is designed to play nicely with school web filters:</p>
<ul>
<li>No embedded social media widgets.</li>
<li>No chat widgets or live-chat overlays.</li>
<li>No auto-redirects to other sites.</li>
<li>No video or audio that auto-plays.</li>
<li>SafeSearch-friendly content — no adult tools, no gambling, no crypto-bro affiliate placements.</li>
</ul>

<h2>Contact for educators</h2>
<p>If you're using Toolhub in a classroom and want to tell me about it, suggest a tool for your subject, or contribute a translation for a language we don't yet cover well, please get in touch via <a href="/contact/">the contact page</a>. Bulk-translation contributions from native speakers — especially for less-served languages — are very welcome.</p>
""".strip(),
            },
            "de": {
                "title": "Toolhub für Schulen",
                "h1": "Toolhub für Schulen",
                "description": "Datenschutzfreundliche Entwickler- und Utility-Tools für den Unterricht. Ohne Anmeldung, ohne Tracking, mehrsprachig, selbst hostbar. Filter-freundlich und sicher zum Teilen mit Schülern.",
                "body": f"""
<h2>Toolhub im Klassenzimmer</h2>
<p>Toolhub ist eine Sammlung kleiner Browser-Tools, die Schülerinnen und Schüler nutzen können, ohne ein Konto anzulegen, ohne getrackt zu werden und ohne auf Werbung oder Affiliate-Trichter umgeleitet zu werden. Jedes Tool läuft komplett im Browser, was heißt: Schüler-Eingaben verlassen das Schulnetz nie — es gibt kein Backend, das aufgerufen würde.</p>
<p>Wenn Sie in einer Grund-, Sekundar- oder Hochschule unterrichten und schnell ein Utility brauchen (einen Regex-Tester, einen Farbkonverter, einen Base64-Encoder, einen Passwortgenerator für eine Security-Stunde), ist Toolhub so gebaut, dass es sicher auf den Beamer kann und sicher an eine Klasse weitergegeben werden kann.</p>

<h2>Anknüpfung an den Lehrplan</h2>
<ul>
<li><strong>Informatik:</strong> der <a href="/regex-tester/">Regex-Tester</a> für Pattern Matching, der <a href="/base64-encoder/">Base64-Encoder</a> für Datenlektionen, der <a href="/hash-generator/">Hash-Generator</a> als Aufhänger zum Thema Integrität, der <a href="/cidr-calculator/">CIDR-Rechner</a> für Netzwerk-Einheiten.</li>
<li><strong>Gestaltung und digitale Medien:</strong> der <a href="/color-converter/">Farbkonverter</a> und der <a href="/color-picker/">Farbwähler</a> für Farbmodelle, der <a href="/wcag-contrast/">WCAG-Kontrast-Checker</a> für Barrierefreiheit.</li>
<li><strong>Security-Awareness:</strong> der <a href="/password-generator/">Passwortgenerator</a> zur Erklärung von Entropie und Passwortstärke, der <a href="/jwt-decoder/">JWT-Decoder</a>, um zu zeigen, was wirklich in einem Token steht.</li>
<li><strong>Mathe und Gesundheit:</strong> der <a href="/percentage-calculator/">Prozentrechner</a>, <a href="/unit-converter/">Einheitenkonverter</a> und <a href="/bmi-calculator/">BMI-Rechner</a> (die BMI-Seite trägt ihren eigenen Hinweis „keine medizinische Beratung").</li>
</ul>

<h2>Unterstützte Sprachen</h2>
<p>Jedes Tool ist in neun Sprachen übersetzt, damit Schülerinnen und Schüler in ihrer Erstsprache arbeiten können:</p>
<ul>
<li>English</li>
<li>Deutsch</li>
<li>Español (Spanisch)</li>
<li>Français (Französisch)</li>
<li>Italiano (Italienisch)</li>
<li>Português (Portugiesisch)</li>
<li>Polski (Polnisch)</li>
<li>日本語 (Japanisch)</li>
<li>Nederlands (Niederländisch)</li>
</ul>

<h2>Self-Hosting-Option</h2>
<p>Wenn Ihr Schulnetzwerk externe Seiten blockiert oder Sie volle Kontrolle haben möchten: Die ganze Seite ist etwa 5 MB groß und funktioniert offline als Progressive Web App. Sie können sie in einem Schul-Intranet spiegeln — es ist ein statischer Ordner aus HTML, CSS und JavaScript, ohne Build-Schritt zum Ausliefern. Einfach die Dateien hinter einen beliebigen Webserver legen.</p>
<p>Der komplette Quellcode liegt auf <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-freundlich</h2>
<p>Toolhub ist so gebaut, dass es gut mit Schul-Webfiltern zusammenarbeitet:</p>
<ul>
<li>Keine eingebetteten Social-Media-Widgets.</li>
<li>Keine Chat-Widgets oder Live-Chat-Overlays.</li>
<li>Keine automatischen Weiterleitungen auf andere Seiten.</li>
<li>Kein Video oder Audio, das von selbst startet.</li>
<li>SafeSearch-freundliche Inhalte — keine Adult-Tools, kein Glücksspiel, keine Krypto-Affiliate-Platzierungen.</li>
</ul>

<h2>Kontakt für Lehrkräfte</h2>
<p>Wenn Sie Toolhub im Unterricht einsetzen und davon erzählen, ein Tool für Ihr Fach vorschlagen oder eine Übersetzung für eine bisher schlecht abgedeckte Sprache beisteuern möchten, melden Sie sich über die <a href="/contact/">Kontaktseite</a>. Größere Übersetzungs-Beiträge von Muttersprachlern — besonders für weniger versorgte Sprachen — sind ausdrücklich willkommen.</p>
""".strip(),
            },
            "es": {
                "title": "Toolhub para escuelas",
                "h1": "Toolhub para escuelas",
                "description": "Herramientas para desarrolladores y utilidades, centradas en la privacidad, pensadas para el aula. Sin registro, sin tracking, multilingüe y autoalojable. Compatible con filtros web y seguro para compartir con estudiantes.",
                "body": f"""
<h2>Toolhub en el aula</h2>
<p>Toolhub es un conjunto de pequeñas herramientas que funcionan en el navegador y que los estudiantes pueden usar sin crear una cuenta, sin ser rastreados y sin que se les redirija a anuncios o embudos de afiliados. Cada herramienta corre enteramente en el navegador, lo que significa que lo que el estudiante escribe nunca sale de la red del centro — no hay backend al que llamar.</p>
<p>Si imparte clases en primaria, secundaria o universidad y necesita una utilidad rápida (un probador de regex, un convertidor de color, un codificador Base64, un generador de contraseñas para una clase de seguridad), Toolhub está pensado para ser seguro de proyectar y seguro de compartir con un grupo.</p>

<h2>Conexión con el currículo</h2>
<ul>
<li><strong>Informática:</strong> el <a href="/regex-tester/">probador de regex</a> para coincidencia de patrones, el <a href="/base64-encoder/">codificador Base64</a> para clases sobre datos, el <a href="/hash-generator/">generador de hash</a> para hablar de integridad, la <a href="/cidr-calculator/">calculadora CIDR</a> para temas de redes.</li>
<li><strong>Diseño y medios digitales:</strong> el <a href="/color-converter/">convertidor de color</a> y el <a href="/color-picker/">selector de color</a> para hablar de modelos de color, el <a href="/wcag-contrast/">comprobador de contraste WCAG</a> para accesibilidad.</li>
<li><strong>Concienciación en seguridad:</strong> el <a href="/password-generator/">generador de contraseñas</a> para hablar de entropía y robustez de contraseñas, el <a href="/jwt-decoder/">decodificador JWT</a> para enseñar qué hay realmente dentro de un token.</li>
<li><strong>Matemáticas y salud:</strong> la <a href="/percentage-calculator/">calculadora de porcentajes</a>, el <a href="/unit-converter/">convertidor de unidades</a> y la <a href="/bmi-calculator/">calculadora de IMC</a> (la página de IMC lleva su propio aviso de "no es consejo médico").</li>
</ul>

<h2>Idiomas disponibles</h2>
<p>Cada herramienta está traducida a nueve idiomas para que los estudiantes puedan trabajar en su lengua materna:</p>
<ul>
<li>English (inglés)</li>
<li>Deutsch (alemán)</li>
<li>Español</li>
<li>Français (francés)</li>
<li>Italiano</li>
<li>Português</li>
<li>Polski (polaco)</li>
<li>日本語 (japonés)</li>
<li>Nederlands (neerlandés)</li>
</ul>

<h2>Opción de alojamiento propio</h2>
<p>Si la red del centro bloquea sitios externos o si prefiere tener control total, el sitio entero pesa unos 5 MB y funciona sin conexión como Progressive Web App. Puede replicarlo en una intranet escolar — es una carpeta estática de HTML, CSS y JavaScript sin paso de build para servir; basta con poner los ficheros detrás de cualquier servidor web.</p>
<p>El código fuente completo está en <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatible con filtros web</h2>
<p>Toolhub está diseñado para llevarse bien con los filtros web escolares:</p>
<ul>
<li>Sin widgets de redes sociales incrustados.</li>
<li>Sin widgets de chat ni overlays de chat en vivo.</li>
<li>Sin redirecciones automáticas a otros sitios.</li>
<li>Sin vídeo o audio que se reproduzca solo.</li>
<li>Contenido compatible con SafeSearch — sin herramientas para adultos, sin apuestas, sin colocaciones de afiliados cripto.</li>
</ul>

<h2>Contacto para educadores</h2>
<p>Si usa Toolhub en el aula y quiere contármelo, sugerir una herramienta para su asignatura o aportar una traducción para un idioma que aún cubrimos mal, contacte a través de la <a href="/contact/">página de contacto</a>. Las contribuciones de traducción de hablantes nativos — sobre todo para idiomas menos cubiertos — son muy bienvenidas.</p>
""".strip(),
            },
            "fr": {
                "title": "Toolhub pour les écoles",
                "h1": "Toolhub pour les écoles",
                "description": "Outils dev et utilitaires axés sur la confidentialité pour la classe. Sans inscription, sans tracking, multilingue, auto-hébergeable. Compatible avec les filtres et sûr à partager avec des élèves.",
                "body": f"""
<h2>Toolhub en classe</h2>
<p>Toolhub est un ensemble de petits outils dans le navigateur que les élèves peuvent utiliser sans créer de compte, sans être pistés, et sans être redirigés vers des pubs ou des tunnels d'affiliation. Chaque outil tourne entièrement dans le navigateur, ce qui veut dire que ce que tape un élève ne sort jamais du réseau de l'établissement — il n'y a pas de backend à appeler.</p>
<p>Si vous enseignez en primaire, secondaire ou supérieur et qu'il vous faut un utilitaire rapide (un testeur de regex, un convertisseur de couleur, un encodeur Base64, un générateur de mots de passe pour une séance de sécurité), Toolhub est conçu pour être sans risque à projeter et sans risque à partager avec une classe.</p>

<h2>Liens avec le programme</h2>
<ul>
<li><strong>Informatique :</strong> le <a href="/regex-tester/">testeur de regex</a> pour la correspondance de motifs, l'<a href="/base64-encoder/">encodeur Base64</a> pour les cours sur les données, le <a href="/hash-generator/">générateur de hash</a> pour parler d'intégrité, la <a href="/cidr-calculator/">calculatrice CIDR</a> pour les unités réseau.</li>
<li><strong>Design et médias numériques :</strong> le <a href="/color-converter/">convertisseur de couleurs</a> et le <a href="/color-picker/">sélecteur de couleurs</a> pour parler des modèles de couleur, le <a href="/wcag-contrast/">vérificateur de contraste WCAG</a> pour l'accessibilité.</li>
<li><strong>Sensibilisation à la sécurité :</strong> le <a href="/password-generator/">générateur de mots de passe</a> pour parler d'entropie et de robustesse, le <a href="/jwt-decoder/">décodeur JWT</a> pour montrer ce qu'il y a vraiment dans un token.</li>
<li><strong>Maths et santé :</strong> la <a href="/percentage-calculator/">calculatrice de pourcentage</a>, le <a href="/unit-converter/">convertisseur d'unités</a> et la <a href="/bmi-calculator/">calculatrice d'IMC</a> (la page IMC porte son propre avertissement « pas un conseil médical »).</li>
</ul>

<h2>Langues supportées</h2>
<p>Chaque outil est traduit dans neuf langues, pour que les élèves puissent travailler dans leur première langue :</p>
<ul>
<li>English (anglais)</li>
<li>Deutsch (allemand)</li>
<li>Español (espagnol)</li>
<li>Français</li>
<li>Italiano (italien)</li>
<li>Português (portugais)</li>
<li>Polski (polonais)</li>
<li>日本語 (japonais)</li>
<li>Nederlands (néerlandais)</li>
</ul>

<h2>Auto-hébergement</h2>
<p>Si le réseau de l'école bloque les sites externes ou si vous voulez tout contrôler, le site entier fait environ 5 Mo et fonctionne hors-ligne en tant que Progressive Web App. Vous pouvez le mirroir sur un intranet scolaire — c'est un dossier statique de HTML, CSS et JavaScript, sans étape de build pour le servir : il suffit de poser les fichiers derrière n'importe quel serveur web.</p>
<p>Le code source complet est sur <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatible avec les filtres</h2>
<p>Toolhub est pensé pour bien s'entendre avec les filtres web scolaires :</p>
<ul>
<li>Pas de widgets de réseaux sociaux intégrés.</li>
<li>Pas de widget de chat ni d'overlay de chat en direct.</li>
<li>Pas de redirections automatiques vers d'autres sites.</li>
<li>Pas de vidéo ou d'audio qui se lance tout seul.</li>
<li>Contenu compatible SafeSearch — pas d'outils pour adultes, pas de paris, pas de placements d'affiliation crypto.</li>
</ul>

<h2>Contact enseignants</h2>
<p>Si vous utilisez Toolhub en classe et voulez m'en parler, suggérer un outil pour votre matière, ou contribuer à une traduction dans une langue encore mal couverte, passez par la <a href="/contact/">page de contact</a>. Les contributions de traduction de locuteurs natifs — surtout pour les langues les moins couvertes — sont très bienvenues.</p>
""".strip(),
            },
            "it": {
                "title": "Toolhub per le scuole",
                "h1": "Toolhub per le scuole",
                "description": "Strumenti per sviluppatori e utility orientati alla privacy per la classe. Senza registrazione, senza tracking, multilingua, self-hostabili. Compatibili con i filtri web e sicuri da condividere con gli studenti.",
                "body": f"""
<h2>Toolhub in classe</h2>
<p>Toolhub è una raccolta di piccoli strumenti che girano in browser e che gli studenti possono usare senza creare un account, senza essere tracciati e senza essere reindirizzati a pubblicità o funnel di affiliazione. Ogni strumento gira interamente nel browser, il che significa che ciò che lo studente scrive non lascia mai la rete della scuola — non c'è alcun backend da chiamare.</p>
<p>Se insegna in una scuola primaria, secondaria o all'università e ha bisogno di un'utility veloce (un tester di regex, un convertitore di colori, un encoder Base64, un generatore di password per una lezione di sicurezza), Toolhub è pensato per essere sicuro da proiettare e sicuro da condividere con la classe.</p>

<h2>Collegamenti con il programma</h2>
<ul>
<li><strong>Informatica:</strong> il <a href="/regex-tester/">tester di regex</a> per il pattern matching, l'<a href="/base64-encoder/">encoder Base64</a> per le lezioni sui dati, il <a href="/hash-generator/">generatore di hash</a> per parlare di integrità, il <a href="/cidr-calculator/">calcolatore CIDR</a> per le unità di reti.</li>
<li><strong>Design e media digitali:</strong> il <a href="/color-converter/">convertitore di colori</a> e il <a href="/color-picker/">selettore di colori</a> per parlare di modelli di colore, il <a href="/wcag-contrast/">verificatore di contrasto WCAG</a> per l'accessibilità.</li>
<li><strong>Consapevolezza sulla sicurezza:</strong> il <a href="/password-generator/">generatore di password</a> per parlare di entropia e forza delle password, il <a href="/jwt-decoder/">decoder JWT</a> per mostrare cosa c'è davvero dentro un token.</li>
<li><strong>Matematica e salute:</strong> il <a href="/percentage-calculator/">calcolatore di percentuali</a>, il <a href="/unit-converter/">convertitore di unità</a> e il <a href="/bmi-calculator/">calcolatore BMI</a> (la pagina BMI ha un proprio avviso "non è un consiglio medico").</li>
</ul>

<h2>Lingue supportate</h2>
<p>Ogni strumento è tradotto in nove lingue, così gli studenti possono lavorare nella loro prima lingua:</p>
<ul>
<li>English (inglese)</li>
<li>Deutsch (tedesco)</li>
<li>Español (spagnolo)</li>
<li>Français (francese)</li>
<li>Italiano</li>
<li>Português (portoghese)</li>
<li>Polski (polacco)</li>
<li>日本語 (giapponese)</li>
<li>Nederlands (olandese)</li>
</ul>

<h2>Opzione self-hosted</h2>
<p>Se la rete della scuola blocca i siti esterni o se preferisce avere il pieno controllo, il sito intero pesa circa 5 MB e funziona offline come Progressive Web App. Può replicarlo su un'intranet scolastica — è una cartella statica di HTML, CSS e JavaScript, senza passi di build per servirlo: basta mettere i file dietro un qualsiasi web server.</p>
<p>Il codice sorgente completo è su <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatibile con i filtri</h2>
<p>Toolhub è progettato per andare d'accordo con i filtri web scolastici:</p>
<ul>
<li>Niente widget social embeddati.</li>
<li>Niente widget di chat o overlay di live-chat.</li>
<li>Niente redirect automatici verso altri siti.</li>
<li>Niente video o audio che parte da solo.</li>
<li>Contenuti compatibili con SafeSearch — niente strumenti per adulti, niente gambling, niente piazzamenti di affiliate crypto.</li>
</ul>

<h2>Contatti per chi insegna</h2>
<p>Se usa Toolhub in classe e vuole raccontarmelo, suggerirmi uno strumento per la sua materia o contribuire a una traduzione per una lingua che copriamo ancora male, mi contatti tramite la <a href="/contact/">pagina di contatto</a>. I contributi di traduzione da madrelingua — soprattutto per le lingue meno servite — sono molto graditi.</p>
""".strip(),
            },
            "pt": {
                "title": "Toolhub para escolas",
                "h1": "Toolhub para escolas",
                "description": "Ferramentas para devs e utilitários com foco em privacidade pra sala de aula. Sem cadastro, sem tracking, multilíngue, possível de hospedar localmente. Compatível com filtros e seguro pra compartilhar com alunos.",
                "body": f"""
<h2>Toolhub na sala de aula</h2>
<p>O Toolhub é um conjunto de pequenas ferramentas que rodam no navegador e que os alunos podem usar sem criar conta, sem serem rastreados e sem serem redirecionados pra anúncios ou funis de afiliados. Cada ferramenta roda inteiramente no navegador, ou seja, o que o aluno digita nunca sai da rede da escola — não tem backend pra ser chamado.</p>
<p>Se você dá aula no ensino fundamental, médio ou superior e precisa de um utilitário rápido (um testador de regex, um conversor de cores, um codificador Base64, um gerador de senhas pra uma aula de segurança), o Toolhub é feito pra ser seguro de projetar e seguro de mandar pra turma.</p>

<h2>Ligação com o currículo</h2>
<ul>
<li><strong>Computação:</strong> o <a href="/regex-tester/">testador de regex</a> pra casamento de padrões, o <a href="/base64-encoder/">codificador Base64</a> pra aulas sobre dados, o <a href="/hash-generator/">gerador de hash</a> pra falar de integridade, a <a href="/cidr-calculator/">calculadora CIDR</a> pra módulos de redes.</li>
<li><strong>Design e mídia digital:</strong> o <a href="/color-converter/">conversor de cores</a> e o <a href="/color-picker/">seletor de cores</a> pra falar de modelos de cor, o <a href="/wcag-contrast/">verificador de contraste WCAG</a> pra acessibilidade.</li>
<li><strong>Consciência em segurança:</strong> o <a href="/password-generator/">gerador de senhas</a> pra falar de entropia e força de senha, o <a href="/jwt-decoder/">decodificador JWT</a> pra mostrar o que realmente tem dentro de um token.</li>
<li><strong>Matemática e saúde:</strong> a <a href="/percentage-calculator/">calculadora de porcentagem</a>, o <a href="/unit-converter/">conversor de unidades</a> e a <a href="/bmi-calculator/">calculadora de IMC</a> (a página de IMC tem o próprio aviso de "não é orientação médica").</li>
</ul>

<h2>Idiomas suportados</h2>
<p>Cada ferramenta está traduzida pra nove idiomas, pra que os alunos possam trabalhar na própria língua:</p>
<ul>
<li>English (inglês)</li>
<li>Deutsch (alemão)</li>
<li>Español (espanhol)</li>
<li>Français (francês)</li>
<li>Italiano</li>
<li>Português</li>
<li>Polski (polonês)</li>
<li>日本語 (japonês)</li>
<li>Nederlands (holandês)</li>
</ul>

<h2>Opção self-hosted</h2>
<p>Se a rede da escola bloqueia sites externos ou se você prefere ter controle total, o site inteiro tem cerca de 5 MB e funciona offline como Progressive Web App. Você pode espelhar isso numa intranet escolar — é uma pasta estática de HTML, CSS e JavaScript, sem build step pra servir: basta colocar os arquivos atrás de qualquer servidor web.</p>
<p>O código-fonte completo está em <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatível com filtros</h2>
<p>O Toolhub é desenhado pra se dar bem com filtros web de escola:</p>
<ul>
<li>Sem widgets de redes sociais embutidos.</li>
<li>Sem widgets de chat ou overlays de chat ao vivo.</li>
<li>Sem redirecionamentos automáticos pra outros sites.</li>
<li>Sem vídeo ou áudio que toca sozinho.</li>
<li>Conteúdo compatível com SafeSearch — sem ferramentas adultas, sem apostas, sem colocações de afiliado de cripto.</li>
</ul>

<h2>Contato pra educadores</h2>
<p>Se você usa o Toolhub em sala de aula e quer me contar, sugerir uma ferramenta pra sua matéria ou contribuir com uma tradução pra algum idioma que ainda cobrimos mal, fala comigo pela <a href="/contact/">página de contato</a>. Contribuições de tradução de falantes nativos — principalmente pra idiomas menos cobertos — são muito bem-vindas.</p>
""".strip(),
            },
            "pl": {
                "title": "Toolhub dla szkół",
                "h1": "Toolhub dla szkół",
                "description": "Narzędzia dla devów i utility z naciskiem na prywatność, do pracy w klasie. Bez rejestracji, bez trackingu, wielojęzyczne, możliwe do self-hostingu. Przyjazne dla filtrów i bezpieczne do udostępniania uczniom.",
                "body": f"""
<h2>Toolhub w klasie</h2>
<p>Toolhub to zestaw niewielkich narzędzi działających w przeglądarce, których uczniowie mogą używać bez zakładania konta, bez śledzenia i bez przekierowań na reklamy czy lejki afiliacyjne. Każde narzędzie działa w całości w przeglądarce, czyli to, co uczeń wpisuje, nigdy nie opuszcza sieci szkolnej — nie ma backendu, do którego trzeba by dzwonić.</p>
<p>Jeśli uczysz w szkole podstawowej, średniej albo na uczelni i potrzebujesz szybkiego utility (testera regex, konwertera kolorów, enkodera Base64, generatora haseł na lekcję o bezpieczeństwie), Toolhub jest zbudowany tak, żeby można go było bezpiecznie puścić na projektor i bezpiecznie wysłać do klasy.</p>

<h2>Powiązanie z podstawą programową</h2>
<ul>
<li><strong>Informatyka:</strong> <a href="/regex-tester/">tester regex</a> do dopasowywania wzorców, <a href="/base64-encoder/">enkoder Base64</a> do lekcji o danych, <a href="/hash-generator/">generator hash</a> do rozmów o integralności, <a href="/cidr-calculator/">kalkulator CIDR</a> do modułów sieciowych.</li>
<li><strong>Design i media cyfrowe:</strong> <a href="/color-converter/">konwerter kolorów</a> i <a href="/color-picker/">picker kolorów</a> do rozmów o modelach barwnych, <a href="/wcag-contrast/">checker kontrastu WCAG</a> do dostępności.</li>
<li><strong>Świadomość bezpieczeństwa:</strong> <a href="/password-generator/">generator haseł</a> do tematu entropii i siły hasła, <a href="/jwt-decoder/">dekoder JWT</a>, żeby pokazać, co naprawdę jest w tokenie.</li>
<li><strong>Matematyka i zdrowie:</strong> <a href="/percentage-calculator/">kalkulator procentów</a>, <a href="/unit-converter/">konwerter jednostek</a> i <a href="/bmi-calculator/">kalkulator BMI</a> (strona BMI ma własne ostrzeżenie „to nie jest porada medyczna").</li>
</ul>

<h2>Wspierane języki</h2>
<p>Każde narzędzie jest przetłumaczone na dziewięć języków, żeby uczniowie mogli pracować w swoim pierwszym języku:</p>
<ul>
<li>English (angielski)</li>
<li>Deutsch (niemiecki)</li>
<li>Español (hiszpański)</li>
<li>Français (francuski)</li>
<li>Italiano (włoski)</li>
<li>Português (portugalski)</li>
<li>Polski</li>
<li>日本語 (japoński)</li>
<li>Nederlands (niderlandzki)</li>
</ul>

<h2>Opcja self-hostingu</h2>
<p>Jeśli sieć szkolna blokuje strony zewnętrzne albo wolisz mieć pełną kontrolę — cała strona ma około 5 MB i działa offline jako Progressive Web App. Można ją zlustrzyć w intranecie szkoły — to statyczny folder z HTML, CSS i JavaScript, bez build stepu do podania: wystarczy położyć pliki za dowolnym serwerem WWW.</p>
<p>Cały kod źródłowy jest na <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Przyjazne filtrom</h2>
<p>Toolhub jest tak zrobiony, żeby grać dobrze ze szkolnymi filtrami WWW:</p>
<ul>
<li>Brak osadzonych widgetów social media.</li>
<li>Brak widgetów czatu i overlayów live-chatu.</li>
<li>Brak auto-przekierowań na inne strony.</li>
<li>Brak wideo ani audio, które samo się uruchamia.</li>
<li>Treść zgodna z SafeSearch — żadnych narzędzi dla dorosłych, żadnego hazardu, żadnych krypto-afiliacji.</li>
</ul>

<h2>Kontakt dla nauczycieli</h2>
<p>Jeśli używasz Toolhub w klasie i chcesz mi o tym powiedzieć, zaproponować narzędzie do swojego przedmiotu albo dorzucić tłumaczenie do języka, który słabo pokrywamy — skontaktuj się przez <a href="/contact/">stronę kontaktową</a>. Większe wkłady tłumaczeniowe od native speakerów — zwłaszcza do mniej pokrytych języków — są bardzo mile widziane.</p>
""".strip(),
            },
            "ja": {
                "title": "学校向け Toolhub",
                "h1": "学校向け Toolhub",
                "description": "教室向けの、プライバシー重視の開発者ツール／ユーティリティ。登録不要、トラッキングなし、多言語、セルフホスト可。フィルタとの相性がよく、生徒に共有しても安心。",
                "body": f"""
<h2>教室での Toolhub</h2>
<p>Toolhub は、ブラウザ内で動く小さなツールの集まりです。生徒はアカウントを作る必要なく、追跡されることなく、広告やアフィリエイト誘導に飛ばされることもなく利用できます。各ツールは完全にブラウザ内で動作するため、生徒が入力した内容が学校ネットワークから外に出ることはありません — 呼び出すバックエンド自体が存在しないからです。</p>
<p>小学校、中学・高校、大学・専門学校などで授業を担当されている方が、ちょっとしたユーティリティ（正規表現テスター、カラーコンバーター、Base64 エンコーダー、セキュリティの授業用パスワードジェネレーターなど）を必要とする場面で、Toolhub はプロジェクターに映しても安心、クラスに共有しても安心、というつくりになっています。</p>

<h2>カリキュラムとのつながり</h2>
<ul>
<li><strong>情報科：</strong>パターンマッチングには <a href="/regex-tester/">正規表現テスター</a>、データの単元には <a href="/base64-encoder/">Base64 エンコーダー</a>、整合性の話には <a href="/hash-generator/">ハッシュ生成ツール</a>、ネットワーク単元には <a href="/cidr-calculator/">CIDR 計算機</a>。</li>
<li><strong>デザイン・デジタルメディア：</strong><a href="/color-converter/">カラーコンバーター</a>と<a href="/color-picker/">カラーピッカー</a>でカラーモデルを、<a href="/wcag-contrast/">WCAG コントラストチェッカー</a>でアクセシビリティを。</li>
<li><strong>セキュリティ教育：</strong>エントロピーやパスワード強度の話には <a href="/password-generator/">パスワードジェネレーター</a>、トークンの中身を見せるには <a href="/jwt-decoder/">JWT デコーダー</a>。</li>
<li><strong>算数・数学・保健：</strong><a href="/percentage-calculator/">パーセンテージ計算機</a>、<a href="/unit-converter/">単位変換ツール</a>、<a href="/bmi-calculator/">BMI 計算機</a>（BMI ページには「医療アドバイスではありません」という注意書きが個別についています）。</li>
</ul>

<h2>対応言語</h2>
<p>各ツールは 9 つの言語に翻訳されているので、生徒が自分の第一言語で作業できます：</p>
<ul>
<li>English（英語）</li>
<li>Deutsch（ドイツ語）</li>
<li>Español（スペイン語）</li>
<li>Français（フランス語）</li>
<li>Italiano（イタリア語）</li>
<li>Português（ポルトガル語）</li>
<li>Polski（ポーランド語）</li>
<li>日本語</li>
<li>Nederlands（オランダ語）</li>
</ul>

<h2>セルフホストという選択肢</h2>
<p>学校のネットワークが外部サイトをブロックしている場合や、すべてを自分の管理下に置きたい場合、サイト全体は約 5 MB で、Progressive Web App としてオフラインでも動作します。校内イントラネットにミラーすることも可能です — HTML、CSS、JavaScript の静的フォルダなので、ビルド手順は不要、ファイルを任意の Web サーバーに置くだけで配信できます。</p>
<p>ソースコード全体は <a href="{REPO_URL}">{REPO_URL}</a> にあります。</p>

<h2>フィルタとの相性</h2>
<p>Toolhub は、学校の Web フィルタとうまく付き合えるように設計されています：</p>
<ul>
<li>SNS ウィジェットの埋め込みなし。</li>
<li>チャットウィジェットやライブチャットのオーバーレイなし。</li>
<li>他サイトへの自動リダイレクトなし。</li>
<li>動画・音声の自動再生なし。</li>
<li>SafeSearch と相性のよい内容 — 成人向けツール、ギャンブル、暗号資産アフィリエイトの掲載はありません。</li>
</ul>

<h2>教育関係の方へのお問い合わせ窓口</h2>
<p>Toolhub を教室で使ってくださっている、教科に合うツールを提案したい、まだ十分にカバーできていない言語の翻訳に協力したい、という方は<a href="/contact/">お問い合わせページ</a>からご連絡ください。ネイティブスピーカーによるまとまった翻訳の協力 — 特にカバーが薄い言語向け — は大歓迎です。</p>
""".strip(),
            },
            "nl": {
                "title": "Toolhub voor scholen",
                "h1": "Toolhub voor scholen",
                "description": "Privacy-first developer- en utility-tools voor in de klas. Geen registratie, geen tracking, meertalig, self-hostable. Filter-vriendelijk en veilig om met leerlingen te delen.",
                "body": f"""
<h2>Toolhub in de klas</h2>
<p>Toolhub is een set kleine in-browser tools die leerlingen kunnen gebruiken zonder een account aan te maken, zonder gevolgd te worden en zonder doorgestuurd te worden naar reclame of affiliate-funnels. Elke tool draait volledig in de browser, wat betekent dat wat een leerling intypt nooit het schoolnetwerk verlaat — er is geen backend om aan te roepen.</p>
<p>Als je lesgeeft in het basis-, voortgezet of hoger onderwijs en je hebt snel een utility nodig (een regex-tester, een colour converter, een Base64-encoder, een wachtwoordgenerator voor een security-les), dan is Toolhub gebouwd om veilig op de beamer te kunnen en veilig naar een klas te kunnen sturen.</p>

<h2>Aansluiting bij het curriculum</h2>
<ul>
<li><strong>Informatica:</strong> de <a href="/regex-tester/">regex tester</a> voor pattern matching, de <a href="/base64-encoder/">Base64 encoder</a> voor lessen over data, de <a href="/hash-generator/">hash generator</a> om over integriteit te praten, de <a href="/cidr-calculator/">CIDR calculator</a> voor netwerk-onderdelen.</li>
<li><strong>Design en digitale media:</strong> de <a href="/color-converter/">colour converter</a> en de <a href="/color-picker/">colour picker</a> om over kleurmodellen te praten, de <a href="/wcag-contrast/">WCAG contrast checker</a> voor toegankelijkheid.</li>
<li><strong>Security-bewustzijn:</strong> de <a href="/password-generator/">wachtwoordgenerator</a> om over entropie en wachtwoordsterkte te praten, de <a href="/jwt-decoder/">JWT decoder</a> om te laten zien wat er echt in een token zit.</li>
<li><strong>Wiskunde en gezondheid:</strong> de <a href="/percentage-calculator/">procentcalculator</a>, <a href="/unit-converter/">eenhedenconverter</a> en <a href="/bmi-calculator/">BMI-calculator</a> (de BMI-pagina heeft een eigen "geen medisch advies"-vermelding).</li>
</ul>

<h2>Ondersteunde talen</h2>
<p>Elke tool is vertaald naar negen talen, zodat leerlingen in hun eerste taal kunnen werken:</p>
<ul>
<li>English (Engels)</li>
<li>Deutsch (Duits)</li>
<li>Español (Spaans)</li>
<li>Français (Frans)</li>
<li>Italiano (Italiaans)</li>
<li>Português (Portugees)</li>
<li>Polski (Pools)</li>
<li>日本語 (Japans)</li>
<li>Nederlands</li>
</ul>

<h2>Self-hosted optie</h2>
<p>Als het schoolnetwerk externe sites blokkeert of als je liever volledige controle hebt, de hele site is ongeveer 5 MB en werkt offline als Progressive Web App. Je kunt hem mirroren op een school-intranet — het is een statische map met HTML, CSS en JavaScript, zonder build step om te serveren: zet de bestanden achter een willekeurige webserver.</p>
<p>De volledige source staat op <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-vriendelijk</h2>
<p>Toolhub is ontworpen om goed samen te werken met schoolwebfilters:</p>
<ul>
<li>Geen ingebedde social media widgets.</li>
<li>Geen chat widgets of live-chat overlays.</li>
<li>Geen automatische redirects naar andere sites.</li>
<li>Geen video of audio dat vanzelf afspeelt.</li>
<li>SafeSearch-vriendelijke inhoud — geen tools voor volwassenen, geen gokken, geen crypto-affiliate placements.</li>
</ul>

<h2>Contact voor docenten</h2>
<p>Gebruik je Toolhub in een klas en wil je het me laten weten, een tool voorstellen voor je vak, of bijdragen aan een vertaling voor een taal die we nog slecht dekken — neem dan contact op via de <a href="/contact/">contactpagina</a>. Bulk-vertaalbijdragen van native speakers — vooral voor minder bediende talen — zijn van harte welkom.</p>
""".strip(),
            },
        },
    },

    "privacy": {
        "slug": "privacy",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "Privacy Policy",
                "h1": "Privacy Policy",
                "description": "Toolhub privacy policy: tools run entirely in your browser, no signup, no accounts, no tool data leaves your device. Plausible for aggregate analytics, AdSense only with explicit consent.",
                "body": f"""
<p><strong>Last updated:</strong> {LAST_UPDATED}</p>

<h2>The short version</h2>
<p>Tools run entirely in your browser — nothing you type into them is sent anywhere. We measure aggregate, anonymous visits with <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (no cookies). If you choose to opt in, we may also serve display ads via Google AdSense, which does use cookies. You can decline ads at the consent banner; the rest of the site works identically either way.</p>

<h2>What we collect</h2>
<ul>
<li><strong>Tool inputs:</strong> nothing. Everything you paste into a tool stays in your browser. No tool sends data to a server.</li>
<li><strong>Visit analytics:</strong> Plausible counts page views, referrer, country, and device type — anonymously, in aggregate, without cookies. <a href="https://plausible.io/data-policy" rel="noopener">Plausible's data policy</a> covers what they do and don't collect.</li>
<li><strong>If you accept ads:</strong> Google AdSense sets cookies and may use them to personalise ads. Google's practices are governed by <a href="https://policies.google.com/technologies/ads" rel="noopener">Google's advertising privacy policy</a>.</li>
<li><strong>If you decline ads:</strong> no advertising scripts are loaded, no advertising cookies are set, ad slots are removed from the page.</li>
</ul>

<h2>Cookies</h2>
<p>The site itself uses one localStorage entry (<code>toolhub:consent</code>) to remember your ad-consent choice, plus a <code>theme</code> entry for your dark/light preference. Neither leaves your browser.</p>
<p>Plausible uses no cookies. Google AdSense uses cookies <em>only if</em> you accept them — you can change your choice anytime via the consent link in the footer.</p>

<h2>Third-party services</h2>
<ul>
<li><strong>Plausible Analytics</strong> — privacy-friendly, GDPR-compliant, EU-hosted. No personal data collected.</li>
<li><strong>Google AdSense</strong> — used only with explicit consent. Loads <code>pagead2.googlesyndication.com</code> and may set advertising cookies.</li>
<li><strong>GitHub Pages</strong> — site host. Standard server logs (IP, timestamp, URL) are kept by GitHub per <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">their privacy statement</a>.</li>
<li><strong>YouTube Thumbnail tool</strong> — when you use this one tool, your browser fetches an image directly from <code>i.ytimg.com</code> (YouTube's CDN). No authentication, no upload. See <a href="/how-we-handle-your-data/">data handling</a> for detail.</li>
</ul>

<h2>Affiliate links</h2>
<p>Some links in the footer are affiliate links — if you click through and sign up to a service we recommend (e.g. hosting providers), Toolhub may earn a referral. The price you pay is unaffected. Affiliate links are tagged with <code>rel="sponsored"</code>. See <a href="/affiliate-disclosure/">affiliate disclosure</a> for the full list.</p>

<h2>Your rights</h2>
<p>Under GDPR / UK GDPR / CCPA / the Slovak DPA, you can request access to or deletion of any personal data we hold. We don't hold any — there is no backend, no accounts, no user database. Plausible holds only aggregated visit data. Google's ad data is governed by their own request channels.</p>

<h2>Contact</h2>
<p>Questions about this policy? Reach out via <a href="/contact/">the contact page</a> or open an issue at <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "de": {
                "title": "Datenschutzerklärung",
                "h1": "Datenschutzerklärung",
                "description": "Toolhub-Datenschutzerklärung: Tools laufen komplett im Browser, ohne Anmeldung, ohne Konto, keine Tool-Daten verlassen dein Gerät. Plausible für aggregierte Statistik, AdSense nur mit ausdrücklicher Zustimmung.",
                "body": f"""
<p><strong>Zuletzt aktualisiert:</strong> {LAST_UPDATED}</p>

<h2>Die Kurzfassung</h2>
<p>Tools laufen komplett in deinem Browser — nichts, was du in sie eingibst, wird irgendwo hingeschickt. Wir zählen aggregierte, anonyme Besuche mit <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (keine Cookies). Wenn du explizit zustimmst, schalten wir zusätzlich Display-Anzeigen über Google AdSense, die Cookies verwenden. Du kannst Werbung im Consent-Banner ablehnen; der Rest der Seite funktioniert identisch.</p>

<h2>Was wir erfassen</h2>
<ul>
<li><strong>Tool-Eingaben:</strong> nichts. Alles, was du in ein Tool einfügst, bleibt in deinem Browser. Kein Tool schickt Daten an einen Server.</li>
<li><strong>Besuchs-Statistik:</strong> Plausible zählt Seitenaufrufe, Referrer, Land und Gerätetyp — anonym, aggregiert, ohne Cookies. <a href="https://plausible.io/data-policy" rel="noopener">Plausibles Datenrichtlinie</a> erklärt, was sie erfassen und was nicht.</li>
<li><strong>Wenn du Werbung akzeptierst:</strong> Google AdSense setzt Cookies und kann sie zur Personalisierung verwenden. Googles Praktiken regelt <a href="https://policies.google.com/technologies/ads" rel="noopener">Googles Werbe-Datenschutzrichtlinie</a>.</li>
<li><strong>Wenn du Werbung ablehnst:</strong> keine Werbe-Skripte werden geladen, keine Werbe-Cookies gesetzt, Anzeigenflächen werden aus der Seite entfernt.</li>
</ul>

<h2>Cookies</h2>
<p>Die Seite selbst nutzt einen localStorage-Eintrag (<code>toolhub:consent</code>), um deine Werbe-Entscheidung zu speichern, plus einen <code>theme</code>-Eintrag für deine Dark/Light-Präferenz. Beides verlässt deinen Browser nicht.</p>
<p>Plausible nutzt keine Cookies. Google AdSense nutzt Cookies <em>nur wenn</em> du zustimmst — die Entscheidung kannst du jederzeit über den Consent-Link im Footer ändern.</p>

<h2>Drittanbieter-Dienste</h2>
<ul>
<li><strong>Plausible Analytics</strong> — datenschutzfreundlich, DSGVO-konform, EU-gehostet. Keine personenbezogenen Daten.</li>
<li><strong>Google AdSense</strong> — nur mit ausdrücklicher Zustimmung. Lädt <code>pagead2.googlesyndication.com</code> und kann Werbe-Cookies setzen.</li>
<li><strong>GitHub Pages</strong> — Hosting. Standard-Serverlogs (IP, Zeitstempel, URL) bewahrt GitHub gemäß <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">ihrer Datenschutzerklärung</a> auf.</li>
<li><strong>YouTube-Thumbnail-Tool</strong> — wenn du dieses eine Tool nutzt, lädt dein Browser das Bild direkt von <code>i.ytimg.com</code> (YouTubes CDN). Keine Authentifizierung, kein Upload. Details unter <a href="/de/how-we-handle-your-data/">Datenverarbeitung</a>.</li>
</ul>

<h2>Affiliate-Links</h2>
<p>Einige Links im Footer sind Affiliate-Links — wenn du klickst und dich bei einem empfohlenen Dienst registrierst (z. B. Hosting-Anbieter), kann Toolhub eine Provision bekommen. Der Preis, den du zahlst, ändert sich nicht. Affiliate-Links sind mit <code>rel="sponsored"</code> markiert. Die vollständige Liste steht unter <a href="/de/affiliate-disclosure/">Affiliate-Offenlegung</a>.</p>

<h2>Deine Rechte</h2>
<p>Nach DSGVO / UK GDPR / CCPA / dem slowakischen Datenschutzgesetz kannst du Auskunft über oder Löschung deiner personenbezogenen Daten verlangen. Wir speichern keine — es gibt kein Backend, keine Konten, keine Nutzerdatenbank. Plausible hält nur aggregierte Besuchsdaten. Googles Werbedaten regeln deren eigene Anfragekanäle.</p>

<h2>Kontakt</h2>
<p>Fragen zu dieser Erklärung? Schreib über die <a href="/de/contact/">Kontaktseite</a> oder öffne ein Issue unter <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "es": {
                "title": "Política de privacidad",
                "h1": "Política de privacidad",
                "description": "Política de privacidad de Toolhub: las herramientas funcionan enteramente en el navegador, sin registro, sin cuentas, ningún dato sale de tu dispositivo. Plausible para analítica agregada, AdSense solo con consentimiento explícito.",
                "body": f"""
<p><strong>Última actualización:</strong> {LAST_UPDATED}</p>

<h2>La versión corta</h2>
<p>Las herramientas funcionan enteramente en tu navegador — lo que escribas en ellas no se envía a ningún sitio. Medimos visitas agregadas y anónimas con <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (sin cookies). Si decides aceptar, también podemos mostrar anuncios de display vía Google AdSense, que sí usa cookies. Puedes rechazar los anuncios en el banner de consentimiento; el resto del sitio funciona igual.</p>

<h2>Qué recogemos</h2>
<ul>
<li><strong>Datos que pegas en herramientas:</strong> nada. Todo lo que pegas en una herramienta se queda en tu navegador. Ninguna herramienta envía datos a un servidor.</li>
<li><strong>Analítica de visitas:</strong> Plausible cuenta páginas vistas, referrer, país y tipo de dispositivo — anónimamente, en agregado, sin cookies. La <a href="https://plausible.io/data-policy" rel="noopener">política de datos de Plausible</a> cubre qué recogen y qué no.</li>
<li><strong>Si aceptas anuncios:</strong> Google AdSense pone cookies y puede usarlas para personalizar anuncios. Las prácticas de Google están reguladas por la <a href="https://policies.google.com/technologies/ads" rel="noopener">política de privacidad publicitaria de Google</a>.</li>
<li><strong>Si rechazas anuncios:</strong> no se cargan scripts de publicidad, no se ponen cookies publicitarias, los huecos de anuncio desaparecen de la página.</li>
</ul>

<h2>Cookies</h2>
<p>El sitio en sí usa una entrada de localStorage (<code>toolhub:consent</code>) para recordar tu decisión sobre anuncios, más una entrada <code>theme</code> para tu preferencia de modo oscuro/claro. Ninguna sale de tu navegador.</p>
<p>Plausible no usa cookies. Google AdSense usa cookies <em>solo si</em> las aceptas — puedes cambiar tu decisión cuando quieras desde el enlace de consentimiento en el pie de página.</p>

<h2>Servicios de terceros</h2>
<ul>
<li><strong>Plausible Analytics</strong> — respetuoso con la privacidad, conforme al RGPD, alojado en la UE. No se recogen datos personales.</li>
<li><strong>Google AdSense</strong> — solo con consentimiento explícito. Carga <code>pagead2.googlesyndication.com</code> y puede poner cookies publicitarias.</li>
<li><strong>GitHub Pages</strong> — alojamiento del sitio. GitHub guarda los logs estándar del servidor (IP, timestamp, URL) según <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">su declaración de privacidad</a>.</li>
<li><strong>Herramienta YouTube Thumbnail</strong> — al usar esta herramienta concreta, tu navegador descarga la imagen directamente desde <code>i.ytimg.com</code> (la CDN de YouTube). Sin autenticación, sin subida. Detalles en <a href="/es/how-we-handle-your-data/">tratamiento de datos</a>.</li>
</ul>

<h2>Enlaces de afiliado</h2>
<p>Algunos enlaces del pie son enlaces de afiliado — si haces clic y te registras en un servicio recomendado (por ejemplo, proveedores de hosting), Toolhub puede ganar una comisión. El precio que pagas no cambia. Los enlaces de afiliado llevan la marca <code>rel="sponsored"</code>. Lista completa en <a href="/es/affiliate-disclosure/">divulgación de afiliados</a>.</p>

<h2>Tus derechos</h2>
<p>Bajo el RGPD / UK GDPR / CCPA / la ley eslovaca de protección de datos, puedes pedir acceso a o borrado de cualquier dato personal que tengamos. No tenemos ninguno — no hay backend, ni cuentas, ni base de datos de usuarios. Plausible guarda solo datos de visita agregados. Los datos publicitarios de Google se gestionan por sus propios canales.</p>

<h2>Contacto</h2>
<p>¿Dudas sobre esta política? Escríbenos desde la <a href="/es/contact/">página de contacto</a> o abre una issue en <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "fr": {
                "title": "Politique de confidentialité",
                "h1": "Politique de confidentialité",
                "description": "Politique de confidentialité de Toolhub : les outils tournent entièrement dans le navigateur, sans inscription, sans compte, aucune donnée d'outil ne sort de ton appareil. Plausible pour la mesure agrégée, AdSense uniquement avec consentement explicite.",
                "body": f"""
<p><strong>Dernière mise à jour :</strong> {LAST_UPDATED}</p>

<h2>La version courte</h2>
<p>Les outils tournent entièrement dans ton navigateur — rien de ce que tu y tapes n'est envoyé quelque part. On mesure des visites agrégées et anonymes avec <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (sans cookies). Si tu choisis d'accepter, on peut aussi afficher des pubs display via Google AdSense, qui utilise des cookies. Tu peux refuser les pubs au bandeau de consentement ; le reste du site fonctionne à l'identique.</p>

<h2>Ce qu'on collecte</h2>
<ul>
<li><strong>Données saisies dans les outils :</strong> rien. Tout ce que tu colles dans un outil reste dans ton navigateur. Aucun outil n'envoie de données à un serveur.</li>
<li><strong>Analytique de visite :</strong> Plausible compte les pages vues, le referrer, le pays et le type d'appareil — anonymement, en agrégat, sans cookies. La <a href="https://plausible.io/data-policy" rel="noopener">politique de données de Plausible</a> détaille ce qu'ils collectent et ce qu'ils ne collectent pas.</li>
<li><strong>Si tu acceptes les pubs :</strong> Google AdSense pose des cookies et peut les utiliser pour personnaliser les pubs. Les pratiques de Google sont régies par la <a href="https://policies.google.com/technologies/ads" rel="noopener">politique de confidentialité publicitaire de Google</a>.</li>
<li><strong>Si tu refuses les pubs :</strong> aucun script publicitaire n'est chargé, aucun cookie publicitaire posé, les emplacements pubs disparaissent de la page.</li>
</ul>

<h2>Cookies</h2>
<p>Le site lui-même utilise une entrée localStorage (<code>toolhub:consent</code>) pour retenir ton choix de consentement pub, et une entrée <code>theme</code> pour ta préférence sombre/claire. Ni l'une ni l'autre ne sort de ton navigateur.</p>
<p>Plausible n'utilise pas de cookies. Google AdSense utilise des cookies <em>uniquement si</em> tu les acceptes — tu peux changer ton choix à tout moment via le lien de consentement dans le pied de page.</p>

<h2>Services tiers</h2>
<ul>
<li><strong>Plausible Analytics</strong> — respectueux de la vie privée, conforme RGPD, hébergé dans l'UE. Aucune donnée personnelle collectée.</li>
<li><strong>Google AdSense</strong> — uniquement avec consentement explicite. Charge <code>pagead2.googlesyndication.com</code> et peut poser des cookies publicitaires.</li>
<li><strong>GitHub Pages</strong> — hébergeur du site. GitHub conserve les logs serveur standard (IP, horodatage, URL) selon <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">sa déclaration de confidentialité</a>.</li>
<li><strong>Outil YouTube Thumbnail</strong> — quand tu utilises spécifiquement cet outil, ton navigateur télécharge l'image directement depuis <code>i.ytimg.com</code> (le CDN de YouTube). Pas d'authentification, pas d'upload. Détails sur <a href="/fr/how-we-handle-your-data/">traitement des données</a>.</li>
</ul>

<h2>Liens d'affiliation</h2>
<p>Certains liens du pied de page sont des liens d'affiliation — si tu cliques et t'inscris à un service recommandé (par exemple un hébergeur), Toolhub peut toucher une commission. Le prix que tu paies est inchangé. Les liens d'affiliation portent la marque <code>rel="sponsored"</code>. Liste complète sur <a href="/fr/affiliate-disclosure/">divulgation des affiliés</a>.</p>

<h2>Tes droits</h2>
<p>Au titre du RGPD / UK GDPR / CCPA / de la loi slovaque sur la protection des données, tu peux demander l'accès à ou la suppression de toute donnée personnelle qu'on détiendrait. On n'en détient aucune — il n'y a pas de backend, pas de comptes, pas de base utilisateurs. Plausible ne stocke que des données de visite agrégées. Les données publicitaires de Google relèvent de leurs propres canaux de demande.</p>

<h2>Contact</h2>
<p>Des questions sur cette politique ? Écris depuis la <a href="/fr/contact/">page de contact</a> ou ouvre une issue sur <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "it": {
                "title": "Informativa sulla privacy",
                "h1": "Informativa sulla privacy",
                "description": "Informativa sulla privacy di Toolhub: gli strumenti girano interamente nel browser, niente registrazione, niente account, nessun dato degli strumenti lascia il tuo dispositivo. Plausible per la misurazione aggregata, AdSense solo con consenso esplicito.",
                "body": f"""
<p><strong>Ultimo aggiornamento:</strong> {LAST_UPDATED}</p>

<h2>La versione breve</h2>
<p>Gli strumenti girano interamente nel tuo browser — niente di quello che ci scrivi viene mandato altrove. Misuriamo visite aggregate e anonime con <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (senza cookie). Se scegli di accettare, possiamo anche mostrare annunci display via Google AdSense, che usa cookie. Puoi rifiutare gli annunci nel banner di consenso; il resto del sito funziona identico.</p>

<h2>Cosa raccogliamo</h2>
<ul>
<li><strong>Input agli strumenti:</strong> nulla. Tutto ciò che incolli in uno strumento resta nel tuo browser. Nessuno strumento manda dati a un server.</li>
<li><strong>Analitica di visita:</strong> Plausible conta visualizzazioni di pagina, referrer, paese e tipo di dispositivo — in modo anonimo e aggregato, senza cookie. La <a href="https://plausible.io/data-policy" rel="noopener">data policy di Plausible</a> copre cosa raccolgono e cosa no.</li>
<li><strong>Se accetti gli annunci:</strong> Google AdSense imposta cookie e può usarli per personalizzare gli annunci. Le pratiche di Google sono regolate dalla <a href="https://policies.google.com/technologies/ads" rel="noopener">privacy policy pubblicitaria di Google</a>.</li>
<li><strong>Se rifiuti gli annunci:</strong> nessuno script pubblicitario viene caricato, nessun cookie pubblicitario impostato, gli slot pubblicitari spariscono dalla pagina.</li>
</ul>

<h2>Cookie</h2>
<p>Il sito stesso usa una voce di localStorage (<code>toolhub:consent</code>) per ricordare la tua scelta sugli annunci, e una voce <code>theme</code> per la preferenza chiaro/scuro. Nessuna delle due lascia il tuo browser.</p>
<p>Plausible non usa cookie. Google AdSense usa cookie <em>solo se</em> li accetti — puoi cambiare scelta in qualsiasi momento dal link consenso nel footer.</p>

<h2>Servizi di terze parti</h2>
<ul>
<li><strong>Plausible Analytics</strong> — rispettoso della privacy, conforme GDPR, ospitato in UE. Nessun dato personale raccolto.</li>
<li><strong>Google AdSense</strong> — solo con consenso esplicito. Carica <code>pagead2.googlesyndication.com</code> e può impostare cookie pubblicitari.</li>
<li><strong>GitHub Pages</strong> — host del sito. GitHub conserva i log server standard (IP, timestamp, URL) secondo la <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">propria informativa sulla privacy</a>.</li>
<li><strong>Strumento YouTube Thumbnail</strong> — quando usi specificamente questo strumento, il tuo browser scarica l'immagine direttamente da <code>i.ytimg.com</code> (la CDN di YouTube). Niente autenticazione, niente upload. Dettagli in <a href="/it/how-we-handle-your-data/">trattamento dei dati</a>.</li>
</ul>

<h2>Link affiliati</h2>
<p>Alcuni link nel footer sono link affiliati — se ci clicchi e ti registri a un servizio consigliato (per es. provider di hosting), Toolhub può guadagnare una commissione. Il prezzo che paghi non cambia. I link affiliati sono marcati con <code>rel="sponsored"</code>. Elenco completo su <a href="/it/affiliate-disclosure/">divulgazione affiliati</a>.</p>

<h2>I tuoi diritti</h2>
<p>Ai sensi di GDPR / UK GDPR / CCPA / legge slovacca sulla protezione dei dati, puoi richiedere accesso o cancellazione di qualunque dato personale che custodiamo. Non ne custodiamo — non c'è backend, né account, né database utenti. Plausible conserva solo dati di visita aggregati. I dati pubblicitari di Google sono regolati dai loro canali di richiesta.</p>

<h2>Contatti</h2>
<p>Domande su questa policy? Scrivi dalla <a href="/it/contact/">pagina di contatto</a> o apri una issue su <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "pt": {
                "title": "Política de privacidade",
                "h1": "Política de privacidade",
                "description": "Política de privacidade do Toolhub: as ferramentas rodam inteiramente no navegador, sem cadastro, sem conta, nenhum dado de ferramenta sai do seu dispositivo. Plausible para métricas agregadas, AdSense só com consentimento explícito.",
                "body": f"""
<p><strong>Última atualização:</strong> {LAST_UPDATED}</p>

<h2>A versão curta</h2>
<p>As ferramentas rodam inteiramente no seu navegador — nada do que você digita nelas é enviado pra lugar nenhum. Medimos visitas agregadas e anônimas com <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (sem cookies). Se você optar por aceitar, também podemos exibir anúncios de display via Google AdSense, que usa cookies. Você pode recusar anúncios no banner de consentimento; o resto do site funciona igual.</p>

<h2>O que coletamos</h2>
<ul>
<li><strong>Entradas das ferramentas:</strong> nada. Tudo que você cola numa ferramenta fica no seu navegador. Nenhuma ferramenta manda dados pra um servidor.</li>
<li><strong>Analytics de visita:</strong> o Plausible conta page views, referrer, país e tipo de dispositivo — anonimamente, agregado, sem cookies. A <a href="https://plausible.io/data-policy" rel="noopener">política de dados do Plausible</a> cobre o que coletam e o que não coletam.</li>
<li><strong>Se você aceitar anúncios:</strong> o Google AdSense define cookies e pode usá-los pra personalizar anúncios. As práticas do Google são regidas pela <a href="https://policies.google.com/technologies/ads" rel="noopener">política de privacidade publicitária do Google</a>.</li>
<li><strong>Se você recusar anúncios:</strong> nenhum script de publicidade é carregado, nenhum cookie de publicidade é definido, os espaços de anúncio somem da página.</li>
</ul>

<h2>Cookies</h2>
<p>O site em si usa uma entrada de localStorage (<code>toolhub:consent</code>) pra lembrar sua decisão sobre anúncios, mais uma entrada <code>theme</code> pra preferência claro/escuro. Nenhuma das duas sai do seu navegador.</p>
<p>O Plausible não usa cookies. O Google AdSense usa cookies <em>só se</em> você aceitar — você pode mudar sua decisão a qualquer momento pelo link de consentimento no rodapé.</p>

<h2>Serviços de terceiros</h2>
<ul>
<li><strong>Plausible Analytics</strong> — amigável à privacidade, em conformidade com o GDPR, hospedado na UE. Nenhum dado pessoal coletado.</li>
<li><strong>Google AdSense</strong> — só com consentimento explícito. Carrega <code>pagead2.googlesyndication.com</code> e pode definir cookies publicitários.</li>
<li><strong>GitHub Pages</strong> — host do site. O GitHub mantém logs de servidor padrão (IP, timestamp, URL) conforme <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">a declaração de privacidade deles</a>.</li>
<li><strong>Ferramenta YouTube Thumbnail</strong> — quando você usa especificamente essa ferramenta, seu navegador baixa a imagem direto de <code>i.ytimg.com</code> (a CDN do YouTube). Sem autenticação, sem upload. Detalhes em <a href="/pt/how-we-handle-your-data/">tratamento de dados</a>.</li>
</ul>

<h2>Links de afiliado</h2>
<p>Alguns links no rodapé são links de afiliado — se você clica e se cadastra num serviço recomendado (por exemplo, provedores de hospedagem), o Toolhub pode ganhar uma comissão. O preço que você paga não muda. Links de afiliado vêm marcados com <code>rel="sponsored"</code>. Lista completa em <a href="/pt/affiliate-disclosure/">divulgação de afiliados</a>.</p>

<h2>Seus direitos</h2>
<p>Sob GDPR / UK GDPR / CCPA / lei eslovaca de proteção de dados, você pode pedir acesso a ou exclusão de qualquer dado pessoal que tenhamos. Não temos nenhum — não tem backend, não tem conta, não tem banco de usuários. O Plausible guarda só dados de visita agregados. Os dados publicitários do Google são geridos pelos canais próprios deles.</p>

<h2>Contato</h2>
<p>Dúvidas sobre essa política? Fala com a gente pela <a href="/pt/contact/">página de contato</a> ou abra uma issue em <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "pl": {
                "title": "Polityka prywatności",
                "h1": "Polityka prywatności",
                "description": "Polityka prywatności Toolhub: narzędzia działają w całości w przeglądarce, bez rejestracji, bez kont, żadne dane z narzędzi nie opuszczają twojego urządzenia. Plausible do zagregowanej statystyki, AdSense tylko za wyraźną zgodą.",
                "body": f"""
<p><strong>Ostatnia aktualizacja:</strong> {LAST_UPDATED}</p>

<h2>Wersja skrócona</h2>
<p>Narzędzia działają w całości w twojej przeglądarce — nic, co w nie wpiszesz, nie jest nigdzie wysyłane. Mierzymy zagregowane, anonimowe odwiedziny przy pomocy <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (bez cookies). Jeśli wyrazisz zgodę, możemy też pokazywać reklamy display przez Google AdSense, który używa cookies. Reklamy możesz odrzucić w bannerze zgody; reszta strony działa tak samo.</p>

<h2>Co zbieramy</h2>
<ul>
<li><strong>Dane wpisywane w narzędzia:</strong> nic. Wszystko, co wkleisz do narzędzia, zostaje w twojej przeglądarce. Żadne narzędzie nie wysyła danych na serwer.</li>
<li><strong>Statystyki odwiedzin:</strong> Plausible liczy odsłony, referrer, kraj i typ urządzenia — anonimowo, w agregacie, bez cookies. <a href="https://plausible.io/data-policy" rel="noopener">Polityka danych Plausible</a> opisuje, co zbierają, a czego nie.</li>
<li><strong>Jeśli zaakceptujesz reklamy:</strong> Google AdSense ustawia cookies i może ich używać do personalizacji. Praktyki Google'a reguluje <a href="https://policies.google.com/technologies/ads" rel="noopener">polityka prywatności reklamowej Google'a</a>.</li>
<li><strong>Jeśli odrzucisz reklamy:</strong> żadne skrypty reklamowe nie są ładowane, żadne cookies reklamowe nie są ustawiane, slot reklamowy znika ze strony.</li>
</ul>

<h2>Cookies</h2>
<p>Sama strona używa jednego wpisu w localStorage (<code>toolhub:consent</code>), żeby zapamiętać twoją decyzję o reklamach, plus wpisu <code>theme</code> dla preferencji jasny/ciemny. Żaden z nich nie opuszcza twojej przeglądarki.</p>
<p>Plausible nie używa cookies. Google AdSense używa cookies <em>tylko jeśli</em> się zgodzisz — decyzję możesz zmienić w dowolnym momencie linkiem zgody w stopce.</p>

<h2>Usługi stron trzecich</h2>
<ul>
<li><strong>Plausible Analytics</strong> — przyjazne prywatności, zgodne z RODO, hostowane w UE. Brak danych osobowych.</li>
<li><strong>Google AdSense</strong> — wyłącznie za wyraźną zgodą. Ładuje <code>pagead2.googlesyndication.com</code> i może ustawiać cookies reklamowe.</li>
<li><strong>GitHub Pages</strong> — host strony. GitHub trzyma standardowe logi serwera (IP, znacznik czasu, URL) zgodnie z <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">ich oświadczeniem o prywatności</a>.</li>
<li><strong>Narzędzie YouTube Thumbnail</strong> — kiedy używasz konkretnie tego narzędzia, twoja przeglądarka pobiera obraz bezpośrednio z <code>i.ytimg.com</code> (CDN YouTube'a). Bez uwierzytelnienia, bez uploadu. Szczegóły w <a href="/pl/how-we-handle-your-data/">obsługa danych</a>.</li>
</ul>

<h2>Linki partnerskie (affiliate)</h2>
<p>Niektóre linki w stopce to linki partnerskie — jeśli klikniesz i zarejestrujesz się w polecanym serwisie (np. dostawca hostingu), Toolhub może dostać prowizję. Cena, którą płacisz, się nie zmienia. Linki partnerskie są oznaczone <code>rel="sponsored"</code>. Pełna lista w <a href="/pl/affiliate-disclosure/">ujawnienie partnerów</a>.</p>

<h2>Twoje prawa</h2>
<p>Zgodnie z RODO / UK GDPR / CCPA / słowacką ustawą o ochronie danych możesz zażądać dostępu do swoich danych osobowych albo ich usunięcia. Żadnych nie przechowujemy — nie ma backendu, kont ani bazy użytkowników. Plausible przechowuje tylko zagregowane dane o odwiedzinach. Dane reklamowe Google'a obsługuje on we własnych kanałach.</p>

<h2>Kontakt</h2>
<p>Pytania o tę politykę? Pisz przez <a href="/pl/contact/">stronę kontaktową</a> albo otwórz issue na <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "ja": {
                "title": "プライバシーポリシー",
                "h1": "プライバシーポリシー",
                "description": "Toolhub のプライバシーポリシー：ツールはすべてブラウザ内で動作し、登録もアカウントも不要、ツールに入力したデータは端末から出ません。集計用に Plausible、AdSense は明示的な同意がある場合のみ。",
                "body": f"""
<p><strong>最終更新:</strong> {LAST_UPDATED}</p>

<h2>要約</h2>
<p>ツールはすべてあなたのブラウザ内で動作します — そこに入力した内容はどこにも送信されません。集計された匿名のアクセス情報は <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a>（クッキーなし）で計測しています。同意していただいた場合のみ、Google AdSense でディスプレイ広告も配信し、こちらはクッキーを使用します。同意バナーで広告を拒否することもでき、サイトの他の機能はどちらでも同じように動作します。</p>

<h2>収集する情報</h2>
<ul>
<li><strong>ツールへの入力内容:</strong> 一切収集しません。ツールに貼り付けた内容はすべてブラウザ内に留まります。どのツールもサーバーへデータを送りません。</li>
<li><strong>アクセス解析:</strong> Plausible はページビュー、リファラ、国、デバイス種別を匿名・集計・クッキーなしで計測します。具体的に何を収集し何を収集しないかは <a href="https://plausible.io/data-policy" rel="noopener">Plausible のデータポリシー</a> をご覧ください。</li>
<li><strong>広告を許可した場合:</strong> Google AdSense はクッキーを設定し、広告のパーソナライズに使うことがあります。Google の取り扱いについては <a href="https://policies.google.com/technologies/ads" rel="noopener">Google 広告プライバシーポリシー</a> に従います。</li>
<li><strong>広告を拒否した場合:</strong> 広告スクリプトは読み込まれず、広告クッキーも設定されず、広告枠はページから削除されます。</li>
</ul>

<h2>クッキー</h2>
<p>サイト自体は、広告同意の選択を覚えるための localStorage エントリ (<code>toolhub:consent</code>) と、ダーク/ライトの好みのための <code>theme</code> エントリの 2 つを使っています。どちらもあなたのブラウザから出ません。</p>
<p>Plausible はクッキーを使いません。Google AdSense は、<em>同意していただいた場合のみ</em>クッキーを使用します — フッターの同意リンクからいつでも選択を変更できます。</p>

<h2>サードパーティサービス</h2>
<ul>
<li><strong>Plausible Analytics</strong> — プライバシー重視、GDPR 準拠、EU ホスティング。個人データは収集しません。</li>
<li><strong>Google AdSense</strong> — 明示的な同意がある場合のみ。<code>pagead2.googlesyndication.com</code> を読み込み、広告クッキーを設定する場合があります。</li>
<li><strong>GitHub Pages</strong> — サイトのホスト。標準的なサーバーログ（IP、タイムスタンプ、URL）は <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">GitHub のプライバシーステートメント</a> に従い GitHub が保持します。</li>
<li><strong>YouTube Thumbnail ツール</strong> — このツールを使うときに限り、ブラウザが <code>i.ytimg.com</code>（YouTube の CDN）から画像を直接取得します。認証もアップロードもありません。詳細は <a href="/ja/how-we-handle-your-data/">データの取り扱い</a> をご覧ください。</li>
</ul>

<h2>アフィリエイトリンク</h2>
<p>フッターのいくつかのリンクはアフィリエイトリンクです — そこから飛んで推奨するサービス（例: ホスティングプロバイダ）に登録していただくと、Toolhub に紹介料が入ることがあります。あなたが支払う価格は変わりません。アフィリエイトリンクには <code>rel="sponsored"</code> を付けています。完全な一覧は <a href="/ja/affiliate-disclosure/">アフィリエイト開示</a> にあります。</p>

<h2>あなたの権利</h2>
<p>GDPR / UK GDPR / CCPA / スロバキア個人情報保護法に基づき、当方が保持する個人データへのアクセスや削除を請求できます — ただし当方は何も保持していません。バックエンドもアカウントもユーザーデータベースもありません。Plausible は集計されたアクセス情報のみを保持しています。Google の広告データは Google 自身のリクエスト経路で扱われます。</p>

<h2>お問い合わせ</h2>
<p>本ポリシーについてのご質問は <a href="/ja/contact/">お問い合わせページ</a> から、または <a href="{REPO_URL}">{REPO_URL}</a> で Issue を立ててください。</p>
""".strip(),
            },
            "nl": {
                "title": "Privacybeleid",
                "h1": "Privacybeleid",
                "description": "Toolhub-privacybeleid: tools draaien volledig in je browser, geen registratie, geen accounts, geen tool-data verlaat je apparaat. Plausible voor geaggregeerde statistiek, AdSense alleen met expliciete toestemming.",
                "body": f"""
<p><strong>Laatst bijgewerkt:</strong> {LAST_UPDATED}</p>

<h2>De korte versie</h2>
<p>Tools draaien volledig in je browser — niets wat je erin typt wordt ergens heen gestuurd. We meten geaggregeerde, anonieme bezoeken met <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (zonder cookies). Als je daarvoor kiest, kunnen we ook display-advertenties tonen via Google AdSense, dat wel cookies gebruikt. Advertenties kun je weigeren in de consent-banner; de rest van de site werkt hetzelfde.</p>

<h2>Wat we verzamelen</h2>
<ul>
<li><strong>Tool-invoer:</strong> niets. Alles wat je in een tool plakt, blijft in je browser. Geen enkele tool stuurt data naar een server.</li>
<li><strong>Bezoekstatistieken:</strong> Plausible telt paginaweergaves, referrer, land en apparaattype — anoniem, geaggregeerd, zonder cookies. Het <a href="https://plausible.io/data-policy" rel="noopener">databeleid van Plausible</a> beschrijft wat ze wel en niet verzamelen.</li>
<li><strong>Als je advertenties accepteert:</strong> Google AdSense plaatst cookies en kan deze gebruiken om advertenties te personaliseren. Google's praktijken vallen onder <a href="https://policies.google.com/technologies/ads" rel="noopener">Google's privacybeleid voor advertenties</a>.</li>
<li><strong>Als je advertenties weigert:</strong> er worden geen advertentiescripts geladen, geen advertentiecookies geplaatst, en advertentieblokken verdwijnen uit de pagina.</li>
</ul>

<h2>Cookies</h2>
<p>De site zelf gebruikt één localStorage-vermelding (<code>toolhub:consent</code>) om je advertentiekeuze te onthouden, plus een <code>theme</code>-vermelding voor je donker/licht-voorkeur. Geen van beide verlaat je browser.</p>
<p>Plausible gebruikt geen cookies. Google AdSense gebruikt cookies <em>alleen als</em> je ze accepteert — je kunt je keuze altijd wijzigen via de consent-link in de footer.</p>

<h2>Externe diensten</h2>
<ul>
<li><strong>Plausible Analytics</strong> — privacyvriendelijk, AVG-conform, EU-gehost. Geen persoonsgegevens.</li>
<li><strong>Google AdSense</strong> — alleen met expliciete toestemming. Laadt <code>pagead2.googlesyndication.com</code> en kan advertentiecookies plaatsen.</li>
<li><strong>GitHub Pages</strong> — site-host. GitHub bewaart standaard serverlogs (IP, timestamp, URL) volgens <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">hun privacyverklaring</a>.</li>
<li><strong>YouTube Thumbnail tool</strong> — als je specifiek deze tool gebruikt, haalt je browser de afbeelding rechtstreeks op vanaf <code>i.ytimg.com</code> (de CDN van YouTube). Geen authenticatie, geen upload. Details op <a href="/nl/how-we-handle-your-data/">dataverwerking</a>.</li>
</ul>

<h2>Affiliate-links</h2>
<p>Sommige links in de footer zijn affiliate-links — als je doorklikt en je aanmeldt bij een aanbevolen dienst (bijvoorbeeld hostingproviders), kan Toolhub een commissie verdienen. De prijs die jij betaalt verandert niet. Affiliate-links zijn gemarkeerd met <code>rel="sponsored"</code>. Volledige lijst op <a href="/nl/affiliate-disclosure/">affiliate-disclosure</a>.</p>

<h2>Jouw rechten</h2>
<p>Onder AVG / UK GDPR / CCPA / de Slowaakse privacywet kun je inzage of verwijdering van persoonsgegevens vragen die wij over je bewaren. Wij bewaren niets — er is geen backend, geen account, geen gebruikersdatabase. Plausible bewaart alleen geaggregeerde bezoekdata. Google's advertentiedata loopt via hun eigen verzoekkanalen.</p>

<h2>Contact</h2>
<p>Vragen over dit beleid? Meld je via de <a href="/nl/contact/">contactpagina</a> of open een issue op <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
        },
    },

    "how-we-handle-your-data": {
        "slug": "how-we-handle-your-data",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "How we handle your data",
                "h1": "How we handle your data",
                "description": "Plain-language disclosure of exactly how Toolhub handles your data. Tools run in your browser, nothing is stored, three named exceptions are listed explicitly.",
                "body": f"""
<p><strong>Last updated:</strong> {LAST_UPDATED}</p>
<p>This page is the plain-language version. It complements the <a href="/privacy/">privacy policy</a>; if they appear to disagree on a point, this page is the more specific one and should be treated as authoritative.</p>

<h2>Where data goes</h2>
<p>Tools on Toolhub run in your browser. Anything you paste, type, or upload into a tool stays on your device — we do not have a server-side tool runner, and there is no upload endpoint behind any of the tools.</p>
<p>There are exactly three named exceptions to "no data leaves your device":</p>
<ol>
<li><strong>YouTube Thumbnail tool</strong> — when you submit a YouTube URL, your browser fetches the thumbnail directly from <code>i.ytimg.com</code> (YouTube's public image CDN). No authentication, no upload, no API key. The video ID in the URL is the only thing YouTube sees, and only because your browser fetched it.</li>
<li><strong>AdSense (only if enabled and consented)</strong> — Google's display-ad system. When you grant ad consent, Google can see your IP address and may set cookies, governed by Google's policy. When you decline (the default), AdSense is not loaded at all.</li>
<li><strong>Plausible analytics</strong> — counts page visits, referrer, country and device class. No cookies, no fingerprinting, aggregate statistics only. Plausible's servers are EU-hosted.</li>
</ol>

<h2>What we store</h2>
<p>Nothing about you. No accounts, no user IDs, no email, no profile. We do not store the content you put into tools.</p>
<p>Your browser stores two small localStorage entries on your device only — both readable and clearable from your browser's developer tools:</p>
<ul>
<li><code>theme</code> — "light" or "dark", roughly one byte of preference.</li>
<li><code>toolhub:consent</code> — your ad consent decision (yes/no/unset). Used to avoid asking you again.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA and the Slovak DPA</h2>
<p>Toolhub processes minimal data:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (EU-hosted) gives a compliant analytics baseline. When AdSense is active, Google operates its own consent layer under TCF v2.</li>
<li><strong>California (CCPA):</strong> we do not sell personal information. We do not have personal information to sell.</li>
<li><strong>Slovakia (Slovak Data Protection Authority):</strong> Toolhub's maintainer is based in Slovakia. The Slovak DPA's rules apply to any processing that does occur — which is essentially limited to Plausible's aggregate metrics and (when enabled) AdSense's own consent-managed flow.</li>
</ul>
<p>Rights to access or delete personal data effectively do not apply because no personal data is stored to access or delete. If you have specific questions, contact us via the <a href="/contact/">contact page</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> no cookies, ever.</li>
<li><strong>Theme preference:</strong> one localStorage entry, not a cookie. Stays on your device. Not transmitted with HTTP requests.</li>
<li><strong>AdSense (when active):</strong> Google sets its own third-party advertising cookies. The consent banner appears before any AdSense script is loaded, and AdSense is not loaded at all if you decline.</li>
</ul>

<h2>Children</h2>
<p>Toolhub is school-friendly (see <a href="/for-schools/">Toolhub for schools</a>). There is no behavioral tracking and no targeted advertising. Under-13 use is acceptable within the existing AdSense terms applied per region — meaning if you are in a region where AdSense restricts ads to children, those restrictions are honored by Google's own systems.</p>

<h2>Downloadable PDF</h2>
<p>A PDF version of this page is available for offline reference or for printing as part of a school's IT documentation:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>The PDF is English only at this stage; per-language PDFs are not in scope for the current release.</p>

<h2>Questions</h2>
<p>If anything here is unclear, please open an issue at <a href="{REPO_URL}">{REPO_URL}</a> or use the <a href="/contact/">contact page</a>. Clarifying questions are a useful way to make this page better for the next reader.</p>
""".strip(),
            },
            "de": {
                "title": "Wie wir mit deinen Daten umgehen",
                "h1": "Wie wir mit deinen Daten umgehen",
                "description": "Verständliche Offenlegung, wie Toolhub konkret mit deinen Daten umgeht. Tools laufen im Browser, nichts wird gespeichert, drei explizit benannte Ausnahmen.",
                "body": f"""
<p><strong>Zuletzt aktualisiert:</strong> {LAST_UPDATED}</p>
<p>Diese Seite ist die Klartext-Version. Sie ergänzt die <a href="/de/privacy/">Datenschutzerklärung</a>; wenn beide an einer Stelle widersprüchlich wirken, ist diese Seite die spezifischere und gilt vorrangig.</p>

<h2>Wo die Daten landen</h2>
<p>Tools auf Toolhub laufen in deinem Browser. Was du in ein Tool einfügst, eintippst oder hochlädst, bleibt auf deinem Gerät — wir haben keine serverseitige Tool-Ausführung, und hinter keinem Tool steht ein Upload-Endpunkt.</p>
<p>Es gibt genau drei namentlich genannte Ausnahmen zu „keine Daten verlassen dein Gerät":</p>
<ol>
<li><strong>YouTube-Thumbnail-Tool</strong> — wenn du eine YouTube-URL absendest, lädt dein Browser das Thumbnail direkt von <code>i.ytimg.com</code> (YouTubes öffentlicher Bild-CDN). Keine Authentifizierung, kein Upload, kein API-Key. YouTube sieht ausschließlich die Video-ID aus der URL, und das nur, weil dein Browser sie abruft.</li>
<li><strong>AdSense (nur wenn aktiviert und zugestimmt)</strong> — Googles Display-Ad-System. Wenn du Werbung zustimmst, kann Google deine IP-Adresse sehen und Cookies setzen, geregelt durch Googles Richtlinien. Wenn du ablehnst (Standard), wird AdSense gar nicht geladen.</li>
<li><strong>Plausible Analytics</strong> — zählt Besuche, Referrer, Land und Geräteklasse. Keine Cookies, kein Fingerprinting, ausschließlich aggregierte Statistik. Plausibles Server stehen in der EU.</li>
</ol>

<h2>Was wir speichern</h2>
<p>Nichts über dich. Keine Konten, keine Nutzer-IDs, keine E-Mail, kein Profil. Wir speichern nicht den Inhalt, den du in die Tools eingibst.</p>
<p>Dein Browser speichert auf deinem Gerät zwei kleine localStorage-Einträge — beide kannst du in den Browser-Entwicklertools sehen und löschen:</p>
<ul>
<li><code>theme</code> — „light" oder „dark", ungefähr ein Byte Präferenz.</li>
<li><code>toolhub:consent</code> — deine Entscheidung zur Werbung (ja/nein/nicht gesetzt). Damit wir dich nicht nochmal fragen.</li>
</ul>

<h2>DSGVO, UK GDPR, CCPA und slowakisches Datenschutzgesetz</h2>
<p>Toolhub verarbeitet minimale Daten:</p>
<ul>
<li><strong>EU / UK (DSGVO / UK GDPR):</strong> Plausible (EU-gehostet) liefert eine konforme Analytics-Basis. Wenn AdSense aktiv ist, betreibt Google seinen eigenen Consent-Layer unter TCF v2.</li>
<li><strong>Kalifornien (CCPA):</strong> wir verkaufen keine personenbezogenen Daten. Wir haben keine personenbezogenen Daten zum Verkaufen.</li>
<li><strong>Slowakei (Datenschutzbehörde):</strong> der Maintainer von Toolhub sitzt in der Slowakei. Die slowakischen Regeln gelten für jede Verarbeitung, die tatsächlich stattfindet — was sich im Wesentlichen auf Plausibles aggregierte Metriken und (wenn aktiv) AdSenses eigenen Consent-Flow beschränkt.</li>
</ul>
<p>Auskunfts- und Löschrechte zu personenbezogenen Daten greifen praktisch nicht, weil nichts gespeichert ist, worüber man Auskunft geben oder was man löschen könnte. Wenn du konkrete Fragen hast, melde dich über die <a href="/de/contact/">Kontaktseite</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> nie Cookies.</li>
<li><strong>Theme-Präferenz:</strong> ein localStorage-Eintrag, kein Cookie. Bleibt auf deinem Gerät. Wird nicht mit HTTP-Requests übertragen.</li>
<li><strong>AdSense (wenn aktiv):</strong> Google setzt seine eigenen Werbe-Cookies (Drittanbieter). Der Consent-Banner erscheint, bevor irgendein AdSense-Skript geladen wird, und AdSense wird gar nicht geladen, wenn du ablehnst.</li>
</ul>

<h2>Kinder</h2>
<p>Toolhub ist schultauglich (siehe <a href="/de/for-schools/">Toolhub für Schulen</a>). Es gibt kein verhaltensbasiertes Tracking und keine personalisierte Werbung. Nutzung durch Unter-13-Jährige ist im Rahmen der regionalen AdSense-Bedingungen in Ordnung — wo AdSense regional Werbung gegenüber Kindern beschränkt, halten Googles eigene Systeme diese Beschränkungen ein.</p>

<h2>PDF zum Herunterladen</h2>
<p>Eine PDF-Version dieser Seite gibt es zum Offline-Lesen oder zum Ausdrucken als Teil der IT-Dokumentation einer Schule:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>Die PDF ist derzeit nur auf Englisch verfügbar; sprachspezifische PDFs sind in diesem Release nicht enthalten.</p>

<h2>Fragen</h2>
<p>Wenn hier etwas unklar ist, öffne bitte ein Issue unter <a href="{REPO_URL}">{REPO_URL}</a> oder nutze die <a href="/de/contact/">Kontaktseite</a>. Rückfragen helfen dabei, diese Seite für die nächste Leserin besser zu machen.</p>
""".strip(),
            },
            "es": {
                "title": "Cómo tratamos tus datos",
                "h1": "Cómo tratamos tus datos",
                "description": "Explicación en lenguaje claro de cómo Toolhub trata exactamente tus datos. Las herramientas funcionan en el navegador, no se almacena nada y se nombran tres excepciones explícitas.",
                "body": f"""
<p><strong>Última actualización:</strong> {LAST_UPDATED}</p>
<p>Esta página es la versión en lenguaje claro. Complementa la <a href="/es/privacy/">política de privacidad</a>; si en algún punto parecen contradecirse, esta página es la más específica y prevalece.</p>

<h2>Adónde van los datos</h2>
<p>Las herramientas de Toolhub corren en tu navegador. Lo que pegues, escribas o subas a una herramienta se queda en tu dispositivo — no tenemos un ejecutor de herramientas en servidor, y ninguna herramienta tiene un endpoint de subida detrás.</p>
<p>Hay exactamente tres excepciones nombradas al «nada sale de tu dispositivo»:</p>
<ol>
<li><strong>Herramienta YouTube Thumbnail</strong> — cuando envías una URL de YouTube, tu navegador descarga la miniatura directamente desde <code>i.ytimg.com</code> (la CDN pública de imágenes de YouTube). Sin autenticación, sin subida, sin clave de API. YouTube solo ve el ID del vídeo de la URL, y solo porque tu navegador lo descarga.</li>
<li><strong>AdSense (solo si está activo y has dado consentimiento)</strong> — el sistema de anuncios display de Google. Si das consentimiento, Google puede ver tu dirección IP y puede poner cookies, regido por la política de Google. Si rechazas (predeterminado), AdSense ni siquiera se carga.</li>
<li><strong>Plausible Analytics</strong> — cuenta visitas a páginas, referrer, país y clase de dispositivo. Sin cookies, sin fingerprinting, solo estadísticas agregadas. Los servidores de Plausible están en la UE.</li>
</ol>

<h2>Qué almacenamos</h2>
<p>Nada sobre ti. Sin cuentas, sin IDs de usuario, sin email, sin perfil. No almacenamos el contenido que metes en las herramientas.</p>
<p>Tu navegador guarda dos pequeñas entradas en localStorage en tu propio dispositivo — ambas legibles y borrables desde las DevTools del navegador:</p>
<ul>
<li><code>theme</code> — "light" o "dark", más o menos un byte de preferencia.</li>
<li><code>toolhub:consent</code> — tu decisión sobre anuncios (sí/no/sin definir). Sirve para no volver a preguntarte.</li>
</ul>

<h2>RGPD, UK GDPR, CCPA y la AEPD eslovaca</h2>
<p>Toolhub procesa datos mínimos:</p>
<ul>
<li><strong>UE / UK (RGPD / UK GDPR):</strong> Plausible (alojado en la UE) ofrece una base de analítica conforme. Cuando AdSense está activo, Google opera su propia capa de consentimiento bajo TCF v2.</li>
<li><strong>California (CCPA):</strong> no vendemos información personal. No tenemos información personal que vender.</li>
<li><strong>Eslovaquia (autoridad eslovaca de protección de datos):</strong> el mantenedor de Toolhub está en Eslovaquia. Las normas eslovacas se aplican a cualquier tratamiento que efectivamente ocurra — limitado en esencia a las métricas agregadas de Plausible y (cuando está activo) al flujo de consentimiento del propio AdSense.</li>
</ul>
<p>Los derechos de acceso o supresión de datos personales no aplican en la práctica porque no hay datos personales almacenados que acceder o suprimir. Si tienes una pregunta concreta, escríbenos desde la <a href="/es/contact/">página de contacto</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> sin cookies, nunca.</li>
<li><strong>Preferencia de tema:</strong> una entrada en localStorage, no una cookie. Se queda en tu dispositivo. No se envía en las peticiones HTTP.</li>
<li><strong>AdSense (cuando está activo):</strong> Google pone sus propias cookies publicitarias de terceros. El banner de consentimiento aparece antes de cargar cualquier script de AdSense, y AdSense ni se carga si rechazas.</li>
</ul>

<h2>Menores</h2>
<p>Toolhub es apto para entornos escolares (ver <a href="/es/for-schools/">Toolhub para escuelas</a>). No hay seguimiento de comportamiento ni publicidad personalizada. El uso por menores de 13 años es aceptable dentro de los términos de AdSense aplicados por región — donde AdSense restringe regionalmente los anuncios a menores, esas restricciones las cumplen los sistemas del propio Google.</p>

<h2>PDF descargable</h2>
<p>Hay una versión en PDF de esta página para referencia offline o para imprimirla como parte de la documentación IT de un centro:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>De momento el PDF está solo en inglés; los PDFs por idioma quedan fuera del alcance de esta entrega.</p>

<h2>Preguntas</h2>
<p>Si algo aquí no está claro, abre una issue en <a href="{REPO_URL}">{REPO_URL}</a> o usa la <a href="/es/contact/">página de contacto</a>. Las dudas que aclaras son una forma útil de mejorar la página para la siguiente persona.</p>
""".strip(),
            },
            "fr": {
                "title": "Comment on traite tes données",
                "h1": "Comment on traite tes données",
                "description": "Présentation en langage clair de la façon dont Toolhub traite tes données. Les outils tournent dans le navigateur, rien n'est stocké, trois exceptions nommées explicitement.",
                "body": f"""
<p><strong>Dernière mise à jour :</strong> {LAST_UPDATED}</p>
<p>Cette page est la version en clair. Elle complète la <a href="/fr/privacy/">politique de confidentialité</a> ; si les deux semblent se contredire quelque part, cette page-ci est la plus spécifique et prévaut.</p>

<h2>Où vont les données</h2>
<p>Les outils de Toolhub tournent dans ton navigateur. Tout ce que tu colles, tapes ou téléverses dans un outil reste sur ton appareil — il n'y a pas d'exécuteur d'outils côté serveur, et aucun outil n'a d'endpoint d'upload derrière.</p>
<p>Il y a exactement trois exceptions nommées à « rien ne sort de ton appareil » :</p>
<ol>
<li><strong>Outil YouTube Thumbnail</strong> — quand tu soumets une URL YouTube, ton navigateur télécharge la miniature directement depuis <code>i.ytimg.com</code> (le CDN d'images public de YouTube). Pas d'authentification, pas d'upload, pas de clé API. YouTube voit seulement l'ID de la vidéo dans l'URL, et seulement parce que ton navigateur fait la requête.</li>
<li><strong>AdSense (uniquement si activé et consenti)</strong> — le système d'annonces display de Google. Quand tu donnes ton consentement, Google peut voir ton adresse IP et poser des cookies, régis par la politique de Google. Quand tu refuses (par défaut), AdSense n'est pas chargé du tout.</li>
<li><strong>Plausible Analytics</strong> — compte les visites de pages, le referrer, le pays et la classe d'appareil. Pas de cookies, pas de fingerprinting, uniquement des statistiques agrégées. Les serveurs de Plausible sont hébergés dans l'UE.</li>
</ol>

<h2>Ce qu'on stocke</h2>
<p>Rien à ton sujet. Pas de comptes, pas d'identifiants utilisateur, pas d'e-mail, pas de profil. On ne stocke pas le contenu que tu mets dans les outils.</p>
<p>Ton navigateur garde deux petites entrées localStorage sur ton appareil seulement — toutes deux lisibles et effaçables depuis les outils de développement du navigateur :</p>
<ul>
<li><code>theme</code> — « light » ou « dark », à peu près un octet de préférence.</li>
<li><code>toolhub:consent</code> — ta décision sur la pub (oui/non/non défini). Pour ne pas te redemander.</li>
</ul>

<h2>RGPD, UK GDPR, CCPA et l'autorité slovaque</h2>
<p>Toolhub traite des données minimales :</p>
<ul>
<li><strong>UE / UK (RGPD / UK GDPR) :</strong> Plausible (hébergé dans l'UE) fournit une base d'analytique conforme. Quand AdSense est actif, Google opère sa propre couche de consentement sous TCF v2.</li>
<li><strong>Californie (CCPA) :</strong> on ne vend pas d'informations personnelles. On n'a pas d'informations personnelles à vendre.</li>
<li><strong>Slovaquie (autorité slovaque de protection des données) :</strong> le mainteneur de Toolhub est basé en Slovaquie. Les règles slovaques s'appliquent à tout traitement qui a effectivement lieu — ce qui se limite essentiellement aux métriques agrégées de Plausible et (quand actif) au flux de consentement propre à AdSense.</li>
</ul>
<p>Les droits d'accès ou de suppression de données personnelles ne s'appliquent en pratique pas, parce qu'aucune donnée personnelle n'est stockée à laquelle accéder ou qu'effacer. Pour des questions précises, écris depuis la <a href="/fr/contact/">page de contact</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible :</strong> jamais de cookies.</li>
<li><strong>Préférence de thème :</strong> une entrée localStorage, pas un cookie. Reste sur ton appareil. N'est pas envoyée avec les requêtes HTTP.</li>
<li><strong>AdSense (quand actif) :</strong> Google pose ses propres cookies publicitaires tiers. La bannière de consentement apparaît avant qu'aucun script AdSense ne soit chargé, et AdSense n'est pas chargé du tout si tu refuses.</li>
</ul>

<h2>Enfants</h2>
<p>Toolhub est adapté à un usage scolaire (voir <a href="/fr/for-schools/">Toolhub pour les écoles</a>). Pas de pistage comportemental, pas de pub ciblée. L'usage par les moins de 13 ans est acceptable dans le cadre des conditions AdSense appliquées par région — là où AdSense restreint régionalement les annonces aux enfants, ces restrictions sont respectées par les systèmes de Google.</p>

<h2>PDF téléchargeable</h2>
<p>Une version PDF de cette page est disponible pour consultation hors-ligne ou pour impression dans la documentation IT d'un établissement :</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>Le PDF est uniquement en anglais à ce stade ; les PDF par langue ne sont pas dans le périmètre de cette livraison.</p>

<h2>Questions</h2>
<p>Si quelque chose n'est pas clair ici, ouvre une issue sur <a href="{REPO_URL}">{REPO_URL}</a> ou utilise la <a href="/fr/contact/">page de contact</a>. Les questions de clarification servent à améliorer la page pour la prochaine personne.</p>
""".strip(),
            },
            "it": {
                "title": "Come trattiamo i tuoi dati",
                "h1": "Come trattiamo i tuoi dati",
                "description": "Spiegazione in linguaggio semplice di come esattamente Toolhub tratta i tuoi dati. Gli strumenti girano nel browser, nulla viene memorizzato, vengono nominate tre eccezioni esplicite.",
                "body": f"""
<p><strong>Ultimo aggiornamento:</strong> {LAST_UPDATED}</p>
<p>Questa pagina è la versione in linguaggio semplice. Integra l'<a href="/it/privacy/">informativa sulla privacy</a>; se in un punto sembrano in disaccordo, questa pagina è la più specifica e prevale.</p>

<h2>Dove vanno i dati</h2>
<p>Gli strumenti di Toolhub girano nel tuo browser. Tutto ciò che incolli, digiti o carichi in uno strumento resta sul tuo dispositivo — non abbiamo un esecutore di strumenti lato server, e nessuno strumento ha dietro un endpoint di upload.</p>
<p>Ci sono esattamente tre eccezioni nominate al «nulla esce dal tuo dispositivo»:</p>
<ol>
<li><strong>Strumento YouTube Thumbnail</strong> — quando invii un URL YouTube, il tuo browser scarica la thumbnail direttamente da <code>i.ytimg.com</code> (la CDN immagini pubblica di YouTube). Nessuna autenticazione, nessun upload, nessuna chiave API. YouTube vede solo l'ID del video dall'URL, e solo perché il tuo browser l'ha richiesto.</li>
<li><strong>AdSense (solo se attivo e con consenso)</strong> — il sistema di annunci display di Google. Quando dai il consenso, Google può vedere il tuo indirizzo IP e impostare cookie, regolato dalla policy di Google. Quando rifiuti (impostazione predefinita), AdSense non viene proprio caricato.</li>
<li><strong>Plausible Analytics</strong> — conta le visite alle pagine, il referrer, il paese e la classe di dispositivo. Nessun cookie, nessun fingerprinting, solo statistiche aggregate. I server di Plausible sono ospitati in UE.</li>
</ol>

<h2>Cosa memorizziamo</h2>
<p>Nulla che ti riguardi. Nessun account, nessun ID utente, nessuna email, nessun profilo. Non memorizziamo il contenuto che metti negli strumenti.</p>
<p>Il tuo browser tiene due piccole voci di localStorage solo sul tuo dispositivo — entrambe leggibili e cancellabili dagli strumenti per sviluppatori del browser:</p>
<ul>
<li><code>theme</code> — "light" o "dark", più o meno un byte di preferenza.</li>
<li><code>toolhub:consent</code> — la tua decisione sugli annunci (sì/no/non impostata). Serve a non richiederlo di nuovo.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA e l'autorità slovacca</h2>
<p>Toolhub tratta dati minimi:</p>
<ul>
<li><strong>UE / UK (GDPR / UK GDPR):</strong> Plausible (ospitato in UE) fornisce una base analitica conforme. Quando AdSense è attivo, Google gestisce il proprio layer di consenso sotto TCF v2.</li>
<li><strong>California (CCPA):</strong> non vendiamo informazioni personali. Non abbiamo informazioni personali da vendere.</li>
<li><strong>Slovacchia (autorità slovacca per la protezione dei dati):</strong> il maintainer di Toolhub è basato in Slovacchia. Le regole slovacche si applicano a qualsiasi trattamento effettivamente in atto — limitato in pratica alle metriche aggregate di Plausible e (quando attivo) al flusso di consenso interno di AdSense.</li>
</ul>
<p>I diritti di accesso o cancellazione dei dati personali in pratica non si applicano perché non ci sono dati personali memorizzati da consultare o cancellare. Per domande specifiche, scrivici dalla <a href="/it/contact/">pagina di contatto</a>.</p>

<h2>Cookie</h2>
<ul>
<li><strong>Plausible:</strong> nessun cookie, mai.</li>
<li><strong>Preferenza tema:</strong> una voce in localStorage, non un cookie. Resta sul tuo dispositivo. Non viaggia con le richieste HTTP.</li>
<li><strong>AdSense (quando attivo):</strong> Google imposta i propri cookie pubblicitari di terze parti. Il banner di consenso compare prima che venga caricato qualunque script AdSense, e AdSense non viene caricato per nulla se rifiuti.</li>
</ul>

<h2>Minori</h2>
<p>Toolhub è adatto alla scuola (vedi <a href="/it/for-schools/">Toolhub per le scuole</a>). Niente tracciamento comportamentale, niente pubblicità mirata. L'uso da parte di minori di 13 anni è accettabile nell'ambito dei termini AdSense applicati per regione — dove AdSense limita regionalmente la pubblicità ai minori, quei limiti sono rispettati dai sistemi di Google.</p>

<h2>PDF scaricabile</h2>
<p>È disponibile una versione PDF di questa pagina per consultazione offline o per essere stampata nella documentazione IT di una scuola:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>Il PDF è al momento solo in inglese; i PDF per lingua non rientrano in questa release.</p>

<h2>Domande</h2>
<p>Se qualcosa qui non è chiaro, apri una issue su <a href="{REPO_URL}">{REPO_URL}</a> o usa la <a href="/it/contact/">pagina di contatto</a>. Le domande di chiarimento aiutano a rendere la pagina migliore per chi legge dopo.</p>
""".strip(),
            },
            "pt": {
                "title": "Como tratamos seus dados",
                "h1": "Como tratamos seus dados",
                "description": "Explicação em linguagem clara de como exatamente o Toolhub trata seus dados. As ferramentas rodam no navegador, nada é armazenado, três exceções nomeadas explicitamente.",
                "body": f"""
<p><strong>Última atualização:</strong> {LAST_UPDATED}</p>
<p>Essa página é a versão em linguagem clara. Ela complementa a <a href="/pt/privacy/">política de privacidade</a>; se em algum ponto parecerem discordar, essa página é a mais específica e prevalece.</p>

<h2>Pra onde os dados vão</h2>
<p>As ferramentas do Toolhub rodam no seu navegador. Tudo que você cola, digita ou faz upload em uma ferramenta fica no seu dispositivo — não temos executor de ferramenta no servidor, e nenhuma ferramenta tem endpoint de upload por trás.</p>
<p>Existem exatamente três exceções nomeadas pro "nada sai do seu dispositivo":</p>
<ol>
<li><strong>Ferramenta YouTube Thumbnail</strong> — quando você envia uma URL do YouTube, seu navegador baixa a thumbnail direto de <code>i.ytimg.com</code> (a CDN de imagens pública do YouTube). Sem autenticação, sem upload, sem API key. O YouTube só vê o ID do vídeo na URL, e só porque seu navegador fez a requisição.</li>
<li><strong>AdSense (só se ativo e com consentimento)</strong> — o sistema de anúncios display do Google. Quando você dá consentimento, o Google pode ver seu IP e pode definir cookies, regidos pela política dele. Quando você recusa (padrão), o AdSense nem é carregado.</li>
<li><strong>Plausible Analytics</strong> — conta visitas, referrer, país e classe de dispositivo. Sem cookies, sem fingerprinting, só estatística agregada. Os servidores do Plausible ficam na UE.</li>
</ol>

<h2>O que armazenamos</h2>
<p>Nada sobre você. Sem contas, sem IDs de usuário, sem email, sem perfil. Não armazenamos o conteúdo que você bota nas ferramentas.</p>
<p>Seu navegador guarda duas pequenas entradas de localStorage só no seu dispositivo — as duas são legíveis e apagáveis pelo DevTools do navegador:</p>
<ul>
<li><code>theme</code> — "light" ou "dark", mais ou menos um byte de preferência.</li>
<li><code>toolhub:consent</code> — sua decisão sobre anúncios (sim/não/não definida). Pra não te perguntar de novo.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA e a autoridade eslovaca</h2>
<p>O Toolhub processa dados mínimos:</p>
<ul>
<li><strong>UE / UK (GDPR / UK GDPR):</strong> o Plausible (hospedado na UE) dá uma base de analytics conforme. Quando o AdSense está ativo, o Google opera a própria camada de consentimento sob TCF v2.</li>
<li><strong>Califórnia (CCPA):</strong> não vendemos informação pessoal. Não temos informação pessoal pra vender.</li>
<li><strong>Eslováquia (autoridade eslovaca de proteção de dados):</strong> o mantenedor do Toolhub está baseado na Eslováquia. As regras eslovacas se aplicam a qualquer processamento que realmente ocorra — limitado essencialmente às métricas agregadas do Plausible e (quando ativo) ao fluxo de consentimento do próprio AdSense.</li>
</ul>
<p>Direitos de acesso ou exclusão de dados pessoais na prática não se aplicam porque não há dado pessoal armazenado a acessar ou excluir. Pra dúvidas específicas, fala com a gente pela <a href="/pt/contact/">página de contato</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> sem cookies, nunca.</li>
<li><strong>Preferência de tema:</strong> uma entrada de localStorage, não um cookie. Fica no seu dispositivo. Não vai junto com requisições HTTP.</li>
<li><strong>AdSense (quando ativo):</strong> o Google define seus próprios cookies publicitários de terceiros. O banner de consentimento aparece antes de qualquer script do AdSense ser carregado, e o AdSense nem é carregado se você recusar.</li>
</ul>

<h2>Crianças</h2>
<p>O Toolhub é adequado pra escola (veja <a href="/pt/for-schools/">Toolhub pra escolas</a>). Não tem tracking comportamental nem publicidade direcionada. O uso por menores de 13 anos é aceitável dentro dos termos do AdSense aplicados por região — onde o AdSense restringe regionalmente anúncios pra crianças, essas restrições são respeitadas pelos sistemas do próprio Google.</p>

<h2>PDF pra download</h2>
<p>Tem uma versão em PDF dessa página pra leitura offline ou pra imprimir como parte da documentação de TI de uma escola:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>O PDF tá só em inglês por enquanto; PDFs por idioma não fazem parte dessa entrega.</p>

<h2>Dúvidas</h2>
<p>Se algo aqui não está claro, abre uma issue em <a href="{REPO_URL}">{REPO_URL}</a> ou usa a <a href="/pt/contact/">página de contato</a>. Perguntas de esclarecimento ajudam a melhorar a página pra próxima pessoa.</p>
""".strip(),
            },
            "pl": {
                "title": "Jak obchodzimy się z twoimi danymi",
                "h1": "Jak obchodzimy się z twoimi danymi",
                "description": "Wyjaśnienie prostym językiem, jak dokładnie Toolhub obchodzi się z twoimi danymi. Narzędzia działają w przeglądarce, nic nie jest przechowywane, trzy wyjątki wymienione wprost.",
                "body": f"""
<p><strong>Ostatnia aktualizacja:</strong> {LAST_UPDATED}</p>
<p>To jest wersja w prostym języku. Uzupełnia <a href="/pl/privacy/">politykę prywatności</a>; jeśli gdzieś wyglądają na sprzeczne, ta strona jest bardziej szczegółowa i ma pierwszeństwo.</p>

<h2>Dokąd trafiają dane</h2>
<p>Narzędzia Toolhub działają w twojej przeglądarce. Wszystko, co wklejasz, wpisujesz lub wgrywasz do narzędzia, zostaje na twoim urządzeniu — nie mamy uruchamiania narzędzi po stronie serwera i żadne narzędzie nie ma za sobą endpointu uploadu.</p>
<p>Są dokładnie trzy nazwane wyjątki od „nic nie opuszcza twojego urządzenia":</p>
<ol>
<li><strong>Narzędzie YouTube Thumbnail</strong> — kiedy wysyłasz URL YouTube, twoja przeglądarka pobiera miniaturę bezpośrednio z <code>i.ytimg.com</code> (publiczny obrazkowy CDN YouTube'a). Bez uwierzytelnienia, bez uploadu, bez klucza API. YouTube widzi tylko ID filmu z URL-a i tylko dlatego, że twoja przeglądarka go pobrała.</li>
<li><strong>AdSense (tylko jeśli włączone i za zgodą)</strong> — system reklam display Google'a. Kiedy wyrażasz zgodę, Google może widzieć twój adres IP i może ustawiać cookies, zgodnie ze swoją polityką. Kiedy odmawiasz (domyślne), AdSense w ogóle nie jest ładowany.</li>
<li><strong>Plausible Analytics</strong> — liczy odwiedziny, referrer, kraj i klasę urządzenia. Bez cookies, bez fingerprintingu, wyłącznie zagregowane statystyki. Serwery Plausible są hostowane w UE.</li>
</ol>

<h2>Co przechowujemy</h2>
<p>Nic na twój temat. Bez kont, bez ID użytkownika, bez maila, bez profilu. Nie przechowujemy treści, którą wkładasz do narzędzi.</p>
<p>Twoja przeglądarka trzyma na twoim urządzeniu dwa małe wpisy localStorage — oba można odczytać i wyczyścić w narzędziach deweloperskich:</p>
<ul>
<li><code>theme</code> — „light" albo „dark", mniej więcej bajt preferencji.</li>
<li><code>toolhub:consent</code> — twoja decyzja o reklamach (tak/nie/niezdefiniowane). Po to, żeby nie pytać znowu.</li>
</ul>

<h2>RODO, UK GDPR, CCPA i słowacki organ ochrony danych</h2>
<p>Toolhub przetwarza dane w minimalnym zakresie:</p>
<ul>
<li><strong>UE / UK (RODO / UK GDPR):</strong> Plausible (hostowany w UE) daje zgodną podstawę analityczną. Kiedy AdSense jest aktywny, Google obsługuje własną warstwę zgody pod TCF v2.</li>
<li><strong>Kalifornia (CCPA):</strong> nie sprzedajemy danych osobowych. Nie mamy danych osobowych do sprzedania.</li>
<li><strong>Słowacja (słowacki organ ochrony danych):</strong> maintainer Toolhub jest w Słowacji. Słowackie przepisy mają zastosowanie do każdego rzeczywistego przetwarzania — co w praktyce ogranicza się do zagregowanych metryk Plausible i (kiedy aktywne) własnego flow zgody AdSense'a.</li>
</ul>
<p>Prawa dostępu lub usunięcia danych osobowych w praktyce nie mają zastosowania, bo nie ma żadnych zapisanych danych osobowych, do których można by sięgnąć czy je usunąć. W konkretnych sprawach pisz przez <a href="/pl/contact/">stronę kontaktową</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> żadnych cookies, nigdy.</li>
<li><strong>Preferencja motywu:</strong> jeden wpis w localStorage, nie cookie. Zostaje na twoim urządzeniu. Nie jest wysyłana z żądaniami HTTP.</li>
<li><strong>AdSense (gdy aktywny):</strong> Google ustawia własne, zewnętrzne cookies reklamowe. Banner zgody pojawia się przed załadowaniem jakiegokolwiek skryptu AdSense, a AdSense w ogóle nie jest ładowany, jeśli odmówisz.</li>
</ul>

<h2>Dzieci</h2>
<p>Toolhub jest przyjazny szkołom (zobacz <a href="/pl/for-schools/">Toolhub dla szkół</a>). Bez śledzenia behawioralnego i bez reklam targetowanych. Korzystanie przez dzieci poniżej 13 lat jest akceptowalne w ramach regionalnych warunków AdSense — tam, gdzie AdSense regionalnie ogranicza reklamy dla dzieci, te ograniczenia są przestrzegane przez systemy Google'a.</p>

<h2>PDF do pobrania</h2>
<p>Dostępna jest wersja PDF tej strony do offline'owego wglądu albo do druku jako część szkolnej dokumentacji IT:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF jest na razie tylko po angielsku; PDF-y per język nie są częścią tego release'u.</p>

<h2>Pytania</h2>
<p>Jeśli coś tu jest niejasne, otwórz issue na <a href="{REPO_URL}">{REPO_URL}</a> albo użyj <a href="/pl/contact/">strony kontaktowej</a>. Pytania doprecyzowujące to dobry sposób, żeby zrobić tę stronę lepszą dla kolejnej osoby.</p>
""".strip(),
            },
            "ja": {
                "title": "データの取り扱いについて",
                "h1": "データの取り扱いについて",
                "description": "Toolhub があなたのデータを具体的にどう扱うかを、平易な言葉で説明します。ツールはブラウザ内で動作し、何も保存されず、3 つの例外を明示しています。",
                "body": f"""
<p><strong>最終更新:</strong> {LAST_UPDATED}</p>
<p>このページは平易な言葉版です。<a href="/ja/privacy/">プライバシーポリシー</a> を補足するものです。両者の記述が食い違って見える箇所がある場合は、本ページの方が具体的であり、こちらが優先されます。</p>

<h2>データはどこへ行くか</h2>
<p>Toolhub のツールはあなたのブラウザ内で動作します。ツールに貼り付けた、入力した、アップロードしたものは、すべてあなたの端末内に留まります — サーバー側のツール実行環境はなく、どのツールにもアップロード用エンドポイントは付いていません。</p>
<p>「あなたの端末からデータが出ない」ことには、はっきりと名前を付けた例外が 3 つだけあります：</p>
<ol>
<li><strong>YouTube Thumbnail ツール</strong> — YouTube の URL を送信したとき、ブラウザが <code>i.ytimg.com</code>（YouTube 公開画像 CDN）から直接サムネイルを取得します。認証もアップロードも API キーも不要です。YouTube が見るのは URL に含まれる動画 ID だけで、それもあなたのブラウザが取得しに行くからにすぎません。</li>
<li><strong>AdSense（有効かつ同意がある場合のみ）</strong> — Google のディスプレイ広告システム。広告に同意していただいた場合、Google はあなたの IP アドレスを見ることがあり、Cookie を設定する場合があります。これらは Google のポリシーに従います。同意しなかった場合（既定）、AdSense は一切読み込まれません。</li>
<li><strong>Plausible Analytics</strong> — ページビュー、リファラ、国、デバイス種別を集計します。Cookie もフィンガープリントもなく、集計値のみです。Plausible のサーバーは EU 内にあります。</li>
</ol>

<h2>当方が保存するもの</h2>
<p>あなたに関するものは何も保存しません。アカウントも、ユーザー ID も、メールアドレスも、プロフィールもありません。ツールに入れた内容も保存しません。</p>
<p>ブラウザがあなたの端末内にのみ保持する localStorage エントリは 2 つあり、どちらもブラウザの開発者ツールから閲覧・削除できます：</p>
<ul>
<li><code>theme</code> — "light" または "dark"、おおよそ 1 バイトの設定。</li>
<li><code>toolhub:consent</code> — 広告同意の判断（yes / no / 未設定）。再度尋ねないために使います。</li>
</ul>

<h2>GDPR・UK GDPR・CCPA・スロバキア個人情報保護法</h2>
<p>Toolhub が取り扱うデータは最小限です：</p>
<ul>
<li><strong>EU / UK（GDPR / UK GDPR）:</strong> Plausible（EU ホスト）が適合する解析基盤を提供します。AdSense が有効な場合、Google が TCF v2 に基づく独自の同意レイヤーを運用します。</li>
<li><strong>カリフォルニア州（CCPA）:</strong> 当方は個人情報を販売しません。販売する個人情報を保有していません。</li>
<li><strong>スロバキア（スロバキア個人情報保護機関）:</strong> Toolhub のメンテナーはスロバキアに所在しています。スロバキアの規則は、実際に行われる処理に対して適用されます — 実態としては Plausible の集計メトリクスと、（有効な場合の）AdSense 自身の同意管理フローに限られます。</li>
</ul>
<p>個人データへのアクセス・削除請求権は、保持している個人データが存在しない以上、実質的に適用されません。具体的なご質問は <a href="/ja/contact/">お問い合わせページ</a> からどうぞ。</p>

<h2>Cookie</h2>
<ul>
<li><strong>Plausible:</strong> Cookie は一切使いません。</li>
<li><strong>テーマ設定:</strong> localStorage エントリ 1 件で、Cookie ではありません。あなたの端末内に留まり、HTTP リクエストには送信されません。</li>
<li><strong>AdSense（有効時）:</strong> Google が独自のサードパーティ広告 Cookie を設定します。同意バナーは AdSense のスクリプトが読み込まれる前に表示され、拒否した場合は AdSense は一切読み込まれません。</li>
</ul>

<h2>子ども</h2>
<p>Toolhub は学校での利用にも適しています（<a href="/ja/for-schools/">学校向けの Toolhub</a> をご覧ください）。行動追跡やターゲティング広告はありません。13 歳未満の利用は、地域ごとに適用される AdSense の条件の範囲内で問題ありません — AdSense が地域単位で子ども向け広告を制限している場合、その制限は Google 自身のシステムで守られます。</p>

<h2>PDF ダウンロード</h2>
<p>本ページの PDF 版があり、オフライン参照や、学校 IT 文書の一部として印刷する用途に使えます：</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>現時点では PDF は英語版のみで、各言語版 PDF は今回のリリースの対象外です。</p>

<h2>質問</h2>
<p>本ページで不明瞭な箇所があれば、<a href="{REPO_URL}">{REPO_URL}</a> で Issue を立てるか、<a href="/ja/contact/">お問い合わせページ</a> をご利用ください。質問は次に読む人にとってもこのページを良くするのに役立ちます。</p>
""".strip(),
            },
            "nl": {
                "title": "Hoe we met je gegevens omgaan",
                "h1": "Hoe we met je gegevens omgaan",
                "description": "Uitleg in gewone taal van hoe Toolhub precies met je gegevens omgaat. Tools draaien in je browser, niets wordt opgeslagen, drie uitzonderingen worden expliciet genoemd.",
                "body": f"""
<p><strong>Laatst bijgewerkt:</strong> {LAST_UPDATED}</p>
<p>Deze pagina is de versie in gewone taal. Ze vult het <a href="/nl/privacy/">privacybeleid</a> aan; als ze ergens lijken te botsen, is deze pagina de specifiekere en geldt die voor.</p>

<h2>Waar gaan de gegevens heen</h2>
<p>De tools op Toolhub draaien in je browser. Wat je in een tool plakt, typt of uploadt, blijft op je apparaat — er is geen server-side tool-uitvoerder en er zit geen upload-endpoint achter de tools.</p>
<p>Er zijn precies drie expliciet genoemde uitzonderingen op "niets verlaat je apparaat":</p>
<ol>
<li><strong>YouTube Thumbnail tool</strong> — wanneer je een YouTube-URL indient, haalt je browser de thumbnail direct op vanaf <code>i.ytimg.com</code> (YouTube's publieke CDN voor afbeeldingen). Geen authenticatie, geen upload, geen API key. YouTube ziet alleen het video-ID uit de URL, en alleen omdat je browser het opvraagt.</li>
<li><strong>AdSense (alleen als ingeschakeld en met toestemming)</strong> — Google's display-advertentiesysteem. Bij toestemming kan Google je IP-adres zien en cookies plaatsen, conform Google's beleid. Bij weigering (standaard) wordt AdSense helemaal niet geladen.</li>
<li><strong>Plausible Analytics</strong> — telt paginabezoeken, referrer, land en apparaatklasse. Geen cookies, geen fingerprinting, alleen geaggregeerde statistieken. Plausible's servers staan in de EU.</li>
</ol>

<h2>Wat we opslaan</h2>
<p>Niets over jou. Geen accounts, geen gebruikers-ID's, geen e-mail, geen profiel. We slaan de inhoud die je in tools stopt niet op.</p>
<p>Je browser bewaart twee kleine localStorage-vermeldingen alleen op je eigen apparaat — beide zijn leesbaar en wisbaar via de developer tools van je browser:</p>
<ul>
<li><code>theme</code> — "light" of "dark", ongeveer een byte voorkeur.</li>
<li><code>toolhub:consent</code> — je advertentiekeuze (ja/nee/onbepaald). Om je niet opnieuw te hoeven vragen.</li>
</ul>

<h2>AVG, UK GDPR, CCPA en de Slowaakse DPA</h2>
<p>Toolhub verwerkt minimale gegevens:</p>
<ul>
<li><strong>EU / UK (AVG / UK GDPR):</strong> Plausible (EU-gehost) levert een conforme analytics-basis. Wanneer AdSense actief is, voert Google een eigen consent-laag onder TCF v2.</li>
<li><strong>Californië (CCPA):</strong> we verkopen geen persoonsgegevens. We hebben geen persoonsgegevens te verkopen.</li>
<li><strong>Slowakije (Slowaakse autoriteit persoonsgegevens):</strong> de maintainer van Toolhub zit in Slowakije. De Slowaakse regels gelden voor elke verwerking die daadwerkelijk plaatsvindt — wat in de praktijk neerkomt op de geaggregeerde metingen van Plausible en (bij activatie) AdSense's eigen consent-flow.</li>
</ul>
<p>Rechten op inzage of verwijdering van persoonsgegevens zijn in de praktijk niet van toepassing omdat er geen persoonsgegevens zijn opgeslagen om in te zien of te verwijderen. Voor specifieke vragen, mail via de <a href="/nl/contact/">contactpagina</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> geen cookies, nooit.</li>
<li><strong>Thema-voorkeur:</strong> één localStorage-vermelding, geen cookie. Blijft op je apparaat. Wordt niet meegestuurd met HTTP-verzoeken.</li>
<li><strong>AdSense (indien actief):</strong> Google plaatst zijn eigen third-party advertentiecookies. De consent-banner verschijnt voordat een AdSense-script geladen wordt, en AdSense wordt helemaal niet geladen als je weigert.</li>
</ul>

<h2>Kinderen</h2>
<p>Toolhub is schoolvriendelijk (zie <a href="/nl/for-schools/">Toolhub voor scholen</a>). Geen gedragstracking, geen gerichte advertenties. Gebruik onder 13 jaar is acceptabel binnen de AdSense-voorwaarden per regio — waar AdSense regionaal advertenties richting kinderen beperkt, worden die beperkingen door de systemen van Google zelf nageleefd.</p>

<h2>Downloadbare PDF</h2>
<p>Er is een PDF-versie van deze pagina beschikbaar voor offline gebruik of om af te drukken als onderdeel van de IT-documentatie van een school:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>De PDF is op dit moment alleen in het Engels; per-taal PDFs vallen buiten de scope van deze release.</p>

<h2>Vragen</h2>
<p>Als iets hier onduidelijk is, open een issue op <a href="{REPO_URL}">{REPO_URL}</a> of gebruik de <a href="/nl/contact/">contactpagina</a>. Verhelderende vragen zijn een goede manier om deze pagina voor de volgende lezer beter te maken.</p>
""".strip(),
            },
        },
    },

    "affiliate-disclosure": {
        "slug": "affiliate-disclosure",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "Affiliate disclosure",
                "h1": "Affiliate disclosure",
                "description": "FTC and EU-compliant disclosure of Toolhub's affiliate relationships. The vendor pays, you pay nothing extra, and editorial coverage is not affiliate-driven.",
                "body": f"""
<p><strong>Last updated:</strong> {LAST_UPDATED}</p>

<h2>What affiliate links are</h2>
<p>An affiliate link is a regular link with a tracking code attached. If you click one and then sign up to the linked service, the service pays Toolhub a small referral commission. The price <em>you</em> pay is identical to the non-affiliate version — you are not paying for the commission, the vendor is.</p>

<h2>Where they appear on Toolhub</h2>
<p>Currently, affiliate links appear in two places:</p>
<ul>
<li>The site footer, marked with a small <code>(affiliate)</code> badge.</li>
<li>Anywhere a tool's help-block or related-tools section mentions a specific paid service we recommend — in those cases the affiliate is called out inline.</li>
</ul>
<p>Affiliate links carry <code>rel="sponsored"</code> in the HTML, which is the search-engine standard for declaring a commercial relationship.</p>

<h2>Who pays</h2>
<p>The vendor pays the commission, not you. If you ignore the affiliate link and sign up via the vendor's homepage directly, you get the same service at the same price; we just don't see a referral.</p>

<h2>FTC and EU compliance</h2>
<p>This page exists because the US Federal Trade Commission's endorsement guides and EU consumer-protection rules both require content creators to disclose when they have a financial relationship with a linked product. The disclosure has to be clear and up-front — hence a top-level page, hence linked from every page footer.</p>

<h2>Specific affiliates</h2>
<p>Toolhub's affiliate accounts are not all live at the time of writing — this is a placeholder list. Once each account is approved, the operator (JXXR1) will populate the link URLs here:</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>If/when other affiliate relationships are added, they will be listed here and the page will be redated.</p>

<h2>No paid placement</h2>
<p>Tool reviews, the order tools appear in on the homepage, and the "related tools" links on each tool are <strong>not</strong> affiliate-driven. We don't accept money to feature a tool, nor to rank one tool above another. If a paid placement ever did get added (it won't, but if), it would be labelled the same way affiliate links are: clearly, up-front, distinguishable from editorial content.</p>

<h2>Editorial independence</h2>
<p>Affiliate relationships do not influence which tools are built, how help-block copy is written, or which "related tools" appear under a given tool. The tools on Toolhub are the tools we'd build with no affiliate program at all — the program just makes a small contribution toward hosting and maintenance.</p>

<h2>Contact</h2>
<p>Questions about a specific affiliate, or want to flag something that looks like it shouldn't be here? Open an issue at <a href="{REPO_URL}">{REPO_URL}</a> or use the <a href="/contact/">contact page</a>.</p>
""".strip(),
            },
            "de": {
                "title": "Affiliate-Offenlegung",
                "h1": "Affiliate-Offenlegung",
                "description": "FTC- und EU-konforme Offenlegung der Affiliate-Beziehungen von Toolhub. Der Anbieter zahlt, dich kostet es nichts extra, und redaktionelle Inhalte sind nicht affiliategetrieben.",
                "body": f"""
<p><strong>Zuletzt aktualisiert:</strong> {LAST_UPDATED}</p>

<h2>Was Affiliate-Links sind</h2>
<p>Ein Affiliate-Link ist ein ganz normaler Link mit einem angehängten Tracking-Code. Wenn du draufklickst und dich beim verlinkten Dienst anmeldest, zahlt der Dienst Toolhub eine kleine Vermittlungsprovision. Der Preis, den <em>du</em> zahlst, ist derselbe wie ohne Affiliate-Link — du zahlst nicht die Provision, der Anbieter tut es.</p>

<h2>Wo sie auf Toolhub auftauchen</h2>
<p>Aktuell tauchen Affiliate-Links an zwei Stellen auf:</p>
<ul>
<li>Im Seiten-Footer, mit einem kleinen <code>(affiliate)</code>-Badge.</li>
<li>Überall dort, wo ein Hilfetext oder „Ähnliche Tools" einen bestimmten kostenpflichtigen Dienst empfiehlt — dort wird der Affiliate inline ausgewiesen.</li>
</ul>
<p>Affiliate-Links tragen im HTML <code>rel="sponsored"</code>, was der Suchmaschinen-Standard zur Kennzeichnung einer kommerziellen Beziehung ist.</p>

<h2>Wer zahlt</h2>
<p>Der Anbieter zahlt die Provision, nicht du. Wenn du den Affiliate-Link ignorierst und dich direkt über die Homepage des Anbieters anmeldest, bekommst du denselben Dienst zum selben Preis; wir sehen dann einfach keine Vermittlung.</p>

<h2>FTC- und EU-Konformität</h2>
<p>Diese Seite existiert, weil sowohl die Endorsement Guides der US-amerikanischen Federal Trade Commission als auch die EU-Verbraucherschutzregeln verlangen, dass Content-Ersteller offenlegen, wenn sie zu einem verlinkten Produkt eine wirtschaftliche Beziehung haben. Die Offenlegung muss klar und im Voraus erfolgen — daher eine Top-Level-Seite, daher die Verlinkung im Footer jeder Seite.</p>

<h2>Konkrete Affiliates</h2>
<p>Nicht alle Affiliate-Konten von Toolhub sind zum Zeitpunkt der Erstellung live — das hier ist eine Platzhalter-Liste. Sobald die einzelnen Konten freigegeben sind, trägt der Betreiber (JXXR1) die URLs hier ein:</p>
<ul>
<li><strong>DigitalOcean</strong> (Cloud-Hosting) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Falls weitere Affiliate-Beziehungen hinzukommen, werden sie hier gelistet und die Seite neu datiert.</p>

<h2>Keine bezahlte Platzierung</h2>
<p>Tool-Besprechungen, die Reihenfolge der Tools auf der Startseite und die „Ähnliche Tools"-Verlinkungen unter jedem Tool sind <strong>nicht</strong> affiliategetrieben. Wir nehmen kein Geld dafür, ein Tool zu featuren oder eines vor einem anderen zu platzieren. Falls jemals eine bezahlte Platzierung hinzukäme (wird es nicht, aber falls), wäre sie genauso gekennzeichnet wie Affiliate-Links: deutlich, im Voraus, klar unterscheidbar vom redaktionellen Inhalt.</p>

<h2>Redaktionelle Unabhängigkeit</h2>
<p>Affiliate-Beziehungen beeinflussen nicht, welche Tools gebaut werden, wie Hilfetexte geschrieben sind oder welche „Ähnlichen Tools" unter einem bestimmten Tool erscheinen. Die Tools auf Toolhub sind die Tools, die wir auch ohne jedes Affiliate-Programm bauen würden — das Programm trägt nur einen kleinen Teil zu Hosting und Wartung bei.</p>

<h2>Kontakt</h2>
<p>Fragen zu einem konkreten Affiliate, oder etwas, das hier nicht stehen sollte? Öffne ein Issue unter <a href="{REPO_URL}">{REPO_URL}</a> oder nutze die <a href="/de/contact/">Kontaktseite</a>.</p>
""".strip(),
            },
            "es": {
                "title": "Divulgación de afiliados",
                "h1": "Divulgación de afiliados",
                "description": "Divulgación conforme a la FTC y normas de la UE de las relaciones de afiliados de Toolhub. El proveedor paga, tú no pagas nada extra, y la cobertura editorial no depende de los afiliados.",
                "body": f"""
<p><strong>Última actualización:</strong> {LAST_UPDATED}</p>

<h2>Qué es un enlace de afiliado</h2>
<p>Un enlace de afiliado es un enlace normal con un código de seguimiento añadido. Si haces clic y luego te registras en el servicio enlazado, el servicio paga a Toolhub una pequeña comisión por la referencia. El precio que pagas <em>tú</em> es idéntico al de la versión no afiliada — tú no pagas la comisión, la paga el proveedor.</p>

<h2>Dónde aparecen en Toolhub</h2>
<p>Actualmente los enlaces de afiliado aparecen en dos sitios:</p>
<ul>
<li>En el pie de página, marcados con una pequeña insignia <code>(afiliado)</code>.</li>
<li>En cualquier sitio donde el bloque de ayuda o el apartado de "herramientas relacionadas" mencione un servicio de pago concreto que recomendemos — en esos casos el afiliado se identifica en línea.</li>
</ul>
<p>Los enlaces de afiliado llevan <code>rel="sponsored"</code> en el HTML, que es el estándar para buscadores cuando se declara una relación comercial.</p>

<h2>Quién paga</h2>
<p>El proveedor paga la comisión, no tú. Si ignoras el enlace de afiliado y te registras directamente desde la home del proveedor, obtienes el mismo servicio al mismo precio; simplemente nosotros no vemos la referencia.</p>

<h2>Cumplimiento FTC y UE</h2>
<p>Esta página existe porque tanto las guías de la Federal Trade Commission de EE. UU. como las normas de protección al consumidor de la UE exigen que los creadores de contenido divulguen si tienen una relación financiera con un producto enlazado. La divulgación tiene que ser clara y por adelantado — de ahí una página de nivel superior, de ahí el enlace desde el pie de cada página.</p>

<h2>Afiliados concretos</h2>
<p>No todas las cuentas de afiliado de Toolhub están activas en el momento de escribir esto — esta es una lista de reserva. En cuanto cada cuenta sea aprobada, el operador (JXXR1) rellenará las URL aquí:</p>
<ul>
<li><strong>DigitalOcean</strong> (alojamiento en la nube) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Si se añaden otras relaciones de afiliado, se listarán aquí y se actualizará la fecha de la página.</p>

<h2>Sin colocaciones pagadas</h2>
<p>Las reseñas de herramientas, el orden en que las herramientas aparecen en la home y los enlaces de "herramientas relacionadas" bajo cada herramienta <strong>no</strong> dependen de afiliados. No aceptamos dinero por destacar una herramienta ni por colocarla por encima de otra. Si alguna vez se añadiera una colocación pagada (no se va a añadir, pero si pasara), iría marcada igual que los enlaces de afiliado: claro, por adelantado, distinguible del contenido editorial.</p>

<h2>Independencia editorial</h2>
<p>Las relaciones de afiliado no influyen en qué herramientas se construyen, cómo se redactan los bloques de ayuda ni qué "herramientas relacionadas" aparecen bajo una herramienta. Las herramientas de Toolhub son las que construiríamos sin programa de afiliados — el programa solo aporta una pequeña contribución al alojamiento y mantenimiento.</p>

<h2>Contacto</h2>
<p>¿Dudas sobre un afiliado concreto, o quieres marcar algo que parece que no debería estar aquí? Abre una issue en <a href="{REPO_URL}">{REPO_URL}</a> o usa la <a href="/es/contact/">página de contacto</a>.</p>
""".strip(),
            },
            "fr": {
                "title": "Divulgation des affiliations",
                "h1": "Divulgation des affiliations",
                "description": "Divulgation conforme FTC et UE des relations d'affiliation de Toolhub. Le vendeur paie, tu ne paies rien en plus, et le contenu éditorial n'est pas piloté par l'affiliation.",
                "body": f"""
<p><strong>Dernière mise à jour :</strong> {LAST_UPDATED}</p>

<h2>Ce qu'est un lien d'affiliation</h2>
<p>Un lien d'affiliation est un lien normal avec un code de tracking accolé. Si tu cliques dessus et que tu t'inscris ensuite au service lié, le service verse à Toolhub une petite commission d'apport. Le prix que <em>tu</em> paies est identique à la version sans affiliation — ce n'est pas toi qui paies la commission, c'est le vendeur.</p>

<h2>Où ils apparaissent sur Toolhub</h2>
<p>Pour l'instant, les liens d'affiliation apparaissent à deux endroits :</p>
<ul>
<li>Dans le pied de page du site, marqués d'un petit badge <code>(affiliation)</code>.</li>
<li>Partout où un bloc d'aide d'outil ou une section « outils similaires » mentionne un service payant précis qu'on recommande — dans ces cas, l'affiliation est annoncée en ligne.</li>
</ul>
<p>Les liens d'affiliation portent <code>rel="sponsored"</code> en HTML, qui est le standard moteur de recherche pour déclarer une relation commerciale.</p>

<h2>Qui paie</h2>
<p>C'est le vendeur qui paie la commission, pas toi. Si tu ignores le lien d'affiliation et que tu t'inscris directement depuis la page d'accueil du vendeur, tu obtiens le même service au même prix ; on ne voit simplement pas l'apport.</p>

<h2>Conformité FTC et UE</h2>
<p>Cette page existe parce que les <em>endorsement guides</em> de la FTC américaine et les règles européennes de protection du consommateur exigent toutes deux que les créateurs de contenu divulguent une relation financière avec un produit lié. La divulgation doit être claire et en amont — d'où une page de premier niveau, d'où le lien dans le pied de chaque page.</p>

<h2>Affiliations spécifiques</h2>
<p>Les comptes d'affiliation de Toolhub ne sont pas tous actifs au moment de la rédaction — voici une liste provisoire. Dès que chaque compte sera validé, l'opérateur (JXXR1) renseignera les URLs ici :</p>
<ul>
<li><strong>DigitalOcean</strong> (hébergement cloud) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Si d'autres relations d'affiliation s'ajoutent, elles seront listées ici et la page sera redatée.</p>

<h2>Pas de placement payé</h2>
<p>Les présentations d'outils, l'ordre dans lequel les outils apparaissent sur la page d'accueil, et les liens « outils similaires » sous chaque outil ne sont <strong>pas</strong> pilotés par l'affiliation. On n'accepte pas d'argent pour mettre un outil en avant, ni pour classer un outil avant un autre. Si un placement payé devait un jour être ajouté (il ne le sera pas, mais imaginons), il serait étiqueté comme les liens d'affiliation : clair, en amont, distinguable du contenu éditorial.</p>

<h2>Indépendance éditoriale</h2>
<p>Les relations d'affiliation n'influencent pas quels outils sont construits, comment les textes d'aide sont rédigés, ni quels « outils similaires » apparaissent sous tel outil. Les outils sur Toolhub sont ceux qu'on construirait sans aucun programme d'affiliation — le programme contribue juste un peu à l'hébergement et à la maintenance.</p>

<h2>Contact</h2>
<p>Une question sur une affiliation précise, ou tu veux signaler quelque chose qui te semble déplacé ? Ouvre une issue sur <a href="{REPO_URL}">{REPO_URL}</a> ou utilise la <a href="/fr/contact/">page de contact</a>.</p>
""".strip(),
            },
            "it": {
                "title": "Divulgazione affiliati",
                "h1": "Divulgazione affiliati",
                "description": "Divulgazione conforme a FTC e UE delle relazioni di affiliazione di Toolhub. Paga il fornitore, tu non paghi nulla in più, e la copertura editoriale non è guidata dagli affiliati.",
                "body": f"""
<p><strong>Ultimo aggiornamento:</strong> {LAST_UPDATED}</p>

<h2>Cos'è un link affiliato</h2>
<p>Un link affiliato è un normalissimo link con un codice di tracking attaccato. Se ci clicchi e poi ti registri al servizio collegato, il servizio paga a Toolhub una piccola commissione di segnalazione. Il prezzo che <em>tu</em> paghi è identico alla versione non affiliata — non sei tu a pagare la commissione, è il fornitore.</p>

<h2>Dove appaiono su Toolhub</h2>
<p>Attualmente i link affiliati appaiono in due posti:</p>
<ul>
<li>Nel footer del sito, contrassegnati da un piccolo badge <code>(affiliato)</code>.</li>
<li>Ovunque un blocco di aiuto o una sezione "strumenti correlati" menzioni un servizio a pagamento specifico che consigliamo — in quei casi l'affiliazione è dichiarata in linea.</li>
</ul>
<p>I link affiliati portano <code>rel="sponsored"</code> nell'HTML, che è lo standard motori di ricerca per dichiarare una relazione commerciale.</p>

<h2>Chi paga</h2>
<p>Paga il fornitore, non tu. Se ignori il link affiliato e ti registri direttamente dalla home del fornitore, ottieni lo stesso servizio allo stesso prezzo; semplicemente noi non vediamo la segnalazione.</p>

<h2>Conformità FTC e UE</h2>
<p>Questa pagina esiste perché sia le linee guida della Federal Trade Commission statunitense sia le regole di tutela del consumatore della UE richiedono che chi produce contenuti dichiari una relazione finanziaria con un prodotto collegato. La dichiarazione deve essere chiara e in anticipo — da qui una pagina di primo livello, da qui il link nel footer di ogni pagina.</p>

<h2>Affiliati specifici</h2>
<p>Non tutti gli account affiliato di Toolhub sono attivi al momento — questa è una lista segnaposto. Appena ogni account viene approvato, l'operatore (JXXR1) compilerà gli URL qui:</p>
<ul>
<li><strong>DigitalOcean</strong> (hosting cloud) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Se/quando si aggiungeranno altre relazioni di affiliazione, saranno elencate qui e la pagina verrà ridatata.</p>

<h2>Niente posizionamenti a pagamento</h2>
<p>Le recensioni di strumenti, l'ordine in cui gli strumenti compaiono in home e i link "strumenti correlati" sotto ogni strumento <strong>non</strong> dipendono da affiliati. Non accettiamo soldi per mettere in evidenza uno strumento, né per posizionarlo sopra un altro. Se un giorno venisse aggiunto un posizionamento a pagamento (non succederà, ma se accadesse), sarebbe etichettato come i link affiliati: chiaro, in anticipo, distinguibile dal contenuto editoriale.</p>

<h2>Indipendenza editoriale</h2>
<p>Le relazioni di affiliazione non influenzano quali strumenti vengono costruiti, come vengono scritti i blocchi di aiuto, né quali "strumenti correlati" appaiono sotto un determinato strumento. Gli strumenti su Toolhub sono quelli che costruiremmo anche senza programma di affiliazione — il programma contribuisce solo in piccola parte ad hosting e manutenzione.</p>

<h2>Contatti</h2>
<p>Hai domande su un affiliato specifico, o vuoi segnalare qualcosa che non dovrebbe stare qui? Apri una issue su <a href="{REPO_URL}">{REPO_URL}</a> o usa la <a href="/it/contact/">pagina di contatto</a>.</p>
""".strip(),
            },
            "pt": {
                "title": "Divulgação de afiliados",
                "h1": "Divulgação de afiliados",
                "description": "Divulgação compatível com FTC e UE das relações de afiliado do Toolhub. O fornecedor paga, você não paga nada a mais, e a cobertura editorial não é movida por afiliação.",
                "body": f"""
<p><strong>Última atualização:</strong> {LAST_UPDATED}</p>

<h2>O que é um link de afiliado</h2>
<p>Um link de afiliado é um link normal com um código de rastreio anexado. Se você clica e depois se cadastra no serviço linkado, o serviço paga ao Toolhub uma pequena comissão de indicação. O preço que <em>você</em> paga é idêntico à versão sem afiliação — quem paga a comissão não é você, é o fornecedor.</p>

<h2>Onde aparecem no Toolhub</h2>
<p>Atualmente, links de afiliado aparecem em dois lugares:</p>
<ul>
<li>No rodapé do site, marcados com um pequeno badge <code>(afiliado)</code>.</li>
<li>Em qualquer ponto onde o bloco de ajuda de uma ferramenta ou a seção "ferramentas relacionadas" mencione um serviço pago específico que a gente recomenda — nesses casos a afiliação é declarada na hora.</li>
</ul>
<p>Links de afiliado levam <code>rel="sponsored"</code> no HTML, que é o padrão de mecanismos de busca pra declarar uma relação comercial.</p>

<h2>Quem paga</h2>
<p>O fornecedor paga a comissão, não você. Se você ignorar o link de afiliado e se cadastrar direto pela home do fornecedor, recebe o mesmo serviço pelo mesmo preço; só que a gente não vê a indicação.</p>

<h2>Conformidade com FTC e UE</h2>
<p>Essa página existe porque tanto os guias de endosso da FTC dos EUA quanto as regras de defesa do consumidor da UE exigem que criadores de conteúdo divulguem quando têm relação financeira com um produto linkado. A divulgação tem que ser clara e antecipada — daí uma página de primeiro nível, daí o link no rodapé de cada página.</p>

<h2>Afiliados específicos</h2>
<p>Nem todas as contas de afiliado do Toolhub estão ativas no momento — essa é uma lista placeholder. Assim que cada conta for aprovada, o operador (JXXR1) preenche as URLs aqui:</p>
<ul>
<li><strong>DigitalOcean</strong> (hospedagem em nuvem) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Se / quando outras relações de afiliado forem adicionadas, vão entrar nessa lista e a página vai ser redatada.</p>

<h2>Sem placement pago</h2>
<p>Resenhas de ferramentas, a ordem em que as ferramentas aparecem na home e os links de "ferramentas relacionadas" sob cada ferramenta <strong>não</strong> são movidos por afiliação. A gente não aceita dinheiro pra destacar ferramenta, nem pra colocar uma ferramenta acima de outra. Se um dia fosse adicionado placement pago (não vai, mas se fosse), ia ser rotulado igual aos links de afiliado: claro, antecipado, distinguível do conteúdo editorial.</p>

<h2>Independência editorial</h2>
<p>Relações de afiliado não influenciam quais ferramentas são construídas, como o texto de ajuda é escrito ou quais "ferramentas relacionadas" aparecem sob determinada ferramenta. As ferramentas do Toolhub são as ferramentas que a gente construiria sem nenhum programa de afiliado — o programa só dá uma pequena contribuição pra hospedagem e manutenção.</p>

<h2>Contato</h2>
<p>Dúvidas sobre um afiliado específico, ou quer apontar algo que parece que não devia estar aqui? Abre uma issue em <a href="{REPO_URL}">{REPO_URL}</a> ou usa a <a href="/pt/contact/">página de contato</a>.</p>
""".strip(),
            },
            "pl": {
                "title": "Ujawnienie partnerów (affiliate)",
                "h1": "Ujawnienie partnerów (affiliate)",
                "description": "Ujawnienie partnerów Toolhub zgodne z FTC i przepisami UE. Płaci dostawca, ty nie płacisz nic więcej, a treść redakcyjna nie jest sterowana partnerstwem.",
                "body": f"""
<p><strong>Ostatnia aktualizacja:</strong> {LAST_UPDATED}</p>

<h2>Czym jest link partnerski (affiliate)</h2>
<p>Link partnerski to zwykły link z doczepionym kodem śledzącym. Jeśli go klikniesz i potem zarejestrujesz się w linkowanym serwisie, serwis płaci Toolhub niewielką prowizję za polecenie. Cena, którą płacisz <em>ty</em>, jest identyczna jak w wersji bez affiliate — to nie ty płacisz prowizję, tylko dostawca.</p>

<h2>Gdzie pojawiają się na Toolhub</h2>
<p>Obecnie linki partnerskie pojawiają się w dwóch miejscach:</p>
<ul>
<li>W stopce strony, oznaczone małą plakietką <code>(affiliate)</code>.</li>
<li>Wszędzie tam, gdzie blok pomocy narzędzia albo sekcja „powiązane narzędzia" wspomina konkretną płatną usługę, którą polecamy — w tych miejscach partnerstwo jest deklarowane na bieżąco.</li>
</ul>
<p>Linki partnerskie noszą w HTML <code>rel="sponsored"</code>, co jest standardem wyszukiwarek do oznaczania relacji komercyjnej.</p>

<h2>Kto płaci</h2>
<p>Prowizję płaci dostawca, nie ty. Jeśli zignorujesz link partnerski i zarejestrujesz się bezpośrednio ze strony dostawcy, dostaniesz tę samą usługę w tej samej cenie; po prostu my nie zobaczymy polecenia.</p>

<h2>Zgodność z FTC i UE</h2>
<p>Ta strona istnieje, bo zarówno wytyczne dotyczące rekomendacji amerykańskiej Federal Trade Commission, jak i unijne przepisy o ochronie konsumentów wymagają, żeby twórcy treści ujawniali relację finansową z linkowanym produktem. Ujawnienie ma być jasne i z góry — stąd osobna strona najwyższego poziomu i link w stopce na każdej podstronie.</p>

<h2>Konkretni partnerzy</h2>
<p>Nie wszystkie konta partnerskie Toolhub są aktywne w momencie pisania — to jest lista zastępcza. Po zatwierdzeniu każdego konta operator (JXXR1) uzupełni tu adresy URL:</p>
<ul>
<li><strong>DigitalOcean</strong> (hosting w chmurze) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Jeśli/gdy dojdą kolejne relacje partnerskie, zostaną tu wymienione, a strona dostanie nową datę.</p>

<h2>Bez płatnych umieszczeń</h2>
<p>Recenzje narzędzi, kolejność narzędzi na stronie głównej i linki „powiązane narzędzia" pod każdym narzędziem <strong>nie</strong> są sterowane partnerstwem. Nie bierzemy pieniędzy za wyróżnianie narzędzia ani za ustawianie jednego nad drugim. Gdyby kiedykolwiek pojawiło się płatne umieszczenie (nie pojawi się, ale gdyby), byłoby oznaczone tak samo jak linki partnerskie: jasno, z góry, odróżnialne od treści redakcyjnej.</p>

<h2>Niezależność redakcyjna</h2>
<p>Relacje partnerskie nie wpływają na to, jakie narzędzia powstają, jak pisane są bloki pomocy ani jakie „powiązane narzędzia" pojawiają się pod danym narzędziem. Narzędzia w Toolhub to narzędzia, które zbudowalibyśmy i tak — program partnerski to po prostu drobny wkład w hosting i utrzymanie.</p>

<h2>Kontakt</h2>
<p>Pytania o konkretnego partnera albo widzisz coś, co nie powinno tu być? Otwórz issue na <a href="{REPO_URL}">{REPO_URL}</a> albo użyj <a href="/pl/contact/">strony kontaktowej</a>.</p>
""".strip(),
            },
            "ja": {
                "title": "アフィリエイト開示",
                "h1": "アフィリエイト開示",
                "description": "Toolhub のアフィリエイト関係について、FTC・EU 規制に準拠した開示。費用はベンダー側が負担し、あなたに追加の支払いはなく、編集内容はアフィリエイトに左右されません。",
                "body": f"""
<p><strong>最終更新:</strong> {LAST_UPDATED}</p>

<h2>アフィリエイトリンクとは</h2>
<p>アフィリエイトリンクとは、トラッキングコードを付加した通常のリンクです。あなたがそのリンクをクリックして、リンク先のサービスに登録すると、そのサービスから Toolhub に少額の紹介手数料が支払われます。あなたが支払う金額は、アフィリエイトを通さない場合と同じです — 手数料を払うのはあなたではなく、ベンダー側です。</p>

<h2>Toolhub のどこに出てくるか</h2>
<p>現時点で、アフィリエイトリンクは 2 か所に登場します：</p>
<ul>
<li>サイトのフッター。小さな <code>(affiliate)</code> バッジで示されます。</li>
<li>ツールのヘルプブロックや「関連ツール」セクションで、特定の有料サービスを推奨している箇所。そこではアフィリエイトであることがその場で明示されます。</li>
</ul>
<p>アフィリエイトリンクは HTML 上で <code>rel="sponsored"</code> を付けています。これは、商業的関係を示すための検索エンジン側の標準です。</p>

<h2>誰が支払うか</h2>
<p>手数料を支払うのはベンダーであって、あなたではありません。アフィリエイトリンクを無視してベンダーの公式トップページから直接登録しても、まったく同じサービスを同じ価格で受けられます — 紹介の事実が当方に届かないだけです。</p>

<h2>FTC および EU 規制への対応</h2>
<p>本ページは、米連邦取引委員会（FTC）の Endorsement Guides と EU の消費者保護規則が、リンク先製品との金銭的関係があるコンテンツ制作者に対して、その関係を開示することを求めているために用意しています。開示は明確で、かつ事前に行う必要があるため、トップレベルの独立ページを設け、フッターから常にリンクしています。</p>

<h2>個別のアフィリエイト</h2>
<p>執筆時点で、Toolhub のすべてのアフィリエイトアカウントが有効になっているわけではありません — 以下は仮の一覧です。各アカウントの承認後、運用者（JXXR1）がリンク URL を埋めていきます：</p>
<ul>
<li><strong>DigitalOcean</strong>（クラウドホスティング） — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>新たなアフィリエイト関係が追加された場合は、この一覧に追記し、ページの更新日も改訂します。</p>

<h2>有償掲載は行いません</h2>
<p>ツール紹介の文章、トップページに並ぶ順序、各ツール下の「関連ツール」リンクは、いずれも<strong>アフィリエイトによって動かされていません</strong>。特定のツールを掲載してもらうため、あるいは他のツールより上に並べてもらうための金銭は受け取りません。仮に将来、有償掲載が加わるようなことがあれば（その予定はありませんが）、アフィリエイトリンクと同じく、明示的・事前的・編集コンテンツと識別可能な形で表示します。</p>

<h2>編集面の独立性</h2>
<p>アフィリエイト関係は、どのツールを作るか、ヘルプブロックの文面、各ツールに表示する「関連ツール」のいずれにも影響しません。Toolhub に並ぶツールは、アフィリエイトプログラムがまったくなくても作るツール群そのものです — プログラムはホスティングと運用にわずかに貢献するだけです。</p>

<h2>お問い合わせ</h2>
<p>特定のアフィリエイトについてご質問がある、あるいはここに載っているべきでないと感じる箇所がある場合は、<a href="{REPO_URL}">{REPO_URL}</a> で Issue を立てるか、<a href="/ja/contact/">お問い合わせページ</a> をご利用ください。</p>
""".strip(),
            },
            "nl": {
                "title": "Affiliate-disclosure",
                "h1": "Affiliate-disclosure",
                "description": "FTC- en EU-conforme openbaarmaking van Toolhub's affiliate-relaties. De aanbieder betaalt, jij betaalt niets extra, en redactionele inhoud is niet affiliate-gedreven.",
                "body": f"""
<p><strong>Laatst bijgewerkt:</strong> {LAST_UPDATED}</p>

<h2>Wat affiliate-links zijn</h2>
<p>Een affiliate-link is een gewone link met een tracking-code eraan vast. Als je erop klikt en je vervolgens aanmeldt bij de gelinkte dienst, betaalt de dienst Toolhub een kleine verwijzingsvergoeding. De prijs die <em>jij</em> betaalt is identiek aan de niet-affiliate versie — niet jij betaalt de commissie, de aanbieder doet dat.</p>

<h2>Waar ze op Toolhub staan</h2>
<p>Op dit moment staan affiliate-links op twee plekken:</p>
<ul>
<li>In de footer van de site, gemarkeerd met een kleine <code>(affiliate)</code>-badge.</li>
<li>Overal waar het help-blok van een tool of de "gerelateerde tools"-sectie een specifieke betaalde dienst noemt die we aanbevelen — daar wordt de affiliate ter plekke aangegeven.</li>
</ul>
<p>Affiliate-links dragen in de HTML <code>rel="sponsored"</code>, wat de zoekmachine-standaard is om een commerciële relatie aan te geven.</p>

<h2>Wie betaalt</h2>
<p>De aanbieder betaalt de commissie, niet jij. Als je de affiliate-link negeert en je rechtstreeks via de homepage van de aanbieder aanmeldt, krijg je dezelfde dienst voor dezelfde prijs; wij zien gewoon geen verwijzing.</p>

<h2>FTC- en EU-naleving</h2>
<p>Deze pagina bestaat omdat zowel de endorsement guides van de Amerikaanse Federal Trade Commission als de EU-regels voor consumentenbescherming vereisen dat contentmakers een financiële relatie met een gelinkt product openbaar maken. De openbaarmaking moet helder en vooraf zijn — vandaar een aparte top-level pagina, vandaar de link in elke pagina-footer.</p>

<h2>Specifieke affiliates</h2>
<p>Niet alle affiliate-accounts van Toolhub zijn al actief op het moment van schrijven — dit is een placeholder-lijst. Zodra elk account is goedgekeurd, vult de operator (JXXR1) hier de URLs in:</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud-hosting) — <code>&lt;DO ref link TBD&gt;</code></li>
<li><strong>GitHub Sponsors</strong> — <code>&lt;URL TBD&gt;</code></li>
<li><strong>Buy Me a Coffee</strong> — <code>&lt;URL TBD&gt;</code></li>
</ul>
<p>Als/wanneer er andere affiliate-relaties bijkomen, worden ze hier vermeld en wordt de paginadatum bijgewerkt.</p>

<h2>Geen betaalde plaatsingen</h2>
<p>Tool-reviews, de volgorde waarin tools op de homepage staan en de "gerelateerde tools"-links onder elke tool zijn <strong>niet</strong> affiliate-gedreven. We accepteren geen geld om een tool uit te lichten of een tool boven een ander te plaatsen. Als er ooit een betaalde plaatsing zou worden toegevoegd (dat gaat niet gebeuren, maar voor het geval), zou die net als affiliate-links worden gelabeld: helder, vooraf, onderscheidbaar van redactionele inhoud.</p>

<h2>Redactionele onafhankelijkheid</h2>
<p>Affiliate-relaties beïnvloeden niet welke tools worden gebouwd, hoe help-blokken zijn geschreven, of welke "gerelateerde tools" onder een gegeven tool verschijnen. De tools op Toolhub zijn de tools die we ook zonder affiliate-programma zouden bouwen — het programma levert alleen een kleine bijdrage aan hosting en onderhoud.</p>

<h2>Contact</h2>
<p>Vragen over een specifieke affiliate, of wil je iets aanwijzen dat hier niet hoort? Open een issue op <a href="{REPO_URL}">{REPO_URL}</a> of gebruik de <a href="/nl/contact/">contactpagina</a>.</p>
""".strip(),
            },
        },
    },
}
