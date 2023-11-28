from os import listdir
from os.path import isfile, join
import os
import re


def view():
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

        title = "View"
        print(f"\n{'=' * 10} {title} {'=' * 10}")

        for item in onlyfiles_sorted:
            print(item[:-4])

        choosefile = input("\nChoose a note to view: ")
        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")

        try:
            if os.path.exists(chosenfile):
                with open(chosenfile, "r") as file_content:
                    print("\n" + file_content.read() + "\n")
                    break
            else:
                print("Note doesn't exist. Check the spelling and try again.")
                return view()
        except Exception as e:
            print("\nAn error occurred: {e}")

            

if __name__ == "__main__":
        view()


