a = int(input())
b = input()
c = int(input())
if b =='/' and c == 0:
    print ("Division by zero!")
elif b =='+':
    print (a + c)
elif b == '-':
    print (a - c)
elif b == '*':
    print (a * c)
elif b != '/' and c != 0:
    print (a / c)
