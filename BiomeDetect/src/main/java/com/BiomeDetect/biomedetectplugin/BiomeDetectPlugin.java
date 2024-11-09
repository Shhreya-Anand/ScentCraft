package com.BiomeDetect.biomedetectplugin;

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.scheduler.BukkitRunnable;

public class BiomeDetectPlugin extends JavaPlugin {
    public String getCurrBiome(Location location, World world) {
        return world.getBiome(location.getBlockX(), location.getBlockY(), location.getBlockZ()).name();
    }

    @Override
    public void onEnable() {
        // Run a task to check the player's biome every few seconds

        new BukkitRunnable() {
            @Override
            public void run() {
                for (Player player : Bukkit.getOnlinePlayers()) {
                    Location location = player.getLocation();
                    World world = location.getWorld();

                    String[] biomes = {"PLAINS", "JUNGLE", "FLOWER_FOREST"};

                    for (String biome : biomes) {
                        if (world != null && getCurrBiome(location, world).equalsIgnoreCase(biome)) {
                            player.sendMessage("You are in the " + biome + " biome!");
                            sendSignalToRaspberryPi(biome);
                        }
                    }
                }
            }
        }.runTaskTimer(this, 0L, 100L); // Run every 5 seconds (100 ticks)
    }
    private void sendSignalToRaspberryPi(String biome) {
        try {
            URL url = new URL("http://172.30.177.75:5000/activate"); // Replace with your Raspberry Pi IP
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            // Construct JSON data
            String jsonInputString = "{\"biome\": \"" + biome + "\"}";
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int responseCode = conn.getResponseCode();
            getLogger().info("HTTP request to Raspberry Pi for " + biome + " returned response code: " + responseCode);
            conn.disconnect();
        } catch (Exception e) {
            getLogger().severe("Failed to send HTTP request for " + biome + ": " + e.getMessage());
            e.printStackTrace();
        }
    }
}