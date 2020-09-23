# GreetingCard.py
# Marcela Gomez

# The program uses a GUI to get the imput of a name then opens a
#greeting card with the persons name and decorated border with a loop.

from graphics import*
from random import *

def main():

    #Input Window
    win = GraphWin("Enter Name", 600, 600)
    win.setBackground("Orange")
    win.setCoords(0,0, 30, 30)

    box = Rectangle(Point(8, 10),Point(22,6))
    box.draw(win)

    name = Text(Point (15,18), "Enter Your Name")
    name.draw(win)
    name.setSize(36)
    name.setTextColor("Black")

    nameEntry = Entry(Point(15,16), 20)
    nameEntry.draw(win)
    nameEntry.setSize(24)
    nameEntry.setTextColor("Black")
    nameEntry.setFill("White")

    text1 = Text(Point(15,8),"Click To Continue")
    text1.draw(win)
    text1.setTextColor("Black")
    text1.setSize(20)

    win.getMouse()

    name = nameEntry.getText()
    print(name)

    win.close()

    #Greeting Card with name entry
    win = GraphWin("Greeting Card", 800,800)
    win.setBackground("Black")
    win.setCoords(0,0, 40,40)
    
    text2 = Text(Point(20,33), "H A P P Y    H A L L O W E E N ")
    text2.draw(win)
    text2.setSize(36)
    text2.setTextColor("Orange")
    

    text3 = nameEntry.getText()
    text3 = Text(Point(20,7), text3)
    text3.draw(win)
    text3.setTextColor("Orange")
    text3.setSize(36)
    
    #Smile
    oval = Oval(Point(8,12),Point(32, 26))
    oval.draw(win)
    oval.setFill("White")

    oval = Oval(Point(8,12.35),Point(32,26.35))
    oval.draw(win)
    oval.setFill("Black")

    #Left Tooth
    triangle = Polygon(Point(13,13.4), Point(15,12.8), Point(12,10))
    triangle.draw(win)
    triangle.setFill("White")
    triangle.setOutline("White")

    polygon = Polygon(Point(13,13.4),Point(15,12.8),Point(13.9,11.85),Point(12.7,12.35))
    polygon.draw(win)
    polygon.setFill("Yellow")
    polygon.setOutline("Yellow")

    polygon = Polygon(Point(13.9,11.85),Point(12.7,12.35),Point(12.3,11.2),Point(13,10.9))
    polygon.draw(win)
    polygon.setFill("Orange")
    polygon.setOutline("Orange")
    
    #Right Tooth
    triangle = Polygon(Point(27,13.4),Point(25,12.8),Point(28,10))
    triangle.draw(win)
    triangle.setFill("White")
    triangle.setOutline("White")

    polygon = Polygon(Point(27,13.4),Point(25,12.8),Point(25.9,12), Point(27.25,12.5))
    polygon.draw(win)
    polygon.setFill("yellow")
    polygon.setOutline("Yellow")

    polygon = Polygon(Point(25.9,12), Point(27.25,12.5), Point(27.6,11.25), Point(27, 11))
    polygon.draw(win)
    polygon.setFill("Orange")
    polygon.setOutline("Orange")

    #Left Cheek
    circ =Circle( Point(7.75,18), 2)
    circ.draw(win)
    circ.setFill("White")

    circ = Circle(Point(7.5,18.25), 2.1)
    circ.draw(win)
    circ.setFill("Black")

    #Right Cheek
    circ = Circle(Point(32.75,18),2)
    circ.draw(win)
    circ.setFill("White")

    circ = Circle(Point(33,18.25),2.1 )
    circ.draw(win)
    circ.setFill("Black")

    # Left Eye
    oval = Oval(Point(19.5,26),Point(14,19))
    oval.draw(win)
    oval.setFill("White")

    circ = Circle(Point(17.75,23), 1.4)
    circ.draw(win)
    circ.setFill("Black")

    circ = Circle(Point(18.5,23.5), 0.35)
    circ.draw(win)
    circ.setFill("White")

    # Right Eye
    oval = Oval(Point( 20.5,26),Point( 26,19))
    oval.draw(win)
    oval.setFill("White")

    circ = Circle(Point(22.25,23), 1.4)
    circ.draw(win)
    circ.setFill("Black")

    circ = Circle(Point(21.5,23.5), 0.35)
    circ.draw(win)
    circ.setFill("White")
                 
    for i in range (0, 39, +3):
        circ = Circle(Point(1, 1 + i), 0.5)
        circ.draw(win)
        circ.setFill("White")

        circ = Circle(Point(1 + i, 1), 0.5)
        circ.draw(win)
        circ.setFill("White")

        circ = Circle(Point(1+i, 38.5), 0.5)
        circ.draw(win)
        circ.setFill("white")

        circ = Circle(Point(38.5, 1+i), 0.5)
        circ.draw(win)
        circ.setFill("white")

        time.sleep(.2)

    for i in range(0, 39, 3):
        square = Polygon(Point(.75,2 + i), Point(1.75,2 + i ),Point(1.75,3 + i),Point(.75,3 + i))
        square.draw(win)
        square.setFill("Orange")

        square = Polygon(Point(1.75 +i ,0.75), Point(2.75 + i,0.75), Point(2.75 + i, 1.75),Point(1.75 + i,1.75))
        square.draw(win)
        square.setFill("Orange")

        square = Polygon(Point(38.75 - i, 38.75),Point(39.75 - i, 38.75),Point(39.75 - i, 39.75), Point(38.75 - i, 39.75))
        square.draw(win)
        square.setFill("Orange")

        square = Polygon(Point(38.75,38.75 - i),Point(39.75,38.75 - i),Point(39.75,39.75 - i), Point(38.75, 39.75 - i))
        square.draw(win)
        square.setFill("Orange")

        time.sleep(.2)

    for i in range(0, 39, 3):
        triangle = Polygon(Point(.75, 1.25 + i), Point(1.75, 1.25 + i), Point(1.25, 2.25 + i))
        triangle.draw(win)
        triangle.setFill("yellow")

        triangle = Polygon(Point(.75 + i, 1.25),Point(1.75 + i, 1.25),Point(1.25 + i, 2.25))
        triangle.draw(win)
        triangle.setFill("yellow")

        triangle = Polygon(Point(38.75,38.25 - i),Point(39.75, 38.25 - i),Point(39.25,39.25 - i))
        triangle.draw(win)
        triangle.setFill("yellow")
         
        triangle = Polygon(Point(38.75 - i, 38.25),Point(39.75 - i, 38.25),Point(39.25 - i,39.25))
        triangle.draw(win)
        triangle.setFill("yellow")

        time.sleep(.2)


main()
