class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                # Pop the two most recent operands (order matters!)
                b = stack.pop()   # right operand
                a = stack.pop()   # left operand
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division truncates toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]