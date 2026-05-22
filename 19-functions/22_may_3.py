# wap to return sum of strings indexes
def strlen(a):
    s=0
    for i in range(len(a)):
        s=s+i
    return s
res = strlen("python")
print(res)
