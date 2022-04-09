num1 = input("enter first number: ")
op = input("enter operand: ")
num2 = input("enter 2nd number: ")
if op == "+":
    print(float(num1) + float(num2))
elif op == "-":
    print(float(num1) - float(num2))
elif op == "/":
    print(float(num1) / float(num2))
elif op == "*":
    print(float(num1) * float(num2))
else:
    print("invalid Operand")    
