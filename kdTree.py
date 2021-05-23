# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html

from node import Node
from collections import deque

class KDTree():
    def __init__(self):
        self.dimensions = [0, 1]   
        self.root = None
        self.treeHeight = 0

    def insert(self, point):
        # IF THERE IS NO ROOT NODE YET, SET CURRENT POINT AS ROOT NODE
        if self.root is None:
            self.root = Node(point, self.dimensions[0], 1)
            self.treeHeight = 1
        else:
            self.insertPoint(self.root, point, 0)
            

    def insertPoint(self, currentNode, point, heightCount):
        heightCount += 1
        
        # IF AXIS IS DIMENSION 0 ('X')
        if currentNode.getAxis() == self.dimensions[0]:
            # IF CURRENT NODE HAS A CHILD SUBTREE
            if currentNode.right or currentNode.left:
                if point[self.dimensions[0]] >= currentNode.getXVal():
                    self.insertPoint(currentNode.right, point, heightCount)
                else:
                    self.insertPoint(currentNode.left, point, heightCount)

            # IF CURRENT NODE HAS NO CHILDREN
            else: 
                heightCount += 1
                if point[self.dimensions[0]] >= currentNode.getXVal():
                    currentNode.right = Node(point, self.dimensions[1], heightCount)
                else:
                    currentNode.left = Node(point, self.dimensions[1], heightCount)

        # IF AXIS IS DIMENSION 1 ('Y') 
        else:
            if currentNode.right or currentNode.left:
                if point[self.dimensions[1]] >= self.root.getYVal():
                    self.insertPoint(currentNode.right, point, heightCount)
                else:
                    self.insertPoint(currentNode.left, point, heightCount)
            
            else:
                heightCount += 1
                if point[self.dimensions[1]] >= currentNode.getXVal():
                    currentNode.right = Node(point, self.dimensions[0], heightCount)
                else:
                    currentNode.left = Node(point, self.dimensions[0], heightCount)

    # def visualize(self):
    #     queue = deque()
    #     queue.append(self.root)
    #     while queue:
    #         current = queue.popleft()

    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)
            
            


    #             (2,3)          -------6
    #            /     \         ---5/ --5\ ---4
    #           /       \        ---4/ --7\ ---3    
    #       (1,10)     (3,5)     ---- 16    ------- finalRow: numLevels * 8   
    #     return

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

    