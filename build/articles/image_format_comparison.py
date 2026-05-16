"""Article: JPG vs WebP vs AVIF — when to use each.

Weekly article ARTICLES-W02 / image vertical. ~1050 words, English only
for this batch (translations come later).
"""

ARTICLE = {
    "slug": "image-format-comparison",
    "date": "2026-05-16",
    "author": "Toolhub Team",
    "category": "image",
    "tags": ["images", "webp", "avif", "jpeg", "performance", "web"],
    "tool_refs": ["image-convert", "image-compress", "exif-stripper", "image-resize"],
    "title": {
        "en": "JPG vs WebP vs AVIF: when to use each",
    },
    "subtitle": {
        "en": "Three image formats, three different jobs. A practical guide to choosing one without burning a weekend on encoder benchmarks.",
    },
    "summary": {
        "en": "JPEG, WebP, and AVIF each win different fights — file size, compatibility, encode time, animation support. A practical guide to picking the right one without re-encoding your entire CDN.",
    },
    "body": {
        "en": r"""
<p>You have a 4&nbsp;MB JPEG. Lighthouse is yelling at you. Someone on Hacker News said AVIF is "30% smaller than WebP." Your PM wants the hero image to load in under 200&nbsp;ms on a 4G connection in Lagos. You open three browser tabs, read three contradictory benchmarks, and end up converting everything to WebP because it sounds like the safe middle. That choice is fine — most of the time. But "most of the time" hides three different jobs, and the wrong format costs you either bandwidth, compatibility, or build time you don't have to spend.</p>

<p>Here's the practical breakdown — what each format is actually good at, the gotchas the marketing pages skip, and a decision tree you can apply in under thirty seconds.</p>

<h2>1. JPEG: the lingua franca that won't quit</h2>

<p>JPEG turns 33 this year. It still ships on every camera, every browser, every photo printer, and the vast majority of the open web. The format compresses photographs by throwing away high-frequency detail in 8×8 pixel blocks — a technique called the discrete cosine transform — which is exactly the right trade-off for natural images full of gradients.</p>

<p>Where JPEG falls down: text, line art, screenshots, anything with sharp edges. The blockiness you see around UI elements in a poorly-encoded JPEG is the algorithm doing its job badly on content it wasn't designed for. It also has no alpha channel — transparent PNG-to-JPEG conversions get flattened to white (or whatever background the encoder picks).</p>

<p>The honest reason to still reach for JPEG in 2026 is reach. If your audience includes a long tail of legacy clients — embedded browsers, RSS readers, screenshot bots, ten-year-old phones — JPEG is the format that everything reads without a fallback chain.</p>

<h2>2. WebP: the obvious 2020s default</h2>

<p>Google released WebP in 2010 and spent a decade arguing for it. In 2020 Safari finally shipped support, and the format went from "Chrome's pet project" to a real cross-browser option overnight. WebP supports both lossy and lossless modes, has an alpha channel, supports animation (think small video clips replacing GIFs), and produces files roughly 25–35% smaller than equivalent JPEGs at matching visual quality.</p>

<blockquote>
  <p>"WebP is an image format that uses either (i) the VP8 key frame encoding to compress image data in a lossy way, or (ii) the WebP lossless encoding. These encoding schemes should make it more efficient than currently used formats."</p>
  <cite>— <a href="https://datatracker.ietf.org/doc/html/rfc9649#section-1" rel="noopener">RFC 9649 §1</a> (IETF, public domain)</cite>
</blockquote>

<p>The catch: WebP's lossless mode is excellent (often beating PNG by 20–30%) but its lossy mode at very high quality settings produces softer images than JPEG. If you compare a JPEG quality-95 and a WebP quality-95 side by side, the WebP sometimes looks slightly smudged on fine textures — skin, fabric, foliage. At quality-80 and below, WebP wins almost every time.</p>

<h2>3. AVIF: the bandwidth king (with caveats)</h2>

<p>AVIF arrived in 2019, built on the AV1 video codec, and the compression ratios are genuinely startling. A photograph that's 200&nbsp;KB as a JPEG is often 80&nbsp;KB as a WebP and 40–60&nbsp;KB as an AVIF at matching quality. For a hero image on a marketing page, that's the difference between hitting a Core Web Vitals target and missing it.</p>

<p>The caveats are real, though. AVIF encoding is <em>slow</em> — on a typical CI runner, encoding a single 4K image can take 30 seconds or longer at the higher effort settings. Cached encodes solve this for serving, but the first build of a 5,000-image catalog can ruin your afternoon. Decode is fast, but older devices (anything pre-2021 on mobile) may struggle on long pages with dozens of AVIFs.</p>

<p>Browser support hit "good enough" in late 2023 when Edge joined Chrome, Firefox, and Safari. Anything older than that needs a fallback — usually a <code>&lt;picture&gt;</code> element listing AVIF, WebP, JPEG in order.</p>

<h2>4. The 30-second decision tree</h2>

<p>If you're picking one format and stopping there:</p>

<ul>
  <li><strong>Photographs, modern web audience</strong> → AVIF with a WebP fallback. Saves real bandwidth.</li>
  <li><strong>Photographs, mixed audience (older devices, email, embedded)</strong> → WebP with a JPEG fallback. Honest middle ground.</li>
  <li><strong>Screenshots, UI mockups, charts</strong> → WebP lossless, or PNG if you need anything to consume it without fuss.</li>
  <li><strong>Animations under 5 MB</strong> → WebP. AVIF supports animation but tooling is patchier.</li>
  <li><strong>"It must work everywhere, even in 2007"</strong> → JPEG. Don't overthink it.</li>
</ul>

<p>The browser-friendly way to ship this is a <code>&lt;picture&gt;</code> element with <code>&lt;source&gt;</code> children — the browser picks the first format it understands and ignores the rest. No JavaScript, no UA sniffing.</p>

<h2>5. Encoder traps that bite people</h2>

<p>Three pitfalls we've seen burn even careful teams. First, <em>quality numbers don't translate across formats</em>. WebP quality-80 is not the same perceptual quality as JPEG quality-80 — WebP at 80 is closer to JPEG at 90. Re-encoding "at the same quality" between formats almost always means re-tuning per format.</p>

<p>Second, <em>EXIF and color profiles travel with the file</em> unless you strip them. A camera-original JPEG might carry GPS coordinates, lens serial numbers, and 12&nbsp;KB of ICC profile metadata. WebP and AVIF preserve this faithfully — meaning the "smaller" file you served might still be leaking location data from the photographer's phone. Our <a href="/exif-stripper/">EXIF stripper</a> removes this in one step before you encode.</p>

<p>Third, <em>resizing first beats encoding harder</em>. A 4000-pixel-wide image displayed at 800px is wasting 96% of the bytes. Resize to the displayed dimensions (or 2× for retina) <em>then</em> encode. Our <a href="/image-resize/">image resize</a> and <a href="/image-compress/">image compress</a> tools run entirely in the browser — useful when you don't want to upload originals to a third-party service.</p>

<h2>The pragmatic bottom line</h2>

<p>For most websites in 2026, the right answer is <em>both</em>: serve AVIF to modern browsers, WebP to slightly older ones, JPEG as the last resort. The bandwidth savings on AVIF alone usually pay for the extra storage within weeks. If you only ship one format — pick WebP. It's the format whose support story is least likely to bite you. Need to convert images between any of these without uploading them anywhere? Our <a href="/image-convert/">image converter</a> handles all three formats in the browser, no server round-trip.</p>
""".strip(),
    },
}
