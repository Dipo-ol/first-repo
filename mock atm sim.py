def withdraw(amount, balance):
    if balance == 0 or amount > balance:
        print('insuffitient funds')
    elif amount < 0:
        print('invalid')
    else:
        balance -= amount
    return balance


def deposit(amount, balance):
    if amount < 0:
        print('invalid')
    else:
        balance += amount
    return balance


balance = 20000
print('welcome to atm sim\n')
while (True):
    print(f'Current balance: {balance}\n')
    operation = int(input('do you want to \n 1.withdraw\n 2.deposit\n'))
    match operation:
        case 1:
            amount = int(input('enter the amount you wish to withdraw\n'))
            print(f'the new balance is {withdraw(amount, balance)}\n')
        case 2:
            amount = int(input('enter the amount you wish to deposit'))
            print(f'the new balance is {deposit(amount, balance)}\n')
    break
