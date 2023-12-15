from Eingabefeld import *

# Funktion um Zeitzonenangaben zu generieren (+12 / - 9 / ...)
def zeitzonenangabe(verschiebung, x):
    text(verschiebung, x, 20)

# Funktion um Uhr an bestimmten Koordinatenpunkt mit Ortsnamen und Zeitverschiebung zu generieren
def uhr(x,y,Name,TimeOffset):
    
    # Ziffernblatt
    stroke(0,0,0)
    fill(255, 255, 255)
    circle(x, y, 60)
    
    # Zeichnet zwischen 0 und 360 Grad alle 30 Grad einen Stundenstrich
    for angle in range(0, 360, 30):
        pushMatrix()
        translate(x, y)
        rotate(radians(angle))
        line(0, 23, 0, 30)
        popMatrix()
    
    # Nullpunkt des Koordinatensystems ins Zentrum der Uhr
    pushMatrix()
    translate(x, y)
    
    # AngleMinCurrent aktualisieren basierend auf der Zeitverschiebung
    AngleMinCurrent = AngleMin
    
    # ueberpruefen, ob die Zeitverschiebung eine Gleitkommazahl ist
    if isinstance(TimeOffset, float):
        AngleMinCurrent = AngleMin + 60 * (TimeOffset % 1)  * 6
        
    # Minutenzeiger
    rotate(radians(AngleMinCurrent))
    line(0, 0, 0, -20)
    rotate(radians(-(AngleMinCurrent)))
    
    # Stundenzeiger: Pro Stundenminute wechselt der Zeiger um 0.5 Grad * 60 (Umrechnung in Minuten) * Stunde + Offset + Minuten
    AngleHr = 0.5 * ( 60 * (float(zeitteile[0]) + TimeOffset) + float(zeitteile[1]))
    rotate(radians(AngleHr))
    line(0, 0, 0, -10)
    
    # Nullpunkt des Koordinatensystems zuruecksetzen
    popMatrix()
        
    # Beschriftung Stadt
    fill(255, 255, 255)
    rect(x - 30, y + 35, 60, 15)
    fill(0, 0, 0)
    textSize(12)
    textAlign(CENTER)
    text(Name, x, y + 47)
    
def drawmap(TimeSwitzerland): 
    
    # Definiert Liste mit Zeitteilen
    global zeitteile
    zeitteile = TimeSwitzerland.split(".")
    
    # Winkel fuer die Minute (6 Grad)
    global AngleMin
    AngleMin = 6 * float(zeitteile[1])    

    # Winkel fuer die Stunde (0.5 Grad pro Minute)
    global AngleHr
    AngleHr = 0.5 * ( 60 * float(zeitteile[0]) + float(zeitteile[1]))
    
    # Weltkarte einfuegen
    img = loadImage("Weltkarte.jpg")
    image(img, 0, 0)

    # Werbung auf Bild uebermalen
    noStroke()
    fill(171, 225, 243)
    rect(25, 580, 250, 40)
   
    # Zeitzonen abgrenzen
    strokeWeight(1)
    stroke(0, 0, 0)
    fill(0, 0, 0)
    
    # Zeitzonen beschriften
    Timelabel = ["-11", "-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", "0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11", "+12"]
    xTimelabel = [35, 85, 135, 185, 235, 285, 340, 400, 455, 505, 555, 605, 655, 710, 770, 830, 890, 945, 995, 1045, 1095, 1145, 1200, 1255]
    
    # Aus beiden Listen zusammen die Beschriftung an richtigem Ort einfuegen
    for element1, element2 in zip(Timelabel, xTimelabel):
        zeitzonenangabe(element1, element2)

    # Zeichne Zeitzonengrenzen
    xTimeline = [1230, 1175, 1120, 1070, 1020, 970, 920, 860, 800, 740, 680, 630, 580, 530, 480, 430, 370, 310, 260, 210, 160, 110, 60, 10]

    # Aus beiden Listen zusammen die Linien an richtigem Ort zeichnen
    for i in xTimeline:
        line(i, 0, i, 742)
    
    # Zeichne Uhren
    uhr(310, 310, "New York", -6)
    uhr(770, 200, "Moskau", 2)
    uhr(1100, 270, " Tokio", 8)
    uhr(1160, 600, "Sidney", 10)
    uhr(440, 500, "Brasilia", -4)
    uhr(600, 200, "London", -1)
    uhr(900, 360, "Neu-Delhi", 4.5)
    
    # Feld Schweizer Zeit
    fill(255, 255, 255)
    rect(440, 700, 655, 25)
    fill(0, 0, 0)
    textSize(15)
    text("Du hast die folgende Schweizer Zeit eingegeben: " + TimeSwitzerland + "       Mit ENTER kannst du eine neue Zeit eingeben.", 770, 718)
    
