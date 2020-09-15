a = float(input('Enter the first number '))
operator = input('Enter an operator ')
b = float(input('Enter the second number '))

if operator == '+' or operator == 'sum':
    print(a + b)
    print('Well done!')
elif operator == '-' or operator == 'diff':
    print(a - b)
    print('Well done!')
elif operator == '*':
    print(a * b)
    print('Well done!')
elif operator == '/':
    print(a / b)
    print('Well done!')
elif operator == '^' or operator == 'pow' or operator == '**':
    print(a ** b)
    print('Well done!')
elif operator == 'mod' or operator == '%':
    print(a % b)
    print('Well done!')
elif operator == 'div' or operator == '//':
    print(a // b)
    print('Well done!')
else:
    print('You are failed. Please, choose a correct operator.')
    print('Valid operators are +, -, *, /, ^, remainder of the division and integer division.')
