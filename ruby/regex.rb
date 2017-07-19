# //, 
# ~= .match

puts /[0-9]/.match("ab9d8") 
puts %r{[0-9]}.match("ab9d8") # first matched MatchData or nil
puts /[0-9]/ =~ "ab9d8" # first matched index or nil
