class Image:
    def __init__(self, filepath):
        self.filepath = filepath
        self._pixels = None
        self._width = None

    @property
    def pixels(self):
        if self._pixels is None:
            print("Loading 50mb....")
            self._pixels = load_image(self.filepath)
        return self._pixels
    @property
    def width(self):
        if self._width is None:
            self._width = read_header(self.filepath).width
        return self._width
    
img = Image("huge png")
print(img.filepath)
print(img.pixels)
print(img.width)