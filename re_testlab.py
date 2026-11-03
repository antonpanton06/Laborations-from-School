import re
YOUR_PATTERN = r"[a-zA-Z0-9._-]+@[A-Za-z0-9]+\.[a-z]{2,}"
pattern = YOUR_PATTERN

user_input = input("Your email adress: ")
if (re.fullmatch(pattern, user_input)):
    print("Valid email!")

else:
    print("Invalid email!")