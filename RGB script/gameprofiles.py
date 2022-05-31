from profiles import *
import wheels

COLORSLIST = ["WHITE","ORANGE","LIGHT_ORANGE","YELLOW","VERY_LIGHT_GREEN","LIGHT_GREEN","GREEN","BLUE","CYAN","PINK"]

class GameProfile():
    def __init__(self,pixels,name="GAME"):
        self.pixels = pixels
        self.name = name
        self.curprofile = Profile(pixels)
        print(self.curprofile)
        self.deathcolor = wheels.COLORS["RED"]
        
    def mainChanges(self):
        pass

    def display(self):
        self.mainChanges()
        self.curprofile.display()

    def __str__(self):
        print(f"This is a {self.name} Profile")


class MinecraftProfile(GameProfile):
    def __init__(self,pixels):
        super().__init__(pixels,"MINECRAFT")
        self.scale = 20
    def setScale(self,scale):
        self.scale = scale
    def mainChanges(self):
        if self.scale<=-100 and not self.curprofile.name == "BREATH":
            self.curprofile = BreathingProfile(self.pixels)
            self.curprofile.rgb = self.deathcolor
            return
        elif self.scale<=0:
            return
        if self.scale>=50 and not self.curprofile.name =="BASIC":
            self.curprofile = Profile(self.pixels)
            self.curprofile.rgb = wheels.COLORS["GREEN"]
        elif self.scale>=50:
            self.scale = 20
        x = round(255*self.scale/20)
        color = self.deathcolor
        for i in range(x):
            color = wheels.colorGradient(color,wheels.COLORS["GREEN"],1)
        self.curprofile.rgb = color


class TrexProfile(GameProfile):
    def __init__(self,pixels):
        super().__init__(pixels,"TREX")
        self.scale = 0
        self.oldscale = 0
        self.curprofile = SnakeProfile(pixels)
    def setScale(self,scale):
        self.scale = scale
        if self.scale != self.oldscale:
            self.curprofile.addToIndex([0,1,2,3])
            self.oldscale = self.scale
    def mainChanges(self):
        if self.scale < 0 and not self.curprofile.name == "BREATH":
            self.curprofile = BreathingProfile(self.pixels)
            self.curprofile.rgb = self.deathcolor
            return
        if self.scale>0 and not self.curprofile.name =="SNAKE":
            self.curprofile = SnakeProfile(self.pixels)
            self.curprofile.rgb = wheels.COLORS["WHITE"]
        self.scale = self.scale%50
        x = round(10*self.scale/50)
        self.curprofile.rgb = wheels.COLORS[COLORSLIST[x]]
        