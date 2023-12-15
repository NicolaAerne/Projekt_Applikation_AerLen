# Variable die den geschriebenen Text speichert
typing = ""
# Variable die den geschriebenen text speichert, nach '\n'
saved = ""

def setTyping(newText):
    global typing
    typing = newText
    
def getTyping():
    return typing

def drawinput():
    # Hintergrundfarbe
    background(171, 225, 243)
    
    # Titel Eingabefenster
    textSize(70)
    textAlign(CENTER)
    text("WELTUHREN", 640, 150)
    
    # Aufgabenstellung Eingabefenster
    textSize(20)
    textAlign(CENTER)
    text("In diesem Programm wird dir die Uhrzeit an folgenden Orten der Welt angezeigt:" '\n' '\n' "New York, Brasilia, London, Moskau, Neu-Delhi, Tokio, Sidney." '\n' '\n' "Gib eine beliebige Zeit in der Schweiz im Format XX.XX an. Mache dir Gedanken, welche Uhrzeit es an den entsprechenden Orten ist und kontrolliere." , 640, 250)
    
    # Rechteck fuer Eingabefeld
    fill(255)
    rect(500, 440, 290, 50, 10)
    
    # Eingabebefehl
    fill(0)
    textAlign(LEFT)
    text("Eingabe: " + typing, 580, 471)
    textAlign(CENTER)
    text ("Mit der ENTER-Taste kannst du fortfahren.", 640, 600)
    
