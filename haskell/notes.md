# reference

A Gentle Introduction to Haskell: https://www.haskell.org/tutorial

# thinking in haskell(my ideas)

- in philosophy view, the origin of the world is  actually function!

# bulit-in types

~~~~
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
~~~~
		  
# user-defined types

~~~~
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
~~~~

# list

~~~~
[] [1..10] [1,3..10] [1,3..]
'a':('b':[]) == ['a', 'b'] == "ab" // : means concat, string is also list
[(a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2] // list comprehension
~~~~

# function

~~~~
// define function: (add e1) e2
add :: Integer -> Integer -> Integer
add x y = x + y

add (x,y) = x + y
inc = add 1
map (add 1) [1,2,3] => [2,3,4]

// lambda
inc = \x -> x+1
add = \x y -> x+y

// section
inc = (+ 1)
add = (+)

// non-terminating expression: _|_ (read "bottom")
bot = bot
v = 1/0

// strict function: fails to terminate when applied to a nonterminating expression

// non-strict function
const1 x = 1
csont 1 bot = 1
const1 (1/0) = 1

// infinite
numsFrom n = n : numsFrom (n+1)
squares = map (^2) (numsfrom 0)
take 5 squares

fib = 1 : 1 : [ a+b | (a,b) <- zip fib (tail fib) ]

~~~~

# built-in functions

~~~~
// infix operation, fixity declarations
(++) :: [a] -> [a] -> [a]
[] ++ ys =  ys
(x:xs) ++ ys =  x : (xs++ys)

(.) :: (b->c) -> (a->b) -> (a->c)
f . g = \ x -> f (g x)

infixr 5 ++
infixr 9 .

// section, the partial application of an infix operator
(x+) = \y -> x+y
(+y) = \x -> x+y
(+)	= \x y -> x+y

// error
error :: String -> a
head [] = error "head{PreludeList}: head []"

// list operation
map :: (a -> b) -> [a] -> [b]
map f xs = [f x | x <- xs]

filter :: (a -> b) -> [a] -> [b]
filter f xs = [x | x <- xs, f x]

length :: [a] -> Integer
length [] =  0
length (x:xs) = 1 + length xs

head :: [a] -> a
head (x:xs) =  x

tail :: [a] -> [a]
tail (x:xs) =  xs

zip :: [a] -> [a] -> [a]
zip (x:xs) (y:ys)       = (x,y) : zip xs ys
zip  xs     ys          = []
~~~~

# ghci

~~~~
:l filename // load
:t value // type
~~~~

# let

~~~~
let x = 4 in x * x // let var = expression in body

let take5s = filter (==5) in map take5s [[1,5],[5],[1,1]] // custom function

let (a:b:c:[]) = "xyz" in a
let (a:_) = "xyz" in a
let (_,a:_) = (10,"abc") in a
~~~~
