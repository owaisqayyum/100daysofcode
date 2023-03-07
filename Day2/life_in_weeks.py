#!/usr/bin/env python3
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_age = 90 - int(age)

days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12

print(f"You have {days}, {weeks} weeks, and {months} months left.")
