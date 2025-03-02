# Construct the system for each pattern

# Measurements are passed as a dictionary, dimensionless.
from pandas import DataFrame
# """
# Debug / standards
measurements = {'waist':'','breast':'','seat':'','height':''}

# """
"""
class pattern:
    def __init__(self, name):
        self.name = name




"""

# actual code

# data
measurementrange = {'col1': [],}

class coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def inOrEx (measurements):
    # Should compare measurements vs system measurement tables and see average variation / expected issue probability.
    # Should return information mainly to the user (0 to IDK), with 0 to 1 being the deviation from the closest "average person",
    # where the average person is defined as a set of equations that yield the tables vs height (height being a skeletal, immutable measurement).
    pass
    