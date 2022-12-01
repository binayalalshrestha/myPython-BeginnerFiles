# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 - 100 -> Excellent
# 80 - 90 -> A
# 70 - 80 -> B
# 60 - 70 -> C
# 50 - 60 -> D
# <50 -> F

marks = int(input("Enter your marks: \n"))

if marks>=90:
    grade = "Excellent"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "F"
print("\n")
print ("your grade is " + grade)
print("\n")


# Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter post here: \n")

if "harry" in post:
    print("Post contains word Harry")
else:
    print("Post does not contain word Harry")
