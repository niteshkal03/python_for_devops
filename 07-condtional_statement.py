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