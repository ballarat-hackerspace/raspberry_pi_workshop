import Adafruit_DHT as dht

h, t = dht.read_retry(dht.AM2302, 4)
#print(“Humidity: {:3.2f}%”.format(h))
#print(“Temperature: {:3.2f}C”.format(t))
print(“h:”, h)
print(“t:”, t)

