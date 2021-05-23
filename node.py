class Node():
    def __init__(self, point, axis, height):
        self.value = point
        self.left = None
        self.right = None
        self.parent = None
        self.axis = axis
        self.rectangle = None
        self.height = height

    def __repr__(self) -> str:
        return "<NODE> - {}".format(self.getValue())

    def __str__(self) -> str:
        return "<NODE> - {}".format(self.getValue())

    def getHeight(self):
        return self.height

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getValue(self):
        return self.value

    def getXVal(self):
        return self.value[0]

    def getYVal(self):
        return self.value[1]
    
    def getAxis(self):
        return self.axis
