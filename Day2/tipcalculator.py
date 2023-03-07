#!/usr/bin/env python3

print("Welcome to the tip caculator.")
bill = float(input("What was the total bill? "))
no_of_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = (bill / no_of_people) * (tip / 10)
bill_per_head = round(total_bill, 2)

print(f"Each person should pay: {bill_per_head}")
