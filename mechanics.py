import os
import random
import glob
from puzzles import puzzle

class mechanic:
    def __init__(self):
        self.hints = 0
        self.puzzle = puzzle()
        self.desk = "home/Desktop/"
        self.doc = "home/Documents/"
        self.down = "home/Downloads/"
        self.vid = "home/Videos/"
        self.mus = "home/Music/"
        self.pic = "home/Pictures/"
        self.trash = "home/Trash/"
        self.dirs = [self.desk,self.doc,self.down,self.vid,self.mus,self.pic,self.trash]
        
    def setupNewGame(self,monster):

        monsterSpelling = list(monster)
        
        #textDirs = [doc,down,trash]
        
        for x in self.dirs:
            self.emptyDir(x)
        
        self.createClues()

        letterCount = len(monster)-1
        fileTypes = ['.txt','.pdf','.png','.jpeg','.csv','.avi']
        for v in monsterSpelling:
            folder = random.choice(self.dirs)
            fType = random.choice(fileTypes)
            digits = ''.join(str(random.randint(0,9)) for _ in range(letterCount))
            docName = folder+v+digits+fType
            ##print(docName)
            self.createFile(docName)
            
    def createClues(self):
        folder = random.choice(self.dirs)
        fileName = folder+"LunarLoom.txt"
        self.createFile(fileName,self.puzzle.mhClue)
        
        folder = random.choice(self.dirs)
        fileName = folder+"DeliriumDawn.eml"
        self.createFile(fileName,self.puzzle.speakClue)

        folder = random.choice(self.dirs)
        fileName = folder+"ChaosQuill.eml"
        self.createFile(fileName,self.puzzle.emailClue1)
        
        folder = random.choice(self.dirs)
        fileName = folder+"WhisperWraith.eml"
        self.createFile(fileName,self.puzzle.emailClue2)
        
        folder = random.choice(self.dirs)
        fileName = folder+"BabelEcho.eml"
        self.createFile(fileName,self.puzzle.emailClue3)

        folder = random.choice(self.dirs)
        fileName = folder+"TwilightThroe.eml"
        self.createFile(fileName,self.puzzle.emailClue4)
        
        folder = random.choice(self.dirs)
        fileName = folder+"FrenzyEdge.eml"
        self.createFile(fileName,self.puzzle.emailClue5)
        
        folder = random.choice(self.dirs)
        fileName = folder+"BedlamHeir.eml"
        self.createFile(fileName,self.puzzle.emailClue6)
        
        folder = random.choice(self.dirs)
        fileName = folder+"MadrigalMind.eml"
        self.createFile(fileName,self.puzzle.emailClue7)

        folder = random.choice(self.dirs)
        fileName = folder+"PandemoniumPoet.eml"
        self.createFile(fileName,self.puzzle.emailClue8)

        folder = random.choice(self.dirs)
        fileName = folder+"destructio-bestiae.txt"
        self.createFile(fileName,self.puzzle.guide)
        
        theCommand = ['01101001.txt', '01101110.txt', '01100100.txt', '01101001.txt', '01100011.txt', '01101001.txt', '01110101.txt', '01101101.txt']
        for x in theCommand:
            fileName = self.desk+x
            self.createFile(fileName)

    def createFile(self,name,content=""):
        with open(name, 'w') as file:
            file.write(content)
            file.close()

    def emptyDir(self,folder):
        files = glob.glob(folder+"*")

        for f in files:
            os.remove(f)
            

    def checkForWin(self):
        pass

    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
