import csv
data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]
try:
    with open('packing_list.csv', 'r', newline='', encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("packing list not found, create a new one")
    with open('packing_list.csv', 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
