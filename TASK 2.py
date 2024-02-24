
## CALCULATOR##
##TASK 2##



# 1.ADD
# 2.SUB
# 3.MULTIPLY
# 4.DIVIDE



print("Select an operation to perform:")
print("1.ADD")
print("2.SUB")
print("3.MULTIPLY")
print("4.DIVIDE")


num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))


operation = input("Enter the operation number:")


if operation=="1":
    print("The Sum is",num1+num2)
elif operation=="2":
    print("The Difference is",num1-num2)
elif operation=="3":
    print("The Multiply is",num1*num2)
elif operation=="4":
    print("The Division is",num1/num2)
else:
    print("INVALID NUMBER...TRY AGAIN...!!!!!")
