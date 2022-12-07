x = int(input("Enter First Number:"))
y = int(input("Enter Second Number:"))
z = int(input("Enter Third Number:"))

if x > y and x > z :
    print(f"{x} is greater than {y} and {z}")
elif y > x and y > z :
    print(f"{y} is greater than {x} and {z}")
elif z > x and z > y :
    print(f"{z} is greater than {x} and {y}")        
else:
    print("Are All Equal")    

