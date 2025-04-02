This project is an attempt to use code to plot patterns for draping.
Overall, this project seeks to use Excel, Python, and Inkscape to make 
this accessible to a wide variety of people, and also able to be edited.
These software choices are mainly comfort based, and these may limit 
execution; there are possible extensions to this idea to a SQL database 
for patterns, and a package with a graphical user interface that 
incorporates all of the above into a binary package to be used on 
windows / mac. I am also interested in software that factors in common 
fitter measurement deviations (per fitter), and error correction to 
adjust the equations that drive the geometry. But I digress.

The goal is to start at men's coats, jackets, and pants, and then slowly 
expand software capabilities. The intent is to provide a framework and 
robust subcomponents that can be reused in order to automate most of the 
math involved in patterning, in order to increase the likelihood of first 
drafts of patterns fitting, allow older systems to be produced en masse, 
and to allow corrected patterns to be printed.

Intended hardware and software required:
Laptop running Windows or Mac
Python 3.

Intended License: GPLv2 Only

Definitions:
System -- A collection of patterns, typically based on one set of 
    measurements, and often drafted using the same construction lines.
Measurements -- Distances that define the person to costumers. They 
    consist of many 
Standard Figure -- Also labeled ideal figure, these are the range 
    over which the system works 
Variations -- These tend to be different figures with significant 
    variation compared to the standard figure, and as such have 
    offsets to measurements that are significant enough to require 
    special adjustments. Common ones in older books are corpulent, 
    stout, and slim. Also referred to as figure.
Construction Lines -- Lines drawn based on measurements that do not 
    often directly translate to the pattern, but provide useful 
    relative points for the pattern draft.

Software to be used:
Microsoft Excel -- The versatility and wide knowledge base of Excel 
    means that many people can learn the specialty formulas used in this
    project. Some specialty excel functions / tricks are used in this project.
    Excel will house the pattern book specific math, and the user 
    interface for selecting which pattern to load.
Python -- This will be the hidden part of the code, mainly being a bridge
    between the Excel document and Inkscape tool. The main goals of the 
    python side of the project will be a) transferring the data over
    to visualization tools (inkscape, previews in Excel), and not having
    to be directly interacted with for most people using the program.
    Modules being considered --
        py2exe -- packaging into executable
        pyinstaller -- packaging into executable
        openpyxl -- Excel visualization
        xlwings -- Excel visualization
        matplotlib -- Excel visualization
        pandas -- Interacting with Excel
        custom python -- Get it to talk with inkscape
Inkscape -- Inkscape enables a user to then edit the pattern output, 
    and for the initial versions allow the user to connect curves.
    Inkscape has been chosen, despite quirks, for being relatively
    straightforward to use.

Additional documentation can be found in the documentation folder.
