# wap to check character pass by user is vowel or consonant
def letter(char):
    if char in "aeiou":
        print("It is Vowels")
    else:
        print("It is Consonant")


usr_input = input("enter your char : ")

letter(usr_input)
 
        