puts %q{"stop", she said, "I can't live without 's and "s. "}
"a\nb\nc".each_line {|c| puts c}

a = :all
b = :all
puts [a==b, a===b, a.eql?(b), a.equal?(b)].join(',')
a = "all"
b = "all"
puts [a==b, a===b, a.eql?(b), a.equal?(b)].join(',')