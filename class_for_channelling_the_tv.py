# CLASS CATEGORY FOR TESTING THE TV

# ========== PSEUDO CODE =========
# || IMPORTS ||


# || ACTUAL CODES || 


# - Class name.
class TV:
    # - Constructor.
    def __init__(self, channel = 1, volume_level = 1, on = False):
        # - Instance Variables.
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    # - Instance Methods.
    # - Instance Method: Turning on the TV.
    def turn_on(self):
        self.on = True # - Making the "turning on" of the TV as "True" or equivalent to "True."
    
    # - Instance Method: Turning off the TV.
    def turn_off(self):
        self.on = False # - Making the "turning off" of the TV as "False" or equivalent to "False."

    # - Instance Method: Get the channel.
    def get_channel(self):
        return self.channel # - Setting in this kind of approach to access the set channel value in the instance variable. Simply , it will return to the default channel of the TV.
    
    # - Instance Method: Set the channel.
    def set_channel(self, channel): # - Putting the 'channel' para maaccess at madetermine ng if else ang sinet na int doon sa object parameter.
        if 1<= channel <= 120:
            self.channel = channel # - Setting this kind of approach will automatically produce an output that is equal to the number that has been set to the tv's channel in the test driver program.
        else: 
            raise ValueError("The channel must be between 1 to 120. Please input a number between this number.")
        
    # - Instance Method: Get the volume.
    # - Instance Method: Set the volume.
    # - Instance Method: Channel up.
    # - Instance Method: Channel down.
    # - Instance Method: Volume up.
    # - Instance Method: Volume down.