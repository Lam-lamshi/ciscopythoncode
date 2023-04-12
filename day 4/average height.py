student_height=input("input a list of student height : ").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)

total_height=0
for height in student_height:
    total_height+=height
print(total_height)
total_lenght=0
for lenght in student_height:
    total_lenght+=1
print(total_lenght)
AVG= round(total_lenght/total_height)
print(f"The total average of student is {AVG} ")
