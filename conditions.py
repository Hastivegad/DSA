#condition

#1. Check whether a number is positive, negative, or zero
num = 5

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


#2. Check whether a person is eligible to vote
age = 10

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#3. Find the largest of 3 numbers
a = 10
b = 45
c = 15

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


#4. Check whether a year is a leap year
year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


#5. Create a grade system based on marks
marks = 85

if marks >= 70:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")


#6. Check whether a number is divisible by 5 and 11
num = 55

if num % 5 == 0 and num % 11 == 0:
    print("Number is not divisible by both 6 and 12")
else:
    print("Number is  divisible by both 5 and 11")


#7. Create a simple calculator using if-elif-else
a = 20
b = 5
operator = "+"

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")    
