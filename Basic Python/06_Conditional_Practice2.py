# Write a program to find out whether a student is pass or fail,
# if it requires total 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter marks for first subject: \n"))
sub2 = int(input("Enter marks for second subject: \n"))
sub3 = int(input("Enter marks for third subject: \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You have failed because you have less than 33 percent in one of the subjects")

elif(sub1+sub2+sub3)/3 <40:
    print("You have failed due to total percentage less than 40")

else:
    print("CONGRATULATIONS !! You have passed the exam !!")

