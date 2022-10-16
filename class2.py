import re

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
for i in range(1,10,-56):
    a = 3
    d = 34+7
for each_word in lambda:
    for each in each_word:
        print("Ansah is my Name")
        a = ansah
    k = 5 + 2
    a = 6*7
d = 97''' 

class AlgoCompiler():
    algorithm = ""
    f_index = 1
    lines = []

    def __init__(self,source):
        self.lines = source.split("\n")
    
    def Tokeniser(self,l):
        OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
        FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]|^ +[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
        CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
        LoRegx = re.findall("^for+.*:$|^while+.*:$|^ +while+.*:$|^ +for+.*:$", l)
        if CoRegx:
            return 0
        elif LoRegx:
            return 1
        elif FnRegx:
            return 2
        elif OpRegx:
            return 3
        else:
            return -1

    def trim_spaces(self,st):
        trimmed = ""
        for i in range(len(st)):
            if st[i] == ' ':
                continue
            else:
                trimmed = st[i:]
                break
        return trimmed

    def level(self,i):
        level = 0
        for eachLett in self.lines[i]:
            if eachLett == ' ':
                level += 1
            else:
                break
        
        return level 
    
    def writer(self,compiled_):
        self.algorithm += str(self.f_index)
        self.algorithm += ". "+str(compiled_)+"\n"
        self.f_index += 1
    
    def operatorParser(self,i):
        compiled_ = self.trim_spaces(self.lines[i])
        self.writer(compiled_)

    def loopsParser(self,i):
        initialLevel = self.level(i)
        start_step = i
        temp_line = i+1
        next_step = temp_line
        while(self.level(temp_line) != initialLevel and temp_line<len(self.lines)):
            temp_line += 1

        next_step = temp_line-1

        whileReg = re.findall("^while|^ +while", self.lines[i])
        forReg = re.findall("^for|^ +for", self.lines[i])
        if start_step+1==next_step:
            fin = "repeat step {} ".format(next_step)
        else:
            fin = "repeat step {} to {} ".format(start_step+1,next_step)

        if whileReg:
            condition_ = self.trim_spaces(self.lines[i])[5:]
            fin += " while {}".format(condition_)
            self.writer(fin)
        elif forReg:
            variable = re.findall("^for .+ in|^ +for .+ in", self.lines[i])
            if variable:
                variable = self.trim_spaces(variable[0])[4:-3]

            rangeReg = re.findall("range(.+):$", self.lines[i])
            
            if rangeReg:
                range_ = rangeReg[0][1:-1]
                range_ = range_.split(",")
                if(len(range_)==1):
                    fin += "for {}=0 to {}={} step 1".format(variable,variable,int(range_[0])-1)                
                elif(len(range_)==2):
                    fin += "for {}={} to {}={} step 1".format(variable,(range_[0]),variable,int(range_[1])-1)
                elif(len(range_)==3):
                    fin += "for {}={} to {}={} step {}".format(variable,(range_[0]),variable,int(range_[1])-1,range_[2])
                self.writer(fin)     
            else:
                forComprehension = re.findall("^for .+|^ +for .+",self.lines[i])[0][:-1]
                forComprehension = self.trim_spaces(forComprehension)
                fin += forComprehension
                self.writer(fin)

    def functionParser(self,i):
        line = self.trim_spaces(self.lines[i])
        general_func = ['print','set','list','dictionary']
        functionName = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*|^ +[a-zA-Z_][a-zA-Z0-9_]*", line)[0]
        fin = functionName
        if functionName in general_func:
            functionContent = line[len(functionName)+1:-1]
            fin += " " + functionContent
        else:
            functionContent = line[len(functionName):]
            fin += " " + functionContent
        self.writer(fin)

    def compile(self):
        for i in range(len(self.lines)):
            a = self.Tokeniser(self.lines[i])
            if a==1:
                self.loopsParser(i)
            elif a==2:
                self.functionParser(i)
            elif a == 3:
                self.operatorParser(i)

        return 1
    
    def returnOut(self):
        return self.algorithm
    
    def printOut(self):
        print(self.algorithm)

model = AlgoCompiler(code)
model.compile()
algorithm = model.returnOut()
print(algorithm)