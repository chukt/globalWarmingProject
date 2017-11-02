



class Snowflake:
    radius = 5
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def falling(self):
        self._y += 1
        
    def update(self):
        self.falling()
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius)