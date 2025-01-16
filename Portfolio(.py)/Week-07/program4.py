'''One approach to analysing some encrypted data where a substitution is suspected
 is frequency analysis. A count of the different symbols in the message can be used
 to identify the language used, and sometimes some of the letters. In English, the
 most common letter is "e", and so the symbol representing "e" should appear most
 in the encrypted text.
 Write a program that processes a string representing a message and reports the six
 most common letters, along with the number of times they appear. Case should
 not matter, so "E" and "e" are considered the same.
 Hint: There are many ways to do this. It is obviously a dictionary, but we will want
 zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
 best to ignore that initially, and then check the usual resources for the runes.'''

def frequency_analysis(message):
    letter_counts = {}

    for char in message:
    
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    most_common = sorted_counts[:6]

    print("The six most common letters are:")
    for letter, count in most_common:
        print(f"Letter: '{letter}', Count: {count}")

if __name__ == "__main__":
    message = input("Enter a message for frequency analysis: ")
    frequency_analysis(message)