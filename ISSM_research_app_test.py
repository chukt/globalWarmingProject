
import tkinter
import random
import time
from ISSM_research_app_test2 import Snowflake

CLOUD_COLOR = '#f0f8ff'
BACKGROUND = '#b0c4de'
FLAKE_COLOR = '#f0ffff'
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
NUM_BINS = 10
NUM_CLOUDS = 7
BIN_HEIGHT = 0.75
TO_FALL = 100
TAG = 'snowflake'



class GlacierApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self.my_canvas = tkinter.Canvas(master = self._root_window, background = BACKGROUND,
                           width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
    def start(self):
        Snowflake(500,100).display(self.my_canvas)
        self.my_canvas.pack()

if __name__ == '__main__':
    GlacierApplication().start()

    
##http://www.tutorialspoint.com/python/tk_canvas.htm
##http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_arc.html
#http://zetcode.com/gui/tkinter/drawing/
#http://www.python-course.eu/tkinter_canvas.php
#http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#http://effbot.org/tkinterbook/canvas.htm
#http://www.cyberciti.biz/faq/python-sleep-command-syntax-example/
#https://www.daniweb.com/software-development/python/threads/468733/time-sleep-in-for-loop-using-tkinter
#https://www.daniweb.com/software-development/python/threads/468733/time-sleep-in-for-loop-using-tkinter#post2042946
#http://programarcadegames.com/index.php?chapter=introduction_to_animation
#http://stackoverflow.com/questions/18720595/python-tkinter-smooth-move
'''
after function? http://effbot.org/tkinterbook/widget.htm
http://programarcadegames.com/index.php?chapter=introduction_to_animation

Draggable class that I never used?
http://www.greenteapress.com/thinkpython/html/thinkpython020.html
'''