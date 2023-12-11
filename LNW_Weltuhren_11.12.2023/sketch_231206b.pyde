
from Einfabefeld import *
from Weltkarte import *

status = "eingabe"
saved = ""

def setup():
    size(1280, 742)

def draw():
    if status == "eingabe":
        drawinput()
        
    if status == "weltkarte":
        drawmap(TimeSwitzerland=saved)
        fill(0)
        #text("show zeit: " + saved, indent, 20)
    
    
def keyPressed():
    global saved
    global status
    # If the return key is pressed, save the String and clear it
    if (key == '\n' ):
        if status == "eingabe":
            saved = getTyping()
            # A String can be cleared by setting it equal to ""
            setTyping("")
            status = "weltkarte"
            return
            
        if status == "weltkarte":
            status = "eingabe"
            setTyping("")
            return
    else:
        # Otherwise, concatenate the String
        # Each character typed by the user is added to the end of the String variable.
        
        if (key == ""):
            old = getTyping()
            new = old[:-1]
            setTyping(new)
        else:
            setTyping(getTyping() + key)
            
        
        
