import time
import board
import adafruit_dht

# Initialize the DHT11 sensor on GPIO4
dht_device = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temp: {temperature_c:.1f}°C  Humidity: {humidity}%")
    except RuntimeError as error:
        # Reading doesn't always work; just retry
        print(f"Reading error: {error.args[0]}")
    time.sleep(2.0)