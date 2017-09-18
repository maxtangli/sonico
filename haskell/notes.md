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

// section: partially applied infix function
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

# patterns

~~~~
// as-pattern to duplicate first value
f s@(x:xs) = x:s

// wild-card
head (x:_)             = x
tail (_:xs)            = xs

// guard
sign x | x > 0 = 1
       | x == 0 = 0
       | otherwise = -1

// case
take m ys = case (m,ys) of
              (0,_)       ->  []
              (_,[])      ->  []
              (n,x:xs)    ->  x : take (n-1) xs	   

// let
let take5s = filter (==5) in take5s [1..10]

// where
f x y  |  y>z           =  ...
       |  y==z          =  ...
       |  y<z           =  ...
     where z = x*x

// layout: haskell use column!
~~~~

# overloading

~~~~
// declartion
class Eq a where 
  (==) :: a -> a -> Bool

// implementation  
instance Eq Integer where 
  x == y =  x `integerEq` y
instance Eq Float where
  x == y =  x `floatEq` y
instance (Eq a) => Eq (Tree a) where 
  Leaf a         == Leaf b          =  a == b
  (Branch l1 r1) == (Branch l2 r2)  =  (l1==l2) && (r1==r2)
  _              == _               =  False  
  
// class extension
class  (Eq a) => Ord a  where
  (<), (<=), (>=), (>)  :: a -> a -> Bool
  max, min              :: a -> a -> a  
~~~~

# io

~~~~
getChar :: IO Char
putChar :: Char -> IO ()

// bind operator: >>=
// bind syntactic sugar: do

return  :: a -> IO a

getLine :: IO String
getLine =  do c <- getChar
			  if c == '\n'
				   then return ""
				   else do l <- getLine
						   return (c:l)

main :: IO ()
main =  do c <- getChar
           putChar c
		   return (c == 'y')
		   
todoList :: [IO ()]
todoList = [putChar 'a',
            do putChar 'b'
               putChar 'c',
            do c <- getChar
               putChar c] 
			   
sequence_        :: [IO ()] -> IO ()
sequence_ []     =  return ()
sequence_ (a:as) =  do a
                       sequence as
					   
sequence_ :: [IO ()] -> IO ()
sequence_ =  foldr (>>) (return ())

putStr :: String -> IO ()
putStr s =  sequence_ (map putChar s)

isEOFError :: IOError -> Bool
catch :: IO a -> (IOError -> IO a) -> IO a

getChar' :: IO Char
// getChar' =  getChar `catch` (\e -> return '\n')
getChar' =  getChar `catch` eofHandler where
    eofHandler e = if isEofError e then return '\n' else ioError e
	
getLine' :: IO String
getLine' = catch getLine'' (\err -> return ("Error: " ++ show err))
        where
                   getLine'' = do c <- getChar'
 	                       if c == '\n' then return ""
                                            else do l <- getLine'
                                                    return (c:l)													
~~~~

# fmap

~~~~
// fmap: ???  
// http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html
class Functor f where
  fmap :: (a -> b) -> f a -> f b  

instance Functor [] where
    fmap = map

instance Functor ((->) r) where
    fmap f g = f . g	  
  
instance Functor Tree where
  fmap f (Leaf x)       = Leaf   (f x)
  fmap f (Branch t1 t2) = Branch (fmap f t1) (fmap f t2)  
~~~~
  
# monad

~~~~
// used in: do, io etc.
// monadic classes: Functor, Monad, MonadPlus, [], Maybe
infixl 1 >>, >>=
class Monad m where
    (>>=) :: m a -> (a -> m b) -> m b
    (>>) :: m a -> m b -> m b
    return :: a -> m a
    fail :: String -> m a

    m >> k =  m >>= \_ -> k

do e1 ; e2 = e1 >> e2
do p <- e1; e2 = e1 >>= \p -> e2

// https://stackoverflow.com/questions/44965/what-is-a-monad
// monad chains operations in some specific, useful way
[x*2 | x<-[1..10], odd x]

do
   x <- [1..10]
   if odd x 
       then [x * 2] 
       else []

[1..10] >>= (\x -> if odd x then [x*2] else [])

do
   putStrLn "What is your name?"
   name <- getLine
   putStrLn ("Welcome, " ++ name ++ "!")
   
putStrLn "What is your name?"
>>= (\_ -> getLine)
>>= (\name -> putStrLn ("Welcome, " ++ name ++ "!"))   
~~~~
	
# ghci

~~~~
:l filename // load
:t value // type
~~~~
