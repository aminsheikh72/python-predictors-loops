# 🟢 Beginner
# 1 se 10 tak numbers print karo using while loop.
# i = 1
# while i <=10:
#     print(i)
#     i +=1
    


# 10 se 1 tak reverse counting print karo.

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# User se n input lo aur 1 se n tak numbers print karo.
# num = int(input("Enter a number : "))
# i =1
# while i <= num:
#     print(i)
#     i += 1


# 1 se 50 tak even numbers print karo.

# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i +=1

# 1 se 50 tak odd numbers print karo.
# num = 1
# while num <= 50:
#     if num % 2 != 0:
#         print(num)
#     num += 1

# User se n lo aur 1 se n tak ka sum calculate karo.

# num = int(input("Enter a number : "))
# sum = 0
# i = 1
# while i<= num:
#     sum += i
#     i +=1
    
# print(sum)

# User se number lo aur uska table (1–10) print karo.

# num = int(input("Enter a number"))
# i = 1
# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i+=1

# User se number lo aur uske digits count karo.
# Example: 58321 → 5 digits

# num = int(input("Enter a number : "))

# count = 0

# while num > 0:
#     count +=1
#     num = num // 10
    
# print(count)

# 🟡 Intermediate
# User se number lo aur uska factorial while loop se nikalo.

# num = int(input("Enter a number : "))
# i = 1
# fact = 1
# while i <= num:
#     fact = fact * i
#     i += 1
    
# print(fact)

# Number ke digits ka sum find karo.
# Example: 1234 → 10
# num = int(input("Enter a number : "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num = num // 10
    
# print(sum)


# Number ko reverse karo.
# Example: 12345 → 54321
# num = 5678
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
    
# print(rev)

# Check karo ki number palindrome hai ya nahi.
# num = 121
# copy = num
# rev = 0
# while copy > 0:
#     digit = copy % 10
#     rev = rev * 10 + digit
#     copy //= 10
    
# if rev == num:
#     print(f"{num} is palindrome number")
# else:
#     print(f"{num} is not a palindrome number")


# Check karo ki number prime hai ya nahi.
# num = int(input("Enter a number : "))
# i = 1
# count = 0
# while i <= num:
#     if num % i == 0:
#         count +=1
#     i +=1
        
# if count == 2:
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not a prime number")

# n terms tak Fibonacci series print karo.

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
    

# User se numbers input lete raho jab tak user 0 enter na kare. End me total sum print karo.
# sum = 0
# while True:
#     num = int(input("Enter a number : "))
#     sum += num
#     if num == 0:
#         break
    
# print(sum)

# User se numbers input lete raho aur positive aur negative numbers ki count batao. 0 par stop karo.
# pos_count = 0
# neg_count = 0
# while True:
#     num = int(input("Enter a number : "))
#     if num > 0:
#         pos_count += 1
#     elif num < 0:
#         neg_count +=1
#     else:
#         break
    
# print(pos_count)
# print(neg_count)

