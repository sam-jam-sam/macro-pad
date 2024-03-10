"""
Example of colour changing pad layering
"""

print("Macro-Pad Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.MOSI,board.D8,board.D7)
keyboard.row_pins = (board.D10,board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.encoder import EncoderHandler
encoder = EncoderHandler()
keyboard.modules = [encoder]

encoder.pins = ( (board.D4, board.D3, board.D1), )
encoder.map = [
    ( (KC.VOLU, KC.VOLD, KC.MUTE), )
    # add extra layers if required
]

from kmk.modules.layers import Layers as Layers
keyboard.modules.append(Layers())

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
keyboard.modules.append(holdtap)

import neopixel
pixel = neopixel.NeoPixel(board.A3, 4)

from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard.SCL = board.A1
keyboard.SDA = board.A0

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
        corner_four={0:OledReactionType.LAYER,1:["Tabs","Play Back","Red","Green"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)

keyboard.extensions.append(oled_ext)

def colour(key, keyboard, *args):
    layer = keyboard.active_layers[0]
    if layer == 0:
        pixel.fill((100,   100,   255))
    elif layer == 1:    
        pixel.fill((100,   50,   255))
    elif layer == 2:
        pixel.fill((255,   50,   50))
    elif layer == 3:
        pixel.fill(( 50,   255,   50))
    
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
        KC.HT(KC.LGUI(KC.N4), TO_LAYER_1), KC.HT(KC.LCTRL(KC.LGUI(KC.N5)), TO_LAYER_2), KC.HT(KC.LGUI(KC.N6), TO_LAYER_3),
        KC.LCTRL(KC.LGUI(KC.N1)), KC.LCTRL(KC.LGUI(KC.N2)), KC.LGUI(KC.N3)
    ],
    # 1 - Red Layer
    [
        KC.HT(KC.MEDIA_PREV_TRACK, TO_LAYER_0), KC.HT(KC.MEDIA_PLAY_PAUSE, TO_LAYER_2), KC.HT(KC.MEDIA_NEXT_TRACK, TO_LAYER_3),
        KC.N1, KC.N1, KC.N1
    ],
    # 2 - Green Layer
    [
        KC.HT(KC.g, TO_LAYER_1), KC.HT(KC.RGB_TOG, TO_LAYER_0), KC.HT(KC.i, TO_LAYER_3),
        KC.RGB_MODE_SWIRL, KC.RGB_MODE_KNIGHT, KC.RGB_MODE_BREATHE_RAINBOW
    ],
    # 3 - Blue Layer
    [
        KC.HT(KC.j, TO_LAYER_1), KC.HT(KC.k, TO_LAYER_2), KC.HT(KC.l, TO_LAYER_0),
        KC.N3, KC.N3, KC.N3
    ],
]

if __name__ == '__main__':
    keyboard.go()
