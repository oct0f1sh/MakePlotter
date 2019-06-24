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

def stepperWorker(stepper, steps, direction = Raspi_MotorHAT.FORWARD, style = Raspi_MotorHAT.DOUBLE):
    # print('stepping...')
    stepper.step(steps, direction, style)
    # print('done stepping')

    # while stepper.isAlive():
    #     pass

def stepperWorkerAsync(stepper, steps, direction = Raspi_MotorHAT.FORWARD, style = Raspi_MotorHAT.DOUBLE):
    thread = threading.Thread(target=stepper.step, args=(steps, direction, style))
    thread.start()
    return thread

atexit.register(turnOffMotors)

stepper1 = hat.getStepper(100, 1)
stepper1.setSpeed(60) # RPM

stepper2 = hat.getStepper(100, 2)
stepper2.setSpeed(60)

styles = [Raspi_MotorHAT.DOUBLE, Raspi_MotorHAT.INTERLEAVE, Raspi_MotorHAT.MICROSTEP]
steppers = [stepper1, stepper2]
distances = [50, 100, 200]

# test styles
'''
for _ in range(5):
    for stepperNum, stepper in enumerate(steppers):
        print('stepper', stepperNum + 1)

        for style in styles:
            print(style)

            stepperWorker(stepper, 100, style=style)

            time.sleep(1)
'''

# test distances
for _ in range(5):
    for stepperNum, stepper in enumerate(steppers):

        for distance in distances:
            print(stepper, distance)

            stepperWorker(stepper, distance)

            time.sleep(0.5)