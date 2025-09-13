print("BANK OF DIPONESS")
pin = int(input("set a new pin \n"))
n_pin = int(input("enter your pin \n"))
while n_pin != pin:
    n_pin = int(input("incorrect pin. enter your pin again \n"))

if n_pin == pin:
    print(" PIN accepted \n")
