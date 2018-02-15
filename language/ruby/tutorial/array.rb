# https://ruby-doc.org/core-2.4.0/Array.html

# new
puts [1, 1, 1].join(',')
puts Array.new(3, 1).join(',')
puts Array.new(3) {1}.join(',')
puts Array.new(3) {|i| i+1}.join(',')

# range
puts [0, 1, 2, 3][1, 3].join(',')
puts [0, 1, 2, 3][1..3].join(',')
puts [0, 1, 2, 3][1..-1].join(',')

# select
puts [0, 1, 2, 3].drop(1).join(',')
[1, 2, 3].each {|e| puts e}
puts [0, 1, 2, 3].reject {|e| e == 0}.join(',')
puts ([0, 1, 2, 3] & [1, 2, 3]).join(',')

# string
puts %w{sonico nanoha}.join(',')

# https://ruby-doc.org/core-2.4.0/Hash.html
puts ({1 => 1, 2 => 2})
puts ({'a' => 1, 'b' => 2})
puts ({a: 1, b: 2})
({'a' => 1, 'b' => 2}).each {|k, v| puts "#{k},#{v}"}