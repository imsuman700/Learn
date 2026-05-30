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
    namaskar="Namaskar"
    def inner():
        print(f"Inner function, message:[{message}]")
        print(f"namaskar:[{namaskar}]")
    #print(f"In outer, inner:[{inner}]")
    return inner

def tst_fn():
    innr=outer()
    #print(f"innr:[{innr}]")
    #innr()
    print(f"{innr.__closure__}")
    print(f"{innr.__closure__[0].cell_contents}")

#Real-world Example: Multipliers
def make_multiplier(n):
    def multipy(m):
        return m*n
    return multipy

def test_fun():
    double=make_multiplier(2)
    triple=make_multiplier(3)
    
    double_5=double(5)
    triple_10=triple(10)
    
    print(f"double_5:[{double_5}], triple_10:[{triple_10}]")

def outer2():
    count=0
    acb="A" #Unless we use this variable inside inner2, it won't be considered in closure scope.
    def inner2():   
        nonlocal count
        count +=1
        return count
    return inner2

def ct():   #ct-> closure test
    inr2=outer2()
    print(f"inr2:[{inr2.__closure__}]")
    print(inr2())
    print(inr2())
    print(inr2())   #The closure remembers the updated value.
    

if __name__ == "__main__":
    print(f"Called via main()")
    #tst_fn()
    #test_fun()
    ct()