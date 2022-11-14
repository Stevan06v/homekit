import network
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('LiwestC959','FTCghagnCTeT')

# WLAN-Verbindungsstatus prüfen
print('Warten auf WLAN-Verbindung')
while not wlan.isconnected() and wlan.status() >= 0:
    time.sleep(1)
print('WLAN-Verbindung hergestellt / Status:', wlan.status())
