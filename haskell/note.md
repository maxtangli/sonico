# reference

A Gentle Introduction to Haskell: https://www.haskell.org/tutorial

# types

5  :: Integer
'a' :: Char
inc :: Integer -> Integer
[1,2,3] :: [Integer]
('b',4) :: (Char,Integer)

data Integer =       ... -2 | -1 | 0 | 1 | 2 ...
data Char = Ca | Cb | Cc | ...
		  | CA | CB | CC | ...
		  | C1 | C2 | C3 | ...
		  ...
data [a] = [] | a : [a] 
data (a,b) = (a,b)
data (a,b,c) = (a,b,c)
...
type String = [Char]
		  
# user-defined types

// data constructors
data Bool = False | True // nullary data constructors
data Point a = Pt a a
data Point a = Point a a

// recursive types
data Tree a = Leaf a | Branch (Tree a) (Tree a)

// recursive functions for recursive types
fringe :: Tree a -> [a]
fringe (Leaf x) = [x]
fringe (Branch left right) =  fringe left ++ fringe right

// type synonyms
type AssocList a b = [(a,b)]

# list

[] [1..10] [1,3..10] [1,3..]
'a':('b':[]) == ['a', 'b'] == "ab" // : means concat, string is also list
[(a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2] // list comprehension
