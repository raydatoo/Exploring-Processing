#-------------------------------
#Name: intro_to_processing.py
#Purpose: Show basic processing stuffs like animation, text, and shapes
#Author: Datoo.R
#Created: 16/11/2018
#-------------------------------

# make global variables
redness = 255
x = 400
y = 100
a = 10
b = 10
presskey = 0
shiploc = 800

#setup and input outside pics
def setup():
    size(800, 800)
    global background_img
    global rocket
    background_img = loadImage("night sky.jpg")
    rocket = loadImage("rocket.png")


def draw():
    
    #intro to program
    if presskey == 0:
        
        background(background_img)
        global rocket
        global shiploc
        image(rocket, 0, shiploc, 200, 200)
        image(rocket, 200, shiploc, 200, 200)
        image(rocket, 400, shiploc, 200, 200)
        image(rocket, 600, shiploc, 200, 200)
        shiploc -= 5
        
        fill(255, 255, 0)
        textSize(36)
        text("Welcome to the", 270, 100)
        text("United Soviet Socialist Galaxy!", 150, 150)
        text("The Notgermans are attacking and", 100, 250)
        text("Smiley needs your help!", 200, 300)
        text("Help him find a place to hide by", 130, 400)
        text("clicking any key on your keyboard!", 110, 450)
        text("But be careful, the more you click your", 70, 550)
        text("mouse, the angrier smiley will become!", 70, 600)
        textSize(64)
        text("Hit any key to continue!", 40, 700)
        
    #make moving smiley at designated key presses     
    if (presskey + 1)%2  == 0:
        global x
        global y
        global a 
        global b
        
        x += a
        y += b
        
        background(background_img)
        if x>= 700:
            a = -a
        if y >= 700:
            b = -b
        if x<= 100:
            a = -a
        if y <= 100:
            b = -b
        fill(255, redness, 0)
        ellipse(x, y, 200, 200)
        fill(255, 255, 255)
        ellipse(x-50, y, 75, 75)
        ellipse(x+50, y, 75, 75)
        fill(128, 0, 0)
        ellipse(x-50, y, 30, 30)
        ellipse(x+50, y, 30, 30)
        arc(x, y+50, 100, 75, 0, PI, CHORD)
        
    #make stopped smiley and star covers    
    if presskey == 2: 
        image(background_img, 275, 0, 225, 225)
        
    if presskey == 4: 
        image(background_img, 575, 275, 225, 225) 
        
    if presskey == 6: 
        image(background_img, 275  , 575, 225, 225) 
              
    if presskey == 8: 
        image(background_img, 0, 275 , 225, 225)
         
    #make name banner in top right    
    fill(192,192,192)    
    triangle(550, 25, 800, 25, 800, 100)
    textSize(25) 
    fill(255, 0, 0)
    text("RAYDATOO", 650, 50)
 


    
#mouse press function to get smiley mad
    
def mousePressed():
    global redness
    redness -= 25
    if redness <= 0:
        redness = 255
    print("smiley has level", int(-(redness - 255)), "anger")
        
#keypress function to play game

def keyPressed():
    global presskey
    presskey += 1 
    if presskey == 9:
        presskey = 1   
    print(presskey)
    
