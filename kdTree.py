# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
## DELETION ALGORITHM BASED ON GEEKS FOR GEEKS' ALGORITHM DESCRIPTION (CODE NOT COPIED AND PASTED): 
### https://www.geeksforgeeks.org/k-dimensional-tree-set-3-delete/

from rectangle import Rectangle
from myNode import MyNode
from ppbtree import *
import math


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
            rectangle = Rectangle(-math.inf, -math.inf, math.inf, math.inf)
            self.root = MyNode(point, self.dimensions[0], 1, rectangle)
            self.treeHeight = 1
        else:
            self._insert(self.root, point, 0)

        print("Inserting point: {}".format(point))
            

    def _insert(self, currentNode, point, heightCount):
        '''
        This method is called by the insert method above. This method goes down the tree recursively 
        to insert the point in the correct location in the kd-Tree.
        '''
        heightCount += 1
        
        # IF AXIS IS DIMENSION 0 ('X')
        if currentNode.getAxis() == self.dimensions[0]:
            # IF CURRENT NODE HAS A CHILD SUBTREE
            if point[self.dimensions[0]] >= currentNode.getX():
                if currentNode.right:
                    self._insert(currentNode.right, point, heightCount)
                else:
                    # RY
                    heightCount += 1
                    rectangle = currentNode.getRectangle()
                    
                    newRectangle = Rectangle(currentNode.getX(), rectangle.getY1(), 
                                            rectangle.getX2(), rectangle.getY2())
                    currentNode.right = MyNode(point, self.dimensions[1], heightCount, newRectangle)
            else:
                if currentNode.left:
                    self._insert(currentNode.left, point, heightCount)
                else:
                    # LY
                    heightCount += 1
                    rectangle = currentNode.getRectangle()
                    newRectangle = Rectangle(rectangle.getX1(), rectangle.getY1(), 
                                            currentNode.getX(), rectangle.getY2())
                    currentNode.left = MyNode(point, self.dimensions[1], heightCount, newRectangle)
                    
                

        # IF AXIS IS DIMENSION 1 ('Y') 
        else:
            if point[self.dimensions[1]] >= currentNode.getY():
                if currentNode.right:
                    self._insert(currentNode.right, point, heightCount)
                else:
                    # RX
                    heightCount += 1
                    rectangle = currentNode.getRectangle()
                    newRectangle = Rectangle(rectangle.getX1(), currentNode.getY(), 
                                            rectangle.getX2(), rectangle.getY2())
                    currentNode.right = MyNode(point, self.dimensions[0], heightCount, newRectangle)
                    
            
            else:
                if currentNode.left:
                    self._insert(currentNode.left, point, heightCount)
                else:
                    # LX
                    # MODIFY CURRENT NODE'S RECTANGLE TO CORRESPOND TO THE AREA
                    # OF THE NEW NODE ABOUT TO BE INSERTED
                    rectangle = currentNode.getRectangle()
                    
                    newRectangle = Rectangle(rectangle.getX1(), rectangle.getY1(), 
                                            rectangle.getX2(), currentNode.getY())
                    currentNode.left = MyNode(point, self.dimensions[0], heightCount, newRectangle)

        if heightCount > self.treeHeight:
            self.treeHeight = heightCount

    

    def delete(self, point):
        '''
        This method deletes a point from the kd-tree.
        '''
        self.root = self._delete(self.root, point)
        print("Deleting point: {}".format(point))

    # BASED ON GEEKS FOR GEEKS' DELETE ALGORITHM PSEUDOCODE
    def _delete(self, currentNode, point):
        # IF CURRENTNODE CONTAINS POINT TO BE DELETED
        if currentNode.value[0] == point[0] and currentNode.value[1] == point[1]:
            # TODO: DO DELETION ALGORITHM
            # 1. IF NODE IS A LEAF NODE, DELETE IT
            if not currentNode.hasChild():
                return None
            # 2. IF NODE HAS RIGHT CHILD AS NOT NULL
            if currentNode.hasRightChild():
                # 2.1 FIND MIN OF CURRENT NODE'S DIMENSION IN RIGHT SUBTREE
                minimumNode = self._findMin(currentNode.right, currentNode.getAxis())
                # 2.2 REPLACE CURRENT NODE WITH ABOVE FOUND MINIMUM (2.1) AND RECURSIVELY DELETE 
                # MINIMUM IN RIGHT SUBTREE
                currentNode.value = minimumNode.value
                currentNode.right = self._delete(currentNode.right, minimumNode.value)
                
            # 3. ELSE IF NODE HAS LEFT CHILD AS NOT NULL
            else:
                # 3.1 FIND MIN OF CURRENT NODE'S DIMENSION IN LEFT SUBTREE
                minimumNode = self._findMin(currentNode.left, currentNode.getAxis())
                # 3.2 REPLACE CURRENT NODE WITH ABOVE FOUND MINIMUM (3.1) AND RECURSIVELY DELETE 
                # MINIMUM IN LEFT SUBTREE
                currentNode.value = minimumNode.value
                minimumNode = self._delete(currentNode.left, minimumNode.value)
                # 3.3 MAKE NEW LEFT SUBTREE AS RIGHT CHILD OF CURRENT NODE
                currentNode.right = minimumNode
                currentNode.left = None
               
        # IF CURRENTNODE DOESN'T CONTAIN POINT TO BE DELETED
        else:
            # 1. IF NODE TO BE DELETED IS SMALLER THAN CURRENTNODE ON CURRENT DIMENSION, RECUR 
            # FOR LEFT SUBTREE
            if point[currentNode.getAxis()] < currentNode.value[currentNode.getAxis()]:
                currentNode.left = self._delete(currentNode.left, point)
            # 2. ELSE, RECUR FOR RIGHT SUBTREE
            else:
                currentNode.right = self._delete(currentNode.right, point)
    
        return currentNode

    def visualize(self):
        '''
        This method is used to visualize the kd-Tree horizontally. 
        The code used to help visualize the tree is taken from the following GitHub repository: 
        https://github.com/clemtoy/pptree
        '''

        root = self._visualize(self.root)
        print("\nVISUALIZATION OF KD-TREE: \n")
        print_tree(root, nameattr='value')
        print("\n")
        print("\n")


    def _visualize(self, currentNode):
        # value = str(currentNode.value) + " Rect: " + currentNode.rectangle.__str__()
        value = str(currentNode.value)
        treeNode = Node(value)

        if not currentNode.hasChild:
            return treeNode
        else:
            if currentNode.left:
                # The tree visualizer's left child goes up, so we make our 
                # left nodes correspond to the visualizer's right child instead (it'll go down).
                treeNode.right = self._visualize(currentNode.left)
            if currentNode.right:
                # The tree visualizer's right child goes down, so we make our 
                # right nodes correspond to the visualizer's left child instead (it'll go up).
                treeNode.left = self._visualize(currentNode.right)
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
        
        # Compare the found minimum with the current node
        # If current node has smaller value in dim dimension, then current node is minimum.
        if currentNode.value[dim] < minimum.value[dim]:
            minimum = currentNode

        # Compare the found minimum with the current node
        # If current node has exact same value in dim dimension as the minimum node,
        # and the current node's other value is smaller than 
        if currentNode.value[dim] == minimum.value[dim] and currentNode.value[dim^1] < minimum.value[dim^1]:
            minimum = currentNode
        return minimum

    def performRangeSearch(self, queryBox):
        # START AT ROOT
        # RECURSIVELY SEARCH FOR POINTS IN BOTH SUBTREES
        # PRUNE: IF QUERY RECTANGLE DOESN'T INTERSECT THE RECTANGLE CORRESPONDING
        # A NODE, NO NEED TO EXPLORE THAT NODE AND ITS SUBTREES
        result = self._performRangeSearch(self.root, queryBox, [])
        return result
    
    def _performRangeSearch(self, currentNode, queryBox, result):
        # CHECK RECTANGLE INTERSECTION
        # IF INTERSECTS, CHECK NODE AND SUBTREES
        if self._checkRectIntersection(currentNode.rectangle, queryBox):
            # CHECK IF NODE IS IN QUERY BOX
            if self._checkPointInRect(currentNode.value, queryBox):
                # TODO: ADD POINT TO RESULT LIST
                result.append(currentNode.value)

            if currentNode.hasRightChild():
                # TRAVERSE DOWN RIGHT SUBTREE
                result = self._performRangeSearch(currentNode.right, queryBox, result)

            if currentNode.hasLeftChild():
                # TRAVERSE DOWN LEFT SUBTREE
                result = self._performRangeSearch(currentNode.left, queryBox, result)

        return result

    def _checkRectIntersection(self, rectangleObj, queryBox):
        # CHECK THE FOLLOWING CONDITIONS FROM THE SLIDE
        if ((rectangleObj.getY1() <= queryBox[1][1]) and
        (queryBox[0][1] <= rectangleObj.getY2()) and 
        (queryBox[0][0] <= rectangleObj.getX2()) and 
        (rectangleObj.getX1() <= queryBox[1][0])):
            return True
        return False

    
    def _checkPointInRect(self, point, queryBox):
        if (point[0] >= queryBox[0][0] and point[0] <= queryBox[1][0] and
        point[1] >= queryBox[0][1] and point[1] <= queryBox[1][1]):
            return True
        return False

    def distanceTo(self, point1, point2):
        result = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
        return result

    def performKNNSearch(self, targetPoint, k=1):
        result = self._performKNNSearch(self.root, targetPoint, [])
        return result

    def _performKNNSearch(self, currentNode, targetPoint, nearestPoints):
        distance = self.distanceTo(currentNode.value, targetPoint)
        # if distance <= radius:
        # TODO: add {currentNode : distance} to nearestPoints dictionary
        # IF NO POINTS IN LIST YET, APPEND
        if currentNode.value[0] != targetPoint[0] or currentNode.value[1] != targetPoint[1]:
            if not nearestPoints:
                nearestPoints = (distance, currentNode.value)
            else:
                if distance < nearestPoints[0]:
                    nearestPoints = (distance, currentNode.value)
        if currentNode.hasLeftChild():
            nearestPoints = self._performKNNSearch(currentNode.left, targetPoint, nearestPoints)
        if currentNode.hasRightChild():
            nearestPoints = self._performKNNSearch(currentNode.right, targetPoint, nearestPoints)


        return nearestPoints

