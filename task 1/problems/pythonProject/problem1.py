numbers = []

while True:
    num = input("Enter a number (or -1 to terminate): ")
    if num == '-1':
        break
    numbers.append(int(num))

print(max(numbers))
print(min(numbers))
