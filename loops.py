# Python for Loop — Practice Worksheet
# Name: __________________________
# Date: __________________________
# Instructions
# • Har question ko Python ke for loop ka use karke solve karo.
# • Pehle khud logic banao, phir code likho.
# • Jahan possible ho, range() ka use karo.
 
# 🟢 Level 1 — Beginner
# 1. Numbers Print
# for loop se 1 se 10 tak numbers print karo.
# Answer:
 
# 2. Reverse Numbers
# 10 se 1 tak numbers print karo.
# Answer:
 
# 3. Even Numbers
# 1 se 50 tak saare even numbers print karo.
# Answer:
 
# 4. Odd Numbers
# 1 se 50 tak saare odd numbers print karo.
# Answer:
 
# 5. 1 to n
# User se n input lo aur 1 se n tak numbers print karo.
# Answer:
 
# 6. Sum
# 1 se 100 tak numbers ka sum nikalo.
# Answer:
 
# 7. Squares
# 1 se 10 tak numbers ke squares print karo.
# Answer:
 
# 8. Multiplication Table
# User se ek number lo aur uska multiplication table (1–10) print karo.
# Answer:
 
# 9. Multiples of 7
# 1 se 100 tak 7 ke multiples print karo.
# Answer:
 
# 10. Divisible by 3
# 1 se 100 tak woh numbers print karo jo 3 se divisible hain.
# Answer:
 
 
# 🟡 Level 2 — Intermediate
# 11. Factorial
# User se ek number lo aur for loop se uska factorial calculate karo.
# Answer:
 
# 12. Factors
# User se ek number lo aur uske saare factors print karo.
# Answer:
 
# 13. Prime Number
# User se ek number lo aur check karo ki woh prime number hai ya nahi.

 
# 14. Prime Numbers
# 1 se 100 tak saare prime numbers print karo.
# for num in range(2,101):
#     count = 0
#     for i in range(1,num + 1):
#         if num % i == 0:
#             count+=1
#     if count == 2:
#         print(num)
# 15. Digit Sum
# User se ek number lo aur uske digits ka sum nikalo.
# Example: 583 → 16

 
# 16. Reverse Number
# User se ek number lo aur uska reverse nikalo.
# Example: 12345 → 54321
# Answer:
 
# 17. Even & Odd Count
# 1 se 100 tak kitne even aur kitne odd numbers hain, count karo.
# Answer:
 
# 18. Sum of Squares
# User se n lo aur:
# 1² + 2² + 3² + ... + n²
# ka result nikalo.
# Answer:
 
# 19. Divisible by 3 and 5
# 1 se 100 tak woh numbers print karo jo 3 aur 5 dono se divisible hain.
# Answer:
 
# 20. Fibonacci Series
# User se n lo aur Fibonacci series ke first n terms print karo.
# Example:
# 0 1 1 2 3 5 8 13...
# Answer:
 
 
# 🟠 Level 3 — Nested for Loop
# 21. Star Pattern
# *
# **
# ***
# ****
# *****
# Answer:
 
# 22. Reverse Star Pattern
# *****
# ****
# ***
# **
# *
# Answer:
 
# 23. Number Pattern
# 1
# 12
# 123
# 1234
# 12345
# Answer:
 
# 24. Repeated Number Pattern
# 1
# 22
# 333
# 4444
# 55555
# Answer:
 
# 25. Multiple Tables
# 1 se 5 tak multiplication tables ek saath print karo.
# Answer:
 
# 26. Square Pattern
# *****
# *****
# *****
# *****
# *****
# Answer:
 
# 27. Number Grid
# 12345
# 12345
# 12345
# 12345
# 12345
# Answer:
 
 
# 🔴 Level 4 — Challenge
# 28. Armstrong Numbers
# 1 se 100 ke andar saare Armstrong numbers find karo.
# Answer:

# 29. Perfect Numbers
# 1 se 1000 ke andar saare Perfect numbers find karo.
# Answer:
 
# 30. FizzBuzz
# 1 se 100 tak numbers print karo:
# • 3 se divisible → Fizz
# • 5 se divisible → Buzz
# • 3 aur 5 dono se divisible → FizzBuzz
# • Otherwise → number itself
# Answer:
 
 
# ⭐ Bonus Challenge
# Bina while loop use kiye, sirf for loop se:
# 1 se 1000 tak kaunsa number sabse zyada baar kisi condition ko satisfy karta hai, uska logic khud design karo.
# Answer:
 
 
# 🎯 Goal
# Pehle Level 1 → phir Level 2 → phir Nested Loops → finally Challenge.
# Har question ko khud solve karne ki koshish karo. Agar code nahi ban raha ho, pehle paper par logic/steps likho



# Ek string lo aur for loop ka use karke har character ko alag-alag line me print karo.
# str = input("Enter a string")
# for i in str:
#     print(i)

#
# Ek string me total characters count karo.
# Example: "Hello" → 5
# str = "hello"
# count = 0
# for i in str:
#     count += 1

# print(count)


# Ek string me vowels (a, e, i, o, u) count karo.
# Example: "education" → 5
# name = "eskillsbarwani"
# count = 0
# for i in name:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count +=1
        
# print(count)
        



# Ek string me consonants count karo.
# str = input("Enter a string : ")
# count = 0
# for i in str:
#     if i != "a" and i != "e" and i != "i" and i != "u" and i != "o":
#         count +=1

# print(count)

# Ek string me spaces kitne hain, count karo.

# name = "eskills bar wani"
# count = 0
# for i in name:
#     if i == " ":
#         count += 1
        
# print(count)


# Ek string me a character kitni baar aaya hai, count karo.
# char = "a"
# str = input("Enter a string : ")
# count = 0
# for i in str:
#     if char == i:
#         count +=1

# print(count)

# Ek string me uppercase characters count karo.

# Example: "Hello PYTHON" → 6
# Ek string me digits count karo.
# Example: "Python123" → 3
# for loop ka use karke string ko reverse karo.
# Example: "Python" → "nohtyP"
# Ek string me vowels aur consonants dono count karo aur result print karo.