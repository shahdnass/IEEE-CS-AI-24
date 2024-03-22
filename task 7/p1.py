def get_numbers():
    try:
        data = input("Enter a list of numbers separated by spaces: ").split()
        data = [int(num) for num in data]

        return data
    except ValueError:
        print("Please enter valid numbers.")
        return []



def probability_distribution(data):
    total_values = len(data)
    distribution = {}

    for value in data:
        if value in distribution:
            distribution[value] += 1
        else:
            distribution[value] = 1

    for value, count in distribution.items():
        distribution[value] = count / total_values

    return distribution



print(probability_distribution(get_numbers()))
