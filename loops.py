#loops

#1. Print numbers from 1 to 10 using for loop
for i in range(1, 12):
    print(i)

#2. Print numbers from 10 to 1 using while loop
i = 12

while i >= 1:
    print(i)
    i -= 1
#3. Print the multiplication table of a number
num = 6

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#4. Find the sum of numbers from 1 to n
n = 10
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#5. Find the factorial of a number
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)
