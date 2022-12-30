# Code2Algo
Code to algorithm
This is a compiler which converts Python code into an Algorithm.

This Compiler helps in distribution of Codes written in Python for non-Python programmers.

<hr>
<h1> Documentation </h1>

<b>__init__(self, source):</b> This is the constructor for the AlgoCompiler class, which takes in a parameter source representing the source code to be compiled. The source is split into individual lines and stored in the lines attribute of the object.<br>
<br>
<b>Tokeniser(self, l):</b> This method takes in a single line of code l as a parameter and returns an integer representing the type of token in the line. The types of tokens are:<br>
<br>
0: Control flow statement (e.g. if, else, elif)<br>
1: Loop statement (e.g. for, while)<br>
2: Function call<br>
3: Operation/assignment<br>
4: Comment<br>
5: Blank line<br>
6: Function definition<br>
-1: Invalid token<br>
level(self, i): This method takes in an integer i representing the index of a line in the lines attribute, and returns the number of leading spaces in the line (indicating the level of indentation).<br>
<br>
writer(self, compiled_, mode=1): This method takes in a list compiled_ of compiled lines and an optional parameter mode, which is an integer representing the mode in which the method should run. The mode parameter can have the following values:<br>
<br>
0: Clear the algorithm attribute and write the compiled lines to it.<br>
1 (default): Append the compiled lines to the algorithm attribute.<br>
2: Write the compiled lines to the algorithm attribute and add a separator line between each line.<br>
Compiler(self): This is the main method of the AlgoCompiler class, which compiles the source code stored in the lines attribute. The method iterates through each line in the lines attribute and uses the Tokeniser method to identify the type of token in the line. It then calls the appropriate method to handle the token and adds the compiled line to a list. The list of compiled lines is then passed to the writer method to be written to the algorithm attribute.<br>
<br>
The AlgoCompiler class also has several attributes:<br>
<br>
algorithm: A string representing the compiled version of the source code.<br>
f_index: An integer representing the index of the current function definition being compiled.<br>
funcdefs: A list of compiled function definitions.<br>
lines: A list of the individual lines of the source code.<br>
