import svgwrite

class svgObj:

    def __init__(self, filename, width, height):
        self.filename = filename
        self.width = width
        self.height = height
        self.dwg = svgwrite.Drawing(filename, profile='tiny', size=(width, height))

    def addLine(self, x1, y1, x2, y2):
        self.dwg.add(self.dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

    def addCircle(self, x, y, r):
        self.dwg.add(self.dwg.circle(center=(x, y), r=r, stroke=svgwrite.rgb(0, 0, 0, '%')))

    def addRect(self, x, y, width, height):
        self.dwg.add(self.dwg.rect(insert=(x, y), size=(width, height), stroke=svgwrite.rgb(0, 0, 0, '%')))

    def save(self):
        self.dwg.save()