## Assignment 2: Parser
***

#### Summary:
Design and implement a lexical part of the compiler i.e. where the input
has already been converted into a list of tokens. Design a set of grammar
rules which will validate a simple expression as being valid or not. Implement 
recursive descent in order to parse the expression to determine validity. Each 
expression passed will return True if valid or False if not valid. 

## Table of Contents
1. [General Info](#general-info)
2.[Learning Outcomes](#learning-outcomes)
3.[Collaboration](#collaboration)

### General Info
***
The rdParser.py file originally contained a skeleton code for which we will build
our parser through. Class recDescent was structured to already include necessary 
instance variables and necessary class functions. Once an expression is given, it is 
transformed into a set of tokens in which we will parse through in order to determine 
the validity of the expression as either True or False. 4 functions have been added to 
the class in order to parse the expression.
parser() : Initial function which loops through tokens and makes function calls to determine validity.
term() : Function which determines if a token matches the grammar of a valid term.
rel_op(): Function which determines if a token is a relational operator.
op(): Function which determines if a token is a logical operator.
With these new functions added to the skeleton code provided, simple expressions can 
be effectively parsed to determine validity of simple expressions.
***
- Effectively parse through tokes file to correctly determine validity of expression.

- Ensure when parsing tokens, we continuously follow the set of grammar rules previously defined.

- Ensure text record parsing checks format conditions for correct assembly statement
output.

- Run tests using provided files as well as testing through GradeScope to ensure
all test cases have been met and passed.

### Learning Outcomes
***
When beginning the assignment, I had no idea where to begin. Recursion is always tricky,
as it involves logical thinking to solve the solution in an effective and efficient manner.
By starting small and validating the simplest expressions first, I was able to improve 
upon the code in order to continuously pass the other test cases. A lack of confidence 
made me start this project later than expected, but once I had some code written down 
and some test cases passed, I was able to finish the code in one sitting. This assignment 
has taught me to tackle any problem I encounter, regardless if the outcome is failure. 

### Collaboration
***
Solo project to properly develop a lexical analyzer parses through simple 
expressions and passed test cases on GradeScope.

Omar Martinez (REDID:818749029) - Contribution:

- Create new functions for the class recDescent in order to properly follow 
EBNF grammar form.
- Create EBNF grammar rules in order to properly validate simple expressions 
when parsing through a list of tokens.
- Implement recursion to validate simple expressions while following grammar rules.