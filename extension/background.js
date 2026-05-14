// Toolhub browser-extension service worker (Manifest V3).
//
// Wires the "Open in Toolhub" context-menu item: detects the content type of
// the selected text and opens the matching tool at toolhub.software with the
// payload pre-filled via URL fragment (handled by EXT-1's prefill bridge).
//
// Toolbar-icon click opens the Toolhub homepage in a new tab.

import { detect } from './auto-detect.js';
import { buildUrl } from './tool-map.js';

const MENU_ID = 'toolhub-open';

function ensureMenu() {
  chrome.contextMenus.removeAll(() => {
    chrome.contextMenus.create({
      id: MENU_ID,
      title: 'Open in Toolhub: %s',
      contexts: ['selection'],
    });
  });
}

chrome.runtime.onInstalled.addListener(ensureMenu);
chrome.runtime.onStartup.addListener(ensureMenu);

chrome.contextMenus.onClicked.addListener((info) => {
  if (info.menuItemId !== MENU_ID) return;
  const text = info.selectionText || '';
  if (!text) return;
  const result = detect(text);
  const url = buildUrl(result && result.slug, text);
  chrome.tabs.create({ url });
});

chrome.action.onClicked.addListener(() => {
  chrome.tabs.create({ url: 'https://toolhub.software' });
});
