# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html

from myNode import MyNode
from ppbtree import *


class KDTree:
    def __init__(self):
        '''
        This method creates an instance of this kd-Tree class.
        The dimensions attribute is set to an array of two values, since this is a 2D implementation 
        of a kd-Tree. The root is initialized to None when the instance is first created. The tree 
        height is set to 0 as there are no nodes in the tree yet.
        '''
        self.dimensions = [0, 1]   
        self.root = None
        self.treeHeight = 0

    def insert(self, point):
        '''
        This method is used to insert a point into the kd-Tree.
        '''
        # IF THERE IS NO ROOT NODE YET, SET CURRENT POINT AS ROOT NODE
        if self.root is None:
            self.root = MyNode(point, self.dimensions[0], 1)
            self.treeHeight = 1
        else:
            self.insertPoint(self.root, point, 0)
            

    def insertPoint(self, currentNode, point, heightCount):
        '''
        This method is called by the insert method above. This method goes down the tree recursively 
        to insert the point in the correct location in the kd-Tree.
        '''
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
        '''
        This method is used to visualize the kd-Tree horizontally. 
        The code used to help visualize the tree is taken from the following GitHub repository: 
        https://github.com/clemtoy/pptree
        '''

        root = self._visualize(self.root, None)
        print("\nVISUALIZATION OF KD-TREE: \n")
        print_tree(root, nameattr='value')
        print("\n")
        print("\n")


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

    def findMin(self, dim):
        result = self._findMin(self.root, dim)
        return result.value

    def _findMin(self, currentNode, dim):
        '''
        This method finds the node with the smallest value in the dim-th dimension.
        '''
        minimum = None
        if currentNode.getAxis() == dim:
            # IF AXIS IS EQUAL TO TARGET DIM, MINIMUM CAN'T BE IN RIGHT SUBTREE
            if currentNode.left is None:
                # IF NO LEFT SUBTREE, CURRENT NODE IS THE MIN FOR THE TREE ROOTED AT THIS NODE
                minimum = currentNode
            else:
                # OTHERWISE, RECURSE ON LEFT SUBTREE
                minimum = self._findMin(currentNode.left, dim)
        
        else:
            # OTHERWISE, MINIMUM COULD BE IN EITHER SUBTREE
            minimumLeft = None
            minimumRight = None
            if currentNode.left:
                minimumLeft = self._findMin(currentNode.left, dim)
            if currentNode.right:
                minimumRight = self._findMin(currentNode.right, dim)
            
            #  IF CURRENT NODE HAS LEFT AND RIGHT SUBTREES
            if minimumLeft and minimumRight:
                # IF IN X-DIMENSION
                if dim == self.dimensions[0]:
                    # IF MINLEFT'S X IS SMALLER THAN MINRIGHT'S X
                    if minimumLeft.value[0] < minimumRight.value[0]:
                        minimum = minimumLeft
                    # IF MINRIGHT'S X IS SMALLER THAN MINLEFT'S X
                    else:
                        minimum = minimumRight
                
                # IF IN Y-DIMENSION
                else:
                    # IF MINLEFT'S Y IS SMALLER THAN MINRIGHT'S Y
                    if minimumLeft.value[1] < minimumRight.value[1]:
                        minimum = minimumLeft
                    # IF MINRIGHT'S Y IS SMALLER THAN MINLEFT'S Y
                    else:
                        minimum = minimumRight

            elif minimumLeft:
                minimum = minimumLeft

            elif minimumRight:
                minimum = minimumRight

            else:
                minimum = currentNode
        
        return minimum





    
    def delete(self):
        return
    
    def performRangeSearch(self, range):
        return
    
    def performKNNSearch(self, radius):
        return

    def drawTree(self):
        return

tree = KDTree()
tree.insert((51,75))
tree.insert((25,40))
tree.insert((70,70))
tree.insert((10,30))
tree.insert((35,90))
tree.insert((55,1)) 
tree.insert((60,80))
tree.insert((1,10)) 
tree.insert((50,50))   
tree.visualize()
print("The minimum point in the x-dimension is: {} \n".format(tree.findMin(tree.dimensions[0])))
print("The minimum point in the y-dimension is: {} \n".format(tree.findMin(tree.dimensions[1])))

tree2 = KDTree()
tree2.insert((2,3))
tree2.insert((1,3))
tree2.insert((4,2))
tree2.insert((4,5))
tree2.insert((3,3))
tree2.insert((4,4))   
tree2.visualize()
print("The minimum point in the x-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[0])))
print("The minimum point in the y-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[1])))
tree2.insert((1,5))
tree2.insert((3,1))
tree2.insert((3,10))
tree2.visualize()
print("The minimum point in the x-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[0])))
print("The minimum point in the y-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[1])))