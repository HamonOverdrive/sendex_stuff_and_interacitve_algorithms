from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 4
    # prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            # while loop pops and appends to postfix list until left parentheses is popped also which means a left and right parentheses matched
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
             # if working correctly the last popped token should be '('
                topToken = opStack.pop()
        else:
            # appends next popped operator from stack if peeked item has larger precedence then current token
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())

            # pushes infix item on stack if peeked stack item has less precedence
            opStack.push(token)

    # this pops the remaining operators from stack to final post list
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))
# print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))

# the problem is wrong in online book for # 3 should be wrote as 5 * 3 ^ ( 4 - 2 ) change code as needed