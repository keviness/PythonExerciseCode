# draw a polygon witn mouse point 2018.10.29

from graphics import *

win = GraphWin("Draw Polygon", 500, 600)
win.setCoords(0.0, 0.0, 300.0, 300.0)
message = Text(Point(200, 20), "Click on five points")


p1 = win.getMouse()

p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
p4 = win.getMouse()
p4.draw(win)
p5 = win.getMouse()
p5.draw(win)

polgy = Polygon(p1, p2, p3, p4, p5)

polgy.setOutline("red")


message.setText("click anywhere to quit.")
win.getMouse()
win.close()