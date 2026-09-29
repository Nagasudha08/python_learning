#Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b:
    if a >= c:
        if a == b == c:
            print("All numbers are equal")
        else:
            print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)


#Marks → Pass and Grade
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 90:
        print("Grade A")
    else:
        if marks >= 75:
            print("Grade B")
        else:
            if marks >= 60:
                print("Grade C")
            else:
                print("Grade D")
else:
    print("Fail")

#Electricity Bill
units = int(input("Enter electricity units: "))
if units >= 0:
    if units <= 100:
        bill = units * 2
        print("Electricity bill:", bill)
    else:
        if units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)
            print("Electricity bill:", bill)
        else:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
            print("Electricity bill:", bill)
else:
    print("Invalid units")

#Leap Year
year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

#Exam Eligibility
attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))
if attendance >= 75:
    if marks >= 40:
        print("Student is eligible to pass")
    else:
        print("Student is not eligible to pass because marks are below 40")
else:
    print("Student is not eligible because attendance is below 75%")