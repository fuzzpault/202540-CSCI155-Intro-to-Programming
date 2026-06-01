
# pip install syllables

import syllables
import random

with open('mockingbird.txt', '+rt') as f:
    book = f.read()
print("Finished reading the book.")

print(f"Number of characters: {len(book)}")

print(f"Number of lines {book.count("\n")}")

print(f"Average number of characters per line: {len(book) / book.count("\n")}")

# List of words
words = book.split()

print(f"Total words in document: {len(words)}")


# Clean up words so no punctuation or caps.
clean_words = []
for w in words:
    result = w.lower()
    #if w != result:
    #    print(f"{w} -> {result}")
    # Remove non-alpha characters
    result = "".join(filter(str.isalpha, result))
    if len(result) == 0:
        continue
    clean_words.append(result)

# No caps or punctuation
for (i, word) in enumerate(clean_words):
    print(f"  {i}: {word}")
    if i >= 10:
        break

unique_words = set(clean_words)
print(f"Number of unique words {len(unique_words)}")

# Total number of syllables
tot_syllables = 0
for w in clean_words:
    tot_syllables += syllables.estimate(w)
    #if random.randint(0,100) <= 0:
    #    print(f"{w} -> {syllables.estimate(w)}")

# $45.34 -> 4534.   $89 -> 8900

avg_syl_per_word = tot_syllables / len(clean_words)

print(f"Avg syllable per word {avg_syl_per_word}")

# Average words per sentence
num_of_sentences = book.count('.') + book.count('?') + book.count("!")
print(f"Number of senctences: {num_of_sentences}")
print(f"Average words per sentence: {len(clean_words) / num_of_sentences}")

#  Flesch-Kincaid Grade Level. 

kfgl = 0.39 * (len(clean_words) / num_of_sentences) + 11.8 * avg_syl_per_word - 15.59

print(f"KFGL: {kfgl}")



#count = syllables.estimate('python')
#print(count)  # Outputs: 2

#print(book)