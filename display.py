from RPLCD import CharLCD
from RPLCD import cursor
import time
import RPi.GPIO as GPIO
import commands
import glob

# get the ip
def get_ip_address(command):
    result = commands.getoutput(command)
    return result

GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#counter = 0

try:
    """
    # here you put your main loop or block of code
    while counter <= 10:

        lcd.write_string(u"Hello world!")
        counter += 1
        time.sleep(1)
        lcd.clear()
        time.sleep(1)
    print "Run " + counter + " times"
    """
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
    time.sleep(10)
    lcd.clear()
    lcd.write_string("IP Address:")
    lcd.cursor_pos = (1, 0)
    x = get_ip_address("ifconfig | grep Bcast | cut -d: -f 2 | cut -d' ' -f1")
    lcd.write_string(x)
    time.sleep(10)
    lcd.clear()


except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    #print "KeyboardInterrupt, counter = " + str(counter) # print value of counter
    print "KeyboardInterrupt"

except Exception, e:
    print(str(e))
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    print "Other error or exception occurred!"

finally:
    GPIO.cleanup() # this ensures a clean exit