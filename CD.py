import re

# Write a program that reads an input text file, and constructs a list of tokens in that file. Your program can
# be written in any programming language of your choice without using standard library functions for lexical
# analysis task assuming that the input file contains the following code string:
# Sample text file :-
# void main ()
# { int sum = 0;
# for(int j=0; j &lt; 10; j=j+1)
# { sum = sum + j + 10.43 + 34E4 + 45.34E-4 + E43 + .34; }
# }
# Output expected:- Define regular expression for tokens and generate DFA. Display the count of No of tokens
# generated.
# keyword : void , identifier : main , ( : (, ) : ) , { : {, keyword : int, identifier : sum , = : = , num : 0 , ; : ; , keyword : for , ( : (
# keyword : int, identifier : j , = : = , num : 0 , ; : ; , identifier : j , &lt; : &lt; , num : 10, ; : ; , identifier : j , = : = , identifier : j
# + : + , num : 1 , ) : ), { : { , identifier : sum , = : = , identifier : sum , + : +, identifier : j , + : + , num : 10.43 , + : +
# num : 34.E4 , + : +, num : 45.34E-4 , + : +, identifier : E43, + : +, Error : . , num : 34 ; : ; ,} : } , } : }





#Readin the file
f = open('Input.c', 'r')

#Count the number of Tokens
Token_count=0


#Operators and Delimiters
operators = {'=': 'Assignment Operator', '+': 'Additon Operator', '-': 'Substraction Operator',
             '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'increment Operator',
             '--': 'Decrement Operator'}
optr_keys = operators.keys()       


delimiter = {'{': 'Opening Curly Bracket', '}': 'Closing Curly Bracket', '(': 'Opening Bracket',
              ')': 'Closing Bracket', '[': 'Opening Square Bracket', ']': 'Closing Square Bracket',
              ';': 'Semicolon', ',': 'Comma'}
delimiter_key = delimiter.keys()


#comments
comments = {r'//': 'Single Line Comment', r'/*': 'Multiline Comment Start', r'*/': 'Multiline Comment End',
            '/**/': 'Empty Multiline comment'}
comment_keys = comments.keys()

#Header
header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>': 'Standard Input Output Header', '<string.h>': 'String Manipulation Library'}

macros = {r'#\w+': 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer', 'float': 'Floating Point', 'char': 'Character', 'long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return': 'keyword that returns a value from a block','if':'keyword ','while':'keyword',
           'continue':'keyword','main()':'keyword','(':'(',')':')'
           }
keyword_keys = keyword.keys()




blocks = {'{': 'Blocked Statement Body Open', '}': 'Blocked Statement Body Closed'}
block_keys = blocks.keys()

builtin_functions = {'printf': 'printf prints its argument on the console'}

non_identifiers = ['_', '-', '+', '/', '*', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '|', '"',
                   ':', ';', '{'
    , '}', '[', ']', '<', '>', '?', '/']

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Flags
dataFlag = False

i = f.read()

count = 0
program = i.split()

for line in program:
    count = count + 1
    print( "Line #", count, "\n", line)


    tokens = line.split(' ')
    print("Tokens are", tokens)
    Token_count+=len(tokens)
    print("Line #", count, 'properties \n')

    for token in tokens:

        if '\r' in token:
            position = token.find('\r')
            token = token[:position]
        # print 1

        if token in block_keys:
            print(blocks[token])

        if token in optr_keys:
            print("Operator is: ", operators[token])

        if token in comment_keys:
            print("Comment Type: ", comments[token])

        if token in macros_keys:
            print("Macro is: ", macros[token])

        if '.h' in token:
            print("Header File is: ", token, sp_header_files[token])

        if '()' in token:
            print("Function named", token)


        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print( "Identifier: ", token)

        if token in datatype_keys:
            print("Data Type")
            print("type is: ", datatype[token])

            dataFlag = True

        if token in keyword_keys:
            print(keyword[token])


        if token in delimiter:
            print("Delimiter", delimiter[token])

        if '#' in token:
            match = re.search(r'#\w+', token)
            print( "Header", match.group())

        if token in numerals:
            print( token, type(int(token)))


    dataFlag = False

    print("________________________")

print(f'Total Tokens Generated are {Token_count}')

f.close()