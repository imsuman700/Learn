Closures are one of those Python concepts that seem confusing at first, but once you understand them, they become a powerful tool for writing elegant code.

Let's go from **zero → hero**.

---

# 1. First, understand functions as objects

In Python, functions are objects.

```python
def greet():
    print("Hello")

print(greet)
```

Output:

```python
<function greet at 0x...>
```

You can assign a function to a variable:

```python
def greet():
    print("Hello")

say_hello = greet

say_hello()
```

Output:

```python
Hello
```

So functions can be:

* Assigned to variables
* Passed as arguments
* Returned from other functions

This is the foundation of closures.

---

# 2. Functions can return functions

Example:

```python
def outer():
    def inner():
        print("I am inner")

    return inner

my_func = outer()

my_func()
```

Output:

```python
I am inner
```

What happened?

```text
outer()
   |
   └── creates inner()
   |
   └── returns inner
```

So now:

```python
my_func
```

points to `inner`.

---

# 3. Accessing outer variables

Now let's make it interesting.

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

my_func = outer()

my_func()
```

Output:

```python
Hello
```

Question:

> outer() already finished. Why does inner() still know message?

This is where closures begin.

---

# 4. What is a Closure?

A **closure** is:

> A function that remembers variables from its enclosing scope even after that scope has finished executing.

Example:

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

my_func = outer()
```

At this point:

```python
outer()
```

has already ended.

Normally local variables disappear:

```python
message = "Hello"
```

should be destroyed.

But Python notices that `inner()` still needs it.

So Python stores it.

```text
inner()
   |
   └── remembers message="Hello"
```

That memory is the closure.

---

# 5. Visualize it

When you run:

```python
my_func = outer()
```

Python internally creates something like:

```text
my_func
   |
   +-- function: inner
   |
   +-- closure:
          message = "Hello"
```

Even though `outer()` is gone.

---

# 6. Example: Custom Greeting Generator

```python
def make_greeter(name):

    def greet():
        print(f"Hello {name}")

    return greet
```

Create two functions:

```python
john_greet = make_greeter("John")
alice_greet = make_greeter("Alice")
```

Now:

```python
john_greet()
```

Output:

```python
Hello John
```

And:

```python
alice_greet()
```

Output:

```python
Hello Alice
```

Each function remembers its own value.

```text
john_greet  -> name="John"

alice_greet -> name="Alice"
```

That's closure magic.

---

# 7. Real-world Example: Multipliers

```python
def make_multiplier(n):

    def multiply(x):
        return x * n

    return multiply
```

Create functions:

```python
double = make_multiplier(2)
triple = make_multiplier(3)
```

Use them:

```python
print(double(10))
```

Output:

```python
20
```

```python
print(triple(10))
```

Output:

```python
30
```

Each function remembers its own `n`.

---

# 8. Inspecting the Closure

Python lets you see closure variables.

```python
def outer():
    x = 100

    def inner():
        print(x)

    return inner

func = outer()

print(func.__closure__)
```

Output:

```python
(<cell at 0x...>,)
```

See actual value:

```python
print(func.__closure__[0].cell_contents)
```

Output:

```python
100
```

---

# 9. Common Interview Question

What happens here?

```python
def outer():
    count = 0

    def inner():
        count += 1
        return count

    return inner
```

Error:

```python
UnboundLocalError
```

Why?

Because Python thinks:

```python
count += 1
```

means:

```python
count = count + 1
```

which creates a local variable.

---

# 10. Fix using nonlocal

```python
def outer():
    count = 0

    def inner():
        nonlocal count

        count += 1
        return count

    return inner
```

Now:

```python
counter = outer()

print(counter())
print(counter())
print(counter())
```

Output:

```python
1
2
3
```

The closure remembers the updated value.

---

# 11. Real-world Use Case: Function Factory

Instead of:

```python
def add5(x):
    return x + 5

def add10(x):
    return x + 10
```

Use:

```python
def make_adder(n):

    def add(x):
        return x + n

    return add
```

Create:

```python
add5 = make_adder(5)
add10 = make_adder(10)
```

---

# 12. Closures vs Classes

Closure version:

```python
def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Usage:

```python
c = counter()

print(c())
print(c())
```

Output:

```python
1
2
```

Class version:

```python
class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
```

Usage:

```python
c = Counter()

print(c.increment())
print(c.increment())
```

Same behavior.

Closures are like lightweight objects with hidden state.

---

# 13. Closures Power Decorators

Most decorators use closures.

```python
def logger(func):

    def wrapper():
        print("Calling function")
        func()

    return wrapper
```

Usage:

```python
@logger
def hello():
    print("Hello")
```

Internally:

```python
hello = logger(hello)
```

The `wrapper()` remembers `func`.

That's a closure.

Decorators are essentially a practical application of closures.

---

# 14. Closure Mental Model

Think of a closure as:

```text
Function
+
Remembered Variables
=
Closure
```

Example:

```python
double = make_multiplier(2)
```

Internally:

```text
double
|
+-- code: multiply(x)
|
+-- remembered:
       n = 2
```

Even after `make_multiplier()` is gone.

---

# 15. Hero-Level Summary

A closure occurs when:

1. An outer function defines a variable.
2. An inner function uses that variable.
3. The inner function is returned.
4. Python keeps the variable alive.

Example:

```python
def outer(x):

    def inner(y):
        return x + y

    return inner

add10 = outer(10)

print(add10(5))
```

Output:

```python
15
```

Here:

* `x = 10` is remembered
* `inner()` survives after `outer()` ends
* `inner + remembered x` = **closure**

Think of a closure as a **function carrying a backpack of remembered variables wherever it goes**. 🎒🐍

That's the key intuition that unlocks decorators, callbacks, function factories, and many advanced Python patterns.
