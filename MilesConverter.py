# MilesConverterGUI.py
# Marcela Gomez

# This program uses a graphical  user interface to get the input of miles
# then once the user clicks, it converts the miles to km and shows the output.

from graphics import*
def main():
    
    win = GraphWin("Mile Converter", 500, 500)
    win.setBackground("Navy")
    win.setCoords(0,0,10,10)

    prompt1=Text(Point(5,8), "Enter distance in miles.")
    prompt1.draw(win)
    prompt1.setSize(30)
    prompt1.setTextColor("Chartreuse")

    miles_input = Entry(Point(5,7),5)
    miles_input.setSize(18)
    miles_input.setTextColor("Dark Slate Blue")
    miles_input.setFill("White")
    miles_input.draw(win)

    prompt2=Text(Point(5,3), "Distance in km.")
    prompt2.draw(win)
    prompt2.setSize(30)
    prompt2.setTextColor("Chartreuse")

    km_output = Text(Point (5,2), "")
    km_output.setSize(30)
    km_output.setFill("Chartreuse")
    km_output.draw(win)

    button = Text(Point(5,6),"Click to Convert")
    button.setSize(30)
    button.draw(win)
    button.setTextColor("White")
    Rectangle(Point(3,5.5),Point (7,6.5)).draw(win)
    
    win.getMouse()
    
    miles = eval(miles_input.getText())
    kilometers = miles * 1.61
    round(kilometers, 2)
    print("The distance", miles,"mile(s) is", round(kilometers,1), "kilometer(s).") 

    km_output.setText(kilometers)
    button.setText("Click to Quit")
    
    win.getMouse()
    win.close()

main()
