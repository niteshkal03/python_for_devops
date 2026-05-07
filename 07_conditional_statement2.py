# WAP to check if a single character is a vowel or not.
vowels ="aeiou"

letters = input("Enter Your Letter : ")

#len() is used for count the number of letters or space and lstrip() use for remove space count
letter_len = len(letters.lstrip())

if letters:
    if letter_len == 1:
        if letters.lower().lstrip() in vowels:           #Lower(): Uppercase letter converts into lower case
            print(f"Yes, {letters} is vowels")
        else:
            print(f"{letters} is Not vowels")
else:
    print("Please Enter Letter first")
