"""Simple program to demo how to use meshtastic library.
   To run: python examples/hello_world_serial.py
"""

import sys
import meshtastic
import meshtastic.serial_interface

from meshtastic.mesh_pb2 import DATA_PAYLOAD_LEN
print('DATA_PAYLOAD_LEN=', DATA_PAYLOAD_LEN)

# simple arg check
# if len(sys.argv) < 2:
#     print(f"usage: {sys.argv[0]} message")
#     sys.exit(3)

# By default will try to find a meshtastic device,
# otherwise provide a device path like /dev/ttyUSB0
# iface = meshtastic.serial_interface.SerialInterface()
iface = meshtastic.serial_interface.SerialInterface('COM6')
#iface = meshtastic.serial_interface.SerialInterface('COM21')

text = '1234567890ffff'
print('text=', text)
#iface.sendText(sys.argv[1])
#iface.sendText('t' * (DATA_PAYLOAD_LEN-3))
iface.sendText(text)

iface.close()
