from node import Node

class KDTree():
    def __init__(self, data=None):
        self.dimensions = 2
        self.root = None
        if data:
            for point in data:
                self.insert(point)
    

    def insert(self, point):
        # IF THERE IS NO ROOT NODE YET, SET CURRENT POINT AS ROOT NODE
        if not self.root:
            self.root = Node(point, 'X')
        else:
            
            

        return

    def balance(self):
        return
    
    def delete(self):
        return
    
    def performRangeSearch(self, range):
        return
    
    def performKNNSearch(self, radius):
        return

    def drawTree(self):
        return

    