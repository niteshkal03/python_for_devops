# 3.Wap to take a number from user input and print reversed formated table.
# format : 
# 3x10=30
# 3x2=6
# 3x1=3
usr_input = int(input("Enter Your Number: "))
val = 0
for i in range(10,0,-1):
    val = usr_input * i
    print(f"{usr_input} * {i} = {val}")