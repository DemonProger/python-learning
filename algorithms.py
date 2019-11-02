
from sys import maxsize
import numpy as np

RANGE_START = 0
RANGE_END = 1
RANGE_STEP = 0.1

# Search of point which is gives max value of function
# simplle algorithm
def findMaxForBinF(F, points): 
    maxP = points[0]
    maxF = F(maxP)
    for p in points: 
        if F(p) > maxF:
            maxP = p
            maxF = F(p)
    return maxP 

sourceF = lambda x, y : x*x + y*y
points = []
for i in np.arange(RANGE_START, RANGE_END + RANGE_STEP, RANGE_STEP):
    points.append(i)
print('Points:', points)    

FIXED_X = 1
sourceFX = lambda x : sourceF(x, FIXED_X)
maxForX = findMaxForBinF(sourceFX, points)
print('Max for x: ', maxForX)

FIXED_Y = 1
sourceFY = lambda y : sourceF(FIXED_Y, y)
maxForY = findMaxForBinF(sourceFY, points)
print('Max for y: ', maxForY)

# Search of point wich is gives max value of function
# Algorithm through numpy.argmax
def findMaxForBinF_v2(F, points): 
    values = [[x, F(x)] for x in points]
    maxInColumns = np.argmax(values, axis=0)
    maxFXIndex = maxInColumns[1]
    return values[maxFXIndex][0]
    
maxForX = findMaxForBinF_v2(sourceFX, points)
print('Max for x: ', maxForX)

maxForY = findMaxForBinF_v2(sourceFY, points)
print('Max for y: ', maxForY)