tree = KDTree()
tree.insert((30,40))
tree.insert((5,25))
tree.insert((70,70))
tree.insert((10,12))
tree.insert((50,30))
tree.insert((35,45))   
tree.visualize()
tree.delete((30,40))
tree.visualize()

tree = KDTree()
rectangle = Rectangle(1, 1, 4, 3)
print(tree._checkRectIntersection(rectangle, [(0,0), (0.5,0.5)]))
print(tree._checkPointInRect((1,0),  [(1,1), (4,3)]))

# tree = KDTree()
# tree.insert((30,40))
# tree.insert((5,25))
# tree.insert((70,70))
# tree.insert((10,12))
# tree.insert((50,30))
# tree.insert((35,45))   
# tree.visualize()
# tree.delete((70,70))
# tree.visualize()


# tree = KDTree()
# tree.insert((51,75))
# tree.insert((25,40))
# tree.insert((70,70))
# tree.insert((10,30))
# tree.insert((35,90))
# tree.insert((55,1)) 
# tree.insert((60,80))
# tree.insert((1,10)) 
# tree.insert((50,50))   
# tree.visualize()
# print("The minimum point in the x-dimension is: {} \n".format(tree.findMin(tree.dimensions[0])))
# print("The minimum point in the y-dimension is: {} \n".format(tree.findMin(tree.dimensions[1])))

