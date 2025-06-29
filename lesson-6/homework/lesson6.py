
#1. Modify String with Underscores
string = 'assalomll'
new_string = ''
char = 1
vowel = 'aouie'
for i in string:
    if (not char % 3) and (i.lower() not in vowel) and (char < len(string)):
        new_string += i + '_'
    else:
        new_string += i
    char += 1
print(new_string)
#2. Integer Squares Exercise
while True:
    n = int(input('Input a number: '))
    if 1 <= n <= 20:
        break
    else:
        print('Input a number between 1 and 20')
for i in range(n):
    print(i**2)
#3 Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1
#Exercise 2: Print the following pattern
n = 5
for i in range(1, n+1):
    
    for j in range(1, i+1):
        print(j, end = ' ')

    print(end ='\n')
#Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input('Enter a number: '))
s = 0
for i in range(1, n+1):
    s += i
print(f'Sum is: {s}')
#Exercise 4: Print multiplication table of a given number
n = int(input('Enter a number: '))
for i in range(1, 11):
    print(n*i)
#Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    print(x)
#Exercise 6: Count the total number of digits in a number
numbers = 75869
num = str(numbers)
counter = 0
for i in num:
    counter += 1
print(counter)
#Exercise 7: Print reverse number pattern
n = 5
for i in range(n):
    for j in range(n, 0, -1):
        print(j, end = ' ')

    print(end ='\n')
    n -= 1
#Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list1.reverse()
for x in list1:
    print(x)
#Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)
#Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
print('Done!')
#Exercise 11: Print all prime numbers within a range
n = range(25, 51)
divisor = 0
for i in n:
    for j in range(2,i):
        if i % j == 0:
            divisor += 1
    if divisor == 0:
        print(i)
    divisor = 0
#Exercise 12: Display Fibonacci series up to 10 terms
fb1 = 0
fb2 = 1
steps = 1
lst = [fb1, fb2]
while steps < 9 :
    fb3 = fb1 + fb2
    lst.append(fb3)
    fb1, fb2 = fb2, fb3
    steps += 1
for i in lst:
    print(i)
#Exercise 13: Find the factorial of a given number
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f'5! = {factorial}')
#4. Return Uncommon Elements of Lists
def uncommon(list1, list2):
    for i in list1:
        if i not in list2:
            new_list.append(i)
    for j in list2:
        if j not in list1:
            new_list.append(j)
    print(new_list)
new_list.clear()
uncommon(list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5])
