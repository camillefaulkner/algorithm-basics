Recursion

- recursion is when a function calls itself
function f() {
    ...
    f()
}

- recursive functions need to have a breaking condition
- this prevents infinite loops and eventual crashes
- each time the function is called, the old arguments are saved
- this is called the "call stack"

function countdown(x) {
    if (x == 0)
        print("done!")
        return
    else 
        print(x, "...")
        countdown(x-1)
}
countdown(4)