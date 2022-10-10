import re

def Tokeniser(l):
    OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
    FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
    CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
    LoRegx = re.findall("^for+.*:$|^while+.*:$", l)
    if CoRegx:
        print("Condition: ", CoRegx)
    elif LoRegx:
        print("Loop: ", LoRegx)    
    elif FnRegx:
        print("Funciton: ", FnRegx)
    elif OpRegx:
        print("Operational: ", OpRegx)

code = '''
a=5+3
b = 5+3
c = a*b
print("if(a>b):")
if(a>b):
    print("Hello")
elif a==b:
    print("yes")    
else:
    print()  
for i in range(10):
    print('a')      
'''


lines = code.split('\n')
for l in lines:
    Tokeniser(l) 

# keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# functions = []