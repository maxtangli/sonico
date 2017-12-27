# const expect = require('chai').expect;

reference
- http://chaijs.com/api/bdd/
- https://gist.github.com/yoavniran/1e3b0162e1545055429e

# ecmascript2017=es8

~~~~
async&await
Observables
console.log(obj)
~~~~

# ecmascript2016=es7

~~~~
base**exponent
Array.prototype.includes()
~~~~

# ecmascript6

http://es6-features.org/
~~~~
# constant
const PI = 3.141593

# block-scoping variable, function
for (let i = 0; i < a.length; i++) {
    let x = a[i]
    …
}

{
	function foo () { return 1 }
}

# closure by arrow function
[[1,2],[3,4],[5,6]].map((x,y)=>x+y)
[1,2,3].forEach(v=>{if(v>1) console.log(v)})

# module
export function sum (x, y) { return x + y }
import * as math from "lib/math"

# class
class Shape {
    constructor (id, x, y) {
        this.id = id
        this.move(x, y)
    }
    move (x, y) {
        this.x = x
        this.y = y
    }
	
	toString () {
        return `Shape(${this.id})`
    }
}
class Circle extends Shape {
    constructor (id, x, y, radius) {
        super(id, x, y)
        this.radius = radius
    }
	toString () {
        return "Circle > " + super.toString()
    }
}

# promise
function fetchAsync (url, timeout, onData, onError) {
    …
}
let fetchPromised = (url, timeout) => {
    return new Promise((resolve, reject) => {
        fetchAsync(url, timeout, resolve, reject)
    })
}
Promise.all([
    fetchPromised("http://backend/foo.txt", 500),
    fetchPromised("http://backend/bar.txt", 500),
    fetchPromised("http://backend/baz.txt", 500)
]).then((data) => {
    let [ foo, bar, baz ] = data
    console.log(`success: foo=${foo} bar=${bar} baz=${baz}`)
}, (err) => {
    console.log(`error: ${err}`)
})
~~~~

# Object

~~~~
o = {k1:v1, k2:v2}

o.k1, o[k1]
o.k3 === undefined

for (name in obj)
entries, keys, values

freeze
~~~~

# Array 

~~~~
// create
a = [0,1]
Array.from(obj|string|map|set, mapFn, thisArg)
Array.of(...elements)

// property
Array.isArray
a[0]
indexOf,lastIndexOf

// modify order
reverse, sort

// modify one element
push, pop, unshift, shift

// modify overall
a.length = 0
fill

// return new
concat, join, slice

// iteration
entries, keys, values
find, findIndex
map, filter, reduce, reduceRight, forEach
every, any
~~~~

# Map

~~~~
new Map([iterable])
new Map([[k1,v1],[k2,v2]])

entries, keys, values, size
has, get, set, delete, clear
for(var [key, value] of map)
foreach
~~~~

# Iteration Protocols

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols

# grammar

type
- number: internally float.
- falsy： false, null, undefined, ' ', 0, NaN.

function
- return: undefined by default, this if new.
- function scope