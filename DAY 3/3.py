num1=int(input("enter number 1:"))
operation = input("Enter operation (+, -, *, /): ")
num2=int(input("enter number 2:"))

if operation=="+":
    Result=num1+num2
    print("Result=",Result)

elif operation=="-":
    Result=num1-num2
    print("Result=",Result)

elif operation=="*":
    Result=num1*num2
    print("Result=",Result)

elif operation=="/":
    Result=num1/num2
    print("Result=",Result)

else:
    print("invalid")