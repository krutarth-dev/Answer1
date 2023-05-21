def find_highest_frequency_word_length(string):
    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find the highest frequency
    max_frequency = max(frequency.values())

    # Find the length of the highest-frequency word
    highest_frequency_word = max(frequency, key=frequency.get)
    highest_frequency_word_length = len(highest_frequency_word)

    return highest_frequency_word_length

# Test the program
string = "the quick brown fox jumps over the lazy dog"
print(find_highest_frequency_word_length(string))
# Output: 3 (since "the" appears twice, so the highest-frequency word length is 3)

# Additional Test Case 1
string = "hello world hello world hello"
print(find_highest_frequency_word_length(string))
# Output: 5 ("hello" appears three times, and its length is 5, which is the highest frequency and length)

# Additional Test Case 2
string = "apple banana apple apple banana"
print(find_highest_frequency_word_length(string))
# Output: 5 ("apple" appears three times, and its length is 5, which is the highest frequency and length)
