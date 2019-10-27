def get_unique_words(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


def most_common_words(filepath, number_of_words = 3):
    with open(filepath) as input_file:
        words = [word.strip(",.:;") for word in input_file.read().lower().split()]
        unique_words = get_unique_words(words)   # list(set(words)) is faster, but order may be different
        frequencies = [words.count(word) for word in unique_words]
        sorted_words = sorted(unique_words, key=lambda x: frequencies[unique_words.index(x)], reverse=True)
    return sorted_words[:number_of_words]

print(most_common_words("data/lorem_ipsum.txt"))
