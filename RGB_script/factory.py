from gameprofiles import *

def Factory(role):
    classes = {
        "BASIC": Profile,
        "INDEX": IndexProfile,
        "COLORFADE": ColorFadeProfile,
        "BREATH": BreathingProfile,
        "FLASH" : FlashProfile,
        "COLORBREATH": ColorBreathingProfile,
        "LOADING": LoadingProfile,
        "SNAKE": SnakeProfile,
        "COMET": CometProfile,
        "COLORWAVE": ColorWaveProfile,
        "STARS": StarsProfile,
        "WEBSITE": WebProfile,
        "MINECRAFT": MinecraftProfile,
        "TREX": TrexProfile
        
    }
    return classes[role]
