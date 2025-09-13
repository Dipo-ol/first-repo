import csv
with open('Bestseller.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    next(reader)
    max_seller = float('-inf')
    best_seller = None

    for row in reader:
        current_sales = float(row[4])
        if current_sales > max_seller:
            max_seller = current_sales
            best_seller = row

print(best_seller)
with open('best_seller.csv', 'w', newline='', encoding='utf8') as best:
    writer = csv.writer(best)
    writer.writerow(best_seller)
