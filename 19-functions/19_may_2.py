def sub(a=0,b=0):
    print(f"Substraction is : {a-b}")
 
def mul(a=0,b=0):
    print(f"Multiplication is : {a*b}")
def div(a=0,b=0):
    print(f"Division is : {a /b}")

num1 = 20
num2 = 10

opt = input("Enter Your Options (+,-,*,/) : ")
if opt == "-":
    sub(num1, num2)
elif opt == "*":
    mul(num1, num2)
elif opt == "/":
    div(num1 / num2)
else:
    print("Please Enter Valid ")