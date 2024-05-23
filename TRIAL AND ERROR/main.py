# TV class
class TV:
    def __init__(self):
        self.channel1 = 30
        self.channel2 = 3
        self.volume_level1 = 3
        self.volume_level2 = 2
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel1(self):
        return self.channel1
    
    def get_channel2(self):
        return self.channel2

    def set_channel1(self, channel):
        if 1 <= channel <= 120:
            self.channel1 = channel
        else:
            raise ValueError("Channel must be between 1 and 120")
            
    def set_channel2(self, channel):
        if 1 <= channel <= 120:
            self.channel2 = channel
        else:
            raise ValueError("Channel must be between 1 and 120")

    def get_volume1(self):
        return self.volume_level1
    
    def get_volume2(self):
        return self.volume_level2

    def set_volume1(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level1 = volume_level
        else:
            raise ValueError("Volume level must be between 1 and 7")
    
    def set_volume2(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level2 = volume_level
        else:
            raise ValueError("Volume level must be between 1 and 7")

    def channel_up1(self):
        if self.channel1 < 120:
            self.channel1 += 1

    def channel_down1(self):
        if self.channel1 > 1:
            self.channel1 -= 1

    def channel_up2(self):
        if self.channel2 < 120:
            self.channel2 += 1

    def channel_down2(self):
        if self.channel2 > 1:
            self.channel2 -= 1

    def volume_up1(self):
        if self.volume_level1 < 7:
            self.volume_level1 += 1

    def volume_down1(self):
        if self.volume_level1 > 1:
            self.volume_level1 -= 1

    def volume_up2(self):
        if self.volume_level2 < 7:
            self.volume_level2 += 1

    def volume_down2(self):
        if self.volume_level2 > 1:
            self.volume_level2 -= 1


# TestTV test driver program
class TestTV:
    def main(self):
        tv1 = TV()
        tv1.turn_on()
        tv1.set_channel1(30)  # corrected to a valid channel number
        tv1.set_volume1(3)

        tv2 = TV()
        tv2.turn_on()
        tv2.set_channel2(3)  # corrected to a valid channel number
        tv2.set_volume2(2)

        print(f"tv1 channel is {tv1.get_channel1()} and volume level is {tv1.get_volume1()}")
        print(f"tv2 channel is {tv2.get_channel2()} and volume level is {tv2.get_volume2()}")


if __name__ == "__main__":
    test_tv = TestTV()
    test_tv.main()
