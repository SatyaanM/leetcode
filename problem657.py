class Solution:
    def judgeCircle(self, moves: str) -> bool:
        robot = [0, 0]
        for move in moves:
            if move == 'R':
                robot[0] += 1
            if move == 'L':
                robot[0] -= 1
            if move == 'U':
                robot[1] += 1
            if move == 'D':
                robot[1] -= 1
        if robot == [0, 0]:
            return True
        else:
            return False