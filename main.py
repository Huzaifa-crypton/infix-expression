'''
    The code applies INFIX operation. The code contains the following features:
    1. Checks if the expression is valid (Brackets are in sequence, no unusual character is placed).
    2. Follows the precedence order.
    3. Applies tokenization
'''

import ast
import re
#### Function to check if expression is valid
def checkExpressionValidation(expression):
    try:
        ast.parse(expression)
        return True
    except:
        return False
#### Function to apply operation on the values    
def applyOperation(val1, val2, operator):
    if operator == '-':
        return val1 - val2
    if operator == '+':
        return val1 + val2
    if operator == '*':
        return val1 * val2
    if operator == '/':
        return val1 / val2

#### Function to check the precedence of the operators
def checkPrecedence(op1 , op2):
    precedenceOrder = ["/" , "*" , "+" , "-"]
    op1_index = precedenceOrder.index(op1)
    op2_index = precedenceOrder.index(op2)
    if (op1_index <= op2_index):
        return 1
    else:
        return 2

# MAIN DRIVER FUNCTION
def main():
    values = []
    operators = []
    ### Taking input from user
    expression = input("Enter your arithmetic expression:")
    expression = expression.replace(" ", "")    
    ### Checking if the entered expression is valid
    while(checkExpressionValidation(expression=expression) == False):
        expression = input("Invalid expression \n Enter your arithmetic expression:")
    i = 0
    while (i < len(expression)):
        token = expression[i]
        print("Token:" , token)
        val = ""
################## Checking if the token is a digit ##################################   
        if (token.isdigit()):
            val = val + token
            i+=1
    # Extracting the number if the number is more than 1 digit        
            while(i < len(expression) and (expression[i].isdigit() or expression[i].__contains__("."))):
                token = expression[i]
                val = val+token
                i+=1
                token = expression[i]
    # Converting to float value if the number is a float number
            if (val.__contains__(".")):
                values.append(float(val))
            else:
    # Converting to int value if the number is a float number
                values.append(int(val))

    ################# Checking if the token is a left parenthesis #####################
        elif (token == "(" or token == "[" or token == "{"):
            operators.append(token)
            i+=1    
    ################# Checking if the token is a right parenthesis ###########
        elif (token == ")" or token == "]" or token == "}"):
            operator = ""
            while (operators[-1] != "(" and operators[-1] != "[" and operators[-1] != "{"):        
                op2 = values.pop()
                op1 = values.pop()
                operator = operators.pop()
                print("Applied Operator:" , operator)
                intermediary_val = applyOperation(op1 , op2 , operator=operator)
                print(f'Left: {op1} , Right: {op2} , Result: {intermediary_val}')
                values.append(intermediary_val)
            operators.pop()
            i+=1
    ################ Checking if the token is an operator (*,-,/,+) ################
        elif (token == "*" or token == "/" or token == "-" or token == "+"):
    # If operators array length is 0 then append the current token operator
            if (len(operators) == 0):
                operators.append(token)
            else:
    # Else check until the top of the operator array is higher in precendence order
                while(len(operators) > 0 and (operators[-1] != "(" and operators[-1] != "[" and operators[-1] != "{") and checkPrecedence(operators[-1] , token) == 1 ):
                    op2 = values.pop()
                    op1 = values.pop()
                    operator = operators.pop()
    # Calculate the intermediary value
                    print("Applied Operator:" , operator)
                    intermediary_val = applyOperation(op1 , op2 , operator=operator)
                    print(f'Left: {op1} , Right: {op2} , Result: {intermediary_val}')
    # Append the intermediary value in the values array
                    values.append(intermediary_val)
    # Append the current token operator
                operators.append(token)
            i+=1
    # When the complete expression is tokenized, we now extract the operators array
    while len(operators) != 0 :        
        op2 = values.pop()
        op1 = values.pop()
        operator = operators.pop()
        print("Applied Operator:" , operator)
        intermediary_val = applyOperation(op1 , op2 , operator=operator)
        print(f'Left: {op1} , Right: {op2} , Result: {intermediary_val}')
        values.append(intermediary_val)
    print("Result:", values[0])
# Executing main function
main()