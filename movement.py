import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time
import json

class robot_arm:
    def __init__():
        pass

    def inverse_kinematics():
        print("Hello")

    def forward_kinematics():
        print("Hello")

    def motor(num, pos_x, pos_y):
        print("Hello")

    def motor_test(num, dir):
        for x in range(0, speed_param["speed"]["pulses_per_rev"]):
            if(dir == "f"):
                io.output(motor_param[str(num)]["direction_pin"], True)
            elif(dir == "r"):
                io.output(motor_param[str(num)]["direction_pin"], False)
            time.sleep(speed_param["speed"]["delay"])
            io.output(motor_param[str(num)]["step_pin"], True)
            time.sleep(speed_param["speed"]["delay"])
            io.output(motor_param[str(num)]["step_pin"], False)
            time.sleep(speed_param["speed"]["delay"])
    
    def setup(motor_param):
        print("Initializing Motors...")
        for i in motor_param:
            io.setup(motor_param[i]["enable_pin"], io.OUT)
            io.setup(motor_param[i]["direction_pin"], io.OUT)
            io.setup(motor_param[i]["step_pin"], io.OUT)

            io.output(motor_param[i]["enable_pin"], False)
            io.output(motor_param[i]["step_pin"], False)

    def stepper_enable(motor_param):
        print("Enabling Motors...")
        for i in motor_param:
            io.output(motor_param[i]["enable_pin"], False)

    def stepper_disable(motor_param):
        print("Disabling Motors...")
        for i in motor_param:
            io.output(motor_param[i]["enable_pin"], True)

if __name__ == '__main__':
    motor_file = open('motor_parameters.json', "r")
    motor_param = json.load(motor_file)
    robot_arm.setup(motor_param)
    robot_arm.stepper_enable(motor_param)

    speed_file = open('speed_parameters.json', "r")
    speed_param = json.load(speed_file)

    print("Beginning Movement")
    print(motor_param[str(1)]["direction_pin"])
    print(speed_param["speed"]["delay"])
    #Note Motor 2 forward is bakcwards
    #Note Motor 6 only goes in one direction
    #robot_arm.motor_test(2, "r")
    #robot_arm.motor_test(2, "r")
    robot_arm.motor_test(3, "r")
    robot_arm.motor_test(3, "r")
    #robot_arm.motor_test(6, "f")
    #robot_arm.motor_test(6, "r")


    io.cleanup()
