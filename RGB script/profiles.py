import wheels
import time

class Profile(object):
    def __init__(self,name="basic"):
        self.name = name
        self.r = 0
        self.g = 0
        self.b = 0

    def setRGB(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def display(self, pixels):
        pixels.fill((self.r,self.g,self.b))
        pixels.show()
        pass


    def __str__(self):
        return f"This is a {self.name} profile\nRGB current values : ({self.r},{self.g},{self.b}) "

class ColorFadeProfile(Profile):
    def __init__(self):
        super().__init__("ColorFade")
        super().setRGB(0,0,255)

    def display(self, pixels):
        self.r, self.g, self.b = wheels.colorwheel(self.r,self.g,self.b)
        super().display(pixels)

class LoadingProfile(Profile):
    def __init__(self,cursor=0,refresh=0.5):
        self.cursor = cursor
        self.refresh = refresh
        super().__init__("Loading")
        super().setRGB(255,0,0)

    def display(self, pixels):
        pixels[self.cursor] = (self.r,self.g,self.b)
        pixels.show()
        if self.cursor<150:
            self.cursor+=1
        if self.cursor == 149:
            self.cursor=0
            pixels.fill((0,0,0))
        time.sleep(self.refresh)
    
    def resetCursor(self):
        self.cursor=0


    
