import os
import random
#import sys


class style:
    def __init__(self):
        self.end = "\033[0m"
        #self.lightred = "\033[91m"
        #self.lightgreen = "\033[92m"
        self.greenBG = "\033[42m"
        self.redBG = "\033[41m"
        self.orangeBG = "\033[43m"
        self.blueBG = "\033[44m"
        self.purpleBG = "\033[45m"
        self.cyanBG = "\033[46m"
        self.greyBG = "\033[47m"

    def computerOut(self,text):
        return self.purple(self.bold(text))

    def monsterTaunt(self,text):
        return self.yellow(text)

    def monsterTalk(self,text):
        return self.lightgreen(text)

    def monsterAnger(self,text):
        return self.red(self.bold(self.underline(text)))

    def lightgreen(self,text):
        coloredText = "\033[92m" + text + "\033[0m"
        return coloredText

    def yellow(self,text):
        coloredText = "\033[93m" + text + "\033[0m"
        return coloredText

    def lightred(self,text):
        coloredText = "\033[91m" + text + "\033[0m"
        return coloredText

    def lightblue(self,text):
        coloredText = "\033[94m" + text + "\033[0m"
        return coloredText

    def lightcyan(self,text):
        coloredText = "\033[96m" + text + "\033[0m"
        return coloredText

    def gray(self,text):
        coloredText = "\033[97m" + text + "\033[0m"
        return coloredText

    def pink(self,text):
        coloredText = "\033[95m" + text + "\033[0m"
        return coloredText

    def red(self,text):
        coloredText = "\033[31m" + text + "\033[0m"
        return coloredText

    def green(self,text):
        coloredText = "\033[32m" + text + "\033[0m"
        return coloredText

    def orange(self,text):
        coloredText = "\033[33m" + text + "\033[0m"
        return coloredText

    def blue(self,text):
        coloredText = "\033[34m" + text + "\033[0m"
        return coloredText

    def purple(self,text):
        coloredText = "\033[35m" + text + "\033[0m"
        return coloredText

    def cyan(self,text):
        coloredText = "\033[36m" + text + "\033[0m"
        return coloredText

    def bold(self,text):
        coloredText = "\033[01m" + text + "\033[0m"
        return coloredText

    def underline(self,text):
        coloredText = "\033[04m" + text + "\033[0m"
        return coloredText

    def reverse(self,text):
        coloredText = "\033[07m" + text + "\033[0m"
        return coloredText

    def strike(self,text):
        coloredText = "\033[09m" + text + "\033[0m"
        return coloredText

    def monsterFace(self):
        print("")
        print(self.red("                |||||||||||||||    "))
        print(self.red("               |||||||||||||||||    "))
        print(self.red("              |||||||||||||||||||    "))
        print(self.red("              |||||||||||||||||||    "))
        print(self.red("               |||||||||||||||||     "))
        print(self.red("               (||{-}|||||{-}||)     "))
        print(self.red("                |||_|||||||_|||      "))
        print(self.red("               /||| ||| ||| |||\    "))
        print(self.red("              / /|| \|/ \|/ ||\ \   "))
        print(self.red("              \ \ |  |   |  | / /   "))
        print(self.red("               \ \           / /    "))
        print(self.red("                \/^^^^^^^^^^^\/     "))
        print("")
        print("")

    def gameTitle(self):
        print(self.red(self.bold("     |\    /|           |      ")))
        print(self.red(self.bold("     | \  / |  __     __|   ,__   __   _   _")))
        print(self.red(self.bold("     |  \/  | |  |   |  |   |  | |__| |_` |_` ")))
        print(self.red(self.bold("     |      | |  |_, |  |_, |  | |__  ,_| ,_|")))
        print(self.red(self.bold("               `` `   `` `                   ")))
        print("")
        print(self.red(self.bold("       |   |                  |          |  ")))
        print(self.red(self.bold("       |   | ,__        __  ^ |   __   __|  ")))
        print(self.red(self.bold("       |   | |  | \  / |__| | |  |__| |  |  ")))
        print(self.red(self.bold("        \_/  |  |  \/  |__, | |_ |__, |  |_,")))
        print(self.red(self.bold("         `                             `` ` ")))
        print("")
        print("")

    def monsterDeath(self):
        pass
