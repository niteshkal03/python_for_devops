#wap to check given how many vowel in a given string.

def check_vowel(name):
    count =0
    for i in name:
        if i in "aeiou":
            count +=1
            # print("this is vowels")
    return count
res = check_vowel("Nitesh")
print(res)    