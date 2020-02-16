import sys

class SaveTeseuFromLabyrinth():

   def __init__(self):
    self.lines = 0
    self.columns = 0
    self.steps = 0
    self.length = 0
    self.artifacts = 0
    self.coordinates = []
    self.labyrinth = []
    self.orientation = True # true => right / false => left

    # create and write a output file with all infos about Teseu odissei
    def createOutputFile():
        file = open(sys.argv[2], "w")
        file.write(str(self.length) + " passos no total \n")
        file.write(str(self.steps) + " passos ate a saida \n")
        for c in self.coordinates:
            file.write(str(c[0]) +" "+ str(c[1]) + " \n")
        file.write(str(self.artifacts) + " artefatos encontrados \n")
        file.close()
    
    # reading txt file
    txt = open(sys.argv[1]).read().splitlines()

    # defining support functions
    ## make movement in the labyrinth and check if exists new artifact or found the exit
    def move(self,i,j):
        increaseStep(self,i,j)
        if self.labyrinth[i][j] == "A":
            increaseArtifact(self)
            nextMove(self,i,j)
        elif self.labyrinth[i][j] == "S":
            ## when Teseu found the exit!! he is saved!
            print("Teseu found the exit!! he is saved now!")
            createOutputFile()
            print("Output file created => " + sys.argv[2])
            sys.exit()
        else:
            nextMove(self,i,j)

    ## when i found Teseu, register your start position and call next move in labyrinth
    def start(self,position):
        registerCoordinates(self, position[0], position[1])
        nextMove(self, position[0], position[1])

    ## check the better move to make in labyrinth
    def nextMove(self,i,j):
        nextRow = i+1
        nextCol = j+1 if self.orientation else j-1
        if self.labyrinth[i][nextCol] != "1":
            move(self, i, nextCol)
        else:
            if self.labyrinth[nextRow][j] != "1":
                move(self, nextRow, j)
            else:
                self.orientation ^= self.orientation ## to right or left
                nextMove(self,i,j)

    ## append x and y coordinates to cordinates list
    def registerCoordinates(self,i,j):
        self.coordinates.append((i,j))

    ## increase new movement in the labyrinth
    def increaseLength(self):
        self.length += 1

    ## increase a new Teseo step to find "S"
    def increaseStep(self,i,j):
        registerCoordinates(self,i,j)
        increaseLength(self)
        self.steps += 1

    ## increase a new artifact found
    def increaseArtifact(self):
        self.artifacts += 1

    # construct labyrinth from txt file

    ## mount list of labyrinth lines
    [self.labyrinth.append(list(i)) for i in txt if txt.index(i) > 0]

    # locate Teseu star position in labyrinth
    for r, line in enumerate(self.labyrinth):
        try:
            currentPosition = r, line.index('T')
            start(self,currentPosition)
        except ValueError:
            pass

SaveTeseuFromLabyrinth()