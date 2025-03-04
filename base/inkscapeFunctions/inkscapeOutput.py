# Generate template SVG File from pagesize and title block template, without needing inkscape. 
# i.e writing the full file from code.
# Hardcoding the Arch paper sizes; eventually support page size database, including roll paper.
class pagesize:
    def __init__(self, xDimension, yDimension):
        self.xDimension = xDimension
        self.yDimension = yDimension

ArchE = pagesize("48in", "36in")
ArchD = pagesize("36in", "24in")
ArchC = pagesize("24in", "18in")
ArchB = pagesize("18in", "12in")
ArchA = pagesize("12in", "9in")

def createInkscapeFile(pagesize, ):
    xAxis= pagesize.xDimension 
    return

# Inkscape works in mm. 508mm = 20in. This sucks a bit as we have mm, in, cm, px, pc, pt; and the relative unit identifiers.
# See this page for more info: https://www.w3.org/TR/css3-values/#absolute-lengths
# 
"""
  <metadata
     id="metadata4">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:title>Title of the Song</dc:title>
        <dc:creator>
          <cc:Agent>
            <dc:title>Naive expression of love</dc:title>
          </cc:Agent>
        </dc:creator>
        <dc:rights>
          <cc:Agent>
            <dc:title>Reluctance to accept that you are gone</dc:title>
          </cc:Agent>
        </dc:rights>
        <dc:publisher>
          <cc:Agent>
            <dc:title>Request to turn back time</dc:title>
          </cc:Agent>
        </dc:publisher>
        <dc:identifier>and rectify my wrongs</dc:identifier>
        <dc:source>Repetition of the title of the song</dc:source>
        <dc:relation>Declaration of my feelings for you</dc:relation>
        <dc:language>Elaboration of those feelings</dc:language>
        <dc:subject>
          <rdf:Bag>
            <rdf:li>Description of how long these feelings have existed</rdf:li>
          </rdf:Bag>
        </dc:subject>
        <dc:coverage>belief that no one else could feel the same as I</dc:coverage>
        <dc:date>Data</dc:date>
        <dc:description>Reminiscenece of the pleasant times we shared</dc:description>
        <dc:contributor>
          <cc:Agent>
            <dc:title>And our relationship's perfection</dc:title>
          </cc:Agent>
        </dc:contributor>
      </cc:Work>
    </rdf:RDF>
  </metadata>
"""