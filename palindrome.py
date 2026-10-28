
text = "madam"

reverse_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reverse_text)

if text == reverse_text:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
