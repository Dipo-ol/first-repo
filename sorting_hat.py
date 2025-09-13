slyth = 0
huff = 0
raven = 0
griff = 0

ques_1 = int(input("""
    Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk """))
ques_2 = int(input("""
    Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold """))
ques_3 = int(input("""
    Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum"""))

if ques_1 == 1:
    griff += 1
    raven += 1
elif ques_1 == 2:
    huff += 1
    slyth += 1
else:
    print("invalid")

if ques_2 == 1:
    huff += 2
elif ques_2 == 2:
    slyth += 2
elif ques_2 == 3:
    raven += 2
elif ques_2 == 4:
    griff += 2
else:
    print("invalid")

if ques_3 == 1:
    slyth += 4
elif ques_3 == 2:
    huff += 4
elif ques_3 == 3:
    raven += 4
elif ques_3 == 4:
    griff += 4
else:
    print("invalid")
print(griff)
print(slyth)
print(raven)
print(huff)
