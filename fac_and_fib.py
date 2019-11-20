from math import factorial

def fac(n):
    return factorial(n)

def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# Test
print("fac(0)=%d" % fac(0))
print("fac(1)=%d" % fac(1))
print("fac(2)=%d" % fac(2))
print("fac(3)=%d" % fac(3))

print("fib(0)=%d" % fib(0))
print("fib(1)=%d" % fib(1))
print("fib(2)=%d" % fib(2))
print("fib(3)=%d" % fib(3))
