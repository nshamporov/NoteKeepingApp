import os
from index import main
from os import listdir
from os.path import isfile, join
import re


def create():
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

                title = "Add"
                print(f"\n{'=' * 10} {title} {'=' * 10}")
                print("\nList of notes: \n")

                for item in onlyfiles_sorted:
                        print("--" + item[:-4])

                
                if not os.path.exists(folder_path):
                        os.makedirs(folder_path)


                fname = input("\nEnter a note name: ").strip()

                                                                        #A function that adds a new note and adds a content for it 
                try:
                        file_path = os.path.join(folder_path, f"{fname}.txt")   
                        if not os.path.exists(file_path):
                                with open(file_path, "w") as file:                     
                                        file.write(input("\n--Enter your content here: "))  
                                print(f"\n<=Note '{fname}' created succefully=>" + f"\n\n{'=' * 38}")
                                break
                        else:
                                print("\n/ / / File already exists. Change the name or edit the existing file. / / /\n ")#If the file exists you will go back to the main menu to add a file with a different name or edit existing file. It wont be looped.
                except Exception as e:
                        print("An error occured: {e}")

if __name__ == "__main__":
        create()



