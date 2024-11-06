#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

with open("./mail merge/input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

for name in names:
    with open("./mail merge/input/letters/starting_letter.docx", "r") as file:
        name = name.replace("\n", "")
        letter = file.read()
        new_letter = letter.replace("[name]", name)
        
        if not os.path.exists("./mail merge/ReadyToSend"):
            os.makedirs("./mail merge/ReadyToSend")
        with open(f"./mail merge/ReadyToSend/letter_for_{name}.docx", "w") as file:
            file.write(new_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp