# Code2Algo
Code to algorithm
This is a compiler which converts Python code into an Algorithm.

This Compiler helps in distribution of Codes written in Python for non-Python programmers.

## Tutorial
```python

# example code
code = """a = 3 > 4
a=5+3
b = 5+3
def printHi(name):
    print("Hi "+name)
    a = 34+2
c = a*b
list(c)
set(a)
if a > 2:
    print("Hello")
elif a < 2:
    print("Hih")
    if a == 2:
        print(2)
    else:
        e = 3    
else:
    s = 2 
if 2<5:
    s = s+1               
while c > d:
    a = 33+45
    b =  a+v
    while a == b:
        d = a+3
    c = 3
def factorial(n):
    if n==1:
        a = 4
    x = n*n-1
for i in range(1,10,1):
    a = 3
    d = 34+7
for each_word in lambda:
    for each in each_word:
        print("Ansah is my Name")
        a = ansah
    k = 5 + 2
    a = 6*7
d = 97"""

model = AlgoCompiler(code)
model.compile()
algorithm = model.returnOut()
print(algorithm)
```