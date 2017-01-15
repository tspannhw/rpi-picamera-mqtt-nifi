#!/usr/bin/python

import os
import datetime
import ftplib
import traceback
import math
import random, string
import base64
import json
import paho.mqtt.client as mqtt
import picamera
from time import sleep
from time import gmtime, strftime

packet_size=3000

def randomword(length):
 return ''.join(random.choice(string.lowercase) for i in range(length))
 

# Create unique image name
img_name = 'pi_image_{0}_{1}.jpg'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
 
# Capture Image from Pi Camera
try: 
 camera = picamera.PiCamera()
 camera.annotate_text = " Stored with Apache NiFi "
 camera.capture(img_name, resize=(500,281))

 pass
finally:
 camera.close()
 
# MQTT
client = mqtt.Client()
client.username_pw_set("CloudMqttUserName","!MakeSureYouHaveAV@5&L0N6Pa55W0$4!")
client.connect("cloudmqttiothoster", 14162, 60)

f=open(img_name)
fileContent = f.read()
byteArr = bytearray(fileContent)
f.close()
message = '"image": {"bytearray":"' + byteArr + '"} } '
print client.publish("image",payload=message,qos=1,retain=False)
client.disconnect()

# FTP
ftp = ftplib.FTP()
ftp.connect("ftpserver", "21")
try:
    ftp.login("reallyLongUserName", "FTP PASSWORDS SHOULD BE HARD")
    ftp.storbinary('STOR ' + img_name, open(img_name, 'rb'))
finally:
    ftp.quit()

# clean up sent file
os.remove(img_name)

