# if true
#   puts 'hello'
# end
puts 'hello1' if true

# if not false
#   puts 'hello'
# end
# unless false
#   puts 'hello'
# end
puts 'hello2' unless false

i = 0
# while (i+=1) <= 1
#   puts 'hello'
# end
puts 'hello3' while (i+=1) <= 1

i = 0
# while (i+=1) != 2
#   puts 'hello'
# end
# until (i+=1) == 2
#   puts 'hello'
# end
puts 'hello4' until (i+=1) == 2

j = case i
      when 0 then
        0
      when 1 then
        1
      when 2 then
        'hello5'
      else
        nil
    end
puts j

puts 'hello6' unless nil # ruby treats only 'false' and 'nil' as false

k = false # pitfalls
k ||= 'hello7'
puts k