tree2 = KDTree()
tree2.insert((2,3))
tree2.insert((1,5))
tree2.insert((4,2))
tree2.insert((4,5))
tree2.insert((3,3))
tree2.insert([4,4])   
tree2.visualize()
print(tree2.performRangeSearch([(1.2,2.5), (3.2, 3.5)]))
print(tree2.performRangeSearch([(3,1), (5,3)]))
print(tree2.performKNNSearch((2,3), k=1))
# linearSearch = [(2,3), ]
# print("The minimum point in the x-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[0])))
# print("The minimum point in the y-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[1])))
# tree2.insert((1,3))
# tree2.insert((3,1))
# tree2.insert((3,10))
# tree2.visualize()
# print("The minimum point in the x-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[0])))
# print("The minimum point in the y-dimension is: {} \n".format(tree2.findMin(tree2.dimensions[1])))


# tree3 = KDTree()
# tree3.insert((35,60))
# tree3.insert((20,45))
# tree3.insert((85,40))
# tree3.insert((10,35))
# tree3.insert((65,30))
# tree3.insert((50,85))  
# tree3.insert((20,20))  
# tree3.insert((70,20))   
# tree3.insert((60,90))  
# tree3.insert((75,60))  
# tree3.insert((65,65))  
# tree3.insert((90,55))  
# tree3.visualize()
# tree3.delete((35,60))
# tree3.visualize()

# print(tree3.root.right.right)
# print("min of (85,40): {}".format(tree3._findMin(tree3.root.right, 0).value))
# print("min of (60,90): {}".format(tree3._findMin(tree3.root.right.right.right, 0).value))
# print("min of (75,60): {}".format(tree3._findMin(tree3.root.right.right.right.left, 1).value))

# tree4 = KDTree()
# tree4.insert((35,60))
# tree4.insert((20,45))
# tree4.insert((85,40))
# tree4.insert((10,35))
# tree4.insert((65,30))
# tree4.insert((50,85))  
# tree4.insert((20,20))  
# tree4.insert((70,20))   
# tree4.insert((60,90))  
# tree4.insert((75,50))  
# tree4.insert((65,65))  
# tree4.insert((90,55))  
# tree4.visualize()
