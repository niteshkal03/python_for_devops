#wap to print the total of even number fromm 1 to 15
a = 1
sum_a =0
while a <= 15:
    if a%2==0:
        print(a)
    a +=1
    sum_a =a + a
    print(sum_a)