# Extension prefill convention

The browser extension can deep-link to any tool with data pre-populated via:
`https://toolhub.software/<tool-slug>/#data=<URLencoded payload>`

The bridge script in `template.html` reads `window.location.hash`, decodes the
`data=` parameter, and dispatches a `toolhub:prefill` `CustomEvent` ~50ms after
`DOMContentLoaded` (giving per-tool init scripts time to attach their listeners
first).

## Privacy property

URL fragments (`#...`) are client-only — they are NEVER sent in `Referer`
headers, request bodies, or any network traffic. This preserves Toolhub's "no
upload" brand promise even when the extension deep-links with sensitive payloads
(JWTs, API responses, etc.).

The bridge will NEVER read query-string data (`?data=`) — only the fragment.

## How to make a NEW tool extension-compatible

Add this at the end of the tool's `<script>` block, just before `</script>`:

```javascript
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('YOUR-INPUT-ID');
  if (!input) return;
  input.value = e.detail.data;
  YOURRunFunction();
});
```

Replace `YOUR-INPUT-ID` with the main input element's ID and `YOURRunFunction`
with whatever the tool calls when fresh input arrives (e.g. `b64Run`, `mdRun`,
`cidrRun`). Trigger a real run so the user lands on a populated, already-
processed page.

## Currently-wired tools (EXT-1 batch)

| Slug              | Input ID    | Run fn        |
|-------------------|-------------|---------------|
| json-formatter    | `json-input`| `jfFormat(2)` |
| base64-encoder    | `b64-in`    | `b64Run()`    |
| url-encoder       | `url-in`    | `urlRun()`    |
| jwt-decoder       | `jwt-in`    | `jwtDecode()` |
| cidr-calculator   | `cidr-in`   | `cidrRun()`   |
| regex-tester      | `re-input`  | `reRun()`     |
| hash-generator    | `h-in`      | `hRun()`      |
| html-formatter    | `hf-in`     | `hfRun()`     |
| markdown-to-html  | `md-in`     | `mdRun()`     |
| slug-generator    | `sg-input`  | `sgRun()`     |

The remaining 81 tools can be wired incrementally — the extension still works
for them (the bridge just dispatches an event nothing listens to, which is a
no-op).

## Test verification

Manually verify by visiting (after build):

```
https://toolhub.software/json-formatter/#data=%7B%22hello%22%3A%22world%22%7D
```

The input field should auto-populate with `{"hello":"world"}` and the formatter
should run, producing pretty-printed output.

For local testing, open the built file directly:

```
file:///root/projects/toolhub-deploy/json-formatter/index.html#data=%7B%22hello%22%3A%22world%22%7D
```
