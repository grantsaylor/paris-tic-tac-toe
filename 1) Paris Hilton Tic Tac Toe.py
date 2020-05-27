#Drawing the window
from graphics import *
win = GraphWin("Paris' Tic Tac Toe", 300,320)

c1 =  Rectangle(Point(0,0), Point(400,400))
c1.setFill('#FF2FB4')
c1.draw(win)

c2 =  Rectangle(Point(0,0), Point(320,20))
c2.setFill('pink')
c2.draw(win)

import pygame

#Graphic for the HUD
Text(Point(150,10), "❤ Paris' Tic Tac Toe ❤").draw(win)

#The points of my perimeter
p1 = Point(2, 22)
p1.draw(win)

p2 = Point(300, 22)
p2.draw(win)

p3 = Point(2, 320)
p3.draw(win)

p4 = Point(300, 320)
p4.draw(win)

p5 = Point(100, 22)
p5.draw(win)

p6 = Point(200, 22)
p6.draw(win)

p7 = Point(100, 320)
p7.draw(win)

p8 = Point(200, 320)
p8.draw(win)

p9 = Point(2, 120)
p9.draw(win)

p10 = Point(2, 220)
p10.draw(win)

p11 = Point(300, 120)
p11.draw(win)

p12 = Point(300, 220)
p12.draw(win)

#Lines to form my grid
l1 = Line(p1,p2)
l1.draw(win)

l2 = Line(p3,p4)
l2.draw(win)

l3 = Line(p1,p3)
l3.draw(win)

l4 = Line(p2,p4)
l4.draw(win)

l5 = Line(p5,p7)
l5.draw(win)

l6 = Line(p6,p8)
l6.draw(win)

l7 = Line(p9,p11)
l7.draw(win)

l8 = Line(p10,p12)
l8.draw(win)

#Matrix of the table
entries = [
    [-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]
]

#Current Player
current_player = 0

while True:
    #Tracking the mouse click
    p = win.getMouse() 

    #Assigning rows and columns 
    row = 0
    if p.getY() in range(120,220):
        row = 1
    elif p.getY() in range(220,320):
        row = 2
    
    column = 0
    if p.getX() in range(100,200):
        column = 1
    elif p.getX() in range(200,300):
        column = 2

    #Centering the marks inside each cell
    x = 50 + column*100
    y = 70 + row*100

    #If the cell is empty, draw... 
    if entries[row][column] == -1:
    
        #Drawing the players marks
        if current_player == 0:
            t = Text(Point(x,y), '❤')
            t.draw(win)
            pygame.mixer.init()
            pygame.mixer.music.load("thats_hot.mp3")
            pygame.mixer.music.play()
            c13 =  Rectangle(Point(0,0), Point(320,20))
            c13.setFill('pink')
            c13.draw(win)
            Text(Point(150,10), "❤ Paris' Tic Tac Toe ❤").draw(win)
        else:
            t = Text(Point(x,y), '★')
            t.draw(win)
            pygame.mixer.init()
            pygame.mixer.music.load("oh_my_god.mp3")
            pygame.mixer.music.play()
            c14 =  Rectangle(Point(0,0), Point(320,20))
            c14.setFill('pink')
            c14.draw(win)
            Text(Point(150,10), "❤ Paris' Tic Tac Toe ❤").draw(win)
        
        entries[row][column] = current_player
       
        #Horizonal winning condition for Player 0
        if entries[row][0] == 0 and entries[row][1] == 0 and entries[row][2] == 0:
            print("Player ❤ is the hottest!")
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c3 =  Rectangle(Point(0,0), Point(320,20))
            c3.setFill('pink')
            c3.draw(win)
            Text(Point(150,10), "Player ❤ is the hottest!").draw(win)
            X = input("Press ENTER to close")
            break

        #Vertical winning condition for Player 0
        if entries[0][column] == 0 and entries[1][column] == 0 and entries[2][column] == 0:
            print("Player ❤ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c4 =  Rectangle(Point(0,0), Point(320,20))
            c4.setFill('pink')
            c4.draw(win)
            Text(Point(150,10), "Player ❤ is the hottest!").draw(win)        
            X = input("Press ENTER to close")    
            break

        #Horizontal winning condition for Player 1
        if entries[row][0] == 1 and entries[row][1] == 1 and entries[row][2] == 1:
            print("Player ★ is the hottest!")
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c5 =  Rectangle(Point(0,0), Point(320,20))
            c5.setFill('pink')
            c5.draw(win)
            Text(Point(150,10), "Player ★ is the hottest!").draw(win)   
            X = input("Press ENTER to close")         
            break
        
        #Vertical winning condition for Player 1
        if entries[0][column] == 1 and entries[1][column] == 1 and entries[2][column] == 1:
            print("Player ★ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c6 =  Rectangle(Point(0,0), Point(320,20))
            c6.setFill('pink')
            c6.draw(win)
            Text(Point(150,10), "Player ★ is the hottest!").draw(win)
            X = input("Press ENTER to close")
            break

        #Diagonal winning condition for Player 0
        if entries[0][0] == 0 and entries[1][1] == 0 and entries[2][2] == 0:
            print("Player ❤ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c7 =  Rectangle(Point(0,0), Point(320,20))
            c7.setFill('pink')
            c7.draw(win)
            Text(Point(150,10), "Player ❤ is the hottest!").draw(win)
            X = input("Press ENTER to close")
            break

        if entries[0][2] == 0 and entries[1][1] == 0 and entries[2][0] == 0:
            print("Player ❤ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c8 =  Rectangle(Point(0,0), Point(320,20))
            c8.setFill('pink')
            c8.draw(win)
            Text(Point(150,10), "Player ❤ is the hottest!").draw(win) 
            X = input("Press ENTER to close")
            break

        #Diagonal winning condition for Player 1
        if entries[0][0] == 1 and entries[1][1] == 1 and entries[2][2] == 1:
            print("Player ★ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c9 =  Rectangle(Point(0,0), Point(320,20))
            c9.setFill('pink')
            c9.draw(win)
            Text(Point(150,10), "Player ★ is the hottest!").draw(win)
            X = input("Press ENTER to close")
            break

        if entries[0][2] == 1 and entries[1][1] == 1 and entries[2][0] == 1:
            print("Player ★ is the hottest!") 
            pygame.mixer.init()
            pygame.mixer.music.load("very_sexy.mp3")
            pygame.mixer.music.play()
            c10 =  Rectangle(Point(0,0), Point(320,20))
            c10.setFill('pink')
            c10.draw(win)
            Text(Point(150,10), "Player ★ is the hottest!").draw(win)
            X = input("Press ENTER to close")
            break

        #Non winning winning condition for Players      
        if entries[0][0] != -1 and entries[0][1] != -1 and entries[0][2] != -1 and entries[1][0] != -1 and entries[1][1] != -1 and entries[1][2] != -1 and entries[2][0] != -1 and entries[2][1] != -1 and entries[2][2] != -1:
            print("Stupid bitch, no one won.")
            pygame.mixer.init()
            pygame.mixer.music.load("private_screenings.mp3")
            pygame.mixer.music.play()
            c11 =  Rectangle(Point(0,0), Point(320,20))
            c11.setFill('pink')
            c11.draw(win)
            Text(Point(150,10), "Ugh, no one won").draw(win) 
            X = input("Press ENTER to close")    
            break    

        #Alternation of players
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0
    
    #If the cell is full, do this instead...
    else:
        print("Someone hotter already picked that square, get your own.")
        c12 =  Rectangle(Point(0,0), Point(320,20))
        c12.setFill('pink')
        c12.draw(win)
        Text(Point(150,10), "Someone hotter already picked that square").draw(win) 

#A game written by Grant Saylor 2/28/18
