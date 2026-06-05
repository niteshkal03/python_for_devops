# 4.Wap to find the count of how many int value and how many str in the list 
# : [70,"aman",50,10,20,"rohan","iq-india"].
my_list = [70,"aman",50,10,20,"rohan","iq-india"]
count=0
count1=0
for i in my_list:
    if type(i)==int:
        count+=1
    else:
        count1+=1
print(f"integer is : {count}")
print(f"strings are : {count1}")

