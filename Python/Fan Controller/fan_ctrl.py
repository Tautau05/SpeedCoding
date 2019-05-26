#import
import time
import os
import RPi.GPIO as GPIO

#variables
temp = ''
update_interval = 5



#Rasp-Temp
def measure_CPU_temp():
  temp = os.popen("sudo vcgencmd measure_temp").readline()

  temp = temp.replace("temp=", '')
  temp = temp.replace("'C", '')
  temp = temp.replace(".", '')

  if int(temp) >= 300:
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
  else:
    GPIO.setup(4, GPIO.IN)


#start
while True:
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)

  while True:
    time.sleep(update_interval)

    #add now parts below
    measure_CPU_temp()

