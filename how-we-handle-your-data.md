# How we handle your data

**Toolhub — toolhub.software**
**Last updated:** 11 May 2026

This document is the plain-language version. It complements the privacy policy at <https://toolhub.software/privacy/>; if the two appear to disagree on a point, this document is the more specific one and should be treated as authoritative.

## Where data goes

Tools on Toolhub run in your browser. Anything you paste, type, or upload into a tool stays on your device — there is no server-side tool runner, and no upload endpoint behind any of the tools.

There are exactly three named exceptions to "no data leaves your device":

1. **YouTube Thumbnail tool** — when you submit a YouTube URL, your browser fetches the thumbnail directly from `i.ytimg.com` (YouTube's public image CDN). No authentication, no upload, no API key. The video ID in the URL is the only thing YouTube sees, and only because your browser fetched it.

2. **AdSense (only if enabled and consented)** — Google's display-ad system. When you grant ad consent, Google can see your IP address and may set cookies, governed by Google's policy. When you decline (the default), AdSense is not loaded at all.

3. **Plausible analytics** — counts page visits, referrer, country and device class. No cookies, no fingerprinting, aggregate statistics only. Plausible's servers are EU-hosted.

## What we store

Nothing about you. No accounts, no user IDs, no email, no profile. We do not store the content you put into tools.

Your browser stores two small localStorage entries on your device only — both readable and clearable from your browser's developer tools:

- `theme` — "light" or "dark", roughly one byte of preference.
- `toolhub:consent` — your ad consent decision (yes/no/unset). Used to avoid asking you again.

## GDPR, UK GDPR, CCPA and the Slovak DPA

Toolhub processes minimal data:

- **EU / UK (GDPR / UK GDPR):** Plausible (EU-hosted) gives a compliant analytics baseline. When AdSense is active, Google operates its own consent layer under TCF v2.
- **California (CCPA):** we do not sell personal information. We do not have personal information to sell.
- **Slovakia (Slovak Data Protection Authority):** Toolhub's maintainer is based in Slovakia. The Slovak DPA's rules apply to any processing that does occur — which is essentially limited to Plausible's aggregate metrics and (when enabled) AdSense's own consent-managed flow.

Rights to access or delete personal data effectively do not apply because no personal data is stored to access or delete. If you have specific questions, contact us via <https://toolhub.software/contact/>.

## Cookies

- **Plausible:** no cookies, ever.
- **Theme preference:** one localStorage entry, not a cookie. Stays on your device. Not transmitted with HTTP requests.
- **AdSense (when active):** Google sets its own third-party advertising cookies. The consent banner appears before any AdSense script is loaded, and AdSense is not loaded at all if you decline.

## Children

Toolhub is school-friendly (see Toolhub for schools at <https://toolhub.software/for-schools/>). There is no behavioral tracking and no targeted advertising. Under-13 use is acceptable within the existing AdSense terms applied per region — meaning if you are in a region where AdSense restricts ads to children, those restrictions are honored by Google's own systems.

## Downloadable PDF

This PDF is the offline-friendly version of <https://toolhub.software/how-we-handle-your-data/>. It is English only at this stage; per-language PDFs are not in scope for the current release.

## Questions

If anything here is unclear, please open an issue at <https://github.com/JXXR1/Toolhub> or use the contact page at <https://toolhub.software/contact/>. Clarifying questions are a useful way to make this page better for the next reader.
