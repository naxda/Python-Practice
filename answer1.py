from cs1robots import *


load_world('test_case1.wld') 
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.015)
  

def pick():
    c = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        c = c+1
    return c


def pickonly():
    y = pick()
    while y < max(y):
        for i in range(y):
            hubo.drop_beeper()
    else:
        for i in range(4):
            hubo.turn_lfet()
    
def throw():
    x = pick()
    for i in range(x):
        hubo.drop_beeper()

def if hubo.left_is_clear():
    hubo.turn_left()
        while hubo.move()
    elif hubo.front_is_clear():
        while hubo.move()
    elif:
        turn_right()
    
def turn_right():
    pass
def turn_around
def go():
    while hubo.front_is_clear():
        hubo.move()
        pick()      
    if not hubo.front_is_clear():
        hubo.turn_left()

def go2():
    while hubo.front_is_clear():
        hubo.move()
        pick()      
    if not hubo.front_is_clear():
        hubo.turn_left()
    




