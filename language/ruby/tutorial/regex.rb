# https://ruby-doc.org/core-2.4.0/Regexp.html

puts /[0-9]/.match("ab9d8")
puts %r{[0-9]}.match("ab9d8") # first matched MatchData or nil
puts /[0-9]/ =~ "ab9d8" # first matched index or nil

puts /[^0-9]/.match("1ab9d8") # inverted
puts /[a-w&&[^c-g]z]/.match("zcb") # ([a-w] AND ([^c-g] OR z)) -> /[abh-w]/
puts /\w+/.match("123") # any word
puts /[[:alnum:]]+/.match("a1") # POSIX bracket expressions
puts /\p{Alnum}+/.match("a1") # character property

puts /[0-9]{2,}/.match("1a234b") # repetition, greedy by default
puts /[0-9]{2,}?/.match("1a234b") # lazy +?
puts /(0|1|2|3|4){2,}/.match("1a234b") # alternation |

puts /[csh](..) [csh]\1 in/.match("The cat sat in the hat") # capturing group ()
puts /[csh](?<suffix>..) [csh]\k<suffix> in/.match("The cat sat in the hat") # capturing named group (?<name>)
puts /[csh](?<suffix>..) [csh]\g<suffix> in/.match("The cat set in the hat")# subexpression calls(re-execute named group) \g<name>
puts /(?:[csh])(..) [csh]\1 in/.match("The cat sat in the hat") # non-capturing group (?:)
puts /"(?>.*)"/.match('"Quote"') # atomic grouping (?>)

# http://www.regular-expressions.info/recurse.html
puts /a\g<0>?z/.match("aaazzz") # recursive regex
puts /\((?>[^()]|\g<0>?)*\)/.match("(aaa(bbb)c(dd))e") # recursive parentheses with content