# Topic: Loops and Modulo

i = 1

while(i<=50):
    if(i%2==0):
        print(i)
    i+=1

# Topic: Loops and Prime Logic

for i in range(10,30,1):
    if(i%2==1):
        print(i)

# Topic: Nested Loops

n= 5
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(f"{i}*{j}={i*j}")
        j+=1
    i+=1

# Topic: Loops and String Iteration

str = input("Enter the string ").strip()
i = 0

for a in str:
    i+=1

print(i)

# Topic: String Manipulation and Loops

str = input("Enter the String ").strip()
result = ""
for a in str:
    result+=a.lower()if a.isupper() else a.upper()

print(result)


# String Filtering and Loops

str = input("Enter the string ").strip()
vowel = "aeiou"
result = ""
for a in str:
    result+= a.lower() if vowel.find(a.lower())==-1 else ""

print(result)
