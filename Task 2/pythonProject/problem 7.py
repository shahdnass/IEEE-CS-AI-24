def count_word_occurrences(file_name):
    word_counts = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:

                word = word.strip().lower().strip('.,!?;:')
                if word:

                    word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
file_name = "Sample.txt"
word_counts = count_word_occurrences(file_name)


for word, count in word_counts.items():
    print(f"{word}: {count}")
