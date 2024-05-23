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
# - Instance Method: Set the channel.
# - Instance Method: Get the volume.
# - Instance Method: Set the volume.
# - Instance Method: Channel up.
# - Instance Method: Channel down.
# - Instance Method: Volume up.
# - Instance Method: Volume down.