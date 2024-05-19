# CLASS CATEGORY FOR TESTING THE TV

# ========== PSEUDO CODE =========
# || IMPORTS ||
# || ACTUAL CODES || 
# - Class name
class TV:
    # - Constructor
    def __init__(self, channel = 1, volume_level = 1, on = False):
    # - Instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    def turn_on(self):
        self.on = True # - Making the "turning on" of the TV as "True" or equivalent to "True."

    def turn_off(self):
        self.on = False # - Making the "turning off" of the TV as "False" or equivalent to "False."
    
    def get_channel(self):
        return self.channel # - Setting in this kind of approach to access the set channel value in the instance variable. Simply , it will return to the default channel of the TV.
    
    def set_channel(self, channel): # - Putting the 'channel' para maaccess at madetermine ng if else ang inputted int doon sa object parameter.
        if 1<= channel <= 120:
            self.channel = channel # - Setting this kind of approach will automatically produce an output that is equal to the number that has been set to the tv's channel.
        else: 
            raise ValueError("The channel must be between 1 to 120. Please input a number between this number.")
    
    def get_volume(self):
        return self.volume_level # - Gets or return the volume of the TV, where volume = 1.
    
    def set_volume(self, volume_level): 
        if 1<= volume_level <=7:
            self.volume_level = volume_level
    
    def channel_up(): None
    
    def channel_down(): None
    
    def volume_up(): None
    
    def volume_down(): None
    
    
    

# - Instance methods