# diary = open('diary.txt', 'w')
# diary.write("hi diary, i'm dipo\n")
# diary.write("i'm new here")

content = open('diary.txt', 'r')
# print(content.read())
# content.close
line1 = content.readline()
print(line1, end='')
line2 = content.readline()
print(line2, end='')
