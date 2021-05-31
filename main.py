from linearSearch import *
from kdTree import *

def testKD(filePath, queryBox, randomPoint):
    print("Testing File: {}...".format(filePath.split("\\")[1]))
    tree = createKDTreeFromFile(filePath)
    rangeSearchResult = tree.performRangeSearch(queryBox)
    nnSearchResult = tree.performKNNSearch(randomPoint, k=1)
    five_nnSearchResult = tree.performKNNSearch(randomPoint, k=5)
    ten_nnSearchResult = tree.performKNNSearch(randomPoint, k=10)

    return (rangeSearchResult, nnSearchResult, five_nnSearchResult, ten_nnSearchResult)

def testLinear(filePath, queryBox, randomPoint):
    print("Testing File: {}...".format(filePath.split("\\")[1]))
    linearObj = createLinearScanArrayFromFile(filePath)
    rangeSearchResult = linearObj.performRangeSearch(queryBox)
    nnSearchResult = linearObj.performKNNSearch(randomPoint, k=1)
    five_nnSearchResult = linearObj.performKNNSearch(randomPoint, k=5)
    ten_nnSearchResult = linearObj.performKNNSearch(randomPoint, k=10)

    return (rangeSearchResult, nnSearchResult, five_nnSearchResult, ten_nnSearchResult)

def testFile(filePath, queryBox):
    randomPoint = chooseRandomPointFromFile(filePath)
    kdTreeResults = testKD(filePath, queryBox, randomPoint)
    print(" ")
    linearScanResults = testLinear(filePath, queryBox, randomPoint)

    return kdTreeResults, linearScanResults

def testFileInsertDeleteKDTree(filePath):
    tree = createKDTreeFromFile(filePath)
    tree.visualize()
    tree.delete(tree.root.value)
    tree.visualize()

'''
A. BEHAVIOUR AND PERFORMANCE OF INSERT AND DELETE
'''

'''TEST CASE 1: FROM TUTORIAL WEEK 5'''
# print("\nBuilding tree from Tutorial Week 4 Q5...\n")
# tree = KDTree()
# tree.insert((35,60))
# tree.insert((20,45))
# tree.insert((85,40))
# tree.insert((10,35))
# tree.insert((65,30))
# tree.insert((50,85))
# tree.insert((20,20))
# tree.insert((70,20))
# tree.insert((60,90))
# tree.insert((75,60))
# tree.insert((65,65))
# tree.insert((90,55))
# tree.visualize()
# tree.delete((tree.root.value))
# tree.visualize()

'''TEST CASE 2: circle10.txt'''
# print("\nBuilding tree from circle10.txt...\n")
# tree = createKDTreeFromFile("kdtree\circle10.txt")
# randomPoint = chooseRandomPointFromFile("kdtree\circle10.txt")
# tree.visualize()
# tree.delete(randomPoint)
# tree.visualize()


'''
B. BEHAVIOUR AND PERFORMANCE OF KD-TREE VS LINEAR SEARCH
'''
'''CHECK IF RESULTS ARE CORRECT FIRST'''

# queryBox = [(0, 0), (0.3, 0.3)]
# kd, linear = testFile("kdtree\input100.txt", queryBox)
# print("CHECKING RESULTS FOR FILE {}: \n".format("input100.txt"))
# print("KD TREE: ")
# print("Range Search Result at {0}: \n{1}".format(queryBox, sorted(kd[0])))
# print("\n1-NN Search Result:", sorted(kd[1]))
# print("5-NN Search Result:", sorted(kd[2]))
# print("10-NN Search Result:", sorted(kd[3]))
# print("\nLinear Scan: ")
# print("Range Search Result at {0}: \n{1}".format(queryBox, sorted(linear[0])))
# print("\n1-NN Search Result:", sorted(linear[1]))
# print("5-NN Search Result:", sorted(linear[2]))
# print("10-NN Search Result:", sorted(linear[3]))

'''CHECK IF RESULTS ARE CORRECT FIRST'''

# queryBox = [(0, 0), (0.3, 0.3)]
# kd, linear = testFile("kdtree\circle100.txt", queryBox)
# print("CHECKING RESULTS FOR FILE {}:\n".format("circle100.txt"))
# print("KD TREE: ")
# print("Range Search Result at {0}: \n{1}".format(queryBox, sorted(kd[0])))
# print("\n1-NN Search Result:", sorted(kd[1]))
# print("5-NN Search Result:", sorted(kd[2]))
# print("10-NN Search Result:", sorted(kd[3]))
# print("\nLinear Scan: ")
# print("Range Search Result at {0}: \n{1}".format(queryBox, sorted(linear[0])))
# print("\n1-NN Search Result:", sorted(linear[1]))
# print("5-NN Search Result:", sorted(linear[2]))
# print("10-NN Search Result:", sorted(linear[3]))


'''KD TREE VS LINEAR SEARCH: RANGE SEARCH & KNN SEARCH'''

# queryBox = [(0, 0), (0.3, 0.3)]
# kd, linear = testFile("kdtree\input100.txt", queryBox)
# kd, linear = testFile("kdtree\input10K.txt", queryBox)
# kd, linear = testFile("kdtree\input100K.txt", queryBox)
# kd, linear = testFile("kdtree\input1M.txt", queryBox)
# kd, linear = testFile("kdtree\circle10.txt", queryBox)
# kd, linear = testFile("kdtree\circle100.txt", queryBox)
# kd, linear = testFile("kdtree\circle1000.txt", queryBox)
# kd, linear = testFile("kdtree\circle10000.txt", queryBox)
