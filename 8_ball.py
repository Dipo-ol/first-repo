import random
input("question? ")
ques = random.randint(0, 8)
if ques == 0:
    print("Yes definitely.")
elif ques == 1:
    print(" It is decidedly so.")
elif ques == 2:
    print("Without a doubt. ")
elif ques == 3:
    print("Reply hazy, try again. ")
elif ques == 4:
    print("Ask again later. ")
elif ques == 5:
    print("Better not tell you now. ")
elif ques == 6:
    print("My sources say no. ")
elif ques == 7:
    print("Outlook not so good. ")
else:
    print(" Very doubtful.")
