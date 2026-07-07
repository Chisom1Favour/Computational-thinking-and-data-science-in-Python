class Figure:
    def __init__(self):
        self._width_inches = 6
        self._dpi = 100
        self._renderer = None

@property
def width(self):
    return self._width_inches

@width.setter
def width(self, value):
    self._width_inches = value
    self._invalidate_renderer()   # triggers redraw
    self.canvas.resize(value * self._dpi)