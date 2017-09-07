factorial :: Integer -> Integer
-- factorial n = product [1..n]

-- factorial 0 = 1
-- factorial n = n * factorial (n - 1)

factorial n
  | n == 0 = 1
  | otherwise = n * factorial (n - 1)
