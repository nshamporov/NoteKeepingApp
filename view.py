from os import listdir
from os.path import isfile, join
import os

title = "View"
print(f"\n{'=' * 10} {title} {'=' * 10}")

folder_path = "Notes"

# Function to view all the files in the folder
def fileslist():
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    print("\nList of notes:" + str(onlyfiles))
fileslist()

def choosefile():
    return input("\nEnter a note to view: ")

# Function to view the content in the specfied file
def viewfile(chosenfile):
    try:
        chosenfile = os.path.join(folder_path, f"{chosenfile}.txt")
        with open(chosenfile, "r") as file_content:
            print("\n" + file_content.read() + "\n")
            return True
    except FileNotFoundError:
        print("\nNote doesn't exist. Please try again.\n")
        return False


while True:
    choice = choosefile()
    view = viewfile(choice)

    if view:
        import index



