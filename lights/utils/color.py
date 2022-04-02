class HSBColor:
    """A hue-saturation-brightness color."""

    def __init__(self, hue: float = 0, saturation: float = 1, brightness: float = 1):
        self.hue = hue
        self.saturation = saturation
        self.brightness = brightness
    
    def average(self, o):
        return HSBColor((self.hue + o.hue) / 2, (self.saturation + o.saturation) / 2, (self.brightness + o.brightness) / 2)

    def __str__(self):
        return f"(H: {self.hue:.3f}, S: {self.saturation:.3f}, B: {self.brightness:.3f})"

COLORS = {
    "default": HSBColor(hue=0.149, saturation=0.551),
    "white": HSBColor(saturation=0, brightness=1),
    "warm": HSBColor(hue=0.127, saturation=0.886),
    "cold": HSBColor(hue=0.733, saturation=0.307),
    "black": HSBColor(saturation=0, brightness=0),
    "red": HSBColor(hue=0),
    "orange": HSBColor(hue=0.08),
    "yellow": HSBColor(hue=0.17),
    "green": HSBColor(hue=0.45),
    "blue": HSBColor(hue=0.82),
    "purple": HSBColor(hue=0.88)
}
