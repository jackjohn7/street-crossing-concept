# this library has everything necessary to instantiate and operate arms in
#  the main .py file
from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as gpio
from time import sleep

# resistor pins
respins = [18,20] 
# factory to avoid jitter
factory = PiGPIOFactory()

# Servo class inherits AngularServo
class Servo(AngularServo):
    def __init__(self, pin: int, zero: int, ninety: int):
        AngularServo.__init__(self, pin=pin, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory)
        self.zero = zero
        self.ninety = ninety
        self.middle = int((ninety + zero) / 2)
    
    # a method that sets the angle of the servo motor to 0 degrees
    def to_zero(self):
        self.angle = self.zero
        
    # a method that sets the angle of the servo motor to 90 degrees
    def to_ninety(self):
        self.angle = self.ninety
        
    # a method that sets the angle of the servo between 0 and 90, 45
    def to_middle(self):
        self.angle = self.middle
        
    # getters for zero, ninety, and middle(unimplemented)
    @property
    def zero(self):
        return self._zero
    
    @zero.setter
    def zero(self, value):
        self._zero = value

    @property
    def ninety(self):
        return self._ninety
    
    @ninety.setter
    def ninety(self, value):
        self._ninety = value
    
    @property
    def middle(self):
        return self._middle
    
    @middle.setter
    def middle(self, value):
        self._middle = value
    
# arm class to abstract code as much as possible
class Arm:
    def __init__(self, servo: Servo):
        self.servo = servo
        if self.servo.angle == self.servo.zero:
            self.is_up = True
        else:
            self.is_up = False
    
    # raises the arms of the crosswalk
    def up(self):
        # sets the servo to the "zero" angle
        self.servo.to_zero()
        self.is_up = True
    
    # lowers the arms of the crosswalk
    def down(self):
        # sets the servo to 90 counter clockwise past the "zero"
        self.servo.to_ninety()
        self.is_up = False
        
    # returns the status of the crosswalk in a string
    def status(self) -> str:
        if self.is_up:
            return "up"
        else:
            return "down"
        
# function that checks whether or not people are currently standing
#  on the pressure pads
def checkpress():
    if gpio.input(respins[0]) == gpio.HIGH:
        return True
    elif gpio.input(respins[1]) == gpio.HIGH:
        return True
    else:
        return False
        
class System:
    def __init__(self, arm1: Arm, arm2: Arm, pad1: int, pad2: int, timer):
        # sets arms, timer, resistors, and some booleans
        self.arms = [arm1, arm2]
        self.timer = timer
        self.pad1 = pad1
        self.pad2 = pad2
        self.crossing = False
        self.just_crossed = False
    
    # begins process
    def run(self):
        # broadcom
        gpio.setmode(gpio.BCM)
        for arm in self.arms:
            arm.up()
        # sets up resistors as inputs in gpio
        gpio.setup(self.pad1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(self.pad2, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        # check for pedestrians crossing and then let arms down
        # set timer for arms that will be reset each time someone attempts
        #  to cross the crosswalk
        #runtime loop
        while True:
            print("made it to while loop")
            # check for pedestrians
            if checkpress():
                #print("pressed")
                # sets the timer to the preset timer length
                timer = self.timer
                # lowers the guard arms
                for arm in self.arms:
                    arm.down()
                # counts down for the timer
                while timer != 0:
                    # checks for more pedestrians
                    if checkpress():
                        # resets the timer if necesssary
                        timer = self.timer
                    timer -= 1
                    sleep(1)
                # says whether or not someone has recently crossed
                self.just_crossed = True
            else:
                #print("not pressed")
                pass
            # checks if nobody is crossing and if a crossing has just occured
            if (not self.crossing) and self.just_crossed:
                # sets just_crossed to False so that arms aren't constantly
                #  being raised
                self.just_crossed = False
                # raises both arms
                for arm in self.arms:
                    arm.up()

    
    # method that does any cleanup
    def stop(self):
        # raises any lowered arms
        for arm in self.arms:
            arm.up()
        # cleans up RPi.GPIO to avoid warnings
        gpio.cleanup()