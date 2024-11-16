Score=int(input("Enter the Score:\n"))
if Score>=90 and Score<=100:
    print("You are in grade A")
elif Score>=80 and Score<=89:
    print("You are in grade B")
elif Score>=70 and Score<=79:
    print("You are in grade C")
elif Score>=60 and Score<=69:
    print("You are in grade D")
else:
    print("You are in grade F")