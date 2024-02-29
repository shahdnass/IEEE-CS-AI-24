import math

def get_numbers():
    try:
        numbers = input("Enter a list of numbers separated by spaces: ").split()
        numbers = [int(num) for num in numbers]

        return numbers
    except ValueError:
        print("Please enter valid numbers.")
        return []


def find_min(numbers):
    if not numbers:
        print("the list is empty")
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def find_max(numbers):
    if not numbers:
        print("the list is empty")
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_mean(numbers):
    if not numbers:
        print("the list is empty")
        return None
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def find_range(numbers):
    if not numbers:
        print("the list is empty")
        return None
    return max(numbers) - min(numbers)


def find_variance(numbers):#ما الخطا هنا 
    if not numbers:
        print("The list is empty")
        return None

    mean = find_mean(numbers)
    t = 0
    for x in numbers:
        t += pow((x - mean), 2)
    variance = t / (len(numbers)-1)
    return variance


def find_STD(numbers):
    if not numbers:
        print("The list is empty")
        return None
    return math.sqrt(find_variance(numbers))


def find_mode(numbers): #معرفتش اظبطها لوحدي كويس
    if not numbers:
        print("The list is empty")
        return None
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]
    return mode


def find_median(numbers):
    if not numbers:
        print("The list is empty")
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:  # If the number of elements is even
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    else:  # If the number of elements is odd
        median = sorted_numbers[n // 2]
    return median

def find_Quariles(numbers):
    if not numbers:
        return None, None, None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    q1 = find_median(sorted_numbers[:n//2])
    q2 = find_median(sorted_numbers)
    q3 = find_median(sorted_numbers[n//2 + (n % 2):])
    return q1, q2, q3


def find_IQR(numbers):
    if not numbers:
        return None
    q1, _, q3 = find_Quariles(numbers)
    return q3 - q1


numbers = get_numbers()
if numbers:
  print("Min:", find_min(numbers))
  print("Max:", find_max(numbers))
  print("Mean:", find_mean(numbers))
  print("Mode:", find_mode(numbers))
  print("Median:", find_median(numbers))
  print("Range:", find_range(numbers))
  print("Variance:", find_variance(numbers))
  print("Standard Deviation:", find_STD(numbers))
  q1, q2, q3 = find_Quariles(numbers)
  print("Quartiles:", (q1, q2, q3))
  print("Interquartile Range (IQR):", find_IQR(numbers))
