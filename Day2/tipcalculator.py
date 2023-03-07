#!/usr/bin/env python3

print("Welcome to the tip caculator.")
bill = float(input("What was the total bill? "))
no_of_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = bill + (tip / bill) * 100
bill_per_head = total_bill / no_of_people


print("Each person should pay: %.2f ", bill_per_head)
