import re
import os 
from os import listdir
from os.path import isfile, join



def delete():
    folder_path = "Notes"

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

        choosefile = input("\nEnter the note you want to delete: ").strip()

        # Function to delete specified file 

        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")
        try:
            if os.path.exists(chosenfile):
                os.remove(chosenfile)
                print("\nNote removed succefully." +  f"\n\n{'=' * 38}")
                break
            else:
                print("\nFile doesn't exist. Check the spelling and try again.")
        except Exception as e:
            print("\nAn error occurred: {e}")

if __name__ == "__main__":
        delete()    