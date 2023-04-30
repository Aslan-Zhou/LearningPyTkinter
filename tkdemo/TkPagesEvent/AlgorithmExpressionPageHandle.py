from TkPagesUtils.Stack import Stack


class AlgorithmExpressionPageHandle:
    def __init__(self, infix_expr):
        self.tokenList = infix_expr
        self.postfix_expr = self.infixToPostfix2()

    def infixToPostfix(self):
        self.prec = {"*": 3, "/": 3, "+": 2,
                     "-": 2, "(": 1}
        self.opStack = Stack()
        self.postfixList = []

        for token in self.tokenList:

            if token.isdigit():
                self.postfixList.append(token)
            elif token == "(":
                self.opStack.push(token)
            elif token == ")":
                topToken = self.opStack.pop()
                while topToken != "(":
                    self.postfixList.append(topToken)
                    topToken = self.opStack.pop()

            else:
                while (not self.opStack.isEmpty()) and \
                        (self.prec[self.opStack.peek()] >= self.prec[token]):
                    self.postfixList.append(self.opStack.pop())
                self.opStack.push(token)

        while not self.opStack.isEmpty():
            self.postfixList.append(self.opStack.pop())

        return " ".join(self.postfixList)

    def postfixEval(self):
        self.operand_Stack = Stack()
        self.tokenList = self.postfix_expr.split()

        for token in self.tokenList:
            if token.isdigit():
                self.operand_Stack.push(int(token))
            else:
                operand2 = self.operand_Stack.pop()
                operand1 = self.operand_Stack.pop()
                result = self.doMath(token, operand1, operand2)
                self.operand_Stack.push(result)

        return self.operand_Stack.pop()

    @staticmethod
    def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        elif op == '-':
            return op1 - op2
        else:
            return '非法运算符号!'

    def postfixEval2(self):
        self.Stack = Stack()
        self.ExprList = self.postfix_expr.split()
        for Expr in self.ExprList:
            if Expr.isdigit():
                self.Stack.push(Expr)
            elif Expr in '+-*/':

                num1 = int(self.Stack.pop())
                num2 = int(self.Stack.pop())
                result = self.doMath(Expr, num2, num1)
                self.Stack.push(result)
        return self.Stack.pop()

    def infixToPostfix2(self):
        self.exprStack = Stack()
        self.exprStack.push('初始化')
        self.postFixList = []

        for token in self.tokenList:
            if token.isdigit():
                self.postFixList.append(token)
            elif token == '(':
                self.exprStack.push(token)
            elif token == ')':
                topToken = self.exprStack.pop()
                while topToken != '(':
                    self.postFixList.append(topToken)
                    if not self.exprStack.isEmpty():
                        topToken = self.exprStack.pop()
                    else:
                        raise IndexError("算式不合法!")
            else:
                if not self.exprStack.isEmpty():
                    if token in '*/':
                        if self.exprStack.peek() in '*/':
                            self.postFixList.append(self.exprStack.pop())
                    else:
                        if self.exprStack.peek() != "(":
                            if self.exprStack.peek() != '初始化':
                                self.postFixList.append(self.exprStack.pop())
                    self.exprStack.push(token)
                else:
                    raise IndexError("算式不合法!")

        while not self.exprStack.isEmpty():
            self.postFixList.append(self.exprStack.pop())
        return " ".join(self.postFixList)
