student_name = input("Enter Your Name: ")
pre_marks = int(input(f"Enter Your Marks : "))

if pre_marks >= 400:
    print("You Are Eligible for Mains !!")

    mains = int(input("Enter Your Mains Marks : "))
    if mains >= 600:
        print("You Are Eligible for Interview !!")

        interview = int(input("Enter Your Interview Marks : "))
        if interview >= 700:
            print(f"Congratulations {student_name} !! 💐💐💐, You Are Eligible For IAS Service !!")
        else:
            print("Oops, You Are Failed in Interview.")
    else:
        print("You Are Failed in Mains ❌")
else:
    print(f"Better Luck Next Time, {student_name} You are Failed ❌")

#we use conditional statment for making intelligence the programe.
    #in condtional statment 0 means false 
    #x =0
    # if a:
    #     means false
    # a = ""--- no space meanse 0 means False
    # but a " " ---space in quotes so count 1 == true

    # a = True
    # b = True
    # print(a + b) answer 2

    # a = True
    # b = False 
    # print(a*b) means 0 


    # else is work only just above if line 

    # true or false 
    # if ----non terminated-----check all true condtion 
    # elif ---terminated process ----- if true then terminate

# nested if else:
# -means conditions into condtions 