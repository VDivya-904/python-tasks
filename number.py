number = int(input("ENTER A NUMBER: "))
if str(number) == str(number)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
