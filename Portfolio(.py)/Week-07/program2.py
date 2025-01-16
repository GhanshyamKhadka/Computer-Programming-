'''Write and test three functions that each take two words (strings) as parameters and
 return sorted lists (as defined above) representing respectively:
 Letters that appear in at least one of the two words.
 Letters that appear in both words.
 Letters that appear in either word, but not in both.'''
 
def unique_sorted_letters(word):
    return sorted(set(char.lower() for char in word if char.isalpha()))

def letters_in_at_least_one(word1, word2):
    letters1 = unique_sorted_letters(word1)
    letters2 = unique_sorted_letters(word2)
    return sorted(set(letters1) | set(letters2))

def letters_in_both(word1, word2):
    letters1 = unique_sorted_letters(word1)
    letters2 = unique_sorted_letters(word2)
    return sorted(set(letters1) & set(letters2))

def letters_in_either_not_both(word1, word2):
    letters1 = unique_sorted_letters(word1)
    letters2 = unique_sorted_letters(word2)
    return sorted(set(letters1) ^ set(letters2))


word1 = "hello"
word2 = "world"

print("Letters in at least one:", letters_in_at_least_one(word1, word2)) 
print("Letters in both:", letters_in_both(word1, word2))                  
print("Letters in either not both:", letters_in_either_not_both(word1, word2))  