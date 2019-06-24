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

stepper1 = hat.getStepper(200, 1)
stepper1.setSpeed(60) # RPM

stepper2 = hat.getStepper(200, 2)
stepper2.setSpeed(60)

while True:
    print('Stepper 1 forward')
    # stepper1.step(100, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # print('Stepper 1 backward')
    # stepper1.step(200, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.DOUBLE)
    stepperWorker(stepper1, 200)

    # time.sleep(3)

    print('Stepper 2 forward')
    # stepper2.step(100, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # print('Stepper 2 backward')
    # stepper2.step(200, Raspi_MotorHAT.BACKWARD, Raspi_MotorHAT.DOUBLE)
    stepperWorker(stepper2, 200)
    time.sleep(3)

    print('Both steppers forward')
    # stepper1.step(200, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # stepper2.step(200, Raspi_MotorHAT.FORWARD, Raspi_MotorHAT.DOUBLE)
    # st1 = threading.Thread(target=stepperWorker, args=(stepper1, 100, Raspi_MotorHAT.FORWARD))
    # st2 = threading.Thread(target=stepperWorker, args=(stepper2, 100, Raspi_MotorHAT.FORWARD))
    stepperWorkerAsync(stepper1, 200)
    stepperWorkerAsync(stepper2, 200)

    print('restarting')
    time.sleep(3)
