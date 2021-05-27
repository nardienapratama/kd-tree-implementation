# References Used for Guidance: 
## https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
## https://math.stackexchange.com/questions/1764878/how-to-efficiently-create-balanced-kd-trees-from-a-static-set-of-points/1764963
## https://stackoverflow.com/questions/2927165/confused-about-definition-of-a-median-when-constructing-a-kd-tree
## https://en.wikipedia.org/wiki/K-d_tree
## DELETION ALGORITHM BASED ON GEEKS FOR GEEKS' ALGORITHM DESCRIPTION (CODE NOT COPIED AND PASTED): 
### https://www.geeksforgeeks.org/k-dimensional-tree-set-3-delete/

# Reference to improve implementation:
# https://stackoverflow.com/questions/5254838/calculating-distance-between-a-point-and-a-rectangular-box-nearest-point

from rectangle import Rectangle
from node import MyNode
from ppbtree import *
from operator import itemgetter
import math, time, random
random.seed(10)

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
            startTime = round(time.time() *1000)
            rectangle = Rectangle(-math.inf, -math.inf, math.inf, math.inf)
            self.root = MyNode(point, self.dimensions[0], 1, rectangle)
            self.treeHeight = 1
            endTime = round(time.time() *1000)
        else:
            startTime = round(time.time() *1000)
            self._insert(self.root, point, 0)
            endTime = round(time.time() *1000)

        print("Inserting point {0} took {1} milliseconds.".format(point, endTime-startTime))
            

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
        startTime = round(time.time() *1000)
        self.root = self._delete(self.root, point)
        endTime = round(time.time() *1000)
        print("Deleting point {0} took {1} milliseconds.".format(point, endTime-startTime))

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

    def _checkBoxLineIntersection(self, queryBox, currentNode):
        '''
        Checks if query box intersects with the current splitting line segment. If so, returns True. Else, returns False.
        '''
        currentAxis = currentNode.getAxis()
        if (queryBox[0][currentAxis] <= currentNode.value[currentAxis] and 
        currentNode.value[currentAxis] <= queryBox[1][currentAxis] ):
            return True
        return False

    def performRangeSearch(self, queryBox):
        print("\nKD-TREE: Range Search with Query Box {}:".format(queryBox))
        # START AT ROOT
        # RECURSIVELY SEARCH FOR POINTS IN BOTH SUBTREES
        # PRUNE: IF QUERY RECTANGLE DOESN'T INTERSECT THE RECTANGLE CORRESPONDING
        # A NODE, NO NEED TO EXPLORE THAT NODE AND ITS SUBTREES
        startTime = round(time.time() *1000)
        result = self._performRangeSearch(self.root, queryBox, [])
        endTime = round(time.time() *1000)
        print("Time Elapsed for Range Search Using kd-Tree: {} milliseconds".format(endTime - startTime))
        return result
    
    def _performRangeSearch(self, currentNode, queryBox, result):
        # CHECK QUERY BOX AND SPLITTING LINE SEGMENT INTERSECTION
        # IF INTERSECTS, CHECK NODE AND SUBTREES
        # IF QUERY BOX INTERSECTS WITH THE SPLITTING LINE SEGMENT:
        if self._checkBoxLineIntersection(queryBox, currentNode):
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
        
        else:
            if queryBox[1][currentNode.getAxis()] < currentNode.value[currentNode.getAxis()]:
                if currentNode.hasLeftChild():
                    # TODO: TRAVERSE LEFT SUBTREE ONLY
                    result = self._performRangeSearch(currentNode.left, queryBox, result)
                    pass
            elif queryBox[0][currentNode.getAxis()] >= currentNode.value[currentNode.getAxis()]:
                if currentNode.hasRightChild():
                    # TODO: TRAVERSE RIGHT SUBTREE ONLY
                    result = self._performRangeSearch(currentNode.right, queryBox, result)
                

        return result

    def performKNNSearch(self, targetPoint, k=1):
        print("\nKD-TREE: KNN Search at point {} with k = {}:".format(targetPoint, k))
        startTime = round(time.time() *1000)
        result = self._performKNNSearch(self.root, targetPoint, {}, k)
        endTime = round(time.time() *1000)
        print("Time Elapsed for kNN Search Using kd-Tree: {} milliseconds".format(endTime - startTime))
        finalResult = []
        for key, _ in result.items():
            finalResult.append(key)

        return finalResult

    def _performKNNSearch(self, currentNode, targetPoint, nearestPoints, k=1):
        distance = distanceTo(currentNode.value, targetPoint)
        if nearestPoints:
            # GET BIGGEST DISTANCE SO FAR
            # OUT OF THE K SMALLEST TUPLES, FIND THE ONE WITH BIGGEST DISTANCE
            nearestPointsMax = max(nearestPoints.items(), key=itemgetter(1))
        else:
            nearestPointsMax = (currentNode.value, math.inf)
        # IF THE DISTANCE FROM TARGET POINT TO CURRENT NODE'S RECTANGLE IS SMALLER THAN THE BIGGEST DISTANCE IN THE DICTIONARY, THEN CHECK NODE AND SUBTREES; ELSE SKIP
        distPointRect = distanceFromPointToRect(targetPoint, currentNode.rectangle)
        if distPointRect < nearestPointsMax[1]:
            if currentNode.value[0] != targetPoint[0] or currentNode.value[1] != targetPoint[1]:
                if len(nearestPoints) < k:
                    nearestPoints[currentNode.value] = distance
                else:
                    # COMPARE CURRENT DISTANCE TO DISTANCE IN THE nearestPointsMax
                    if distance < nearestPointsMax[1]:
                        del nearestPoints[nearestPointsMax[0]]
                        nearestPoints[currentNode.value] = distance
            if currentNode.hasLeftChild():
                nearestPoints = self._performKNNSearch(currentNode.left, targetPoint, nearestPoints, k)
            if currentNode.hasRightChild():
                nearestPoints = self._performKNNSearch(currentNode.right, targetPoint, nearestPoints, k)

        return nearestPoints

