from kdTree import distanceTo
from operator import itemgetter


class Linear():
    def __init__(self) -> None:
        self.data = None

    def insertLinear(self, inputFile):
        with open(inputFile, 'r') as f:
            contents = f.readlines()
        linearSearchArray = []
        for line in contents:
            point = line.split()
            point[0] = float(point[0])
            point[1] = float(point[1])
            linearSearchArray.append((point[0], point[1]))

        self.data = linearSearchArray

    def performRangeSearch(self, queryBox):
        print("LINEAR SCAN: Performing Range Search with Query Box {}:".format(queryBox))
        result = []
        for point in self.data:
            if (point[0] >= queryBox[0][0] and 
            point [0] <= queryBox[1][0] and
            point[1] >= queryBox[0][1] and
            point[1] <= queryBox[1][1]):
                result.append(point)

        return result

    def performKNNSearch(self, targetPoint, k=1):
        print("LINEAR SCAN: Performing KNN Search at point {} with k = {}:".format(targetPoint, k))
        result = []
        for point in self.data:
            distance = distanceTo(point, targetPoint)
            if len(result) < k:
                result.append((point, distance))
            else:
                nearestPointsMax = max(result, key=itemgetter(1))
                # COMPARE CURRENT DISTANCE TO DISTANCE IN THE nearestPointsMax
                if distance < nearestPointsMax[1]:
                    result.remove(nearestPointsMax)
                    result.append((point, distance))
            
        return result
