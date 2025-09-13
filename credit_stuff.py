height = int(input("How tall are you (in m)?:"))
credits = int(input("How many credits do you have?: "))
if height >= 137 and credits >= 10:
    print("Enjoy the ride")
elif height >= 137 and credits < 10:
    print("you dont have enough credits")
elif height < 137 and credits >= 10:
    print(" you're not tall enough")
else:
    print("you don't meet the criteria")
