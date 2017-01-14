#!/usr/bin/python

import math
import random, string
import base64
import json
import paho.mqtt.client as paho
import picamera
from time import sleep

packet_size=3000

def randomword(length):
 return ''.join(random.choice(string.lowercase) for i in range(length))
 
def convertImageToBase64():
 with open("image_test.jpg", "rb") as image_file:
 encoded = base64.b64encode(image_file.read())
 return encoded
 
try: 
 camera = picamera.PiCamera()
 camera.capture('image_test.jpg', resize=(500,281))
 camera.annotate_background = Color('blue')
 camera.annotate_foreground = Color('yellow')
 camera.annotate_text = " Apache NiFi "

 pass
finally:
 camera.close()
 
json_string = json.dumps(row)
client = paho.Client()
client.username_pw_set("username","password")
client.connect("server.cloudmqtt.com", 14162, 60)
client.publish("sensor", payload=json_string, qos=0, retain=True)
