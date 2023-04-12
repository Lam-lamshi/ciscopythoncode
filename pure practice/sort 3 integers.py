a=int(input("Enter the  first number "))
b=int(input("Enter the second term "))
c=int(input("Enter the third term "))

mn=min(a,b,c)
mx=max(a,b,c)
md=a+b+c-mn-mx
print("the number in sorted order: ")
print("",mn)
print("" , md )
print("",mx)
