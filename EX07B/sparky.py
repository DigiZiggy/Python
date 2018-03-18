"""Simulation."""


def map_size(wmap, row, col):
    """
    Defining how can Sparky move.

    :param wmap:
    :param row:
    :param col:
    :return:
    """
    if row < 0 or row >= len(wmap) or col < 0 or col >= len(wmap[0]):
        return False
    if wmap[row][col] == "#":
        return False
    return True


def simulate(wmap: list, moves: list) -> list:
    """
    Simulate a robotic lawn mower.

    :param wmap: A list of strings indicating rows that make up the map.
                 The map is always rectangular and the minimum given size is 1x1.
                 Cut grass is indicated by the symbol ('-'), low grass by ('w') and high grass by ('W').
                 The robot position is indicated by the symbol ('X'). There is always one robot on the map.
                 Obstacles are indicated by the symbol ('#').

    :param moves: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the robot out of bounds or crash it into an obstacle.

    :return: A list of strings indicating rows that make up the map. Same format as the given wmap.

    Grass under Sparky's starting position is always cut grass ('-').
    If Sparky mows high grass, it first turns into low grass ('w') and then from low grass into cut grass ('-').
    """
    srow, scol = 0, 0
    mm = []
    for rowi, row in enumerate(wmap):
        mrow = []
        for coli, space in enumerate(row):
            if space == "X":
                srow = rowi
                scol = coli
                space = "-"
            mrow.append(space)
        mm.append(mrow)
        print(mrow)

    for move in moves:
        trow, tcol = srow, scol
        for i in range(1, 3):
            if move == "N":
                trow = srow - 1
            if move == "S":
                trow = srow + 1
            if move == "W":
                tcol = scol - 1
            if move == "E":
                tcol = scol + 1
                can = map_size(mm, trow, tcol)
                if not can:
                    break
        srow = srow - 1
        scol = scol - 1
        scol = scol + 1
        srow = srow + 1


    result = ""
    for rowi, row in enumerate(mm):
        for coli, col in enumerate(row):
            if rowi == srow and coli ==scol:
                result += "X"
            else:
                result += col
        result += "\n"
    print(result)
    return result


if __name__ == '__main__':
    wmap1 = [
        "#www-",
        "wXw#-",
    ]

    moves1 = ["N", "E", "E", "S", "E"]
    print("\n".join(simulate(wmap1, moves1)))

    # #---X
    # w-w#-

 #   assert simulate(wmap1, moves1) == ["#---X", "w-w#-"]

    print()

    wmap2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    moves2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print("\n".join(simulate(wmap2, moves2)))

    # wwwW
    # ---W
    # -X#W

 #   assert simulate(wmap2, moves2) == ["wwwW", "---W", "-X#W"]