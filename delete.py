import re
import os 
from os import listdir
from os.path import isfile, join



def delete():
    folder_path = "Notes"

                                                #Prints the list of notes in the folder
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
        print(f"\n{'=' * 10} {title} {'=' * 10}")
        print("\nList of notes: \n")

        for item in onlyfiles_sorted:
             print("--" + item[:-4])


        choosefile = input("\nEnter the note you want to delete: ").strip()
        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")


                                                                #Function to delete the note specified from the folder
        try:
            if os.path.exists(chosenfile):
                os.remove(chosenfile)
                print("\n<-Note removed succefully.->" +  f"\n\n{'=' * 38}")
                break
            else:
                print("\n/ / / File doesn't exist. Check the spelling and try again. / / /")
        except Exception as e:
            print("\n/ / / An error occurred: {e} / / /")

if __name__ == "__main__":
        delete()    