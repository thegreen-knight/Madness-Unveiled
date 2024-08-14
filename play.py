from player import Player
from monster import Monster
import json
import os
from mechanics import mechanic
from style import style
import readline


# Entry point of the program
if __name__ == "__main__":
    player = Player()
    monster = Monster()
    mech = mechanic()
    style = style()
    #print("    Welcome to Madness Unveiled!\n")
    
    # Ask if the player wants to play
    def ask_to_play():
        response = input(" ~/Want to play Madness Unveiled? (yes/no): ").strip().lower()
        print(" ~/")
        if response == "yes": ## or "y":
            if os.path.exists("save.json"):
                load_game = input(" ~/Do you want to continue where you were last? (yes/no)").strip().lower()
                print(" ~/")
                if load_game == "yes": ## or "y":
                    game_data = load()
                    monster.playerName = game_data["playerName"]
                    monster.cthuluName = game_data["monsterName"]
                    monster.hints = game_data["hint"]
                    player.playerEntries = game_data["entryCount"]
                
                    monster.welcomeback()
                else:
                    check = input(" ~/Are you sure? If you start a new game your old data will be lost. (yes/no)")
                    print(style.computerOut(" ~/"))
                    if check == "yes": ## or "y":
                        new_game()
                        style.monsterFace()
                        monster.introduce_cthulhu()
                        player.current_directory = "home"
                    else:
                        print(style.computerOut(" ~/Restart the game to load the saved game."))
                        exit()
            else:
                new_game()
                style.monsterFace()
                monster.introduce_cthulhu()
                player.current_directory = "home"
        else:
            print(style.computerOut(" ~/Maybe another time. Exiting the game."))
            exit()
            
    def new_game():
        monster.namer()
        mech.setupNewGame(monster.cthuluName)
        
    
    def load():
        try:
            with open("save.json", "r") as json_file:
                game_data = json.load(json_file)
            print(f"Game data loaded successfully.")
            return game_data
        except Exception as e:
            print(f"Error loading game data: {e}")
            return None
    
    def save():
        
        save_data = {
            "hint": monster.hints,
            "playerName": monster.playerName,
            "monsterName": monster.cthuluName,
            "entryCount" : player.playerEntries
        }
        
        file_path = "save.json"
        try:
            with open(file_path, "w") as json_file:
                json.dump(save_data, json_file, indent=4)
            ##print(f"Game saved.")
        except Exception as e:
            print(f"Error saving game: {e}")
        
    def monitor():
        player.playerEntries+=1
        if player.playerEntries == 10:
            monster.setPlayerName()

    # Define function to handle player actions
    def handle_player_action(action,augment):
        actions = {
            "ls": player.explore,
            "create": player.create_file,
            "delete": player.delete_file,
            "change": player.change_directory,
            "read": player.read_file,
            "pleh": player.real_help,
            "pleh-erom": player.more_help,
            "help": monster.help_response,
            "edit": player.edit_file,
            "more-help": monster.help_response,
            "quit": exit,  # Exits the game
            "loqui": monster.talk_to_monster,
            "indicium": monster.hint,
            "clear": mech.clear_screen
        }
        # Check if action is in the dictionary, if not, print error message
        if action in actions:
            # Call the corresponding function
            monitor()
            save()
            if augment:
                if action == "help":
                    #print("help was called")
                    monster.help_response()
                elif action == "please":
                    monster.help_response()
                else:
                    actions[action](augment)
            else:
                actions[action]()
        else:
            monster.readRespond(action)
    ## Game start
    style.gameTitle()
    ask_to_play()
    
    # Game loop
    while True:
        data = input(style.computerOut("\n ~/Enter your action: ")).strip()
        
        # Split data by space
        split_data = data.split()

# Extract action and augment from split_data
        if len(split_data) >= 2:
            action = split_data[0]
            augment = split_data[1]
            handle_player_action(action, augment)
        else:
    # Handle case where there's no augment provided
            action = data
            handle_player_action(action, None)
