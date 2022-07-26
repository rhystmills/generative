import svgwrite
import math

dwg = svgwrite.Drawing('test.svg', size=(700, 500), profile='tiny')

def fractalTree(startCoords, angle, magnitude, remainingSteps):
    # print(startCoords)
    # print(angle)
    # print(magnitude)
    # print(remainingSteps)

    endCoords = (startCoords[0]+magnitude * math.sin(angle),startCoords[1]+magnitude * math.cos(angle))
    dwg.add(dwg.line(startCoords, endCoords,stroke_width=0.5,stroke='black',stroke_opacity=1.0))

    # newCoords = (magnitude * math.sin(angle)/2,magnitude * math.cos(angle)/2)
    newCoords = (startCoords[0] + magnitude * 1 * math.sin(angle),startCoords[1] + magnitude * 1 * math.cos(angle))
    newAngle = angle + 0.5
    newMagnitude = magnitude * 0.8
    newSteps = remainingSteps - 1

    #Alternate branch
    altMagnitude = magnitude * 0.8
    altAngle = angle - 0.5

    if remainingSteps > 0:
        fractalTree(newCoords, newAngle, newMagnitude, newSteps)
        fractalTree(endCoords, altAngle, altMagnitude, newSteps)

# fractalTree((350.00,470.00),math.pi,100,10)

for i in range(20,21):
    dwg = svgwrite.Drawing('test.svg', size=(700, 500), profile='tiny')
    fractalTree((350.00,470.00),math.pi,100,i)
    dwg.saveas("fractalTree_2_" + str(i).zfill(2) + ".svg")

