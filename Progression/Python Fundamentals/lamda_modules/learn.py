import math

# Compute Area of Circle Using Lambda

n = int(input("Enter the radius "))
result = lambda n : math.pi*(n*n)
print(result(n))

# Calculate Compound Interest Using Lambda

p = int(input("Enter the principal "))
n = int(input("Enter the no of years "))
r = int(input("Enter the Annual Rate "))

ci= lambda p,t,r: p *((1+r)**t)

print(p,t,r)

