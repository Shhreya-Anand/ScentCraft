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
        // Run a task to check player's biome every few seconds
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
                            sendSignalToRaspberryPi();
                        }
                    }
                }
            }
        }.runTaskTimer(this, 0L, 100L); // Run every 5 seconds (100 ticks)
    }
private void sendSignalToRaspberryPi() {
        try {
            URL url = new URL("http://172.30.177.75:5000/trigger");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setDoOutput(true);

            try (OutputStream os = conn.getOutputStream()) {
                os.write("trigger".getBytes("utf-8"));  // Simple message body
            }

            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                System.out.println("Signal sent successfully.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
