class Blender:
    """Blender class for modeling a blender oject"""
    def __init__(self, color, brand, volume):
        """ a little something"""
        self.color = color
        self.brand = brand
        self.volume = volume

    def blend(self, speed, time):
        """ a method to model blending"""
        print( "The", self.color, " blender is")
        print("blending at", speed, " for", time, "minutes")


# now test the blender...
my_blender = Blender("green", "Ninja", 48)
my_blender.blend(3, 2)


