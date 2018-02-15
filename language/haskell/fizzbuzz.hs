fizzbuzz :: Integer -> [String]
fizzbuzz n = map f [1..n]

f :: Integer -> String
f n | n `mod` 15 == 0 = "fizzbuzz"
    | n `mod` 3 == 0 = "fizz"
    | n `mod` 5 == 0 = "buzz"
    | otherwise = show n
