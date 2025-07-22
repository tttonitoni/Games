import random

class Minen:
    def __init__(self):
        self.Map = [["" for _ in range(20)] for _ in range(20)]

    def GeneratesMines(self, count):
        for i in range(count):
            placed = False
            while not placed:
                x = random.randint(0,19)
                y = random.randint(0,19)
                MapPos = self.Map[x][y]
                print(MapPos)
                if MapPos == "":
                    self.Map[x][y] = "X"
                    placed = True
    
    def ShowMap(self):
        for row in self.Map:
            print(row)

    def Reveal(self,x,y):
        MapPos = self.Map[x][y]
        if MapPos == "X":
            return False
        else:
            