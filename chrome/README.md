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
- background: evemt pages=high performance single long-running script.
- commands: hotkeys.
- content_scripts: run in context of web pages.
- devtools_page: customize devtool.

# calendar

https://www.googleapis.com/calendar/v3/calendars/tantanmen255%40gmail.com/events?orderBy=startTime&singleEvents=true&timeMax=2018-02-01T00%3A00%3A00-09%3A00&timeMin=2018-01-01T00%3A00%3A00-09%3A00&fields=items(end%2Cstart%2Csummary)&key=AIzaSyCvSRZ3M0wPB3BnIDUccTAtC9E_UmmFAbM