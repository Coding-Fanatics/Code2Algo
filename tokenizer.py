import re

global algorithm
global f_index
algorithm = ""
f_index = 1

def Tokeniser(l):
    OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
    FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
    CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
    LoRegx = re.findall("^for+.*:$|^while+.*:$", l)
    if CoRegx:
        # print("Condition: ", CoRegx)
        return 0
    elif LoRegx:
        # print("Loop: ", LoRegx)    
        return 1
    elif FnRegx:
        # print("Funciton: ", FnRegx)
        return 2
    elif OpRegx:
        # print("Operational: ", OpRegx)
        return 3



code = '''
a=5+3
b = 5+3
c = a*b
while c > d:
    a = 33+45
    b =  a+v

d = 97    
'''
lines = code.split('\n')

def level(i):
    level = 0
    for eachLett in lines[i]:
        if eachLett == ' ':
            level += 1
        else:
            break
    
    return level

def writer(compiled_):
    global algorithm
    global f_index
    algorithm += str(f_index)
    algorithm += ". {}".format(compiled_)
    algorithm += "\n"
    f_index += 1

def loopsParser(i):
    initialLevel = level(i)
    start_step = i
    temp_line = i+1
    next_step = temp_line
    while(level(temp_line) != initialLevel and i<len(lines)):
        temp_line += 1

    next_step = temp_line-1

    whileReg = re.findall("^while", lines[i])
    if whileReg:
        condition_ = lines[i][5:]
        fin = "repeat step {} to {} while {}".format(start_step+1,next_step,condition_)
        writer(fin)

for i in range(len(lines)):
    a = Tokeniser(lines[i]) 
    if a == 3:
        writer(lines[i])
    elif a==1:
        loopsParser(i)


# keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# functions = []

#def contrller(type,i)



print(algorithm)