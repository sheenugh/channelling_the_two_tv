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
        
        


if __name__ == "__test_driver_for_the_two_tv_channel__":
    test_tv = TestTV()
    test_tv.test_driver_for_the_two_tv_channel()