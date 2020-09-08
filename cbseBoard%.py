# Program to find persentage acc to the input

print("Enter Marks in 5 subjects accordingly !")

# subjectsNum = str(input("Enter No. of Subjects from 5 to 10 : ")) 

sub1 = int(input("Subject 1 : "))
sub2 = int(input("Subject 2 : "))
sub3 = int(input("Subject 3 : "))
sub4 = int(input("Subject 4 : "))
sub5 = int(input("Subject 5 : "))

totalMarksObtained = sub1 + sub2 + sub3 + sub4 + sub5

print("Total Marks out of 500 : " + str(totalMarksObtained))

totalMarks = int(input("Enter Total Marks Possible : "))
percentage = totalMarksObtained/totalMarks * 100

print("Percentage is : " + str(percentage) + "%")

if percentage >= 90 < 100:
	print("Congratulations you have got A grade !")
elif percentage >= 80 < 90:
	print("You have got B Grade")
elif percentage >= 70 < 80:
	print("You have got C Grade. Need Little improvement")
else:
	print("Better Luck next Time")


