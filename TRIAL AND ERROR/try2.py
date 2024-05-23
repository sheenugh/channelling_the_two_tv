class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self) -> int:
        return self.channel

    def set_channel(self, channel: int):
        if 1 <= channel <= 120:
            self.channel = channel

    def get_volume(self) -> int:
        return self.volume_level

    def set_volume(self, volume_level: int):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 1:
            self.volume_level -= 1
