import os 
from os import listdir
from os.path import isfile, join

folder_path = "Notes"

# Function to show the list of files
def fileslist():
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    print("List of notes: " + str(onlyfiles))
fileslist()

choosefile = input("Enter the note you want to edit: ")


# Function to edit the specified file
def edit():
    chosenfile = os.path.join(folder_path, f"{choosefile}.txt")

    if not os.path.exists(chosenfile):          # Check if the file exists 
        print(f"The note doesn't exist. Check the spelling and try again.")
        return

    editingtype = input("Would you like to append or overwrite the specified note? Type (a) for Append or (w) for Overwrite: ")
    if editingtype == "a":      # Append content
        editing = open(chosenfile, "a")
        editing.write(input("Enter your content here: "))
        editing.close()
    elif editingtype == "w":    # Overwrite content
        editing = open(chosenfile, "w")
        editing.write(input("Enter your content here: "))
        editing.close()
    else:                       # Error message
        print("Error: Wrong input.")
edit()

