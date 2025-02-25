from collections import deque


def validParenthesis(input: str) -> bool:

    stack = deque()

    for char in input:
       
        if (char=='{' or  char =='[' or char =='('):
            #print('char> ', char)
            stack.append(char)
        else:
            if getOppositeParen(char) in stack:
                stack.pop()
            else:
                return False
        
    return True
    



def getOppositeParen(input: str) -> str:
    if (input==')'):
        return '('
    elif (input =='}'):
        return '{'
    elif (input==']'):
        return '['
    else:
        return input


print(validParenthesis("()]"))

"""

({}[]{})


({[ insert

if ), check if last index is (, pop, else return false
if ], check if last index is [, pop, else return false
if }, check if last index is {, pop, else return false
"""