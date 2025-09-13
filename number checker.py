even = 0
odd = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        even += 1
    else:
        odd += 1
        continue
print(f"we have {even} even numbers and {odd} odd numbers")
