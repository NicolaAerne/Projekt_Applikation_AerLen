from Einfabefeld import *

    
def uhr(x,y,AngleHr,AngleMin,Name,TimeOffset):
    stroke(0,0,0)
    fill(255,255,255)
    circle(x,y,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(x, y)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(x,y)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + Timeoffset) + float(zeitteile[1]))
    rotate(radians(AngleHr + Timeoffset))
    line(0,0,0, -10)
    popMatrix()
        
    #Titel NewYork
    fill(255,255,255)
    rect(281,344,58,15)
    fill(0,0,0)
    text(Name, 287, 356)
        
def uhrCH():
    stroke(0,0,0)
    strokeWeight(1.75)
    fill(255,255,255)
    circle(xPosCH,yPosCH,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(xPosCH,yPosCH)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(xPosCH,yPosCH)
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
    circle(770,200,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(770, 200)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Moskau
    fill(255,255,255)
    rect(742,234,58,15)
    fill(0,0,0)
    text("Moskau", 751, 246) 
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(770,200)
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
    circle(600,200,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(600, 200)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel London
    fill(255,255,255)
    rect(572,234,58,15)
    fill(0,0,0)
    text("London", 581, 246) 
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(600, 200)
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
    circle(440,500,60)
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(440, 500)
        rotate(radians(angle))
        line(0,23,0,30)
        popMatrix()
        
    #Titel Brasilia
    fill(255,255,255)
    rect(413,534,58,15)
    fill(0,0,0)
    text("Brasilia", 423, 546) 
    
    #Minuten- und Stundenzeiger
    pushMatrix()
    translate(440,500)
    rotate(radians(AngleMin + 6))
    line(0,0,0, -20)
    rotate(radians(-(AngleMin + 6)))
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) - 4) + float(zeitteile[1]))
    rotate(radians(AngleHr + 6))
    line(0,0,0, -10)
    popMatrix()


def drawmap(TimeSwitzerland): 
    global zeitteile
    zeitteile = TimeSwitzerland.split(".")
    global AngleMin
    AngleMin = 6 * float(zeitteile[1])    
    global AngleHr
    AngleHr = 0.5 * ( 60 * float(zeitteile[0]) + float(zeitteile[1]))
    global xPosCH
    xPosCH = 630
    global yPosCH 
    yPosCH = 250

    
    
    #Weltkarte einfuegen
    img = loadImage("Weltkarte.jpg")
    image(img, 0, 0)


    
    
    
    #Werbung auf Bild uebermalen
    noStroke()
    fill(171,225,243)
    rect(25, 580, 250, 40)
    #Zeitzonen abgrenzen
    strokeWeight(1)
    stroke(0,0,0)
    #x = 630
    #for i in range(x,1280):
    #   line(x,0,x,742)
    #   x = x + 56
        
    #for i in range(0,x):
    #   line(x,0,x,742)
    #  x = x - 56
    
    Timezone = -11
    xPosTimezone = 50
    

    text("-11", 30, 20)
    text("-10", 80, 20)
    text("-9", 130, 20)
    text("-8", 180, 20)
    text("-7", 230, 20)
    text("-6", 280, 20)
    text("-5", 335, 20)
    text("-4", 395, 20)
    text("-3", 450, 20)
    text("-2", 500, 20)
    text("-1", 550, 20)
    text("0", 600, 20)
    text("+1", 650, 20)
    text("+2", 705, 20)
    text("+3", 765, 20)
    text("+4", 825, 20)
    text("+5", 885, 20)
    text("+6", 940, 20)
    text("+7", 990, 20)
    text("+8", 1040, 20)
    text("+9", 1090, 20)
    text("+10", 1140, 20)
    text("+11", 1195, 20)
    text("+12", 1245, 20)

    
#schrib abstand du adusvabdfialjb
    line(1230, 0, 1230, 742) 
    line(1175, 0,1175,742)  
    line(1120, 0,1120,742)  
    line(1070, 0,1070,742)  
    line(1020, 0,1020,742)
    line(970,0,970,742)
    line(920,0,920,742)
    line(860,0,860,742)
    line(800,0,800,742)
    line(740,0,740,742)
    line(680,0,680,742)
    line(630,0,630,742)
    line(580,0,580,742)
    line(530,0,530,742)
    line(480,0,480,742)
    line(430,0,430,742)
    line(370,0,370,742)
    line(310,0,310,742)
    line(260,0,260,742)
    line(210,0,210,742)
    line(160,0,160,742)
    line(110,0,110,742)
    line(60,0,60,742)
    line(10,0,10,742)

    uhrNY()
    uhrMO()
    uhrTO()
    uhrSI()
    uhrBR()
    uhrLO()
    
