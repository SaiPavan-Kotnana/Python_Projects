#input a list of student scores
student_scores=input().split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
highest_score=0
for score in student_scores:
    if score > student_scores:
        highest_score=score#print(highest_score)
print(f"the highest score in the class is:{highest_score}")