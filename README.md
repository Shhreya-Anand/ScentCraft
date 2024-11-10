# Aromaverse

The Aromaverse Spigot plugin enhances the Minecraft gaming experience by adding a new dimension of immersion: scent. The plugin can be added to a Spigot Minecraft server. It communicates with a Flask app hosted on a Raspberry Pi to control the smell the user experineces. Depending on the biome the player is in (Plains, Jungle, or Flower Forest), a different scent profile will be experienced. The scent will be sprayed once every few seconds, so long as you are in the biome.

To use this Spigot plugin, follow these steps:

## Build the Plugin
Make sure you have Java and Maven installed.
Create a `pom.xml` if you’re using Maven, or set up your build environment to include Spigot API as a dependency.
Compile the code to create a `BiomeDetector.jar` file.

## Install the Plugin on a Spigot Server
Copy the `BiomeDetector.jar` file to the plugins folder of your Spigot Minecraft server.
Start or restart the server to load the plugin.

## Configure the Plugin
Ensure your Raspberry Pi’s IP address is specified in the `sendSignalToRaspberryPi()` method. Replace `<Raspberry_Pi_IP>` with the actual IP of your Raspberry Pi.

## Run the Python Script on Raspberry Pi
Make sure the Flask app on the Raspberry Pi is running to receive HTTP POST requests.
Run the Python script (python3 script.py) to start the server that listens on port 5000.

## Verify Communication
Ensure the server and the Raspberry Pi are on the same network or can communicate over the internet.
Test by moving a player into the "PLAINS" biome and check if the motor on the Raspberry Pi is activated.

## Monitor Logs
Check the Minecraft server console for any error messages or plugin-related output.
If the signal isn't being sent, verify the Raspberry Pi is reachable and debug any network/firewall issues.

With these steps, the plugin should be active, detecting when players enter the "PLAINS" biome and sending a signal to your Raspberry Pi to control the motor.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Steps to Install Spigot:

    Download BuildTools:
        Go to the Spigot BuildTools page and download BuildTools.jar.

    Set Up BuildTools:
        Place BuildTools.jar in an empty folder.
        Run the following command in that folder:

java -jar BuildTools.jar --rev 1.21.3

    This will build the Spigot server .jar file (e.g., spigot-1.x.x.jar).

Create a New Server Folder:

    Create a folder for your Spigot server (e.g., MySpigotServer).
    Move the generated spigot-1.x.x.jar file into this folder.

Start the Server:

    Open a terminal or command prompt in the server folder and run:

        java -Xmx1024M -Xms1024M -jar spigot-1.x.x.jar nogui

        The server will start and generate the necessary files, including the plugins folder.

    Accept the EULA:
        Open the eula.txt file and change eula=false to eula=true.
        Save the file and restart the server.

Adding Your Plugin:

    Place your BiomeDetector.jar file in the plugins folder.
    Restart the server to load your plugin.

Now, you should have a running Spigot server that can support and run your plugin.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Credits
- Soliman Tomoum
- Shhreya Anand
- Mikhael Thesman
- AJ Young
- Ludovic Anglade
- Covie Yung
