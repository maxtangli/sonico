# csv

history
- 1972-, commercial computers
- [rfc4180(2005)](https://tools.ietf.org/html/rfc4180), .csv, text/csv
- [rfc7111(2014)](https://tools.ietf.org/html/rfc7111), text/csv fragment identifiers
- widely used

.csv
- newline: CRLF(also consider other implementations). last record may ignore.
- optional header: no reliable way to tell, should be indicated by user
- delimiter character: comma, (last record should not contain)
- quotation character: quotes""
- escape , by "", e.g. "go, go, go."
- escape " by "", e.g. "say: ""hello"". "
- (possibly not supported)escape newline by ""
- rfc4180 forbidden: leading and trailing spaces and tabs trimming
- rfc4180 forbidden: spaces outside quotes in a field
- rfc4180 forbidden: double quotes in unquoted fields

text/csv
- mime: text/csv
- optional charset: suggest default utf-8. 
- optional header: present|absent.

# csv coding

testcase
- utf8, utf8-bom, some locale encoding
- crlf, lf, extra end line
- invalid column count

# csv coding in ruby

file <-> array
~~~~
rows = CSV.read(file)
CSV.foreach(file) do |row|

CSV.open(file) do |csv| csv << row
~~~~

string <-> array
~~~~
rows = CSV.parse(s)
CSV.parse(s) do |row|

s = CSV.generate do |csv| csv << row

rows = s.parse_csv
s = rows.to_csv
~~~~
