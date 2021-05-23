# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html

from pptree.pptree import print_tree_vertically
from myNode import MyNode
from ppbtree import *


class KDTree:
    def __init__(self):
        self.dimensions = [0, 1]   
        self.root = None
        self.treeHeight = 0

    def insert(self, point):
        # IF THERE IS NO ROOT NODE YET, SET CURRENT POINT AS ROOT NODE
        if self.root is None:
            self.root = MyNode(point, self.dimensions[0], 1)
            self.treeHeight = 1
        else:
            self.insertPoint(self.root, point, 0)
            

    def insertPoint(self, currentNode, point, heightCount):
        heightCount += 1
        
        # IF AXIS IS DIMENSION 0 ('X')
        if currentNode.getAxis() == self.dimensions[0]:
            # IF CURRENT NODE HAS A CHILD SUBTREE
            if point[self.dimensions[0]] >= currentNode.getXVal():
                if currentNode.right:
                    self.insertPoint(currentNode.right, point, heightCount)
                else:
                    heightCount += 1
                    currentNode.right = MyNode(point, self.dimensions[1], heightCount)
            else:
                if currentNode.left:
                    self.insertPoint(currentNode.left, point, heightCount)
                else:
                    heightCount += 1
                    currentNode.left = MyNode(point, self.dimensions[1], heightCount)
                

        # IF AXIS IS DIMENSION 1 ('Y') 
        else:
            if point[self.dimensions[1]] >= currentNode.getYVal():
                if currentNode.right:
                    self.insertPoint(currentNode.right, point, heightCount)
                else:
                    heightCount += 1
                    currentNode.right = MyNode(point, self.dimensions[0], heightCount)
            
            else:
                if currentNode.left:
                    self.insertPoint(currentNode.left, point, heightCount)
                else:
                    currentNode.left = MyNode(point, self.dimensions[0], heightCount)

        if heightCount > self.treeHeight:
            self.treeHeight = heightCount

    def visualize(self):
        # CODE USED FROM THIS GITHUB REPOSITORY: https://github.com/clemtoy/pptree
        root = self._visualize(self.root, None)
        print_tree(root, nameattr='value')


    def _visualize(self, currentNode, parentNode):
        treeNode = Node(currentNode.value)

        if not currentNode.hasChild:
            return treeNode
        else:
            if currentNode.left:
                # The tree visualizer's left child goes up, so we make our 
                # left nodes correspond to the visualizer's right child instead (it'll go down).
                treeNode.right = self._visualize(currentNode.left, treeNode)
            if currentNode.right:
                # The tree visualizer's right child goes down, so we make our 
                # right nodes correspond to the visualizer's left child instead (it'll go up).
                treeNode.left = self._visualize(currentNode.right, treeNode)
            return treeNode

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

