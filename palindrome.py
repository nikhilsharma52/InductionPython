text = input("Enter a string: ")

r_text = text[::-1]

print("Reversed string:", r_text)

if text == r_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
