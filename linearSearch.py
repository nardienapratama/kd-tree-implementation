from typing import final
from kdTree import distanceTo
from operator import itemgetter
import time

class Linear():
    def __init__(self) -> None:
        self.data = None

    def insertLinear(self, pointsArr):
        self.data = pointsArr

    def performRangeSearch(self, queryBox):
        print("\nLINEAR SCAN: Range Search with Query Box {}:".format(queryBox))
        result = []
        startTime = round(time.time() *1000)
        for point in self.data:
            if (point[0] >= queryBox[0][0] and 
            point [0] <= queryBox[1][0] and
            point[1] >= queryBox[0][1] and
            point[1] <= queryBox[1][1]):
                result.append(point)
        endTime = round(time.time() *1000)
        print("Time Elapsed for Range Search Using Linear Scan: {} milliseconds".format(endTime - startTime))
        return result

    def performKNNSearch(self, targetPoint, k=1):
        print("\nLINEAR SCAN: KNN Search at point {} with k = {}:".format(targetPoint, k))
        result = {}
        startTime = round(time.time() *1000)
        for point in self.data:
            if point[0] != targetPoint[0] or point[1] != targetPoint[1]:
                distance = distanceTo(point, targetPoint)
                if len(result) < k:
                    result[point] = distance
                else:
                    # OUT OF THE K SMALLEST TUPLES, FIND THE ONE WITH BIGGEST DISTANCE
                    nearestPointsMax = max(result.items(), key=itemgetter(1))
                    # COMPARE CURRENT DISTANCE TO DISTANCE IN THE nearestPointsMax
                    if distance < nearestPointsMax[1]:
                        del result[nearestPointsMax[0]]
                        result[point] = distance
        endTime = round(time.time() *1000)
        print("Time Elapsed for kNN Search Using Linear Scan: {} milliseconds".format(endTime - startTime))
        finalResult = []
        for key, _ in result.items():
            finalResult.append(key)
        return finalResult

def createLinearScanArrayFromFile(filepath):
    startTime = round(time.time() *1000)
    with open(filepath, 'r') as f:
        contents = f.readlines()

    linearSearchArray = []
    for line in contents:
        point = line.split()
        point[0] = float(point[0])
        point[1] = float(point[1])
        linearSearchArray.append((point[0], point[1]))

    linearObj = Linear()
    linearObj.insertLinear(linearSearchArray)
    endTime = round(time.time() *1000)
    print("Construction time of array for linear scan: {} milliseconds".format(endTime-startTime))

    return linearObj