from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )


color = [ 0, 0, 0 ]

def herm(x0, y0, x1, y1, rx0, ry0, rx1, ry1):
    return ('hermite\n%d %d %d %d %d %d %d %d\n' % (x0,y0,x1,y1,rx0,ry0,rx1,ry1))

def bez(x0, y0, x1, y1, x2, y2, x3, y3):
    return ('bezier\n%d %d %d %d %d %d %d %d\n' % (x0,y0,x1,y1,x2,y2,x3,y3))

def line(x0,y0,z0,x1,y1,z1):
    return ('line\n%d %d %d %d %d %d\n' % (x0,y0,z0,x1,y1,z1))

def circ(x,y,z,r):
    return ('circle\n%d %d %d %d\n' % (x,y,z,r))

#takes 8 arguments (x0, y0, x1, y1, rx0, ry0, rx1, ry1)

def modify_script():
    f = open('script','w')

    
    #check lines
    '''
    f.write(line(375,140,0,375,168,0)) #top for split
    f.write(line(60,180,0,60,155,0))   #top for split
    f.write(line(100,167,0,100,200,0)) #bottom for split
    f.write(line(242,152,0,242,170,0)) #top for split

    f.write(line(242,122,0,242,92,0)) #top is for mouth top intersect
    f.write(line(145,130,0,145,100,0)) #top is mouth top
    f.write(line(278,120,0,278,90,0)) #top is mouth top
    f.write(line(100,138,0,100,100,0)) #top mouth top
    f.write(line(350,130,0,350,100,0))
    f.write(line(80,145,0,80,110,0))

    f.write(line(135,92,0,135,60,0)) #top mouth bottom
    f.write(line(327,99,0,327,60,0))
    '''

    #f.write(line(100,256,0,100,227,0))
    #f.write(line(242,246,0,242,217,0))

    '''
    left eyebrow check
    f.write(line(84,370,0,84,400,0))  #bottom is for left brow  #curving pt
    f.write(line(100,347,0,100,377,0))
    f.write(line(121,309,0,121,340,0))
    f.write(line(60,342,0,60,370,0))
    '''

    '''
    right eyebrow check
    not finished

    #200 222
    f.write(line(200,278,0,200,300,0)) #bottom for right brow
    f.write(line(306,375,0,306,400,0))  #bottom is turning point
    f.write(line(242,400,0,242,323,0)) #bottom is brow
    f.write(line(349,341,0,349,400,0)) #bottom
    f.write(line(263,344,0,263,400,0))
    '''
    
    #check lines end

    f.write(circ(250,250,0,250)) #circle
    f.write(herm(4,210,498,240,200,-250,50,310)) #splitter
    
    f.write(herm(60,155,375,140,100,-105,50,70)) #top mouth
    
    f.write(herm(80,145,350,130,440,-430,70,150)) #bottom mouth
    
    f.write(line(256,99,0,256,66,0)) #right tooth
    f.write(line(200,83,0,200,69,0)) #left tooth

    for x in range(96,104): #left eye
        f.write(line(x,256,0,x,227,0))    
    for x in range(238,246): #right eye
        f.write(line(x,246,0,x,217,0))   

    f.write(herm(44,295,129,287,150,470,100,-150)) #left eyebrow
    f.write(herm(196,270,368,317,0,50,0,-50))  #improv right eyebrow
    
    f.write('save\ne.png\n')
    f.close()

#modify_script()

parse_file( 'script', edges, transform, screen, color )
