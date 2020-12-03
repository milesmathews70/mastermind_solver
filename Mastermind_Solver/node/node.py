class Node:
    def __init__(self, i, o, c):
        self.input = i
        self.output = o
        self.children = []
        self.colors = c
        self.past = {"", "", "", ""}

    def addChild(self, Node n):
        self.children.append(n)

    def randomColor(self):
        color = self.colors[randint(len(self.colors))]
        return color
    
    def deleteColor(self, color):
        self.colors.remove(color)
    