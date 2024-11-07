#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

def get_names(filename):
    with open(filename, "r") as file:
        names = file.readlines()
    return names
def get_letter(filename):
    with open(filename, "r") as file:
        letter = file.read()
    return letter
def write_letters(names, letter):
        name = name.replace("\n", "")
        new_letter = letter.replace("[name]", name)
        
        if not os.path.exists("./mail merge/ReadyToSend"):
            os.makedirs("./mail merge/ReadyToSend")
        with open(f"./mail merge/ReadyToSend/letter_for_{name}.docx", "w") as file:
            file.write(new_letter)

write_letters(get_names("./mail merge/input/Names/invited_names.txt"), get_letter("./mail merge/input/letters/starting_letter.docx"))


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
