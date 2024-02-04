"""
Example of colour changing layering
"""

print("Macro-Pad Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D2,board.D5,board.D6)
keyboard.row_pins = (board.D3,board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.encoder import EncoderHandler
encoder = EncoderHandler()
keyboard.modules = [encoder]

encoder.pins = ( (board.D9, board.D8, board.D7,))
encoder.map = [
    (( KC.VOLU, KC.VOLD, KC.MEDIA_PLAY_PAUSE )) 
]

from kmk.modules.layers import Layers as Layers
keyboard.modules.append(Layers())

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
keyboard.modules.append(holdtap)

import neopixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

def colour(key, keyboard, *args):
    layer = keyboard.active_layers[0]
    if layer == 0:
        pixel.fill((  0,   0,   0))
    elif layer == 1:    
        pixel.fill((255,   0,   0))
    elif layer == 2:
        pixel.fill((  0, 255,   0))
    elif layer == 3:
        pixel.fill((  0,   0, 255))
    

TO_LAYER_0 = KC.TO(0)
TO_LAYER_0.after_press_handler(colour)

TO_LAYER_1 = KC.TO(1)
TO_LAYER_1.after_press_handler(colour)

TO_LAYER_2 = KC.TO(2)
TO_LAYER_2.after_press_handler(colour)

TO_LAYER_3 = KC.TO(3)
TO_LAYER_3.after_press_handler(colour)


keyboard.keymap = [
    # 0 - Base Layer
    [
        KC.HT(KC.a, TO_LAYER_1), KC.HT(KC.b, TO_LAYER_2), KC.HT(KC.c, TO_LAYER_3),
        KC.VOLU, KC.VOLD, KC.N0
    ],
    # 1 - Red Layer
    [
        KC.HT(KC.d, TO_LAYER_0), KC.HT(KC.e, TO_LAYER_2), KC.HT(KC.f, TO_LAYER_3),
        KC.N1, KC.N1, KC.N1
    ],
    # 2 - Green Layer
    [
        KC.HT(KC.g, TO_LAYER_1), KC.HT(KC.h, TO_LAYER_0), KC.HT(KC.i, TO_LAYER_3),
        KC.N2, KC.N2, KC.N2
    ],
    # 3 - Blue Layer
    [
        KC.HT(KC.j, TO_LAYER_1), KC.HT(KC.k, TO_LAYER_2), KC.HT(KC.l, TO_LAYER_0),
        KC.N3, KC.N3, KC.N3
    ],
]

# 

if __name__ == '__main__':
    keyboard.go()