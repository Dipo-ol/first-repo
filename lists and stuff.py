# a_list = ["hi", 1, 2, "yo"]
# a_list.append("hey")
# # for i in a_list:
# #     print(i)
# a_list.pop(3)
# # for i in a_list:
# #     print(i)
# a_list.remove(1)
# # for i in a_list:
# #     print(i)
# a_list.reverse()
# print(a_list)

# yo = [1, 4, 56, 7, 8]
# yo.sort()
# print(yo)
# print((help(yo)))

# tup = (1, 2, 3, 4)
# for i in tup:
#     print(i)
# a_dict = {
#     "dipo": "boy",
#     "mary": "girl"
# }
# print(a_dict)
# print(a_dict.get(""))
# a_dict.update({"jon": "boy"})
# print(a_dict)
# a_dict.update({"mary": "transformer"})
# # a_dict.pop("mary")
# # a_dict.popitem()
# keys = a_dict.keys()
# print(a_dict)
# print(keys)
# for key in a_dict.keys():  # since we have a variable for keys, this can be used because it returns a value
#     print(key)
# values = a_dict.values()
# print(values)
# items = a_dict.items()
# print(items)
# for key, value in a_dict.items():
#     print(f"{key}:{value}")

# 2d lists
td_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(td_list[1][2])
for list in td_list:
    for r_list in list:
        print(r_list)
num = 15//2
print()
