import re

global algorithm
global f_index
algorithm = ""
f_index = 1

def trim_spaces(st):
    trimmed = ""
    for i in range(len(st)):
        if st[i] == ' ':
            continue
        else:
            trimmed = st[i:]
            break
    return trimmed

def Tokeniser(l):
    OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
    FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]|^ +[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
    CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
    LoRegx = re.findall("^for+.*:$|^while+.*:$|^ +while+.*:$|^ +for+.*:$", l)
    if CoRegx:
        # print("Condition: ", CoRegx)
        return 0
    elif LoRegx:
        # print("Loop: ", LoRegx)    
        return 1
    elif FnRegx:
        # print("Function: ", FnRegx)
        return 2
    elif OpRegx:
        # print("Operational: ", OpRegx)
        return 3
    else:
        return -1



code = '''
print("1932 is worse")
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
for i in range(1,10,-56):
    a = 3
    d = 34+7
for each_word in lambda:
    for each in each_word:
        print("Ansah is my Name")
        a = ansah
    k = 5 + 2
    a = 6*7
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

def operatorParser(i):
    compiled_ = trim_spaces(lines[i])
    writer(compiled_)

def loopsParser(i):
    initialLevel = level(i)
    start_step = i
    temp_line = i+1
    next_step = temp_line
    while(level(temp_line) != initialLevel and temp_line<len(lines)):
        temp_line += 1

    next_step = temp_line-1

    whileReg = re.findall("^while|^ +while", lines[i])
    forReg = re.findall("^for|^ +for", lines[i])
    if start_step+1==next_step:
        fin = "repeat step {} ".format(next_step)
    else:
        fin = "repeat step {} to {} ".format(start_step+1,next_step)

    if whileReg:
        condition_ = trim_spaces(lines[i])[5:]
        fin += " while {}".format(condition_)
        writer(fin)
    elif forReg:
        variable = re.findall("^for .+ in|^ +for .+ in", lines[i])
        if variable:
            variable = trim_spaces(variable[0])[4:-3]

        rangeReg = re.findall("range(.+):$", lines[i])
        # print(variable)
        if rangeReg:
            range_ = rangeReg[0][1:-1]
            range_ = range_.split(",")
            if(len(range_)==1):
                fin += "for {}=0 to {}={} step 1".format(variable,variable,int(range_[0])-1)                
            elif(len(range_)==2):
                fin += "for {}={} to {}={} step 1".format(variable,(range_[0]),variable,int(range_[1])-1)
            elif(len(range_)==3):
                fin += "for {}={} to {}={} step {}".format(variable,(range_[0]),variable,int(range_[1])-1,range_[2])
            writer(fin)     
        else:
            forComprehension = re.findall("^for .+|^ +for .+",lines[i])[0][:-1]
            forComprehension = trim_spaces(forComprehension)
            fin += forComprehension
            writer(fin)

def functionParser(i):
    line = trim_spaces(lines[i])
    general_func = ['print','set','list','dictionary']
    functionName = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*|^ +[a-zA-Z_][a-zA-Z0-9_]*", line)[0]
    fin = functionName
    if functionName in general_func:
        functionContent = line[len(functionName)+1:-1]
        fin += " " + functionContent
    else:
        functionContent = line[len(functionName):]
        fin += " " + functionContent
    writer(fin)

#main function
for i in range(len(lines)):
    a = Tokeniser(lines[i])
    if a==1:
        loopsParser(i)
    elif a==2:
        functionParser(i)
    elif a == 3:
        operatorParser(i)

print(algorithm)