def distanceFromPointToRect(point, rect):
    # REFERENCE: https://stackoverflow.com/questions/5254838/calculating-distance-between-a-point-and-a-rectangular-box-nearest-point
    dx = max(rect.getX1() - point[0], 0, point[0] - rect.getX2())
    dy = max(rect.getY1() - point[1], 0, point[1] - rect.getY2())
    return math.sqrt((dx)**2 + (dy)**2)

def distanceTo(point1, point2):
    result = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return result

def chooseRandomPointFromFile(inputFile):
    with open(inputFile, 'r') as f:
        contents = f.readlines()
    
    randomLineIndex = random.randrange(0, len(contents))
    randomLine = contents[randomLineIndex]
    randomLinePoint = randomLine.split()
    randomLinePoint[0] = float(randomLinePoint[0])
    randomLinePoint[1] = float(randomLinePoint[1])

    return randomLinePoint

def createKDTreeFromFile(inputFile):
    startTime = round(time.time() *1000)
    with open(inputFile, 'r') as f:
        contents = f.readlines()
    
    points = []
    for line in contents:
        point = line.split()
        point[0] = float(point[0])
        point[1] = float(point[1])
        points.append((point[0], point[1]))
    
    tree = KDTree()
    modifiedTree = _createKDTreeFromFile(tree, points, 0)
    endTime = round(time.time() *1000)
    print("Construction time of kd-Tree: {} milliseconds".format(endTime-startTime))
    
    return modifiedTree

# Based on wikipedia's construction algorithm
def _createKDTreeFromFile(tree, pointsList, depth):
    if not pointsList:
        return None
    else:
        axis = depth % 2
        if axis == 0:
            sortedList = sorted(pointsList, key=lambda x:x[0])
        else:
            sortedList = sorted(pointsList, key=lambda x:x[1])

        medianIndex = len(sortedList) // 2
        median = sortedList[medianIndex]
        tree.insert(median)

        _createKDTreeFromFile(tree, sortedList[:medianIndex], depth+1)
        _createKDTreeFromFile(tree, sortedList[medianIndex+1::], depth+1)

    return tree
        