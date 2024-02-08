word = input()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"the word {word} is a palindrome")
else:
    print(f"the word {word} is not a palindrome")
