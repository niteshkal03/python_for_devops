#wap to takes start point and end point user input and print all number divisible by 2 and 3

start_num = int(input("Enter Your First Number: "))
end_num = int(input("Enter Your Last Number: "))

for i in range(start_num, end_num):
    if i%2 == 0 or i%3 == 0:
        print(f"Divisible by 2 and 3:- {i}")
     






