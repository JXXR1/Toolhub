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


# Trust signals block for /for-schools/ — Google Safe Browsing + VirusTotal scan
# refs plus open-source pointer. Public, third-party verification signals that
# an IT admin can check before whitelisting a new domain on a school filter.
# Same factual content across langs; only the framing is translated.
SAFE_BROWSING_URL = "https://safebrowsing.google.com/safebrowsing/diagnostic?site=toolhub.software"
VIRUSTOTAL_URL = "https://www.virustotal.com/gui/url/915d00d574ca73037fd2d5b639a257886c75e26c17583c11d03e2db1e3d7e80d/detection"

_TRUST_SIGNALS_I18N = {
    "en": {
        "h2": "Trust signals for IT admins",
        "intro": "If your school's network filter requires verification before allowing access to a new domain, these are the public, third-party signals you can check:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Verify Toolhub's status",
        "gsb_after": "Google's automated phishing/malware classifier. Toolhub is on the clean list.",
        "vt_label": "VirusTotal scan:",
        "vt_link": "View latest scan result",
        "vt_after": "Independent third-party multi-engine scan (70+ antivirus engines).",
        "oss_text": "Toolhub is also {link} — IT admins can inspect every line of code before approving the domain.",
        "oss_link": "open source on GitHub",
    },
    "de": {
        "h2": "Vertrauenssignale für IT-Admins",
        "intro": "Wenn der Netzwerkfilter Ihrer Schule eine Prüfung verlangt, bevor eine neue Domain freigegeben wird — das sind die öffentlichen, unabhängigen Signale, die Sie prüfen können:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Toolhub-Status prüfen",
        "gsb_after": "Googles automatischer Phishing-/Malware-Klassifikator. Toolhub steht auf der sauberen Liste.",
        "vt_label": "VirusTotal-Scan:",
        "vt_link": "Aktuelles Scan-Ergebnis ansehen",
        "vt_after": "Unabhängiger Multi-Engine-Scan eines Drittanbieters (70+ Antivirus-Engines).",
        "oss_text": "Toolhub ist außerdem {link} — IT-Admins können jede Zeile Code prüfen, bevor sie die Domain freigeben.",
        "oss_link": "auf GitHub Open Source",
    },
    "es": {
        "h2": "Señales de confianza para administradores de TI",
        "intro": "Si el filtro de red de su centro requiere verificación antes de permitir el acceso a un nuevo dominio, estas son las señales públicas y de terceros que puede comprobar:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Comprobar el estado de Toolhub",
        "gsb_after": "El clasificador automático de phishing/malware de Google. Toolhub está en la lista limpia.",
        "vt_label": "Análisis VirusTotal:",
        "vt_link": "Ver el último resultado del escaneo",
        "vt_after": "Análisis multi-motor independiente de terceros (más de 70 motores antivirus).",
        "oss_text": "Toolhub también es {link} — los administradores de TI pueden revisar cada línea de código antes de aprobar el dominio.",
        "oss_link": "open source en GitHub",
    },
    "fr": {
        "h2": "Signaux de confiance pour les admins IT",
        "intro": "Si le filtre réseau de votre établissement exige une vérification avant d'autoriser l'accès à un nouveau domaine, voici les signaux publics et tiers que vous pouvez vérifier :",
        "gsb_label": "Google Safe Browsing :",
        "gsb_link": "Vérifier le statut de Toolhub",
        "gsb_after": "Le classificateur automatique phishing/malware de Google. Toolhub est sur la liste propre.",
        "vt_label": "Analyse VirusTotal :",
        "vt_link": "Voir le dernier résultat d'analyse",
        "vt_after": "Analyse multi-moteurs indépendante d'un tiers (plus de 70 moteurs antivirus).",
        "oss_text": "Toolhub est aussi {link} — les admins IT peuvent inspecter chaque ligne de code avant d'autoriser le domaine.",
        "oss_link": "open source sur GitHub",
    },
    "it": {
        "h2": "Segnali di fiducia per gli admin IT",
        "intro": "Se il filtro di rete della sua scuola richiede una verifica prima di consentire l'accesso a un nuovo dominio, questi sono i segnali pubblici e di terze parti che può controllare:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Verifica lo stato di Toolhub",
        "gsb_after": "Il classificatore automatico phishing/malware di Google. Toolhub è nella lista pulita.",
        "vt_label": "Scansione VirusTotal:",
        "vt_link": "Vedi l'ultimo risultato della scansione",
        "vt_after": "Scansione multi-engine indipendente di terze parti (oltre 70 motori antivirus).",
        "oss_text": "Toolhub è anche {link} — gli admin IT possono ispezionare ogni riga di codice prima di approvare il dominio.",
        "oss_link": "open source su GitHub",
    },
    "pt": {
        "h2": "Sinais de confiança pra admins de TI",
        "intro": "Se o filtro de rede da sua escola precisa de verificação antes de permitir acesso a um novo domínio, esses são os sinais públicos e de terceiros que você pode checar:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Verificar o status do Toolhub",
        "gsb_after": "Classificador automático de phishing/malware do Google. O Toolhub está na lista limpa.",
        "vt_label": "Análise VirusTotal:",
        "vt_link": "Ver o último resultado do scan",
        "vt_after": "Análise multi-engine independente de terceiros (mais de 70 engines antivírus).",
        "oss_text": "O Toolhub também é {link} — admins de TI podem inspecionar cada linha de código antes de aprovar o domínio.",
        "oss_link": "open source no GitHub",
    },
    "pl": {
        "h2": "Sygnały zaufania dla adminów IT",
        "intro": "Jeśli filtr sieci szkolnej wymaga weryfikacji przed dopuszczeniem nowej domeny, oto publiczne sygnały od stron trzecich, które możesz sprawdzić:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Sprawdź status Toolhub",
        "gsb_after": "Automatyczny klasyfikator phishingu/malware Google. Toolhub jest na czystej liście.",
        "vt_label": "Skan VirusTotal:",
        "vt_link": "Zobacz najnowszy wynik skanu",
        "vt_after": "Niezależny multi-engine skan strony trzeciej (ponad 70 silników antywirusowych).",
        "oss_text": "Toolhub jest też {link} — adminowie IT mogą obejrzeć każdą linijkę kodu, zanim zatwierdzą domenę.",
        "oss_link": "open source na GitHub",
    },
    "ja": {
        "h2": "IT 管理者向けの信頼シグナル",
        "intro": "学校のネットワークフィルタが新しいドメインへのアクセスを許可する前に確認を要求する場合、確認できる公開・第三者シグナルは次のとおりです：",
        "gsb_label": "Google Safe Browsing：",
        "gsb_link": "Toolhub のステータスを確認",
        "gsb_after": "Google の自動フィッシング／マルウェア分類。Toolhub はクリーンリストに掲載されています。",
        "vt_label": "VirusTotal スキャン：",
        "vt_link": "最新のスキャン結果を表示",
        "vt_after": "独立した第三者によるマルチエンジン スキャン（70 以上のアンチウイルスエンジン）。",
        "oss_text": "Toolhub は {link} でもあります — IT 管理者はドメインを承認する前にすべてのコードを検査できます。",
        "oss_link": "GitHub 上でオープンソース",
    },
    "nl": {
        "h2": "Vertrouwenssignalen voor IT-admins",
        "intro": "Als het netwerkfilter van je school verificatie vereist voordat een nieuw domein wordt toegestaan, dit zijn de publieke, externe signalen die je kunt controleren:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Verifieer de status van Toolhub",
        "gsb_after": "Google's geautomatiseerde phishing/malware-classifier. Toolhub staat op de schone lijst.",
        "vt_label": "VirusTotal-scan:",
        "vt_link": "Bekijk het laatste scanresultaat",
        "vt_after": "Onafhankelijke multi-engine scan van een derde partij (meer dan 70 antivirus-engines).",
        "oss_text": "Toolhub is ook {link} — IT-admins kunnen elke regel code inspecteren voordat ze het domein goedkeuren.",
        "oss_link": "open source op GitHub",
    },
    "tr": {
        "h2": "BT yöneticileri için güven sinyalleri",
        "intro": "Okulunuzun ağ filtresi yeni bir domain'e erişime izin vermeden önce doğrulama gerektiriyorsa, kontrol edebileceğiniz herkese açık, üçüncü taraf sinyalleri şunlardır:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Toolhub'ın durumunu doğrula",
        "gsb_after": "Google'ın otomatik phishing/malware sınıflandırıcısı. Toolhub temiz listede.",
        "vt_label": "VirusTotal taraması:",
        "vt_link": "Son tarama sonucunu gör",
        "vt_after": "Bağımsız üçüncü taraf çoklu motor taraması (70'ten fazla antivirüs motoru).",
        "oss_text": "Toolhub aynı zamanda {link} — BT yöneticileri domain'i onaylamadan önce her kod satırını inceleyebilir.",
        "oss_link": "GitHub'da open source",
    },
    "id": {
        "h2": "Sinyal kepercayaan untuk admin TI",
        "intro": "Jika filter jaringan sekolahmu membutuhkan verifikasi sebelum mengizinkan akses ke domain baru, berikut adalah sinyal publik dari pihak ketiga yang bisa kamu cek:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Verifikasi status Toolhub",
        "gsb_after": "Klasifikator phishing/malware otomatis dari Google. Toolhub ada di daftar bersih.",
        "vt_label": "Pemindaian VirusTotal:",
        "vt_link": "Lihat hasil pemindaian terbaru",
        "vt_after": "Pemindaian multi-engine pihak ketiga independen (70+ engine antivirus).",
        "oss_text": "Toolhub juga {link} — admin TI bisa memeriksa setiap baris kode sebelum menyetujui domain.",
        "oss_link": "open source di GitHub",
    },
    "vi": {
        "h2": "Tín hiệu tin cậy cho admin IT",
        "intro": "Nếu bộ lọc mạng trường học yêu cầu xác minh trước khi cho phép truy cập một domain mới, đây là các tín hiệu công khai từ bên thứ ba mà bạn có thể kiểm tra:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Xác minh trạng thái Toolhub",
        "gsb_after": "Trình phân loại phishing/malware tự động của Google. Toolhub nằm trong danh sách sạch.",
        "vt_label": "Quét VirusTotal:",
        "vt_link": "Xem kết quả quét mới nhất",
        "vt_after": "Quét đa engine từ bên thứ ba độc lập (hơn 70 engine antivirus).",
        "oss_text": "Toolhub cũng là {link} — admin IT có thể kiểm tra từng dòng code trước khi phê duyệt domain.",
        "oss_link": "mã nguồn mở trên GitHub",
    },
    "hi": {
        "h2": "IT admins के लिए trust signals",
        "intro": "अगर आपके स्कूल का network filter किसी नए domain को अनुमति देने से पहले verification मांगता है, तो ये सार्वजनिक, third-party signals हैं जिन्हें आप check कर सकते हैं:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Toolhub का status verify करें",
        "gsb_after": "Google का स्वचालित phishing/malware classifier। Toolhub clean list में है।",
        "vt_label": "VirusTotal scan:",
        "vt_link": "नवीनतम scan परिणाम देखें",
        "vt_after": "स्वतंत्र third-party multi-engine scan (70+ antivirus engines)।",
        "oss_text": "Toolhub {link} भी है — IT admins domain को approve करने से पहले कोड की हर पंक्ति की जांच कर सकते हैं।",
        "oss_link": "GitHub पर open source",
    },
    "sk": {
        "h2": "Signály dôvery pre IT adminov",
        "intro": "Ak školský sieťový filter vyžaduje overenie pred povolením prístupu k novej doméne, tu sú verejné signály od tretích strán, ktoré si môžete overiť:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Overiť stav Toolhubu",
        "gsb_after": "Automatický klasifikátor phishingu/malvéru od Google. Toolhub je na čistom zozname.",
        "vt_label": "VirusTotal sken:",
        "vt_link": "Zobraziť najnovší výsledok skenu",
        "vt_after": "Nezávislý multi-engine sken tretej strany (vyše 70 antivírusových engineov).",
        "oss_text": "Toolhub je tiež {link} — IT adminovia môžu skontrolovať každý riadok kódu pred schválením domény.",
        "oss_link": "open source na GitHub",
    },
    "cs": {
        "h2": "Signály důvěry pro IT adminy",
        "intro": "Pokud školní síťový filtr vyžaduje ověření před povolením přístupu k nové doméně, toto jsou veřejné signály od třetích stran, které si můžete ověřit:",
        "gsb_label": "Google Safe Browsing:",
        "gsb_link": "Ověřit stav Toolhubu",
        "gsb_after": "Automatický klasifikátor phishingu/malwaru od Google. Toolhub je na čistém seznamu.",
        "vt_label": "VirusTotal sken:",
        "vt_link": "Zobrazit nejnovější výsledek skenu",
        "vt_after": "Nezávislý multi-engine sken třetí strany (přes 70 antivirových enginů).",
        "oss_text": "Toolhub je také {link} — IT adminové můžou prohlédnout každý řádek kódu před schválením domény.",
        "oss_link": "open source na GitHub",
    },
}


