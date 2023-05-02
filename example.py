import time

import meshtastic
import meshtastic.serial_interface
from pubsub import pub

n = 0

def onReceive(packet, interface): # called when a packet arrives
    print(f"\n\nReceived: >>>>>{packet}<<<<<")

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    interface.sendText("hello mesh")

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
# By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0

#interface = meshtastic.serial_interface.SerialInterface('COM21')
interface = meshtastic.serial_interface.SerialInterface('COM6')

t = time.time()
while True:
    if time.time() > t + 10:
        t = time.time()
        n += 1
        interface.sendText('Beacon:' + str(n))
