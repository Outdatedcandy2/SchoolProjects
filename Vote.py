age = int(input("Enter Your Age:"))

if age >= 18:
    print("You Are Eligible To Vote")
elif age < 18 :
    yea = 18 - age
    print("Sorry You Are Not Eligible To Vote.")
    print(f"You Will Be Eligible To Vote In {yea} Years")    
else:
    print("error")    