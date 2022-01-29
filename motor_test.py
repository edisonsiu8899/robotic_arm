import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time

# This blocks of code defines the three GPIO
# pins used for the stepper motor
#motor_enable_pin = 17
#motor_direction_pin = 27
#motor_step_pin = 22
motor_enable_pin_1 = 2
motor_direction_pin_1 = 3
motor_step_pin_1 = 4

motor_enable_pin_2 = 14
motor_direction_pin_2 = 15
motor_step_pin_2 = 18

motor_enable_pin_3 = 17
motor_direction_pin_3 = 27
motor_step_pin_3 = 22

motor_enable_pin_4 = 23
motor_direction_pin_4 = 24
motor_step_pin_4 = 25

motor_enable_pin_5 = 10
motor_direction_pin_5 = 9
motor_step_pin_5 = 11

motor_enable_pin_6 = 8
motor_direction_pin_6 = 7
motor_step_pin_6 = 1

delay = 3E-004              # By playing with this delay you can influence the rotational speed.
pulses_per_rev = 400        # This can be configured on the driver using the DIP-switches
io.setup(motor_enable_pin_1, io.OUT)
io.setup(motor_direction_pin_1, io.OUT)
io.setup(motor_step_pin_1, io.OUT)

io.setup(motor_enable_pin_2, io.OUT)
io.setup(motor_direction_pin_2, io.OUT)
io.setup(motor_step_pin_2, io.OUT)

io.setup(motor_enable_pin_3, io.OUT)
io.setup(motor_direction_pin_3, io.OUT)
io.setup(motor_step_pin_3, io.OUT)

io.setup(motor_enable_pin_4, io.OUT)
io.setup(motor_direction_pin_4, io.OUT)
io.setup(motor_step_pin_4, io.OUT)

io.setup(motor_enable_pin_5, io.OUT)
io.setup(motor_direction_pin_5, io.OUT)
io.setup(motor_step_pin_5, io.OUT)

io.setup(motor_enable_pin_6, io.OUT)
io.setup(motor_direction_pin_6, io.OUT)
io.setup(motor_step_pin_6, io.OUT)


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

	
# This section of code defines the methods used to determine
# whether the stepper motor needs to spin forward or backwards. 
# Different directions are acheived by setting the
# direction GPIO pin to true or to false. 
# My driver required:
#   DIR must be ahead of PUL effective edge by 5 micro-s to ensure correct direction;
#   Pulse width not less than 2.5 micro-s;
#   Pulse low-level width not less than 2.5 micro-s.

def stepper_enable():
    io.output(motor_enable_pin_1, False)
    io.output(motor_enable_pin_2, False)
    io.output(motor_enable_pin_3, False)
    io.output(motor_enable_pin_4, False)
    io.output(motor_enable_pin_5, False)
    io.output(motor_enable_pin_6, False)

def stepper_disable():
    io.output(motor_enable_pin_1, True)
    io.output(motor_enable_pin_2, True)
    io.output(motor_enable_pin_3, True)
    io.output(motor_enable_pin_4, True)
    io.output(motor_enable_pin_5, True)
    io.output(motor_enable_pin_6, True)

def step_once():
    io.output(motor_step_pin_1, True)
    io.output(motor_step_pin_2, True)
    io.output(motor_step_pin_3, True)
    io.output(motor_step_pin_4, True)
    io.output(motor_step_pin_5, True)
    io.output(motor_step_pin_6, True)
    time.sleep(delay)
    io.output(motor_step_pin_1, False)
    io.output(motor_step_pin_2, False)
    io.output(motor_step_pin_3, False)
    io.output(motor_step_pin_4, False)
    io.output(motor_step_pin_5, False)
    io.output(motor_step_pin_6, False)
    time.sleep(delay)

def step_forward():
    #io.output(motor_direction_pin_1, True)
    #io.output(motor_direction_pin_2, True)
    io.output(motor_direction_pin_3, True)
    io.output(motor_direction_pin_4, True)
    io.output(motor_direction_pin_5, True)
    io.output(motor_direction_pin_6, True)
    time.sleep(delay)
    step_once()
    

def step_reverse():
    #io.output(motor_direction_pin_1, False)
    #io.output(motor_direction_pin_2, False)
    io.output(motor_direction_pin_3, False)
    io.output(motor_direction_pin_4, False)
    io.output(motor_direction_pin_5, False)
    io.output(motor_direction_pin_6, False)
    time.sleep(delay)
    step_once()

# Setting the stepper pins to false so the motors will not move
# until the user presses the first key
io.output(motor_enable_pin_1, False)
io.output(motor_step_pin_1, False)
io.output(motor_enable_pin_2, False)
io.output(motor_step_pin_2, False)
io.output(motor_enable_pin_3, False)
io.output(motor_step_pin_3, False)
io.output(motor_enable_pin_4, False)
io.output(motor_step_pin_4, False)
io.output(motor_enable_pin_5, False)
io.output(motor_step_pin_5, False)
io.output(motor_enable_pin_6, False)
io.output(motor_step_pin_6, False)


# Print instructions for when the user has an interface
print("Program Initiated...")
print("e/d: enable/disable")
print("f/r: step forward / reverse")
print("g/t: rotate forward / reverse")
print("x: exit")


# Infinite loop that will not end until the user presses the
# exit key
while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    char = getch()
    print(char)	

    # The stepper will be enabled when the "e" key is pressed
    if (char == "e"):
        stepper_enable()

    # The stepper will be disabled when the "d" key is pressed
    if (char == "d"):
        stepper_disable()

    # The "f" key will step the motor forward
    if (char == "f"):
        step_forward()

    # The "r" key will step the motor in reverse
    if (char == "r"):
        step_reverse()

    # The "g" key will step the motor 1 rotation forwards
    if (char == "g"):
        for x in range(0, pulses_per_rev):
            step_forward()

    # The "t" key will step the motor 1 rotation in reverse
    if (char == "t"):
        for x in range(0, pulses_per_rev):
            step_reverse()

    # The "x" key will break the loop and exit the program
    if (char == "x"):
        print("Program Ended")
        break

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""

# Program will cease all GPIO activity before terminating
io.cleanup()