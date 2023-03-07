#!/usr/bin/env python3

print("hello"[0]) # first character
print("hello"[4]) # last character
print("1234" + "12345") # strint concat
print(123_123_123) # equals to print(123123123)

# type error
num_char = len(input("What is your name? "))

# type casting
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

# math
#** means power
2 ** 2

# rounding the values
round(8/3, 2) # round the answer of 8/3 to 2 decimal places.
# 2.67

8 // 2 # flow condition, we get int straight away

i = i + 1 # increment
i += 1

# f-string
f"your score is {i}"
