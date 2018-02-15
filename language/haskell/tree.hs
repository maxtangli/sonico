data Tree a = Leaf a | Branch (Tree a) (Tree a)

fringe :: Tree a -> [a]
fringe (Leaf x) = [x]
fringe (Branch left right) =  fringe left ++ fringe right
-- fringe (Branch (Leaf 1) (Branch (Leaf 2) (Branch (Leaf 3) (Leaf 4))))
