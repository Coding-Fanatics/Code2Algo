from codeop import Compile
import re

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

class algoCompiler:
    source = ""
    pc = 1
    lines = []
    def __init__(self,Source) -> None:
        self.source = Source
        self.lines = Source.split('\n')
        print(self.pc)

    def level(self,i):
        level = 0
        for eachLett in self.lines[i]:
            if eachLett == ' ':
                level += 1
            else:
                break
        
        return level
    
    def trim_spaces(st):
        trimmed = ""
        for i in range(len(st)):
            if st[i] == ' ':
                continue
            else:
                trimmed = st[i:]
                break
        return trimmed

    def compile(self):
        for i in range(len(self.lines)): 
            t1 = uniCompiler(self.lines[self.pc]) 
            t1.process()
            print(t1.getCompiled())
            self.pc += 1

class uniCompiler(algoCompiler):
    Dat = ""
    Compiled = ""
    lineIndex = 1

    def __init__(self,Dat):
        self.Dat = Dat

    def getCompiled(self):
        return self.Compiled

    def writer(self,compiled_):
        self.Compiled += str(self.lineIndex)
        self.Compiled += ". {}".format(compiled_)
        self.Compiled += "\n"
        self.lineIndex += 1

    def Tokeniser(self,line):
        OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", line)
        FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]|^ +[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", line)
        CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", line)
        LoRegx = re.findall("^for+.*:$|^while+.*:$|^ +while+.*:$|^ +for+.*:$", line)
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

    def process(self):
        a = self.Tokeniser(self.Dat)
        if a==1:
            self.loopsParser(self.pc)
        elif a==2:
            self.functionParser(self.pc)
        elif a == 3:
            self.operatorParser(self.pc)

    def printPC(self):
        print(self.pc)

model = algoCompiler(code)
model.compile()