def _trust_signals(lang: str) -> str:
    s = _TRUST_SIGNALS_I18N.get(lang, _TRUST_SIGNALS_I18N["en"])
    oss_link_html = f'<a href="{REPO_URL}">{s["oss_link"]}</a>'
    oss_para = s["oss_text"].replace("{link}", oss_link_html)
    return f"""
<h2>{s["h2"]}</h2>
<p>{s["intro"]}</p>
<ul>
<li><strong>{s["gsb_label"]}</strong> <a href="{SAFE_BROWSING_URL}" rel="noopener">{s["gsb_link"]}</a> — {s["gsb_after"]}</li>
<li><strong>{s["vt_label"]}</strong> <a href="{VIRUSTOTAL_URL}" rel="noopener">{s["vt_link"]}</a> — {s["vt_after"]}</li>
</ul>
<p>{oss_para}</p>
""".strip()


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
            "tr": {
                "title": "Toolhub Hakkında",
                "h1": "Toolhub Hakkında",
                "description": "Toolhub, tek kişi tarafından inşa edilmiş küçük takipsiz bir araç sitesidir. Tamamen tarayıcında çalışan, kayıt veya veri toplama olmadan ücretsiz geliştirici araçları.",
                "body": _about_body(
                    intro_what="Toolhub, tamamen tarayıcında çalışan ücretsiz geliştirici ve günlük araçların bir koleksiyonudur. Kayıt yok, hesap yok, takip yok, sunucu tarafında işleme yok. Verini yapıştır, sonucu al, sekmeyi kapat — hiçbir şey saklanmaz veya iletilmez.",
                    intro_why="Çoğu online araç sitesi reklamla dolu parking sayfalardır veya bir tıklama yapmadan önce verini on dört üçüncü taraf takipçisinden geçirir. Toolhub alternatiftir: tek sayfa, tek araç, yerel çalışır, seni rahat bırakır.",
                    intro_who=f'JXXR1, bağımsız maintainer. Şirket yok, finansman turu yok, yatırımcı yok. Toolhub kişisel bir kaşıntıyı gidermek için bir yan proje olarak başladı — bir aracı iyi yapan tek bir sayfa — ve oradan büyüdü. <a href="{REPO_URL}">GitHub</a> üzerinden ulaşılabilir.',
                    intro_how="Site GitHub Pages üzerinde barındırılan statik HTML'dir. Her araç tarayıcında JavaScript olarak çalışır — API çağrısı yok, sunucu tarafı hesaplama yok, açıkça belirtilmedikçe (örneğin YouTube Thumbnail aracı YouTube'un CDN'inden bir görsel çeker; her şey tamamen yerel) hiçbir veri cihazını terk etmez.",
                    intro_oss=f'Tüm kaynak <a href="{REPO_URL}">{REPO_URL}</a>\'dadır. Katkılar, hata raporları ve araç fikirleri GitHub Issues üzerinden hoş karşılanır.',
                    intro_no_ai="Araç yardım blokları ve çeviriler makul ölçüde insanlar tarafından gözden geçirilir, bir LLM\'den yapıştırılmaz. Robotik veya yanlış görünen bir çeviri görürsen, bir issue aç — kolay bir düzeltmedir ve siteyi herkes için daha iyi yapan türden bir katkıdır.",
                    h_what="Toolhub nedir",
                    h_why="Neden",
                    h_who="Kim",
                    h_how="Nasıl çalışır",
                    h_oss="Açık kaynak",
                    h_no_ai="AI saçmalığı yok",
                ),
            },
            "id": {
                "title": "Tentang Toolhub",
                "h1": "Tentang Toolhub",
                "description": "Toolhub adalah situs utilitas kecil tanpa pelacakan yang dibangun oleh satu orang. Alat developer gratis yang berjalan sepenuhnya di browser, tanpa pendaftaran, tanpa pengumpulan data.",
                "body": _about_body(
                    intro_what="Toolhub adalah kumpulan alat developer dan utilitas sehari-hari yang gratis dan berjalan sepenuhnya di browser. Tanpa pendaftaran, tanpa akun, tanpa pelacakan, tanpa pemrosesan di sisi server. Tempel data, dapatkan hasil, tutup tab — tidak ada yang disimpan atau dikirim.",
                    intro_why="Kebanyakan situs alat online adalah halaman parkir yang penuh iklan, atau melewatkan datamu melalui empat belas pelacak pihak ketiga sebelum kamu sempat mengklik apa pun. Toolhub adalah alternatifnya: satu halaman, satu alat, berjalan lokal, dan membiarkanmu sendiri.",
                    intro_who=f'JXXR1, maintainer independen. Tanpa perusahaan, tanpa putaran pendanaan, tanpa investor. Toolhub dimulai sebagai proyek sampingan untuk menggaruk gatal pribadi — satu halaman yang melakukan satu alat dengan baik — dan tumbuh dari sana. Bisa dihubungi via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Situs ini adalah HTML statis yang di-host di GitHub Pages. Setiap alat berjalan sebagai JavaScript di browser-mu — tanpa panggilan API, tanpa komputasi sisi server, tanpa data yang meninggalkan perangkatmu kecuali dinyatakan secara eksplisit (misalnya alat YouTube Thumbnail mengambil gambar dari CDN YouTube; semua yang lain sepenuhnya lokal).",
                    intro_oss=f'Seluruh source code ada di <a href="{REPO_URL}">{REPO_URL}</a>. Kontribusi, laporan bug, dan ide alat diterima dengan baik melalui GitHub Issues.',
                    intro_no_ai="Blok bantuan alat dan terjemahan secara wajar ditinjau oleh manusia, tidak ditempel dari LLM. Jika kamu melihat terjemahan yang terdengar robotik atau salah, buka issue — itu perbaikan yang mudah dan jenis kontribusi yang membuat situs ini lebih baik untuk semua orang.",
                    h_what="Apa itu Toolhub",
                    h_why="Mengapa",
                    h_who="Siapa",
                    h_how="Cara kerjanya",
                    h_oss="Open source",
                    h_no_ai="Tanpa omong kosong AI",
                ),
            },
            "vi": {
                "title": "Giới thiệu Toolhub",
                "h1": "Giới thiệu Toolhub",
                "description": "Toolhub là một site tiện ích nhỏ không theo dõi do một người xây dựng. Công cụ dev miễn phí chạy hoàn toàn trong trình duyệt của bạn, không cần đăng ký, không thu thập dữ liệu.",
                "body": _about_body(
                    intro_what="Toolhub là một bộ sưu tập công cụ dev và tiện ích hằng ngày miễn phí, chạy hoàn toàn trong trình duyệt của bạn. Không cần đăng ký, không có tài khoản, không theo dõi, không xử lý phía server. Dán dữ liệu vào, lấy kết quả, đóng tab — không có gì được lưu hoặc truyền đi.",
                    intro_why="Hầu hết các site tiện ích online đều là các trang đỗ đầy quảng cáo, hoặc đẩy dữ liệu của bạn qua mười bốn trình theo dõi của bên thứ ba trước khi bạn kịp click bất kỳ thứ gì. Toolhub là phương án thay thế: một trang, một công cụ, chạy cục bộ, và để bạn yên.",
                    intro_who=f'JXXR1, maintainer độc lập. Không có công ty, không có vòng gọi vốn, không có nhà đầu tư. Toolhub bắt đầu như một dự án phụ để giải quyết một nhu cầu cá nhân — một trang duy nhất làm tốt một công cụ — và phát triển từ đó. Có thể liên hệ qua <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Site này là HTML tĩnh được host trên GitHub Pages. Mỗi công cụ chạy dưới dạng JavaScript trong trình duyệt của bạn — không có lời gọi API, không có tính toán phía server, không có dữ liệu nào rời khỏi thiết bị của bạn trừ khi được ghi rõ ràng (ví dụ công cụ YouTube Thumbnail fetch một ảnh từ CDN của YouTube; mọi thứ khác hoàn toàn cục bộ).",
                    intro_oss=f'Toàn bộ source code ở <a href="{REPO_URL}">{REPO_URL}</a>. Đóng góp, báo lỗi và ý tưởng công cụ được hoan nghênh qua GitHub Issues.',
                    intro_no_ai="Block trợ giúp công cụ và bản dịch được con người xem xét trong khả năng, không được paste từ LLM. Nếu bạn thấy bản dịch nghe có vẻ máy móc hoặc sai, hãy mở issue — đó là một sửa chữa dễ và là loại đóng góp làm cho site tốt hơn cho mọi người.",
                    h_what="Toolhub là gì",
                    h_why="Tại sao",
                    h_who="Ai",
                    h_how="Hoạt động ra sao",
                    h_oss="Open source",
                    h_no_ai="Không xài rác AI",
                ),
            },
            "sk": {
                "title": "O Toolhube",
                "h1": "O Toolhube",
                "description": "Toolhub je malá utility stránka bez sledovania, ktorú postavil jeden človek. Bezplatné developer nástroje, čo bežia úplne v tvojom prehliadači — bez registrácie, bez zbierania údajov.",
                "body": _about_body(
                    intro_what="Toolhub je zbierka bezplatných developer nástrojov a každodenných utilít, ktoré bežia úplne v tvojom prehliadači. Bez registrácie, bez účtu, bez sledovania, bez spracovania na serveri. Vložíš svoje dáta, dostaneš výsledok, zavrieš záložku — nič sa neukladá ani neprenáša.",
                    intro_why="Väčšina online utility stránok je buď reklamami zaprataná parking page, alebo prepúšťa tvoje dáta cez štrnásť third-party trackerov skôr, než vôbec na niečo klikneš. Toolhub je alternatíva: jedna stránka, jeden nástroj, beží lokálne, necháva ťa na pokoji.",
                    intro_who=f'JXXR1, nezávislý maintainer. Žiadna firma, žiadne investičné kolo, žiadni investori. Toolhub začal ako vedľajší projekt na osobnú potrebu — jedna stránka, ktorá robí jeden nástroj poriadne — a odtiaľ rástol. Kontakt cez <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Stránka je statické HTML hostované na GitHub Pages. Každý nástroj beží ako JavaScript v tvojom prehliadači — žiadne API volania, žiadny server-side compute, žiadne dáta neopúšťajú tvoje zariadenie, pokiaľ to nie je explicitne uvedené (napríklad nástroj YouTube Thumbnail si načíta obrázok z YouTube CDN; všetko ostatné je čisto lokálne).",
                    intro_oss=f'Celý zdrojový kód je na <a href="{REPO_URL}">{REPO_URL}</a>. Príspevky, bug reporty a nápady na nástroje sú vítané cez GitHub Issues.',
                    intro_no_ai="Help bloky nástrojov a preklady sú v rámci možností kontrolované ľuďmi, nie nakopírované z LLM. Ak nájdeš preklad, ktorý znie roboticky alebo zle, otvor issue — je to ľahká oprava a typ príspevku, ktorý robí stránku lepšou pre všetkých.",
                    h_what="Čo Toolhub je",
                    h_why="Prečo",
                    h_who="Kto",
                    h_how="Ako to funguje",
                    h_oss="Open source",
                    h_no_ai="Žiadny AI odpad",
                ),
            },
            "cs": {
                "title": "O Toolhubu",
                "h1": "O Toolhubu",
                "description": "Toolhub je malá utility stránka bez sledování, kterou postavil jeden člověk. Bezplatné developer nástroje, co běží zcela v tvém prohlížeči — bez registrace, bez sběru dat.",
                "body": _about_body(
                    intro_what="Toolhub je sbírka bezplatných developer nástrojů a každodenních utilit, které běží zcela v tvém prohlížeči. Bez registrace, bez účtu, bez sledování, bez zpracování na serveru. Vložíš svoje data, dostaneš výsledek, zavřeš kartu — nic se neukládá ani nepřenáší.",
                    intro_why="Většina online utility stránek je buď reklamou přecpaná parking page, nebo posílá tvoje data přes čtrnáct third-party trackerů dřív, než vůbec na cokoli klikneš. Toolhub je alternativa: jedna stránka, jeden nástroj, běží lokálně, nechává tě být.",
                    intro_who=f'JXXR1, nezávislý maintainer. Žádná firma, žádné investiční kolo, žádní investoři. Toolhub začal jako vedlejší projekt pro osobní potřebu — jedna stránka, která by jeden nástroj dělala pořádně — a odtud rostl. Kontakt přes <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Stránka je statické HTML hostované na GitHub Pages. Každý nástroj běží jako JavaScript v tvém prohlížeči — žádná API volání, žádný server-side compute, žádná data neopouštějí tvé zařízení, pokud to není výslovně uvedeno (například nástroj YouTube Thumbnail si stahuje obrázek z YouTube CDN; všechno ostatní je čistě lokální).",
                    intro_oss=f'Celý zdrojový kód je na <a href="{REPO_URL}">{REPO_URL}</a>. Příspěvky, bug reporty a nápady na nástroje jsou vítány přes GitHub Issues.',
                    intro_no_ai="Help bloky nástrojů a překlady jsou v rámci možností kontrolovány lidmi, ne nakopírovány z LLM. Pokud najdeš překlad, který zní roboticky nebo špatně, otevři issue — je to snadná oprava a typ příspěvku, který dělá stránku lepší pro všechny.",
                    h_what="Co je Toolhub",
                    h_why="Proč",
                    h_who="Kdo",
                    h_how="Jak to funguje",
                    h_oss="Open source",
                    h_no_ai="Žádný AI odpad",
                ),
            },
            "hi": {
                "title": "Toolhub के बारे में",
                "h1": "Toolhub के बारे में",
                "description": "Toolhub एक छोटी, ट्रैकिंग-मुक्त utility साइट है जिसे एक ही व्यक्ति ने बनाया है। मुफ़्त developer tools जो पूरी तरह आपके browser में चलते हैं — साइनअप नहीं, ट्रैकिंग नहीं, डेटा संग्रह नहीं।",
                "body": _about_body(
                    intro_what="Toolhub मुफ़्त developer और रोज़मर्रा के utility tools का संग्रह है जो पूरी तरह आपके browser में चलते हैं। कोई साइनअप नहीं, कोई अकाउंट नहीं, कोई ट्रैकिंग नहीं, कोई server-side processing नहीं। अपना डेटा paste कीजिए, परिणाम पाइए, tab बंद कीजिए — कुछ भी संग्रहित या प्रसारित नहीं होता।",
                    intro_why="ज़्यादातर online utility साइटें या तो विज्ञापनों से भरी parking pages होती हैं, या आपके क्लिक करने से पहले ही आपका डेटा चौदह third-party trackers से गुज़ार देती हैं। Toolhub इसका विकल्प है: एक page, एक tool, locally चलता है, आपको शांति से रहने देता है।",
                    intro_who=f'JXXR1, स्वतंत्र maintainer। कोई कंपनी नहीं, कोई funding round नहीं, कोई investor नहीं। Toolhub एक side project के रूप में शुरू हुआ — एक निजी ज़रूरत पूरी करने के लिए, एक page जो एक tool को अच्छे से करे — और वहीं से बढ़ा। संपर्क <a href="{REPO_URL}">GitHub</a> के ज़रिए।',
                    intro_how="यह साइट GitHub Pages पर hosted static HTML है। हर tool आपके browser में JavaScript के रूप में चलता है — कोई API call नहीं, कोई server-side compute नहीं, कोई डेटा आपके device से बाहर नहीं जाता जब तक स्पष्ट रूप से न बताया जाए (उदाहरण के लिए YouTube Thumbnail tool YouTube के CDN से एक image fetch करता है; बाकी सब पूरी तरह locally है)।",
                    intro_oss=f'पूरा source code <a href="{REPO_URL}">{REPO_URL}</a> पर है। योगदान, bug reports और tool के सुझाव GitHub Issues के माध्यम से स्वागत हैं।',
                    intro_no_ai="Tool help blocks और अनुवाद यथासंभव मनुष्यों द्वारा जाँचे गए हैं, LLM से paste किए हुए नहीं। अगर आपको कोई अनुवाद robotic या ग़लत लगे, तो एक issue खोलिए — यह आसान सुधार है और ऐसा योगदान है जो साइट को सबके लिए बेहतर बनाता है।",
                    h_what="Toolhub क्या है",
                    h_why="क्यों",
                    h_who="कौन",
                    h_how="यह कैसे काम करता है",
                    h_oss="Open source",
                    h_no_ai="कोई AI कूड़ा नहीं",
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
            "tr": {
                "title": "İletişim",
                "h1": "İletişim",
                "description": "Hata raporları, özellik istekleri ve araç fikirleri için GitHub Issues üzerinden veya gerisi için e-posta ile Toolhub maintainer'ına ulaş.",
                "body": f"""
<p>Toolhub tek kişilik bir yan projedir. Best-effort yanıt süreleri, ticari değil. İletişim formu yoktur — bu sitenin kasıtlı olarak backend\'i yok.</p>

<h2>GitHub Issues</h2>
<p>Hata raporları, özellik istekleri, çeviri düzeltmeleri ve yeni araç fikirleri için — bir issue aç:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues tercih edilir çünkü tartışmaya aynı soruya sahip diğer insanların daha sonra bulabileceği kalıcı bir URL verir.</p>

<h2>E-posta</h2>
<p>GitHub Issues'a uymayan konular için — basın, ortaklık, güvenlik açığı raporları, kaldırma talepleri — <code>{CONTACT_EMAIL}</code> adresine e-posta gönder.</p>

<h2>Yanıt süreleri</h2>
<p>Her şeyi bir hafta içinde okumaya çalışırım, ama Toolhub gündüz işiminin yanında boş zamanlarımda inşa edilir ve sürdürülür. Bir şey acilse (örneğin güvenlik), bunu subject satırına koy.</p>
""".strip(),
            },
            "id": {
                "title": "Kontak",
                "h1": "Kontak",
                "description": "Hubungi maintainer Toolhub melalui GitHub Issues untuk laporan bug, permintaan fitur, dan ide alat — atau via email untuk hal lainnya.",
                "body": f"""
<p>Toolhub adalah proyek sampingan satu orang. Waktu respons best-effort, bukan komersial. Tidak ada formulir kontak — situs ini sengaja tidak punya backend.</p>

<h2>GitHub Issues</h2>
<p>Untuk laporan bug, permintaan fitur, perbaikan terjemahan, dan ide alat baru — buka issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues lebih disukai karena memberi diskusi URL permanen yang bisa ditemukan kemudian oleh orang lain dengan pertanyaan yang sama.</p>

<h2>Email</h2>
<p>Untuk hal-hal yang tidak cocok di GitHub Issues — pers, kemitraan, laporan kerentanan keamanan, permintaan takedown — kirim email ke <code>{CONTACT_EMAIL}</code>.</p>

<h2>Waktu respons</h2>
<p>Saya berusaha membaca semuanya dalam waktu seminggu, tetapi Toolhub dibangun dan dirawat di waktu luang di samping pekerjaan utama. Jika sesuatu mendesak (misalnya keamanan), tulis itu di baris subjek.</p>
""".strip(),
            },
            "vi": {
                "title": "Liên hệ",
                "h1": "Liên hệ",
                "description": "Liên hệ với maintainer Toolhub qua GitHub Issues để báo lỗi, yêu cầu tính năng và ý tưởng công cụ — hoặc qua email cho các vấn đề khác.",
                "body": f"""
<p>Toolhub là dự án phụ một-người. Thời gian phản hồi best-effort, không phải thương mại. Không có form liên hệ — site này cố ý không có backend.</p>

<h2>GitHub Issues</h2>
<p>Cho báo lỗi, yêu cầu tính năng, sửa bản dịch, và ý tưởng công cụ mới — mở một issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues được ưu tiên vì nó cho thảo luận một URL vĩnh viễn mà người khác có cùng câu hỏi có thể tìm thấy sau này.</p>

<h2>Email</h2>
<p>Cho những thứ không phù hợp với GitHub Issues — báo chí, hợp tác, báo cáo lỗ hổng bảo mật, yêu cầu takedown — gửi email tới <code>{CONTACT_EMAIL}</code>.</p>

<h2>Thời gian phản hồi</h2>
<p>Tôi cố gắng đọc mọi thứ trong vòng một tuần, nhưng Toolhub được xây dựng và bảo trì vào thời gian rảnh ngoài công việc chính. Nếu có gì khẩn cấp (ví dụ bảo mật), hãy ghi vào dòng chủ đề.</p>
""".strip(),
            },
            "sk": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Maintainera Toolhub-u kontaktuj cez GitHub Issues pre bug reporty, feature requesty a nápady na nástroje — alebo e-mailom na všetko ostatné.",
                "body": f"""
<p>Toolhub je vedľajší projekt jednej osoby. Časy odpovedí v rámci možností, nie komerčný support. Kontaktný formulár tu nie je — táto stránka zámerne nemá backend.</p>

<h2>GitHub Issues</h2>
<p>Pre bug reporty, feature requesty, opravy prekladov a nápady na nové nástroje otvor prosím issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues je preferovaný kanál, lebo diskusii dáva stálu URL, ktorú neskôr nájdu aj iní s rovnakou otázkou.</p>

<h2>E-mail</h2>
<p>Na veci, čo sa nehodia do GitHub Issues — press, partnerstvo, security disclosure, takedown žiadosti — pošli e-mail na <code>{CONTACT_EMAIL}</code>.</p>

<h2>Časy odpovedí</h2>
<p>Snažím sa všetko prečítať do týždňa, ale Toolhub je stavianý a udržiavaný vo voľnom čase popri hlavnej práci. Ak je niečo urgentné (napr. security), napíš to do predmetu.</p>
""".strip(),
            },
            "cs": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Maintainera Toolhubu kontaktuj přes GitHub Issues pro bug reporty, feature requesty a nápady na nástroje — nebo e-mailem na všechno ostatní.",
                "body": f"""
<p>Toolhub je vedlejší projekt jednoho člověka. Časy odpovědí v rámci možností, ne komerční support. Kontaktní formulář tu není — tahle stránka záměrně nemá backend.</p>

<h2>GitHub Issues</h2>
<p>Pro bug reporty, feature requesty, opravy překladů a nápady na nové nástroje prosím otevři issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues je preferovaný kanál, protože diskusi dává trvalou URL, kterou později najdou i ostatní se stejnou otázkou.</p>

<h2>E-mail</h2>
<p>Na věci, co se nehodí do GitHub Issues — press, partnerství, security disclosure, takedown žádosti — pošli e-mail na <code>{CONTACT_EMAIL}</code>.</p>

<h2>Časy odpovědí</h2>
<p>Snažím se všechno přečíst do týdne, ale Toolhub se staví a udržuje ve volném čase vedle hlavní práce. Pokud je něco urgentní (např. security), napiš to do předmětu.</p>
""".strip(),
            },
            "hi": {
                "title": "संपर्क",
                "h1": "संपर्क",
                "description": "Bug रिपोर्ट, feature अनुरोध और tool के सुझावों के लिए GitHub Issues के ज़रिए Toolhub maintainer से संपर्क करें, या बाक़ी सब के लिए email द्वारा।",
                "body": f"""
<p>Toolhub एक-व्यक्ति का side project है। Best-effort जवाब का समय, कोई व्यावसायिक support नहीं। यहाँ कोई संपर्क फ़ॉर्म नहीं है — इस साइट का जानबूझकर कोई backend नहीं है।</p>

<h2>GitHub Issues</h2>
<p>Bug रिपोर्ट, feature अनुरोध, अनुवाद सुधार और नए tool के सुझावों के लिए कृपया एक issue खोलें:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues को प्राथमिकता दी जाती है क्योंकि इससे चर्चा को एक स्थायी URL मिलता है जिसे बाद में वही प्रश्न रखने वाले अन्य लोग खोज सकते हैं।</p>

<h2>Email</h2>
<p>जो विषय GitHub Issues में फ़िट नहीं होते — प्रेस, साझेदारी, security disclosure, takedown अनुरोध — उनके लिए <code>{CONTACT_EMAIL}</code> पर email भेजें।</p>

<h2>जवाब का समय</h2>
<p>मैं एक हफ़्ते के भीतर सब कुछ पढ़ने की कोशिश करता हूँ, पर Toolhub को मुख्य नौकरी के साथ-साथ खाली समय में बनाया और बनाए रखा जाता है। अगर कुछ ज़रूरी है (जैसे security), तो subject line में यह लिख दीजिए।</p>
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

{_trust_signals("en")}

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

{_trust_signals("de")}

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

{_trust_signals("es")}

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

{_trust_signals("fr")}

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

{_trust_signals("it")}

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

{_trust_signals("pt")}

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

{_trust_signals("pl")}

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

{_trust_signals("ja")}

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

{_trust_signals("nl")}

<h2>Contact voor docenten</h2>
<p>Gebruik je Toolhub in een klas en wil je het me laten weten, een tool voorstellen voor je vak, of bijdragen aan een vertaling voor een taal die we nog slecht dekken — neem dan contact op via de <a href="/contact/">contactpagina</a>. Bulk-vertaalbijdragen van native speakers — vooral voor minder bediende talen — zijn van harte welkom.</p>
""".strip(),
            },
            "tr": {
                "title": "Okullar için Toolhub",
                "h1": "Okullar için Toolhub",
                "description": "Sınıf için privacy-first geliştirici ve utility araçları. Kayıt yok, takip yok, çok dilli, self-hostable. Filtre-dostu ve öğrencilerle paylaşmak için güvenli.",
                "body": f"""
<h2>Sınıfta Toolhub</h2>
<p>Toolhub, öğrencilerin hesap oluşturmadan, takip edilmeden ve reklam veya affiliate huni'lerine yönlendirilmeden kullanabilecekleri küçük tarayıcı içi araçlar setidir. Her araç tamamen tarayıcıda çalışır, bu da bir öğrencinin yazdığının okul ağını asla terk etmediği anlamına gelir — çağrılacak bir backend yoktur.</p>
<p>İlk, orta veya yükseköğretimde ders veriyorsan ve hızla bir utility'e ihtiyacın varsa (bir regex tester, renk dönüştürücü, Base64 encoder, güvenlik dersi için parola oluşturucu), Toolhub projektöre yansıtmak ve sınıfa göndermek için güvenli olacak şekilde inşa edilmiştir.</p>

<h2>Müfredatla uyum</h2>
<ul>
<li><strong>Bilgisayar bilimi:</strong> pattern matching için <a href="/tr/regex-tester/">regex tester</a>, veri dersleri için <a href="/tr/base64-encoder/">Base64 encoder</a>, bütünlük hakkında konuşmak için <a href="/tr/hash-generator/">hash üretici</a>, ağ konuları için <a href="/tr/cidr-calculator/">CIDR hesaplayıcı</a>.</li>
<li><strong>Tasarım ve dijital medya:</strong> renk modelleri hakkında konuşmak için <a href="/tr/color-converter/">renk dönüştürücü</a> ve <a href="/tr/color-picker/">renk seçici</a>, erişilebilirlik için <a href="/tr/wcag-contrast/">WCAG kontrast denetleyici</a>.</li>
<li><strong>Güvenlik farkındalığı:</strong> entropi ve parola gücü hakkında konuşmak için <a href="/tr/password-generator/">parola üretici</a>, bir token'ın içinde gerçekten ne olduğunu göstermek için <a href="/tr/jwt-decoder/">JWT decoder</a>.</li>
<li><strong>Matematik ve sağlık:</strong> <a href="/tr/percentage-calculator/">yüzde hesaplayıcı</a>, <a href="/tr/unit-converter/">birim dönüştürücü</a> ve <a href="/tr/bmi-calculator/">BMI hesaplayıcı</a> (BMI sayfasının kendi "tıbbi tavsiye değildir" notu vardır).</li>
</ul>

<h2>Desteklenen diller</h2>
<p>Öğrencilerin ana dillerinde çalışabilmesi için her araç on dile çevrildi:</p>
<ul>
<li>English (İngilizce)</li>
<li>Deutsch (Almanca)</li>
<li>Español (İspanyolca)</li>
<li>Français (Fransızca)</li>
<li>Italiano (İtalyanca)</li>
<li>Português (Portekizce)</li>
<li>Polski (Lehçe)</li>
<li>日本語 (Japonca)</li>
<li>Nederlands (Felemenkçe)</li>
<li>Türkçe</li>
</ul>

<h2>Self-hosted seçeneği</h2>
<p>Okul ağı dış siteleri engelliyorsa veya tam kontrol istiyorsan, tüm site yaklaşık 5 MB'tır ve Progressive Web App olarak çevrimdışı çalışır. Bunu bir okul intranetinde mirror edebilirsin — servis etmek için build adımı olmadan HTML, CSS ve JavaScript içeren statik bir klasördür: dosyaları herhangi bir web sunucusunun arkasına koy.</p>
<p>Tüm kaynak <a href="{REPO_URL}">{REPO_URL}</a>\'dadır.</p>

<h2>Filtre-dostu</h2>
<p>Toolhub okul web filtreleriyle iyi çalışacak şekilde tasarlandı:</p>
<ul>
<li>Gömülü sosyal medya widget'ları yok.</li>
<li>Chat widget'ları veya canlı chat overlay'leri yok.</li>
<li>Diğer sitelere otomatik yönlendirme yok.</li>
<li>Otomatik oynatılan video veya ses yok.</li>
<li>SafeSearch-dostu içerik — yetişkin araçları yok, kumar yok, kripto affiliate yerleştirmeleri yok.</li>
</ul>

{_trust_signals("tr")}

<h2>Öğretmenler için iletişim</h2>
<p>Toolhub'ı bir sınıfta kullanıyorsan ve haberdar etmek istersen, dersine bir araç önermek istersen veya hâlâ zayıf kapsadığımız bir dil için çeviriye katkıda bulunmak istersen — <a href="/tr/contact/">iletişim sayfası</a> üzerinden ulaş. Native konuşurlardan toplu çeviri katkıları — özellikle daha az hizmet verilen diller için — sevinçle karşılanır.</p>
""".strip(),
            },
            "id": {
                "title": "Toolhub untuk Sekolah",
                "h1": "Toolhub untuk Sekolah",
                "description": "Alat developer dan utilitas yang mengutamakan privasi untuk kelas. Tanpa pendaftaran, tanpa pelacakan, multibahasa, bisa self-host. Ramah filter dan aman dibagikan ke siswa.",
                "body": f"""
<h2>Toolhub di kelas</h2>
<p>Toolhub adalah serangkaian alat kecil dalam browser yang bisa digunakan siswa tanpa membuat akun, tanpa dilacak, dan tanpa diarahkan ke corong iklan atau afiliasi. Setiap alat berjalan sepenuhnya di browser, artinya apa pun yang diketik siswa tidak pernah meninggalkan jaringan sekolah — tidak ada backend yang dipanggil.</p>
<p>Jika kamu mengajar di sekolah dasar, menengah, atau perguruan tinggi dan butuh utilitas dengan cepat (regex tester, konverter warna, encoder Base64, generator kata sandi untuk pelajaran keamanan), Toolhub dibangun supaya aman diproyeksikan dan dibagikan ke kelas.</p>

<h2>Sejajar dengan kurikulum</h2>
<ul>
<li><strong>Ilmu komputer:</strong> <a href="/id/regex-tester/">regex tester</a> untuk pattern matching, <a href="/id/base64-encoder/">Base64 encoder</a> untuk pelajaran data, <a href="/id/hash-generator/">generator hash</a> untuk membicarakan integritas, <a href="/id/cidr-calculator/">kalkulator CIDR</a> untuk topik jaringan.</li>
<li><strong>Desain dan media digital:</strong> <a href="/id/color-converter/">konverter warna</a> dan <a href="/id/color-picker/">pemilih warna</a> untuk membicarakan model warna, <a href="/id/wcag-contrast/">pemeriksa kontras WCAG</a> untuk aksesibilitas.</li>
<li><strong>Kesadaran keamanan:</strong> <a href="/id/password-generator/">generator kata sandi</a> untuk membicarakan entropi dan kekuatan kata sandi, <a href="/id/jwt-decoder/">JWT decoder</a> untuk menunjukkan apa yang sebenarnya ada di dalam token.</li>
<li><strong>Matematika dan kesehatan:</strong> <a href="/id/percentage-calculator/">kalkulator persentase</a>, <a href="/id/unit-converter/">konverter satuan</a>, dan <a href="/id/bmi-calculator/">kalkulator BMI</a> (halaman BMI punya catatan "bukan saran medis" sendiri).</li>
</ul>

<h2>Bahasa yang didukung</h2>
<p>Setiap alat diterjemahkan ke sebelas bahasa supaya siswa bisa bekerja dalam bahasa ibu mereka:</p>
<ul>
<li>English (Inggris)</li>
<li>Deutsch (Jerman)</li>
<li>Español (Spanyol)</li>
<li>Français (Prancis)</li>
<li>Italiano (Italia)</li>
<li>Português (Portugis)</li>
<li>Polski (Polandia)</li>
<li>日本語 (Jepang)</li>
<li>Nederlands (Belanda)</li>
<li>Türkçe (Turki)</li>
<li>Bahasa Indonesia</li>
</ul>

<h2>Opsi self-hosted</h2>
<p>Jika jaringan sekolah memblokir situs eksternal atau kamu ingin kontrol penuh, seluruh situs berukuran sekitar 5 MB dan berjalan offline sebagai Progressive Web App. Kamu bisa mirror di intranet sekolah — ini folder statis berisi HTML, CSS, dan JavaScript, tanpa langkah build untuk menyajikannya: letakkan file di belakang web server apa saja.</p>
<p>Seluruh source code ada di <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Ramah filter</h2>
<p>Toolhub didesain agar bermain baik dengan filter web sekolah:</p>
<ul>
<li>Tidak ada widget media sosial yang disematkan.</li>
<li>Tidak ada widget chat atau overlay chat langsung.</li>
<li>Tidak ada pengalihan otomatis ke situs lain.</li>
<li>Tidak ada video atau audio yang berjalan otomatis.</li>
<li>Konten ramah SafeSearch — tanpa alat dewasa, tanpa judi, tanpa penempatan afiliasi crypto.</li>
</ul>

{_trust_signals("id")}

<h2>Kontak untuk guru</h2>
<p>Jika kamu menggunakan Toolhub di kelas dan ingin memberi tahu, menyarankan alat untuk pelajaranmu, atau berkontribusi terjemahan untuk bahasa yang masih kami cakup buruk — hubungi melalui <a href="/id/contact/">halaman kontak</a>. Kontribusi terjemahan massal dari penutur asli — terutama untuk bahasa yang kurang terlayani — sangat diterima.</p>
""".strip(),
            },
            "vi": {
                "title": "Toolhub cho Trường học",
                "h1": "Toolhub cho Trường học",
                "description": "Công cụ dev và tiện ích ưu tiên quyền riêng tư cho lớp học. Không cần đăng ký, không theo dõi, đa ngôn ngữ, có thể tự host. Thân thiện với bộ lọc và an toàn để chia sẻ cho học sinh.",
                "body": f"""
<h2>Toolhub trong lớp học</h2>
<p>Toolhub là một bộ công cụ nhỏ trong trình duyệt mà học sinh có thể dùng mà không cần tạo tài khoản, không bị theo dõi và không bị chuyển hướng đến phễu quảng cáo hoặc affiliate. Mỗi công cụ chạy hoàn toàn trong trình duyệt, nghĩa là bất kỳ điều gì học sinh gõ không bao giờ rời khỏi mạng trường học — không có backend để gọi.</p>
<p>Nếu bạn dạy ở trường tiểu học, trung học hoặc đại học và cần một tiện ích nhanh (regex tester, bộ chuyển màu, encoder Base64, trình tạo mật khẩu cho bài học bảo mật), Toolhub được xây dựng để an toàn khi chiếu lên máy chiếu và an toàn để chia sẻ với lớp.</p>

<h2>Liên kết với chương trình</h2>
<ul>
<li><strong>Khoa học máy tính:</strong> <a href="/vi/regex-tester/">regex tester</a> cho pattern matching, <a href="/vi/base64-encoder/">Base64 encoder</a> cho bài học dữ liệu, <a href="/vi/hash-generator/">trình tạo hash</a> để nói về tính toàn vẹn, <a href="/vi/cidr-calculator/">máy tính CIDR</a> cho chủ đề mạng.</li>
<li><strong>Thiết kế và truyền thông số:</strong> <a href="/vi/color-converter/">bộ chuyển màu</a> và <a href="/vi/color-picker/">bộ chọn màu</a> để nói về mô hình màu, <a href="/vi/wcag-contrast/">kiểm tra tương phản WCAG</a> cho khả năng tiếp cận.</li>
<li><strong>Nhận thức bảo mật:</strong> <a href="/vi/password-generator/">trình tạo mật khẩu</a> để nói về entropy và độ mạnh mật khẩu, <a href="/vi/jwt-decoder/">JWT decoder</a> để cho thấy thực sự có gì bên trong một token.</li>
<li><strong>Toán và sức khỏe:</strong> <a href="/vi/percentage-calculator/">máy tính phần trăm</a>, <a href="/vi/unit-converter/">bộ chuyển đơn vị</a>, và <a href="/vi/bmi-calculator/">máy tính BMI</a> (trang BMI có thông báo "không phải lời khuyên y tế" riêng).</li>
</ul>

<h2>Ngôn ngữ được hỗ trợ</h2>
<p>Mỗi công cụ được dịch sang mười hai ngôn ngữ để học sinh có thể làm việc bằng tiếng mẹ đẻ:</p>
<ul>
<li>English (Anh)</li>
<li>Deutsch (Đức)</li>
<li>Español (Tây Ban Nha)</li>
<li>Français (Pháp)</li>
<li>Italiano (Ý)</li>
<li>Português (Bồ Đào Nha)</li>
<li>Polski (Ba Lan)</li>
<li>日本語 (Nhật)</li>
<li>Nederlands (Hà Lan)</li>
<li>Türkçe (Thổ Nhĩ Kỳ)</li>
<li>Bahasa Indonesia</li>
<li>Tiếng Việt</li>
</ul>

<h2>Tùy chọn self-host</h2>
<p>Nếu mạng trường học chặn các site ngoài hoặc bạn muốn toàn quyền kiểm soát, toàn bộ site khoảng 5 MB và hoạt động offline dưới dạng Progressive Web App. Bạn có thể mirror trên intranet trường học — đây là thư mục tĩnh gồm HTML, CSS và JavaScript, không có bước build để phục vụ: chỉ cần đặt file phía sau bất kỳ web server nào.</p>
<p>Toàn bộ source code ở <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Thân thiện với bộ lọc</h2>
<p>Toolhub được thiết kế để hoạt động tốt với bộ lọc web trường học:</p>
<ul>
<li>Không có widget mạng xã hội nhúng.</li>
<li>Không có widget chat hoặc overlay chat trực tiếp.</li>
<li>Không có chuyển hướng tự động đến site khác.</li>
<li>Không có video hoặc âm thanh tự phát.</li>
<li>Nội dung thân thiện với SafeSearch — không có công cụ người lớn, không có cờ bạc, không có quảng cáo affiliate crypto.</li>
</ul>

{_trust_signals("vi")}

<h2>Liên hệ cho giáo viên</h2>
<p>Nếu bạn dùng Toolhub trong lớp và muốn cho biết, đề xuất công cụ cho môn học của bạn, hoặc đóng góp bản dịch cho ngôn ngữ mà chúng tôi vẫn chưa cover tốt — hãy liên hệ qua <a href="/vi/contact/">trang liên hệ</a>. Đóng góp dịch hàng loạt từ người bản xứ — đặc biệt cho các ngôn ngữ ít được phục vụ — được hoan nghênh.</p>
""".strip(),
            },
            "sk": {
                "title": "Toolhub pre školy",
                "h1": "Toolhub pre školy",
                "description": "Privacy-first developer a utility nástroje do triedy. Bez registrácie, bez sledovania, viacjazyčné, self-hostable. Vhodné cez filtre a bezpečné zdieľať so žiakmi.",
                "body": f"""
<h2>Toolhub v triede</h2>
<p>Toolhub je sada malých in-browser nástrojov, ktoré žiaci môžu používať bez vytvorenia účtu, bez toho, aby boli sledovaní, a bez presmerovaní na reklamy alebo affiliate lieviky. Každý nástroj beží úplne v prehliadači, čo znamená, že vstup žiaka nikdy neopustí školskú sieť — neexistuje backend, ktorý by sa volal.</p>
<p>Ak učíš na základnej, strednej alebo vysokej škole a potrebuješ rýchly utility (regex tester, color converter, Base64 encoder, password generator na hodinu bezpečnosti), Toolhub je postavený tak, aby sa dal bezpečne hodiť na projektor a bezpečne poslať triede.</p>

<h2>Prepojenie s učebným plánom</h2>
<ul>
<li><strong>Informatika:</strong> <a href="/sk/regex-tester/">regex tester</a> na pattern matching, <a href="/sk/base64-encoder/">Base64 encoder</a> na hodiny o dátach, <a href="/sk/hash-generator/">hash generator</a> na rozhovor o integrite, <a href="/sk/cidr-calculator/">CIDR kalkulačka</a> na sieťové jednotky.</li>
<li><strong>Dizajn a digitálne médiá:</strong> <a href="/sk/color-converter/">color converter</a> a <a href="/sk/color-picker/">color picker</a> na rozhovor o farebných modeloch, <a href="/sk/wcag-contrast/">WCAG contrast checker</a> na prístupnosť.</li>
<li><strong>Bezpečnostné povedomie:</strong> <a href="/sk/password-generator/">password generator</a> na výklad entropie a sily hesiel, <a href="/sk/jwt-decoder/">JWT decoder</a>, aby si žiakom ukázal, čo je naozaj v tokene.</li>
<li><strong>Matematika a zdravie:</strong> <a href="/sk/percentage-calculator/">percentage calculator</a>, <a href="/sk/unit-converter/">unit converter</a> a <a href="/sk/bmi-calculator/">BMI calculator</a> (BMI page má vlastné upozornenie „nejde o medicínsku radu").</li>
</ul>

<h2>Podporované jazyky</h2>
<p>Každý nástroj je preložený do pätnástich jazykov, aby žiaci mohli pracovať v materinskom jazyku:</p>
<ul>
<li>English (angličtina)</li>
<li>Deutsch (nemčina)</li>
<li>Español (španielčina)</li>
<li>Français (francúzština)</li>
<li>Italiano (taliančina)</li>
<li>Português (portugalčina)</li>
<li>Polski (poľština)</li>
<li>日本語 (japončina)</li>
<li>Nederlands (holandčina)</li>
<li>Türkçe (turečtina)</li>
<li>Bahasa Indonesia (indonézština)</li>
<li>Tiếng Việt (vietnamčina)</li>
<li>हिन्दी (hindčina)</li>
<li>Slovenčina</li>
<li>Čeština (čeština)</li>
</ul>

<h2>Self-hosted varianta</h2>
<p>Ak školská sieť blokuje externé stránky alebo chceš mať plnú kontrolu, celá stránka má okolo 5 MB a funguje offline ako Progressive Web App. Môžeš ju zrkadliť na školskom intranete — je to statický priečinok HTML, CSS a JavaScriptu, žiadny build step na servovanie netreba, stačí súbory dať za ľubovoľný web server.</p>
<p>Celý zdrojový kód je na <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Priateľské k filtrom</h2>
<p>Toolhub je navrhnutý tak, aby vychádzal so školskými web filtrami:</p>
<ul>
<li>Žiadne embeddované social media widgety.</li>
<li>Žiadne chat widgety ani live-chat overlay.</li>
<li>Žiadne auto-presmerovania na iné stránky.</li>
<li>Žiadne video alebo audio, ktoré sa spustí samé.</li>
<li>Obsah priateľský k SafeSearch — žiadne adult nástroje, žiadne hazardné hry, žiadne crypto-bro affiliate placementy.</li>
</ul>

{_trust_signals("sk")}

<h2>Kontakt pre pedagógov</h2>
<p>Ak používaš Toolhub v triede a chceš mi to dať vedieť, navrhnúť nástroj pre svoj predmet alebo prispieť prekladom do jazyka, ktorý ešte dobre nepokrývame — ozvi sa cez <a href="/sk/contact/">kontaktnú stránku</a>. Hromadné prekladateľské príspevky od native speakerov — najmä pre menej obslúžené jazyky — sú veľmi vítané.</p>
""".strip(),
            },
            "cs": {
                "title": "Toolhub pro školy",
                "h1": "Toolhub pro školy",
                "description": "Privacy-first developer a utility nástroje do třídy. Bez registrace, bez sledování, vícejazyčné, self-hostable. Vhodné přes filtry a bezpečné sdílet se žáky.",
                "body": f"""
<h2>Toolhub ve třídě</h2>
<p>Toolhub je sada malých in-browser nástrojů, které žáci můžou používat bez vytvoření účtu, aniž by byli sledováni, a bez přesměrování na reklamy nebo affiliate trychtýře. Každý nástroj běží zcela v prohlížeči, což znamená, že vstup žáka nikdy neopustí školní síť — neexistuje backend, na který by se volalo.</p>
<p>Pokud učíš na základní, střední nebo vysoké škole a potřebuješ rychlý utility (regex tester, color converter, Base64 encoder, password generator na hodinu bezpečnosti), Toolhub je postaven tak, aby šel bezpečně hodit na projektor a bezpečně poslat třídě.</p>

<h2>Propojení s učebním plánem</h2>
<ul>
<li><strong>Informatika:</strong> <a href="/cs/regex-tester/">regex tester</a> na pattern matching, <a href="/cs/base64-encoder/">Base64 encoder</a> na hodiny o datech, <a href="/cs/hash-generator/">hash generator</a> na výklad integrity, <a href="/cs/cidr-calculator/">CIDR kalkulačka</a> na síťové jednotky.</li>
<li><strong>Design a digitální média:</strong> <a href="/cs/color-converter/">color converter</a> a <a href="/cs/color-picker/">color picker</a> na výklad barevných modelů, <a href="/cs/wcag-contrast/">WCAG contrast checker</a> na přístupnost.</li>
<li><strong>Bezpečnostní povědomí:</strong> <a href="/cs/password-generator/">password generator</a> na výklad entropie a síly hesel, <a href="/cs/jwt-decoder/">JWT decoder</a>, abys žákům ukázal, co je vlastně v tokenu.</li>
<li><strong>Matematika a zdraví:</strong> <a href="/cs/percentage-calculator/">percentage calculator</a>, <a href="/cs/unit-converter/">unit converter</a> a <a href="/cs/bmi-calculator/">BMI calculator</a> (BMI page má vlastní upozornění „nejde o lékařskou radu").</li>
</ul>

<h2>Podporované jazyky</h2>
<p>Každý nástroj je přeložen do patnácti jazyků, aby žáci mohli pracovat v rodném jazyce:</p>
<ul>
<li>English (angličtina)</li>
<li>Deutsch (němčina)</li>
<li>Español (španělština)</li>
<li>Français (francouzština)</li>
<li>Italiano (italština)</li>
<li>Português (portugalština)</li>
<li>Polski (polština)</li>
<li>日本語 (japonština)</li>
<li>Nederlands (nizozemština)</li>
<li>Türkçe (turečtina)</li>
<li>Bahasa Indonesia (indonéština)</li>
<li>Tiếng Việt (vietnamština)</li>
<li>हिन्दी (hindština)</li>
<li>Slovenčina (slovenština)</li>
<li>Čeština</li>
</ul>

<h2>Self-hosted varianta</h2>
<p>Pokud školní síť blokuje externí stránky nebo chceš mít plnou kontrolu, celá stránka má kolem 5 MB a funguje offline jako Progressive Web App. Můžeš ji zrcadlit na školním intranetu — je to statický adresář HTML, CSS a JavaScriptu, žádný build step pro servování netřeba, stačí soubory dát za libovolný web server.</p>
<p>Celý zdrojový kód je na <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Přátelské k filtrům</h2>
<p>Toolhub je navržen tak, aby vycházel se školními web filtry:</p>
<ul>
<li>Žádné embedované social media widgety.</li>
<li>Žádné chat widgety ani live-chat overlay.</li>
<li>Žádná auto-přesměrování na jiné stránky.</li>
<li>Žádné video nebo audio, které se spustí samo.</li>
<li>Obsah přátelský k SafeSearch — žádné adult nástroje, žádné hazardní hry, žádné crypto-bro affiliate placementy.</li>
</ul>

{_trust_signals("cs")}

<h2>Kontakt pro pedagogy</h2>
<p>Pokud používáš Toolhub ve třídě a chceš mi to dát vědět, navrhnout nástroj pro svůj předmět nebo přispět překladem do jazyka, který ještě dobře nepokrýváme — ozvi se přes <a href="/cs/contact/">kontaktní stránku</a>. Hromadné překladatelské příspěvky od native speakerů — zvlášť pro méně obsluhované jazyky — jsou velmi vítány.</p>
""".strip(),
            },
            "hi": {
                "title": "स्कूलों के लिए Toolhub",
                "h1": "स्कूलों के लिए Toolhub",
                "description": "कक्षा के लिए privacy-first developer और utility tools। साइनअप नहीं, ट्रैकिंग नहीं, बहुभाषी, self-hostable। Filter-friendly और छात्रों के साथ साझा करने के लिए सुरक्षित।",
                "body": f"""
<h2>कक्षा में Toolhub</h2>
<p>Toolhub छोटे in-browser tools का एक सेट है जिसका छात्र बिना अकाउंट बनाए, बिना ट्रैक हुए, और बिना विज्ञापन या affiliate funnels पर redirect हुए उपयोग कर सकते हैं। हर tool पूरी तरह browser में चलता है, जिसका मतलब है छात्र का input कभी स्कूल network से बाहर नहीं जाता — कोई backend है ही नहीं जिसे call किया जा सके।</p>
<p>अगर आप प्राथमिक, माध्यमिक या उच्च शिक्षा में पढ़ाते हैं और एक त्वरित utility चाहिए (regex tester, color converter, Base64 encoder, security पाठ के लिए password generator), तो Toolhub इस तरह बना है कि इसे projector पर दिखाना और कक्षा के साथ साझा करना सुरक्षित है।</p>

<h2>पाठ्यक्रम से जुड़ाव</h2>
<ul>
<li><strong>Computer science:</strong> pattern matching के लिए <a href="/hi/regex-tester/">regex tester</a>, डेटा के पाठों के लिए <a href="/hi/base64-encoder/">Base64 encoder</a>, integrity की बात के लिए <a href="/hi/hash-generator/">hash generator</a>, networking इकाइयों के लिए <a href="/hi/cidr-calculator/">CIDR calculator</a>।</li>
<li><strong>Design और digital media:</strong> color models पर चर्चा के लिए <a href="/hi/color-converter/">color converter</a> और <a href="/hi/color-picker/">color picker</a>, accessibility के लिए <a href="/hi/wcag-contrast/">WCAG contrast checker</a>।</li>
<li><strong>Security awareness:</strong> entropy और password मज़बूती की चर्चा के लिए <a href="/hi/password-generator/">password generator</a>, token के अंदर वास्तव में क्या है यह दिखाने के लिए <a href="/hi/jwt-decoder/">JWT decoder</a>।</li>
<li><strong>गणित और स्वास्थ्य:</strong> <a href="/hi/percentage-calculator/">percentage calculator</a>, <a href="/hi/unit-converter/">unit converter</a>, और <a href="/hi/bmi-calculator/">BMI calculator</a> (BMI page पर "यह चिकित्सीय सलाह नहीं है" का अपना notice है)।</li>
</ul>

<h2>समर्थित भाषाएँ</h2>
<p>हर tool तेरह भाषाओं में अनुवादित है ताकि छात्र अपनी मातृभाषा में काम कर सकें:</p>
<ul>
<li>English (अंग्रेज़ी)</li>
<li>Deutsch (जर्मन)</li>
<li>Español (स्पैनिश)</li>
<li>Français (फ़्रेंच)</li>
<li>Italiano (इतालवी)</li>
<li>Português (पुर्तगाली)</li>
<li>Polski (पोलिश)</li>
<li>日本語 (जापानी)</li>
<li>Nederlands (डच)</li>
<li>Türkçe (तुर्की)</li>
<li>Bahasa Indonesia (इंडोनेशियाई)</li>
<li>Tiếng Việt (वियतनामी)</li>
<li>हिन्दी (Hindi)</li>
</ul>

<h2>Self-hosted विकल्प</h2>
<p>अगर आपका स्कूल network बाहरी साइटों को block करता है या आप पूरा नियंत्रण चाहते हैं, तो पूरी साइट लगभग 5 MB की है और Progressive Web App के रूप में offline काम करती है। आप इसे स्कूल intranet पर mirror कर सकते हैं — यह HTML, CSS और JavaScript का एक static folder है, serve करने के लिए कोई build step ज़रूरी नहीं: बस फ़ाइलों को किसी भी web server के पीछे रख दीजिए।</p>
<p>पूरा source code <a href="{REPO_URL}">{REPO_URL}</a> पर है।</p>

<h2>Filter-friendly</h2>
<p>Toolhub को इस तरह design किया गया है कि वह स्कूल के web filters के साथ अच्छी तरह काम करे:</p>
<ul>
<li>कोई embedded social media widget नहीं।</li>
<li>कोई chat widget या live-chat overlay नहीं।</li>
<li>अन्य साइटों पर कोई auto-redirect नहीं।</li>
<li>कोई video या audio जो अपने आप चले।</li>
<li>SafeSearch-friendly सामग्री — कोई adult tools नहीं, कोई जुआ नहीं, कोई crypto affiliate placement नहीं।</li>
</ul>

{_trust_signals("hi")}

<h2>शिक्षकों के लिए संपर्क</h2>
<p>अगर आप कक्षा में Toolhub का उपयोग कर रहे हैं और मुझे बताना चाहते हैं, अपने विषय के लिए कोई tool सुझाना चाहते हैं, या किसी ऐसी भाषा के लिए अनुवाद में योगदान देना चाहते हैं जिसे हम अभी तक अच्छी तरह cover नहीं कर पाए — कृपया <a href="/hi/contact/">संपर्क page</a> के माध्यम से संपर्क करें। मूल वक्ताओं से बड़े पैमाने पर अनुवाद योगदान — विशेष रूप से कम सेवा वाली भाषाओं के लिए — बहुत स्वागत है।</p>
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
            "tr": {
                "title": "Gizlilik Politikası",
                "h1": "Gizlilik Politikası",
                "description": "Toolhub gizlilik politikası: araçlar tamamen tarayıcında çalışır, kayıt yok, hesap yok, araç verisi cihazını terk etmez. Toplu istatistik için Plausible, sadece açık onayla AdSense.",
                "body": f"""
<p><strong>Son güncelleme:</strong> {LAST_UPDATED}</p>

<h2>Kısa versiyon</h2>
<p>Araçlar tamamen tarayıcında çalışır — içine yazdığın hiçbir şey hiçbir yere gönderilmez. <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> ile toplu, anonim ziyaretler ölçeriz (cookie olmadan). Tercih edersen, cookie kullanan Google AdSense üzerinden display reklam da gösterebiliriz. Reklamları consent banner'da reddedebilirsin; sitenin geri kalanı aynı çalışır.</p>

<h2>Ne topluyoruz</h2>
<ul>
<li><strong>Araç girişi:</strong> hiçbir şey. Bir araca yapıştırdığın her şey tarayıcında kalır. Hiçbir araç sunucuya veri göndermez.</li>
<li><strong>Ziyaret istatistikleri:</strong> Plausible sayfa görüntülemelerini, referrer'ı, ülkeyi ve cihaz türünü sayar — anonim, toplu, cookie olmadan. <a href="https://plausible.io/data-policy" rel="noopener">Plausible'ın veri politikası</a> ne topladıklarını ve toplamadıklarını açıklar.</li>
<li><strong>Reklamları kabul edersen:</strong> Google AdSense cookie yerleştirir ve reklamları kişiselleştirmek için bunları kullanabilir. Google'ın uygulamaları <a href="https://policies.google.com/technologies/ads" rel="noopener">Google\'ın reklam gizlilik politikasına</a> tabidir.</li>
<li><strong>Reklamları reddedersen:</strong> reklam scriptleri yüklenmez, reklam cookie'leri yerleştirilmez ve reklam blokları sayfadan kaybolur.</li>
</ul>

<h2>Cookie'ler</h2>
<p>Site reklam tercihini hatırlamak için bir localStorage girişi (<code>toolhub:consent</code>) artı koyu/açık tercihin için bir <code>theme</code> girişi kullanır. Hiçbiri tarayıcını terk etmez.</p>
<p>Plausible cookie kullanmaz. Google AdSense <em>sadece</em> kabul edersen cookie kullanır — footer'daki consent linki üzerinden seçimini her zaman değiştirebilirsin.</p>

<h2>Harici servisler</h2>
<ul>
<li><strong>Plausible Analytics</strong> — gizlilik dostu, GDPR uyumlu, EU barındırmalı. Kişisel veri yok.</li>
<li><strong>Google AdSense</strong> — sadece açık onayla. <code>pagead2.googlesyndication.com</code>'u yükler ve reklam cookie'leri yerleştirebilir.</li>
<li><strong>GitHub Pages</strong> — site host'u. GitHub varsayılan olarak <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">gizlilik beyanlarına</a> göre sunucu logları (IP, timestamp, URL) tutar.</li>
<li><strong>YouTube Thumbnail aracı</strong> — özellikle bu aracı kullanırsan, tarayıcın görseli doğrudan <code>i.ytimg.com</code> (YouTube\'un CDN'i) üzerinden çeker. Kimlik doğrulama yok, upload yok. Detaylar <a href="/tr/how-we-handle-your-data/">veri işleme</a>\'de.</li>
</ul>

<h2>Affiliate linkleri</h2>
<p>Footer'daki bazı linkler affiliate linklerdir — tıklarsan ve önerilen bir servise kayıt olursan (örneğin hosting sağlayıcıları), Toolhub komisyon kazanabilir. Senin ödediğin fiyat değişmez. Affiliate linkler <code>rel="sponsored"</code> ile işaretlenir. Tam liste <a href="/tr/affiliate-disclosure/">affiliate bildirimi</a>\'nde.</p>

<h2>Haklarınız</h2>
<p>GDPR / UK GDPR / CCPA / Slovak gizlilik yasası altında, hakkında tuttuğumuz kişisel verilerin erişimini veya silinmesini talep edebilirsin. Hiçbir şey saklamıyoruz — backend yok, hesap yok, kullanıcı veritabanı yok. Plausible sadece toplu ziyaret verisi saklar. Google\'ın reklam verisi kendi istek kanalları üzerinden gider.</p>

<h2>İletişim</h2>
<p>Bu politika hakkında sorular? <a href="/tr/contact/">İletişim sayfası</a> üzerinden ulaş veya <a href="{REPO_URL}">{REPO_URL}</a> üzerinde bir issue aç.</p>
""".strip(),
            },
            "id": {
                "title": "Kebijakan Privasi",
                "h1": "Kebijakan Privasi",
                "description": "Kebijakan privasi Toolhub: alat berjalan sepenuhnya di browser, tanpa pendaftaran, tanpa akun, data alat tidak meninggalkan perangkatmu. Plausible untuk statistik agregat, AdSense hanya dengan persetujuan eksplisit.",
                "body": f"""
<p><strong>Terakhir diperbarui:</strong> {LAST_UPDATED}</p>

<h2>Versi singkat</h2>
<p>Alat berjalan sepenuhnya di browser-mu — apa pun yang kamu ketik di dalamnya tidak dikirim ke mana pun. Kami mengukur kunjungan secara agregat dan anonim dengan <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (tanpa cookie). Jika kamu memilih, kami juga bisa menampilkan iklan display melalui Google AdSense yang menggunakan cookie. Kamu bisa menolak iklan di banner persetujuan; sisa situs bekerja sama saja.</p>

<h2>Apa yang kami kumpulkan</h2>
<ul>
<li><strong>Input alat:</strong> tidak ada. Apa pun yang kamu tempel ke sebuah alat tetap di browser-mu. Tidak ada alat yang mengirim data ke server.</li>
<li><strong>Statistik kunjungan:</strong> Plausible menghitung tampilan halaman, referrer, negara, dan tipe perangkat — anonim, agregat, tanpa cookie. <a href="https://plausible.io/data-policy" rel="noopener">Kebijakan data Plausible</a> menjelaskan apa yang mereka kumpulkan dan tidak.</li>
<li><strong>Jika kamu menerima iklan:</strong> Google AdSense menempatkan cookie dan bisa menggunakannya untuk mempersonalisasi iklan. Praktik Google tunduk pada <a href="https://policies.google.com/technologies/ads" rel="noopener">kebijakan privasi iklan Google</a>.</li>
<li><strong>Jika kamu menolak iklan:</strong> skrip iklan tidak dimuat, cookie iklan tidak ditempatkan, dan blok iklan menghilang dari halaman.</li>
</ul>

<h2>Cookie</h2>
<p>Situs ini menggunakan satu entri localStorage (<code>toolhub:consent</code>) untuk mengingat preferensi iklanmu, plus entri <code>theme</code> untuk preferensi gelap/terang. Tidak ada yang meninggalkan browser-mu.</p>
<p>Plausible tidak menggunakan cookie. Google AdSense menggunakan cookie <em>hanya</em> jika kamu menerima — kamu selalu bisa mengubah pilihanmu via tautan persetujuan di footer.</p>

<h2>Layanan eksternal</h2>
<ul>
<li><strong>Plausible Analytics</strong> — ramah privasi, sesuai GDPR, di-host di EU. Tanpa data pribadi.</li>
<li><strong>Google AdSense</strong> — hanya dengan persetujuan eksplisit. Memuat <code>pagead2.googlesyndication.com</code> dan bisa menempatkan cookie iklan.</li>
<li><strong>GitHub Pages</strong> — host situs. GitHub secara default menyimpan log server (IP, timestamp, URL) sesuai <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">pernyataan privasinya</a>.</li>
<li><strong>Alat YouTube Thumbnail</strong> — khusus jika kamu menggunakan alat ini, browser-mu mengambil gambar langsung dari <code>i.ytimg.com</code> (CDN YouTube). Tanpa otentikasi, tanpa upload. Detail di <a href="/id/how-we-handle-your-data/">penanganan data</a>.</li>
</ul>

<h2>Tautan afiliasi</h2>
<p>Beberapa tautan di footer adalah tautan afiliasi — jika kamu mengklik dan mendaftar ke layanan yang direkomendasikan (misalnya penyedia hosting), Toolhub bisa mendapat komisi. Harga yang kamu bayar tidak berubah. Tautan afiliasi ditandai dengan <code>rel="sponsored"</code>. Daftar lengkap di <a href="/id/affiliate-disclosure/">pengungkapan afiliasi</a>.</p>

<h2>Hak kamu</h2>
<p>Berdasarkan GDPR / UK GDPR / CCPA / undang-undang privasi Slovakia, kamu bisa meminta akses atau penghapusan data pribadi yang kami simpan tentangmu. Kami tidak menyimpan apa-apa — tanpa backend, tanpa akun, tanpa database pengguna. Plausible hanya menyimpan data kunjungan agregat. Data iklan Google melalui saluran permintaan mereka sendiri.</p>

<h2>Kontak</h2>
<p>Pertanyaan tentang kebijakan ini? Hubungi via <a href="/id/contact/">halaman kontak</a> atau buka issue di <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "vi": {
                "title": "Chính sách bảo mật",
                "h1": "Chính sách bảo mật",
                "description": "Chính sách bảo mật của Toolhub: công cụ chạy hoàn toàn trong trình duyệt, không cần đăng ký, không có tài khoản, dữ liệu công cụ không rời khỏi thiết bị của bạn. Plausible cho thống kê tổng hợp, AdSense chỉ với sự đồng ý rõ ràng.",
                "body": f"""
<p><strong>Cập nhật lần cuối:</strong> {LAST_UPDATED}</p>

<h2>Phiên bản ngắn</h2>
<p>Công cụ chạy hoàn toàn trong trình duyệt của bạn — bất cứ điều gì bạn gõ vào chúng đều không được gửi đi đâu cả. Chúng tôi đo lường lượt truy cập một cách tổng hợp và ẩn danh bằng <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (không có cookie). Nếu bạn chọn, chúng tôi cũng có thể hiển thị quảng cáo display thông qua Google AdSense vốn sử dụng cookie. Bạn có thể từ chối quảng cáo ở banner đồng ý; phần còn lại của site hoạt động như nhau.</p>

<h2>Những gì chúng tôi thu thập</h2>
<ul>
<li><strong>Input công cụ:</strong> không gì cả. Bất cứ điều gì bạn dán vào một công cụ đều ở lại trong trình duyệt của bạn. Không có công cụ nào gửi dữ liệu lên server.</li>
<li><strong>Thống kê lượt truy cập:</strong> Plausible đếm lượt xem trang, referrer, quốc gia, và loại thiết bị — ẩn danh, tổng hợp, không cookie. <a href="https://plausible.io/data-policy" rel="noopener">Chính sách dữ liệu của Plausible</a> giải thích chính xác họ thu thập và không thu thập gì.</li>
<li><strong>Nếu bạn chấp nhận quảng cáo:</strong> Google AdSense đặt cookie và có thể dùng chúng để cá nhân hóa quảng cáo. Hoạt động của Google tuân theo <a href="https://policies.google.com/technologies/ads" rel="noopener">chính sách quyền riêng tư về quảng cáo của Google</a>.</li>
<li><strong>Nếu bạn từ chối quảng cáo:</strong> script quảng cáo không tải, cookie quảng cáo không được đặt, và các block quảng cáo biến mất khỏi trang.</li>
</ul>

<h2>Cookie</h2>
<p>Site này dùng một entry localStorage (<code>toolhub:consent</code>) để ghi nhớ tùy chọn quảng cáo của bạn, cộng với một entry <code>theme</code> cho tùy chọn dark/light. Không có gì rời khỏi trình duyệt của bạn.</p>
<p>Plausible không dùng cookie. Google AdSense dùng cookie <em>chỉ</em> khi bạn chấp nhận — bạn luôn có thể thay đổi lựa chọn của mình qua link đồng ý ở footer.</p>

<h2>Dịch vụ bên ngoài</h2>
<ul>
<li><strong>Plausible Analytics</strong> — thân thiện quyền riêng tư, tuân thủ GDPR, host ở EU. Không có dữ liệu cá nhân.</li>
<li><strong>Google AdSense</strong> — chỉ khi có sự đồng ý rõ ràng. Tải <code>pagead2.googlesyndication.com</code> và có thể đặt cookie quảng cáo.</li>
<li><strong>GitHub Pages</strong> — host site. GitHub mặc định lưu trữ log server (IP, timestamp, URL) theo <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">tuyên bố bảo mật</a> của họ.</li>
<li><strong>Công cụ YouTube Thumbnail</strong> — riêng nếu bạn dùng công cụ này, trình duyệt của bạn fetch ảnh trực tiếp từ <code>i.ytimg.com</code> (CDN của YouTube). Không có xác thực, không có upload. Chi tiết ở <a href="/vi/how-we-handle-your-data/">xử lý dữ liệu</a>.</li>
</ul>

<h2>Link affiliate</h2>
<p>Một số link ở footer là link affiliate — nếu bạn click và đăng ký dịch vụ được giới thiệu (ví dụ nhà cung cấp hosting), Toolhub có thể nhận hoa hồng nhỏ. Giá bạn trả không thay đổi. Link affiliate được đánh dấu bằng <code>rel="sponsored"</code>. Danh sách đầy đủ ở <a href="/vi/affiliate-disclosure/">tiết lộ affiliate</a>.</p>

<h2>Quyền của bạn</h2>
<p>Theo GDPR / UK GDPR / CCPA / luật bảo mật Slovakia, bạn có thể yêu cầu truy cập hoặc xóa dữ liệu cá nhân mà chúng tôi giữ về bạn. Chúng tôi không giữ gì cả — không có backend, không có tài khoản, không có database người dùng. Plausible chỉ lưu dữ liệu lượt truy cập tổng hợp. Dữ liệu quảng cáo của Google đi qua kênh yêu cầu riêng của họ.</p>

<h2>Liên hệ</h2>
<p>Câu hỏi về chính sách này? Liên hệ qua <a href="/vi/contact/">trang liên hệ</a> hoặc mở issue ở <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "sk": {
                "title": "Zásady ochrany súkromia",
                "h1": "Zásady ochrany súkromia",
                "description": "Zásady súkromia Toolhub: nástroje bežia úplne v tvojom prehliadači, bez registrácie, bez účtov, žiadne dáta z nástrojov neopúšťajú tvoje zariadenie. Plausible na agregované analytiky, AdSense iba s výslovným súhlasom.",
                "body": f"""
<p><strong>Naposledy aktualizované:</strong> {LAST_UPDATED}</p>

<h2>Krátka verzia</h2>
<p>Nástroje bežia úplne v tvojom prehliadači — nič, čo do nich napíšeš, sa nikam neodošle. Anonymné agregované návštevy meriame cez <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (bez cookies). Ak sa rozhodneš opt-in, môžeme zobrazovať display reklamy cez Google AdSense, ktorý cookies používa. Reklamy môžeš odmietnuť pri consent banneri; zvyšok stránky funguje rovnako tak či tak.</p>

<h2>Čo zbierame</h2>
<ul>
<li><strong>Vstupy do nástrojov:</strong> nič. Všetko, čo vložíš do nástroja, zostáva v tvojom prehliadači. Žiaden nástroj neposiela dáta na server.</li>
<li><strong>Návštevné analytiky:</strong> Plausible počíta page views, referrer, krajinu a typ zariadenia — anonymne, v agregáte, bez cookies. <a href="https://plausible.io/data-policy" rel="noopener">Plausible data policy</a> pokrýva, čo zbierajú a čo nie.</li>
<li><strong>Ak akceptuješ reklamy:</strong> Google AdSense nastavuje cookies a môže ich používať na personalizáciu reklám. Praktiky Google sa riadia <a href="https://policies.google.com/technologies/ads" rel="noopener">Google advertising privacy policy</a>.</li>
<li><strong>Ak reklamy odmietneš:</strong> nenahrávajú sa žiadne reklamné skripty, nenastavujú sa reklamné cookies, ad sloty sa zo stránky odstránia.</li>
</ul>

<h2>Cookies</h2>
<p>Samotná stránka používa jeden localStorage záznam (<code>toolhub:consent</code>) na zapamätanie tvojho rozhodnutia ohľadom reklám, plus záznam <code>theme</code> pre tvoju preferenciu dark/light. Ani jedno neopúšťa tvoj prehliadač.</p>
<p>Plausible nepoužíva žiadne cookies. Google AdSense používa cookies <em>iba ak</em> ich akceptuješ — rozhodnutie môžeš kedykoľvek zmeniť cez consent odkaz v päte.</p>

<h2>Third-party služby</h2>
<ul>
<li><strong>Plausible Analytics</strong> — privacy-friendly, GDPR-compliant, EU-hosted. Žiadne osobné dáta sa nezbierajú.</li>
<li><strong>Google AdSense</strong> — používa sa iba s výslovným súhlasom. Načítava <code>pagead2.googlesyndication.com</code> a môže nastaviť reklamné cookies.</li>
<li><strong>GitHub Pages</strong> — hosting stránky. Štandardné server logy (IP, timestamp, URL) si GitHub uchováva podľa svojho <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">privacy statementu</a>.</li>
<li><strong>Nástroj YouTube Thumbnail</strong> — keď použiješ konkrétne tento nástroj, tvoj prehliadač si načíta obrázok priamo z <code>i.ytimg.com</code> (YouTube CDN). Bez autentifikácie, bez uploadu. Detail v <a href="/sk/how-we-handle-your-data/">spracovaní údajov</a>.</li>
</ul>

<h2>Affiliate odkazy</h2>
<p>Niektoré odkazy v päte sú affiliate — ak cez ne klikneš a zaregistruješ sa do služby, ktorú odporúčame (napr. hostingu), Toolhub môže dostať referral. Cena, ktorú platíš, sa nemení. Affiliate odkazy sú označené <code>rel="sponsored"</code>. Plný zoznam v <a href="/sk/affiliate-disclosure/">affiliate disclosure</a>.</p>

<h2>Tvoje práva</h2>
<p>Podľa GDPR / UK GDPR / CCPA / slovenského zákona o ochrane osobných údajov môžeš žiadať prístup alebo vymazanie akýchkoľvek osobných údajov, ktoré o tebe máme. Nemáme žiadne — neexistuje backend, žiadne účty, žiadna user databáza. Plausible drží len agregované návštevné dáta. Reklamné dáta Google sa riadia ich vlastnými kanálmi pre žiadosti.</p>

<h2>Kontakt</h2>
<p>Otázky k týmto zásadám? Ozvi sa cez <a href="/sk/contact/">kontaktnú stránku</a> alebo otvor issue na <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "cs": {
                "title": "Zásady ochrany soukromí",
                "h1": "Zásady ochrany soukromí",
                "description": "Zásady soukromí Toolhubu: nástroje běží zcela v tvém prohlížeči, bez registrace, bez účtů, žádná data z nástrojů neopouštějí tvé zařízení. Plausible na agregovanou analytiku, AdSense pouze s výslovným souhlasem.",
                "body": f"""
<p><strong>Naposledy aktualizováno:</strong> {LAST_UPDATED}</p>

<h2>Krátká verze</h2>
<p>Nástroje běží zcela v tvém prohlížeči — nic, co do nich napíšeš, se nikam neodesílá. Anonymní agregované návštěvy měříme přes <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> (bez cookies). Pokud si vybereš opt-in, můžeme zobrazovat display reklamy přes Google AdSense, který cookies používá. Reklamy můžeš odmítnout na consent banneru; zbytek stránky funguje stejně tak jako tak.</p>

<h2>Co sbíráme</h2>
<ul>
<li><strong>Vstupy do nástrojů:</strong> nic. Vše, co vložíš do nástroje, zůstává v tvém prohlížeči. Žádný nástroj neposílá data na server.</li>
<li><strong>Návštěvní analytika:</strong> Plausible počítá page views, referrer, zemi a typ zařízení — anonymně, v agregátu, bez cookies. <a href="https://plausible.io/data-policy" rel="noopener">Data policy Plausible</a> pokrývá, co sbírají a co ne.</li>
<li><strong>Pokud reklamy přijmeš:</strong> Google AdSense nastavuje cookies a může je používat k personalizaci reklam. Praktiky Google se řídí <a href="https://policies.google.com/technologies/ads" rel="noopener">Google advertising privacy policy</a>.</li>
<li><strong>Pokud reklamy odmítneš:</strong> nenahrávají se žádné reklamní skripty, nenastavují se reklamní cookies, ad sloty se ze stránky odstraní.</li>
</ul>

<h2>Cookies</h2>
<p>Stránka sama používá jeden localStorage záznam (<code>toolhub:consent</code>) k zapamatování tvého rozhodnutí ohledně reklam, plus záznam <code>theme</code> pro tvou preferenci dark/light. Ani jedno neopouští tvůj prohlížeč.</p>
<p>Plausible nepoužívá žádné cookies. Google AdSense používá cookies <em>jen pokud</em> je přijmeš — rozhodnutí můžeš kdykoli změnit přes consent odkaz v patičce.</p>

<h2>Third-party služby</h2>
<ul>
<li><strong>Plausible Analytics</strong> — privacy-friendly, GDPR-compliant, EU-hosted. Žádná osobní data se nesbírají.</li>
<li><strong>Google AdSense</strong> — používá se pouze s výslovným souhlasem. Načítá <code>pagead2.googlesyndication.com</code> a může nastavit reklamní cookies.</li>
<li><strong>GitHub Pages</strong> — hosting stránky. Standardní server logy (IP, timestamp, URL) si GitHub uchovává podle svého <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">privacy statementu</a>.</li>
<li><strong>Nástroj YouTube Thumbnail</strong> — když použiješ zrovna tento nástroj, tvůj prohlížeč si stáhne obrázek přímo z <code>i.ytimg.com</code> (YouTube CDN). Bez autentifikace, bez uploadu. Detail v <a href="/cs/how-we-handle-your-data/">zpracování dat</a>.</li>
</ul>

<h2>Affiliate odkazy</h2>
<p>Některé odkazy v patičce jsou affiliate — pokud na ně klikneš a zaregistruješ se k službě, kterou doporučujeme (např. hostingu), Toolhub může dostat referral. Cena, kterou platíš, se nemění. Affiliate odkazy jsou označeny <code>rel="sponsored"</code>. Úplný seznam v <a href="/cs/affiliate-disclosure/">affiliate disclosure</a>.</p>

<h2>Tvá práva</h2>
<p>Podle GDPR / UK GDPR / CCPA / českého zákona o ochraně osobních údajů můžeš žádat přístup k jakýmkoli osobním údajům, které o tobě máme, nebo jejich vymazání. Nemáme žádné — neexistuje backend, žádné účty, žádná uživatelská databáze. Plausible drží jen agregovaná návštěvní data. Reklamní data Google se řídí jejich vlastními kanály pro žádosti.</p>

<h2>Kontakt</h2>
<p>Otázky k těmto zásadám? Ozvi se přes <a href="/cs/contact/">kontaktní stránku</a> nebo otevři issue na <a href="{REPO_URL}">{REPO_URL}</a>.</p>
""".strip(),
            },
            "hi": {
                "title": "गोपनीयता नीति",
                "h1": "गोपनीयता नीति",
                "description": "Toolhub गोपनीयता नीति: tools पूरी तरह आपके browser में चलते हैं, साइनअप नहीं, अकाउंट नहीं, कोई tool डेटा आपके device से बाहर नहीं जाता। समग्र analytics के लिए Plausible, स्पष्ट सहमति पर ही AdSense।",
                "body": f"""
<p><strong>अंतिम बार अद्यतन:</strong> {LAST_UPDATED}</p>

<h2>संक्षिप्त संस्करण</h2>
<p>Tools पूरी तरह आपके browser में चलते हैं — आप उनमें जो भी टाइप करते हैं वह कहीं नहीं भेजा जाता। हम <a href="https://plausible.io/data-policy" rel="noopener">Plausible Analytics</a> के साथ समग्र, अनाम विज़िट गिनते हैं (cookies नहीं)। अगर आप opt-in करना चुनते हैं, तो हम Google AdSense के माध्यम से display विज्ञापन भी दिखा सकते हैं, जो cookies का उपयोग करता है। आप consent banner पर विज्ञापन अस्वीकार कर सकते हैं; बाकी साइट दोनों ही स्थितियों में समान रूप से काम करती है।</p>

<h2>हम क्या एकत्र करते हैं</h2>
<ul>
<li><strong>Tool inputs:</strong> कुछ नहीं। आप जो भी किसी tool में paste करते हैं वह आपके browser में ही रहता है। कोई भी tool server को डेटा नहीं भेजता।</li>
<li><strong>विज़िट analytics:</strong> Plausible page views, referrer, देश, और device प्रकार गिनता है — अनाम रूप से, समग्र रूप में, cookies के बिना। <a href="https://plausible.io/data-policy" rel="noopener">Plausible की data policy</a> बताती है कि वे क्या एकत्र करते हैं और क्या नहीं।</li>
<li><strong>अगर आप विज्ञापन स्वीकार करते हैं:</strong> Google AdSense cookies set करता है और उनका उपयोग विज्ञापनों को personalize करने के लिए कर सकता है। Google की प्रथाएँ <a href="https://policies.google.com/technologies/ads" rel="noopener">Google की विज्ञापन गोपनीयता नीति</a> के तहत आती हैं।</li>
<li><strong>अगर आप विज्ञापन अस्वीकार करते हैं:</strong> कोई विज्ञापन script load नहीं होती, कोई विज्ञापन cookie set नहीं होती, page से विज्ञापन slots हटा दिए जाते हैं।</li>
</ul>

<h2>Cookies</h2>
<p>साइट स्वयं एक localStorage entry (<code>toolhub:consent</code>) का उपयोग आपकी विज्ञापन-सहमति के निर्णय को याद रखने के लिए करती है, साथ ही आपकी dark/light वरीयता के लिए एक <code>theme</code> entry। दोनों आपके browser से बाहर नहीं जाते।</p>
<p>Plausible कोई cookies उपयोग नहीं करता। Google AdSense cookies <em>केवल तभी</em> उपयोग करता है जब आप उन्हें स्वीकार करते हैं — आप footer में consent link के माध्यम से किसी भी समय अपना निर्णय बदल सकते हैं।</p>

<h2>तृतीय-पक्ष सेवाएँ</h2>
<ul>
<li><strong>Plausible Analytics</strong> — privacy-friendly, GDPR-compliant, EU-hosted। कोई व्यक्तिगत डेटा एकत्र नहीं।</li>
<li><strong>Google AdSense</strong> — केवल स्पष्ट सहमति के साथ। <code>pagead2.googlesyndication.com</code> load करता है और विज्ञापन cookies set कर सकता है।</li>
<li><strong>GitHub Pages</strong> — साइट host। मानक server logs (IP, timestamp, URL) GitHub द्वारा अपनी <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" rel="noopener">गोपनीयता वक्तव्य</a> के अनुसार रखे जाते हैं।</li>
<li><strong>YouTube Thumbnail tool</strong> — जब आप विशेष रूप से इस एक tool का उपयोग करते हैं, तो आपका browser सीधे <code>i.ytimg.com</code> (YouTube के CDN) से एक image fetch करता है। कोई प्रमाणीकरण नहीं, कोई upload नहीं। विवरण के लिए <a href="/hi/how-we-handle-your-data/">data handling</a> देखें।</li>
</ul>

<h2>Affiliate links</h2>
<p>Footer के कुछ links affiliate links हैं — अगर आप उनके माध्यम से click करते हैं और हमारे द्वारा सुझाई गई सेवा (जैसे hosting providers) के लिए sign up करते हैं, तो Toolhub को एक referral मिल सकता है। आप जो क़ीमत चुकाते हैं वह नहीं बदलती। Affiliate links <code>rel="sponsored"</code> से tag किए जाते हैं। पूरी सूची के लिए <a href="/hi/affiliate-disclosure/">affiliate disclosure</a> देखें।</p>

<h2>आपके अधिकार</h2>
<p>GDPR / UK GDPR / CCPA / Slovak DPA के तहत, आप अपने पास रखे गए किसी भी व्यक्तिगत डेटा तक पहुँच या उसे हटाने का अनुरोध कर सकते हैं। हमारे पास कोई नहीं है — कोई backend नहीं, कोई अकाउंट नहीं, कोई user database नहीं। Plausible केवल समग्र विज़िट डेटा रखता है। Google का विज्ञापन डेटा उनके अपने अनुरोध माध्यमों द्वारा नियंत्रित होता है।</p>

<h2>संपर्क</h2>
<p>इस नीति के बारे में प्रश्न? <a href="/hi/contact/">संपर्क page</a> के माध्यम से पहुँचें या <a href="{REPO_URL}">{REPO_URL}</a> पर एक issue खोलें।</p>
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
            "tr": {
                "title": "Verilerini nasıl işliyoruz",
                "h1": "Verilerini nasıl işliyoruz",
                "description": "Toolhub'ın verilerini tam olarak nasıl işlediğinin sade bir dilde açıklaması. Araçlar tarayıcında çalışır, hiçbir şey saklanmaz, üç istisna açıkça adlandırılır.",
                "body": f"""
<p><strong>Son güncelleme:</strong> {LAST_UPDATED}</p>
<p>Bu sayfa sade dildeki versiyondur. <a href="/tr/privacy/">Gizlilik politikasını</a> tamamlar; bir yerde çelişiyorlarsa, bu sayfa daha spesifik olandır ve geçerlidir.</p>

<h2>Veriler nereye gider</h2>
<p>Toolhub'daki araçlar tarayıcında çalışır. Bir araca yapıştırdığın, yazdığın veya yüklediğin şey cihazında kalır — sunucu tarafı araç yürütücüsü yoktur ve araçların arkasında upload endpoint'i yoktur.</p>
<p>"Hiçbir şey cihazını terk etmez"e tam olarak üç açıkça adlandırılmış istisna vardır:</p>
<ol>
<li><strong>YouTube Thumbnail aracı</strong> — bir YouTube URL'i gönderdiğinde, tarayıcın thumbnail'i doğrudan <code>i.ytimg.com</code>'dan (YouTube\'un görseller için public CDN'i) çeker. Kimlik doğrulama yok, upload yok, API anahtarı yok. YouTube sadece URL'den video ID'sini görür ve sadece tarayıcın istediği için.</li>
<li><strong>AdSense (sadece etkinleştirildiğinde ve onayla)</strong> — Google'ın display reklam sistemi. Onayla, Google IP adresini görebilir ve Google'ın politikalarına göre cookie yerleştirebilir. Reddedildiğinde (varsayılan), AdSense hiç yüklenmez.</li>
<li><strong>Plausible Analytics</strong> — sayfa ziyaretlerini, referrer'ı, ülkeyi ve cihaz sınıfını sayar. Cookie yok, fingerprinting yok, sadece toplu istatistik. Plausible'ın sunucuları EU'dadır.</li>
</ol>

<h2>Ne sakladığımız</h2>
<p>Senin hakkında hiçbir şey. Hesap yok, kullanıcı ID'leri yok, e-posta yok, profil yok. Araçlara koyduğun içeriği saklamayız.</p>
<p>Tarayıcın yalnızca kendi cihazında iki küçük localStorage girişi tutar — her ikisi de tarayıcının developer tool'ları üzerinden okunabilir ve silinebilir:</p>
<ul>
<li><code>theme</code> — "light" veya "dark", yaklaşık bir byte tercih.</li>
<li><code>toolhub:consent</code> — reklam tercihin (evet/hayır/belirsiz). Sana tekrar sormamak için.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA ve Slovak DPA</h2>
<p>Toolhub minimal veri işler:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (EU barındırmalı) uyumlu bir analitik temeli sağlar. AdSense aktif olduğunda, Google TCF v2 altında kendi consent katmanını yürütür.</li>
<li><strong>Kaliforniya (CCPA):</strong> kişisel veri satmıyoruz. Satacak kişisel verimiz yok.</li>
<li><strong>Slovakya (Slovak veri koruma otoritesi):</strong> Toolhub'ın maintainer'ı Slovakya'dadır. Slovak kuralları fiilen gerçekleşen herhangi bir işlemeye uygulanır — ki pratikte Plausible'ın toplu ölçümlerine ve (etkinleştirildiğinde) AdSense'in kendi consent akışına iner.</li>
</ul>
<p>Kişisel verilerin erişimi veya silinmesi hakları pratikte uygulanamaz çünkü erişilecek veya silinecek hiçbir kişisel veri saklanmaz. Spesifik sorular için <a href="/tr/contact/">iletişim sayfası</a> üzerinden e-posta gönder.</p>

<h2>Cookie'ler</h2>
<ul>
<li><strong>Plausible:</strong> cookie yok, asla.</li>
<li><strong>Tema tercihi:</strong> bir localStorage girişi, cookie değil. Cihazında kalır. HTTP isteklerine eklenmez.</li>
<li><strong>AdSense (etkinse):</strong> Google kendi üçüncü taraf reklam cookie'lerini yerleştirir. Consent banner herhangi bir AdSense scripti yüklenmeden önce görünür ve reddedersen AdSense hiç yüklenmez.</li>
</ul>

<h2>Çocuklar</h2>
<p>Toolhub okul dostudur (<a href="/tr/for-schools/">Okullar için Toolhub</a>'a bak). Davranışsal takip yok, hedefli reklamlar yok. 13 yaş altı kullanım bölgeye göre AdSense koşulları içinde kabul edilebilirdir — AdSense'in bölgesel olarak çocuklara yönelik reklamı sınırladığı yerlerde, bu sınırlar Google'ın kendi sistemleri tarafından uygulanır.</p>

<h2>İndirilebilir PDF</h2>
<p>Bu sayfanın çevrimdışı kullanım için veya bir okulun IT belgelerinin parçası olarak yazdırılması için bir PDF versiyonu mevcuttur:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF şu anda sadece İngilizcedir; dil başına PDF'ler bu sürümün kapsamı dışındadır.</p>

<h2>Sorular</h2>
<p>Burada bir şey net değilse, <a href="{REPO_URL}">{REPO_URL}</a> üzerinde bir issue aç veya <a href="/tr/contact/">iletişim sayfası</a>\'nı kullan. Açıklayıcı sorular bu sayfayı sonraki okuyucu için daha iyi yapmanın iyi bir yoludur.</p>
""".strip(),
            },
            "id": {
                "title": "Bagaimana kami menangani datamu",
                "h1": "Bagaimana kami menangani datamu",
                "description": "Penjelasan bahasa polos tentang bagaimana Toolhub menangani datamu. Alat berjalan di browser, tidak ada yang disimpan, tiga pengecualian disebut secara eksplisit.",
                "body": f"""
<p><strong>Terakhir diperbarui:</strong> {LAST_UPDATED}</p>
<p>Halaman ini adalah versi bahasa polos. Ini melengkapi <a href="/id/privacy/">kebijakan privasi</a>; jika keduanya bertentangan di suatu tempat, halaman ini lebih spesifik dan yang berlaku.</p>

<h2>Ke mana data pergi</h2>
<p>Alat di Toolhub berjalan di browser-mu. Apa pun yang kamu tempel, ketik, atau unggah ke sebuah alat tetap di perangkatmu — tidak ada eksekutor alat sisi server, dan tidak ada endpoint upload di balik alat.</p>
<p>Ada tepat tiga pengecualian yang disebut eksplisit terhadap "tidak ada yang meninggalkan perangkatmu":</p>
<ol>
<li><strong>Alat YouTube Thumbnail</strong> — ketika kamu mengirimkan URL YouTube, browser-mu mengambil thumbnail langsung dari <code>i.ytimg.com</code> (CDN publik YouTube untuk gambar). Tanpa otentikasi, tanpa upload, tanpa kunci API. YouTube hanya melihat video ID dari URL, dan hanya karena browser-mu memintanya.</li>
<li><strong>AdSense (hanya ketika diaktifkan dan dengan persetujuan)</strong> — sistem iklan display Google. Dengan persetujuan, Google bisa melihat alamat IP-mu dan menempatkan cookie sesuai kebijakannya. Ketika ditolak (default), AdSense tidak dimuat sama sekali.</li>
<li><strong>Plausible Analytics</strong> — menghitung kunjungan halaman, referrer, negara, dan kelas perangkat. Tanpa cookie, tanpa fingerprinting, hanya statistik agregat. Server Plausible ada di EU.</li>
</ol>

<h2>Apa yang kami simpan</h2>
<p>Tidak ada tentangmu. Tanpa akun, tanpa ID pengguna, tanpa email, tanpa profil. Kami tidak menyimpan konten yang kamu masukkan ke alat.</p>
<p>Browser-mu menyimpan dua entri localStorage kecil hanya di perangkatmu sendiri — keduanya bisa dibaca dan dihapus via developer tools browser:</p>
<ul>
<li><code>theme</code> — "light" atau "dark", preferensi sekitar satu byte.</li>
<li><code>toolhub:consent</code> — preferensi iklanmu (ya/tidak/belum jelas). Supaya kami tidak menanyakan ulang.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA, dan DPA Slovakia</h2>
<p>Toolhub memproses data minimal:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (di-host di EU) menyediakan dasar analitik yang sesuai. Ketika AdSense aktif, Google menjalankan lapisan persetujuannya sendiri di bawah TCF v2.</li>
<li><strong>California (CCPA):</strong> kami tidak menjual data pribadi. Tidak ada data pribadi untuk dijual.</li>
<li><strong>Slovakia (otoritas perlindungan data Slovakia):</strong> maintainer Toolhub berada di Slovakia. Aturan Slovakia berlaku untuk pemrosesan apa pun yang benar-benar terjadi — yang dalam praktiknya hanya berarti pengukuran agregat Plausible dan (ketika diaktifkan) alur persetujuan AdSense sendiri.</li>
</ul>
<p>Hak akses atau penghapusan data pribadi dalam praktiknya tidak berlaku karena tidak ada data pribadi yang disimpan untuk diakses atau dihapus. Untuk pertanyaan spesifik, kirim email via <a href="/id/contact/">halaman kontak</a>.</p>

<h2>Cookie</h2>
<ul>
<li><strong>Plausible:</strong> tanpa cookie, tidak pernah.</li>
<li><strong>Preferensi tema:</strong> sebuah entri localStorage, bukan cookie. Tetap di perangkatmu. Tidak dilampirkan ke request HTTP.</li>
<li><strong>AdSense (jika aktif):</strong> Google menempatkan cookie iklan pihak ketiganya sendiri. Banner persetujuan muncul sebelum skrip AdSense dimuat, dan jika kamu menolak, AdSense tidak dimuat sama sekali.</li>
</ul>

<h2>Anak-anak</h2>
<p>Toolhub ramah sekolah (lihat <a href="/id/for-schools/">Toolhub untuk Sekolah</a>). Tanpa pelacakan perilaku, tanpa iklan tertarget. Penggunaan di bawah 13 tahun diperbolehkan dalam syarat AdSense menurut wilayah — di tempat AdSense membatasi iklan yang ditujukan untuk anak-anak secara regional, batas-batas itu ditegakkan oleh sistem Google sendiri.</p>

<h2>PDF yang bisa diunduh</h2>
<p>Versi PDF halaman ini tersedia untuk penggunaan offline atau untuk dicetak sebagai bagian dari dokumentasi IT sekolah:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF saat ini hanya dalam bahasa Inggris; PDF per bahasa di luar cakupan rilis ini.</p>

<h2>Pertanyaan</h2>
<p>Jika ada yang tidak jelas di sini, buka issue di <a href="{REPO_URL}">{REPO_URL}</a> atau gunakan <a href="/id/contact/">halaman kontak</a>. Pertanyaan klarifikasi adalah cara yang baik untuk membuat halaman ini lebih baik bagi pembaca berikutnya.</p>
""".strip(),
            },
            "vi": {
                "title": "Cách chúng tôi xử lý dữ liệu của bạn",
                "h1": "Cách chúng tôi xử lý dữ liệu của bạn",
                "description": "Giải thích bằng ngôn ngữ thông thường chính xác cách Toolhub xử lý dữ liệu của bạn. Công cụ chạy trong trình duyệt, không có gì được lưu, ba ngoại lệ được liệt kê rõ ràng.",
                "body": f"""
<p><strong>Cập nhật lần cuối:</strong> {LAST_UPDATED}</p>
<p>Trang này là phiên bản ngôn ngữ thông thường. Nó bổ sung cho <a href="/vi/privacy/">chính sách bảo mật</a>; nếu cả hai mâu thuẫn ở đâu đó, trang này cụ thể hơn và sẽ áp dụng.</p>

<h2>Dữ liệu đi về đâu</h2>
<p>Công cụ trên Toolhub chạy trong trình duyệt của bạn. Bất cứ điều gì bạn dán, gõ, hoặc tải lên một công cụ đều ở lại trên thiết bị của bạn — không có executor công cụ phía server, và không có endpoint upload đằng sau các công cụ.</p>
<p>Có chính xác ba ngoại lệ được nêu rõ ràng cho "không có gì rời khỏi thiết bị của bạn":</p>
<ol>
<li><strong>Công cụ YouTube Thumbnail</strong> — khi bạn gửi URL YouTube, trình duyệt của bạn fetch thumbnail trực tiếp từ <code>i.ytimg.com</code> (CDN công khai của YouTube cho ảnh). Không có xác thực, không có upload, không có API key. YouTube chỉ thấy video ID từ URL, và chỉ vì trình duyệt của bạn yêu cầu nó.</li>
<li><strong>AdSense (chỉ khi bật và có sự đồng ý)</strong> — hệ thống quảng cáo display của Google. Với sự đồng ý, Google có thể thấy địa chỉ IP của bạn và đặt cookie theo chính sách của họ. Khi từ chối (mặc định), AdSense không tải gì cả.</li>
<li><strong>Plausible Analytics</strong> — đếm lượt xem trang, referrer, quốc gia, và loại thiết bị. Không có cookie, không có fingerprinting, chỉ có thống kê tổng hợp. Server Plausible ở EU.</li>
</ol>

<h2>Những gì chúng tôi lưu</h2>
<p>Không gì về bạn cả. Không có tài khoản, không có ID người dùng, không có email, không có hồ sơ. Chúng tôi không lưu nội dung bạn đưa vào công cụ.</p>
<p>Trình duyệt của bạn lưu hai entry localStorage nhỏ chỉ trên thiết bị của bạn — cả hai có thể đọc và xóa qua developer tools của trình duyệt:</p>
<ul>
<li><code>theme</code> — "light" hoặc "dark", tùy chọn khoảng một byte.</li>
<li><code>toolhub:consent</code> — tùy chọn quảng cáo của bạn (có/không/chưa quyết định). Để chúng tôi không hỏi lại.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA, và DPA Slovakia</h2>
<p>Toolhub xử lý dữ liệu tối thiểu:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (host ở EU) cung cấp cơ sở analytics tuân thủ. Khi AdSense bật, Google chạy lớp đồng ý riêng dưới TCF v2.</li>
<li><strong>California (CCPA):</strong> chúng tôi không bán dữ liệu cá nhân. Không có dữ liệu cá nhân để bán.</li>
<li><strong>Slovakia (cơ quan bảo vệ dữ liệu Slovakia):</strong> maintainer Toolhub đặt tại Slovakia. Quy tắc Slovakia áp dụng cho bất kỳ xử lý nào thực sự xảy ra — mà trong thực tế chỉ có nghĩa là phép đo tổng hợp của Plausible và (khi bật) luồng đồng ý AdSense của chính nó.</li>
</ul>
<p>Quyền truy cập hoặc xóa dữ liệu cá nhân trong thực tế không áp dụng vì không có dữ liệu cá nhân nào được lưu để truy cập hoặc xóa. Đối với câu hỏi cụ thể, gửi email qua <a href="/vi/contact/">trang liên hệ</a>.</p>

<h2>Cookie</h2>
<ul>
<li><strong>Plausible:</strong> không có cookie, không bao giờ.</li>
<li><strong>Tùy chọn theme:</strong> một entry localStorage, không phải cookie. Ở lại trên thiết bị của bạn. Không được đính kèm vào HTTP request.</li>
<li><strong>AdSense (nếu bật):</strong> Google đặt cookie quảng cáo bên thứ ba của riêng họ. Banner đồng ý xuất hiện trước khi script AdSense tải, và nếu bạn từ chối, AdSense không tải gì cả.</li>
</ul>

<h2>Trẻ em</h2>
<p>Toolhub thân thiện với trường học (xem <a href="/vi/for-schools/">Toolhub cho Trường học</a>). Không có theo dõi hành vi, không có quảng cáo nhắm mục tiêu. Việc sử dụng dưới 13 tuổi được cho phép trong điều khoản AdSense theo khu vực — ở nơi AdSense hạn chế quảng cáo nhắm vào trẻ em theo khu vực, các giới hạn đó được thực thi bởi chính hệ thống của Google.</p>

<h2>PDF có thể tải xuống</h2>
<p>Phiên bản PDF của trang này có sẵn cho việc sử dụng offline hoặc để in như một phần của tài liệu IT trường học:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF hiện chỉ có bản tiếng Anh; PDF theo từng ngôn ngữ nằm ngoài phạm vi của bản phát hành này.</p>

<h2>Câu hỏi</h2>
<p>Nếu có gì không rõ ở đây, mở issue ở <a href="{REPO_URL}">{REPO_URL}</a> hoặc dùng <a href="/vi/contact/">trang liên hệ</a>. Câu hỏi làm rõ là cách tốt để làm cho trang này tốt hơn cho người đọc tiếp theo.</p>
""".strip(),
            },
            "sk": {
                "title": "Ako narábame s tvojimi údajmi",
                "h1": "Ako narábame s tvojimi údajmi",
                "description": "Otvorené vysvetlenie v ľudskej reči, ako presne Toolhub narába s tvojimi údajmi. Nástroje bežia v prehliadači, nič sa neukladá, tri pomenované výnimky sú výslovne uvedené.",
                "body": f"""
<p><strong>Naposledy aktualizované:</strong> {LAST_UPDATED}</p>
<p>Táto stránka je verzia v bežnej reči. Dopĺňa <a href="/sk/privacy/">zásady ochrany súkromia</a>; ak by sa zdalo, že si v niečom protirečia, táto stránka je tá konkrétnejšia a má sa brať ako smerodajná.</p>

<h2>Kam idú dáta</h2>
<p>Nástroje na Toolhube bežia v tvojom prehliadači. Čokoľvek vložíš, napíšeš alebo nahráš do nástroja, zostáva na tvojom zariadení — nemáme server-side runner nástrojov a za žiadnym z nich nie je upload endpoint.</p>
<p>Existujú presne tri pomenované výnimky z „žiadne dáta neopúšťajú tvoje zariadenie":</p>
<ol>
<li><strong>Nástroj YouTube Thumbnail</strong> — keď pošleš YouTube URL, tvoj prehliadač si načíta thumbnail priamo z <code>i.ytimg.com</code> (verejné image CDN YouTube). Bez autentifikácie, bez uploadu, bez API kľúča. Video ID v URL je jediné, čo YouTube vidí, a aj to len preto, že to tvoj prehliadač natiahol.</li>
<li><strong>AdSense (iba ak je zapnuté a so súhlasom)</strong> — display-ad systém Google. Keď udelíš súhlas s reklamami, Google môže vidieť tvoju IP adresu a môže nastaviť cookies podľa svojich pravidiel. Keď odmietneš (východiskový stav), AdSense sa vôbec nenačíta.</li>
<li><strong>Plausible analytika</strong> — počíta návštevy stránok, referrer, krajinu a triedu zariadenia. Žiadne cookies, žiadny fingerprinting, len agregované štatistiky. Servery Plausible sú EU-hosted.</li>
</ol>

<h2>Čo ukladáme</h2>
<p>O tebe nič. Žiadne účty, žiadne user ID, žiadne e-maily, žiadny profil. Obsah, ktorý dáš do nástrojov, neukladáme.</p>
<p>Tvoj prehliadač u teba lokálne ukladá dva malé localStorage záznamy — oba čitateľné a zmazateľné z developer tools tvojho prehliadača:</p>
<ul>
<li><code>theme</code> — „light" alebo „dark", zhruba byte preferencie.</li>
<li><code>toolhub:consent</code> — tvoje rozhodnutie o súhlase s reklamami (áno/nie/nenastavené). Aby sme sa nepýtali znova.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA a slovenský ÚOOÚ</h2>
<p>Toolhub spracúva minimum dát:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (EU-hosted) tvorí compliant analytics baseline. Keď je AdSense aktívny, Google si spravuje vlastnú consent vrstvu pod TCF v2.</li>
<li><strong>Kalifornia (CCPA):</strong> osobné informácie nepredávame. Žiadne osobné informácie na predaj nemáme.</li>
<li><strong>Slovensko (Úrad na ochranu osobných údajov SR):</strong> maintainer Toolhubu žije na Slovensku. Pravidlá slovenského ÚOOÚ platia na akékoľvek spracovanie, ktoré skutočne prebieha — a to je v praxi obmedzené na agregované metriky Plausible a (keď je zapnutý) consent-managed flow AdSense.</li>
</ul>
<p>Práva na prístup alebo vymazanie osobných údajov sa fakticky nedajú uplatniť, lebo žiadne osobné údaje na prístup ani vymazanie sa neukladajú. Ak máš konkrétne otázky, kontaktuj nás cez <a href="/sk/contact/">kontaktnú stránku</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> žiadne cookies, nikdy.</li>
<li><strong>Theme preferencia:</strong> jeden localStorage záznam, nie cookie. Zostáva na tvojom zariadení. Neposiela sa s HTTP requestami.</li>
<li><strong>AdSense (keď aktívny):</strong> Google nastavuje vlastné third-party reklamné cookies. Consent banner sa zobrazí pred načítaním AdSense skriptu a ak odmietneš, AdSense sa vôbec nenačíta.</li>
</ul>

<h2>Deti</h2>
<p>Toolhub je školsky priateľský (pozri <a href="/sk/for-schools/">Toolhub pre školy</a>). Žiadny behavioral tracking, žiadna cielená reklama. Použitie deťmi pod 13 rokov je v poriadku v rámci existujúcich AdSense podmienok podľa regiónu — ak si v regióne, kde AdSense obmedzuje reklamy voči deťom, tieto obmedzenia rešpektujú vlastné systémy Google.</p>

<h2>PDF na stiahnutie</h2>
<p>PDF verzia tejto stránky je k dispozícii na offline referenciu alebo na tlač ako súčasť školskej IT dokumentácie:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF je momentálne len v angličtine; per-jazyk PDF nie sú v rozsahu tohto releasu.</p>

<h2>Otázky</h2>
<p>Ak ti tu niečo nie je jasné, otvor issue na <a href="{REPO_URL}">{REPO_URL}</a> alebo použi <a href="/sk/contact/">kontaktnú stránku</a>. Otázky na ujasnenie sú dobrý spôsob, ako urobiť túto stránku lepšou pre ďalšieho čitateľa.</p>
""".strip(),
            },
            "cs": {
                "title": "Jak nakládáme s tvými daty",
                "h1": "Jak nakládáme s tvými daty",
                "description": "Otevřené vysvětlení v běžné řeči, jak přesně Toolhub nakládá s tvými daty. Nástroje běží v prohlížeči, nic se neukládá, tři pojmenované výjimky jsou výslovně uvedeny.",
                "body": f"""
<p><strong>Naposledy aktualizováno:</strong> {LAST_UPDATED}</p>
<p>Tato stránka je verze v běžné řeči. Doplňuje <a href="/cs/privacy/">zásady ochrany soukromí</a>; pokud by se zdálo, že si v něčem odporují, tato stránka je ta konkrétnější a má se brát jako směrodatná.</p>

<h2>Kam jdou data</h2>
<p>Nástroje na Toolhubu běží v tvém prohlížeči. Cokoli vložíš, napíšeš nebo nahraješ do nástroje, zůstává na tvém zařízení — nemáme server-side runner nástrojů a za žádným z nich není upload endpoint.</p>
<p>Existují přesně tři pojmenované výjimky z „žádná data neopouštějí tvé zařízení":</p>
<ol>
<li><strong>Nástroj YouTube Thumbnail</strong> — když pošleš YouTube URL, tvůj prohlížeč si načte thumbnail přímo z <code>i.ytimg.com</code> (veřejné image CDN YouTube). Bez autentifikace, bez uploadu, bez API klíče. Video ID v URL je jediné, co YouTube vidí, a to jen proto, že to tvůj prohlížeč stáhl.</li>
<li><strong>AdSense (jen pokud je zapnutý a se souhlasem)</strong> — display-ad systém Google. Když udělíš souhlas s reklamami, Google může vidět tvou IP adresu a může nastavit cookies podle svých pravidel. Když odmítneš (výchozí stav), AdSense se vůbec nenačte.</li>
<li><strong>Plausible analytika</strong> — počítá návštěvy stránek, referrer, zemi a třídu zařízení. Žádné cookies, žádný fingerprinting, jen agregované statistiky. Servery Plausible jsou EU-hosted.</li>
</ol>

<h2>Co ukládáme</h2>
<p>O tobě nic. Žádné účty, žádné user ID, žádné e-maily, žádný profil. Obsah, který dáš do nástrojů, neukládáme.</p>
<p>Tvůj prohlížeč u tebe lokálně ukládá dva malé localStorage záznamy — oba čitelné a smazatelné z developer tools tvého prohlížeče:</p>
<ul>
<li><code>theme</code> — „light" nebo „dark", zhruba byte preference.</li>
<li><code>toolhub:consent</code> — tvé rozhodnutí o souhlasu s reklamami (ano/ne/nenastaveno). Abychom se neptali znovu.</li>
</ul>

<h2>GDPR, UK GDPR, CCPA a český ÚOOÚ</h2>
<p>Toolhub zpracovává minimum dat:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (EU-hosted) tvoří compliant analytics baseline. Když je AdSense aktivní, Google si spravuje vlastní consent vrstvu pod TCF v2.</li>
<li><strong>Kalifornie (CCPA):</strong> osobní informace neprodáváme. Žádné osobní informace na prodej nemáme.</li>
<li><strong>Česko (Úřad pro ochranu osobních údajů):</strong> maintainer Toolhubu žije ve střední Evropě. Pravidla českého ÚOOÚ a slovenského ÚOOÚ platí na jakékoli zpracování, které skutečně probíhá — a to je v praxi omezeno na agregované metriky Plausible a (když je zapnutý) consent-managed flow AdSense.</li>
</ul>
<p>Práva na přístup nebo vymazání osobních údajů se fakticky nedají uplatnit, protože žádné osobní údaje pro přístup ani vymazání se neukládají. Pokud máš konkrétní otázky, kontaktuj nás přes <a href="/cs/contact/">kontaktní stránku</a>.</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> žádné cookies, nikdy.</li>
<li><strong>Theme preference:</strong> jeden localStorage záznam, ne cookie. Zůstává na tvém zařízení. Neposílá se s HTTP requesty.</li>
<li><strong>AdSense (když aktivní):</strong> Google nastavuje vlastní third-party reklamní cookies. Consent banner se objeví před načtením AdSense skriptu a pokud odmítneš, AdSense se vůbec nenačte.</li>
</ul>

<h2>Děti</h2>
<p>Toolhub je školsky přátelský (viz <a href="/cs/for-schools/">Toolhub pro školy</a>). Žádný behavioral tracking, žádná cílená reklama. Použití dětmi pod 13 let je v pořádku v rámci existujících AdSense podmínek podle regionu — pokud jsi v regionu, kde AdSense omezuje reklamy vůči dětem, tato omezení respektují vlastní systémy Google.</p>

<h2>PDF ke stažení</h2>
<p>PDF verze této stránky je k dispozici pro offline referenci nebo k tisku jako součást školní IT dokumentace:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF je momentálně jen v angličtině; per-jazyk PDF nejsou v rozsahu tohoto releasu.</p>

<h2>Dotazy</h2>
<p>Pokud ti tu něco není jasné, otevři issue na <a href="{REPO_URL}">{REPO_URL}</a> nebo použij <a href="/cs/contact/">kontaktní stránku</a>. Dotazy na ujasnění jsou dobrý způsob, jak udělat tuhle stránku lepší pro dalšího čtenáře.</p>
""".strip(),
            },
            "hi": {
                "title": "हम आपके डेटा को कैसे संभालते हैं",
                "h1": "हम आपके डेटा को कैसे संभालते हैं",
                "description": "Toolhub आपके डेटा को कैसे संभालता है, इसकी सीधी भाषा में जानकारी। Tools आपके browser में चलते हैं, कुछ भी संग्रहित नहीं होता, तीन नामित अपवाद स्पष्ट रूप से सूचीबद्ध हैं।",
                "body": f"""
<p><strong>अंतिम बार अद्यतन:</strong> {LAST_UPDATED}</p>
<p>यह page सीधी भाषा का संस्करण है। यह <a href="/hi/privacy/">गोपनीयता नीति</a> का पूरक है; अगर वे किसी बिंदु पर असहमत प्रतीत हों, तो यह page अधिक विशिष्ट है और इसे प्राथमिक माना जाना चाहिए।</p>

<h2>डेटा कहाँ जाता है</h2>
<p>Toolhub पर tools आपके browser में चलते हैं। आप जो भी किसी tool में paste, टाइप या upload करते हैं वह आपके device पर ही रहता है — हमारे पास कोई server-side tool runner नहीं है, और किसी भी tool के पीछे कोई upload endpoint नहीं है।</p>
<p>"कोई डेटा आपके device से बाहर नहीं जाता" के लिए ठीक तीन नामित अपवाद हैं:</p>
<ol>
<li><strong>YouTube Thumbnail tool</strong> — जब आप एक YouTube URL submit करते हैं, तो आपका browser सीधे <code>i.ytimg.com</code> (YouTube का सार्वजनिक image CDN) से thumbnail fetch करता है। कोई प्रमाणीकरण नहीं, कोई upload नहीं, कोई API key नहीं। URL में video ID ही एकमात्र चीज़ है जो YouTube देखता है, और वह भी केवल इसलिए कि आपके browser ने इसे fetch किया।</li>
<li><strong>AdSense (केवल जब enabled और सहमति प्राप्त)</strong> — Google का display-ad सिस्टम। जब आप विज्ञापन सहमति देते हैं, तो Google आपका IP address देख सकता है और cookies set कर सकता है, जो Google की नीति के तहत हैं। जब आप अस्वीकार करते हैं (default), तो AdSense बिल्कुल load नहीं होता।</li>
<li><strong>Plausible analytics</strong> — page विज़िट, referrer, देश और device class गिनता है। कोई cookies नहीं, कोई fingerprinting नहीं, केवल समग्र आँकड़े। Plausible के servers EU-hosted हैं।</li>
</ol>

<h2>हम क्या संग्रहित करते हैं</h2>
<p>आपके बारे में कुछ नहीं। कोई अकाउंट नहीं, कोई user IDs नहीं, कोई email नहीं, कोई profile नहीं। हम tools में डाली गई आपकी सामग्री संग्रहित नहीं करते।</p>
<p>आपका browser आपके device पर ही दो छोटी localStorage entries संग्रहित करता है — दोनों आपके browser के developer tools से पढ़ी और साफ़ की जा सकती हैं:</p>
<ul>
<li><code>theme</code> — "light" या "dark", लगभग एक byte की वरीयता।</li>
<li><code>toolhub:consent</code> — आपका विज्ञापन सहमति निर्णय (हाँ/नहीं/unset)। आपसे दोबारा न पूछने के लिए।</li>
</ul>

<h2>GDPR, UK GDPR, CCPA और Slovak DPA</h2>
<p>Toolhub न्यूनतम डेटा process करता है:</p>
<ul>
<li><strong>EU / UK (GDPR / UK GDPR):</strong> Plausible (EU-hosted) एक compliant analytics baseline देता है। जब AdSense सक्रिय हो, तो Google TCF v2 के तहत अपनी consent layer चलाता है।</li>
<li><strong>California (CCPA):</strong> हम व्यक्तिगत जानकारी नहीं बेचते। हमारे पास बेचने को व्यक्तिगत जानकारी है ही नहीं।</li>
<li><strong>Slovakia (Slovak Data Protection Authority):</strong> Toolhub का maintainer Slovakia में स्थित है। Slovak DPA के नियम किसी भी ऐसी processing पर लागू होते हैं जो वास्तव में होती है — जो प्रभावी रूप से Plausible के समग्र metrics और (जब enabled हो) AdSense के अपने consent-managed flow तक सीमित है।</li>
</ul>
<p>व्यक्तिगत डेटा तक पहुँचने या उसे हटाने के अधिकार प्रभावी रूप से लागू नहीं होते क्योंकि access या delete करने के लिए कोई व्यक्तिगत डेटा संग्रहित नहीं है। विशिष्ट प्रश्नों के लिए <a href="/hi/contact/">संपर्क page</a> के माध्यम से हमसे संपर्क करें।</p>

<h2>Cookies</h2>
<ul>
<li><strong>Plausible:</strong> कोई cookies नहीं, कभी नहीं।</li>
<li><strong>Theme वरीयता:</strong> एक localStorage entry, cookie नहीं। आपके device पर रहती है। HTTP requests के साथ नहीं भेजी जाती।</li>
<li><strong>AdSense (जब सक्रिय):</strong> Google अपनी स्वयं की तृतीय-पक्ष विज्ञापन cookies set करता है। AdSense script load होने से पहले consent banner दिखता है, और अगर आप अस्वीकार करते हैं तो AdSense बिल्कुल load नहीं होता।</li>
</ul>

<h2>बच्चे</h2>
<p>Toolhub स्कूल-friendly है (देखें <a href="/hi/for-schools/">स्कूलों के लिए Toolhub</a>)। कोई behavioral tracking नहीं और कोई targeted विज्ञापन नहीं। 13 साल से कम आयु का उपयोग AdSense की क्षेत्रवार लागू मौजूदा शर्तों के अंतर्गत स्वीकार्य है — मतलब अगर आप ऐसे क्षेत्र में हैं जहाँ AdSense बच्चों के लिए विज्ञापनों पर प्रतिबंध लगाता है, तो उन प्रतिबंधों का पालन Google के अपने सिस्टम द्वारा किया जाता है।</p>

<h2>Downloadable PDF</h2>
<p>इस page का एक PDF संस्करण offline reference के लिए या स्कूल के IT documentation के हिस्से के रूप में print करने के लिए उपलब्ध है:</p>
<p><a href="{PDF_URL}">how-we-handle-your-data.pdf</a></p>
<p>PDF इस समय केवल अंग्रेज़ी में है; प्रति-भाषा PDFs वर्तमान release के दायरे में नहीं हैं।</p>

<h2>प्रश्न</h2>
<p>अगर यहाँ कुछ अस्पष्ट है, तो कृपया <a href="{REPO_URL}">{REPO_URL}</a> पर एक issue खोलें या <a href="/hi/contact/">संपर्क page</a> का उपयोग करें। स्पष्टीकरण के प्रश्न इस page को अगले पाठक के लिए बेहतर बनाने का एक उपयोगी तरीक़ा हैं।</p>
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
<p>Toolhub currently uses these affiliate and support accounts (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub nutzt derzeit die folgenden Affiliate- und Support-Konten (Betreiber: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (Cloud-Hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub utiliza actualmente las siguientes cuentas de afiliado y de apoyo (operador: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (alojamiento en la nube) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub utilise actuellement ces comptes d'affiliation et de soutien (opérateur : JXXR1) :</p>
<ul>
<li><strong>DigitalOcean</strong> (hébergement cloud) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub utilizza attualmente questi account di affiliazione e di supporto (operatore: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (hosting cloud) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>O Toolhub usa atualmente estas contas de afiliado e de apoio (operador: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (hospedagem em nuvem) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub korzysta obecnie z następujących kont partnerskich i wsparcia (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (hosting w chmurze) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub は現在、以下のアフィリエイトおよびサポートアカウントを利用しています（運用者：JXXR1）：</p>
<ul>
<li><strong>DigitalOcean</strong>（クラウドホスティング） — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
<p>Toolhub gebruikt momenteel deze affiliate- en support-accounts (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud-hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
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
            "tr": {
                "title": "Affiliate bildirimi",
                "h1": "Affiliate bildirimi",
                "description": "FTC ve EU uyumlu Toolhub affiliate ilişkilerinin bildirimi. Sağlayıcı öder, ek bir şey ödemen, ve editöryel içerik affiliate-güdümlü değildir.",
                "body": f"""
<p><strong>Son güncelleme:</strong> {LAST_UPDATED}</p>

<h2>Affiliate linkleri ne</h2>
<p>Bir affiliate link, üzerine eklenmiş bir takip koduyla normal bir linktir. Tıklayıp ardından linkli servise kayıt olursan, servis Toolhub'a küçük bir referans ücreti öder. <em>Senin</em> ödediğin fiyat affiliate olmayan sürümle aynıdır — komisyonu sen ödemiyorsun, sağlayıcı ödüyor.</p>

<h2>Toolhub'da nerede oldukları</h2>
<p>Şu anda affiliate linkleri iki yerdedir:</p>
<ul>
<li>Sitenin footer'ında, küçük bir <code>(affiliate)</code> rozetiyle işaretli.</li>
<li>Bir aracın yardım bloğu veya "ilgili araçlar" bölümünün önerdiğimiz belirli bir ücretli servisi adlandırdığı her yerde — affiliate yerinde gösterilir.</li>
</ul>
<p>Affiliate linkleri HTML'de <code>rel="sponsored"</code> taşır, bu da ticari bir ilişkiyi belirtmek için arama motoru standardıdır.</p>

<h2>Kim öder</h2>
<p>Komisyonu sağlayıcı öder, sen değil. Affiliate linkini yok sayıp doğrudan sağlayıcının ana sayfasından kayıt olursan, aynı fiyata aynı hizmeti alırsın; biz sadece referansı görmeyiz.</p>

<h2>FTC ve EU uyumluluğu</h2>
<p>Bu sayfa var çünkü hem ABD Federal Ticaret Komisyonu'nun endorsement kılavuzları hem de tüketici koruması için EU kuralları, içerik üreticilerinin linkli bir ürünle finansal bir ilişkiyi bildirmesini gerektirir. Bildirim açık ve önden olmalıdır — bu yüzden ayrı bir üst düzey sayfa, bu yüzden her sayfa footer'ında link.</p>

<h2>Spesifik affiliate'ler</h2>
<p>Toolhub şu anda bu affiliate ve destek hesaplarını kullanır (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>Başka affiliate ilişkileri eklendiğinde, burada listelenirler ve sayfa tarihi güncellenir.</p>

<h2>Ücretli yerleştirme yok</h2>
<p>Araç incelemeleri, araçların ana sayfada görünme sırası ve her aracın altındaki "ilgili araçlar" linkleri affiliate-güdümlü <strong>değildir</strong>. Bir aracı öne çıkarmak veya bir aracı diğerinin üstüne yerleştirmek için para kabul etmiyoruz. Eğer ücretli bir yerleştirme eklenirse (olmayacak, ama her ihtimale karşı), affiliate linkleri gibi etiketlenir: açık, önden, editöryel içerikten ayırt edilebilir.</p>

<h2>Editöryel bağımsızlık</h2>
<p>Affiliate ilişkileri hangi araçların inşa edildiğini, yardım bloklarının nasıl yazıldığını veya verilen bir aracın altında hangi "ilgili araçların" göründüğünü etkilemez. Toolhub'daki araçlar affiliate programı olmadan da inşa edeceğimiz araçlardır — program sadece hosting ve bakıma küçük bir katkı sağlar.</p>

<h2>İletişim</h2>
<p>Belirli bir affiliate hakkında soruların var mı, veya burada olmaması gereken bir şeyi işaret etmek istiyorsan? <a href="{REPO_URL}">{REPO_URL}</a> üzerinde bir issue aç veya <a href="/tr/contact/">iletişim sayfası</a>\'nı kullan.</p>
""".strip(),
            },
            "id": {
                "title": "Pengungkapan afiliasi",
                "h1": "Pengungkapan afiliasi",
                "description": "Pengungkapan hubungan afiliasi Toolhub yang sesuai FTC dan EU. Vendor yang membayar, kamu tidak bayar tambahan apa pun, dan liputan editorial tidak digerakkan afiliasi.",
                "body": f"""
<p><strong>Terakhir diperbarui:</strong> {LAST_UPDATED}</p>

<h2>Apa itu tautan afiliasi</h2>
<p>Tautan afiliasi adalah tautan biasa dengan kode pelacak yang dilampirkan. Jika kamu mengkliknya dan kemudian mendaftar ke layanan yang ditautkan, layanan tersebut membayar Toolhub komisi rujukan kecil. Harga yang <em>kamu</em> bayar identik dengan versi non-afiliasi — kamu tidak membayar komisinya, vendor yang membayar.</p>

<h2>Di mana mereka di Toolhub</h2>
<p>Saat ini tautan afiliasi ada di dua tempat:</p>
<ul>
<li>Di footer situs, ditandai dengan badge <code>(affiliate)</code> kecil.</li>
<li>Di mana pun blok bantuan alat atau bagian "alat terkait" menyebut layanan berbayar tertentu yang kami rekomendasikan — afiliasi muncul di tempatnya.</li>
</ul>
<p>Tautan afiliasi membawa <code>rel="sponsored"</code> di HTML, yang merupakan standar mesin pencari untuk menandakan hubungan komersial.</p>

<h2>Siapa yang membayar</h2>
<p>Vendor yang membayar komisi, bukan kamu. Jika kamu mengabaikan tautan afiliasi dan mendaftar langsung dari beranda vendor, kamu mendapat layanan yang sama dengan harga yang sama; kami hanya tidak melihat rujukan.</p>

<h2>Kepatuhan FTC dan EU</h2>
<p>Halaman ini ada karena baik panduan endorsement Komisi Perdagangan Federal AS maupun aturan EU untuk perlindungan konsumen mewajibkan pembuat konten untuk mengungkapkan hubungan finansial dengan produk yang ditautkan. Pengungkapan harus jelas dan di muka — itulah sebabnya ada halaman top-level terpisah, dan itulah sebabnya ada tautan di footer setiap halaman.</p>

<h2>Afiliasi spesifik</h2>
<p>Toolhub saat ini menggunakan afiliasi dan akun dukungan berikut (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>Ketika hubungan afiliasi lain ditambahkan, mereka akan dicantumkan di sini dan tanggal halaman akan diperbarui.</p>

<h2>Tanpa penempatan berbayar</h2>
<p>Ulasan alat, urutan kemunculan alat di beranda, dan tautan "alat terkait" di bawah tiap alat <strong>tidak</strong> digerakkan afiliasi. Kami tidak menerima uang untuk menampilkan alat atau menempatkan satu alat di atas alat lainnya. Jika penempatan berbayar ditambahkan (tidak akan, tapi untuk berjaga-jaga), itu akan diberi label seperti tautan afiliasi: jelas, di muka, bisa dibedakan dari konten editorial.</p>

<h2>Independensi editorial</h2>
<p>Hubungan afiliasi tidak memengaruhi alat mana yang dibangun, bagaimana blok bantuan ditulis, atau "alat terkait" mana yang muncul di bawah alat tertentu. Alat di Toolhub adalah alat yang akan kami bangun bahkan tanpa program afiliasi — program hanya berkontribusi sedikit pada hosting dan perawatan.</p>

<h2>Kontak</h2>
<p>Punya pertanyaan tentang afiliasi tertentu, atau ingin menunjukkan sesuatu yang seharusnya tidak ada di sini? Buka issue di <a href="{REPO_URL}">{REPO_URL}</a> atau gunakan <a href="/id/contact/">halaman kontak</a>.</p>
""".strip(),
            },
            "vi": {
                "title": "Tiết lộ affiliate",
                "h1": "Tiết lộ affiliate",
                "description": "Tiết lộ về các quan hệ affiliate của Toolhub tuân thủ FTC và EU. Vendor trả tiền, bạn không trả thêm gì, và việc viết nội dung biên tập không bị chi phối bởi affiliate.",
                "body": f"""
<p><strong>Cập nhật lần cuối:</strong> {LAST_UPDATED}</p>

<h2>Link affiliate là gì</h2>
<p>Link affiliate là một link bình thường với mã theo dõi đính kèm. Nếu bạn click vào nó và sau đó đăng ký dịch vụ được liên kết, dịch vụ đó trả Toolhub một khoản hoa hồng giới thiệu nhỏ. Giá <em>bạn</em> trả giống hệt với phiên bản không-affiliate — bạn không trả hoa hồng, vendor trả.</p>

<h2>Chúng ở đâu trên Toolhub</h2>
<p>Hiện tại link affiliate có ở hai chỗ:</p>
<ul>
<li>Trong footer của site, được đánh dấu bằng badge <code>(affiliate)</code> nhỏ.</li>
<li>Bất cứ nơi nào block trợ giúp công cụ hoặc phần "công cụ liên quan" đề cập đến một dịch vụ trả phí cụ thể mà chúng tôi giới thiệu — affiliate xuất hiện trong vị trí.</li>
</ul>
<p>Link affiliate mang <code>rel="sponsored"</code> trong HTML, đó là tiêu chuẩn của công cụ tìm kiếm để báo hiệu quan hệ thương mại.</p>

<h2>Ai trả tiền</h2>
<p>Vendor trả hoa hồng, không phải bạn. Nếu bạn bỏ qua link affiliate và đăng ký trực tiếp từ trang chủ của vendor, bạn nhận được cùng dịch vụ với cùng giá; chúng tôi chỉ không thấy giới thiệu.</p>

<h2>Tuân thủ FTC và EU</h2>
<p>Trang này tồn tại vì cả hướng dẫn xác nhận của Federal Trade Commission Hoa Kỳ và quy tắc EU về bảo vệ người tiêu dùng đều yêu cầu người tạo nội dung tiết lộ mối quan hệ tài chính với sản phẩm được liên kết. Việc tiết lộ phải rõ ràng và trả trước — đó là lý do có một trang riêng cấp cao, và đó là lý do có một link ở footer của mọi trang.</p>

<h2>Affiliate cụ thể</h2>
<p>Toolhub hiện tại dùng các affiliate và tài khoản hỗ trợ sau (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>Khi quan hệ affiliate khác được thêm, chúng sẽ được liệt kê ở đây và ngày của trang sẽ được cập nhật.</p>

<h2>Không có vị trí trả phí</h2>
<p>Đánh giá công cụ, thứ tự xuất hiện của công cụ trên trang chủ, và link "công cụ liên quan" dưới mỗi công cụ <strong>không</strong> bị chi phối bởi affiliate. Chúng tôi không nhận tiền để giới thiệu công cụ hoặc đặt một công cụ trên công cụ khác. Nếu vị trí trả phí được thêm vào (sẽ không, nhưng đề phòng), nó sẽ được dán nhãn như link affiliate: rõ ràng, trả trước, phân biệt được với nội dung biên tập.</p>

<h2>Độc lập biên tập</h2>
<p>Quan hệ affiliate không ảnh hưởng đến công cụ nào được xây dựng, block trợ giúp được viết như thế nào, hoặc "công cụ liên quan" nào xuất hiện dưới một công cụ cụ thể. Công cụ trên Toolhub là những công cụ chúng tôi sẽ xây dựng ngay cả khi không có chương trình affiliate — chương trình chỉ đóng góp một chút vào hosting và bảo trì.</p>

<h2>Liên hệ</h2>
<p>Có câu hỏi về một affiliate cụ thể, hoặc muốn chỉ ra điều gì đó không nên ở đây? Mở issue ở <a href="{REPO_URL}">{REPO_URL}</a> hoặc dùng <a href="/vi/contact/">trang liên hệ</a>.</p>
""".strip(),
            },
            "sk": {
                "title": "Affiliate zverejnenie",
                "h1": "Affiliate zverejnenie",
                "description": "FTC- a EU-compliant zverejnenie affiliate vzťahov Toolhubu. Vendor platí, ty nezaplatíš nič navyše a editoriálne pokrytie sa neriadi affiliate-mi.",
                "body": f"""
<p><strong>Naposledy aktualizované:</strong> {LAST_UPDATED}</p>

<h2>Čo sú affiliate odkazy</h2>
<p>Affiliate odkaz je bežný odkaz s pripojeným tracking kódom. Ak naň klikneš a potom sa registruješ do odkazovanej služby, služba zaplatí Toolhub-u malú referral províziu. Cena, ktorú <em>ty</em> platíš, je rovnaká ako non-affiliate verzia — províziu neplatíš ty, platí ju vendor.</p>

<h2>Kde sa na Toolhube objavujú</h2>
<p>Aktuálne sa affiliate odkazy objavujú na dvoch miestach:</p>
<ul>
<li>V päte stránky, označené malým <code>(affiliate)</code> badge-om.</li>
<li>Kdekoľvek help-block nástroja alebo related-tools sekcia spomína konkrétnu platenú službu, ktorú odporúčame — v tých prípadoch je affiliate uvedený inline.</li>
</ul>
<p>Affiliate odkazy nesú v HTML <code>rel="sponsored"</code>, čo je search-engine štandard na deklarovanie komerčného vzťahu.</p>

<h2>Kto platí</h2>
<p>Províziu platí vendor, nie ty. Ak affiliate odkaz ignoruješ a registruješ sa priamo cez homepage vendora, dostaneš tú istú službu za rovnakú cenu; my len referral nevidíme.</p>

<h2>FTC a EU compliance</h2>
<p>Táto stránka existuje preto, že endorsement guidelines US Federal Trade Commission a EU pravidlá ochrany spotrebiteľa vyžadujú, aby tvorcovia obsahu zverejnili finančný vzťah s odkazovaným produktom. Zverejnenie musí byť jasné a vopred — preto top-level stránka a preto odkaz v päte každej stránky.</p>

<h2>Konkrétne affiliate</h2>
<p>Toolhub aktuálne používa tieto affiliate a support účty (operátor: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>Keď pribudnú ďalšie affiliate vzťahy, budú uvedené tu a stránka bude prešítaná.</p>

<h2>Žiadne platené umiestnenia</h2>
<p>Recenzie nástrojov, poradie, v akom sa nástroje na homepage zobrazujú, ani „related tools" odkazy pod každým nástrojom <strong>nie sú</strong> riadené affiliate-mi. Neprijímame peniaze za to, aby sme nástroj featurovali alebo jeden nástroj nadradili nad druhý. Ak by sa niekedy platené umiestnenie pridalo (nepridá sa, ale ak by), bolo by označené rovnako ako affiliate odkazy: jasne, vopred, odlíšiteľne od editoriálneho obsahu.</p>

<h2>Editoriálna nezávislosť</h2>
<p>Affiliate vzťahy neovplyvňujú, ktoré nástroje sa stavajú, ako sa píše help-block text, ani ktoré „related tools" sa pod daným nástrojom objavia. Nástroje na Toolhub-e sú nástroje, ktoré by sme stavali aj bez akéhokoľvek affiliate programu — program len zložkou prispieva na hosting a údržbu.</p>

<h2>Kontakt</h2>
<p>Otázky ku konkrétnemu affiliate alebo chceš upozorniť na niečo, čo by tu nemalo byť? Otvor issue na <a href="{REPO_URL}">{REPO_URL}</a> alebo použi <a href="/sk/contact/">kontaktnú stránku</a>.</p>
""".strip(),
            },
            "cs": {
                "title": "Affiliate zveřejnění",
                "h1": "Affiliate zveřejnění",
                "description": "FTC- a EU-compliant zveřejnění affiliate vztahů Toolhubu. Vendor platí, ty nezaplatíš nic navíc a editorialní pokrytí se neřídí affiliate.",
                "body": f"""
<p><strong>Naposledy aktualizováno:</strong> {LAST_UPDATED}</p>

<h2>Co jsou affiliate odkazy</h2>
<p>Affiliate odkaz je běžný odkaz s připojeným tracking kódem. Pokud na něj klikneš a poté se zaregistruješ k odkazované službě, služba zaplatí Toolhubu malou referral provizi. Cena, kterou <em>ty</em> platíš, je stejná jako u non-affiliate verze — provizi neplatíš ty, platí ji vendor.</p>

<h2>Kde se na Toolhubu objevují</h2>
<p>Aktuálně se affiliate odkazy objevují na dvou místech:</p>
<ul>
<li>V patičce stránky, označené malým <code>(affiliate)</code> badgem.</li>
<li>Kdekoli help-block nástroje nebo related-tools sekce zmiňuje konkrétní placenou službu, kterou doporučujeme — v těchto případech je affiliate uveden inline.</li>
</ul>
<p>Affiliate odkazy nesou v HTML <code>rel="sponsored"</code>, což je search-engine standard pro deklarování komerčního vztahu.</p>

<h2>Kdo platí</h2>
<p>Provizi platí vendor, ne ty. Pokud affiliate odkaz ignoruješ a zaregistruješ se přímo přes homepage vendora, dostaneš tutéž službu za stejnou cenu; my jen referral nevidíme.</p>

<h2>FTC a EU compliance</h2>
<p>Tato stránka existuje proto, že endorsement guidelines US Federal Trade Commission a EU pravidla ochrany spotřebitele vyžadují, aby tvůrci obsahu zveřejnili finanční vztah k odkazovanému produktu. Zveřejnění musí být jasné a předem — proto top-level stránka a proto odkaz v patičce každé stránky.</p>

<h2>Konkrétní affiliate</h2>
<p>Toolhub aktuálně používá tyto affiliate a support účty (operátor: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>Když přibudou další affiliate vztahy, budou uvedeny zde a stránka bude přerazítkována.</p>

<h2>Žádné placené umístění</h2>
<p>Recenze nástrojů, pořadí, v jakém se nástroje na homepage zobrazují, ani „related tools" odkazy pod každým nástrojem <strong>nejsou</strong> řízeny affiliate. Nepřijímáme peníze za to, abychom nástroj featurovali nebo jeden nástroj nadřadili druhému. Pokud by někdy placené umístění přibylo (nepřibude, ale kdyby), bylo by označeno stejně jako affiliate odkazy: jasně, předem, odlišitelně od editorialního obsahu.</p>

<h2>Editorialní nezávislost</h2>
<p>Affiliate vztahy neovlivňují, které nástroje se staví, jak se píše help-block text, ani které „related tools" se pod daným nástrojem objeví. Nástroje na Toolhubu jsou nástroje, které bychom stavěli i bez jakéhokoli affiliate programu — program jen drobně přispívá na hosting a údržbu.</p>

<h2>Kontakt</h2>
<p>Otázky ke konkrétnímu affiliate nebo chceš upozornit na něco, co by tu nemělo být? Otevři issue na <a href="{REPO_URL}">{REPO_URL}</a> nebo použij <a href="/cs/contact/">kontaktní stránku</a>.</p>
""".strip(),
            },
            "hi": {
                "title": "Affiliate disclosure",
                "h1": "Affiliate disclosure",
                "description": "Toolhub के affiliate संबंधों का FTC- और EU-compliant disclosure। Vendor पैसा देता है, आप अतिरिक्त कुछ नहीं देते, और संपादकीय कवरेज affiliate से प्रभावित नहीं है।",
                "body": f"""
<p><strong>अंतिम बार अद्यतन:</strong> {LAST_UPDATED}</p>

<h2>Affiliate links क्या हैं</h2>
<p>Affiliate link एक सामान्य link है जिसमें एक tracking code जुड़ा होता है। अगर आप किसी पर click करते हैं और फिर linked सेवा के लिए sign up करते हैं, तो वह सेवा Toolhub को एक छोटा referral commission देती है। <em>आप</em> जो क़ीमत चुकाते हैं वह non-affiliate संस्करण के समान ही है — आप commission नहीं चुका रहे, vendor चुका रहा है।</p>

<h2>वे Toolhub पर कहाँ दिखाई देते हैं</h2>
<p>वर्तमान में, affiliate links दो जगहों पर दिखाई देते हैं:</p>
<ul>
<li>साइट के footer में, एक छोटे <code>(affiliate)</code> badge से चिह्नित।</li>
<li>जहाँ कहीं किसी tool का help-block या related-tools section किसी विशिष्ट paid सेवा का उल्लेख करता है जिसकी हम सिफ़ारिश करते हैं — उन मामलों में affiliate को inline बताया जाता है।</li>
</ul>
<p>Affiliate links HTML में <code>rel="sponsored"</code> रखते हैं, जो किसी व्यावसायिक संबंध की घोषणा के लिए search-engine standard है।</p>

<h2>कौन भुगतान करता है</h2>
<p>Commission vendor चुकाता है, आप नहीं। अगर आप affiliate link को नज़रअंदाज़ करके सीधे vendor के homepage से sign up करते हैं, तो आपको वही सेवा उसी क़ीमत पर मिलती है; बस हमें referral नहीं दिखता।</p>

<h2>FTC और EU अनुपालन</h2>
<p>यह page इसलिए मौजूद है क्योंकि US Federal Trade Commission के endorsement guides और EU उपभोक्ता-संरक्षण नियम दोनों ही content creators से माँग करते हैं कि वे किसी linked product के साथ अपने वित्तीय संबंध का खुलासा करें। यह disclosure स्पष्ट और पहले से होना चाहिए — इसी कारण एक top-level page है, और इसी कारण हर page के footer से link है।</p>

<h2>विशिष्ट affiliates</h2>
<p>Toolhub वर्तमान में इन affiliate और support accounts का उपयोग करता है (operator: JXXR1):</p>
<ul>
<li><strong>DigitalOcean</strong> (cloud hosting) — <a href="https://m.do.co/c/05c01e8aec67" target="_blank" rel="noopener sponsored">m.do.co/c/05c01e8aec67</a></li>
<li><strong>GitHub Sponsors</strong> — <a href="https://github.com/sponsors/JXXR1" target="_blank" rel="noopener noreferrer">github.com/sponsors/JXXR1</a></li>
<li><strong>Buy Me a Coffee</strong> — <a href="https://www.buymeacoffee.com/Tool_hub" target="_blank" rel="noopener noreferrer">buymeacoffee.com/Tool_hub</a></li>
</ul>
<p>जब/जैसे ही अन्य affiliate संबंध जोड़े जाते हैं, उन्हें यहाँ सूचीबद्ध किया जाएगा और page की तारीख़ अद्यतन की जाएगी।</p>

<h2>कोई paid placement नहीं</h2>
<p>Tool reviews, homepage पर tools जिस क्रम में दिखाई देते हैं, और हर tool पर "related tools" links affiliate से <strong>नहीं</strong> चलते। हम किसी tool को feature करने के लिए या एक tool को दूसरे से ऊपर रखने के लिए पैसा स्वीकार नहीं करते। अगर कभी paid placement जोड़ा भी जाए (नहीं जोड़ा जाएगा, पर अगर हो भी), तो उसे ठीक उसी तरह label किया जाएगा जैसे affiliate links को: स्पष्ट रूप से, पहले से, संपादकीय सामग्री से अलग पहचाने जाने योग्य।</p>

<h2>संपादकीय स्वतंत्रता</h2>
<p>Affiliate संबंध इस बात को प्रभावित नहीं करते कि कौन से tools बनाए जाते हैं, help-block की सामग्री कैसे लिखी जाती है, या किसी विशेष tool के नीचे कौन से "related tools" दिखाई देते हैं। Toolhub पर tools वही tools हैं जो हम बिना किसी affiliate program के भी बनाते — program केवल hosting और maintenance में थोड़ा सा योगदान करता है।</p>

<h2>संपर्क</h2>
<p>किसी विशिष्ट affiliate के बारे में प्रश्न, या ऐसा कुछ बताना चाहते हैं जो यहाँ नहीं होना चाहिए? <a href="{REPO_URL}">{REPO_URL}</a> पर एक issue खोलें या <a href="/hi/contact/">संपर्क page</a> का उपयोग करें।</p>
""".strip(),
            },
        },
    },
    "companion-tools": {
        "slug": "companion-tools",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "Companion Tools",
                "h1": "Companion Tools",
                "description": "External host-side security tools that complement Toolhub's in-browser utilities. sentinel and skill-scanner — both MIT-licensed open source.",
                "body": f"""
<p class="tagline">Host-side security tools that complement Toolhub's in-browser utilities.</p>

<p>Toolhub is fully browser-based — nothing runs server-side, nothing needs install. These external tools are different: they run on your own machine or server. We list them here because they fit Toolhub's privacy-first ethos and address use cases that genuinely require host-side execution.</p>

<p>All are <strong>built by JXXR1</strong>, the same maintainer as Toolhub. <strong>MIT licensed.</strong> Self-host them. Audit the source. They're not affiliate links — just companion utilities.</p>

<h2>🤖 AI Agents &amp; Harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Security scanner for AI agent skills — 38 modules detecting credential theft, supply-chain attacks, prompt injection, and runtime abuse across any skill bundle.</p>
<p>Works on any skill bundle that ships a SKILL.md or manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkits. With AI agent harnesses proliferating, the supply chain for downloadable agent "skills" is the next frontier for malware injection. skill-scanner statically analyses skill packages across 38 detection modules — pattern matching, AST taint tracking, LLM semantic analysis, YARA rules, and typo-squat detection.</p>
<p>Recent supply-chain wave (v3.4 + v3.5) adds: bundled-content provenance for RAG corpora, external-model-download detection (HuggingFace / replicate / etc.), hash-pinning verification against in-flight tampering, and PGP release-signature verification.</p>
<p class="meta">Stack: bash + JavaScript + Python wrapper + YARA. Host-side execution required. Open source, MIT.</p>
</div>

<h2>🛡️ Security</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Lightweight bash security monitor for Linux servers — six-layer defense covering file access, port exposure, egress allowlist, full audit, stack health, and nightly deep scan. Zero dependencies.</p>
<p>Six-tier latency: file-watch (&lt;1s) · watchdog (&lt;2min) · outbound-guard (&lt;2min) · check-v2+intel (6h) · stack-health (&lt;4h) · daily (24h).</p>
<p>Open-port allowlist · sensitive-service exposure detection · root-process audit · world-writable scan · SSH-key delta · failed-login spike detection · cron/systemd delta · security-stack health (ClamAV / CrowdSec / Wazuh / fail2ban) · CVE-feed intel · supply-chain skill-scanner integration · LLM-vendor egress audit · backup integrity verification · Tailscale posture audit.</p>
<p>v1.9.0 (today) adds two new layers: outbound-guard for egress allowlist enforcement on monitored processes, and stack-health for verifying the security stack itself is alive, fresh, and vocal — not just running.</p>
<p class="meta">Stack: pure bash + inotify + standard Linux utilities. Probes localhost services + reads /etc. Host-side execution required. Open source, MIT.</p>
</div>

<h2>Why these and not just "a list of cool tools"?</h2>

<p>Both are JXXR1's own work. We recommend tools we've built or audited ourselves. Toolhub doesn't publish a "best Linux security tools" listicle — there are plenty of those, and most are SEO farms. This page is a curated handoff for the specific audiences who arrive at Toolhub and need a host-side companion: school IT admins, agent-builders, sysadmins.</p>

<p>If you'd like a tool added: open an issue on the <a href="{REPO_URL}">Toolhub repo</a>. We won't accept paid placements.</p>
""".strip(),
            },
            "de": {
                "title": "Begleit-Tools",
                "h1": "Begleit-Tools",
                "description": "Externe Host-seitige Security-Tools, die Toolhubs Browser-Utilities ergänzen. sentinel und skill-scanner — beide MIT-Open-Source.",
                "body": f"""
<p class="tagline">Host-seitige Security-Tools, die Toolhubs Browser-Utilities ergänzen.</p>

<p>Toolhub läuft komplett im Browser — nichts auf dem Server, keine Installation. Diese externen Tools sind anders: sie laufen auf deinem eigenen Rechner oder Server. Wir listen sie hier, weil sie zu Toolhubs Privacy-First-Haltung passen und Anwendungsfälle abdecken, die wirklich Host-seitige Ausführung brauchen.</p>

<p>Alle sind <strong>von JXXR1 gebaut</strong>, demselben Maintainer wie Toolhub. <strong>MIT-lizenziert.</strong> Self-hoste sie. Prüf den Quellcode. Das sind keine Affiliate-Links — einfach nur Begleit-Werkzeuge.</p>

<h2>🤖 KI-Agenten &amp; Harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Security-Scanner für KI-Agenten-Skills — 38 Module zur Erkennung von Credential-Diebstahl, Supply-Chain-Angriffen, Prompt-Injection und Runtime-Missbrauch in jedem beliebigen Skill-Bundle.</p>
<p>Funktioniert mit jedem Skill-Bundle, das eine SKILL.md oder ein Manifest mitbringt — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP-Toolkits. Da KI-Agenten-Harnesses sich weiter verbreiten, wird die Supply Chain für herunterladbare Agenten-„Skills" zur nächsten Front für Malware-Injektion. skill-scanner analysiert Skill-Pakete statisch über 38 Detection-Module — Pattern-Matching, AST-Taint-Tracking, LLM-Semantik-Analyse, YARA-Regeln und Typo-Squat-Erkennung.</p>
<p>Die letzte Supply-Chain-Welle (v3.4 + v3.5) ergänzt: Provenance für gebündelte RAG-Corpora, Erkennung externer Modell-Downloads (HuggingFace / replicate / etc.), Hash-Pinning gegen In-Flight-Tampering und PGP-Release-Signaturprüfung.</p>
<p class="meta">Stack: bash + JavaScript + Python-Wrapper + YARA. Host-seitige Ausführung nötig. Open Source, MIT.</p>
</div>

<h2>🛡️ Security</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Leichtgewichtiger Bash-Security-Monitor für Linux-Server — sechsstufige Verteidigung für Dateizugriff, Port-Exposure, Egress-Allowlist, Full-Audit, Stack-Health und nächtlichen Deep-Scan. Null Abhängigkeiten.</p>
<p>Sechs Latenz-Stufen: file-watch (&lt;1s) · watchdog (&lt;2 Min) · outbound-guard (&lt;2 Min) · check-v2+intel (6 h) · stack-health (&lt;4 h) · daily (24 h).</p>
<p>Offen-Port-Allowlist · Erkennung exponierter sensibler Dienste · Root-Prozess-Audit · World-Writable-Scan · SSH-Key-Delta · Spike-Erkennung fehlgeschlagener Logins · Cron/systemd-Delta · Security-Stack-Health (ClamAV / CrowdSec / Wazuh / fail2ban) · CVE-Feed-Intel · Supply-Chain-Integration mit skill-scanner · LLM-Vendor-Egress-Audit · Backup-Integritätsprüfung · Tailscale-Posture-Audit.</p>
<p>v1.9.0 (heute) ergänzt zwei neue Schichten: outbound-guard erzwingt die Egress-Allowlist für überwachte Prozesse, und stack-health prüft, dass der Security-Stack selbst aktiv, frisch und vocal ist — nicht nur „läuft".</p>
<p class="meta">Stack: reines bash + inotify + Standard-Linux-Utilities. Prüft Localhost-Dienste + liest /etc. Host-seitige Ausführung nötig. Open Source, MIT.</p>
</div>

<h2>Warum genau diese und nicht einfach „eine Liste cooler Tools"?</h2>

<p>Beide sind JXXR1s eigene Arbeit. Wir empfehlen Tools, die wir selbst gebaut oder geprüft haben. Toolhub veröffentlicht keine „Best Linux Security Tools"-Liste — davon gibt's reichlich, und die meisten sind SEO-Farmen. Diese Seite ist eine kuratierte Übergabe für die konkreten Zielgruppen, die bei Toolhub landen und einen Host-seitigen Begleiter brauchen: Schul-IT-Admins, Agent-Builder, Sysadmins.</p>

<p>Möchtest du ein Tool ergänzt haben? Öffne ein Issue im <a href="{REPO_URL}">Toolhub-Repo</a>. Bezahlte Platzierungen nehmen wir nicht an.</p>
""".strip(),
            },
            "es": {
                "title": "Herramientas complementarias",
                "h1": "Herramientas complementarias",
                "description": "Herramientas de seguridad host-side externas que complementan las utilidades browser de Toolhub. sentinel y skill-scanner — ambas open source MIT.",
                "body": f"""
<p class="tagline">Herramientas de seguridad host-side que complementan las utilidades browser de Toolhub.</p>

<p>Toolhub funciona enteramente en el navegador — nada se ejecuta en servidor, nada hay que instalar. Estas herramientas externas son distintas: se ejecutan en tu propio equipo o servidor. Las listamos aquí porque encajan con la ética privacy-first de Toolhub y cubren casos de uso que realmente requieren ejecución host-side.</p>

<p>Todas están <strong>construidas por JXXR1</strong>, el mismo mantenedor que Toolhub. <strong>Licenciadas MIT.</strong> Hospédalas tú. Audita el código. No son enlaces de afiliado — solo utilidades complementarias.</p>

<h2>🤖 Agentes IA y harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Escáner de seguridad para skills de agentes IA — 38 módulos que detectan robo de credenciales, ataques supply-chain, prompt injection y abuso en runtime en cualquier skill bundle.</p>
<p>Funciona en cualquier skill bundle que traiga un SKILL.md o un manifiesto — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, kits MCP. Con la proliferación de harnesses de agentes IA, la supply chain de "skills" descargables se convierte en la siguiente frontera para inyección de malware. skill-scanner analiza estáticamente paquetes de skills a través de 38 módulos de detección — pattern matching, taint tracking AST, análisis semántico LLM, reglas YARA y detección de typo-squat.</p>
<p>La última oleada supply-chain (v3.4 + v3.5) añade: provenance de contenido empaquetado para corpora RAG, detección de descargas externas de modelos (HuggingFace / replicate / etc.), verificación de hash-pinning contra manipulación en tránsito y verificación de firma PGP de releases.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Requiere ejecución host-side. Open source, MIT.</p>
</div>

<h2>🛡️ Seguridad</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Monitor de seguridad bash ligero para servidores Linux — defensa en seis capas que cubre acceso a ficheros, exposición de puertos, egress allowlist, auditoría completa, salud del stack y escaneo profundo nocturno. Cero dependencias.</p>
<p>Seis niveles de latencia: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6h) · stack-health (&lt;4h) · daily (24h).</p>
<p>Allowlist de puertos abiertos · detección de exposición de servicios sensibles · auditoría de procesos root · escaneo world-writable · delta de claves SSH · detección de picos de logins fallidos · delta cron/systemd · salud del stack de seguridad (ClamAV / CrowdSec / Wazuh / fail2ban) · inteligencia de feed CVE · integración supply-chain con skill-scanner · auditoría egress de proveedores LLM · verificación de integridad de backups · auditoría de postura Tailscale.</p>
<p>v1.9.0 (hoy) añade dos nuevas capas: outbound-guard impone la egress allowlist en los procesos monitorizados, y stack-health verifica que el propio stack de seguridad esté vivo, fresco y vocal — no solo "corriendo".</p>
<p class="meta">Stack: bash puro + inotify + utilidades Linux estándar. Sondea servicios en localhost + lee /etc. Requiere ejecución host-side. Open source, MIT.</p>
</div>

<h2>¿Por qué estas y no simplemente "una lista de herramientas chulas"?</h2>

<p>Las dos son obra del propio JXXR1. Recomendamos herramientas que hemos construido o auditado nosotros mismos. Toolhub no publica un listicle de "las mejores herramientas de seguridad Linux" — de esos hay de sobra, y la mayoría son granjas SEO. Esta página es una entrega curada para los públicos concretos que llegan a Toolhub y necesitan un complemento host-side: administradores IT de centros educativos, constructores de agentes, sysadmins.</p>

<p>¿Quieres que añadamos alguna herramienta? Abre una issue en el <a href="{REPO_URL}">repo de Toolhub</a>. No aceptamos colocaciones pagadas.</p>
""".strip(),
            },
            "fr": {
                "title": "Outils complémentaires",
                "h1": "Outils complémentaires",
                "description": "Outils de sécurité host-side externes qui complètent les utilitaires navigateur de Toolhub. sentinel et skill-scanner — open source MIT tous les deux.",
                "body": f"""
<p class="tagline">Outils de sécurité host-side qui complètent les utilitaires navigateur de Toolhub.</p>

<p>Toolhub tourne entièrement dans le navigateur — rien côté serveur, rien à installer. Ces outils externes sont différents : ils tournent sur ta propre machine ou ton propre serveur. On les liste ici parce qu'ils collent à l'éthique privacy-first de Toolhub et qu'ils répondent à des usages qui exigent vraiment une exécution côté hôte.</p>

<p>Tous sont <strong>construits par JXXR1</strong>, le même mainteneur que Toolhub. <strong>Sous licence MIT.</strong> Auto-héberge-les. Audite le code. Ce ne sont pas des liens d'affiliation — juste des utilitaires complémentaires.</p>

<h2>🤖 Agents IA et harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Scanner de sécurité pour skills d'agents IA — 38 modules détectant le vol d'identifiants, les attaques supply-chain, le prompt injection et l'abus en runtime sur n'importe quel skill bundle.</p>
<p>Fonctionne sur n'importe quel skill bundle qui livre un SKILL.md ou un manifeste — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkits. Avec la prolifération des harnesses d'agents IA, la supply chain des « skills » téléchargeables devient la prochaine frontière pour l'injection de malware. skill-scanner analyse statiquement les paquets de skills via 38 modules de détection — pattern matching, taint tracking AST, analyse sémantique LLM, règles YARA et détection de typo-squat.</p>
<p>La dernière vague supply-chain (v3.4 + v3.5) ajoute : provenance du contenu embarqué pour les corpora RAG, détection des téléchargements externes de modèles (HuggingFace / replicate / etc.), hash-pinning contre les altérations en transit et vérification de signature PGP des releases.</p>
<p class="meta">Stack : bash + JavaScript + wrapper Python + YARA. Exécution côté hôte requise. Open source, MIT.</p>
</div>

<h2>🛡️ Sécurité</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Moniteur de sécurité bash léger pour serveurs Linux — défense à six couches couvrant l'accès fichier, l'exposition des ports, l'egress allowlist, l'audit complet, la santé du stack et le scan profond nocturne. Zéro dépendance.</p>
<p>Six paliers de latence : file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6 h) · stack-health (&lt;4 h) · daily (24 h).</p>
<p>Allowlist des ports ouverts · détection d'exposition de services sensibles · audit des processus root · scan world-writable · delta des clés SSH · détection de pics de logins échoués · delta cron/systemd · santé du stack de sécurité (ClamAV / CrowdSec / Wazuh / fail2ban) · intel de feed CVE · intégration supply-chain avec skill-scanner · audit de sortie des fournisseurs LLM · vérification d'intégrité des sauvegardes · audit de posture Tailscale.</p>
<p>v1.9.0 (aujourd'hui) ajoute deux nouvelles couches : outbound-guard impose l'egress allowlist sur les processus surveillés, et stack-health vérifie que le stack de sécurité lui-même est vivant, frais et vocal — pas juste « en marche ».</p>
<p class="meta">Stack : bash pur + inotify + utilitaires Linux standard. Sonde les services localhost + lit /etc. Exécution côté hôte requise. Open source, MIT.</p>
</div>

<h2>Pourquoi ceux-là et pas juste « une liste d'outils sympas » ?</h2>

<p>Les deux sont le travail propre de JXXR1. On recommande des outils qu'on a construits ou audités nous-mêmes. Toolhub ne publie pas de listicle « meilleurs outils de sécurité Linux » — il y en a déjà à la pelle, et la plupart sont des fermes SEO. Cette page est une passation soignée pour les publics précis qui atterrissent sur Toolhub et ont besoin d'un complément côté hôte : admins IT scolaires, constructeurs d'agents, sysadmins.</p>

<p>Tu veux qu'un outil soit ajouté ? Ouvre une issue sur le <a href="{REPO_URL}">repo Toolhub</a>. On n'accepte pas de placements payés.</p>
""".strip(),
            },
            "it": {
                "title": "Strumenti complementari",
                "h1": "Strumenti complementari",
                "description": "Strumenti di sicurezza host-side esterni che completano le utility browser di Toolhub. sentinel e skill-scanner — entrambi open source MIT.",
                "body": f"""
<p class="tagline">Strumenti di sicurezza host-side che completano le utility browser di Toolhub.</p>

<p>Toolhub gira interamente nel browser — niente lato server, niente da installare. Questi strumenti esterni sono diversi: girano sulla tua macchina o sul tuo server. Li elenchiamo qui perché si allineano all'etica privacy-first di Toolhub e coprono casi d'uso che richiedono davvero l'esecuzione host-side.</p>

<p>Sono tutti <strong>costruiti da JXXR1</strong>, lo stesso maintainer di Toolhub. <strong>Licenza MIT.</strong> Self-hostali. Controlla il codice. Non sono link affiliati — solo utility complementari.</p>

<h2>🤖 Agenti IA e harness</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Scanner di sicurezza per skill di agenti IA — 38 moduli che rilevano furto di credenziali, attacchi supply-chain, prompt injection e abuso a runtime su qualsiasi skill bundle.</p>
<p>Funziona su qualsiasi skill bundle che porti uno SKILL.md o un manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkit. Con il proliferare degli harness per agenti IA, la supply chain delle "skill" scaricabili diventa la prossima frontiera per l'iniezione di malware. skill-scanner analizza staticamente i pacchetti di skill attraverso 38 moduli di rilevamento — pattern matching, taint tracking AST, analisi semantica LLM, regole YARA e rilevamento typo-squat.</p>
<p>L'ultima ondata supply-chain (v3.4 + v3.5) aggiunge: provenance dei contenuti bundlati per i corpora RAG, rilevamento dei download esterni di modelli (HuggingFace / replicate / ecc.), verifica hash-pinning contro le manomissioni in transito e verifica firma PGP delle release.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Richiede esecuzione host-side. Open source, MIT.</p>
</div>

<h2>🛡️ Sicurezza</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Monitor di sicurezza bash leggero per server Linux — difesa a sei livelli che copre accesso ai file, esposizione delle porte, egress allowlist, audit completo, salute dello stack e scansione profonda notturna. Zero dipendenze.</p>
<p>Sei livelli di latenza: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6h) · stack-health (&lt;4h) · daily (24h).</p>
<p>Allowlist delle porte aperte · rilevamento esposizione servizi sensibili · audit dei processi root · scansione world-writable · delta delle chiavi SSH · rilevamento picchi di login falliti · delta cron/systemd · salute dello stack di sicurezza (ClamAV / CrowdSec / Wazuh / fail2ban) · intel CVE feed · integrazione supply-chain con skill-scanner · audit egress dei vendor LLM · verifica integrità dei backup · audit di postura Tailscale.</p>
<p>v1.9.0 (oggi) aggiunge due nuovi livelli: outbound-guard impone l'egress allowlist sui processi monitorati, e stack-health verifica che lo stack di sicurezza stesso sia vivo, fresco e vocal — non solo "in esecuzione".</p>
<p class="meta">Stack: bash puro + inotify + utility Linux standard. Sonda i servizi localhost + legge /etc. Richiede esecuzione host-side. Open source, MIT.</p>
</div>

<h2>Perché proprio questi e non semplicemente "una lista di tool fighi"?</h2>

<p>Entrambi sono lavoro proprio di JXXR1. Consigliamo strumenti che abbiamo costruito o auditato noi stessi. Toolhub non pubblica un listicle "i migliori strumenti di sicurezza Linux" — ce ne sono già a bizzeffe, e la maggior parte sono SEO farm. Questa pagina è una consegna curata per i pubblici specifici che arrivano su Toolhub e hanno bisogno di un complemento host-side: admin IT scolastici, agent-builder, sysadmin.</p>

<p>Vuoi che venga aggiunto uno strumento? Apri una issue sul <a href="{REPO_URL}">repo di Toolhub</a>. Non accettiamo posizionamenti a pagamento.</p>
""".strip(),
            },
            "pt": {
                "title": "Ferramentas complementares",
                "h1": "Ferramentas complementares",
                "description": "Ferramentas de segurança host-side externas que complementam as utilidades browser do Toolhub. sentinel e skill-scanner — ambas open source MIT.",
                "body": f"""
<p class="tagline">Ferramentas de segurança host-side que complementam as utilidades browser do Toolhub.</p>

<p>O Toolhub roda inteiramente no browser — nada do lado servidor, nada precisa instalar. Essas ferramentas externas são diferentes: rodam na sua própria máquina ou servidor. A gente lista elas aqui porque combinam com a ética privacy-first do Toolhub e cobrem casos de uso que realmente exigem execução host-side.</p>

<p>Todas foram <strong>feitas pelo JXXR1</strong>, o mesmo mantenedor do Toolhub. <strong>Licença MIT.</strong> Hospede você mesmo. Audite o código. Não são links de afiliado — são só utilitários complementares.</p>

<h2>🤖 Agentes IA e harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Scanner de segurança para skills de agentes IA — 38 módulos detectando roubo de credenciais, ataques supply-chain, prompt injection e abuso em runtime em qualquer skill bundle.</p>
<p>Funciona em qualquer skill bundle que traga um SKILL.md ou manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, kits MCP. Com a proliferação dos harnesses de agentes IA, a supply chain das "skills" baixáveis vira a próxima fronteira para injeção de malware. O skill-scanner analisa estaticamente pacotes de skill em 38 módulos de detecção — pattern matching, taint tracking AST, análise semântica LLM, regras YARA e detecção de typo-squat.</p>
<p>A última leva supply-chain (v3.4 + v3.5) adiciona: provenance de conteúdo bundlado pra corpora RAG, detecção de downloads externos de modelos (HuggingFace / replicate / etc.), verificação de hash-pinning contra adulteração em trânsito e verificação de assinatura PGP de release.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Execução host-side necessária. Open source, MIT.</p>
</div>

<h2>🛡️ Segurança</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Monitor de segurança bash leve para servidores Linux — defesa em seis camadas cobrindo acesso a arquivos, exposição de portas, egress allowlist, auditoria completa, saúde do stack e varredura profunda noturna. Zero dependências.</p>
<p>Seis níveis de latência: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6h) · stack-health (&lt;4h) · daily (24h).</p>
<p>Allowlist de portas abertas · detecção de exposição de serviços sensíveis · auditoria de processos root · varredura world-writable · delta de chaves SSH · detecção de picos de logins falhos · delta cron/systemd · saúde do stack de segurança (ClamAV / CrowdSec / Wazuh / fail2ban) · intel de feed CVE · integração supply-chain com skill-scanner · auditoria de egress de vendors LLM · verificação de integridade de backup · auditoria de postura Tailscale.</p>
<p>v1.9.0 (hoje) adiciona duas novas camadas: outbound-guard impõe a egress allowlist nos processos monitorados, e stack-health verifica se o próprio stack de segurança está vivo, fresco e vocal — não só "rodando".</p>
<p class="meta">Stack: bash puro + inotify + utilitários Linux padrão. Sonda serviços localhost + lê /etc. Execução host-side necessária. Open source, MIT.</p>
</div>

<h2>Por que essas e não só "uma lista de ferramentas legais"?</h2>

<p>As duas são trabalho do próprio JXXR1. Recomendamos ferramentas que a gente mesmo construiu ou auditou. O Toolhub não publica listicle "melhores ferramentas de segurança Linux" — disso já tem aos montes e a maioria é fazenda de SEO. Essa página é uma passagem curada pros públicos específicos que chegam ao Toolhub e precisam de um complemento host-side: admins de TI escolar, agent-builders, sysadmins.</p>

<p>Quer que alguma ferramenta seja adicionada? Abra uma issue no <a href="{REPO_URL}">repo do Toolhub</a>. Não aceitamos colocações pagas.</p>
""".strip(),
            },
            "pl": {
                "title": "Narzędzia uzupełniające",
                "h1": "Narzędzia uzupełniające",
                "description": "Zewnętrzne narzędzia bezpieczeństwa host-side uzupełniające utility przeglądarkowe Toolhub. sentinel i skill-scanner — oba open source MIT.",
                "body": f"""
<p class="tagline">Narzędzia bezpieczeństwa host-side, które uzupełniają utility przeglądarkowe Toolhub.</p>

<p>Toolhub działa w całości w przeglądarce — nic po stronie serwera, nic do instalowania. Te zewnętrzne narzędzia są inne: działają na twojej własnej maszynie albo serwerze. Wymieniamy je tu, bo pasują do privacy-first etosu Toolhub i obsługują przypadki, które naprawdę wymagają wykonania po stronie hosta.</p>

<p>Wszystkie <strong>zbudowane przez JXXR1</strong>, tego samego maintainera co Toolhub. <strong>Licencja MIT.</strong> Hostuj je sam. Audytuj kod. To nie linki afiliacyjne — po prostu narzędzia towarzyszące.</p>

<h2>🤖 Agenci AI i harnesy</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Skaner bezpieczeństwa dla skille agentów AI — 38 modułów wykrywających kradzież poświadczeń, ataki supply-chain, prompt injection i nadużycia w czasie wykonania w dowolnym skill bundle.</p>
<p>Działa na każdym skill bundle, który dostarcza plik SKILL.md lub manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, zestawy MCP. Wraz z rozprzestrzenianiem się harnesów agentów AI, supply chain pobieranych „skilli" staje się następną granicą dla wstrzykiwania malware'u. skill-scanner analizuje statycznie pakiety skille przez 38 modułów detekcji — pattern matching, taint tracking AST, analiza semantyczna LLM, reguły YARA i detekcja typo-squatów.</p>
<p>Ostatnia fala supply-chain (v3.4 + v3.5) dodaje: provenance bundlowanej zawartości dla korporów RAG, detekcję zewnętrznych pobrań modeli (HuggingFace / replicate / itp.), weryfikację hash-pinning przeciw manipulacji w locie oraz weryfikację podpisu PGP wydań.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Wymagane wykonanie host-side. Open source, MIT.</p>
</div>

<h2>🛡️ Bezpieczeństwo</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Lekki bashowy monitor bezpieczeństwa do serwerów Linux — sześciowarstwowa obrona obejmująca dostęp do plików, ekspozycję portów, egress allowlist, pełny audyt, zdrowie stacka i nocny głęboki skan. Zero zależności.</p>
<p>Sześć poziomów opóźnienia: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6h) · stack-health (&lt;4h) · daily (24h).</p>
<p>Allowlist otwartych portów · detekcja ekspozycji wrażliwych usług · audyt procesów root · skan world-writable · delta kluczy SSH · detekcja skoków nieudanych logowań · delta cron/systemd · zdrowie stacka bezpieczeństwa (ClamAV / CrowdSec / Wazuh / fail2ban) · intel feedu CVE · integracja supply-chain ze skill-scannerem · audyt egress dostawców LLM · weryfikacja integralności backupów · audyt postury Tailscale.</p>
<p>v1.9.0 (dziś) dodaje dwie nowe warstwy: outbound-guard wymusza egress allowlist na monitorowanych procesach, a stack-health weryfikuje, że sam stack bezpieczeństwa jest żywy, świeży i głośny — nie tylko „uruchomiony".</p>
<p class="meta">Stack: czysty bash + inotify + standardowe utility Linux. Sonduje usługi localhost + czyta /etc. Wymagane wykonanie host-side. Open source, MIT.</p>
</div>

<h2>Dlaczego akurat te, a nie po prostu „lista fajnych narzędzi"?</h2>

<p>Oba to praca JXXR1-a. Polecamy narzędzia, które sami zbudowaliśmy lub audytowaliśmy. Toolhub nie publikuje listicle „najlepsze narzędzia bezpieczeństwa Linux" — takich już jest mnóstwo, a większość to farmy SEO. Ta strona to skuratorowany handoff dla konkretnych odbiorców, którzy trafiają do Toolhub i potrzebują host-side towarzysza: szkolni admini IT, agent-builderzy, sysadmini.</p>

<p>Chcesz, żebyśmy dodali jakieś narzędzie? Otwórz issue w <a href="{REPO_URL}">repozytorium Toolhub</a>. Płatnych pozycjonowań nie przyjmujemy.</p>
""".strip(),
            },
            "ja": {
                "title": "コンパニオンツール",
                "h1": "コンパニオンツール",
                "description": "Toolhubのブラウザユーティリティを補完するホスト側のセキュリティツール群。sentinel と skill-scanner — どちらも MITライセンスのオープンソース。",
                "body": f"""
<p class="tagline">Toolhub のブラウザ内ユーティリティを補完するホスト側セキュリティツール。</p>

<p>Toolhub は完全にブラウザベースで動作します — サーバー側で動くものは何もなく、インストールも不要です。ここで紹介する外部ツールは事情が異なります。あなた自身のマシンやサーバー上で動作するツールです。これらをここに掲載するのは、Toolhub のプライバシーファースト姿勢と合致し、なおかつ本当にホスト側実行が必要な用途をカバーしているからです。</p>

<p>すべて <strong>JXXR1 が開発</strong>しました — Toolhub と同じメンテナーです。<strong>MIT ライセンス。</strong>セルフホストしてください。ソースを監査してください。これらはアフィリエイトリンクではありません — 純粋なコンパニオンユーティリティです。</p>

<h2>🤖 AIエージェントとハーネス</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">AI エージェントのスキル向けセキュリティスキャナ — 認証情報窃取、サプライチェーン攻撃、プロンプトインジェクション、ランタイム不正利用を検出する 38 モジュール。あらゆるスキルバンドルに対応。</p>
<p>SKILL.md やマニフェストを同梱するあらゆるスキルバンドルで動作します — Claude Code、OpenClaw、AgentPress、Hermes Skills Hub、MCP ツールキットなど。AI エージェントハーネスが普及するにつれて、ダウンロード可能なエージェント「スキル」のサプライチェーンはマルウェア注入の次のフロンティアになっています。skill-scanner はスキルパッケージを 38 の検出モジュール — パターンマッチ、AST テイントトラッキング、LLM 意味解析、YARA ルール、タイポスクワット検出 — で静的解析します。</p>
<p>直近のサプライチェーン対応波（v3.4 + v3.5）で追加されたもの: RAG コーパス向けバンドルコンテンツの由来検証、外部モデルダウンロード検出（HuggingFace / replicate ほか）、ハッシュピン検証による転送中改ざん検知、PGP リリース署名検証。</p>
<p class="meta">スタック: bash + JavaScript + Python ラッパー + YARA。ホスト側実行が必要です。オープンソース、MIT ライセンス。</p>
</div>

<h2>🛡️ セキュリティ</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Linux サーバー向けの軽量 bash セキュリティモニター — ファイルアクセス、ポート露出、egress 許可リスト、フル監査、スタック健全性、夜間ディープスキャンを 6 層で防御。ゼロ依存。</p>
<p>6 段階のレイテンシ: file-watch (&lt;1s) ・ watchdog (&lt;2 分) ・ outbound-guard (&lt;2 分) ・ check-v2+intel (6 h) ・ stack-health (&lt;4 h) ・ daily (24 h)。</p>
<p>開放ポート許可リスト ・ 機微サービス露出検出 ・ root プロセス監査 ・ world-writable スキャン ・ SSH 鍵差分 ・ ログイン失敗スパイク検出 ・ cron/systemd 差分 ・ セキュリティスタック健全性（ClamAV / CrowdSec / Wazuh / fail2ban） ・ CVE フィードインテル ・ skill-scanner との供給網連携 ・ LLM ベンダーへの egress 監査 ・ バックアップ整合性検証 ・ Tailscale ポスチャ監査。</p>
<p>v1.9.0（本日リリース）は 2 つの新レイヤーを追加します: outbound-guard は監視対象プロセスに egress 許可リストを強制し、stack-health はセキュリティスタック自体が「動いている」だけでなく、生きていて、新鮮で、声を出している（=アラート可能な）状態であることを確認します。</p>
<p class="meta">スタック: 純 bash + inotify + 標準 Linux ユーティリティ。localhost サービスをプローブし /etc を読みます。ホスト側実行が必要です。オープンソース、MIT。</p>
</div>

<h2>なぜ「クールなツールのリスト」ではなく、この 2 つなのか</h2>

<p>どちらも JXXR1 自身の作品です。Toolhub は自分たちが作ったか監査したツールしか勧めません。「Linux セキュリティツール ベスト n」のような listicle は出しません — そういう記事は山ほどあり、ほとんどが SEO ファームです。このページは、Toolhub に辿り着いてホスト側コンパニオンを必要とする特定の層 — 学校 IT 管理者、エージェント開発者、システム管理者 — への厳選された受け渡しです。</p>

<p>追加してほしいツールがありますか？ <a href="{REPO_URL}">Toolhub リポジトリ</a>で issue を開いてください。有料掲載は受け付けません。</p>
""".strip(),
            },
            "nl": {
                "title": "Aanvullende tools",
                "h1": "Aanvullende tools",
                "description": "Externe host-side security-tools die de browser-utilities van Toolhub aanvullen. sentinel en skill-scanner — beide MIT-open-source.",
                "body": f"""
<p class="tagline">Host-side security-tools die de browser-utilities van Toolhub aanvullen.</p>

<p>Toolhub draait volledig in de browser — niks aan de serverkant, niks te installeren. Deze externe tools zijn anders: ze draaien op je eigen machine of server. We zetten ze hier omdat ze passen bij de privacy-first-ethos van Toolhub en omdat ze use cases dekken waarvoor host-side uitvoering écht nodig is.</p>

<p>Alle zijn <strong>gebouwd door JXXR1</strong>, dezelfde maintainer als Toolhub. <strong>MIT-licentie.</strong> Self-host ze. Audit de broncode. Het zijn geen affiliate links — gewoon aanvullende utilities.</p>

<h2>🤖 AI-agents &amp; harnesses</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Security-scanner voor AI-agent skills — 38 modules die credential-diefstal, supply-chain-aanvallen, prompt injection en runtime-misbruik detecteren in elke skill bundle.</p>
<p>Werkt op elke skill bundle die een SKILL.md of manifest meelevert — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP-toolkits. Nu AI-agent harnesses zich verder verspreiden wordt de supply chain voor downloadbare agent-„skills" het volgende slagveld voor malware-injectie. skill-scanner analyseert skill-pakketten statisch met 38 detectiemodules — pattern matching, AST taint tracking, LLM-semantische analyse, YARA-regels en typo-squat-detectie.</p>
<p>De laatste supply-chain-golf (v3.4 + v3.5) voegt toe: provenance van gebundelde content voor RAG-corpora, detectie van externe modeldownloads (HuggingFace / replicate / etc.), hash-pinning-verificatie tegen manipulatie onderweg en PGP-release-handtekeningverificatie.</p>
<p class="meta">Stack: bash + JavaScript + Python-wrapper + YARA. Host-side uitvoering vereist. Open source, MIT.</p>
</div>

<h2>🛡️ Security</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Lichtgewicht bash-security-monitor voor Linux-servers — zeslaagse verdediging die bestandstoegang, port-exposure, egress-allowlist, volledige audit, stack-gezondheid en nachtelijke deep-scan dekt. Nul afhankelijkheden.</p>
<p>Zes latentielagen: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6 u) · stack-health (&lt;4 u) · daily (24 u).</p>
<p>Open-port-allowlist · detectie van blootgestelde gevoelige services · root-procesaudit · world-writable-scan · SSH-key-delta · spike-detectie van mislukte logins · cron/systemd-delta · gezondheid van de security-stack (ClamAV / CrowdSec / Wazuh / fail2ban) · CVE-feed-intel · supply-chain-integratie met skill-scanner · LLM-vendor egress-audit · backup-integriteitscontrole · Tailscale-posture-audit.</p>
<p>v1.9.0 (vandaag) voegt twee nieuwe lagen toe: outbound-guard dwingt de egress-allowlist af op gemonitorde processen, en stack-health verifieert dat de security-stack zelf actief, vers en vocaal is — niet alleen maar „draaiend".</p>
<p class="meta">Stack: puur bash + inotify + standaard Linux-utilities. Polt localhost-services + leest /etc. Host-side uitvoering vereist. Open source, MIT.</p>
</div>

<h2>Waarom deze en niet gewoon „een lijstje met coole tools"?</h2>

<p>Beide zijn werk van JXXR1 zelf. We bevelen tools aan die we zelf hebben gebouwd of geauditeerd. Toolhub publiceert geen „beste Linux security-tools"-listicle — daarvan zijn er meer dan genoeg, en de meeste zijn SEO-farms. Deze pagina is een doordachte overdracht naar de specifieke doelgroepen die op Toolhub landen en een host-side aanvulling nodig hebben: school-IT-admins, agent-bouwers, sysadmins.</p>

<p>Wil je dat we een tool toevoegen? Open een issue op de <a href="{REPO_URL}">Toolhub-repo</a>. Betaalde plaatsingen accepteren we niet.</p>
""".strip(),
            },
            "tr": {
                "title": "Tamamlayıcı araçlar",
                "h1": "Tamamlayıcı araçlar",
                "description": "Toolhub'ın tarayıcı tabanlı araçlarını tamamlayan harici, host-side güvenlik araçları. sentinel ve skill-scanner — ikisi de MIT lisanslı açık kaynak.",
                "body": f"""
<p class="tagline">Toolhub'ın tarayıcı içi araçlarını tamamlayan host-side güvenlik araçları.</p>

<p>Toolhub tamamen tarayıcıda çalışır — sunucu tarafında hiçbir şey yok, kurulum gerekmez. Bu harici araçlar farklıdır: kendi makinende ya da sunucunda çalışırlar. Onları burada listeliyoruz çünkü Toolhub'ın privacy-first anlayışıyla örtüşüyorlar ve gerçekten host-side yürütme isteyen kullanım durumlarını karşılıyorlar.</p>

<p>Hepsi <strong>JXXR1 tarafından inşa edildi</strong>, Toolhub'ın maintainer'ıyla aynı kişi. <strong>MIT lisanslı.</strong> Sen kendin host et. Kaynağı denetle. Bunlar affiliate link değil — sadece tamamlayıcı araçlar.</p>

<h2>🤖 AI ajanlar ve harness'lar</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">AI ajan skill'leri için güvenlik tarayıcı — kimlik bilgisi hırsızlığı, supply-chain saldırıları, prompt injection ve runtime istismarını tespit eden 38 modül; herhangi bir skill bundle üzerinde çalışır.</p>
<p>SKILL.md veya manifest dosyası taşıyan herhangi bir skill bundle üzerinde çalışır — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkit'leri. AI ajan harness'ları yaygınlaştıkça, indirilebilir ajan „skill"lerinin supply chain'i malware enjeksiyonu için bir sonraki cephe haline geliyor. skill-scanner, skill paketlerini 38 detection modülü üzerinden statik olarak analiz ediyor — pattern matching, AST taint tracking, LLM semantik analiz, YARA kuralları ve typo-squat tespiti.</p>
<p>Son supply-chain dalgası (v3.4 + v3.5) şunları ekliyor: RAG corpus'ları için bundle'lanmış içerik provenance'ı, dış model indirme tespiti (HuggingFace / replicate / vs.), aktarım sırasında oynamaya karşı hash-pinning doğrulaması ve PGP release imza doğrulaması.</p>
<p class="meta">Stack: bash + JavaScript + Python wrapper + YARA. Host-side yürütme gerektirir. Açık kaynak, MIT.</p>
</div>

<h2>🛡️ Güvenlik</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Linux sunucuları için hafif bash güvenlik monitörü — dosya erişimi, port maruziyeti, egress allowlist, tam audit, stack sağlığı ve gecelik derin tarama için altı katmanlı savunma. Sıfır bağımlılık.</p>
<p>Altı gecikme katmanı: file-watch (&lt;1s) · watchdog (&lt;2 dk) · outbound-guard (&lt;2 dk) · check-v2+intel (6 sa) · stack-health (&lt;4 sa) · daily (24 sa).</p>
<p>Açık port allowlist · hassas servis maruziyet tespiti · root süreç denetimi · world-writable taraması · SSH key delta · başarısız giriş sıçraması tespiti · cron/systemd delta · güvenlik stack sağlığı (ClamAV / CrowdSec / Wazuh / fail2ban) · CVE feed intel · skill-scanner ile supply-chain entegrasyonu · LLM vendor egress denetimi · yedek bütünlük doğrulaması · Tailscale postur denetimi.</p>
<p>v1.9.0 (bugün) iki yeni katman ekliyor: outbound-guard izlenen süreçlerde egress allowlist'i zorlar, ve stack-health güvenlik stack'inin kendisinin canlı, taze ve sesli (alarm üretebilir) olduğunu doğrular — sadece „çalışır halde" değil.</p>
<p class="meta">Stack: saf bash + inotify + standart Linux araçları. Localhost servislerini prob eder, /etc'yi okur. Host-side yürütme gerektirir. Açık kaynak, MIT.</p>
</div>

<h2>Neden bunlar, neden „havalı araçlar listesi" değil?</h2>

<p>İkisi de JXXR1'ın kendi işi. Sadece kendimizin inşa ettiği ya da denetlediği araçları öneriyoruz. Toolhub „en iyi Linux güvenlik araçları" türünden bir listicle yayımlamıyor — bunlardan zaten bol var ve çoğu SEO çiftliği. Bu sayfa, Toolhub'a gelip host-side bir tamamlayıcıya ihtiyacı olan belirli kitlelere yapılmış kürate bir aktarım: okul IT yöneticileri, ajan geliştiricileri, sistem yöneticileri.</p>

<p>Bir aracın eklenmesini ister misin? <a href="{REPO_URL}">Toolhub repo</a>'sunda bir issue aç. Ücretli yerleşimleri kabul etmiyoruz.</p>
""".strip(),
            },
            "id": {
                "title": "Alat pendamping",
                "h1": "Alat pendamping",
                "description": "Alat keamanan host-side eksternal yang melengkapi utilitas berbasis browser Toolhub. sentinel dan skill-scanner — keduanya open source MIT.",
                "body": f"""
<p class="tagline">Alat keamanan host-side yang melengkapi utilitas dalam-browser Toolhub.</p>

<p>Toolhub berjalan sepenuhnya di browser — tidak ada yang berjalan di sisi server, tidak perlu instalasi. Alat-alat eksternal ini berbeda: mereka berjalan di mesin atau server kamu sendiri. Kami daftarkan di sini karena cocok dengan etos privacy-first Toolhub dan menangani use case yang benar-benar membutuhkan eksekusi host-side.</p>

<p>Semuanya <strong>dibangun oleh JXXR1</strong>, maintainer yang sama dengan Toolhub. <strong>Lisensi MIT.</strong> Hosting sendiri. Audit kodenya. Ini bukan link afiliasi — hanya utilitas pendamping.</p>

<h2>🤖 AI Agent &amp; Harness</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Pemindai keamanan untuk skill agen AI — 38 modul mendeteksi pencurian kredensial, serangan supply-chain, prompt injection, dan penyalahgunaan runtime di skill bundle apa pun.</p>
<p>Bekerja di skill bundle apa pun yang menyertakan SKILL.md atau manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkit. Seiring meluasnya harness agen AI, supply chain untuk „skill" agen yang dapat diunduh menjadi medan berikutnya untuk injeksi malware. skill-scanner menganalisis paket skill secara statis melalui 38 modul deteksi — pattern matching, AST taint tracking, analisis semantik LLM, aturan YARA, dan deteksi typo-squat.</p>
<p>Gelombang supply-chain terbaru (v3.4 + v3.5) menambahkan: provenance konten bundled untuk korpus RAG, deteksi unduhan model eksternal (HuggingFace / replicate / dll.), verifikasi hash-pinning terhadap perubahan dalam transit, dan verifikasi tanda tangan PGP rilis.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Eksekusi host-side diperlukan. Open source, MIT.</p>
</div>

<h2>🛡️ Keamanan</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Monitor keamanan bash yang ringan untuk server Linux — pertahanan enam lapis mencakup akses berkas, paparan port, egress allowlist, audit penuh, kesehatan stack, dan pemindaian dalam malam hari. Tanpa dependensi.</p>
<p>Enam tingkat latensi: file-watch (&lt;1d) · watchdog (&lt;2 mnt) · outbound-guard (&lt;2 mnt) · check-v2+intel (6 jam) · stack-health (&lt;4 jam) · daily (24 jam).</p>
<p>Allowlist port terbuka · deteksi paparan layanan sensitif · audit proses root · pemindaian world-writable · delta kunci SSH · deteksi lonjakan login gagal · delta cron/systemd · kesehatan stack keamanan (ClamAV / CrowdSec / Wazuh / fail2ban) · intel feed CVE · integrasi supply-chain dengan skill-scanner · audit egress vendor LLM · verifikasi integritas backup · audit postur Tailscale.</p>
<p>v1.9.0 (hari ini) menambah dua lapis baru: outbound-guard menegakkan egress allowlist pada proses yang dipantau, dan stack-health memverifikasi bahwa stack keamanan itu sendiri hidup, segar, dan vokal — bukan sekadar „berjalan".</p>
<p class="meta">Stack: bash murni + inotify + utilitas Linux standar. Memeriksa layanan localhost + membaca /etc. Eksekusi host-side diperlukan. Open source, MIT.</p>
</div>

<h2>Kenapa dua ini dan bukan sekadar „daftar alat keren"?</h2>

<p>Keduanya karya JXXR1 sendiri. Kami merekomendasikan alat yang kami bangun atau audit sendiri. Toolhub tidak menerbitkan listicle „alat keamanan Linux terbaik" — sudah banyak yang seperti itu dan sebagian besar adalah SEO farm. Halaman ini adalah serah-terima kurasi untuk audiens spesifik yang mendarat di Toolhub dan butuh pendamping host-side: admin IT sekolah, pembangun agen, sysadmin.</p>

<p>Ingin alat tertentu ditambahkan? Buka issue di <a href="{REPO_URL}">repo Toolhub</a>. Kami tidak menerima placement berbayar.</p>
""".strip(),
            },
            "vi": {
                "title": "Công cụ bổ sung",
                "h1": "Công cụ bổ sung",
                "description": "Các công cụ bảo mật host-side bên ngoài bổ sung cho các tiện ích chạy trên trình duyệt của Toolhub. sentinel và skill-scanner — cả hai đều mã nguồn mở MIT.",
                "body": f"""
<p class="tagline">Công cụ bảo mật host-side bổ sung cho các tiện ích chạy trong trình duyệt của Toolhub.</p>

<p>Toolhub chạy hoàn toàn trên trình duyệt — không có gì chạy ở phía máy chủ, không cần cài đặt. Các công cụ bên ngoài này thì khác: chúng chạy trên máy hoặc máy chủ của chính bạn. Chúng tôi liệt kê chúng ở đây vì chúng phù hợp với tinh thần privacy-first của Toolhub và đáp ứng những trường hợp sử dụng thực sự đòi hỏi thực thi phía host.</p>

<p>Tất cả đều <strong>do JXXR1 xây dựng</strong>, cùng một maintainer với Toolhub. <strong>Giấy phép MIT.</strong> Tự host. Tự audit mã nguồn. Đây không phải liên kết affiliate — chỉ là các tiện ích đi kèm.</p>

<h2>🤖 AI agent và harness</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Trình quét bảo mật cho skill của AI agent — 38 module phát hiện đánh cắp thông tin xác thực, tấn công supply-chain, prompt injection và lạm dụng tại runtime trên bất kỳ skill bundle nào.</p>
<p>Hoạt động trên bất kỳ skill bundle nào có sẵn SKILL.md hoặc manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, các MCP toolkit. Khi các harness AI agent ngày càng nhiều, supply chain của các „skill" có thể tải xuống trở thành chiến tuyến tiếp theo cho việc tiêm malware. skill-scanner phân tích tĩnh các gói skill qua 38 module phát hiện — pattern matching, AST taint tracking, phân tích ngữ nghĩa LLM, luật YARA và phát hiện typo-squat.</p>
<p>Đợt supply-chain gần đây nhất (v3.4 + v3.5) bổ sung: provenance nội dung được bundle cho corpus RAG, phát hiện tải mô hình bên ngoài (HuggingFace / replicate / v.v.), xác minh hash-pinning chống can thiệp trong khi truyền và xác minh chữ ký PGP của bản phát hành.</p>
<p class="meta">Stack: bash + JavaScript + wrapper Python + YARA. Yêu cầu thực thi host-side. Mã nguồn mở, MIT.</p>
</div>

<h2>🛡️ Bảo mật</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Monitor bảo mật bash nhẹ cho máy chủ Linux — phòng thủ sáu lớp bao trùm truy cập tệp, phơi nhiễm cổng, egress allowlist, audit đầy đủ, sức khỏe stack và quét sâu hằng đêm. Không phụ thuộc.</p>
<p>Sáu mức độ trễ: file-watch (&lt;1s) · watchdog (&lt;2 phút) · outbound-guard (&lt;2 phút) · check-v2+intel (6 giờ) · stack-health (&lt;4 giờ) · daily (24 giờ).</p>
<p>Allowlist cổng mở · phát hiện phơi nhiễm dịch vụ nhạy cảm · audit tiến trình root · quét world-writable · delta khóa SSH · phát hiện đợt tăng đột biến đăng nhập thất bại · delta cron/systemd · sức khỏe stack bảo mật (ClamAV / CrowdSec / Wazuh / fail2ban) · intel feed CVE · tích hợp supply-chain với skill-scanner · audit egress nhà cung cấp LLM · xác minh tính toàn vẹn backup · audit tư thế Tailscale.</p>
<p>v1.9.0 (hôm nay) bổ sung hai lớp mới: outbound-guard thực thi egress allowlist trên các tiến trình được giám sát, và stack-health xác minh rằng stack bảo mật còn sống, còn mới và còn „lên tiếng" được — không chỉ đang chạy.</p>
<p class="meta">Stack: bash thuần + inotify + tiện ích Linux tiêu chuẩn. Thăm dò các dịch vụ localhost + đọc /etc. Yêu cầu thực thi host-side. Mã nguồn mở, MIT.</p>
</div>

<h2>Tại sao là hai cái này chứ không phải „một danh sách công cụ ngầu"?</h2>

<p>Cả hai đều là tác phẩm của chính JXXR1. Chúng tôi chỉ giới thiệu những công cụ mà chính chúng tôi đã xây dựng hoặc audit. Toolhub không xuất bản listicle „công cụ bảo mật Linux tốt nhất" — kiểu đó đã quá nhiều và phần lớn là trang trại SEO. Trang này là một bàn giao được tuyển chọn cho các đối tượng cụ thể đến với Toolhub và cần một bạn đồng hành phía host: quản trị IT trường học, người dựng agent, sysadmin.</p>

<p>Bạn muốn thêm một công cụ? Hãy mở một issue trên <a href="{REPO_URL}">repo Toolhub</a>. Chúng tôi không nhận đặt chỗ trả phí.</p>
""".strip(),
            },
            "hi": {
                "title": "साथी टूल्स",
                "h1": "साथी टूल्स",
                "description": "Toolhub के in-browser utilities के पूरक बाहरी host-side सुरक्षा टूल्स। sentinel और skill-scanner — दोनों MIT-licensed open source।",
                "body": f"""
<p class="tagline">Toolhub के in-browser utilities के पूरक host-side सुरक्षा टूल्स।</p>

<p>Toolhub पूरी तरह browser-based है — server-side कुछ नहीं चलता, install करने की ज़रूरत नहीं। ये बाहरी टूल्स अलग हैं: ये आपकी अपनी मशीन या server पर चलते हैं। हम इन्हें यहाँ इसलिए सूचीबद्ध करते हैं क्योंकि ये Toolhub के privacy-first दर्शन से मेल खाते हैं और ऐसे use cases को संबोधित करते हैं जिनके लिए वास्तव में host-side execution की ज़रूरत होती है।</p>

<p>सभी <strong>JXXR1 द्वारा बनाए गए</strong> हैं, वही maintainer जो Toolhub का है। <strong>MIT लाइसेंस।</strong> इन्हें खुद host करें। source का audit करें। ये affiliate links नहीं हैं — बस साथी utilities हैं।</p>

<h2>🤖 AI एजेंट और हार्नेस</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">AI एजेंट skills के लिए security scanner — credential चोरी, supply-chain हमलों, prompt injection और runtime दुरुपयोग का पता लगाने वाले 38 modules; किसी भी skill bundle पर काम करता है।</p>
<p>किसी भी ऐसे skill bundle पर काम करता है जिसमें SKILL.md या manifest शामिल हो — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkits। AI एजेंट harnesses के बढ़ने के साथ, डाउनलोड किए जाने वाले एजेंट „skills" की supply chain malware injection की अगली सीमा बन रही है। skill-scanner 38 detection modules — pattern matching, AST taint tracking, LLM semantic analysis, YARA rules और typo-squat detection — के ज़रिए skill packages का statically विश्लेषण करता है।</p>
<p>हालिया supply-chain wave (v3.4 + v3.5) जोड़ता है: RAG corpora के लिए bundled-content provenance, बाहरी मॉडल downloads का पता लगाना (HuggingFace / replicate / आदि), in-flight tampering के विरुद्ध hash-pinning verification और PGP release-signature verification।</p>
<p class="meta">Stack: bash + JavaScript + Python wrapper + YARA। Host-side execution आवश्यक। Open source, MIT।</p>
</div>

<h2>🛡️ सुरक्षा</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Linux servers के लिए हल्का bash security monitor — file access, port exposure, egress allowlist, full audit, stack health और रात्रिकालीन deep scan को कवर करने वाली छह-परत वाली रक्षा। शून्य निर्भरताएँ।</p>
<p>छह विलंब स्तर: file-watch (&lt;1s) · watchdog (&lt;2 मिनट) · outbound-guard (&lt;2 मिनट) · check-v2+intel (6 घंटे) · stack-health (&lt;4 घंटे) · daily (24 घंटे)।</p>
<p>खुले पोर्ट allowlist · संवेदनशील सेवा एक्सपोज़र का पता लगाना · root-process audit · world-writable scan · SSH-key delta · failed-login spike detection · cron/systemd delta · security-stack health (ClamAV / CrowdSec / Wazuh / fail2ban) · CVE-feed intel · skill-scanner के साथ supply-chain integration · LLM-vendor egress audit · backup integrity verification · Tailscale posture audit।</p>
<p>v1.9.0 (आज) दो नई परतें जोड़ता है: outbound-guard निगरानी की जा रही प्रक्रियाओं पर egress allowlist लागू करता है, और stack-health सत्यापित करता है कि security stack खुद जीवित, ताज़ा और स्वर वाला हो — सिर्फ़ „चल रहा" नहीं।</p>
<p class="meta">Stack: शुद्ध bash + inotify + standard Linux utilities। localhost services को probe करता है + /etc को पढ़ता है। Host-side execution आवश्यक। Open source, MIT।</p>
</div>

<h2>ये क्यों और सिर्फ़ „cool tools की सूची" क्यों नहीं?</h2>

<p>दोनों JXXR1 का अपना काम हैं। हम वही टूल्स suggest करते हैं जिन्हें हमने खुद बनाया या audit किया है। Toolhub „best Linux security tools" listicle नहीं publish करता — वैसे बहुत हैं और ज़्यादातर SEO farms हैं। यह page एक curated handoff है उन specific audiences के लिए जो Toolhub पर पहुँचते हैं और एक host-side साथी की ज़रूरत महसूस करते हैं: school IT admins, agent-builders, sysadmins।</p>

<p>क्या आप कोई टूल जुड़वाना चाहते हैं? <a href="{REPO_URL}">Toolhub repo</a> पर issue खोलें। हम paid placements स्वीकार नहीं करते।</p>
""".strip(),
            },
            "sk": {
                "title": "Doplnkové nástroje",
                "h1": "Doplnkové nástroje",
                "description": "Externé host-side bezpečnostné nástroje, ktoré dopĺňajú in-browser utility Toolhub-u. sentinel a skill-scanner — oba open source MIT.",
                "body": f"""
<p class="tagline">Host-side bezpečnostné nástroje, ktoré dopĺňajú in-browser utility Toolhub-u.</p>

<p>Toolhub beží celý v prehliadači — nič na strane servera, nič netreba inštalovať. Tieto externé nástroje sú iné: bežia na tvojom vlastnom stroji alebo serveri. Uvádzame ich tu, lebo pasujú k privacy-first prístupu Toolhub-u a riešia prípady použitia, ktoré naozaj vyžadujú host-side beh.</p>

<p>Všetky sú <strong>postavené JXXR1-om</strong>, tým istým maintainerom ako Toolhub. <strong>MIT licencia.</strong> Self-hostuj si ich. Audituj zdroj. Nie sú to affiliate odkazy — len doplnkové utility.</p>

<h2>🤖 AI agenti a harnessy</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Bezpečnostný skener pre skille AI agentov — 38 modulov, ktoré detegujú krádež poverení, útoky na supply chain, prompt injection a zneužitie počas behu na ľubovoľnom skill bundle.</p>
<p>Funguje na ľubovoľnom skill bundle, ktorý prináša súbor SKILL.md alebo manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkity. S rozmachom AI agent harnessov sa supply chain pre stiahnuteľné agentské „skille" stáva ďalšou frontou pre injekciu malware-u. skill-scanner staticky analyzuje skill balíky cez 38 detekčných modulov — pattern matching, AST taint tracking, LLM sémantická analýza, YARA pravidlá a detekcia typo-squat.</p>
<p>Posledná supply-chain vlna (v3.4 + v3.5) pridáva: provenance bundlovaného obsahu pre RAG korpusy, detekciu sťahovania externých modelov (HuggingFace / replicate / atď.), verifikáciu hash-pinning-u proti manipulácii počas prenosu a verifikáciu PGP podpisu vydania.</p>
<p class="meta">Stack: bash + JavaScript + Python wrapper + YARA. Vyžaduje host-side beh. Open source, MIT.</p>
</div>

<h2>🛡️ Bezpečnosť</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Ľahký bashový bezpečnostný monitor pre Linux servery — šesťvrstvová obrana pokrývajúca prístup k súborom, expozíciu portov, egress allowlist, plný audit, zdravie stacku a nočný hlboký sken. Nula závislostí.</p>
<p>Šesť úrovní latencie: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6 h) · stack-health (&lt;4 h) · daily (24 h).</p>
<p>Allowlist otvorených portov · detekcia expozície citlivých služieb · audit root procesov · world-writable scan · delta SSH kľúčov · detekcia spike-u neúspešných prihlásení · delta cron/systemd · zdravie security stacku (ClamAV / CrowdSec / Wazuh / fail2ban) · intel CVE feedu · supply-chain integrácia so skill-scannerom · audit egress-u LLM dodávateľov · verifikácia integrity záloh · audit posture-y Tailscale.</p>
<p>v1.9.0 (dnes) pridáva dve nové vrstvy: outbound-guard vynucuje egress allowlist pre monitorované procesy a stack-health overuje, že samotný bezpečnostný stack je živý, čerstvý a hlasný — nie len „beží".</p>
<p class="meta">Stack: čistý bash + inotify + štandardné Linux utility. Sondá localhost služby + číta /etc. Vyžaduje host-side beh. Open source, MIT.</p>
</div>

<h2>Prečo práve tieto a nie len „zoznam cool nástrojov"?</h2>

<p>Oba sú vlastné dielo JXXR1-a. Odporúčame nástroje, ktoré sme sami postavili alebo auditovali. Toolhub nepublikuje listicle „najlepšie Linux security nástroje" — takých je už dosť a väčšina sú SEO farmy. Táto stránka je kurátorovaný handoff pre konkrétne publikum, ktoré príde na Toolhub a potrebuje host-side spoločníka: školských IT adminov, agent-builderov, sysadminov.</p>

<p>Chceš, aby sme pridali nejaký nástroj? Otvor issue v <a href="{REPO_URL}">Toolhub repu</a>. Platené umiestnenia neprijímame.</p>
""".strip(),
            },
            "cs": {
                "title": "Doplňkové nástroje",
                "h1": "Doplňkové nástroje",
                "description": "Externí host-side bezpečnostní nástroje, které doplňují in-browser utility Toolhubu. sentinel a skill-scanner — obě open source MIT.",
                "body": f"""
<p class="tagline">Host-side bezpečnostní nástroje, které doplňují in-browser utility Toolhubu.</p>

<p>Toolhub běží celý v prohlížeči — nic na straně serveru, nic se neinstaluje. Tyhle externí nástroje jsou jiné: běží na tvém vlastním stroji nebo serveru. Uvádíme je tady, protože sedí k privacy-first přístupu Toolhubu a řeší případy použití, které opravdu vyžadují běh na straně hostitele.</p>

<p>Všechny jsou <strong>postavené JXXR1-em</strong>, tím samým maintainerem jako Toolhub. <strong>MIT licence.</strong> Hostuj si je sám. Audituj zdroj. Nejsou to affiliate odkazy — jen doprovodné utility.</p>

<h2>🤖 AI agenti a harnessy</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/skill-scanner" target="_blank" rel="noopener noreferrer">skill-scanner <span class="version">v3.5.0</span> ↗</a></h3>
<p class="tagline">Bezpečnostní skener pro skilly AI agentů — 38 modulů detekujících krádež přihlašovacích údajů, útoky na supply chain, prompt injection a zneužití za běhu na jakémkoli skill bundle.</p>
<p>Funguje na jakémkoli skill bundle, který přináší soubor SKILL.md nebo manifest — Claude Code, OpenClaw, AgentPress, Hermes Skills Hub, MCP toolkity. S rozmachem AI agent harnessů se supply chain stahovatelných agentských „skillů" stává další frontou pro injekci malwaru. skill-scanner staticky analyzuje balíčky skill napříč 38 detekčními moduly — pattern matching, AST taint tracking, LLM sémantická analýza, YARA pravidla a detekce typo-squat.</p>
<p>Poslední supply-chain vlna (v3.4 + v3.5) přidává: provenance bundlovaného obsahu pro RAG korpusy, detekci stahování externích modelů (HuggingFace / replicate / atd.), verifikaci hash-pinningu proti manipulaci za běhu a verifikaci PGP podpisu vydání.</p>
<p class="meta">Stack: bash + JavaScript + Python wrapper + YARA. Vyžaduje host-side běh. Open source, MIT.</p>
</div>

<h2>🛡️ Bezpečnost</h2>

<div class="companion-tool">
<h3><a href="https://github.com/JXXR1/sentinel" target="_blank" rel="noopener noreferrer">sentinel <span class="version">v1.9.0</span> ↗</a></h3>
<p class="tagline">Lehký bashový bezpečnostní monitor pro Linux servery — šestivrstvá obrana pokrývající přístup k souborům, expozici portů, egress allowlist, plný audit, zdraví stacku a noční hloubkový sken. Nula závislostí.</p>
<p>Šest stupňů latence: file-watch (&lt;1s) · watchdog (&lt;2 min) · outbound-guard (&lt;2 min) · check-v2+intel (6 h) · stack-health (&lt;4 h) · daily (24 h).</p>
<p>Allowlist otevřených portů · detekce expozice citlivých služeb · audit root procesů · world-writable sken · delta SSH klíčů · detekce skoku neúspěšných přihlášení · delta cron/systemd · zdraví security stacku (ClamAV / CrowdSec / Wazuh / fail2ban) · intel CVE feedu · supply-chain integrace se skill-scannerem · audit egress-u LLM dodavatelů · verifikace integrity záloh · audit postury Tailscale.</p>
<p>v1.9.0 (dnes) přidává dvě nové vrstvy: outbound-guard vynucuje egress allowlist na monitorovaných procesech a stack-health ověřuje, že samotný bezpečnostní stack je živý, čerstvý a hlasitý — ne jen „běží".</p>
<p class="meta">Stack: čistý bash + inotify + standardní Linux utility. Sonduje localhost služby + čte /etc. Vyžaduje host-side běh. Open source, MIT.</p>
</div>

<h2>Proč zrovna tyhle a ne jen „seznam cool nástrojů"?</h2>

<p>Oba jsou vlastní dílo JXXR1-a. Doporučujeme nástroje, které jsme sami postavili nebo auditovali. Toolhub nevydává listicle „nejlepší Linux security nástroje" — takových je už dost a většinou jsou to SEO farmy. Tahle stránka je kurátorovaný handoff pro konkrétní publikum, které dorazí na Toolhub a potřebuje host-side společníka: školní IT adminy, agent-buildery, sysadminy.</p>

<p>Chceš, abychom přidali nějaký nástroj? Otevři issue v <a href="{REPO_URL}">Toolhub repu</a>. Placené umístění nepřijímáme.</p>
""".strip(),
            },
        },
    },
}
