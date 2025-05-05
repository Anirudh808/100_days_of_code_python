# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open invited names file and store all the names in a list.
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    # for each name in the invited names list read sample letter and replace [name] with the actual name and create a
    # new file in output directory with final result.
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            letter_lines = letter.readlines()
            # after getting hold of lines in the sample letter. create a new file with the name of the invited person.
            with open(f"./Output/ReadyToSend/{name.strip()}", "w") as final_letter:
                # write the contents from sample letter to final ready to send letter line by line
                for line in letter_lines:
                    # replace [name] with the actual name if it exists.
                    writable_line = line.replace("[name]", name.strip())
                    final_letter.write(writable_line)

