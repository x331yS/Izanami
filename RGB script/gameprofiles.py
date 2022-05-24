from profiles import *
import wheels


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


class MinecraftProfile(GameProfile):
    def __init__(self,pixels):
        super().__init__(pixels,"MINECRAFT")
        self.scale = 20
    def setScale(self,scale):
        self.scale = scale
    def mainChanges(self):
        if self.scale<=0 and not self.curprofile.name == "BREATH":
            self.curprofile = BreathingProfile(self.pixels)
            self.curprofile.rgb = self.deathcolor
            return
        elif self.scale<=0:
            return
        if self.scale>=50 and not self.curprofile.name =="BASIC":
            self.curprofile = Profile(self.pixels)
            self.curprofile.rgb = color,wheels.COLORS["GREEN"]
        x = round(255*self.scale/20)
        color = self.deathcolor
        for i in range(x):
            color = wheels.colorGradient(color,wheels.COLORS["GREEN"],1)
        self.curprofile.rgb = color

