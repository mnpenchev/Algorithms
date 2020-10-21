""" robot is standing at coords i.e. SL(2,2) in a 2D grid, given astring consisting his moves
 find the final location(FL) of the robot. If FL==SL return True
 command are U,D,L,R. U(0,+1) D(0, -1), L(-1,0), R(+1,0) """


class Sol:
    def check(self, moves):
        x = 0
        y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x==0 and y==0


s = Sol()
a = s.check("URRDL")
b = s.check("UD")
print(a, b)
