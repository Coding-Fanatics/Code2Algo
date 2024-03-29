"""Compiler module to convert python to algorithm"""
import re


class AlgoCompiler:
    """Compiler class for the algorithm"""

    algorithm = ""
    f_index = 1
    funcdefs = []
    lines = []

    def __init__(self, source):
        self.lines = source.split("\n")

    def Tokeniser(self, l):
        """Tokenizer function to recognize the type of line"""
        OpRegx = re.findall(
            "^[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+|^ +[a-zA-Z_][a-zA-Z0-9_]*[ ]*=[ ]*.+", l
        )
        FnRegx = re.findall(
            "[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]|^ +[a-zA-Z_][a-zA-Z0-9_]*[(].*[)]", l
        )
        CoRegx = re.findall(
            "^if+.*:$|^else+.*:$|^elif+.*:$|^ +if+.*:$|^ +else+.*:$|^ +elif+.*:$", l
        )
        LoRegx = re.findall("^for+.*:$|^while+.*:$|^ +while+.*:$|^ +for+.*:$", l)
        FunRegx = re.findall("^def .*:$", l.lstrip())
        ComRegx = re.findall("^#", l)
        BlankRegx = re.findall("^ +", l)
        if CoRegx:
            return 0
        if LoRegx:
            return 1
        if FunRegx:
            return 6
        if FnRegx:
            return 2
        if OpRegx:
            return 3
        if ComRegx:
            return 4
        if BlankRegx or l == "":
            return 5

        if "while" in l.lstrip()[:5] or "for" in l.lstrip()[:3]:
            return 1
        if (
            "if" in l.lstrip()[:2]
            or "else" in l.lstrip()[:4]
            or "elif" in l.lstrip()[:4]
        ):
            return 0
        return -1

    def level(self, i):
        """
        Level to identify the level inendation
        primarily helpful in identifying the block of codes
        """
        level = 0
        for eachLett in self.lines[i]:
            if eachLett == " ":
                level += 1
            else:
                break

        return level

    def writer(self, compiled_, mode=1):
        """ "Code writing handler"""
        if mode == 0:
            self.f_index = 0
            self.algorithm = ""
        elif self.f_index == 0:
            self.algorithm = "-" * 10 + "\n"
            self.algorithm += str(compiled_) + "\n"
            self.f_index += 1
        else:
            self.algorithm += str(self.f_index)
            self.algorithm += ". " + str(compiled_) + "\n"
            self.f_index += 1

    def Translate(self, op):
        """translator for converting code to english"""
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

    def operatorParser(self, i):
        """parser which translates operands to english"""
        compiled_ = self.Translate(self.lines[i].lstrip())
        self.writer(compiled_)

    def loopsParser(self, i):
        """
        Python loop parser
        handles the parsing of : while, for loops
        """
        initialLevel = self.level(i)
        start_step = i
        temp_line = i + 1
        next_step = temp_line
        while self.level(temp_line) != initialLevel and temp_line < len(self.lines):
            temp_line += 1

        next_step = temp_line - 1

        whileReg = re.findall("^while|^ +while", self.lines[i])
        forReg = re.findall("^for|^ +for", self.lines[i])
        if start_step + 1 == next_step:
            fin = "repeat step {} ".format(next_step + 1)
        else:
            fin = "repeat step {} to {} ".format(start_step + 2, next_step + 1)

        if whileReg:
            condition_ = self.lines[i][initialLevel + 5 :].lstrip()
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
                if len(range_) == 1:
                    fin += "for {}=0 to {}={} step 1".format(
                        variable, variable, int(range_[0]) - 1
                    )
                elif len(range_) == 2:
                    fin += "for {}={} to {}={} step 1".format(
                        variable, (range_[0]), variable, int(range_[1]) - 1
                    )
                elif len(range_) == 3:
                    fin += "for {}={} to {}={} step {}".format(
                        variable, (range_[0]), variable, int(range_[1]) - 1, range_[2]
                    )
                self.writer(self.Translate(fin))
            else:
                forComprehension = re.findall("^for .+|^ +for .+", self.lines[i])[0][
                    :-1
                ]
                forComprehension = forComprehension.lstrip()
                fin += forComprehension
                self.writer(self.Translate(fin))

    def functionParser(self, i):
        """
        Python function parser
        handles common functions such as print(), set() etc
        """
        line = self.lines[i].lstrip()
        general_func = ["print", "set", "list", "dictionary"]
        functionName = re.findall(
            "^[a-zA-Z_][a-zA-Z0-9_]*|^ +[a-zA-Z_][a-zA-Z0-9_]*", line
        )[0]
        fin = functionName
        if functionName in general_func:
            functionContent = line[len(functionName) + 1 : -1]
            fin += " " + functionContent
        else:
            functionContent = line[len(functionName) :]
            fin += " " + functionContent
        self.writer(self.Translate(fin))

    # def userFunctionParser(self,i):
    #     line = self.lines[i].lstrip()
    #     line = 'define '+line[4:]
    #     line = ' '*self.level(i) + line
    #     self.writer(line)

    def FunCollect(self, i):
        """
        Python functions collector
        identifies python and appends to function list
        new saperate function generation can be done by extracting from function list
        """
        line = self.lines[i].lstrip()
        # functionName = re.findall("^[a-zA-Z_][a-zA-Z0-9_]*|^ +[a-zA-Z_][a-zA-Z0-9_]*", line)[0]
        functionName = re.findall("^def [a-zA-Z_].*", line)[0][4:-1]
        funcLines = []
        init_level = self.level(i)
        temp_line = i + 1
        while self.level(temp_line) > init_level and temp_line < len(self.lines):
            funcLines.append(self.lines[temp_line])
            del self.lines[temp_line]
        self.funcdefs.append((functionName, funcLines))

    def conditionParser(self, i):
        """
        Python conditions parser
        handles : if, elif, else
        """
        initialLevel = self.level(i)
        start_step = i
        temp_line = i + 1
        next_step = temp_line
        while self.level(temp_line) != initialLevel and temp_line < len(self.lines):
            temp_line += 1

        next_step = temp_line - 1

        ifRegx = re.findall("^if|^ +if", self.lines[i])
        elseRegx = re.findall("^else|^ +else", self.lines[i])
        elifRegx = re.findall("^elif|^ +elif", self.lines[i])

        _elseRegx = re.findall("^else|^ +else", self.lines[next_step + 1])
        _elifRegx = re.findall("^elif|^ +elif", self.lines[next_step + 1])

        if len(ifRegx):
            condition_ = self.lines[i][initialLevel + 2 :].lstrip()
            fin = "if {} ".format(condition_)
            if len(_elifRegx) or len(_elseRegx):
                fin += "- go to step {} else to {}".format(
                    start_step + 2, next_step + 2
                )
            else:
                fin += "- go to step {}".format(start_step + 2)
            # self.writer(self.Translate(fin))
        elif len(elifRegx):
            condition_ = self.lines[i][initialLevel + 4 :].lstrip()
            fin = "Else if {} ".format(condition_)
            if len(_elseRegx):
                fin += "- go to step {} else to {}".format(
                    start_step + 2, next_step + 2
                )
            else:
                fin += "- go to step {}".format(start_step + 2)
            # self.writer(self.Translate(fin))
        elif len(elseRegx):
            fin = "Else "
            fin += "- go to step {} ".format(start_step + 2)

        self.writer(self.Translate(fin))

    def compile(self):
        """
        primary compiler
        goes line-by-line
        """
        funcs = self.compile1()
        algorithm1 = self.returnOut()
        for each in funcs:
            self.writer("", 0)
            name, self.lines = each
            self.writer("Function Defenition of {}".format(name))
            self.compile1()
            algorithm1 = self.returnOut(algorithm1)
        self.algorithm = algorithm1

    def compile1(self):
        """
        Secondary compiler
        identifies tokens and compiles accordingly
        """
        i = 0
        while i < len(self.lines):
            a = self.Tokeniser(self.lines[i])
            if a == 5:
                del self.lines[i]
            elif a == 6:
                self.FunCollect(i)
                del self.lines[i]
            else:
                if a == 0:
                    self.conditionParser(i)
                elif a == 1:
                    self.loopsParser(i)
                elif a == 2:
                    self.functionParser(i)
                elif a == 3:
                    self.operatorParser(i)
                elif a == 4:
                    pass
                i += 1
        return self.funcdefs

    def returnOut(self, fileExt=""):
        """Return output, to use the generated algorithm in other functions"""
        return fileExt + self.algorithm

    def printOut(self):
        """display the generated algorithm"""
        print(self.algorithm)

    def printFunCollect(self):
        """display collected funciton"""
        print(self.funcdefs)
