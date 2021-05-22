# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html

from node import Node

class KDTree():
    def __init__(self):
        self.dimensions = [0, 1]   
        self.root = None

    def insert(self, point):
        # IF THERE IS NO ROOT NODE YET, SET CURRENT POINT AS ROOT NODE
        if self.root is None:
            self.root = Node(point, self.dimensions[0])
        else:
            self.insertPoint(self.root, point)

    def insertPoint(self, currentNode, point):
        if currentNode is None:
            return currentNode
        if currentNode.getAxis() == self.dimensions[0]:
            if currentNode.right or currentNode.left:
                if point[self.dimensions[0]] >= currentNode.getXVal():
                    self.insertPoint(currentNode.right, point)
                else:
                    self.insertPoint(currentNode.left, point)
            else: 
                if point[self.dimensions[0]] >= currentNode.getXVal():
                    currentNode.right = Node(point, self.dimensions[1])
                else:
                    currentNode.left = Node(point, self.dimensions[1])

        else:
            if currentNode.right or currentNode.left:
                if point[self.dimensions[1]] >= self.root.getYVal():
                    self.insertPoint(currentNode.right, point)
                else:
                    self.insertPoint(currentNode.left, point)
            
            else:
                if point[self.dimensions[1]] >= currentNode.getXVal():
                    currentNode.right = Node(point, self.dimensions[0])
                else:
                    currentNode.left = Node(point, self.dimensions[0])

    def visualize(self):
        return

    def balance(self):
        return
    
    def delete(self):
        return
    
    def performRangeSearch(self, range):
        return
    
    def performKNNSearch(self, radius):
        return

    def drawTree(self):
        return

    