import qwiic_scmd
import time

class RijuBot():
    
    R_MTR = 0
    L_MTR = 1
    FWD = 0
    BWD = 1
    
    def __init__(self, *args, **kwargs):        
        self.myMotor = qwiic_scmd.QwiicScmd()
        
        if self.myMotor.connected == False:
            print("Motor Driver not connected. Check connections.", \
                file=sys.stderr)
            return
        
        self.myMotor.begin()
        print("Motor initialized.")
        time.sleep(.250)

        # Zero Motor Speeds
        self.myMotor.set_drive(self.R_MTR,0,0)
        self.myMotor.set_drive(self.L_MTR,0,0)

        self.myMotor.enable()
        print("Motor enabled")
        time.sleep(.250)

        
    def set_motors(self, left_speed, right_speed):
        self.myMotor.set_drive(self.R_MTR,self.FWD,right_speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,left_speed)
        
    def forward(self, speed=80, duration=None):
        self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,speed)

    def backward(self, speed=80):
        self.myMotor.set_drive(self.R_MTR,self.FWD,-speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,-speed)

    def left(self, speed=80):
        self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,-speed)

    def right(self, speed=80):
        self.myMotor.set_drive(self.R_MTR,self.FWD,-speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,speed)

    def stop(self):
        self.myMotor.set_drive(self.R_MTR,0,0)
        self.myMotor.set_drive(self.L_MTR,0,0)
