# Topic: Arithmetic and Math Functions

import math

x = int(input("Enter the value of X"))
y = int(input("Enter the value of Y"))

print(f"Addition : {x+y}")
print(f"Subtraction : {x-y}")
print(f"Multiplication : {x*y}")
print(f"Division : {x/y}")
print(f"Modulus : {x%y}")
print(f"Floor division : {x//y}")
print(f"Exponentiation : {x**y}")
print(f"Round of Division : {round(x/y)}")
print(f"Factorial of Smaller Number : {math.factorial(x if x<y  else y)}")
print(f"Greatest common divisor (GCD) of the two numbers : {math.gcd(x,y)}")

# Topic: String Comparison

str1 = input("Enter the first word")
str2 = input("Enter the second word")

print(f"{str1 if str1<str2 else str2} will comes first")


# Topic: Conditional Statements

age = int(input("Enter your age"))

if(age < 18):
    print("Minor")
elif((age >=18)&(age<=60)):
    print("Adult")
else:
    print("Senior Citizen")

# Topic:  Conditionals and Arithmetic

amount = int(input("Enter the amount"))

if(amount>=5000):
    discount = amount*(20/100)
    print(f"Discount :{discount}\n"
          f"Final Amount :{amount-discount}")
elif(amount>2000&(amount<5000)):
    discount=(amount*(10/100))
    print(f"Discount :{discount}\n"
          f"Final Amount :{amount-discount}")
else:
    print(amount)

# Topic: Conditionals and Modulo

year = int(input("Enter the year "))

if year%4==0 :
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not leap year.")


# Topic: Conditional Statements

temp = int(input("Enter the temperature "))

if(temp>=30):
    print("Hot")
elif((temp>20)&(temp<30)):
    print("Warm")
else:
    print("Cold")

# Topic: Logical Operators and Conditionals

customer = (input("Enter the customer is loyal in y or n")).lower()=='y'
purchase_amount = int(input("Enter the purchase amount"))

if((customer) or (purchase_amount>=10000)):
    print("Discount applied!")
else:
    print("No Discount applied!")