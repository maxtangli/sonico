# todo

install
- [x] setup: hello 0.2h
- [x] setup: dockerize nodejs 1h

language
- [x] ecmascript6 0.5h

Node.js in Action.Mike Cantelon etc.2012.pdf
- know more

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

# nodejs

web history
- static page
- form-driven application e.g. 1996 hotmail
- ajax-drive application e.g. 2004 gmail, 2005 google map
- real-time application e.g. 2006 twitter
- ?

nodejs
- node: minimalist server-side JavaScript TCP/IP framework.
- impl: google's v8 javascript engine, libev, libeio.
- pros: fast, scalable, accessible.

features
- asynchronous io
- event driven
- single thread
- cross platform

usecase
- io intensive application
- cpu intensive application by cpp, child_process
- legacy system intergration
- distributed application
- online game