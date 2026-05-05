# Membership Operator
# its check sequence if its match the will true
#its not work on numbers, only work on strings
#this operator work on (not, in)
# str1 = "this is python for devops"
# find = "this"
# print("this" in str1)

# num1 = "3434" #no working on integer value
# print("4" in num1)

# find = "3" and "6" # its jump on last value 
# print(find in num1)

email="iqindia123@gmail.com"
find = "@gmail.com"
if find in email:
# if "@gmail.com" in email:
    print("Valid")
else:
    print("Invalid")


min_age = 18
nationality = "Indian"
user_age = int(input("Enter Your Age: "))
user_id = input("Enter Your Nationality: ")

if user_age >= min_age and user_id == nationality:
    print("Your Are Eligible for Voting")

else:
    print("Your Are Not Eligible for Voting")


# Class 4.20 Class

# Wsl Ubuntu
# commands: 
# sudo apt update #superuser do means admin
# apt-get means advanced package tool use for refresh libraries and package
# sudo apt upgrade command use for upgrade new versions of libraries or new changes upgrade
# Study about Linux