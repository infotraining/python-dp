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

# TODO: Write object Adapter


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
    # btn = ToggleButton(TODO)
    # btn.click()
    # btn.click()
    # btn.click()
    # btn.click()

    print('*' * 40)

    # led = LEDLight()
    # btn = ToggleButton(TODO)
    # btn.click()
    # btn.click()
    # btn.click()
    # btn.click()
