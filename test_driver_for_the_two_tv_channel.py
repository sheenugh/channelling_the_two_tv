# TEST DRIVER PROGRAM FOR TESTING THE TV

# ========== PSEUDO CODE =========
# || IMPORTS ||
from class_for_channelling_the_tv import TV


# || PACKAGES/LIBRARY ||


# || ACTUAL CODES || 
# - Class name 
class TestTV:
    # - TV 1 and TV 2 objects together with the def function
    def channelling_tv1_and_tv2(self):
        tv1 = TV()
        tv1.turn_on()
        tv1.set_channel(30)
        tv1.set_volume(3)

        tv2 = TV()
        tv2.turn_on()
        tv2.set_channel(3)
        tv2.set_volume(2)
        
        print(f"tv1 channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
        print(f"tv2 channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")
        
        
if __name__ == "__main__":
    test_tv = TestTV()
    test_tv.channelling_tv1_and_tv2()