from Eingabefeld import *
from Weltkarte import *

status = "eingabe"
error_status = False
saved = ""

def fehlermeldung():
    # Zentriert den Text
    textAlign(CENTER)
    
    # Setzt Textfarbe auf rot
    fill(255, 0, 0)
    text("Achtung, du musst eine Zeit zwischen 00.00 und 23.59 eingeben!", 640, 530)
    
    # Setzt die Farbe zurueck auf Schwarz für normalen Text
    fill(0)  
        
def setup():
    # Fenstergroesse
    size(1280, 742)

def draw():
    global error_status
    # Wenn Status "eingabe", zeichnet Eingabefeld, bei Error_status, zeichne Fehlermeldung noch im Eingabefeld / Status "weltkarte" zeichnet Weltkarte und gibt die Eingabe als Argument weiter
    if status == "eingabe":
        drawinput()
        if error_status:
            fehlermeldung()
    elif status == "weltkarte":
        drawmap(TimeSwitzerland=saved)
        fill(0)

def keyPressed():
    global saved, status, error_status
    if key == '\n':
        if status == "eingabe":
            saved = getTyping()
            setTyping("")
            
            # Ueberprueft, ob der gespeicherte Text ein Punkt enthält, wenn ja, dann werden Zeitteile zerlegt und geschaut, ob sie gültige (Zeit-)Werte haben
            if '.' in saved:
                timeparts = saved.split(".")
                if len(timeparts) == 2 and timeparts[0].isdigit() and timeparts[1].isdigit():
                    if int(timeparts[0]) > 23 or int(timeparts[1]) > 59:
                        error_status = True
                    else:
                        status = "weltkarte"
                        error_status = False
                else:
                    error_status = True
            elif saved:
                error_status = True
        elif status == "weltkarte":
            status = "eingabe"
            error_status = False
    
    # Sonst, wenn Backspace gedrueckt wird, loescht aus der Eingabe den letzten Wert
    elif (key == '\b'):
            old = getTyping()
            new = old[:-1]
            setTyping(new)
    else:
        setTyping(getTyping() + key)
        
