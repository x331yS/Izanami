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

    def colorController(self):
        pass

    def brightnessController(self,pixels):
        pass
    
    def display(self, pixels):
        self.colorController()
        self.brightnessController(pixels)
        pixels.fill((self.r,self.g,self.b))
        pixels.show()

    def __str__(self):
        return f"This is a {self.name} profile\nRGB current values : ({self.r},{self.g},{self.b}) "

class ColorFadeProfile(Profile):
    def __init__(self):
        super().__init__("ColorFade")
        super().setRGB(0,0,255)
    def colorController(self):
        self.r, self.g, self.b = wheels.colorwheel(self.r,self.g,self.b)

class BreathingProfile(Profile):
    def __init__(self, refresh=0.02):
        super().__init__("Breathing")
        super().setRGB(255,255,255)
        self.refresh = refresh
        self.x = 0.01

    def display(self, pixels):
        super().display(pixels)
        time.sleep(self.refresh)
        
    def brightnessController(self,pixels):
        if pixels.brightness >= 0.2:
            self.x = -self.x
        elif pixels.brightness <= 0:
            self.x = -self.x
            pixels.brightness = 0 
        pixels.brightness += self.x
        print(pixels.brightness)

class ColorBreathingProfile(BreathingProfile):
    def __init__(self):
        super().__init__()
        super().setRGB(0,0,255)
        self.name = "ColorBreathing"
    def colorController(self):
        self.r, self.g, self.b = wheels.colorwheel(self.r,self.g,self.b,3)


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

class SnakeProfile(Profile):
    def __init__(self, refresh=0.05):
        super().__init__("Snake")
        super().setRGB(255,255,255)
        self.refresh = refresh
        self.index=[0]

    def addToIndex(self):
        self.index.extend((0, 1, 2))
        print("index:"+str(self.index))

    def cleanIndex(self):
        indextopop = None
        for y in range(len(self.index)):
            if self.index[y]>150:
                indextopop=y
        if indextopop != None:
            self.index.pop(indextopop)
    def display(self, pixels):

        for i in range(150):
            for y in range(len(self.index)):
                if i == self.index[y]:
                    pixels[self.index[y]] = (self.r,self.g,self.b)
    
            if i not in self.index:
                pixels[i] = (0,0,0)

        
        pixels.show()

        for y in range(len(self.index)):
            self.index[y] += 1
        self.cleanIndex()
        time.sleep(self.refresh)



    
