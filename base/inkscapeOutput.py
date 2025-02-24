# Generate template SVG File from pagesize and title block template
# 
class pagesize:
    def __init__(self, xDimension, yDimension):
        self.xDimension = xDimension
        self.yDimension = yDimension

ArchE = pagesize("48in", "36in")
ArchD = pagesize("36in", "24in")
ArchC = pagesize("24in", "18in")
ArchB = pagesize("18in", "12in")
ArchA = pagesize("12in", "9in")
