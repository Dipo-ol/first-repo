# diary = open('diary.txt', 'w')
# diary.write("hi diary, i'm dipo\n")
# diary.write("i'm new here")

# content = open('diary.txt', 'r')
# print(content.read())
# content.close
# line1 = content.readline()
# print(line1, end='')
# line2 = content.readline()
# print(line2, end='')


message = 'hey bitch i\'m here'
with open('message.txt', 'w') as text:
    text.write(message)

unsend = '*this message was deleted*'
with open('message.txt', 'r+') as text:
    og_message = text.read()
    text.seek(0)
    text.truncate(len(unsend))
    text.write(unsend)
print(f"old message: {message}")
print(f"new message: {unsend}")
