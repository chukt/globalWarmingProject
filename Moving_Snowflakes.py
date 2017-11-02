
import tkinter
import random
import time
import ISSM_Snowflake

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
        self.snowflake_list = []
    def start(self):
        '''Starts the application and draws all the needed tkinter objects'''
        self.my_canvas.pack()
        self.my_canvas.tag_bind(TAG, '<B1-Motion>', lambda e: self.drag_circle(e, self.my_canvas))
        frame = tkinter.Frame(self._root_window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
        self.my_canvas.bind("<Button-1>", self.clicked_at)
        self.draw_cloud()
        self.draw_bins()
        self.draw_snowflake()

        heights = self.accumulate(NUM_BINS, [5, 15, 8, 15, 24, 30, 4, 17], None)
        glacier =  self.draw_glacier(heights)
        self.my_canvas.delete(glacier)
        for i in range(10):
            heights = self.accumulate(NUM_BINS, heights, None)
            glacier = self.draw_glacier(heights)
            self.my_canvas.delete(glacier)
            heights = self.accumulate(NUM_BINS, heights, None)
            glacier = self.draw_glacier(heights)
        self._root_window.mainloop()
        
    def draw_snowflake(self):
        '''Draws one snowflake'''
        self.snow_list = []
        for i in range(100):
            x = random.randrange(0, CANVAS_WIDTH)
            y = random.randrange(0, CANVAS_HEIGHT)
            self.snow_list.append([x, y])
        while True:
            for i in range(len(self.snow_list)):   # ADDS SNOWLAKES ON THE SIDE
                self.flake = self.my_canvas.create_oval(self.snow_list[i][0], self.snow_list[i][1], self.snow_list[i][0]+7, self.snow_list[i][1]+7, outline = FLAKE_COLOR, fill = FLAKE_COLOR, tag=TAG)
                self.snow_list[i][1] += 1
#                 self.snow_list[i][0] += (random.randrange(-10,10))
            self._root_window.update()
            self.snow_list.sort()
            print(self.snow_list)
            time.sleep(.1)
            for i in range(len(self.snow_list)):
                x = self.my_canvas.find_closest(self.snow_list[i][0],self.snow_list[i][1]) 
                self.my_canvas.delete(x)
                if self.snow_list[i][1] > CANVAS_HEIGHT:
                    self.snow_list[i][1] = random.randrange(-50,-10)
                    self.snow_list[i][0] = random.randrange(0, CANVAS_WIDTH)
        
    def drag_circle(self, event, canvas):
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        print('coord', canvas.coords(TAG, x-7, y-7, x+7, y+7))
        
        
    def draw_cloud(self):
        '''Draws the cloud (made for different sized windows)'''
        for i in range(NUM_CLOUDS):
            self.my_canvas.create_arc((i/NUM_CLOUDS)*CANVAS_WIDTH-100, -100, (i/NUM_CLOUDS)*CANVAS_WIDTH+200, 50, start = 189, extent = 190, style = 'chord', fill = CLOUD_COLOR, outline = CLOUD_COLOR)
            
    
    def draw_bins(self):
        '''Draws bins according to the number of bins needed and percent of canvas height'''
        for i in range(NUM_BINS):
            self.my_canvas.create_line((i/NUM_BINS)*CANVAS_WIDTH, BIN_HEIGHT*CANVAS_HEIGHT, (i/NUM_BINS)*CANVAS_WIDTH, CANVAS_HEIGHT)

    def draw_glacier(self, heights:list):
        '''Draws the glacier using the polygon'''
        coord = []
        for i in range(len(heights)-1):
            coord.append((i/NUM_BINS)*CANVAS_WIDTH)
            coord.append(CANVAS_HEIGHT - heights[i])
        coord.append(CANVAS_WIDTH)
        coord.append(CANVAS_HEIGHT)
        coord.append(0)
        coord.append(CANVAS_HEIGHT)
        self.glacier = self.my_canvas.create_polygon(coord, outline = '#b0c4de', fill = 'white')
        return self.glacier
        
    def delete_glacier (self, heights: list):
        coord = []
        for i in range(len(heights)-1):
            coord.append((i/NUM_BINS)*CANVAS_WIDTH)
            coord.append(CANVAS_HEIGHT - heights[i])
        coord.append(CANVAS_WIDTH)
        coord.append(CANVAS_HEIGHT)
        coord.append(0)
        coord.append(CANVAS_HEIGHT)
        self.my_canvas.delete(coord)


    def accumulate(self, bins:int, heights: [int], flakes_in_bin:[int]):
        '''Randomly changes the heights of the glacier'''
        self.points = []
        for height in heights:
            self.points.append(height + random.randint(0,10))
        return self.points
    
    def clicked_at(self, event):
        print(event.x, event.y)
        for i in range(len(self.snow_list)):
            if self.snow_list[i][0]<=event.x<=self.snow_list[i][0]+7 and self.snow_list[i][1]<=event.y<=self.snow_list[i][1]:
                print("here!")

if __name__ == '__main__':
    GlacierApplication().start()

    
# http://www.tutorialspoint.com/python/tk_canvas.htm
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_arc.html
# http://zetcode.com/gui/tkinter/drawing/
# http://www.python-course.eu/tkinter_canvas.php
# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# http://effbot.org/tkinterbook/canvas.htm
# http://www.cyberciti.biz/faq/python-sleep-command-syntax-example/
# https://www.daniweb.com/software-development/python/threads/468733/time-sleep-in-for-loop-using-tkinter
# https://www.daniweb.com/software-development/python/threads/468733/time-sleep-in-for-loop-using-tkinter#post2042946
# http://programarcadegames.com/index.php?chapter=introduction_to_animation
# http://stackoverflow.com/questions/18720595/python-tkinter-smooth-move
# http://effbot.org/tkinterbook/widget.htm
# http://programarcadegames.com/index.php?chapter=introduction_to_animation
# http://www.greenteapress.com/thinkpython/html/thinkpython020.html

'''
after function? http://effbot.org/tkinterbook/widget.htm
http://programarcadegames.com/index.php?chapter=introduction_to_animation

Draggable class that I never used?
http://www.greenteapress.com/thinkpython/html/thinkpython020.html
'''