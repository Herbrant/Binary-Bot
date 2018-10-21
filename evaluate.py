import re

#Decimal to binary function
def dec_to_binary(n):
    if n == 0:
        return '0'
    else:
        return dec_to_binary(n // 2) + str(n%2)

#Decimal to two's complement function
def dec_to_two(n):
    if(n[0] == '+'):
        return dec_to_binary(int(n[1:]))
    elif n[0] == "-":
        binary = dec_to_binary(int(n[1:]))
        binary2 = ""
        for i in range(len(str(binary)) - 1, -1, -1):
            if binary[i] == '0':
                binary2 = '1' + binary2
            else:
                binary2 = '0' + binary2
        return binary_sum(binary2, "01")

    else:
        return dec_to_binary(int(n))

#Two's complement to decimal function
def binary_to_dec(n):
    sum = 0
    if n[0] == '1':
        sum += (2**(len(str(n)) - 1))* -1
    for i in range(1, len(str(n)), 1):
        if n[i] == '1':
            sum += 2**(len(str(n)) - 1 - i)
    return sum

#Normalize lengths Function
def normalizelen(a, b):
    maxlen = max(len(str(a)), len(str(b)))

    for i in range(0, maxlen - len(str(a)), 1):
        a = a[0] + a
    for i in range(0, maxlen - len(str(b)), 1):
        b = b[0] + b
    return (a,b)

#Binary comparison operators
def is_greater(a, b):
    maxlen = max(len(str(a)), len(str(b)))
    #Normalize lengths

    if a[0] == '0' and b[0] == '1':
        return True
    elif a[0] == '1' and b[0] == '0':
        return False
    else:
        for i in range(0, maxlen, 1):
            if a[i] > b[i]:
                return True
    return False

#Reverse binary number function
def binary_reverse(a):
    reverse = ""

    for i in range(len(str(a)) - 1, -1, -1):
        if a[i] == '0':
            reverse = '1' + reverse
        else:
            reverse = '0' + reverse
    return binary_sum(reverse, "01")

#Binary sum
def binary_sum(a,b):
    maxlen = max(len(str(a)), len(str(b)))
    signequal = -1
    if a[0] == b[0]:
        signequal = a[0]
    #Normalize lengths
    (a,b) = normalizelen(a,b)

    result = ''
    carry = 0

    for i in range(maxlen - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if (signequal == '0') & (result[0] != signequal):   #Signbit check1
        result = '0' + result
    elif (signequal == '1') & (result[0] != signequal): #Signbit check2
        result = '1' + result

    return result

#Binary subtraction
def binary_sub(a,b):
    #Normalize lengths
    (a,b) = normalizelen(a,b)
    return binary_sum(a, binary_reverse(b))

#Binary multiply
def binary_multiply(a, b):
    sum = "0"
    maxlen = max(len(str(a)), len(str(b)))

    #Normalize lengths
    (a,b) = normalizelen(a,b)
    for i in range(0, maxlen, 1):
        a = a[0] + a
        b = b[0] + b

    for i in range(len(str(b)) - 1,-1, -1):
        partial = ""
        for j in range(0 , len(str(a)), 1):
            if a[j] == '1' and b[i] == '1':
                partial += '1'
            elif a[j] == '1' and b[i] == '0':
                partial += '0'
            elif a[j] == '0' and b[i] == '1':
                partial += '0'
            elif a[j] == '0' and b[j] == '0':
                partial += '0'
        partial = partial + '0'*(len(b) - i - 1)
        sum = binary_sum(sum, partial)

    return sum[-maxlen*2:]

#Binary division
def binary_div(a, b):
    maxlen = max(len(str(a)), len(str(b)))

    #Normalize lengths
    (a,b) = normalizelen(a,b)
    for i in range(0, maxlen, 1):
        a = a[0] + a
        b = b[0] + b

    for i in range(0, len(str(b)) - 1, 1):
        a = a[:i+len(str(b)) - 1]           #Arith

    return a

#Shunting-yard algorithm (Edger Dijkstra).

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
        values.append(binary_multiply(left, right))
    elif operator == '/':
        values.append(binary_div(left, right))

def greater_precedence(op1, op2):
    precedences = {'+' : 0, '-' : 0, '*' : 1, '/' : 1}
    return precedences[op1] > precedences[op2]

def evaluate(expression):
    tokens = re.findall("[+/*()-]|[0-1]+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_binary(token):
            values.append(token)
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
