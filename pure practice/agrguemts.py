user_name=input("please input your name : ")
num_of_input=int(input(user_name + " Enter the number of times you want to do calculation :"))
first_num=int(input("enter the first number :"))
second_num=int(input("enter the second number : "))
for first_num in range(num_of_input):

    def subtractnum(num1, num2):
        print("subtraction = ",num1 - num2)
    subtractnum(first_num,second_num)
    def addnum(num1,num2):
        print("addition = ", num1 + num2)
    addnum (first_num,second_num)
    def multiplynum(num1):
        return num1 * first_num
    results= multiplynum(second_num)
    print("multiplication =", results)
    def divisionnum(num1) :
        return first_num / num1
    results= divisionnum(second_num)
    print("division = ", results)
    def modulenum(num1):
        return first_num % num1
    results=modulenum(second_num)
    print("modulus = ", results)


