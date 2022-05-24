from profiles import *
import wheels


class GameProfile():
    def __init__(self,pixels,name="GAME"):
        self.pixels = pixels
        self.name = name
        self.curprofile = Profile(pixels,name)
        
    def mainChanges(self):
        pass

    def display(self):
        self.mainChanges()
        self.curprofile.display()


class MinecraftProfile(GameProfile):
    def __init__(self,pixels,name="MINECRAFT"):
        super().__init__(pixels,name)
        self.scale = 20
    def setScale(self,scale):
        self.scale = scale
    def mainChanges(self):
        if self.scale<=0:
            curprofile= BreathingProfile(self.pixels,self.name)
            curprofile.rgb = wheels.COLORS["RED"]
            return
        x = 255*self.scale/20
        for i in range(x):
            curprofile.rgb = wheels.colorGradient(wheels.COLORS["RED"],wheels.COLORS["GREEN"],1)

