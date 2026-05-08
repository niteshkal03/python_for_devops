# Loops in Python
# 1.for loop: range based
# 2.while loop: condtion based


# 1. FOR LOOP
# range(start, stop, step) (0, 10, 1)
# range alwsay works with integer
for i in range(10): #underscore use for run the loop 
    # if i%2 != 0 #it print opposite of 
    # print(i, end = " ") #end will give you horizontally output
        print(i, end = " ")
        print("python", end= " ") #end use for horizontally
    # if i == 10:
    #     continue # use for skip 10
    #     break # for terminate loop
    # print(i)

s=0
for i in range (1,5):
    s = s+1
    print(s) #print continuously 
print(s) #total answer will print