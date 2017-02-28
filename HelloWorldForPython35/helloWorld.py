print("Hello world!")
print("Hello world again!")
the_world_is_flat = 1
if the_world_is_flat:
    print("Be careful not to fall off!")
# this is the first comment
SPAM = 1  # and this is the second comment
# ... and now a third!
STRING = "# This is not a comment."
print(2 + 2)
hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
Note that whitespace at the beginning of the line is\n\
significant."
print(hello)
a = ['spam', 'eggs', 100, 1234]
print(a)
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
i = 256 * 256
print('The value of i is', i)
a, b = 0, 1
while b < 100:
    print(b, ',')
    a, b = b, a + b
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
 print(i, a[i])

def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b

fib(2000)

class MyEmptyClass:
    pass
print()
f = fib
f(100)

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) # see below
        a, b = b, a+b
        return result
    
f100 = fib2(100) # call it
print(f100)

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))