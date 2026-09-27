num1=int(input("enter no1 :"))
num2=int(input("enter no2 :"))
operator=input("Enter your choice +,-,*,/ ")

if operator=="+":
    print(num1 +num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1 * num2)
elif operator =="/":
    print(num1/num2)
else:
    print("invalid operator")
