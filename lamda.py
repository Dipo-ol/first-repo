def squared(num): return num**2
# lambda num : num**2


print(squared(2))
####################


def funcbuilder(x):
    return lambda num: num + x


addten = funcbuilder(10)
add15 = funcbuilder(15)

print(addten(6))
print(add15(6))
