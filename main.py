a = int(input())
b = int(input())
2
opr = input()
 
if opr in '+-*/':
    if opr == '+':
        print(a + b)
    elif opr == '-':
        print(a - b)
    elif opr == '*':
        print(a * b)
    else:
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / b)
else:
    print('Неверная операция')