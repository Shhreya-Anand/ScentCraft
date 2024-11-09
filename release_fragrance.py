from flask import Flask, request
import RPi.GPIO as GPIO
import time

app = Flask(name)

Set up GPIO pins (e.g., Pin 17, Pin 27, Pin 22 for different biomes)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Jungle
GPIO.setup(18, GPIO.OUT)  # Plains
GPIO.setup(19, GPIO.OUT)  # Flower Forest

Function to trigger fragrance release based on biome
def releasefragrance(biome):
    # Set the GPIO pin based on the biome
    if biome == "JUNGLE":
        pin = 17  # Jungle uses pin 17
        releasetime = 5  # 5 seconds for Jungle
        waittime = 10  # 10 seconds wait
    elif biome == "PLAINS":
        pin = 18  # Plains uses pin 27
        releasetime = 4  # 4 seconds for Plains
        wait_time = 8  # 8 seconds wait
    elif biome == "FLOWER_FOREST":
        pin = 19  # Flower Forest uses pin 22
        release_time = 6  # 6 seconds for Flower Forest
        wait_time = 12  # 12 seconds wait
    else:
        print(f"Unknown biome: {biome}") #idk this can be sort of our edge case
        return

    # Activate the fragrance release for the selected pin
    GPIO.output(pin, GPIO.HIGH)
    print(f"Releasing fragrance in the {biome} biome...") #when to start
    time.sleep(release_time)
    GPIO.output(pin, GPIO.LOW)
    print(f"Fragrance release for {biome} complete.") #when it stops
    time.sleep(wait_time)
#flask api needs to recieve a post request: write that here

@app.route('/trigger', methods=['POST']) 
def trigger_fragrance():
    biome = request.data.decode('utf-8')  # Get the biome sent from the plugin
    print(f"Biome received: {biome}")

    if biome in ["JUNGLE", "PLAINS", "FLOWER_FOREST"]:
        release_fragrance(biome)
        return "Fragrance triggered successfully!", 200
    else:
        return "Unknown biome", 400

if __name == '__main':
    app.run(host='0.0.0.0', port=5000) #idk which port you're running it on but we can change this
