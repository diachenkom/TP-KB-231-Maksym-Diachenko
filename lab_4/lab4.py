import math
operations = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def is_operator(expr):
    return expr in operations

def prior(op):
    return operations[op]

def is_number(expr):
    try:
        float(expr)
        return True
    except ValueError:
        return False

def to_zpz(expression):
    output = []
    stack = []
    input_expr = expression.split()

    for expr in input_expr:
        if is_number(expr):
            output.append(expr) 
        elif expr == '(':
            stack.append(expr)
        elif expr == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        elif is_operator(expr):
            while (stack and stack[-1] != '(' and
                   prior(stack[-1]) >= prior(expr)):
                output.append(stack.pop())
            stack.append(expr)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_zpz(zpz_expression):
    stack = []
    for expr in zpz_expression:
        if is_number(expr):
            stack.append(float(expr))
        elif is_operator(expr):
            b = stack.pop()
            a = stack.pop()
            if expr == '+':
                stack.append(a + b)
            elif expr == '-':
                stack.append(a - b)
            elif expr == '*':
                stack.append(a * b)
            elif expr == '/':
                stack.append(a / b)
            elif expr == '^':
                stack.append(a ** b)
    return stack[0] if stack else None

def main():
    print("Введіть математичний вираз (числа, оператори і дужки розділені пробілом):")
    expression = input()
    zpz = to_zpz(expression)
    print("Зворотний польський запис:", zpz)
    result = evaluate_zpz(zpz)
    print("Результат:", result)

if __name__ == "__main__":
    main()
