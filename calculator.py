a = float(input('Enter a number 1: '))
b = input('Enter a operator: ')
c = float(input('Enter a number 2: '))
if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '**':
    print(a ** c)
elif b == '/' and c != 0:
    print(a / c)
elif b == '//' and c != 0:
    print(a // c)
elif b == '%' and c != 0:
    print(a % c)
elif b == '/' or b == '//' or b == '%' and c == 0:
    print("Division by zero!")
else:
    print("Unknown operator! Available operators: '+','-','*','/','//','%','**'")

