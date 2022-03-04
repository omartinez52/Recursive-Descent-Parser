"""
    rdParser.py
    - Program which uses syntactical analysis to parse tokens of an expression.
    - Utilizes grammar rules in Extended Backus-Naur Form (EBNF) to determine
      validity of expressions.
    - Recursively parses through list of tokens while maintaining EBNF grammar.
    - Outputs True if expression is valid, False otherwise.
"""
import re
from functools import *

"""

Assignment 2 - 
A LL(1) recursive descent parser for validating simple expressions.

# Task A:
You would need to first write the grammar rules (non-terminal) in EBNF 
according to the token patterns and grammar rules specified in the prompt,
put the rules in a separate PDF file, see prompt. 
(Refer to the EBNF example in Figure 5.15)

# Task B:
You would then write the recursive descent parsing procedures for the 
validation parsing according to the rules from Task A. 
(Refer to the parsing algorithm in Figure 5.17)

It implements one parsing procedure for each one of the 
non-terminals (grammar rules), starting from the top of the parse tree, 
then drilling into lower hierachical levels.

The procedures work together to handle all combinations of the grammar 
rules, and they automatically handle the nested compositions of terms 
with multi-level priority brackets. 

----------------------------------------------------------------------------
Usage (Refer to the prompt for more examples - both positive and negative cases)

r = recDecsent('7 - 17')
print(r.validate()) # will print True as '7 - 17' is a valid expression

r = recDecsent('7 - ')
print(r.validate()) # will print False as '7 - ' is an invalid expression

"""

class recDescent:

    # IMPORTANT:
    # You MUST NOT change the signatures of 
    # the constructor, lex(self) and validate(self)
    # Otherwise, autograding tests will FAIL

    # constructor to initialize and set class level variables
    def __init__(self, expr = ""):

        # string to be parsed
        self.expr = expr
        # list of valid logical operators
        self.log_ops = ['and','or','nand','xor','xnor']
        # number of open parenthesis
        self.open_par = 0
        # number of closed parenthesis
        self.close_par = 0
        # tokens from lexer tokenization of the expression
        self.tokens = []

    # lexer - tokenize the expression into a list of tokens
    # the tokens are stored in an list which can be accessed by self.tokens
    # do not edit any piece of code in this function
    def lex(self):
        self.tokens = re.findall("[-\(\)=]|[!<>]=|[<>]|\w+|[^ +]\W+", self.expr)
        # transform tokens to lower case, and filter out possible spaces in the tokens
        self.tokens = list(filter((lambda x: len(x)), 
                           list(map((lambda x: x.strip().lower()), self.tokens))))    
    
    # parser - determine if the input expression is valid or not
    
    # validate() function will return True if the expression is valid, False otherwise 
    # do not change the method signature as this function will be called by the autograder
    def validate(self):
        # Using the tokens from lex() tokenization,
        # your validate would first call lex() to first tokenize the expression
        # then call the top level parsing procedure and go from there
        self.lex()
        flag = self.parser()
        return flag
        pass

    # parsing procedures corresponding to the grammar rules - follow Figure 5.17

    def parser(self):
        """
        parser()
            - Function parses through tokens to determine the validity of the expression.
            - Makes calls to determine is a valid term or is a valid operator.
            - Also determines validity through open and closed parenthesis observed.
        :return: True if expression is valid, False OW.
        """
        # flag to determine validity
        found = False
        # return false if empty
        if len(self.tokens) <= 1:
            return found
        # check if token is a term
        if self.term():
            found = True
            # loop through token list until empty.
            while len(self.tokens):
                if self.term():
                    found = True
                elif self.op():
                    found = True
                else:
                    found = False
                    break
        # return false if # of '(' not equal to # of ')'
        if self.open_par != self.close_par:
            return False
        return found

    def rel_op(self):
        """
        rel_op()
            - Determines if token is a relation operator or not.
        :return: True if token is relational operator, False OW.
        """
        found = False
        if self.tokens[0] == '<':
            found = True
        elif self.tokens[0] == '>':
            found = True
        elif self.tokens[0] == '<=':
            found = True
        elif self.tokens[0] == '>=':
            found = True
        elif self.tokens[0] == '!=':
            found = True
        elif self.tokens[0] == '=':
            found = True
        elif self.tokens[0] == 'not':
            found = True
        return found

    # checks if token is a logical operator
    def op(self):
        """
        op()
            - Determines if token is in list of valid logical operators.
            - Checks if token list is empty before proceeding.
        :return: True if token is logical operator, False OW.
        """
        # return false if empty
        if not len(self.tokens):
            return False
        # check if token in list of logical operators
        if self.log_ops.count(self.tokens[0]):
            self.tokens.pop(0)
            return True
        return False

    def term(self, prev = ''):
        print(f"Prev term : {prev} \n curr token: {self.tokens[0]}")
        """
        term()
            - Determines if token is a valid term.
            - Checks if token is a int/digit, relational operator,
              dash operator or if a new expression has been started.
            - Keeps track of open and closed parenthesis to determine
              validity at end of parsing.
        :return: True if term is valid, False OW.
        """
        # return false if empty
        if not len(self.tokens):
            return False
        # check if term is an integer
        if self.tokens[0].isdigit():
            # remove token after being read
            self.tokens.pop(0)
            # recursive call to check if next token is a term
            return True
        # check if term is relop int
        elif self.rel_op():
            if prev == "relop":
                return False
            # remove token after being read
            self.tokens.pop(0)
            # recursive call to see if next token is term
            return self.term("relop")
        elif self.tokens[0] == '-':
            # remove token after being read
            self.tokens.pop(0)
            # recursive call to see if next token is term
            return self.term()
        elif self.tokens[0] == '(':
            # increment number of open parentheses & closed par needed
            self.open_par += 1
            # remove token after being read
            self.tokens.pop(0)
            # recursive call to see if next token is term
            return self.term()
        elif self.tokens[0] == ')':
            self.close_par += 1
            # remove token after being read
            self.tokens.pop(0)
            # recursive call to see if next token is term
            return True
        # return false if not valid
        else:
            return False

# obj = recDescent(expr="7")
# obj.validate()
# print(obj.tokens)