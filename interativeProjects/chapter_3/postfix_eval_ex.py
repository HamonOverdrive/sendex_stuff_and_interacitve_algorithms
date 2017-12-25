from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    # split expresssions into individual list
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

# self check 1 answer : 10 3 5 * 16 4 - / +
# self check 2 answer : 17+10 * 3 == 3 / 9