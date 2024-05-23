# TEST DRIVER PROGRAM FOR TESTING THE TV

# ========== PSEUDO CODE =========
# || IMPORTS ||
from class_for_channelling_the_tv import TV
import tkinter as tk 



# || PACKAGES/LIBRARY ||


# || ACTUAL CODES || 
# - Class name 
class TestTV(tk.Tk):
    # - Constructor.
    def __init__(self, tv1_channel, tv1_volume, tv2_channel, tv2_volume, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
            self.tv1_channel = tv1_channel
            self.tv1_volume = tv1_volume
            self.tv2_channel = tv2_channel
            self.tv2_volume = tv2_volume
            self.tv1 = TestTV()
            self.tv2 = TestTV()
            self.initialize_tv_settings()
            self.title("TV Controller")
            self.configure(bg="#2c3e50")
        except:
            None
        
    # - Using the try and except for the tkinter window for the purpose of to appear or destroy if the channel will be changed in the range of 1>channel<120 and the volume 1>volume<7.

    # - Instance variables.
    # - TV Frame.
    # - Load TV image.
    # - Channel control buttons
    # - Volume control buttons
    # - Display the current channel
    # - Operator
    
if __name__ == "__main__":
    app = TestTV(tv1_channel=30, tv1_volume=3, tv2_channel=3, tv2_volume=2)
    app.mainloop()
