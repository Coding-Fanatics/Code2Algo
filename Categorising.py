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
    IndRegx = re.findall("^ +", l)
    ElseRegx = re.findall("^else", l)
    if CoRegx:
        # print("Condition: ", CoRegx)
        return 0
    elif LoRegx:
        # print("Loop: ", LoRegx)
        return 1    
    elif FnRegx:
        # print(i, " --------------- ")
        # print("Funciton: ", FnRegx)
        return 2
    elif OpRegx:
        # print("Operational: ", OpRegx)
        return 3
    elif IndRegx:
        return 4 
    elif ElseRegx:
        return 5       

def conditionTranslator(i):
    if_elif_else = re.findall("if|elif|else", lines[i])
    try:
        op1 = lines[i].split(if_elif_else[0])
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
    except:
        print("Error", i)    
    # op1 = op1[1]
    # op1 = op1.split(">")
    # op1 = " greater than ".join(op1)
    # op1 = op1.split("<")
    # op1 = " less than ".join(op1)
    # op1 = op1.split("<=")
    # op1 = " less than or equal to ".join(op1)
    # op1 = op1.split(">=")
    # op1 = " greater than or equal to ".join(op1)
    # op1 = op1.split("!=")
    # op1 = " not equal to ".join(op1)
    # op1 = op1.split("==")
    # op1 = " equal to ".join(op1)  
    # op1 = op1.split(":")
    # op1 = op1[0]
    # return op1


def controller(type, i):
    if type == 3:
        op(i)
        return 1
    elif type == 0:
        j = i
        while((type == 4 or type != 5)and j<len(lines)):
            type = Tokeniser(lines[j])
            j+=1
        co(i, j)    
        return j-i
    elif type == 2:
        fn(i)
    elif type == 1:
        pass

    return 1    

    


class line:
    def conditions(self):
        pass

def fn(i):
    print(str(i)+". "+lines[i])

def op(i):                              # Prints the Operational Statements
    print(str(i)+". "+ lines[i])

def co(i1, i2):
    if_elif_else = re.findall("if|elif|else", lines[i])
    op1 = conditionTranslator(i)
    if(if_elif_else[0] != "else"):
        print(str(i)+". " + if_elif_else[0] + " " + op1 + " goto step-" + str(i1+1) + " else goto step-" + str(i2))
    else:
        print(str(i)+". " + if_elif_else[0] + " " + op1 + " goto step-" + str(i1+1))            
    


def Checker(i=0):                        # Checker Goes line by line checking and sending line to tokensier
    type = Tokeniser(lines[i]) 
    n = controller(type, i)
    return n
    

lines = code.split('\n')
i=0
while(i<len(lines)):
    n = Checker(i)
    i+=1









# keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# functions = []