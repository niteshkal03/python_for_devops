# wap to check number completely divide by 2 and 3 and return
"yes number is completly divide"
"No number is not completely"
def check_num(a):
    # return "yes number is completly divide"
    if a%2 == 0 and a%3==0:
        return "yes number is completly divide"
    else:
        return "No number is not completely"

res = check_num(15)
print(res)