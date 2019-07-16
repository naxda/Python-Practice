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

def turn_right():
    pass

def travel():
    while hubo.front_is_clear():
        hubo.move()
        pick()      
    for i in range(2):
        hubo.turn_left()

def travel2():
    while hubo.front_is_clear():
        hubo.move()
        pickonly()      
    for i in range(2):
        hubo.turn_left()
 
def comeback():
    while hubo.front_is_clear():
        hubo.move()

def goback():
    travel()
    comeback()

def world():
    while hubo.front_is_clear():
        travel()
        comeback()
        for i in range(3):
            hubo.turn_left()
        hubo.move()
        for i in range(3):
            hubo.turn_left()        

def world2():
    while hubo.front_is_clear():
        travel2()
        comeback()
        hubo.move()
        for i in range(3):
            hubo.turn_left()        
    travel()
    comeback()  



def prepare():
    world()
    for i in range(2):
        hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    

def execute():
    world()
    for i in range(2):
        hubo.turn_left()


world()


    




