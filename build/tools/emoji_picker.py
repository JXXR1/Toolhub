TOOL = {
    "slug": "emoji-picker",
    "category": "text",
    "icon": "😀",
    "tags": ["emoji", "picker", "search", "copy", "unicode", "smiley", "symbol"],
    "i18n": {
        "en": {
            "name": "Emoji Picker",
            "tagline": "Searchable emoji palette by name and keyword. Click any emoji to copy. Categories: smileys, animals, food, travel, objects, symbols, flags.",
            "description": "Free emoji picker with keyword search. Click to copy any emoji. Curated set covering smileys, people, animals, food, travel, objects, symbols, and flags. Pure Unicode — works anywhere.",
        },
        "de": {"name": "Emoji-Auswahl", "tagline": "Durchsuchbare Emoji-Palette nach Name und Stichwort. Klick zum Kopieren. Kategorien: Smileys, Tiere, Essen, Reisen, Objekte, Symbole, Flaggen.", "description": "Kostenlose Emoji-Auswahl mit Stichwort-Suche. Klick zum Kopieren. Kuratierter Satz: Smileys, Personen, Tiere, Essen, Reisen, Objekte, Symbole, Flaggen. Reines Unicode — überall verwendbar."},
        "es": {"name": "Selector de Emojis", "tagline": "Paleta de emojis con búsqueda por nombre y palabra clave. Clic para copiar. Categorías: caras, animales, comida, viajes, objetos, símbolos, banderas.", "description": "Selector gratuito de emojis con búsqueda por palabra clave. Clic para copiar. Conjunto curado: caras, personas, animales, comida, viajes, objetos, símbolos, banderas. Unicode puro."},
        "fr": {"name": "Sélecteur d'Emojis", "tagline": "Palette d'emojis avec recherche par nom et mot-clé. Cliquez pour copier. Catégories : sourires, animaux, nourriture, voyage, objets, symboles, drapeaux.", "description": "Sélecteur gratuit d'emojis avec recherche par mot-clé. Clic pour copier. Ensemble curaté : sourires, personnes, animaux, nourriture, voyage, objets, symboles, drapeaux. Unicode pur."},
        "it": {"name": "Selettore di Emoji", "tagline": "Tavolozza di emoji con ricerca per nome e parola chiave. Clicca per copiare. Categorie: faccine, animali, cibo, viaggi, oggetti, simboli, bandiere.", "description": "Selettore gratuito di emoji con ricerca per parole chiave. Clicca per copiare. Set curato: faccine, persone, animali, cibo, viaggi, oggetti, simboli, bandiere. Unicode puro."},
        "pt": {"name": "Seletor de Emoji", "tagline": "Paleta de emojis pesquisável por nome e palavra-chave. Clique em qualquer emoji para copiar. Categorias: smileys, animais, comida, viagem, objetos, símbolos, bandeiras.", "description": "Seletor gratuito de emojis com busca por palavra-chave. Clique para copiar qualquer emoji. Conjunto curado cobrindo smileys, pessoas, animais, comida, viagem, objetos, símbolos e bandeiras. Unicode puro — funciona em qualquer lugar."},
        "pl": {"name": "Picker Emoji", "tagline": "Paleta emoji z wyszukiwaniem po nazwie i słowach kluczowych. Kliknij dowolne emoji, aby skopiować. Kategorie: smileys, zwierzęta, jedzenie, podróże, obiekty, symbole, flagi.", "description": "Darmowy picker emoji z wyszukiwaniem po słowach kluczowych. Kliknij, aby skopiować dowolne emoji. Wyselekcjonowany zestaw: smileys, ludzie, zwierzęta, jedzenie, podróże, obiekty, symbole i flagi. Czysty Unicode — działa wszędzie."},
        "ja": {"name": "絵文字ピッカー", "tagline": "名前とキーワードで検索できる絵文字パレット。クリックでコピー。カテゴリ：スマイリー、動物、食べ物、旅行、オブジェクト、記号、国旗。", "description": "キーワード検索付きの無料絵文字ピッカー。クリックして絵文字をコピーできます。スマイリー、人物、動物、食べ物、旅行、オブジェクト、記号、国旗をカバーする厳選セットです。Unicode のみなのでどこでも動作します。"},
        "nl": {"name": "Emoji-picker", "tagline": "Doorzoekbaar emoji-palet op naam en keyword. Klik een emoji om te kopiëren. Categorieën: smileys, dieren, eten, reizen, objecten, symbolen, vlaggen.", "description": "Gratis emoji-picker met keyword-search. Klik om elke emoji te kopiëren. Gecureerde set met smileys, mensen, dieren, eten, reizen, objecten, symbolen en vlaggen. Pure Unicode — werkt overal."},
    },
    "body": """
<div class="tool-card">
  <label>Search</label>
  <input type="text" id="ep-q" oninput="epRun()" placeholder="Type to filter — 'happy', 'fire', 'pizza', 'rocket'…" autocomplete="off" spellcheck="false">
  <div class="meta" id="ep-cats" style="margin-top:0.6rem;display:flex;flex-wrap:wrap;gap:0.3rem"></div>
</div>
<div class="tool-card">
  <label id="ep-recent-lbl" style="display:none">Recent</label>
  <div id="ep-recent" style="display:flex;flex-wrap:wrap;gap:0.3rem;margin-bottom:0.5rem"></div>
  <label>{LBL_RESULT}</label>
  <div id="ep-grid"></div>
  <div id="ep-toast" style="position:fixed;bottom:2rem;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;padding:0.5rem 1rem;border-radius:6px;font-size:0.9rem;display:none;z-index:1000;font-family:ui-monospace,monospace"></div>
</div>
""",
    "script": """
<style>
.ep-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(2.6rem,1fr));gap:0.3rem}
.ep-tile{display:flex;align-items:center;justify-content:center;font-size:1.5rem;padding:0.45rem 0.3rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;cursor:pointer;transition:all 0.1s;line-height:1}
.ep-tile:hover{background:var(--surface);border-color:var(--accent);transform:scale(1.1)}
.ep-cat-btn{padding:0.25rem 0.7rem;font-size:0.78rem;background:var(--surface);color:var(--text-muted);border:1px solid var(--border);border-radius:14px;cursor:pointer}
.ep-cat-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.ep-empty{color:var(--text-muted);text-align:center;padding:1.5rem 0;grid-column:1/-1}
.ep-section{margin-bottom:0.8rem}
.ep-section h4{font-size:0.78rem;color:var(--text-muted);font-weight:600;margin:0.5rem 0 0.3rem;letter-spacing:0.04em;text-transform:uppercase}
</style>
<script>
const EP_DATA = {
  smileys: [
    ['😀','grinning happy face'],['😃','smiley happy joy'],['😄','grinning eyes happy'],['😁','beaming grin smile'],
    ['😆','laughing satisfied'],['😅','sweat smile relief'],['🤣','rofl laughing rolling'],['😂','tears joy laughing'],
    ['🙂','slight smile happy'],['🙃','upside-down sarcasm silly'],['😉','wink playful'],['😊','blush smile happy'],
    ['😇','innocent halo angel'],['🥰','smile hearts love'],['😍','heart eyes love admire'],['🤩','star eyes wow'],
    ['😘','kiss face love'],['😋','yum tongue tasty'],['😛','tongue cheeky'],['🤪','zany silly crazy'],
    ['😎','cool sunglasses'],['🤓','nerd geek glasses'],['🥳','party hat celebrate'],['😏','smirk sly'],
    ['😞','disappointed sad'],['😟','worried concerned'],['😕','confused unsure'],['🙁','frown sad'],
    ['☹️','frowning sad'],['😣','persevere strain'],['😖','confounded frustrated'],['😫','tired weary'],
    ['😩','weary tired'],['😢','cry sad tear'],['😭','sob crying loud'],['😤','triumph annoyed steam'],
    ['😡','angry mad red'],['😠','angry mad'],['🤬','curse swearing angry'],['😨','fearful afraid'],
    ['😰','anxious sweat fear'],['😥','sad relieved'],['😓','sweat downcast'],['😱','scream shock fear'],
    ['🥺','pleading puppy beg'],['😴','sleeping zzz'],['😪','sleepy drowsy'],['🤤','drool tasty'],
    ['🤔','thinking pondering'],['🤨','raised eyebrow skeptical'],['😐','neutral expressionless'],['😑','expressionless meh'],
    ['🙄','eye roll annoyed'],['😬','grimace awkward'],['🤐','zipper mouth quiet'],['🤫','shush quiet secret'],
    ['🤥','liar pinocchio nose'],['😷','mask sick covid'],['🤒','thermometer sick fever'],['🤢','nauseated sick gross'],
    ['🤮','vomit sick gross'],['🤧','sneeze cold'],['🥶','cold freezing blue'],['🥵','hot heat sweat'],
    ['🥴','woozy dizzy drunk'],['😵','dizzy ko knocked'],['🤯','mind blown explode'],['🤠','cowboy hat'],
    ['🤡','clown'],['👻','ghost halloween'],['💀','skull death dead'],['👽','alien et space'],
    ['🤖','robot bot ai'],['😺','grinning cat'],['😸','smile cat'],['😻','heart eyes cat love'],
    ['😼','smirk cat'],['🙀','scared cat'],['👍','thumbs up like ok'],['👎','thumbs down dislike'],
    ['👌','ok perfect'],['✌️','peace victory'],['🤞','fingers crossed luck'],['🤟','love rock horns'],
    ['🤘','rock metal horns'],['👊','fist punch'],['✊','fist solidarity'],['🤝','handshake deal'],
    ['🙏','pray thanks please'],['👏','clap applause'],['🙌','raised hands celebrate'],['👋','wave hello bye'],
    ['💪','muscle strong flex'],['🫶','heart hands love'],['🫡','salute respect'],['🤲','open hands prayer'],
  ],
  animals: [
    ['🐶','dog puppy'],['🐱','cat kitten'],['🐭','mouse'],['🐹','hamster'],['🐰','rabbit bunny'],
    ['🦊','fox'],['🐻','bear'],['🐼','panda'],['🐨','koala'],['🐯','tiger'],['🦁','lion'],
    ['🐮','cow'],['🐷','pig'],['🐸','frog'],['🐵','monkey'],['🙈','see no evil monkey'],
    ['🙉','hear no evil monkey'],['🙊','speak no evil monkey'],['🐒','monkey'],['🦍','gorilla'],
    ['🦒','giraffe'],['🦓','zebra'],['🐴','horse'],['🦄','unicorn'],['🐔','chicken hen'],
    ['🐧','penguin'],['🐦','bird'],['🐤','baby chick'],['🦆','duck'],['🦅','eagle'],['🦉','owl'],
    ['🦇','bat'],['🐺','wolf'],['🐗','boar'],['🐴','horse face'],['🦌','deer'],
    ['🐢','turtle'],['🐍','snake'],['🦎','lizard'],['🦖','t-rex dinosaur'],['🦕','sauropod dinosaur'],
    ['🐙','octopus'],['🦑','squid'],['🦐','shrimp'],['🦞','lobster'],['🦀','crab'],
    ['🐠','tropical fish'],['🐟','fish'],['🐬','dolphin'],['🐳','whale'],['🦈','shark'],
    ['🐊','crocodile'],['🐅','tiger'],['🐆','leopard'],['🦏','rhino'],['🦛','hippo'],
    ['🐂','ox'],['🐃','buffalo'],['🐎','horse'],['🐖','pig'],['🐑','sheep'],['🐐','goat'],
    ['🐪','camel'],['🐘','elephant'],['🦘','kangaroo'],['🦡','badger'],['🐾','paw prints'],
    ['🦋','butterfly'],['🐛','caterpillar bug'],['🐝','bee'],['🐞','ladybug'],['🐜','ant'],
    ['🕷️','spider'],['🦂','scorpion'],['🐌','snail'],['🐚','shell'],['🌸','blossom'],
    ['🌹','rose flower'],['🌻','sunflower'],['🌷','tulip'],['🌳','tree'],['🌴','palm'],
    ['🌵','cactus'],['🍀','clover luck four-leaf'],['🍁','maple leaf'],
  ],
  food: [
    ['🍎','apple'],['🍏','green apple'],['🍐','pear'],['🍊','orange tangerine'],['🍋','lemon'],
    ['🍌','banana'],['🍉','watermelon'],['🍇','grapes'],['🍓','strawberry'],['🫐','blueberry'],
    ['🍈','melon'],['🍒','cherry'],['🍑','peach'],['🥭','mango'],['🍍','pineapple'],
    ['🥥','coconut'],['🥝','kiwi'],['🍅','tomato'],['🍆','eggplant'],['🥑','avocado'],
    ['🥦','broccoli'],['🥬','leafy green'],['🥒','cucumber'],['🌶️','hot pepper chili'],['🫑','bell pepper'],
    ['🌽','corn'],['🥕','carrot'],['🧄','garlic'],['🧅','onion'],['🥔','potato'],
    ['🍠','sweet potato'],['🥐','croissant'],['🥯','bagel'],['🍞','bread'],['🥖','baguette'],
    ['🧀','cheese'],['🥚','egg'],['🍳','fried egg'],['🥞','pancakes'],['🧇','waffle'],
    ['🥓','bacon'],['🥩','steak meat'],['🍗','poultry leg'],['🍖','meat bone'],['🌭','hot dog'],
    ['🍔','burger hamburger'],['🍟','fries'],['🍕','pizza'],['🥪','sandwich'],['🥙','wrap pita'],
    ['🌮','taco'],['🌯','burrito'],['🫔','tamale'],['🥗','salad'],['🥘','paella'],
    ['🍝','spaghetti pasta'],['🍜','ramen noodles'],['🍲','stew'],['🍛','curry'],['🍣','sushi'],
    ['🍱','bento'],['🥟','dumpling'],['🍤','shrimp tempura'],['🍙','rice ball'],['🍚','rice bowl'],
    ['🍘','rice cracker'],['🍡','dango skewer'],['🍦','soft serve ice cream'],['🍨','ice cream'],
    ['🍧','shaved ice'],['🍰','cake slice'],['🎂','birthday cake'],['🧁','cupcake'],['🍮','custard pudding'],
    ['🍭','lollipop'],['🍬','candy'],['🍫','chocolate bar'],['🍩','donut'],['🍪','cookie'],
    ['🥛','milk'],['🍼','baby bottle'],['☕','coffee hot'],['🍵','tea'],['🧃','juice box'],
    ['🥤','soft drink'],['🧋','bubble tea'],['🍺','beer'],['🍻','beers cheers'],['🍷','wine glass'],
    ['🥂','champagne toast'],['🍸','cocktail martini'],['🍹','tropical drink'],['🍾','champagne bottle'],
    ['🥃','whiskey'],['🧉','mate'],['🍴','fork knife'],['🥢','chopsticks'],['🥄','spoon'],
  ],
  travel: [
    ['🚗','car'],['🚕','taxi'],['🚙','suv'],['🚌','bus'],['🚎','trolleybus'],['🏎️','race car'],
    ['🚓','police car'],['🚑','ambulance'],['🚒','fire engine'],['🚐','minibus'],['🛻','pickup truck'],
    ['🚚','delivery truck'],['🚛','articulated lorry'],['🚜','tractor'],['🏍️','motorcycle'],['🛵','scooter'],
    ['🚲','bike bicycle'],['🛹','skateboard'],['🛼','roller skate'],['🚏','bus stop'],
    ['🚂','steam locomotive'],['🚆','train'],['🚇','metro subway'],['🚊','tram'],['🚝','monorail'],
    ['🚄','high-speed train'],['🚅','bullet train shinkansen'],['🚉','train station'],
    ['✈️','airplane'],['🛫','takeoff plane'],['🛬','landing plane'],['🚀','rocket'],['🛸','flying saucer ufo'],
    ['🚁','helicopter'],['🚢','ship'],['⛴️','ferry'],['🛥️','motor boat'],['🛳️','passenger ship'],
    ['⛵','sailboat'],['🚤','speedboat'],['🛶','canoe'],['⚓','anchor'],
    ['🏖️','beach'],['🏝️','desert island'],['⛰️','mountain'],['🏔️','snowy mountain'],['🌋','volcano'],
    ['🏕️','camping'],['🏞️','national park'],['🛤️','railway track'],['🛣️','motorway'],
    ['🏛️','classical building'],['🏟️','stadium'],['🏰','castle'],['🏯','japanese castle'],['🗽','statue of liberty'],
    ['🗼','tokyo tower'],['🗻','mount fuji'],['🗿','moai'],['🌁','foggy bridge'],['🌃','city night'],
    ['🌄','sunrise mountain'],['🌅','sunrise'],['🌆','dusk city'],['🌇','sunset city'],['🌉','bridge night'],
    ['🎡','ferris wheel'],['🎢','roller coaster'],['🎠','carousel'],['⛲','fountain'],
    ['🏨','hotel'],['🏩','love hotel'],['🏪','convenience store'],['🏫','school'],['🏬','department store'],
    ['🏭','factory'],['🏥','hospital'],['🏦','bank'],['⛪','church'],['🕌','mosque'],['🛕','hindu temple'],
    ['🕍','synagogue'],['🛤️','tracks'],['🌍','earth africa'],['🌎','earth americas'],['🌏','earth asia'],
    ['🗺️','world map'],['🧭','compass'],['🧳','luggage suitcase'],
  ],
  objects: [
    ['⌚','watch'],['📱','phone mobile'],['💻','laptop'],['⌨️','keyboard'],['🖥️','desktop computer'],
    ['🖨️','printer'],['🖱️','mouse'],['💾','floppy save disk'],['💿','cd'],['📀','dvd'],
    ['📷','camera'],['📸','camera flash'],['🎥','movie camera'],['📺','tv television'],['📻','radio'],
    ['🎙️','microphone studio'],['🎚️','level slider'],['🎛️','control knobs'],['⏰','alarm clock'],
    ['⏱️','stopwatch'],['🕰️','mantelpiece clock'],['⏳','hourglass'],['📡','satellite antenna'],
    ['🔋','battery'],['🔌','plug power'],['💡','lightbulb idea'],['🔦','flashlight torch'],['🕯️','candle'],
    ['🧯','fire extinguisher'],['🛢️','oil drum'],['💸','money flying'],['💵','dollar bill'],
    ['💴','yen bill'],['💶','euro bill'],['💷','pound bill'],['💰','money bag'],['💳','credit card'],
    ['🧾','receipt'],['💎','gem diamond'],['⚖️','balance scale'],['🧰','toolbox'],
    ['🔧','wrench'],['🔨','hammer'],['⚒️','hammer pick'],['🛠️','tools'],['⛏️','pick'],
    ['🪓','axe'],['🔩','nut bolt'],['⚙️','gear settings'],['🧲','magnet'],['🧪','test tube'],
    ['🧫','petri dish'],['🧬','dna'],['🔬','microscope'],['🔭','telescope'],['📐','triangular ruler'],
    ['📏','straight ruler'],['🧮','abacus'],['📌','pushpin'],['📍','round pushpin'],['🖇️','paperclip'],
    ['📎','paperclip'],['✂️','scissors'],['🖊️','pen'],['🖋️','fountain pen'],['✒️','nib pen'],
    ['🖌️','paintbrush'],['🖍️','crayon'],['📝','memo note'],['✏️','pencil'],['📓','notebook'],
    ['📒','ledger'],['📔','decorative notebook'],['📕','closed book'],['📖','open book'],['📗','green book'],
    ['📘','blue book'],['📙','orange book'],['📚','books library'],['📰','newspaper'],['📦','package box'],
    ['📤','outbox'],['📥','inbox'],['📨','envelope incoming'],['✉️','envelope email'],['📧','email'],
    ['📩','envelope arrow'],['📪','closed mailbox'],['📫','mailbox'],['📬','mailbox open'],
    ['📭','mailbox empty'],['📮','postbox'],['🗳️','ballot box'],['🔒','lock'],['🔓','unlock'],
    ['🔏','lock pen'],['🔐','lock key'],['🔑','key'],['🗝️','old key'],['🛎️','bellhop bell'],
    ['🔔','bell'],['🔕','bell off mute'],['🎵','music note'],['🎶','music notes'],['🎼','musical score'],
    ['🎹','piano keyboard'],['🥁','drum'],['🎷','saxophone'],['🎺','trumpet'],['🎸','guitar'],
    ['🎻','violin'],['🎤','microphone'],['🎧','headphones'],['🎬','clapper'],['🎮','game controller'],
    ['🕹️','joystick'],['🎲','dice'],['🧸','teddy bear'],['🎨','artist palette'],['🖼️','framed picture'],
  ],
  symbols: [
    ['❤️','red heart love'],['🧡','orange heart'],['💛','yellow heart'],['💚','green heart'],
    ['💙','blue heart'],['💜','purple heart'],['🖤','black heart'],['🤍','white heart'],['🤎','brown heart'],
    ['💔','broken heart'],['❣️','heart exclamation'],['💕','two hearts'],['💞','revolving hearts'],
    ['💓','beating heart'],['💗','growing heart'],['💖','sparkling heart'],['💘','arrow heart cupid'],
    ['💝','heart ribbon'],['💟','heart decoration'],['☮️','peace'],['✝️','latin cross'],['☪️','star crescent'],
    ['🕉️','om'],['☸️','wheel dharma'],['✡️','star david'],['🔯','six pointed star'],['🕎','menorah'],
    ['☯️','yin yang'],['☦️','orthodox cross'],['🛐','place worship'],['⛎','ophiuchus'],['♈','aries'],
    ['♉','taurus'],['♊','gemini'],['♋','cancer zodiac'],['♌','leo'],['♍','virgo'],['♎','libra'],
    ['♏','scorpio'],['♐','sagittarius'],['♑','capricorn'],['♒','aquarius'],['♓','pisces'],
    ['🆔','id'],['⚛️','atom science'],['☢️','radioactive'],['☣️','biohazard'],['📴','phone off'],
    ['📳','vibration'],['🈶','japanese not free'],['🈚','japanese free'],['🆚','vs versus'],
    ['🆎','blood type ab'],['🆑','cl symbol'],['🆘','sos help'],['🆔','id'],['🆕','new'],['🆓','free'],
    ['🆖','ng'],['🆗','ok'],['🆙','up'],['🆒','cool'],['🆓','free'],['0️⃣','keycap zero'],
    ['1️⃣','keycap one'],['2️⃣','keycap two'],['3️⃣','keycap three'],['4️⃣','keycap four'],
    ['5️⃣','keycap five'],['6️⃣','keycap six'],['7️⃣','keycap seven'],['8️⃣','keycap eight'],
    ['9️⃣','keycap nine'],['🔟','keycap ten'],['#️⃣','keycap hash'],['*️⃣','keycap asterisk'],
    ['🔢','numbers'],['🔣','symbols'],['🔤','letters abc'],['🅰️','a button'],['🅱️','b button'],
    ['🆎','ab button'],['🅾️','o button'],['💯','100 hundred'],['🔝','top'],['🔚','end'],
    ['🔙','back'],['🔜','soon'],['🔛','on'],['🔃','clockwise vertical arrows'],['🔄','counterclockwise arrows'],
    ['↩️','left arrow curved'],['↪️','right arrow curved'],['⬆️','up arrow'],['⬇️','down arrow'],
    ['⬅️','left arrow'],['➡️','right arrow'],['↗️','up-right arrow'],['↘️','down-right arrow'],
    ['↙️','down-left arrow'],['↖️','up-left arrow'],['↕️','up-down arrow'],['↔️','left-right arrow'],
    ['🔀','shuffle'],['🔁','repeat'],['🔂','repeat single'],['▶️','play'],['⏸️','pause'],['⏹️','stop'],
    ['⏺️','record'],['⏭️','next track'],['⏮️','previous track'],['⏩','fast forward'],['⏪','rewind'],
    ['⏫','fast up'],['⏬','fast down'],['⏏️','eject'],['🔆','bright'],['🔅','dim'],['🔇','muted'],
    ['🔈','speaker low'],['🔉','speaker medium'],['🔊','speaker loud'],['🔔','bell'],['🔕','bell off'],
    ['💬','speech bubble'],['💭','thought bubble'],['🗯️','right anger bubble'],['♻️','recycle'],
    ['✅','check mark'],['❎','x button'],['❌','cross x'],['❓','question'],['❔','white question'],
    ['❗','exclamation'],['❕','white exclamation'],['‼️','double exclamation'],['⁉️','exclamation question'],
    ['⭐','star'],['🌟','glowing star'],['✨','sparkles'],['⚡','lightning'],['🔥','fire'],['💥','collision boom'],
    ['☀️','sun'],['🌤️','sun small cloud'],['⛅','sun behind cloud'],['🌥️','sun large cloud'],
    ['☁️','cloud'],['🌦️','sun rain'],['🌧️','rain cloud'],['⛈️','thunderstorm'],['🌩️','lightning cloud'],
    ['🌨️','snow cloud'],['❄️','snowflake'],['☃️','snowman'],['⛄','snowman no snow'],['🌬️','wind blowing'],
    ['💨','dash wind'],['💧','droplet'],['💦','sweat droplets'],['🌊','wave'],['🌈','rainbow'],
    ['🌚','new moon face'],['🌝','full moon face'],['🌞','sun face'],['🌛','crescent moon face'],
    ['🌜','last quarter moon face'],['🌙','crescent moon'],['🪐','ringed planet'],['☄️','comet'],
    ['💤','sleep zzz'],['🚫','prohibited'],['⛔','no entry'],['📛','name badge'],['🔰','japanese symbol beginner'],
  ],
  flags: [
    ['🏳️','white flag'],['🏴','black flag'],['🏁','checkered flag'],['🚩','triangular flag'],
    ['🏳️‍🌈','rainbow flag pride'],['🏳️‍⚧️','transgender flag'],['🏴‍☠️','pirate flag'],
    ['🇦🇷','argentina'],['🇦🇺','australia'],['🇦🇹','austria'],['🇧🇪','belgium'],['🇧🇷','brazil'],
    ['🇨🇦','canada'],['🇨🇳','china'],['🇨🇿','czech republic'],['🇩🇰','denmark'],['🇪🇬','egypt'],
    ['🇫🇮','finland'],['🇫🇷','france'],['🇩🇪','germany'],['🇬🇷','greece'],['🇭🇰','hong kong'],
    ['🇭🇺','hungary'],['🇮🇸','iceland'],['🇮🇳','india'],['🇮🇩','indonesia'],['🇮🇪','ireland'],
    ['🇮🇱','israel'],['🇮🇹','italy'],['🇯🇵','japan'],['🇰🇷','south korea'],['🇲🇽','mexico'],
    ['🇳🇱','netherlands'],['🇳🇿','new zealand'],['🇳🇴','norway'],['🇵🇱','poland'],['🇵🇹','portugal'],
    ['🇷🇴','romania'],['🇷🇺','russia'],['🇸🇦','saudi arabia'],['🇸🇬','singapore'],['🇿🇦','south africa'],
    ['🇪🇸','spain'],['🇸🇪','sweden'],['🇨🇭','switzerland'],['🇹🇼','taiwan'],['🇹🇭','thailand'],
    ['🇹🇷','turkey'],['🇺🇦','ukraine'],['🇦🇪','united arab emirates'],['🇬🇧','united kingdom uk britain'],
    ['🇺🇸','united states us america'],['🇻🇳','vietnam'],['🇪🇺','european union eu'],['🇺🇳','united nations un'],
  ],
};
const EP_CAT_LABELS = {smileys:'Smileys & People', animals:'Animals & Nature', food:'Food & Drink', travel:'Travel & Places', objects:'Objects', symbols:'Symbols', flags:'Flags'};
let EP_ACTIVE = 'all';
let EP_RECENT = [];
try { EP_RECENT = JSON.parse(localStorage.getItem('emoji-recent') || '[]'); } catch(e){ EP_RECENT = []; }
function epToast(msg){
  const t = document.getElementById('ep-toast');
  t.textContent = msg;
  t.style.display = 'block';
  clearTimeout(t._timer);
  t._timer = setTimeout(()=>{ t.style.display='none'; }, 1200);
}
function epCopy(emoji){
  navigator.clipboard.writeText(emoji).then(()=>{
    epToast('Copied: ' + emoji);
    EP_RECENT = [emoji].concat(EP_RECENT.filter(e => e !== emoji)).slice(0, 12);
    try { localStorage.setItem('emoji-recent', JSON.stringify(EP_RECENT)); } catch(e){}
    epRenderRecent();
  });
}
function epRenderCats(){
  const cats = ['all'].concat(Object.keys(EP_DATA));
  document.getElementById('ep-cats').innerHTML = cats.map(c => {
    const lbl = c === 'all' ? 'All' : EP_CAT_LABELS[c];
    const cls = c === EP_ACTIVE ? 'ep-cat-btn active' : 'ep-cat-btn';
    return `<button type="button" class="${cls}" data-cat="${c}" onclick="epCat('${c}')">${lbl}</button>`;
  }).join('');
}
function epCat(c){
  EP_ACTIVE = c;
  epRenderCats();
  epRun();
}
function epRenderRecent(){
  const wrap = document.getElementById('ep-recent');
  const lbl = document.getElementById('ep-recent-lbl');
  if(EP_RECENT.length === 0){ wrap.innerHTML = ''; lbl.style.display = 'none'; return; }
  lbl.style.display = '';
  wrap.innerHTML = EP_RECENT.map(e => `<button type="button" class="ep-tile" onclick="epCopy('${e.replace(/'/g,'\\\\\\'')}')" title="${e}">${e}</button>`).join('');
}
function epRun(){
  const q = (document.getElementById('ep-q').value || '').toLowerCase().trim();
  const grid = document.getElementById('ep-grid');
  const cats = EP_ACTIVE === 'all' ? Object.keys(EP_DATA) : [EP_ACTIVE];
  let html = '';
  let total = 0;
  for(const cat of cats){
    const matches = EP_DATA[cat].filter(([e, kw]) => !q || kw.toLowerCase().includes(q));
    if(matches.length === 0) continue;
    if(cats.length > 1) html += `<div class="ep-section"><h4>${EP_CAT_LABELS[cat]}</h4><div class="ep-grid">`;
    else html += '<div class="ep-grid">';
    for(const [e, kw] of matches){
      const ej = e.replace(/'/g, "\\\\'");
      html += `<button type="button" class="ep-tile" onclick="epCopy('${ej}')" title="${kw}">${e}</button>`;
      total++;
    }
    html += cats.length > 1 ? '</div></div>' : '</div>';
  }
  if(total === 0) html = '<div class="ep-empty">No matching emoji.</div>';
  grid.innerHTML = html;
}
document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(() => { epRenderCats(); epRenderRecent(); epRun(); }));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Operating systems all ship emoji pickers (Win+. on Windows, Cmd+Ctrl+Space on macOS, the keyboard on phones), but they're inconsistent, sometimes hidden, and often slow. This tool gives you a curated grid of the most-used emoji organised by category and searchable by keyword. Click any tile to copy the emoji to your clipboard. Recently-copied emoji are remembered between visits in browser-local storage — nothing is sent to a server.</p>

<h3>When to use it</h3>
<ul>
  <li>You're on a desktop without a quick OS-level emoji shortcut.</li>
  <li>You want a keyword search wider than your OS picker offers.</li>
  <li>You're using a remote desktop or older system that has no native picker.</li>
  <li>You need an emoji to paste into a text field that doesn't accept your IME.</li>
</ul>

<h3>How rendering works</h3>
<p>An emoji is just one or more Unicode code points. <em>How</em> it looks depends on the font your browser/OS picks: Apple's emoji are different from Google's Noto, Microsoft's Segoe UI Emoji, and Twitter's Twemoji. The bytes are identical — the picture is local. If an emoji shows as a square or a fallback "unsupported", your system font doesn't have a glyph for it; updating the OS or installing a font like Noto Color Emoji fixes it.</p>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Skin tones and family/profession variants are sequences.</strong> 👨‍🍳 is "man" + ZWJ + "cooking" — five code points. Some systems display the components individually if they don't support the sequence.</li>
  <li><strong>Flags are regional indicators.</strong> 🇬🇧 is "🇬" + "🇧" — two regional-indicator letters. Sequences for territories (Scotland, Texas) need extra tag characters and may not render on every system.</li>
  <li><strong>This tool is curated, not exhaustive.</strong> Unicode 15 has 3,664 emoji including hundreds of skin-tone and gender variants. The picker focuses on the ~600 you're most likely to want; for the full list, see Unicode's emoji data or your OS picker.</li>
  <li><strong>Some characters look like emoji but render as text.</strong> The "variation selector" (U+FE0F) tells the renderer "draw this as emoji". Without it, ☂ might render as plain text rather than 🌂. The tool includes the selectors where needed.</li>
  <li><strong>Clipboard support varies.</strong> Some browsers' clipboard API needs a user gesture (the click does that), but a permission denial will silently fail. If copying doesn't work, use the keyboard shortcut to copy from the address bar instead.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Sistemas operacionais todos têm seletores de emoji (Win+. no Windows, Cmd+Ctrl+Espaço no macOS, o teclado em celulares), mas eles são inconsistentes, às vezes escondidos e frequentemente lentos. Esta ferramenta dá uma grade curada dos emojis mais usados, organizada por categoria e pesquisável por palavra-chave. Clique em qualquer ladrilho para copiar o emoji para o clipboard. Os emojis copiados recentemente são lembrados entre visitas no localStorage do browser — nada é enviado a um servidor.</p>

<h3>Quando usar</h3>
<ul>
  <li>Você está num desktop sem um atalho rápido de emoji no nível do SO.</li>
  <li>Quer uma busca por palavra-chave mais ampla do que o seletor do SO oferece.</li>
  <li>Está usando um desktop remoto ou sistema antigo sem seletor nativo.</li>
  <li>Precisa colar um emoji num campo de texto que não aceita seu IME.</li>
</ul>

<h3>Como funciona a renderização</h3>
<p>Um emoji é apenas um ou mais code points Unicode. <em>Como</em> ele aparece depende da fonte que seu browser/SO escolhe: os emojis da Apple são diferentes dos do Google Noto, do Microsoft Segoe UI Emoji e do Twemoji do Twitter. Os bytes são idênticos — a imagem é local. Se um emoji aparece como um quadrado ou um fallback "não suportado", a fonte do seu sistema não tem glifo para ele; atualizar o SO ou instalar uma fonte como Noto Color Emoji resolve.</p>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Tons de pele e variantes de família/profissão são sequências.</strong> 👨‍🍳 é "homem" + ZWJ + "cozinhando" — cinco code points. Alguns sistemas mostram os componentes individualmente se não suportam a sequência.</li>
  <li><strong>Bandeiras são indicadores regionais.</strong> 🇧🇷 é "🇧" + "🇷" — duas letras de indicador regional. Sequências para territórios (Escócia, Texas) precisam de caracteres tag extras e podem não renderizar em todo sistema.</li>
  <li><strong>Esta ferramenta é curada, não exaustiva.</strong> O Unicode 15 tem 3.664 emojis incluindo centenas de variantes de tom de pele e gênero. O seletor foca nos ~600 que você provavelmente vai querer; para a lista completa, veja os dados de emoji do Unicode ou o seletor do seu SO.</li>
  <li><strong>Alguns caracteres parecem emoji mas renderizam como texto.</strong> O "variation selector" (U+FE0F) diz ao renderizador "desenhe isso como emoji". Sem ele, ☂ pode aparecer como texto puro em vez de 🌂. A ferramenta inclui os selectors onde necessário.</li>
  <li><strong>Suporte a clipboard varia.</strong> A clipboard API de alguns browsers precisa de um gesto do usuário (o clique faz isso), mas uma negação de permissão falha silenciosamente. Se copiar não funcionar, use o atalho de teclado para copiar da barra de endereços.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Betriebssysteme haben Emoji-Picker (Win+., Cmd+Ctrl+Leertaste), aber sie sind inkonsistent und manchmal versteckt. Dieses Tool bietet ein kuratierte Raster der wichtigsten Emojis nach Kategorie sortiert und per Stichwort durchsuchbar. Klick auf eine Kachel kopiert. Zuletzt kopierte werden im Browser gespeichert — nichts wird an einen Server gesendet.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Auf einem Desktop ohne schnellen OS-Picker.</li>
<li>Stichwort-Suche breiter als der OS-Picker.</li>
<li>Remote-Desktop oder ältere Systeme ohne nativen Picker.</li>
</ul>
<h3>Wie das Rendering funktioniert</h3>
<p>Emojis sind Unicode-Code-Points. Das Aussehen hängt vom System-Font ab — Apple, Google Noto, Microsoft Segoe sind unterschiedlich. Die Bytes sind identisch, das Bild ist lokal.</p>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Hautfarben und Berufs-Varianten sind Sequenzen.</strong> 👨‍🍳 = mehrere Code-Points mit ZWJ.</li>
<li><strong>Flaggen sind Regional-Indikatoren.</strong> 🇩🇪 = "🇩" + "🇪".</li>
<li><strong>Kuratiert, nicht vollständig.</strong> Unicode 15 hat 3664 Emojis; hier ~600 gängige.</li>
<li><strong>Variation Selector (U+FE0F)</strong> erzwingt Emoji-Stil.</li>
<li><strong>Clipboard-API benötigt Geste</strong> (der Klick reicht).</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Los sistemas operativos tienen selectores de emojis (Win+., Cmd+Ctrl+Espacio), pero son inconsistentes y a veces lentos. Esta herramienta ofrece una rejilla curada por categoría con búsqueda por palabra clave. Clic = copiado. Los recientes se guardan en el almacenamiento local del navegador — nada se envía a un servidor.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Escritorio sin atajo rápido de emojis.</li>
<li>Búsqueda por palabra clave más amplia.</li>
<li>Escritorio remoto o sistema sin selector nativo.</li>
</ul>
<h3>Cómo funciona el renderizado</h3>
<p>Los emojis son puntos de código Unicode. El aspecto depende de la fuente del sistema (Apple, Google Noto, Microsoft Segoe). Los bytes son idénticos.</p>
<h3>Errores comunes</h3>
<ul>
<li><strong>Tonos de piel y profesiones son secuencias</strong> con ZWJ.</li>
<li><strong>Las banderas son indicadores regionales.</strong> 🇪🇸 = "🇪" + "🇸".</li>
<li><strong>Curado, no exhaustivo.</strong> Unicode 15 tiene 3664 emojis; aquí ~600.</li>
<li><strong>Selector de variación (U+FE0F)</strong> fuerza el estilo emoji.</li>
<li><strong>La API de portapapeles necesita un gesto</strong> (el clic basta).</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Les systèmes ont des sélecteurs d'emojis (Win+., Cmd+Ctrl+Espace), mais ils sont inconsistants et parfois lents. Cet outil fournit une grille curée par catégorie avec recherche par mot-clé. Clic = copie. Les récents sont conservés dans le stockage local — rien n'est envoyé à un serveur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Bureau sans raccourci rapide.</li>
<li>Recherche par mot-clé plus large.</li>
<li>Bureau distant ou système sans sélecteur natif.</li>
</ul>
<h3>Comment fonctionne le rendu</h3>
<p>Un emoji est un ou plusieurs points de code Unicode. L'apparence dépend de la police système (Apple, Google Noto, Microsoft Segoe). Les octets sont identiques.</p>
<h3>Pièges courants</h3>
<ul>
<li><strong>Teintes et professions sont des séquences</strong> avec ZWJ.</li>
<li><strong>Drapeaux = indicateurs régionaux.</strong> 🇫🇷 = "🇫" + "🇷".</li>
<li><strong>Curaté, non exhaustif.</strong> Unicode 15 a 3664 emojis ; ici ~600.</li>
<li><strong>Sélecteur de variation (U+FE0F)</strong> force le style emoji.</li>
<li><strong>L'API presse-papiers exige un geste</strong> (le clic suffit).</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>I sistemi operativi hanno selettori di emoji (Win+., Cmd+Ctrl+Spazio), ma sono inconsistenti e talvolta lenti. Questo strumento offre una griglia curata per categoria con ricerca per parola chiave. Clic = copia. I recenti rimangono nello storage locale — nulla viene inviato al server.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Desktop senza scorciatoia veloce.</li>
<li>Ricerca per parola chiave più ampia.</li>
<li>Desktop remoto o sistema senza selettore nativo.</li>
</ul>
<h3>Come funziona il rendering</h3>
<p>Un emoji è uno o più code point Unicode. L'aspetto dipende dal font di sistema (Apple, Google Noto, Microsoft Segoe). I byte sono identici.</p>
<h3>Errori comuni</h3>
<ul>
<li><strong>Tonalità e professioni sono sequenze</strong> con ZWJ.</li>
<li><strong>Le bandiere sono indicatori regionali.</strong> 🇮🇹 = "🇮" + "🇹".</li>
<li><strong>Curato, non esaustivo.</strong> Unicode 15 ha 3664 emoji; qui ~600.</li>
<li><strong>Variation Selector (U+FE0F)</strong> forza lo stile emoji.</li>
<li><strong>L'API clipboard richiede un gesto</strong> (il clic basta).</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Wszystkie systemy operacyjne mają pickery emoji (Win+. na Windowsie, Cmd+Ctrl+Spacja na macOS, klawiatura na telefonach), ale są niespójne, czasem ukryte i często powolne. To narzędzie daje wyselekcjonowaną siatkę najczęściej używanych emoji posortowanych po kategoriach i przeszukiwalnych po słowach kluczowych. Kliknij kafelek, żeby skopiować emoji do schowka. Ostatnio kopiowane emoji są zapamiętywane między wizytami w localStorage przeglądarki — nic nie idzie na serwer.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Jesteś na desktopie bez szybkiego skrótu emoji na poziomie OS.</li>
  <li>Chcesz wyszukiwania po słowach kluczowych szerszego niż oferuje picker OS.</li>
  <li>Używasz remote desktopa albo starszego systemu, który nie ma natywnego pickera.</li>
  <li>Potrzebujesz emoji do wklejenia w pole tekstowe, które nie akceptuje twojego IME.</li>
</ul>

<h3>Jak działa renderowanie</h3>
<p>Emoji to po prostu jeden albo więcej code pointów Unicode. <em>Jak</em> wygląda, zależy od fontu, który wybierze twoja przeglądarka/OS: emoji od Apple są inne niż Google Noto, Microsoft Segoe UI Emoji albo Twemoji od Twittera. Bajty są identyczne — obrazek jest lokalny. Jeśli emoji pokazuje się jako kwadrat albo "nieobsługiwane", twój systemowy font nie ma dla niego glifu; aktualizacja OS albo zainstalowanie fontu typu Noto Color Emoji to naprawia.</p>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Tony skóry i warianty rodzin/zawodów to sekwencje.</strong> 👨‍🍳 to "mężczyzna" + ZWJ + "gotowanie" — pięć code pointów. Niektóre systemy wyświetlają komponenty osobno, jeśli nie wspierają sekwencji.</li>
  <li><strong>Flagi to regional indicators.</strong> 🇵🇱 to "🇵" + "🇱" — dwie litery regional indicator. Sekwencje dla terytoriów (Szkocja, Teksas) wymagają dodatkowych tag characters i mogą nie renderować się na każdym systemie.</li>
  <li><strong>To narzędzie jest wyselekcjonowane, nie wyczerpujące.</strong> Unicode 15 ma 3664 emoji wliczając setki wariantów tonów skóry i płci. Picker skupia się na ~600, których prawdopodobnie chcesz; po pełną listę zerknij w dane emoji Unicode albo picker OS.</li>
  <li><strong>Niektóre znaki wyglądają jak emoji, ale renderują się jako tekst.</strong> "Variation selector" (U+FE0F) mówi rendererowi "narysuj to jako emoji". Bez tego ☂ może wyświetlić się jako zwykły tekst zamiast 🌂. Narzędzie dodaje selektory tam, gdzie trzeba.</li>
  <li><strong>Wsparcie schowka się różni.</strong> Clipboard API niektórych przeglądarek wymaga gestu użytkownika (kliknięcie to robi), ale odmowa uprawnień zawodzi po cichu. Jeśli kopiowanie nie działa, użyj skrótu klawiaturowego z paska adresu.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>OS には絵文字ピッカーが用意されています（Windows は Win+.、macOS は Cmd+Ctrl+Space、スマホはキーボード）が、挙動が一貫しなかったり、隠れていたり、遅かったりします。本ツールは、よく使われる絵文字をカテゴリ別に整理し、キーワードで検索できる厳選グリッドを提供します。タイルをクリックすればクリップボードにコピーされます。最近コピーした絵文字はブラウザの localStorage に保存され、再訪時にも残ります。サーバーには何も送信されません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>OS レベルの絵文字ショートカットがすぐに使えないデスクトップにいるとき。</li>
  <li>OS のピッカーより広いキーワード検索が欲しいとき。</li>
  <li>リモートデスクトップやネイティブピッカーがない古いシステムを使っているとき。</li>
  <li>IME が使えないテキストフィールドに絵文字を貼り付けたいとき。</li>
</ul>

<h3>レンダリングの仕組み</h3>
<p>絵文字は 1 つ以上の Unicode コードポイントです。<em>見た目</em>は、ブラウザや OS が選ぶフォントに依存します。Apple、Google Noto、Microsoft Segoe UI Emoji、Twitter の Twemoji ではそれぞれ異なります。バイトは同一で、画像はローカルで描画されます。もし絵文字が四角形や「未対応」のフォールバックで表示されるなら、システムフォントにグリフがありません。OS をアップデートするか、Noto Color Emoji のようなフォントをインストールしてください。</p>

<h3>よくある注意点</h3>
<ul>
  <li><strong>肌色や家族・職業のバリエーションはシーケンスです。</strong> 👨‍🍳 は「男性」+ ZWJ +「料理」など計 5 つのコードポイントから成ります。シーケンス未対応のシステムでは構成要素が個別に表示されることがあります。</li>
  <li><strong>国旗は Regional Indicator です。</strong> 🇯🇵 は「🇯」+「🇵」の 2 つの Regional Indicator 文字です。地域旗（スコットランド、テキサスなど）は追加のタグ文字が必要で、すべてのシステムで描画されるとは限りません。</li>
  <li><strong>本ツールは厳選版で、網羅していません。</strong> Unicode 15 には肌色や性別バリアントを含めて 3,664 個の絵文字があります。本ピッカーは使用頻度の高い約 600 個に絞っています。フルセットは Unicode の絵文字データや OS のピッカーをご覧ください。</li>
  <li><strong>絵文字に見えるが文字として描画される文字があります。</strong> "Variation Selector"（U+FE0F）が「絵文字として描画」を指示します。これがないと ☂ がプレーンテキストとして描画されます（🌂 にはなりません）。本ツールは必要な箇所でセレクタを付与します。</li>
  <li><strong>クリップボードのサポートはまちまちです。</strong> 一部ブラウザの Clipboard API はユーザー操作（クリックは該当）を要求しますが、権限拒否時には黙って失敗することがあります。コピーに失敗する場合はアドレスバーから手動コピーをお試しください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Besturingssystemen leveren allemaal emoji-pickers (Win+. op Windows, Cmd+Ctrl+Space op macOS, het toetsenbord op telefoons), maar ze zijn inconsistent, soms verborgen en vaak traag. Deze tool geeft je een gecureerd grid van de meest-gebruikte emoji geordend per categorie en doorzoekbaar op keyword. Klik een tegel om de emoji naar je klembord te kopiëren. Recent gekopieerde emoji worden tussen bezoeken onthouden in browser-local storage — niets wordt naar een server gestuurd.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Je zit op desktop zonder een snelle OS-level emoji-shortcut.</li>
  <li>Je wil een keyword-search die breder is dan je OS-picker biedt.</li>
  <li>Je gebruikt een remote desktop of ouder systeem zonder native picker.</li>
  <li>Je hebt een emoji nodig om te plakken in een tekstveld dat je IME niet accepteert.</li>
</ul>

<h3>Hoe rendering werkt</h3>
<p>Een emoji is gewoon één of meer Unicode code points. <em>Hoe</em> hij eruit ziet hangt af van de font die je browser/OS kiest: Apple's emoji verschillen van Google's Noto, Microsoft's Segoe UI Emoji en Twitter's Twemoji. De bytes zijn identiek — het plaatje is lokaal. Als een emoji als een vierkant of fallback "unsupported" verschijnt, heeft je systeem-font er geen glyph voor; de OS updaten of een font zoals Noto Color Emoji installeren fixt het.</p>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Huidstinten en family/profession-varianten zijn sequences.</strong> 👨‍🍳 is "man" + ZWJ + "kook" — vijf code points. Sommige systemen tonen de componenten apart als ze de sequence niet ondersteunen.</li>
  <li><strong>Vlaggen zijn regional indicators.</strong> 🇬🇧 is "🇬" + "🇧" — twee regional-indicator letters. Sequences voor territoria (Schotland, Texas) hebben extra tag-tekens nodig en renderen misschien niet op elk systeem.</li>
  <li><strong>Deze tool is gecureerd, niet uitputtend.</strong> Unicode 15 heeft 3.664 emoji inclusief honderden huidstint- en gender-varianten. De picker focust op de ~600 die je waarschijnlijk wil; voor de volle lijst zie Unicode's emoji-data of je OS-picker.</li>
  <li><strong>Sommige karakters lijken op emoji maar renderen als tekst.</strong> De "variation selector" (U+FE0F) zegt tegen de renderer "teken dit als emoji". Zonder dat rendert ☂ misschien als gewone tekst in plaats van 🌂. De tool voegt de selectors toe waar nodig.</li>
  <li><strong>Clipboard-ondersteuning varieert.</strong> Sommige browsers' clipboard-API vereist een user gesture (de klik doet dat), maar een permission denial faalt stil. Als kopiëren niet werkt, gebruik dan de toetsenbord-shortcut om vanuit de adresbalk te kopiëren.</li>
</ul>
""",
    },
    "related": ["unicode-inspector", "ascii-table", "lorem-ipsum"],
}
