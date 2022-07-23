#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    names_list = [name.replace('\n', '') for name in names_list]
    print(names_list)

with open("Input/Letters/starting_letter.docx") as letter:
    letter_pattern = letter.read()
    for name in names_list:
        with open(f"Output/ReadyToSend/{name}.docx", "w") as new_file:
            new_file.write(letter_pattern.replace('[name]', name))
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp