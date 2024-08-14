import os
from monster import Monster
from style import style

class Player:
    def __init__(self):
        self.current_directory = "home"
        self.playerEntries = 0
        self.style = style()

    def explore(self):
        print(self.style.computerOut(f"\n ~/Exploring directory '{self.current_directory}'..."))
        # Read out the contents of the current directory
        directory_contents = os.listdir(self.current_directory)
        if directory_contents:
            print(self.style.computerOut(" ~/Directory contents:"))
            for item in directory_contents:
                print(self.style.computerOut(" ~", item))
        else:
            print(self.style.computerOut(" ~/The directory is empty."))
            print("")


    def create_file(self, file_name):
        file_path = os.path.join(self.current_directory, f"{file_name}")
        print(self.style.computerOut(f"\n ~/Creating file '{file_name}' in directory '{self.current_directory}'..."))
        try:
            with open(file_path, 'w') as file:
                file.write("")  # Empty content for now
            print(self.style.computerOut(f" ~/File '{file_name}' created successfully."))
        except Exception as e:
            print(self.style.monsterTaunt(" ~/If you can't even manage to create a simple file, how do you expect to stand\nagainst me? Your incompetence will be your downfall."))##print(f"Error creating file: {e}")

    def delete_file(self, file_name):
        file_path = self.current_directory+"/"+file_name
        print(self.style.computerOut(f"\nDeleting file '{file_name}'..."))
        if os.path.exists(file_path):
            os.remove(file_path)
            print(self.style.computerOut(f" ~/File '{file_name}' deleted successfully."))
        else:
            print(self.style.computerOut(f" ~/There is no file named '{file_name}'."))
            print("")
            print(self.style.monsterTaunt(" ~/Foolish mortal you don't understand the program do you? lol"))

    def change_directory(self, new_directory):
        monster = Monster()
        if new_directory == "home":
            self.current_directory = "home"
            print(self.style.computerOut(" ~/Returned to the home directory."))
        else:
            print(self.style.computerOut(f"\n ~/Changing directory to '{new_directory}'..."))
            # Check if the directory exists
            if os.path.exists(self.current_directory+"/"+new_directory):
                # Implement logic for changing directory
                self.current_directory = os.path.join(self.current_directory, new_directory)
                print(self.style.computerOut(f" ~/Directory changed to '{new_directory}'."))
                print(monster.dir_response())
            else:
                print(self.style.monsterTaunt(" ~/Mortal, one does not shift into something that does not exist."))

    def read_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        outputOne = self.style.computerOut(f"\n ~/Reading contents of file '{file_name}'...")
        print(outputOne)
        print("")
        try:
            with open(file_path, 'r') as file:
                contents = file.read()
                outputTwo = self.style.computerOut(f" ~/Contents of '{file_name}':")
                print(outputTwo)
                print("--------------")
                print(contents)
        except FileNotFoundError:
            print(self.style.computerOut(f" ~/File '{file_name}' not found."))
            
    def edit_file(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        print(self.style.computerOut(f"\n ~/Editing file '{file_name}'..."))
        print("")
        try:
            with open(file_path, 'r') as file:
                contents = file.read()
                print(self.style.computerOut(f" ~/Current contents of '{file_name}':"))
                print("--------------")
                print(contents)
            new_contents = input("Enter new contents: ")
            with open(file_path, 'a') as file:
                file.write(new_contents)
                file.write("\n")
                print(self.style.computerOut(f" ~/File '{file_name}' updated successfully."))
        except FileNotFoundError:
            print(self.style.monsterTaunt(" ~/Mortal one does not shift into something that does not exist."))
            
    def real_help(self):
        print(self.style.computerOut(" ~/User Commands:"))
        print(" - ls")
        print(" - create")
        print(" - delete")
        print(" - change")
        print(" - edit")
        print(" - read")
        print(" - quit")
                
    def more_help(self):
        print(self.style.computerOut(" ~/User Commands:"))
        print(" - ls: Print out the current directory.")
        print(" - create <file_name>: Create a new file.")
        print(" - delete <file_name>: Delete a file.")
        print(" - edit <file_name>: Add a line of text to a file")
        print(" - change <directory_name>: Change the current directory.")
        print(" - read <file_name>: Read the contents of a file.")
        print(" - quit: Quit the game.")



            
# Example usage
#if __name__ == "__main__":
    #player = Player()
    #player.explore()
    #player.create_file("test")
    #player.delete_file("test")
    #player.change_directory("Downloads")
    #player.read_file("example.txt")  # Change "example.txt" to an existing file in your directory
