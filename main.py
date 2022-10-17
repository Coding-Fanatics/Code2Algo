import re
from Compiler import AlgoCompiler

code = '''print("1932 is worse")
a=5+3
b = 5+3
c = a*b
list(c)
set(a)
while c > d:
    a = 33+45
    b =  a+v
    while a == b:
        d = a+3
    c = 3
for i in range(1,10,2):
    a = 3
    d = 34+7
for each_word in lambda:
    for each in each_word:
        print("Ansah is my Name")
        a = ansah
    k = 5 + 2
    a = 6*7
d = 97''' 

#initializing the compiler

model = AlgoCompiler(code)

#compiling the code :

model.compile()

#getting the output from the compiler

algorithm = model.returnOut()
print(algorithm)

#o r we can directly use model.printOut()