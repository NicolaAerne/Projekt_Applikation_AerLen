
# Variable to store text currently being typed
typing = ""
# Variable to store saved text when return is hit
saved = ""

def setTyping(newText):
    global typing
    typing = newText
    
def getTyping():
    return typing


def drawinput():
    background(255)
    indent = 50
  
    # Set the font and fill for text
    #textFont(f)
    fill(1)
    
    # Display everything
    text("Gib die Uhrzeit im Format xx.xx an. Mit der Enter-Taste kannst du fortfahren. ", indent, 40)
    text("Eingabe: " + typing, indent, 190)        
    text("saved: " + saved, indent, 230)
