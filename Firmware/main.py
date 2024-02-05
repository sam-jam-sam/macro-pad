print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

import neopixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
keyboard.modules.append(holdtap)

keyboard.col_pins = (board.D2,board.D5,board.D6)
keyboard.row_pins = (board.D3,board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.modules.encoder import EncoderHandler
encoder = EncoderHandler()
keyboard.modules = [encoder]
encoder.pins = ( (board.D9, board.D8, board.D7,),
)

def colour(key, keyboard, *args):
    layer = keyboard.active_layers[0]
    if layer == 0:
        pixel.fill((  50,   10,   255))
    elif layer == 1:    
        pixel.fill((200,   10,   50))
    elif layer == 2:
        pixel.fill((  0, 255,   0))
    elif layer == 3:
        pixel.fill((  0,   0, 255))
    

TO_LAYER_0 = KC.TO(0)
TO_LAYER_0.after_press_handler(colour)

TO_LAYER_1 = KC.TO(1)
TO_LAYER_1.after_press_handler(colour)

keyboard.keymap = [
    #Base Layer - 0
    [
        TO_LAYER_1, KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.LCTRL(KC.LGUI(KC.N3)), KC.LGUI(KC.N4), KC.LGUI(KC.N5)
    ],
    #RGB Control - 1
    [
        TO_LAYER_0, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6
    ],
]

encoder.map = [
    (( KC.VOLU, KC.VOLD, KC.MEDIA_PLAY_PAUSE),),
    (( KC.VOLU, KC.VOLD, KC.MEDIA_PLAY_PAUSE),),
]

if __name__ == '__main__':
    keyboard.go()