from typing import List
from .color import Color

class Light:
    @property
    def name(self) -> str:
        """Fetches the lamp's name."""
        return None

    @property
    def brightness(self) -> float:
        """Fetches the brightness of the lamp (on the range [0, 1])."""
        return None

    @brightness.setter
    def brightness(self, value: float):
        """Sets the brightness of the lamp (on the range [0, 1])."""
        raise NotImplementedError("Setting the brightness is not supported")

    @property
    def on(self) -> bool:
        """Whether the lamp is activated."""
        return None

    @on.setter
    def on(self, value: bool):
        """Activates or deactivates the lamp."""
        raise NotImplementedError("Activating or deactivating the lamp is not supported")

    def toggle(self):
        self.on = not self.on

    @property
    def color(self):
        """Fetches the RGB color of the lamp."""
        return None

    @color.setter
    def color(self, color: Color) -> Color:
        """Sets the RGB color of the lamp."""
        raise NotImplementedError("Setting the color is not supported")

class LightSystem:
    def connect(self):
        """If required by the implementation, connects to the light system."""
        pass

    @property
    def lights(self) -> List[Light]:
        """Lists the available lights."""
        raise NotImplementedError("Cannot fetch lights")
