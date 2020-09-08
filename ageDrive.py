# Program to enter age and check if one is eligible to drive or not

age = int(input("Enter Your Age : "))

"""This code just works.
	   Thank You"""
if age > 7 and age <=100:
	if age > 18 :
		print("You can Drive.")
	elif age == 18:
		print("We cannot say that you can drive.")
	else:
		print("You can not drive.")
else:
	print("Invalid Age")

# print(__doc__)

