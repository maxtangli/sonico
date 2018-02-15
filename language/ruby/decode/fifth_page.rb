require './utility.rb'

# https://www.guballa.de/vigenere-solver
$plain_text="*iszerothblockPicktwentytwogreenboxesOrdinalshavenodivisorsEachpairmeansxandynumn"
KEY = 9

if __FILE__ == $0
  puts $plain_text.to_grid
  puts
  puts "step3 answer: #{$plain_text[KEY*2, KEY]}"
end