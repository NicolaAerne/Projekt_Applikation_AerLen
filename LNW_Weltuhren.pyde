def setup():
    size(1280, 742)
    #Weltkarte einfügen
    img = loadImage("WorldMap.jpg")
    image(img, 0, 0)
    #Werbung auf Bild übermalen
    noStroke()
    fill(171,225,243)
    rect(25, 580, 250, 40)
 
def uhrCH():
    stroke(0,0,0)
    fill(255,255,255)
    circle(630,250,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(630, 250)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Schweiz
    fill(255,255,255)
    rect(601,284,58,15)
    fill(0,0,0)      
    text("Schweiz", 610, 296)
    
def uhrNY():
    stroke(0,0,0)
    fill(255,255,255)
    circle(310,310,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(310, 310)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel NewYork
    fill(255,255,255)
    rect(281,344,58,15)
    fill(0,0,0)
    text("New York", 287, 356)
 
def uhrTO():
    stroke(0,0,0)
    fill(255,255,255)
    circle(1100,270,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(1100, 270)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Tokio
    fill(255,255,255)
    rect(1073,304,58,15)
    fill(0,0,0)
    text("Tokio", 1088, 316)
    
def uhrSI():
    stroke(0,0,0)
    fill(255,255,255)
    circle(1160,600,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(1160, 600)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Sydney
    fill(255,255,255)
    rect(1132,635,58,15)
    fill(0,0,0)
    text("Sydney", 1142, 647) 
        
def uhrND():
    stroke(0,0,0)
    fill(255,255,255)
    circle(900,360,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(900, 360)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Neu-Dehli
    fill(255,255,255)
    rect(872,394,58,15)
    fill(0,0,0)
    text("Neu-Dehli", 877, 406) 
    
def uhrMO():
    stroke(0,0,0)
    fill(255,255,255)
    circle(750,200,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(750, 200)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Moskau
    fill(255,255,255)
    rect(722,234,58,15)
    fill(0,0,0)
    text("Moskau", 731, 246) 
    
def uhrLO():
    stroke(0,0,0)
    fill(255,255,255)
    circle(550,200,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(550, 200)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel London
    fill(255,255,255)
    rect(522,234,58,15)
    fill(0,0,0)
    text("London", 531, 246) 
    
def uhrBR():
    stroke(0,0,0)
    fill(255,255,255)
    circle(465,500,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(465, 500)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Brasilia
    fill(255,255,255)
    rect(438,534,58,15)
    fill(0,0,0)
    text("Brasilia", 448, 546) 
 
def draw(): 
    uhrCH()
    uhrNY()
    uhrMO()
    uhrTO()
    uhrSI()
    uhrBR()
    uhrLO()
    uhrND()
