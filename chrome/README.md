# chrome

chrome development for fun.

# extension

flow
- extension: 1 manifest, >=1 html, optional js, optional images etc.
- debug: extensions -> developer mode.
- release: .crx package -> Chrome Developer Dashboard -> Chrome Web Store.

manifest
- browserAction: put icon in toolbar.
- pageAction: put icon in toolbar, appear grayed out when inactive.
- commands: hotkeys.
- devtools_page: customize devtool.

permission
- tabs: chrome.tabs.url, chrome.tabs.title, chrome.tabs.favIconUrl.
- activeTab: currently active tab, e.g. tabs.executeScript, tabs.Tab.

# event pages

features
- high performance single long-running script.
- load: installed, event came, message came, other view call runtime.getBackgroundPage.
- unload: all visible views and all message ports closed.
- idle handling: idle trigger runtime.onSuspend event, other event trigger runtime.onSuspendCanceled event.

manifest: background
~~~~
  "background": {
    "scripts": ["eventPage.js"],
    "persistent": false
  },
~~~~

best practice
- runtime.onInstalled event for one-time-only init.
- register event listeners each time loaded. also consider event filters.
- runtime.onSuspend event for cleanup. close unused message ports.
- to keep state in browser session, use storage API.
- test reload case.

# content scripts

features
- run in context of web pages.
- can access page DOM.
- can refer extension files
~~~~
var imgURL = chrome.extension.getURL("images/myimage.png");
document.getElementById("someImage").src = imgURL;
~~~~
- cannot use external variables e.g. those defiend by page, other content pages, extension's pages.
- cannot use chrome.* APIs except extension, i18n, runtime, storage. to request, use sendMessage or ajax.

manifest: content_scripts 
- matches, exclude_matches, match_about_blank, include_globs, exclude_globs
~~~~
  "permissions": [
    "tabs", "http://www.google.com/*"
  ],
~~~~
- css, js
- run_at, all_frames

programmatic creatation of content script
~~~~
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.executeScript({
    code: 'document.body.style.backgroundColor="red"'
  });
});

chrome.tabs.executeScript(null, {file: "content_script.js"});

"permissions": [
  "activeTab"
],
~~~~

page -> content script
~~~~
var port = chrome.runtime.connect();

window.addEventListener("message", function(event) {
  // We only accept messages from ourselves
  if (event.source != window)
    return;

  if (event.data.type && (event.data.type == "FROM_PAGE")) {
    console.log("Content script received: " + event.data.text);
    port.postMessage(event.data.text);
  }
}, false);

document.getElementById("theButton").addEventListener("click",
    function() {
  window.postMessage({ type: "FROM_PAGE", text: "Hello from the webpage!" }, "*");
}, false);
~~~~ 

# calendar

https://www.googleapis.com/calendar/v3/calendars/tantanmen255%40gmail.com/events?orderBy=startTime&singleEvents=true&timeMax=2018-02-01T00%3A00%3A00-09%3A00&timeMin=2018-01-01T00%3A00%3A00-09%3A00&fields=items(end%2Cstart%2Csummary)&key=AIzaSyCvSRZ3M0wPB3BnIDUccTAtC9E_UmmFAbM