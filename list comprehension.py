numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
# even/odd printer
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0]
print(f"even no: {even_num}")
print(f'odd no: {odd_num}')
