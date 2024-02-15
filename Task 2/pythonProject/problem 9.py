def find_common_elements(set1, set2):

    common_elements = set1.intersection(set2)
    return common_elements


set1 = set(input("Enter elements for set 1 separated by spaces: ").split())
set2 = set(input("Enter elements for set 2 separated by spaces: ").split())


result = find_common_elements(set1, set2)
print("Common Elements:", result)
