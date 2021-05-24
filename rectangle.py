class Rectangle:
    def __init__(self, X1, Y1, X2, Y2) -> None:
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2
        self.value = [(X1, Y1), (X2, Y2)]

    def __str__(self) -> str:
        return "[({0}, {1}), ({2}, {3})]".format(self.X1, self.Y1, self.X2, self.Y2)

    def getX1(self):
        return self.X1

    def getY1(self):
        return self.Y1

    def getX2(self):
        return self.X2

    def getY2(self):
        return self.Y2

    def getValue(self):
        return self.value