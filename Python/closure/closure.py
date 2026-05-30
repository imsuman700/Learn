import os

def say_hello():
    print(f"Hello")
    

def shl():
    sh=say_hello
    print(f"sh:[{sh}]")
    sh()

########
# A closure is:
#A function that remembers variables from its enclosing scope even after that scope has finished executing.
def outer():
    message="Hello"
    def inner():
        print(f"Inner function, message:[{message}]")
    print(f"In outer, inner:[{inner}]")
    return inner

def tst_fn():
    innr=outer()
    print(f"innr:[{innr}]")
    innr()

if __name__ == "__main__":
    print(f"Called via main()")
    tst_fn()