import re
import os 
from os import listdir
from os.path import isfile, join

folder_path = "Notes"


# Function to edit the specified file
def edit():
    def fileslist():
        onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        return onlyfiles
    

    def filter_condition(filename):
        return "exclude" not in filename
    
    def extract_number(filename):
        numbers = re.findall(r'\d+', filename)
        return [int(num) for num in numbers]
    
    while True:
        onlyfiles = fileslist()

        onlyfiles_filtered = filter(filter_condition, onlyfiles)

        onlyfiles_sorted = sorted(onlyfiles_filtered, key=extract_number)

        title = "Delete"
        print(f"\n{'=' * 10} {title} {'=' * 10}\n")

        for item in onlyfiles_sorted:
             print(item)
            
        choosefile = input("\nEnter the note you want to edit: ")
        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")

        if not os.path.exists(chosenfile):          # Check if the file exists 
            print(f"\nThe note doesn't exist. Check the spelling and try again.")
            return

        editingtype = input("\nWould you like to append or overwrite the specified note? Type (a) for Append or (w) for Overwrite: ")
        if editingtype == "a" or "A":      # Append content
            editing = open(chosenfile, "a")
            editing.write(input("Enter your content here: "))
            editing.close()
            break
        elif editingtype == "w" or "W":    # Overwrite content
            editing = open(chosenfile, "w")
            editing.write(input("Enter your content here: "))
            editing.close()
            break
        else:                       # Error message
            print("\nError: Wrong input.")


if __name__ == "__main__":
        edit()  

