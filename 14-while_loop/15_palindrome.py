#wap to check the give string by user is "palindrome" or "not palindrome"
text = "Nitesh"
copy_text = text
rev=""
i = len(text)-1

while i >= 0:
    rev = rev + text[i]
    i -=1
if copy_text ==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
