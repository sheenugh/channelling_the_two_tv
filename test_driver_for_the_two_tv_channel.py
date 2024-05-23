# TEST DRIVER PROGRAM FOR TESTING THE TV


# ========== PSEUDO CODE =========
# || IMPORTS ||
from class_for_channelling_the_tv import TV
import tkinter as tk 


# || ACTUAL CODES || 
# - Class name 
class TestTV(tk.Tk):
# >> This category is for the tkinter window, such as buttons, TV frame, displayed output, and bg image. <<
    def __init__(self, tv1_channel, tv1_volume, tv2_channel, tv2_volume, *args, **kwargs): # - Constructor.
        # - Using the try and except for the tkinter window for the purpose of to appear or destroy if the channel will be changed in the range of 1>channel<120 and the volume 1>volume<7.
        try:
            # - Instance variables.
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
            
            # - TV Frame.
            tv_frame = tk.Frame(self, bg="#34495e", padx=20, pady=20)
            tv_frame.pack(pady=20)
            
            # - Volume control buttons.
            tk.Button(tv_frame, text="+", command=self.volume_up, bg="#e74c3c", fg="white", font=("Helvetica", 16, "bold")).grid(row=1, column=1, padx=(20,0))
            tk.Button(tv_frame, text="-", command=self.volume_down, bg="#e74c3c", fg="white", font=("Helvetica", 16, "bold")).grid(row=2, column=1, padx=(20,0))
            
            # - Channel control buttons.
            tk.Button(tv_frame, text="↑", command=self.channel_up, bg="#2ecc71", fg="white", font=("Helvetica", 16, "bold")).grid(row=1, column=0)
            tk.Button(tv_frame, text="↓", command=self.channel_down, bg="#2ecc71", fg="white", font=("Helvetica", 16, "bold")).grid(row=2, column=0)
            
        except:
            None
            

    # - Load TV image.
    
    
    # - Display the current channel
    
    
    # - Initializing TV settings.
    def initialize_tv_settings(self):
        self.tv1.set_channel(self.tv1_channel)
        self.tv1.set_volume(self.tv1_volume)
        self.tv2.set_channel(self.tv2_channel)
        self.tv2.set_volume(self.tv2_volume)
        
# >> This category is for the instance methods << 
    # - Instance method channel up for tv1 and tv2.
    def channel_up(self):
        self.tv1.channel_up()
        self.tv2.channel_up()
        
    # - Instance method channel down for tv1 and tv2.
    def channel_down(self):
        self.tv1.channel_down()
        self.tv2.channel_down()
    # - Instance method volume up for tv1 and tv2.
    # - Instance method volume down for tv1 and tv2.

# - Operator
if __name__ == "__main__":
    app = TestTV(tv1_channel=30, tv1_volume=3, tv2_channel=3, tv2_volume=2)
    app.mainloop()
