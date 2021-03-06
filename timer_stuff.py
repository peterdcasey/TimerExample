"""
Peter Casey
"""

def test1():
    lst = []
    for i in range(1000):
        lst = lst + [i]
       
        
def test2():
    lst = []
    for i in range(1000):
        lst.append(i)
       
        
def test3():
    lst = [i for i in range(1000)]
    
    
def test4():
    lst = list(range(1000))


def test5():
    pass


# Import the Timer class defined in the module
from timeit import Timer
# If the above line is excluded, you need to replace Timer with
#   timeit.Timer when defining a Timer object

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

t5 = Timer("test5()", "from __main__ import test5")
print("list range ",t5.timeit(number=1000), "milliseconds")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
print("pop(0) pop()")

for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))
