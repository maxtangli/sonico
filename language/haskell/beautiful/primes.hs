primes :: Integer -> [Integer]
primes n = filterPrime [2..n] 
  where filterPrime [] = []
	filterPrime (p:xs) =  p : filterPrime [x | x <- xs, x `mod` p /= 0]
