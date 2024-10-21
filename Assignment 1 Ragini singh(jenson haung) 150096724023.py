
# Q1. WAP to check whether a number is even or odd.

# %%
num=int(input("Enter the number : "))
if num %2 ==0:
    print("The number is even")
else:
    print("The number is odd")    

# %% [markdown]
# Q2. WAP to check whether person is eligible for voting.

# %%
age=int(input("Enter your age: "))
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")    

# %% [markdown]
# Q3. WAP to enter a number between 1 to 7 as days of a week and print the day
# accordingly. (Monday, Tuesday ...) using if elif case.

# %%
day=int(input("Enter the number"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")   
elif day==3:
    print("Wednesday")   
elif day==4:
    print("Thursday")   
elif day==5:
    print("Friday")   
elif day==6:
    print("Saturday")   
elif day==7:
    print("Sunday")
else:
    print("The number enter is invalid") 

# %% [markdown]
# Q4. WAP to enter a number between 1 to 7 as days of a week and print the day
# accordingly. (Monday, Tuesday ...) using match case.

# %%
day=int(input("Enter the number between (1 to 7)"))
match day:
     case 1:
       print("Monday")
     case 2:
       print("Tuesday")
     case 3:
       print("Wednesday")  
     case 4:
      print("Thursday")      
     case 5:
        print("Friday")  
     case 6:
        print("Saturday") 
     case 7:
        print("Sunday")
     case _:
        print("The number enter is not between the (1 to 7)") 
        

# %% [markdown]
# Q5. WAP to check whether a year is a leap year or not. A year is a leap year if “any
# one of ” the following conditions are satisfied:
# • The year is multiple of 400.
# • The year is a multiple of 4 and not a multiple of 100

# %%
year=int(input("Enter the year : "))
if (year  %400 ==0 ) or (year %4 ==0  and year %100 !=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")    

# %% [markdown]
# Q6. WAP to calculate to take in the marks of 5 subjects, compute average and display
# the grade as per following rules:
# • average >= 90 : “A"
# • average >= 80 : “B"
# • average >= 70 : “C"
# • average >= 60 : “D”

# %%
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for  subjects {i+1}:"))
    marks.append(mark)

average = sum(marks)/5
print("The average marks obtained is:",average)

if average>=90:
    print("The grade obtained is A")
elif average>=80:
    print("The grade obtained is B")    
elif average>=70:
    print("The grade obtained is C")    
elif average>=60:
    print("The grade obtained is D")    
else :
    print("The student is falied in exam!!")

# %% [markdown]
# Q7. WAP to input a character . Check whether the charecter is vowel or consonant

# %%
character= input("Enter a chracter: ")

if len(character) == 1:
    character= character.lower()
    if character in 'a e i o u':
        print("The character is a vowel.")
    else: 
        print("The character is a consonant.")
else:
    print("PLease enter a single character ")

# %% [markdown]
# Q8. WAP to search an element in a list [use for: else clause]

# %%
list= [10,20,30,40,50,60,70,80,90,100]

search_element=int(input("Enter the element to search: "))

for item in list:
    if item== search_element:
        print(f"Element {search_element} found in the list.") 
        break
else :
     print(f"Element {search_element} not found in the list")

# %% [markdown]
# Q9. Write a program to take a single digit number from the key board and print its
# spelling in English word using if elif.

# %%
digit = int(input("Enter a single-digit number (0 to 9): "))

if digit == 0:
    print("Zero")
elif digit==1:
    print("One")
elif digit==2:
    print("Two")
elif digit==3:
    print("Three")
elif digit==4:
    print("Four")
elif digit==5:
    print("Five")
elif digit==6:
    print("Six")
elif digit==7:
    print("Seven")
elif digit==8:
    print("Eight")
elif digit==9:
    print("Nine")
else:
    print("The enter number is not between the (0-9.)")

# %% [markdown]
# Q10. WAP to input three numbers and arrange them in ascending numbers.

# %%
num1=float(input("Enter the frist number: "))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the thrid number:"))

numbers = [num1 ,num2 ,num3]
numbers.sort()
print("Number in ascending order:",numbers)

# %% [markdown]
# Q11. Write a program to take a single digit number from the key board and print its
# spelling in English word using match case

# %%
digit=int(input("Enter the single digir number between (0-9):"))

match digit:

    case 0:
        print("Zero")
    case 1:
        print("One")   
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")  
    case 5:
        print("Five")
    case 6:
        print("Six") 
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _:
        print("The number is not between the (0-9).")

# %% [markdown]
# Q.12 WAP to read two numbers and arithmetic operator [+,-,*,/,%] perform the
# operation and display the computed result. [Hint: use elif statement]

# %%
num1= float(input("Enter the Frist number:"))
num2= float(input("Enter the second number:"))

operator = input("Enter an operator ")

if operator== '+' :
    answer= num1+num2
    print(f"The answer is {num1} + {num2}= {answer}" )
elif operator =='-':
     answer= num1-num2
     print(f"The answer is {num1} - {num2}= {answer}" )
     
elif operator =='*':
     answer= num1*num2
     print(f"The answer is {num1} * {num2}= {answer}" )
elif operator =='/':
     answer= num1/num2
     print(f"The answer is {num1} / {num2}= {answer}" )
elif operator =='%':
     answer= num1%num2
     print(f"The answer is {num1} % {num2}= {answer}" )

# %% [markdown]
# Q.13 WAP to check whether a inputted character is uppercase or lowercase or digit or
# any other character.

# %%
char = input("Enter a character")
if len(char) !=1:
    print("Please enter only one character.")
else :
    if char.isupper():
        print("The character is uppercase.")  
    elif char.islower():
        print("The character is lowercase.") 
    elif char.isdigit():
        print("The character is digit.")   
    else: 
        print("The character is neither uppercase,lowercase , nor a digit.")  


# %% [markdown]
# Q14. Develop a number guessing game using loops and conditional statements. Ask
# user to guess a secret number. If user has not guessed correct number, provide
# him/her hint.

# %%
import random

secret_number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I ahev chossen a secret number between 1 and 100")
print("Try to guess it!")

while True:
    guess = input("Enter the guess:")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue 

    guess = int(guess)  

    if guess < secret_number:
        print("Too low ! Try again")  
    elif guess > secret_number:
        print("too high! Try again.")
    else:
        print("Congratulation! You've guessed the secret number!")    
        break

# %% [markdown]
# Q16. WAP to display numbers from 15 to 1 in descending order.

# %%
for num in range (15,0,-1):
    print(num, end=' ')

# %% [markdown]
# Q17. WAP to display sum of numbers from 11 to 200 using for loop.

# %%
total_sum = 0

for number in range(11 ,201):
    total_sum  += number 
print("The sum of number from 11 to 200 is: ", total_sum)

# %% [markdown]
# Q18. WAP to display average of numbers from 5to 15 and 21 to 60.

# %%
sum =0 
count=0

for num in range (5,16):
    total_sum += num 
    count += 1

for num in range (21,60):
    total_sum +=num
    count += 1

average = total_sum/count

print("The average of number from 5 to 15 and 21 to 60 is:",average)

# %% [markdown]
# Q19. WAP to display odd numbers from 5 to 30.

# %%
5
7
9
11
13
15
17
19
21
23
25
27
29

# %% [markdown]
# Q20. WAP to find factorial of a number inputted by the user.

# %%
num = int(input("Enter a non-negative integer:"))

if num <0:
    print("Factorial is not defined for negative number")
else :
    factorial=1
    for i in range (1,num +1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

# %% [markdown]
# Q21. WAP to find sum of digits of a int number.

# %%
def sum_of_digit(n):
    sum=0
    while n>0:
        digit = n % 10
        sum += digit
        n //=10


# %% [markdown]
# Q22. WAP to display sum of even numbers between 30 and 50.

# %%
print(sum(range(30,51,2)))

# %% [markdown]
# Q23. WAP to print multiplication table.

# %%
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

# %% [markdown]
# Q24. WAP to print the following patterns: 
#     1
#     2 2
#     3 3 3
#     4 4 4 4

# %%
for i in range(1,5):
    print(((str(i)) + ' ' ) * i)

# %% [markdown]
# Q.25 WAP to print pattern:
#    *
#    * *
#    * * *
#    * * * *
#    * * *
#    * *
#    *

# %%
for i in range(1,5):
    print('* ' *i)

for i in range (3,0,-1):
    print('* '  *i)

# %% [markdown]
# Q.26 WAP to print pattern:
#    A
#    B B
#    C C C 

# %%
for i in range (1,4):
     print((chr(65 + i -1) + ' ' ) * i)

# %% [markdown]
# Q.27 Write a program to find whether given number is an Armstrong Number
# Hint:
# Given a number x, determine whether the given number is Armstrong number
# or not. A positive integer of n digits is called an Armstrong number of order
# n (order is number of digits) if.
# abcd = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n)
# Ex:
# 153 is an Armstrong number.
# 
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# %%
num= int(input("Enter a number"))

if num == sum(int(digit) ** len(str(num)) for digit in str(num)):
    print(num,"is the Armstrong number.")
else:
    print(num,"is not a Armstrong number.")

# %% [markdown]
# Q28. WAP to generate the Fibonacci series up to n terms. 
# Hint:
# Fibonacci series: 0 1 1 2 3 5 8
# Formulae: Fn = Fn-1 + Fn-2
# with seed values : F0 = 0 and F1 = 1.
# 
# f1=0, f2=1,
# f3=f1+f2,
# f4=f3+f2
# f5=f4+f3 ....

# %%
n = int(input("Enter the number of terms:"))

f1,f2= 0,1
print("Fibonacci Series: ")
for i in range(n):
    if i==0:
        print(f1,end=' ')
    elif i == 1:
        print(f2, end=' ')
    else:
        f3 = f1 + f2 
        print(f3 , end=' ')
        f1,f2 = f2,f3

# %% [markdown]
# Q29. Write a program that check whether a number is prime number or not.

# %%
num= int(input("Enter the number: "))

prime_num = True 
for i in range(2,num):
    if num %1 ==0:
        prime_num= False
        break

if prime_num:
    print(f"{num} is a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not primt number.")

# %% [markdown]
# Q30. WAP to calculate sum and average of a given array: arr=(‘i’,[1,2,3,4,5])

# %%
arr= ('i' , [1,2,3,4,5,])

num= arr[1]

total_sum = sum(num)
average= total_sum/len(num)

print(f"Sum: {total_sum}")
print(f"Average:{average}")

# %% [markdown]
# Q31. Write the program to reverse the order of the items in the array

# %%
arr= ('i', [1,2,3,4,5,6,7,8])

num=arr[1]

reversed_num= num[::-1]
print("Original array:", num)
print("Reversed array:", reversed_num)

# %% [markdown]
# Q32. Write the program to remove duplicate elements in a given arrat of intergers.

# %%
arr=  [1,2,3,4,5,5,6,6,4,6]
unique_num= list(set(arr))

print("Original number:" ,arr)
print("Array without duplication: ", unique_num)

# %% [markdown]
# Q33.Write a program that takes a string as input and prints it in reverse order.

# %%
input_string= input("Enter a string:")
reversed_string= input_string[::-1]

print("Reversed string:", reversed_string)

# %% [markdown]
# Q34. Write a program that counts the number of vowels in a given string.
# 

# %%
input_string= input("Enter a string:")

vowels = "a e i o u A E I O U"

vowel_count= 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("Number of vowel in the string:", vowel_count)

# %% [markdown]
# Q35. Write a program that checks if a given string is a palindrome (reads the same
# forwards and backwards).

# %%
input_string= input("Enter a string: ")

if input_string == input_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string} is not a palindrome')

# %% [markdown]
# Q36. Write a program that removes duplicate characters from a string.

# %%
input_string= input("Enter  a string: ")
 
output_string= " "

for char in input_string:
    if char not in output_string:
        output_string += char
print("String after removing duplicates: ", output_string)

# %% [markdown]
# Q37. WAP to print even length words in string
# [hint: split() and for loop]

# %%
input_string= "This is sample string  some even length words"

words = input_string.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)

# %% [markdown]
# Q38. WAP to remove spaces from given string:
# “Python is very easy”
# [Hint: use split() and then join()]

# %%
input_string= "Python is very easy"

words= input_string.split()
output_string =''.join(words)

print(output_string)

# %% [markdown]
#  Q39. WAP to convert given list of ASCII value to string. [65, 66, 67, 68, 69]
# [Hint: use chr() to convert ASCII value to character]

# %%
ascii_values= [65,66,67,68,69]

for value in ascii_values:
    print(chr(value), end=' ')

# %% [markdown]
# Q40. WAP to print the individual characters of the string inputted by user in the
# following way
# Example: H—e—l—l—o

# %%
input_string= input("Enter a string: ")
output_string= '-' .join(input_string)
print(output_string)


