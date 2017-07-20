# https://ruby-doc.org/core-2.4.0/Regexp.html
puts /[0-9]/.match("ab9d8")
puts %r{[0-9]}.match("ab9d8") # first matched MatchData or nil
puts /[0-9]/ =~ "ab9d8" # first matched index or nil
puts /[^0-9]/.match("1ab9d8") # inverted
puts /[a-w&&[^c-g]z]/.match("zcb") # ([a-w] AND ([^c-g] OR z)) -> /[abh-w]/
puts /\w+/.match("123") # any word
puts /[[:alnum:]]+/.match("a1") # POSIX bracket expressions
puts /[0-9]{2,}/.match("1a234b") # repetition, greedy by default
puts /[0-9]{2,}?/.match("1a234b") # +? -> lazy

# http://www.regular-expressions.info/recurse.html
puts /a\g<0>?z/.match("aaazzz") # recursive regex
puts /\((?>[^()]|\g<0>?)*\)/.match("(aaa(bbb)c(dd))e") # recursive parentheses with content


