# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_file = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = pandas.DataFrame(nato_alphabet_file)
nato_dictionary = {}
for (index, row) in nato_alphabet.iterrows():
    letter = row["letter"].rstrip("\n")
    code = row["code"].rstrip("\n")
    nato_dictionary[letter] = code
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Type in a word").upper()
for char in user_word:
    print(nato_dictionary.get(char))
