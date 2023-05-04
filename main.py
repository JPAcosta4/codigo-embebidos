import time
from machine import Pin, SoftI2C, time_pulse_us
from stepper import Stepper
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

def measure_distance():
    # Send a trigger pulse
    TRIGGER_PIN.value(1)
    time.sleep(0.1)  # Wait for 10 microseconds
    TRIGGER_PIN.value(0)

    # Measure the duration of the echo pulse
    duration = time_pulse_us(ECHO_PIN, 1, 30000)  # Wait for up to 30 milliseconds

    # Calculate distance based on the duration of the echo pulse
    distance_cm = duration / 58  # Divide by 58 to convert duration to distance in centimeters
    return distance_cm


def measure_distance_avg(num_measurements):
    distances = []
    for i in range(num_measurements):
        distance_cm = measure_distance()
        distances.append(distance_cm)
        time.sleep(0.05)
    avg_distance = sum(distances) / len(distances)
    return avg_distance

TRIGGER_PIN = Pin(32, mode=Pin.OUT)
ECHO_PIN = Pin(35, mode=Pin.IN)

boton_azul= Pin(21, Pin.IN, Pin.PULL_UP)
boton_negro=Pin(4, Pin.IN, Pin.PULL_UP)
boton_blanco=Pin(16, Pin.IN, Pin.PULL_UP)


I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(17), freq=10000) #I2C for ESP32
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


IN1 = Pin(13,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(27,Pin.OUT)
IN4 = Pin(33,Pin.OUT)

# Define the number of steps per revolution
# Divide the degrees per step by 360 to get the steps
stepsPerRevolution = 2048

# Create a new Stepper object
stepperName = Stepper(stepsPerRevolution, IN1, IN2, IN3, IN4)

# Set the RPM of the stepper motor
stepperName.setRPM(10)

bul=True
bul1=True
luzbul=True

luzroja = Pin(25, Pin.OUT)
luzverde = Pin(26, Pin.OUT)

while True:
    distance = measure_distance_avg(10)

    if luzbul == False:
        luzverde.value(0)
        luzroja.value(1)
    else:
        luzverde.value(1)
        luzroja.value(0)


    if bul1 == True:
        lcd.putstr("Presione un     boton")
        bul1 = False
            
    if boton_azul.value() == 0:
        lcd.clear()
        time.sleep(1)
        lcd.putstr("Dispensando     Mani ...")
        stepperName.step(stepsPerRevolution)
        lcd.clear()
        bul = True
        bul1= True
        
    elif boton_negro.value() == 0:
        lcd.clear()
        time.sleep(1)
        lcd.putstr("Dispensando     Almendras ...")
        stepperName.step(stepsPerRevolution)
        lcd.clear()
        bul = True
        bul1 = True

    elif boton_blanco.value() == 0:
        lcd.clear()
        time.sleep(1)
        lcd.putstr("Dispensando     Nueces ...")
        stepperName.step(stepsPerRevolution)
        lcd.clear()
        bul = True
        bul1 = True

    if distance > 12.8 and bul == True:
        lcd.clear()
        time.sleep(1)
        lcd.putstr("Capacidad menor al 20%")
        time.sleep(2)
        lcd.clear()
        bul = False 
        bul1 = True
        luzbul = False

    
    """
    time.sleep(1.5)
    motor.move(90) # tourne le servo à 90°
    time.sleep(1.5)
    motor.move(0) # tourne le servo à 180°
    time.sleep(1.5)
    motor.move(180) # tourne le servo à 90°
    time.sleep(1.5)
    motor.move(0) # tourne le servo à 0°
    time.sleep(3)

    led1.value(1)
    time.sleep(1)
    led1.value(0)
    time.sleep(1)
    led1.value(1)
    time.sleep(1)
    led1.value(0)

    from machine import Pin
    from time import sleep
    from stepper import Stepper

    IN1 = Pin(13,Pin.OUT)
    IN2 = Pin(14,Pin.OUT)
    IN3 = Pin(27,Pin.OUT)
    IN4 = Pin(33,Pin.OUT)


    # Define the number of steps per revolution
    # Divide the degrees per step by 360 to get the steps
    stepsPerRevolution = 2048

    # Create a new Stepper object
    stepperName = Stepper(stepsPerRevolution, IN1, IN2, IN3, IN4)

    # Set the RPM of the stepper motor
    stepperName.setRPM(10)


    while True:
        # This should make the stepper do a full 360 degrees
        stepperName.step(stepsPerRevolution)
        sleep(2)
    """
    