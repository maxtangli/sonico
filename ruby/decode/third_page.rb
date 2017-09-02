# third_page.rb
require './utility.rb'

$grid = <<EOT.delete("\n")
154286973
738914652
692537481
923758146
861423795
475691238
516349827
389172564
247865319
EOT

if __FILE__ == $0
  puts $grid.to_grid
  puts
  puts "step1 answer: #{$grid[0..8]}"
end