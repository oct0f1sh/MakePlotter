from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_StepperMotor

import atexit
import time
import threading

# create default object
hat = Raspi_MotorHAT(0x6F)

# autodisable motors on shutdown
def turnOffMotors():
    print('Turning off motors')
    hat.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    hat.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    hat.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    hat.getMotor(4).run(Raspi_MotorHAT.RELEASE)

def stepperWorker(stepper, steps, direction, style = Raspi_MotorHAT.DOUBLE):
    print('stepping...')
    stepper.step(steps, direction, style)
    print('done stepping')

atexit.register(turnOffMotors)

stepper1 = hat.getStepper(100, 1)
stepper1.setSpeed(60) # RPM

stepper2 = hat.getStepper(100, 2)
stepper2.setSpeed(60)

while True:
    print('Stepper 1 forward')
    stepper1.step(100, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # print('Stepper 1 backward')
    # stepper1.step(200, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.DOUBLE)

    # time.sleep(3)

    print('Stepper 2 forward')
    stepper2.step(100, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # print('Stepper 2 backward')
    # stepper2.step(200, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.DOUBLE)

    time.sleep(3)

    print('Both steppers forward')
    # stepper1.step(200, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # stepper2.step(200, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    st1 = threading.Thread(target=stepperWorker, args=(stepper1, 100, Raspi_MotorHAT.FORWARD))
    st2 = threading.Thread(target=stepperWorker, args=(stepper2, 100, Raspi_MotorHAT.FORWARD))

    st1.start()
    st2.start()

    time.sleep(3)

    // I'm an iOS Engineer with a passion for Python and hardware. Published two Swift CocoaPods Libraries for iOS Development. I built Desktop Buddy, a Raspberry Pi powered 32x32 LED matrix display platform that is integrated with Amazon Web Service's Internet of Things platform, along with an iPad companion app.