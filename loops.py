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
# num = int(input("Enter a number : "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10
    
# print(sum)


 
# 16. Reverse Number
# User se ek number lo aur uska reverse nikalo.
# Example: 12345 → 54321
# Answer:
# num = 5678
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
    
# print(rev)

# 17. Even & Odd Count
# 1 se 100 tak kitne even aur kitne odd numbers hain, count karo.
# Answer:
# even_count = 0
# odd_count = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         even_count +=1 
#     else:
#         odd_count += 1
#     i +=1
    
# print(f"even numbers : {even_count}")
# print(f"odd numbers : {odd_count}")



# 18. Sum of Squares
# User se n lo aur:
# 1² + 2² + 3² + ... + n²
# ka result nikalo.
# Answer:
# num = int(input("Enter a number : "))
# sum = 0

# for i in range(1,num +1):
#     sum = sum + i * i
    
# print(sum)


# 19. Divisible by 3 and 5
# 1 se 100 tak woh numbers print karo jo 3 aur 5 dono se divisible hain.
# Answer:

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1
    

 
# 20. Fibonacci Series
# User se n lo aur Fibonacci series ke first n terms print karo.
# Example:
# 0 1 1 2 3 5 8 13...
# Answer:
# num = int(input("Enter a number : "))
# i = 1
# a = 0
# b = 1
# while i <= num:
#     print(a,end=" ") 
#     c = a + b
#     a = b
#     b = c
#     i +=1
 
 
# 🟠 Level 3 — Nested for Loop
# 21. Star Pattern
# *
# **
# ***
# ****
# *****
# Answer:

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
    
 
# 22. Reverse Star Pattern
# *****
# ****
# ***
# **
# *
# Answer:
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end="")
#     print()
 
# 23. Number Pattern
# 1
# 12
# 123
# 1234
# 12345
# Answer:
# for i in range(1,6):
#     for j in range(i):
#         print(j +1,end="")
#     print()
 
# 24. Repeated Number Pattern
# 1
# 22
# 333
# 4444
# 55555
# Answer:
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()
 
# 25. Multiple Tables
# 1 se 5 tak multiplication tables ek saath print karo.
# Answer:
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")
 
# 26. Square Pattern
# *****
# *****
# *****
# *****
# *****
# Answer:

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print()
 
# 27. Number Grid
# 12345
# 12345
# 12345
# 12345
# 12345
# Answer:
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()
 

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