import re
import os 
from os import listdir
from os.path import isfile, join



def edit():
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

        title = "Edit"
        print(f"\n{'=' * 10} {title} {'=' * 10}\n")
        print("The list of notes: \n")

        for item in onlyfiles_sorted:
             print("--" + item[:-4])
            

        choosefile = input("\nEnter the note you want to edit: ")
        chosenfile = os.path.join(folder_path, f"{choosefile}.txt")


        if not os.path.exists(chosenfile):       
            print(f"\n/ / / The note doesn't exist. Check the spelling and try again. / / /  ")
            return edit()
        

                                                        #Prints the content of the note specified
        with open(chosenfile, "r") as file_content:
            print("\n" + "{ " + file_content.read() + " }")


                                                        #Function to either append or overwright the content
        def edit_type():
            editingtype = input("\nWould you like to append or overwrite the specified note?\nType (a) for Append or (w) for Overwrite: ")
        
            try:
                if editingtype == "a":                              #Appends 
                    appending = open(chosenfile, "a")
                    appending.write(input("\nEnter your content here: "))
                    appending.close()
                    print("\n<-Note edited successfuly.->" + f"\n\n{'=' * 38}")
                    exit
                elif editingtype == "w":                            #Overwrites
                    overwriting = open(chosenfile, "w")
                    overwriting.write(input("\n--Enter your content here:  "))
                    overwriting.close()
                    print("\n<-Note edited successfuly.->" + f"\n\n{'=' * 38}")
                    exit
                else:                       
                    print("\n/ / / Error: Wrong input. / / /")
                    return edit_type()
            except Exception as e:
                print("An error occurred: {e}")
        edit_type()
        break
        
    
if __name__ == "__main__":
    edit()  



