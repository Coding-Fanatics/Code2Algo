import re

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



def Tokeniser(l):
    OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
    FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
    CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
    LoRegx = re.findall("^for+.*:$|^while+.*:$", l)
    # IndRegx = re.findall("^ +")
    if CoRegx:
        # print("Condition: ", CoRegx)
        return 0
    elif LoRegx:
        # print("Loop: ", LoRegx)
        return 1    
    elif FnRegx:
        print("Funciton: ", FnRegx)
        return 2
    elif OpRegx:
        # print("Operational: ", OpRegx)
        return 3
    # elif IndRegx:
    #     return 4    

def opTranslator(i):
    if_or_elif = re.findall("if|elif", lines[i])
    op1 = lines[i].split(if_or_elif[0])
    op1 = op1[1]
    op1 = op1.split(">")
    op1 = " greater than ".join(op1)
    op1 = op1.split("<")
    op1 = " less than ".join(op1)
    op1 = op1.split("<=")
    op1 = " less than or equal to ".join(op1)
    op1 = op1.split(">=")
    op1 = " greater than or equal to ".join(op1)
    op1 = op1.split("!=")
    op1 = " not equal to ".join(op1)
    op1 = op1.split("==")
    op1 = " equal to ".join(op1)  
    op1 = op1.split(":")
    op1 = op1[0]
    return op1


def controller(type, i):
    if type == 3:
        op(i)
        return 1
    elif type == 0:
        Checker(i+1)
        if_or_elif = re.findall("if|elif", lines[i])

        op1 = opTranslator(i)
        print(str(i)+". " + if_or_elif[0] + " " + op1 + " goto step " + "__" + "else" + "__")
        Checker(i+1)
        return 1

    pass


class line:
    def conditions(self):
        pass

def op(i):
    print(str(i)+". "+ lines[i])

lines = code.split('\n')

def Checker(i=0):
    while(i<len(lines)):
        type = Tokeniser(lines[i]) 
        controller(type, i)
        i +=1

Checker()









# keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# functions = []