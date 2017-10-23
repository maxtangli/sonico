-- a dp solution by L.W.
f :: Int -> Int -> Int
f n 0 = 1
f n m | m < 0 = 0
f 0 m = 0
f n m = sum [f (n-1) (m-x) | x <- [0..4]]

main = print $ sum [ f 9 x | x <- [1..14]]
