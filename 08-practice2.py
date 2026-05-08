# 2.wap to take a number from user input and print formated table
# format:
# 3x1=3
# 3x2=6
# ....
# 3x10=30
usr_input = int(input("Enter Your Number: "))
s = 0
for i in range (1,11):
    s = usr_input * i
    print(f"{usr_input} x {i} = {s}")