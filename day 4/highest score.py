student_scores=input("input a list of student scores : ").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
maximum_lenghts=0
for lenght in student_scores:
    if lenght >maximum_lenghts:
        maximum_lenghts=lenght
print(f"The highest score in the class is {maximum_lenghts}")
