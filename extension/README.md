# Toolhub browser extension

Right-click any selected text in your browser → "Open in Toolhub" → the
matching tool opens at [toolhub.software](https://toolhub.software) with the
text pre-filled.

Pairs with the URL-fragment prefill bridge in
[`build/template.html`](../build/template.html) (see
[`build/EXT-INTEGRATION.md`](../build/EXT-INTEGRATION.md)).

## What it does

When you right-click selected text, the extension detects the content type
(in order, first match wins):

| # | Detector            | Opens                  |
|---|---------------------|------------------------|
| 1 | JWT (header has `alg`)        | `jwt-decoder`         |
| 2 | JSON (parses cleanly)         | `json-formatter`      |
| 3 | CIDR (`N.N.N.N/M`)            | `cidr-calculator`     |
| 4 | URL-encoded (`%XX` present)   | `url-encoder`         |
| 5 | Base64 (strict charset, ≥16)  | `base64-encoder`      |
| 6 | HTML (starts with a tag)      | `html-formatter`      |
| 7 | Markdown-ish (heads/links/`code`) | `markdown-to-html` |
| 8 | Anything else                 | homepage with `?q=`   |

A toolbar-icon click opens the Toolhub homepage in a new tab.

## Privacy

- **No telemetry.** No analytics, no error reporting, no remote logging.
- **No storage.** No cookies, localStorage, IndexedDB, or sync state.
- **No host permissions.** The extension cannot read or modify page contents.
- **Data travels in the URL fragment.** Fragments (`#...`) are client-only —
  browsers never send them in `Referer` headers or request bodies, so even
  sensitive payloads (JWTs, API responses) never leave your machine over the
  wire.
- **Only permission requested:** `contextMenus` — needed to add the
  right-click menu item.

See [`PRIVACY.md`](./PRIVACY.md) for the full statement.

## Tools currently wired for auto-prefill

10 tools listen for the `toolhub:prefill` event the bridge dispatches:

`json-formatter`, `base64-encoder`, `url-encoder`, `jwt-decoder`,
`cidr-calculator`, `regex-tester`, `hash-generator`, `html-formatter`,
`markdown-to-html`, `slug-generator`.

Other tools still open from the extension — they just don't auto-fill
their inputs yet. Wiring the rest is mechanical (see EXT-INTEGRATION.md).

## Local development

1. Open `chrome://extensions/` (or `edge://extensions/`)
2. Enable **Developer mode** (top-right)
3. Click **Load unpacked**
4. Select this `extension/` directory
5. Select some text on any page, right-click → "Open in Toolhub"

Firefox: open `about:debugging#/runtime/this-firefox` → "Load Temporary
Add-on…" → pick `manifest.json`. Firefox 121+ supports MV3 module service
workers used here.

After editing files, hit the reload icon in `chrome://extensions/` to pick
up changes (or remove + re-add the unpacked extension).

## Build for store submission

```bash
./package.zip-build.sh
```

Produces `toolhub-extension-v<version>.zip` in this directory. Upload that to:

- **Chrome Web Store** — <https://chrome.google.com/webstore/devconsole> (one-time $5 developer fee)
- **Edge Add-ons** — <https://partner.microsoft.com/dashboard/microsoftedge> (free)
- **Firefox AMO** — <https://addons.mozilla.org/developers/> (free)

The zip is gitignored (`extension/*.zip`); regenerate on each release.

## File layout

```
extension/
├── manifest.json              MV3 manifest (Chrome / Edge / Firefox 121+)
├── background.js              Service worker — context menu + action click
├── auto-detect.js             Pure content-type detection
├── tool-map.js                Slug → toolhub.software URL with #data= payload
├── icons/                     16/32/48/128 PNGs (rendered from favicon.svg)
├── _locales/en/messages.json  Extension UI strings (multi-lang in v2)
├── package.zip-build.sh       Bundles for store upload
├── README.md                  This file
└── PRIVACY.md                 Privacy statement (required by stores)
```

## Versions

- **0.1.0** — first release: context-menu deep-link with auto-detect for
  JWT / JSON / CIDR / URL-encoded / Base64 / HTML / Markdown.
