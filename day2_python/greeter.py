print("What's your name?")
name = input("Type your name here: ")
if name != str:
	print("Please input your name as a String.")
print("What year were you born? ")
byear = 2026 - int(input("Type your birth year here: "))
if byear != int:
	print("Please input your birth year as an integer.")
print(f"Hello, {name}! You are {byear} years old.")
