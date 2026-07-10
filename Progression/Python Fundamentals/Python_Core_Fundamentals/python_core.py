##Topic: Input/Output and Variables

name = input("Enter your name ")
age = int(input("Enter your age "))
city = input("Enter your city ")
print(f"Hi, My name is {name} . I am {age} years old and live in {city}.")

## Topic:  Variables and Print Formatting

owner = input("Enter the owner name ")
items = int(input("Enter the no.of.items "))
total_cost = float(input("Enter the total cost in floats"))

print(
    f"Owner: {owner}\n"
    f"Items: {items}\n"
    f"Total Cost: {total_cost}" 
)


## Topic: String Formatting and Input

name = input("Enter the name ")
productName = input("Enter the product name ")
deliveryDate = input("Enter the Delivery Date ")

print(
    f"Dear {name}\n"
        f"Thank you for purchasing {productName}.\n"
        f"Your order will be delivered by {deliveryDate}."
)

## String Operations

sen = input("Enter the sen ")
fun = False
if(sen.find("fun")==-1):
    fun = False
else:
    fun = True

print(f"Convert the sen to title case {sen.title()}")
print(f"Remove leading and trailing spaces {sen.strip()}")
print(f"Find the position of the word Python (case-sensitive) {sen.strip().find("Python")}")
print(f"Replace Python with Java if it exists {sen.lower().replace("python","Java")}")
print(f"Check if the word fun (case-sensitive) is present {fun}")

