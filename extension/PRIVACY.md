# Privacy statement — Toolhub browser extension

**TL;DR:** the extension does not collect, store, or transmit your data to
any server. The only thing it does is open a new tab at toolhub.software
with text you explicitly selected.

## What the extension collects

**Nothing.** No analytics, no telemetry, no error reporting, no usage
statistics, no crash reports.

## What the extension stores

**Nothing.** No cookies, no `localStorage`, no `IndexedDB`, no sync state,
no preferences, no history.

## What the extension transmits

Only the text you actively select and click "Open in Toolhub" on. That text
is placed into the **URL fragment** of a new tab — for example:

```
https://toolhub.software/jwt-decoder/#data=<your-selected-text>
```

URL fragments (the part after `#`) are a special part of a URL: browsers
keep them client-side only. They are **never** included in:

- `Referer` headers,
- request bodies,
- server access logs,
- network analytics.

The Toolhub tool then reads the fragment **inside your browser** to populate
its input field. The data is never uploaded.

## Permissions

The extension requests exactly one Chrome / Edge / Firefox permission:

| Permission     | Purpose                                                |
|----------------|--------------------------------------------------------|
| `contextMenus` | Add the "Open in Toolhub" right-click menu item.       |

The extension does **not** request:

- `activeTab` or any host permission (cannot read or modify page contents)
- `storage` (cannot persist any state)
- `tabs` beyond `chrome.tabs.create` (does not enumerate, inspect, or close
  your tabs)
- `webRequest` / `webNavigation` (does not observe your browsing)
- `notifications`, `cookies`, `history`, `bookmarks`, `downloads`, `webNavigation`

## Third-party services

The extension does not contact any third-party service. The only network
request happens when the new Toolhub tab loads — which is the same request
you would make by visiting toolhub.software directly in your browser.

Toolhub itself has no third-party trackers; see
<https://toolhub.software/how-we-handle-your-data>.

## Open source

This extension is open source. You can audit every line at:

<https://github.com/JXXR1/Toolhub/tree/main/extension>

## Contact

Questions or concerns? Open an issue at
<https://github.com/JXXR1/Toolhub/issues>.
