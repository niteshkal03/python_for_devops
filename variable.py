n=10
print(id(n)) #variable location id print
#Addition 
num1=20
num2=30
total= num1+num2
print(f"Addition: {num1} + {num2} = {total}") # use f string for formatting
print(num1, "+", num2, "=", total) #its not good practice.

#Multiplication
multi = num1 * num2
print(f"Multiplication: {num1} * {num2} = {multi}")

#Dividation
a = 3
b = 13
divide = b // a
print(f"{b} // {a} = {divide}")

power=10**2 #we use ** for define power of any value
print(f"{power}")

#Input method
#we gave int means its a type casting. if we not use int then output will be come in string
val1=int(input("Enter Your Number1: "))
val2=int(input("Enter Your Number2: "))
result = val1 + val2
print(result)