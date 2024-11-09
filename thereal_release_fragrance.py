from flask import Flask, request
import RPi.GPIO as GPIO
import time
from threading import Timer

#Setup for GPIO
GPIO.setmode(GPIO.BCM)
relaypins = {
    "PLAINS": 17,      # Replace with your actual GPIO pin numbers
    "JUNGLE": 27,
    "FLOWERFOREST": 22
}

#Initialize GPIO pins
for pin in relaypins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Ensure all relays start in the OFF state

app = Flask(name)

#Timer dictionary to manage relay activation every 30 seconds
timers = {}

def activaterelay(biome, pin):
    print(f"Activating relay for {biome} biome on GPIO pin {pin}.")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(5)  # Relay stays on for 5 seconds
    GPIO.output(pin, GPIO.LOW)
    print(f"Deactivated relay for {biome} biome.")

    # Schedule the relay to activate again after 30 seconds
    timers[biome] = Timer(30, activate_relay, args=[biome, pin])
    timers[biome].start()

@app.route('/activate', methods=['POST'])
def activate_relay_endpoint():
    data = request.get_json()
    biome = data.get('biome')

    if biome in relay_pins:
        # If a timer for the biome already exists, cancel it to reset the cycle
        if biome in timers:
            timers[biome].cancel()

        pin = relay_pins[biome]
        activate_relay(biome, pin)  # Trigger the relay immediately
        return f'Relay for {biome} activated and scheduled', 200
    else:
        return 'Invalid biome', 400 
        

if __name == '__main':
    app.run(host='0.0.0.0', port=5000)