#wap is function in python

# def newfun():
#     {

#     print("Hello World")
# }

# newfun()



#function define
# def add():
#     a = 21
#     b= 20
#     c=a+b
#     print(c)
# add()


# parameters(para) and argument(args)
# positional parameter/arguments
#Default parameter

#use for reusable
# def newadd(a,b): #parameters
#     c=a+b
#     print(c)
# newadd(10,20) #arguments


def table_print(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
table_print(2)

# if we pass default value is 0 then it will give ouput 0 if we not assign argumnets.
#its use to avoid errors if we not pass anything in argumnets.
def newadd(a=0,b=0): #paramters
     c=a+b
     print(c)
newadd(10,20) #arguments