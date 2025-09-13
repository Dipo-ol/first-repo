roman_numeral = input('enter the roman numeral to be converted\n').upper()


def roman_to_int(numeral):
    answer = 0
    if "CM" in numeral:
        answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in roman_numeral:
        answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        answer += 4
        numeral = numeral.replace("IV", "")

    for i in numeral:
        match i:
            case 'M':
                answer += 1000
            case 'D':
                answer += 500
            case 'C':
                answer += 100
            case 'L':
                answer += 50
            case 'X':
                answer += 10
            case 'I':
                answer += 1
    print(f'translates to {answer}')


roman_to_int(roman_numeral)
