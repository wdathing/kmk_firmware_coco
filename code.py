print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP8, board.GP9, board.GP10,  board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.COMM,KC.A, KC.B,  KC.C,  KC.D,  KC.E,  KC.F,  KC.G, 
    KC.H,KC.I, KC.J,  KC.K,  KC.L,  KC.M,  KC.N,  KC.O, 
    KC.P,KC.Q, KC.R,  KC.S,  KC.T,  KC.U,  KC.V,  KC.W, 
    KC.X,KC.Y, KC.Z,  KC.UP,  KC.DOWN,  KC.LEFT,  KC.RIGHT,  KC.SPC, 
    KC.N0,KC.N1, KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7, 
    KC.N8,KC.N9, KC.CLN,  KC.SCLN,  KC.COMM,  KC.MINS,  KC.DOT,  KC.SLSH, 
    KC.ENTER,KC.HOME, KC.GESC,  KC.LALT,  KC.LCTRL,  KC.F1,  KC.F2,  KC.LSFT, 
    ]
]

if __name__ == '__main__':
    keyboard.go()