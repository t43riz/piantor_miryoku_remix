
import board
        
       
from kb import KMKKeyboard, isRight; keyboard = KMKKeyboard()
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.keys import KC
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())
LAYER_TAP = KC.LT(1, KC.END, prefer_hold=True, tap_interrupted=False, tap_time=250) 
def rcmd_handler(event, keymap):
    if event.event_type == EventType.KEY_DOWN:
        # If KC.RCMD is held down, activate the "Number Row" layer
        keymap.layer_change(1)  # 2 corresponds to the "Number Row" layer
    elif event.event_type == EventType.KEY_UP:
        # If KC.RCMD is released, revert to the base layer
        keymap.layer_change(0)  # 0 corresponds to the "Base" layer

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

data_pin = board.GP1 if split_side == SplitSide.LEFT else board.GP0
data_pin2 = board.GP0 if split_side == SplitSide.LEFT else board.GP1

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False, 
    data_pin=data_pin,
    data_pin2=data_pin2
)
keyboard.modules.append(split)
MOMENTARY = KC.MO(1)
MOMENTARY2 = KC.MO(2)

keyboard.keymap = [
# BASE
[
    KC.TAB,  KC.Q,  KC.W, KC.E, KC.R,  KC.T,      KC.Y,  KC.U,  KC.I, KC.O, KC.P,  KC.BSPC,
    KC.LSHIFT, KC.A, KC.S, KC.D, KC.F,  KC.G,     KC.H, KC.J, KC.K, KC.L, KC.SCOLON,  KC.QUOTE,
    KC.LCTRL, KC.Z, KC.X,  KC.C,  KC.V, KC.B,     KC.N, KC.M, KC.COMM,  KC.DOT,  KC.SLASH, KC.ENT,
                    KC.LCMD , KC.SPACE, MOMENTARY,    KC.RALT, KC.SPACE, MOMENTARY2,

],

# TAP
[
    KC.TAB, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,     KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS,
    KC.LSHIFT, KC.A, KC.S, KC.D, KC.F,  KC.G,                 KC.H, KC.J, KC.K, KC.UP, KC.RIGHT,  KC.BSPC,
    KC.LCMD, KC.Z, KC.X,  KC.C,  KC.V, KC.B,                 KC.N, KC.M, KC.LEFT,  KC.DOWN,  KC.SLASH, KC.ENT,
                    KC.LCMD , KC.SPACE, KC.NO,             KC.RALT, KC.SPACE, KC.SLASH,
],
# t2
[
    KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,     KC.MB_LMB, KC.MS_UP, KC.MB_RMB, KC.N9, KC.N0, KC.MINUS,
    KC.LSHIFT, KC.A, KC.S, KC.D, KC.F,  KC.G,                 KC.MS_LEFT, KC.MS_DOWN, KC.MS_RIGHT, KC.UP, KC.RIGHT,  KC.BSPC,
    KC.LCMD, KC.Z, KC.X,  KC.C,  KC.V, KC.B,                 KC.N, KC.M, KC.LEFT,  KC.DOWN,  KC.SLASH, KC.ENT,
                    KC.LCMD , KC.SPACE, KC.NO,             KC.RALT, KC.SPACE, KC.NO,
],

]

layer_names_list = [
"Base", "Tap", "t2",
]

if __name__ == '__main__':
     print('starting  KMK')
     keyboard.go()
