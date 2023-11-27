import os
from index import main


def create():
        folder_path = "Notes"

        if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        title = "Add"
        print(f"\n{'=' * 10} {title} {'=' * 10}")
        
        fname = input("\nEnter a note name: ").strip()

        try:
                file_path = os.path.join(folder_path, f"{fname}.txt")   
                if not os.path.exists(file_path):
                        with open(file_path, "w") as file:                     
                                file.write(input("\nEnter your content here: "))  
                        print(f"\nNote '{fname}' created succefully." + f"\n\n{'=' * 38}")
                        # print(f"\n{'=' * 38}")
                else:
                        print("File already exists. Change the  or edit the existing file.")     
        except Exception as e:
                print("An error occured: {e}")

if __name__ == "__main__":
        create()



