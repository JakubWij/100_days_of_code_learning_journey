# TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    for name in names_file.readlines():
        striped_names = name.strip("\n")


        with open("./Input/Letters/starting_letter.txt") as file:
            letter_as_list = file.readlines()
            replaced_fragment = (letter_as_list[0].replace("[name]", f"{striped_names}"))
            letter_as_list[0] = replaced_fragment

            for line in letter_as_list:
                # Replace the [name] placeholder with the actual name.
                # Save the letters in the folder "ReadyToSend".
                with open(f"./Output/ReadyToSend/letter_to_{striped_names}.txt", mode="a") as letters:
                    # print(line.strip("\n"))
                    letters.write(line)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp