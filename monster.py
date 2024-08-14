import os
import random
from style import style
from puzzles import puzzle

class Monster:
    def __init__(self):
        self.hints = 0
        self.playerName = "Mortal"
        self.cthuluName = "monster"
        self.style = style()
        self.puzzle = puzzle()
        
    def introduce_cthulhu(self):
        print(self.style.monsterTalk("mWelcome player. I have taken over your computer and erased all of your files. "
              "Just see for yourself."))
        print("")
        message = self.style.green("As much fun as it would be to watch you put random keys like an ")+self.style.bold("idiot")+self.style.green(" I am gonna\ngive you your first command to type:")+" "+self.style.bold("sl")
        print(message)

    def dir_response(self):
        responses = [
            " ~/Ah, another directory to roam in darkness...",
            " ~/This directory seems to be a labyrinth of lost hopes and dreams.",
            " ~/I can smell the fear lingering in this directory...",
            " ~/How quaint, a directory filled with echoes of forgotten files.",
            " ~/In this directory, shadows dance to the tune of chaos.",
            " ~/I wonder what secrets lie hidden within this directory...",
            " ~/This directory feels like a maze of endless nightmares.",
            " ~/A directory ripe for my malevolent presence to dwell...",
            " ~/The files in this directory will soon succumb to oblivion.",
            " ~/Ah, the perfect place for me to unleash my dark whims..."
        ]
        # Select a random response
        random_response = random.choice(responses)
        # Print the response in green
        print(self.style.monsterTalk(random_response))
        
            
    def help_response(self):
        snarky_responses = [
            " ~/You seek help from me? How amusing...",
            " ~/Ah, the lost soul cries out for guidance...",
            " ~/Help? Oh, you poor, misguided mortal...",
            " ~/In this realm of darkness, help is but a distant dream...",
            " ~/You think I would aid you? How naive...",
            " ~/Your plea for help echoes in the void...",
            " ~/If you need help maybe you should try going backwards.",
            " ~/Oh, to be so foolish as to seek help in the domain of chaos...",
            " ~/Help is a concept foreign to this realm of madness...",
            " ~/The shadows laugh at your feeble attempts to seek assistance...",
            " ~/Help? Hah! You are truly beyond salvation..."
        ]
        # Select a random snarky response
        random_response = random.choice(snarky_responses)
        # Print the response in yellow
        print(self.style.monsterTalk(random_response))

    def talk_to_monster(self,question):
        pass
    
    def hint(self):
        if self.hints:
            print(self.style.monsterAnger(" ~/I will not tell you again, MORTAL!!!!"))
        else:
            print(self.style.monsterAnger("~/If you find my name and name a file with it you will have power over me.\n"
            " ~/I will not be compeled again, mortal!!!"))
            self.hints = 1
    
    def namer(self):
        cthulhu_cyber_names = [
            "Cythulon",
            "Cyberthulhu",
            "Cthulhonicron",
            "Cyberthulu",
            "Nyarbyte",
            "Tekhulhu",
            "Cthulink",
            "Cyberathulhu",
            "Neurathulhu",
            "Technothulhu",
            "Cthulinkton",
            "Cthulogic",
            "Cyberkthon",
            "Cthulhuscend",
            "Cybercthulh",
            "Necrocyberth",
            "Cthultrix",
            "Cybercthunian",
            "Techulhulian"
        ]
        random_response = random.choice(cthulhu_cyber_names)
        # Print the response in yellow
        self.cthuluName = random_response
    
    def welcomeback(self):
        print("\033[92m ~/Welcome back "+self.playerName+". Think you can still win?\033[0m")

    def setPlayerName(self):
        playerName = input("\033[92m ~/Out of curriosity what is your name, Mortal?\033[0m")
        self.playerName = playerName
        print("\033[92m ~/Fine I will call you "+self.playerName+"\033[0m")
        print("")
        print(self.style.red(" ~/This will be my only act of kindness."))
        print(self.style.blue(self.puzzle.helpClue))
        print("")

    def readRespond(self,text):
        print("\033[93m ~/What does " + text + " even mean? Have you already lost your mind?\033[0m")
        
