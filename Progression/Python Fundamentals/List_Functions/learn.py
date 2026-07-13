#  Calculator Function

operation = input("Enter the operation to perform")
a = int(input("Enter the number 1 "))
b = int(input("Enter the number 2 "))
def calculate(a, b, operation):
    if(operation.strip().lower()=="add"):
        return a+b
    elif(operation.strip().lower()=="subtract"):
        return a-b
    else:
        return a/b

print(calculate(a,b,operation))

#Even or Odd Checker

a = int(input("Enter the number to check odd or even "))

def check_odd_even(a):
    return "Odd" if a%2==1 else "Even"


print(check_odd_even(a))


#Word Counter

word = input("Enter the words")

def count_the_words(a):
    result = a.strip().split()
    count = 0
    for a in result:
        a = a.strip()
        count=len(a)+count
    return count

print(count_the_words(word))


# Leap Year Checker

year = int(input("Enter the year "))

def is_leap_year(a):
    return a%4==0

print(is_leap_year(year))


#Create a List of First 10 Cubes Using List

i = 1
result = []
while(i<=10):
    result.append(i*i*i)
    i+=1

print(result)

# Extract Only Odd Numbers from a Given List

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for a in list:
    if(a%2==1):
        result.append(a)

print(result)

# Convert a List of Names to Lowercase Using List Comprehension

a = ["John", "ALICE", "BOB"]
result = []

for b in a:
    result.append(b.strip().lower())

print(result)

