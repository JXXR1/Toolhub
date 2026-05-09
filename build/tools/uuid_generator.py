TOOL = {
    "slug": "uuid-generator",
    "category": "developer",
    "icon": "🆔",
    "tags": ["uuid", "guid", "v4", "v7", "random", "unique", "identifier"],
    "i18n": {
        "en": {
            "name": "UUID Generator",
            "tagline": "Generate RFC 4122 UUIDs (v4 random or v7 time-ordered). Batch up to 100. Cryptographically secure.",
            "description": "Free online UUID generator. RFC 4122 v4 (random) and v7 (time-ordered, sortable). Generate one or many at a time, all in your browser.",
        },
        "de": {
            "name": "UUID-Generator",
            "tagline": "RFC 4122 UUIDs erzeugen (v4 zufällig oder v7 zeitgeordnet). Bis zu 100 auf einmal. Kryptographisch sicher.",
            "description": "Kostenloser UUID-Generator. RFC 4122 v4 (zufällig) und v7 (zeitgeordnet, sortierbar). Einzeln oder im Stapel erzeugen, alles im Browser.",
        },
        "es": {
            "name": "Generador UUID",
            "tagline": "Genera UUIDs RFC 4122 (v4 aleatorio o v7 ordenado por tiempo). Hasta 100 por lote. Criptográficamente seguro.",
            "description": "Generador UUID gratuito en línea. RFC 4122 v4 (aleatorio) y v7 (ordenado por tiempo). Genera uno o varios, todo en tu navegador.",
        },
        "fr": {
            "name": "Générateur UUID",
            "tagline": "Générez des UUIDs RFC 4122 (v4 aléatoire ou v7 ordonné par temps). Jusqu'à 100 à la fois. Cryptographiquement sûr.",
            "description": "Générateur UUID gratuit en ligne. RFC 4122 v4 (aléatoire) et v7 (ordonné par temps, triable). Un ou plusieurs, tout dans votre navigateur.",
        },
        "it": {
            "name": "Generatore UUID",
            "tagline": "Genera UUID RFC 4122 (v4 casuale o v7 ordinato per tempo). Fino a 100 per batch. Crittograficamente sicuro.",
            "description": "Generatore UUID gratuito online. RFC 4122 v4 (casuale) e v7 (ordinato per tempo, ordinabile). Uno o molti, tutto nel browser.",
        },
        "pt": {
            "name": "Gerador de UUID",
            "tagline": "Gere UUIDs RFC 4122 (v4 aleatório ou v7 ordenado por tempo). Em lote de até 100. Criptograficamente seguro.",
            "description": "Gerador de UUID online gratuito. RFC 4122 v4 (aleatório) e v7 (ordenado por tempo, sortable). Gere um ou vários de uma vez, tudo no seu navegador.",
        },
        "pl": {
            "name": "Generator UUID",
            "tagline": "Generuj UUID-y RFC 4122 (v4 losowy albo v7 uporządkowany czasem). Hurtowo do 100. Kryptograficznie bezpieczny.",
            "description": "Darmowy online generator UUID. RFC 4122 v4 (losowy) i v7 (uporządkowany czasem, sortowalny). Generuj jeden albo wiele naraz, wszystko w przeglądarce.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Version</label>
      <select id="uuid-ver">
        <option value="4">v4 (random)</option>
        <option value="7">v7 (time-ordered, sortable)</option>
      </select>
    </div>
    <div>
      <label>{LBL_COUNT} (1-100)</label>
      <input type="number" id="uuid-count" value="1" min="1" max="100">
    </div>
  </div>
  <div class="button-row">
    <button onclick="uuidGen()">{LBL_GENERATE}</button>
    <button class="secondary" onclick="copyOutput('uuid-out', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <pre class="output" id="uuid-out"></pre>
</div>
""",
    "script": """
<script>
function uuidV4(){
  const b = new Uint8Array(16);
  crypto.getRandomValues(b);
  b[6] = (b[6] & 0x0f) | 0x40;
  b[8] = (b[8] & 0x3f) | 0x80;
  const h = [...b].map(x => x.toString(16).padStart(2,'0'));
  return h.slice(0,4).join('') + '-' + h.slice(4,6).join('') + '-' + h.slice(6,8).join('') + '-' + h.slice(8,10).join('') + '-' + h.slice(10,16).join('');
}
function uuidV7(){
  // RFC 9562 v7: 48-bit unix-ms timestamp + 12 bits rand_a + 62 bits rand_b + version/variant bits
  const ts = BigInt(Date.now());
  const r = new Uint8Array(10);
  crypto.getRandomValues(r);
  const b = new Uint8Array(16);
  // 6 bytes of timestamp (big-endian)
  for (let i = 0; i < 6; i++) b[i] = Number((ts >> BigInt(40 - 8*i)) & 0xffn);
  for (let i = 0; i < 10; i++) b[i+6] = r[i];
  b[6] = (b[6] & 0x0f) | 0x70;     // version 7
  b[8] = (b[8] & 0x3f) | 0x80;     // variant 10
  const h = [...b].map(x => x.toString(16).padStart(2,'0'));
  return h.slice(0,4).join('') + '-' + h.slice(4,6).join('') + '-' + h.slice(6,8).join('') + '-' + h.slice(8,10).join('') + '-' + h.slice(10,16).join('');
}
function uuidGen(){
  const ver = document.getElementById('uuid-ver').value;
  const n = Math.max(1, Math.min(100, parseInt(document.getElementById('uuid-count').value, 10) || 1));
  const out = [];
  for (let i = 0; i < n; i++) out.push(ver === '7' ? uuidV7() : uuidV4());
  document.getElementById('uuid-out').textContent = out.join('\\n');
}
document.addEventListener('DOMContentLoaded', uuidGen);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A UUID (or GUID) is a 128-bit identifier — written as 32 hex digits in 5 groups, like <code>550e8400-e29b-41d4-a716-446655440000</code>. They're collision-free across systems without coordination: any process anywhere can mint one and the chance of two ever colliding is effectively zero. Useful when you need an ID before talking to a database, when you want to avoid leaking row counts, or when an ID has to be generated client-side and synced later. This tool emits RFC 4122 / RFC 9562 compliant UUIDs in v4 (random) or v7 (time-ordered) form, generated with cryptographically-secure randomness in your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Primary keys for distributed systems where you don't want to round-trip to the database for an ID.</li>
  <li>Idempotency keys for API requests (stripe, payment providers, queue messages).</li>
  <li>File-upload identifiers, session tokens, correlation IDs in logs.</li>
  <li>Anywhere you'd otherwise expose an auto-incrementing ID and leak how many records you have.</li>
  <li>Test data — seed a hundred records with realistic identifiers in one click.</li>
</ul>

<h3>v4 vs v7 — which should I use?</h3>
<ul>
  <li><strong>v4 (random)</strong> — 122 bits of randomness, no embedded creation time. Use when you want zero correlation between IDs and creation order, or when the ID will live in a hash-map / non-clustered index where ordering doesn't matter.</li>
  <li><strong>v7 (time-ordered)</strong> — 48-bit Unix-ms timestamp prefix + random tail. <strong>Default to this for new database primary keys.</strong> The timestamp prefix gives B-tree indexes locality (recent inserts go to the same pages, much better cache behaviour than v4), and IDs sort in roughly chronological order. Defined in RFC 9562 (May 2024) — supersedes ULID and v1/v6 for most use cases.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>UUIDs are not secrets.</strong> v4 has 122 bits of entropy and is unguessable, but the format itself doesn't authorize anything. Don't use a UUID as a session token or password-reset token unless you're treating it as a secret (HTTPS-only, time-limited, single-use).</li>
  <li><strong>v7 leaks creation time.</strong> The first 48 bits encode the millisecond it was minted. Fine for internal IDs; bad if you don't want users to learn when records were created. Use v4 in that case.</li>
  <li><strong>Index size matters.</strong> A UUID is 16 bytes vs 8 for a bigint — your B-tree indexes get bigger. Worth it for distributed/no-coordination, often not worth it for single-server apps with a sequential ID.</li>
  <li><strong>v4 fragments database indexes.</strong> Random IDs scatter writes across the index, hurting page cache hit rate and write throughput. This is the original argument for v7.</li>
  <li><strong>Don't use v1.</strong> The old time-and-MAC variant leaks the generating machine's MAC address. v7 is the modern replacement.</li>
  <li><strong>Use crypto-secure randomness.</strong> This tool uses <code>crypto.getRandomValues</code>; never roll your own with <code>Math.random</code> — it's not random enough and IDs become predictable.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um UUID (ou GUID) é um identificador de 128 bits — escrito como 32 dígitos hex em 5 grupos, tipo <code>550e8400-e29b-41d4-a716-446655440000</code>. Eles são livres de colisão entre sistemas sem precisar de coordenação: qualquer processo em qualquer lugar pode gerar um e a chance de dois colidirem é praticamente zero. Útil quando você precisa de um ID antes de falar com o banco, quando quer evitar vazar contagem de linhas, ou quando o ID tem que ser gerado no cliente e sincronizado depois. Esta ferramenta gera UUIDs em conformidade com RFC 4122 / RFC 9562 na forma v4 (aleatória) ou v7 (ordenada por tempo), com aleatoriedade criptograficamente segura no seu navegador.</p>

<h3>Quando usar</h3>
<ul>
  <li>Primary keys para sistemas distribuídos quando você não quer fazer round-trip ao banco só para pegar um ID.</li>
  <li>Idempotency keys para requisições de API (Stripe, processadores de pagamento, mensagens de fila).</li>
  <li>Identificadores de upload de arquivo, session tokens, correlation IDs em logs.</li>
  <li>Em qualquer lugar onde você expõe um ID auto-incrementado e acaba vazando quantos registros tem.</li>
  <li>Dados de teste — semeie cem registros com identificadores realistas com um clique.</li>
</ul>

<h3>v4 vs v7 — qual usar?</h3>
<ul>
  <li><strong>v4 (aleatório)</strong> — 122 bits de aleatoriedade, sem timestamp embutido. Use quando quiser zero correlação entre IDs e ordem de criação, ou quando o ID vai viver em um hash map / índice não-clusterizado onde ordenação não importa.</li>
  <li><strong>v7 (ordenado por tempo)</strong> — prefixo de timestamp Unix-ms de 48 bits + cauda aleatória. <strong>Use por padrão para novas primary keys de banco.</strong> O prefixo de timestamp dá localidade aos índices B-tree (inserts recentes vão para as mesmas páginas, comportamento de cache muito melhor que v4), e os IDs ordenam aproximadamente em ordem cronológica. Definido na RFC 9562 (maio de 2024) — substitui ULID e v1/v6 na maioria dos casos.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>UUIDs não são segredos.</strong> v4 tem 122 bits de entropia e é impossível de adivinhar, mas o formato em si não autoriza nada. Não use um UUID como session token ou token de reset de senha a menos que esteja tratando como segredo (HTTPS-only, com tempo limitado, single-use).</li>
  <li><strong>v7 vaza tempo de criação.</strong> Os primeiros 48 bits codificam o milissegundo em que foi gerado. Tudo bem para IDs internos; ruim se você não quer que usuários descubram quando os registros foram criados. Use v4 nesse caso.</li>
  <li><strong>Tamanho do índice importa.</strong> Um UUID tem 16 bytes vs 8 de um bigint — seus índices B-tree ficam maiores. Vale a pena para distribuído/sem coordenação, geralmente não vale para apps de servidor único com ID sequencial.</li>
  <li><strong>v4 fragmenta índices de banco.</strong> IDs aleatórios espalham writes pelo índice, prejudicando a taxa de hit do cache de páginas e a vazão de escrita. Esse é o argumento original a favor do v7.</li>
  <li><strong>Não use v1.</strong> A variante antiga de tempo-e-MAC vaza o endereço MAC da máquina geradora. v7 é o substituto moderno.</li>
  <li><strong>Use aleatoriedade crypto-segura.</strong> Esta ferramenta usa <code>crypto.getRandomValues</code>; nunca implemente sua própria solução com <code>Math.random</code> — não é aleatório o suficiente e os IDs ficam previsíveis.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>UUID (albo GUID) to 128-bitowy identyfikator — zapisywany jako 32 cyfry hex w 5 grupach, np. <code>550e8400-e29b-41d4-a716-446655440000</code>. Są bezkolizyjne między systemami bez koordynacji: dowolny proces gdziekolwiek może wygenerować jeden, a szansa, że dwa kiedykolwiek się zderzą, jest praktycznie zerowa. Przydatne, gdy potrzebujesz ID przed rozmową z bazą, gdy chcesz uniknąć wycieku liczby wierszy, albo gdy ID musi powstać po stronie klienta i zostać zsynchronizowany później. To narzędzie generuje UUID-y zgodne z RFC 4122 / RFC 9562 w formie v4 (losowej) albo v7 (uporządkowanej czasem), z kryptograficznie bezpieczną losowością w przeglądarce.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Klucze główne w systemach rozproszonych, gdy nie chcesz robić round-tripu do bazy po ID.</li>
  <li>Idempotency keys dla requestów API (Stripe, providery płatności, wiadomości w kolejce).</li>
  <li>Identyfikatory uploadu plików, session tokeny, correlation ID-ki w logach.</li>
  <li>Wszędzie tam, gdzie inaczej eksponowałbyś auto-incrementowane ID i wyciekał, ile masz rekordów.</li>
  <li>Dane testowe — zaseeduj sto rekordów realistycznymi identyfikatorami jednym kliknięciem.</li>
</ul>

<h3>v4 vs v7 — którego użyć?</h3>
<ul>
  <li><strong>v4 (losowy)</strong> — 122 bity losowości, brak osadzonego czasu utworzenia. Używaj, gdy chcesz zerowej korelacji między ID a kolejnością tworzenia, albo gdy ID będzie żył w hash-mapie / nieklastrowanym indeksie, gdzie kolejność nie ma znaczenia.</li>
  <li><strong>v7 (uporządkowany czasem)</strong> — 48-bitowy prefiks Unix-ms timestamp + losowy ogon. <strong>Domyślnie używaj go do nowych kluczy głównych w bazie.</strong> Prefiks timestampu daje indeksom B-tree lokalność (świeże inserty trafiają do tych samych stron, znacznie lepsze zachowanie cache niż v4), a ID-ki sortują się mniej więcej w porządku chronologicznym. Zdefiniowany w RFC 9562 (maj 2024) — wypiera ULID i v1/v6 w większości zastosowań.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>UUID-y to nie sekrety.</strong> v4 ma 122 bity entropii i jest nie do zgadnięcia, ale sam format niczego nie autoryzuje. Nie używaj UUID-a jako session tokena ani tokena resetu hasła, chyba że traktujesz go jak sekret (HTTPS-only, ograniczony czasowo, jednokrotny).</li>
  <li><strong>v7 wycieka czas utworzenia.</strong> Pierwsze 48 bitów koduje milisekundę, w której był wygenerowany. OK do ID wewnętrznych; źle, gdy nie chcesz, żeby użytkownicy dowiadywali się, kiedy rekordy powstały. W takim wypadku użyj v4.</li>
  <li><strong>Rozmiar indeksu ma znaczenie.</strong> UUID to 16 bajtów vs 8 dla bigint — twoje indeksy B-tree rosną. Warto dla rozproszenia/braku koordynacji, często niewarto dla apek na jednym serwerze z sekwencyjnym ID.</li>
  <li><strong>v4 fragmentuje indeksy bazy.</strong> Losowe ID rozsiewają zapisy po indeksie, psując hit rate cache stron i przepustowość zapisu. To oryginalny argument za v7.</li>
  <li><strong>Nie używaj v1.</strong> Stary wariant time-and-MAC wycieka adres MAC maszyny generującej. v7 to nowoczesny zamiennik.</li>
  <li><strong>Używaj kryptograficznie bezpiecznej losowości.</strong> To narzędzie używa <code>crypto.getRandomValues</code>; nigdy nie pisz własnego z <code>Math.random</code> — nie jest wystarczająco losowy i ID-ki stają się przewidywalne.</li>
</ul>
""",
    },
    "related": ["password-generator", "hash-generator", "timestamp-converter"],
}
