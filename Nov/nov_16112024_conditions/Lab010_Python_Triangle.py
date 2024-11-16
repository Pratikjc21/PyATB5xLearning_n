S1=int(input("Enter the value of S1 of Triangle:"))
S2=int(input("Enter the value of S2 of Triangle:"))
S3=int(input("Enter the value of S3 of Triangle:"))

if S1==S2 and S2==S3:
    print("Its an Equilateral Triangle")
elif S1==S2 and S2!=S3:
    print("Its an Soscele Triangle")
else:
    print("Its an Scalene Triangle")