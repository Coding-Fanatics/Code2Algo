import re

# code = '''a = 3 > 4
# a=5+3
# b = 5+3
# c = a*b
# list(c)
# set(a)
# while c > d:
#     a = 33+45
#     b =  a+v
#     while a == b:
#         d = a+3
#     c = 3
# for i in range(1,10,1):
#     a = 3
#     d = 34+7
# for each_word in lambda:
#     for each in each_word:
#         print("Ansah is my Name")
#         a = ansah
#     k = 5 + 2
#     a = 6*7
# d = 97''' 

class AlgoCompiler():
    algorithm = ""
    f_index = 1
    lines = []

    def __init__(self,source):
        self.lines = source.split("\n")
    
    def Tokeniser(l):
        OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l)
        FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l)
        CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", l)
        LoRegx = re.findall("^for+.*:$|^while+.*:$", l)
        IndRegx = re.findall("^ +", l)
        ElseRegx = re.findall("^else", l)
        CommRegx = re.findall("^#", l)
        if len(CommRegx):
            return 6
        elif len(IndRegx):
            return 4
        elif len(CoRegx):
            return 0
        elif len(LoRegx):
            return 1    
        elif len(FnRegx):
            return 2
        elif len(OpRegx):
            return 3      
        else:
            return -1 



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
    
    def Translate(self,op):
        op = op.split(">")
        op = "greater than".join(op)
        op = op.split("<")
        op = "less than".join(op)
        op = op.split("<=")
        op = "less than or equal to".join(op)
        op = op.split(">=")
        op = "greater than or equal to".join(op)
        op = op.split("!=")
        op = "not equal to".join(op)
        op = op.split("==")
        op = "equal to".join(op)
        return op

        # raise ValueError("There's an error in line "+str(i))

    def operatorParser(self,i):
        compiled_ = self.Translate(self.lines[i].lstrip())
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
            condition_ = self.lines[i][5:].lstrip()
            fin += " while {}".format(condition_)
            self.writer(self.Translate(fin))
        elif forReg:
            variable = re.findall("^for .+ in|^ +for .+ in", self.lines[i])
            if variable:
                variable = variable[0][4:-3].lstrip()

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
                self.writer(self.Translate(fin))     
            else:
                forComprehension = re.findall("^for .+|^ +for .+",self.lines[i])[0][:-1]
                forComprehension = forComprehension.lstrip()
                fin += forComprehension
                self.writer(self.Translate(fin))

    def functionParser(self,i):
        line = self.lines[i].lstrip()
        general_func = ['print','set','list','dictionary']
        functionName = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*|^ +[a-zA-Z_][a-zA-Z0-9_]*", line)[0]
        fin = functionName
        if functionName in general_func:
            functionContent = line[len(functionName)+1:-1]
            fin += " " + functionContent
        else:
            functionContent = line[len(functionName):]
            fin += " " + functionContent
        self.writer(self.Translate(fin))

    def compile(self):
        for i in range(len(self.lines)):
            a = self.Tokeniser(self.lines[i])
            if a==1:
                self.loopsParser(i)
            elif a==2:
                self.functionParser(i)
            elif a == 3:
                self.operatorParser(i)
            elif a == 4:
                pass
            else:
                raise ValueError("There is an error in line {}".format(i))

        return 1
    
    def returnOut(self):
        return self.algorithm
    
    def printOut(self):
        print(self.algorithm)

# model = AlgoCompiler(code)
# model.compile()
# algorithm = model.returnOut()
# print(algorithm)