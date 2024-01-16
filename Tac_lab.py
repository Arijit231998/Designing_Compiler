def generate_three_address_code(expression):
    stack = []
    operators = []
    temp_var_count = 1
    three_address_code = []

    def generate_temp_var():
        nonlocal temp_var_count
        temp_var = f'T{temp_var_count}'
        temp_var_count += 1
        return temp_var

    for token in expression.split():
        if token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                operator = operators.pop()
                op2 = stack.pop()
                op1 = stack.pop()
                temp_var = generate_temp_var()
                three_address_code.append(f'{temp_var} = {op1} {operator} {op2}')
                stack.append(temp_var)
            operators.pop()  # Remove the opening parenthesis
        elif token in ('+', '-', '*', '/'):
            while operators and operators[-1] in ('+', '-', '*', '/'):
                operator = operators.pop()
                op2 = stack.pop()
                op1 = stack.pop()
                temp_var = generate_temp_var()
                three_address_code.append(f'{temp_var} = {op1} {operator} {op2}')
                stack.append(temp_var)
            operators.append(token)
        else:
            stack.append(token)

    while operators:
        operator = operators.pop()
        op2 = stack.pop()
        op1 = stack.pop()
        temp_var = generate_temp_var()
        three_address_code.append(f'{temp_var} = {op1} {operator} {op2}')
        stack.append(temp_var)

    if len(stack) != 1 or len(operators) != 0:
        raise ValueError("Invalid expression")

    return three_address_code

# Input expression
expression = "-(a * b) + (c + d) - (a + b + c + d)"

# Generate three-address code
result = generate_three_address_code(expression)

# Print the generated three-address code
for statement in result:
    print(statement)