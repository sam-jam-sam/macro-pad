print("Starting")

import board

from kmk.extensions.media_keys import MediaKeys

from kmk.extensions.RGB import RGB



from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

rgb = RGB(pixel_pin=board.NEOPIXEL, num_pixels=1)
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.D2,board.D5,board.D6)
keyboard.row_pins = (board.D3,board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())

keyboard.modules = [encoder_handler]

encoder_handler.pins = ( (board.D9, board.D8, board.D7,),
)

keyboard.keymap = [
    [KC.RGB_MODE_BREATHE_RAINBOW, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.LCTRL(KC.LGUI(KC.N3)), KC.LGUI(KC.N4), KC.LGUI(KC.N5)]
]

encoder_handler.map = [ (( KC.VOLU, KC.VOLD, KC.MEDIA_PLAY_PAUSE),), 
]

if __name__ == '__main__':
    keyboard.go()