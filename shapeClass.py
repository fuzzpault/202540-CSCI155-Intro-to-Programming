import sys
import os
import time
import math

FRAME_DURATION = 1/30

class Tree:
    def __init__(self):
        self.t =   ["  ^  ",
                    " /|\\ ",
                    "/ | \\"]
        
    def getLoc(self, x, y):
        return shift_Y(shift_X(self.t, x), y)
    
    def flipY(self):
        self.t.reverse()

def make_dot(i: int, w: int, c: str)  -> str:
    return (" " * (i)) + c + (" " * (w - i - len(c)))

#def make_tree():
#    return ["  ^  ",
#            " /|\\ ",
#            "/ | \\"]

def shift_X(ob: [str], x: int) -> [str]:
    ret = []
    for line in ob:
        ret.append((" " * x) + line)
    return ret

def shift_Y(ob: [str], y: int) -> [str]:
    return ([''] * y) + ob

def makeHeight(ob: [str], y: int) -> [str]:
    return ob + ([''] * (y - len(ob)))


#def merge(data: [[str]]) -> [str]:  # A list of images
#    ret = []
#    for y in range(len(data[0])):
#        for x in range(len(data[0][0]))


#    return ret

def print2d(ob: [str]):
    for line in ob:
        print(line)

tree1 = Tree()
tree1.flipY()

print(tree1.t)

sys.exit(1)
for frame_i in range(360):
    # max 20, min -20
    y = math.sin(frame_i * math.pi / 180) * 20 + 20
    x = math.cos(frame_i * math.pi / 180) * 20 + 20
    x = x * 2
    #print(x,y)
    os.system('clear')
    print2d( makeHeight(tree1.getLoc(int(x), int(y)), 40))
    #print2d( makeHeight(tree1.getLoc(int(40-x), int(40-y)), 40))
    time.sleep(FRAME_DURATION)

    #for x in range(10,0,-1): # Dot moves to the left
    #    os.system('clear')
    #    print2d( shift_Y(shift_X(make_tree(), x), x))
    #    time.sleep(FRAME_DURATION) 
