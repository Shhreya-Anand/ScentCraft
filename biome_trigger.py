from flask import Flask, request
import RPi.GPIO as GPIO
import time

Setup for GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Use GPIO pin 18 for the action

app = Flask(name)

@app.route('/trigger', methods=['POST'])
def handletrigger():
    print("Biome detected, turning on GPIO pin for 5 seconds.")
    GPIO.output(18, GPIO.HIGH)  # Turn on GPIO pin
    time.sleep(5)               # Wait for 5 seconds
    GPIO.output(18, GPIO.LOW)   # Turn off GPIO pin
    return 'GPIO pin activated', 200

if name == '_main':
    app.run(host='172.30.177.75', port=5000)
