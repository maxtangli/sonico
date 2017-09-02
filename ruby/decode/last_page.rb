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
$plain_text="*iszerothblockPicktwentytwogreenboxesOrdinalshavenodivisorsEachpairmeansxandynumn"
$ordinals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

puts $grid.split('').values_at(*$ordinals[0..21]).each_slice(2)
         .map {|x, y| $plain_text.cell(x, y)}.join