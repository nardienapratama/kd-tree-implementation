class MyNode:
    def __init__(self, point, axis, height, rectangle):
        self.value = point
        self.left = None
        self.right = None
        self.parent = None
        self.axis = axis
        self.rectangle = rectangle
        self.height = height

    def __repr__(self) -> str:
        return "<NODE> - {}".format(self.getValue())

    def __str__(self) -> str:
        return "<NODE> - {}".format(self.getValue())

    def hasChild(self):
        return self.right or self.left

    def getRectangle(self):
        return self.rectangle

    def getHeight(self):
        return self.height

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getValue(self):
        return self.value

    def getX(self):
        return self.value[0]

    def getY(self):
        return self.value[1]
    
    def getAxis(self):
        return self.axis
