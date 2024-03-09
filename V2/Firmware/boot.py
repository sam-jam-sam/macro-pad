import supervisor
import board
import storage
import usb_cdc

from digitalio import DigitalInOut, Direction, Pull

row = DigitalInOut(board.D10)
col = DigitalInOut(board.MOSI)

row.direction = Direction.INPUT
col.direction = Direction.OUTPUT

row.pull = Pull.DOWN
col.value = True

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
