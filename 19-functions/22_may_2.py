#wap to count "p" in "python programming" return accuurence.

def find(dest, find1):
    for i in dest:
        count = 0
        if i == "p":
            count +=1
        print(count)
    return count
dest ="python Programming"
find1 ="n"
res = find(dest, find1)