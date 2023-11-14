TimeSwitzerland = "22:22"
zeitteile = TimeSwitzerland.split(":")
AngleMin = 6 * float(zeitteile[1])
AngleHr = 0.5 * ( 60 * float(zeitteile[0]) + float(zeitteile[1]))
eingabe = ""
 
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
    strokeWeight(1.75)
    fill(255,255,255)
    circle(630,250,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(630, 250)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(630,250)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
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
        
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(310,310)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) - 6) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(1100,270)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + 8) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()
    
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(1160,600)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + 10) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()
    
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(900,360)
    MinutenDL = float(zeitteile[1]) + 30
    AngleMin = 6 * (MinutenDL)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    if MinutenDL > 60:
        AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + 5) + float(zeitteile[1]))
        rotate(radians(AngleHr + 6))
        line(0,0,0, -10)
    else:
        AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + 4) + float(zeitteile[1]))
        rotate(radians(AngleHr + 6))
        line(0,0,0, -10)
    popMatrix()
    
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(750,200)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + 2) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()
    
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(550, 200)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) - 1) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()
    
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
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(465,500)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) - 4) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()
    
def draw(): 
    uhrCH()
    uhrNY()
    uhrMO()
    uhrTO()
    uhrSI()
    uhrBR()
    uhrLO()
    uhrND()
