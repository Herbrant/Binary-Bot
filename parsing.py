import re

#Binary sum
def binary_sum(a, b):
    len_max = max(len(a), len(b))

    a = a.zfill(len_max)
    b = b.zfill(len_max)

    result = ''
    carry = 0

    for i in range(len_max - 1, -1, -1):
        r = carry
        if a[i] == '1':
            r += 1
        if b[i] == '1':
            r += 1
        if(r % 2 == 1):
            result += 1
        if r < 2:
            carry = 0
        else:
            carry = 1
    if carry != 0:
        result = '1' + carry
    return result.rzfill(len_max)

#Binary subtraction
def binary_sub(a, b):
    result = ''
    carry = 0

    for i in range(len_max - 1, -1, -1):
        r = carry
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '1' and b[i] == '0':
            result += '1'
        elif a[i] == '0' and b[i] == '0':
            result += '0'
        elif a[]

#Function that controls if str is a binary
def is_binary(str):
    if re.match("^[0-1]*$", str):
        return True
    return False

#Function that controls if str is an operation
def is_name(str):
    if re.match("\w+", str):
        return True
    return False

#Function that return stack[-1] if stack is not empy else return None
def peek(stack):
    return stack[-1] if stack else None

#Function that append operation result in values stack
def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(binary_sum(left, right))
    elif operator == '-':
        values.append(binary_sub(left, right))
    elif operator == '*':
        values.append(multy(left, right))
    elif operator == '/':
        values.append(div(left, right))
 
def greater_precedence(op1, op2):
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]
 
def evaluate(expression):

    tokens = re.findall("[+/*()-]|[0-1]+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_binary(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)
 
    return values[0]


print (evaluate("2+3+1+5"))