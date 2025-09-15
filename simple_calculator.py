def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def expo(x, y):
    return x**y


print("welcome to the simple calculator")
choice = int(input(""" what operation would you like to do\n 1.) addition\n 2.) subtraction\n 3.) multiplication\n 4.) division\n 5.) power\n (integer only) """))
match choice:
    case 1:
        x = int(input("enter the value of the first integer\n"))
        y = int(input('enter the value of the second integer\n'))
        print(f'the answer is {add(x, y)}')
    case 2:
        x = int(input("enter the value of the first integer\n"))
        y = int(input('enter the value of the second integer\n'))
        print(f'the answer is {sub(x, y)}')
    case 3:
        x = int(input("enter the value of the first integer\n"))
        y = int(input('enter the value of the second integer\n'))
        print(f'the answer is {mul(x, y)}')
    case 4:
        x = int(input("enter the value of the first integer\n"))
        y = int(input('enter the value of the second integer\n'))
        print(f'the answer is {div(x, y)}')
    case 5:
        x = int(input("enter the value of the first integer\n"))
        y = int(input('enter the value of the second integer\n'))
        print(f'the answer is {expo(x, y)}')
