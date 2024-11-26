# create a program with sum of three nos
# if user des not input then it will show default value as 100,200 and 300

def Sum(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

Num1 = int(input("Enter 1st no.:\n"))
Num2 = int(input("Enter 2nd no.:\n"))
Num3 = int(input("Enter 3rd no.:\n"))
result = Num1 + Num2 + Num3
print("sum of 3 no. is:", result)
result2= Sum()
print("default sum is:",result2)