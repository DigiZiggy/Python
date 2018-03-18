class NoMoreMoves(Exception):
    pass

class InvalidMove(Exception):
    pass

class World:
    def __init__(self, wmap):
        # robot location should be set based on the map
        # this could also be don in "add_robot" method.
        self.robots = []
        pass

    def add_robot(self, robot):
        self.robots.append(robot)

    def is_valid_move(self, old_location, new_location):
        # check is the move is valid
        # e.g. you cannot move outside the map
        # you cannot move more than 1 tile
        # you cannot move to another robot nor wall
        return True

    def run(self):
        # DO NOT CHANGE THIS
        moves_done = [False] * len(self.robots)
        while True:
            for i, robot in enumerate(self.robots):
                if moves_done[i]: continue
                try:
                    old_position = (robot.x, robot.y)
                    new_position = robot.move()

                    if robot.x != old_position[0] or robot.y != old_position[1]:
                        raise InvalidMove("Robot x and y cannot change in move().")
                    if not self.is_valid_move(old_position, new_position):
                        raise InvalidMove(f"Cannot move from {old_position} to {new_position}!")

                    # let's move the robot
                    robot.x = new_position[0]
                    robot.y = new_position[1]

                    # if the move is ok, let's process it
                    self.after_move(old_position, new_position)

                except NoMoreMoves:
                    moves_done[i] = True
            if all(moves_done):
                break

    def after_move(self, old_position, move_result):
        # Use this to do something (e.g. modify the map) after the move
        # old_position is the (x, y) of the robot before the move
        # move_result is what Robot.move() returns.
        # Robot.move() has to return (x, y) as first 2 values,
        # If needed, you can return something in addition (third element etc).
        pass

    def get_map(self):
        # return map with objects as list of string (rows)
        pass


class Robot:
    def __init__(self, world, name, moves):
        # you need x and y members (World uses those)
        self.x = -1
        self.y = -1
        pass

    def move(self):
        # return the new location of the robot.
        # DO NOT make the move here, world will validate the returned move. If it's ok, the robot will be moved.
        # process "next" move in the list

        # in case of invalid move, just return the same location and move to the next move

        # in case the robot has to move to a place of another robot, the move is not executed
        # and is queued - on the next call, try to same move.

        # this should be raised after all the moves are processed
        raise NoMoreMoves("but this is not correct")
        pass

if __name__ == '__main__':
    wmap = [
        "#wwww",
        "XWY#-",
    ]
    w = World(wmap)

    x = Robot(w, "X", ["E", "N", "E", "E"])
    y = Robot(w, "Y", ["W", "N", "E", "S", "E"])

    w.add_robot(x)
    w.add_robot(y)

    print(w.get_map())  # => ['#wwww', 'XWY#-']
    print("\n".join(w.get_map()))
    """
    #wwww
    XWY#-
    """

    w.run()

    print(w.get_map())  # => ['#--Xw', '--Y#-']
    print("\n".join(w.get_map()))
    """
    #--Xw
    --Y#-
    """