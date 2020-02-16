# Feel free to add more classes/helper functions if you like, code quality counts!

class RobotRouter:
    # This class will be initialized with the map features from the problem input.
    # barriers and laserCoordinates are arrays of Coordinate objects.
    # laserDirections is an array of strings representing the direction of
    # the corresponding laser in laserCoordinates.
    def __init__(self, barriers, laserCoordinates, laserDirections):
        pass

    # This method will be called to get your optimal route.
    # origin and destination are Coordinate objects (with x and y properties)
    # It should return a list of Coordinate objects,
    # starting with the origin and ending with the destination.
    # If you could not find a valid route, return an empty list.
    def route(self, origin, destination):
        list = [origin]
        pointA = origin
        pointB = destination
        while origin != destination:
            nextStep = self.move(pointA, pointB)
            list.append(nextStep)
        return list

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return '%d,%d' % (self.x, self.y)

import sys

def move(pointA, pointB):
    next = pointA
    #change the x coordinate according to direction
    if shortestDirectionX(pointA, pointB) == "W"
        next.x = next.x - 1
    if shortestDirectionX(pointA, pointB) == "E"
        next.x = next.x + 1
    if shortestDirectionX(pointA, pointB) == None
        next.x = next.x
    #change the y coordinate according to direciton
    if shortestDirectionY(pointA, pointB) == "S"
        next.y = next.y - 1
    if shortestDirectionY(pointA, pointB) == "N"
        next.y = next.y + 1
    if shortestDirectionY(pointA, pointB) == None
        next.y = next.y
    return next

def shortestDirectionX(pointA, pointB):
    if pointA.x > pointB.x:
        return "W"
    elif pointA.x < pointB.x:
        return "E"
    else:
        return None

def shortestDistanceY(pointA, pointB):
    if pointA.y > pointB.y:
        return "S"
    elif pointA.y < pointB.y:
        return "N"
    else:
        return None

def readCoordinate(rawCoordinate):
    parts = rawCoordinate.split(',')
    return Coordinate(int(parts[0]), int(parts[1]))

def writeMapAndRoute(origin, destination, barriers, laserCoordinates, laserDirections, route):
    bottomLeft = origin
    topRight = origin

    for coordinate in (destination, *barriers, *laserCoordinates, *route):
        bottomLeft = Coordinate(min(bottomLeft.x, coordinate.x), min(bottomLeft.y, coordinate.y))
        topRight = Coordinate(max(topRight.x, coordinate.x), max(topRight.y, coordinate.y))

    barrierSet = set(barriers)
    lasers = { laserCoordinates[i]: laserDirections[i] for i in range(len(laserCoordinates)) }
    routeSet = set(route)

    for y in range(topRight.y, bottomLeft.y - 1, -1):
        for x in range(bottomLeft.x, topRight.x + 1):
            coordinate = Coordinate(x, y)

            if coordinate == origin:
                sys.stdout.write('o')
            elif coordinate == destination:
                sys.stdout.write('d')
            elif coordinate in barrierSet:
                sys.stdout.write('X')
            elif coordinate in lasers:
                direction = lasers[coordinate]
                if direction == 'N':
                    sys.stdout.write('^')
                elif direction == 'E':
                    sys.stdout.write('>')
                elif direction == 'W':
                    sys.stdout.write('<')
                elif direction == 'S':
                    sys.stdout.write('v')
                else:
                    sys.stdout.write('?')
            elif coordinate in routeSet:
                sys.stdout.write('.')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

    sys.stdout.write('\n')

    if route:
        sys.stdout.write('Route:\n')
        for coordinate in route:
            sys.stdout.write(str(coordinate))
            sys.stdout.write('\n')
    else:
        sys.stdout.write('No Route')

def main():
    origin = readCoordinate(sys.stdin.readline().strip())
    print("origin=", origin)
    destination = readCoordinate(sys.stdin.readline().strip())
    print("destination=", destination)
    barriers = []
    laserCoordinates = []
    laserDirections = []

    barrierLine = sys.stdin.readline().strip()
    if barrierLine:
        barriers = [readCoordinate(barrier) for barrier in barrierLine.split(' ')]

    laserLine = sys.stdin.readline().strip()
    if laserLine:
        rawLasers = laserLine.split(' ')
        laserCoordinates = [readCoordinate(laser) for laser in rawLasers]
        laserDirections = [laser.rsplit(',', 1)[1] for laser in rawLasers]

    route = RobotRouter(barriers, laserCoordinates, laserDirections).route(origin, destination)
    writeMapAndRoute(origin, destination, barriers, laserCoordinates, laserDirections, route)

main()
