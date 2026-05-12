# Toolhub deploy-time config setup

All deploy-time switches live in one place: the `window.TOOLHUB_CONFIG`
object literal in `build/template.html`. Empty / unset values default to
safe sandbox behaviour — the site builds and renders fine with everything
blank, so don't worry about partial setups.

## Cloudflare Web Analytics

Privacy-preserving page-view analytics. No cookies, no fingerprinting, no
PII, GDPR-compliant by default — no consent banner required.

1. Sign up at https://dash.cloudflare.com → Web Analytics → "Add a site"
2. Enter `toolhub.software` (or your domain)
3. Copy the JavaScript snippet token (the hex string after `"token":"…"`)
4. In `build/template.html`, set:

   ```js
   cloudflareAnalyticsToken: "<your-token-here>",
   ```

   inside the `window.TOOLHUB_CONFIG` block.
5. Rebuild and push:

   ```bash
   python3 build/build.py
   git add -A
   git commit -m "config: enable Cloudflare Web Analytics"
   git push
   ```

That's it. No DNS changes needed; the beacon is JS-only.

The site works identically whether analytics is on or off. With an empty
token the inline gate exits before any network request — Cloudflare is
never contacted at all. With a token set, a single `defer`-loaded script
is injected just before `</body>`.

The build validates that a non-empty token in `deploy_env="production"`
matches `/^[a-f0-9]{32,}$/i` (Cloudflare tokens are hex strings, typically
32–64 chars). A malformed token fails the build instead of shipping
broken analytics.

## AdSense

Optional display ads. Off by default — sandbox mode renders placeholder
ad boxes and never loads `adsbygoogle.js`.

1. Get approved at https://www.google.com/adsense/
2. Note your publisher ID (format `ca-pub-NNNNNNNNNNNNNNNN`, 16 digits)
3. Create at least one ad unit and copy its slot ID
4. In `build/template.html`, set:

   ```js
   deploy_env: "production",
   adsenseClientId: "ca-pub-XXXXXXXXXXXXXXXX",
   adSlotIds: { content: "1234567890", footer: "", indexTop: "", indexBottom: "" },
   ```

5. Rebuild and push.

The build refuses to ship `deploy_env="production"` unless the client ID
matches the expected shape and at least one slot ID is set.

## DigitalOcean / GitHub Sponsors / Buy Me a Coffee

These are plain URL strings — replace with your own referral / sponsor
links. They are never validated; an empty string just disables the
corresponding link in the footer.
