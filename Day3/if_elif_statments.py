#!/usr/bin/env python3

height = int(input("Whats your height? "))

if height > 120:
    age = int(input("Whats your age? "))
    if age > 18 :
        print("ticket price is 12$")
    else:
        print("ticket price is 7$")
else:
    print("better luck next time")
