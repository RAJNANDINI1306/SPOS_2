import RPi . GPIO as GPIO
import time
IR_SENSOR_PIN=7
LED_PIN=3


GPIO.setmode(GPIO.BCM)
GPIO.setup( IR_SENSOR_PIN , GPIO.IN)
GPIO.setup( LED_PIN , GPIO.OUT)


def monitor_ir_sensor ():
    try:
        while True:
            if(GPIO.input( IR_SENSOR_PIN)==0):
               print("obstacle detected")
               GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                print(" no obstacle detected")
                GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("program stopped by user ")
    finally:
        GPIO.cleanup()
if __name__ == "__main__" :
    monitor_ir_sensor()
