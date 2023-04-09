"""
ASSIGNMENT 1: Convert Roman numerals to integer
"""
roman = input("Enter Roman numeral: ")
roman = roman.upper()

d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

total = 0   
for i in range(len(roman)):
    if (i+1 != len(roman) and d[roman[i]] < d[roman[i+1]]):
        total -= d[roman[i]]
    else:
        total += d[roman[i]]

print(f"Numerical value of {roman} is {total}")
