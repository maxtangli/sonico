# haskell

0. hello 0.2h //sudo yum install haskell-platform --enablerepo=epel
1. tutorial 0.4h 

# note: basics

5+7
"chris"
sort [42,13,22]
sort "chris"  
fst (28, "chris")
let x = 4 in x * x // let var = expression in body 

'a' : 'b' : [] == ['a','b'] // : means concat
['a','b','c'] == "abc" // "" means a list of characters

map (+1) [1..5]
filter (>5) [62,3,25,7,1,9]
let take5s = filter (==5) in map take5s [[1,5],[5],[1,1]] // custom function
toUpper 'a'

let (a:b:c:[]) = "xyz" in a
let (a:_) = "xyz" in a
let (_,a:_) = (10,"abc") in a 