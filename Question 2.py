
# int main ( )
# {
#      int a ;
#      a = 10 ;
#      printf("The value of a is %d" ,a) ;
#      return 0;
# }

#List 
keyword = ['break','case','char','const','countinue','deafult','do','int','else','enum','extern','float','for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['clrscr()','printf(','scanf(','getch()','main()']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
specialsymbol = ['@','#','$','_','!']
separator = [',',':',';','\n','\t','{','}','(',')','[',']']

#Dictionary
operators = {'=': 'Assignment Operator', '+': 'Additon Operator', '-': 'Substraction Operator',
             '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'increment Operator',
             '--': 'Decrement Operator','(':'(',')':')','{':'{','}':'}','[':'[',']':']'}
# print(operators['='])
optr_keys = operators.keys()       #keys of operators
Token_count=0               #count of tokens

import re

#Function to check if the token is a keyword
file = open('Input.c','r+')
contents = file.read()
splitCode = contents.split() 
print(splitCode)
Token_count=len(splitCode)
print(f'Token Count is {Token_count}')
length = len(splitCode)      
for i in range(0,length):
    if splitCode[i] in keyword:
        print("Keyword -->",splitCode[i])
        continue
    if splitCode[i] in optr_keys:
        print("Operators --> ",operators[splitCode[i]])
        continue
    if splitCode[i] in specialsymbol:
        print("Special Operator -->",splitCode[i])
        continue
    if splitCode[i] in built_in_functions:
        print("Built_in Function -->",splitCode[i])
        continue
    if splitCode[i] in separator:
        print("Separator -->",splitCode[i])
        continue
    # if re.match(r'(#include*).*', splitCode[i]):
    #     print ("Header File -->", splitCode[i])
    #     continue
    if re.match(r'^[-+]?[0-9]+$',splitCode[i]):
        print("Numerals --> ",splitCode[i])
        continue
    if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):
        print("Identifier --> ",splitCode[i])