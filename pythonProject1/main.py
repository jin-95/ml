import nltk
from nltk.corpus import words
from itertools import permutations

def function_to_find_words(list_of_alphabets,no_of_alphabets):
    """function to create a list of all existing words from a list of alphabets,
    input needs to be in string format """

    # Ensure the words dataset is downloaded
    nltk.download('words', quiet=True)  # Using quiet=True to suppress download messages

    list_of_all_available_words = set(words.words())  # Convert to set for faster lookups

    common_words = {}  # Dictionary to store results

    list_of_alphabets = list(list_of_alphabets)

    for r in range(1, len(list_of_alphabets) + 1):  # r is the length of the permutation
        words_of_length_r = [''.join(p) for p in permutations(list_of_alphabets, r) if ''.join(p) in list_of_all_available_words]
        if words_of_length_r:  # If there are any words of this length
            key = f"{r} alphabet{'s' if r > 1 else ''}"  # e.g., "1 alphabet", "2 alphabets", etc.
            common_words[key] = words_of_length_r

    for key, value in common_words.items():
        common_words[key] = set(value)

    # Print the results for words with (x) or more alphabets
    for key, value in common_words.items():
        if int(key.split()[0]) >= no_of_alphabets:  # Check if the number of alphabets is 3 or more
            print(key, ":", value)

    return None

lst = 'eupgldg'
function_to_find_words(lst,3)