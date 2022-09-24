import re

#Readin the file
f = open('Input.c', 'r')
#Count the number of Tokens
Token_count=0
#Count the number of Lines
dataFlag = False
i = f.read()
count = 0
program = i.split()
for line in program:
    count = count + 1
    tokens = line.split(' ')
    print("Tokens at line: ", count," is: ", tokens)
    Token_count+=len(tokens)
    for token in tokens:
        if '\r' in token:
            position = token.find('\r')
            token = token[:position]
    dataFlag = False
    # print("________________________\n")

print(f'Total Number of Tokens Generated are {Token_count}')
print("Token Generated Are: ")
print(program)
f.close()
