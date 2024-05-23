# TV class
class TV:
    def __init__(self, channel = 1, volume_level = 1, on = False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        try: 
            if 1 <= channel <= 120:
                self.channel = channel
            else:
                pass
        except ValueError:
            print("Tanga")

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level
        else:
            raise ValueError("Volume level must be between 1 and 7")

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


# TestTV test driver program
class TestTV:
    def main(self):
        tv1 = TV()
        tv1.turn_on()
        tv1.set_channel(30000000)
        tv1.set_volume(3)

        tv2 = TV()
        tv2.turn_on()
        tv2.set_channel(3)
        tv2.set_volume(2)

        print(f"tv1 channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
        print(f"tv2 channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")


if __name__ == "__main__":
    test_tv = TestTV()
    test_tv.main()