from collections import namedtuple
from dataclasses import dataclass, field
import typing

RGB = namedtuple('RGB', ['R', 'G', 'B'])


@dataclass
class LEDLight:
    color: RGB = field(default=RGB(0, 0, 0))

    def set_rgb(self, color: RGB = RGB(0, 0, 0)):
        self.color = color
        print(f'Color({color.R}, {color.G}, {color.B}) is set for a LED light')


class LightSwitch(typing.Protocol):
    def on(self): ...

    def off(self): ...


# TODO: Write class Adapter
class LEDSwitchClassAdapter(LEDLight):
    def on(self):
        super().set_rgb(RGB(255, 255, 255))

    def off(self):
        super().set_rgb(RGB(0, 0, 0))

# TODO: Write object Adapter
class LEDSwitchObjectAdapter:
    def __init__(self, led: LEDLight):
        self.__led = led

    def on(self):
        self.__led.set_rgb(RGB(255, 255, 255))

    def off(self):
        self.__led.set_rgb(RGB(0, 0, 0))


class ToggleButton:
    def __init__(self, switchable_light: LightSwitch):
        self._is_on = False
        self._switchable_light = switchable_light

    def click(self):
        if self._is_on:
            self._is_on = False
            self._switchable_light.off()
        else:
            self._is_on = True
            self._switchable_light.on()


if __name__ == "__main__":
    btn = ToggleButton(LEDSwitchClassAdapter())
    btn.click()
    btn.click()
    btn.click()
    btn.click()


    led = LEDLight()
    btn = ToggleButton(LEDSwitchObjectAdapter(led))
    btn.click()
    btn.click()
    btn.click()
    btn.click()