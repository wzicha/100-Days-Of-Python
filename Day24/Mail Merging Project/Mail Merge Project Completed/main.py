# TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", "r") as sl:
    starting_letter = sl.read()

with open("Input/Names/invited_names.txt", "r") as ns:
    names = ns.readlines()
# for each name in invited_names.txt
for name in names:
    personalized_letter = starting_letter.replace("[name]", name.strip())

    # Replace the [name] placeholder with the actual name.
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as letter_file:
        # Write the personalized letter to the new file
        letter_file.write(personalized_letter)
# Save the letters in the folder "ReadyToSend".


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
