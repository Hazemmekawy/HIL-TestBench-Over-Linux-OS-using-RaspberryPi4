#GPIO levels
OFF   = 0
LOW   = 0
CLEAR = 0

ON   = 1
HIGH = 1
SET  = 1

# GPIO edges
RISING_EDGE  = 0
FALLING_EDGE = 1
EITHER_EDGE  = 2

# GPIO modes
INPUT  = 0
OUTPUT = 1
ALT0   = 4
ALT1   = 5
ALT2   = 6
ALT3   = 7
ALT4   = 3
ALT5   = 2

# GPIO Pull Up Down
PUD_OFF  = 0
PUD_DOWN = 1
PUD_UP   = 2

#PWM status
PI_PWM_OK        = 0
PI_NOT_HPWM_GPIO = -95
PI_BAD_HPWM_FREQ = -96
PI_BAD_HPWM_DUTY = -97
PI_BAD_GPIO = -3
PI_NOT_PERMITTED = -41

#SERIAL 
HIGH_PERFORMANCE_SERIAL = "/dev/ttyAMA0"
BAUD_RATE = 9600
SERIAL_FLAGS   =   0
