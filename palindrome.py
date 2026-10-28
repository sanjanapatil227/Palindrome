
text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
