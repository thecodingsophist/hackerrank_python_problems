def roverMove(matrixSize, cmds):
    # Write your code here
    print("matrixSize = " + str(matrixSize))
    print("cmds = " + str(cmds))
    final_integer = 0
    for command in cmds:
        if command == "UP":
            print("UP")
            if final_integer%matrixSize < 1:
                pass
            else:
                final_integer -= matrixSize
        elif command == "DOWN":
            print("DOWN")
            if final_integer//matrixSize > matrixSize - 1:
                pass
            else:
                final_integer += matrixSize
        elif command == "LEFT":
            print("LEFT")
            if final_integer%matrixSize == 0:
                pass
            else:
                final_integer -= 1
        else:
            print("RIGHT")
            if final_integer%matrixSize == matrixSize - 1:
                pass
            else:
                final_integer += 1

        print(final_integer)

    return final_integer

if __name__ == '__main__':
    print(str(roverMove(3, ["UP"])) + " is equal to 0")
    print(str(roverMove(3, ["DOWN"])) + " is equal to 3")
    print(str(roverMove(3, ["LEFT"])) + " is equal to 0")
    print(str(roverMove(3, ["RIGHT"])) + " is equal to 1")
    print(str(roverMove(3, ["UP", "DOWN"])) + " is equal to 3")
    print(str(roverMove(3, ["UP", "DOWN", "RIGHT"])) + " is equal to 4")
