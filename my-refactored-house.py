import graphics as g
from graphics import *

win = g.GraphWin( 'Click to switch from day to night', 1000, 500)
def roof():
    CenterPointRoof = g.Point( 500, 100 )
    LeftRoofLine = g.Line( g.Point( 400, 150 ), CenterPointRoof )
    LeftRoofLine.draw( win )
    RightRoofLine = g.Line( g.Point( 600, 150 ), CenterPointRoof )
    RightRoofLine.draw( win )
    return roof

def sun():
    ExtraDot = g.Point( 300, 75 )
    ExtraDot.draw( win )
    Sun = g.Circle( ExtraDot, 25 )
    Sun.setFill( 'yellow' )
    Sun.draw( win )
    return sun

def house():
    Housebody = g.Rectangle( g.Point( 400, 150 ), g.Point( 600, 400) )
    Housebody.draw( win )
    Window = g.Rectangle( g.Point( 500, 200 ), g.Point( 550, 250 ))
    Window.setFill( 'brown' )
    Window.draw( win )
    Door = g.Rectangle( g.Point( 450, 300 ), g.Point( 500, 400 ))
    Door.draw( win )
    return house

def bushes():
    point1 = g.Point( 250, 400 )
    bush1 = g.Circle( point1, 25)
    bush1.setFill( 'green' )
    bush1.draw( win )
    point2 = g.Point( 200, 400)
    bush2 = g.Circle( point2, 25)
    bush2.setFill( 'green' )
    bush2.draw( win )
    point3 = g.Point( 150, 400)
    bush3 = g.Circle( point3, 25)
    bush3.setFill( 'green' )
    bush3.draw( win )
    return bushes

def tree():
    Treetrunk = g.Rectangle( g.Point( 750, 250 ), g.Point( 775, 400) )
    Treetrunk.setFill( 'brown' )
    Treetrunk.draw( win)
    point4 = g.Point( 763, 199)
    Treetop = g.Circle( point4, 50)
    Treetop.setFill( 'green' )
    Treetop.draw( win )
    return tree
    
def windlines():
    firstline = g.Line( g.Point( 700, 100), g.Point( 800, 100 ))
    firstline.draw( win )
    secondline = g.Line( g.Point( 710, 115), g.Point(810, 115))
    secondline.draw( win )
    thirdline = g.Line(g.Point( 720, 130), g.Point(830, 130))
    thirdline.draw( win )
    return windlines
    
    

def main():
    roof()
    sun()
    house()
    bushes()
    tree()
    windlines()
    win.getMouse()
    Text( Point( 300, 50 ), 'Goodnight' ).draw( win )
    win.setBackground( 'black' )
    win.getMouse()
    win.setBackground('white')
    win.getMouse()
    win.close()
    
main()
