import re
import os 
from os import listdir
from os.path import isfile, join

folder_path = "Notes"

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
        print("The list of notes: \n")

        for item in onlyfiles_sorted:
             print(item[:-4])
            
        choosefile = input("\nEnter the note you want to edit: ")
        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")

        if not os.path.exists(chosenfile):       
            print(f"\nThe note doesn't exist. Check the spelling and try again.")
            return edit()

        def edit_type():
            editingtype = input("\nWould you like to append or overwrite the specified note? Type (a) for Append or (w) for Overwrite: ")

            if editingtype == "a":      
                appending = open(chosenfile, "a")
                appending.write(input("\nEnter your content here: "))
                appending.close()
                print("Note edited successfuly." + f"\n\n{'=' * 38}")
                break
            elif editingtype == "w":    
                overwriting = open(chosenfile, "w")
                overwriting.write(input("Enter your content here: "))
                overwriting.close()
                print("Note edited successfuly." + f"\n\n{'=' * 38}")
                break
            else:                       
                print("\nError: Wrong input.")
                return edit_type()
        edit_type()
        
if __name__ == "__main__":
    edit()  


# edit type loop doesnt break

