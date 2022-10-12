import re

lines = []

class lines:
    def __init__(self):
        pass

    def Tokeniser(self):
        OpRegx = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", self)
        FnRegx = re.findall("[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", self)
        CoRegx = re.findall("^if+.*:$|else+.*:$|elif+.*:$", self)
        LoRegx = re.findall("^for+.*:$|^while+.*:$", self)
        IndRegx = re.findall("^ +", self)
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


    def opTranslator(self, i):
        if_or_elif = re.findall("if|elif", self)
        op1 = self.split(if_or_elif[0])
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