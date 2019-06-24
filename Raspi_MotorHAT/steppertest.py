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
    print('stepping...')
    stepper.step(steps, direction, style)
    print('done stepping')

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

while True:
    for stepperNum, stepper in enumerate(steppers):
        print('stepper', stepperNum + 1)

        for style in styles:
            print(style)

            stepperWorker(stepper, 100, style=style)

# while True:
#     print('Stepper 1 forward DOUBLE')
#     stepperWorker(stepper1, 100)

#     time.sleep(1)

#     print('Stepper 1 forward MICROSTEP')
#     stepperWorker(stepper1, 100, style = Raspi_MotorHAT.MICROSTEP)

#     time.sleep(1)

#     print('Stepper 1 forward INTERLEAVE')
#     stepperWorker(stepper1, 100, style=Raspi_MotorHAT.INTERLEAVE)
    
#     time.sleep(1)

#     print('Stepper 2 forward')
#     stepperWorker(stepper2, 100)

#     print('Both steppers forward DOUBLE')
#     st1 = stepperWorkerAsync(stepper1, 100)
#     st2 = stepperWorkerAsync(stepper2, 100)

#     while st1.isAlive() or st2.isAlive():
#         pass

#     print('restarting')
#     time.sleep(3)
