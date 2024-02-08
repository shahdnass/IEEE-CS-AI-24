num = int(input("ENTER THE NUM : "))
fact = 1
n = num

while n > 0 :
    fact *= n
    n -= 1

print(f"the factorial of {num} is {fact}")
