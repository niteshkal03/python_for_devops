# 3.Wap to find the sum of only odd elments in the list : [10,3,4,6,22,31,33,55,40].
my_list = [10,3,4,6,22,31,33,55,40]
total=0
for i in my_list:
    if i%2!=0:
        total=total+i
print(f"Sum of Odd Numbers : {total}")