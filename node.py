class Node():
    def __init__(self, point, axis):
        self.value = point
        self.left = None
        self.right = None
        self.axis = axis
        self.rectangle = None

    def getValue(self):
        return self.value
    
    def getAxis(self):
        return self.axis
