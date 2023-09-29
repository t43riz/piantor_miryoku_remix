
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


keyboard.keymap = [
# BASE
[
    KC.TAB,  KC.Q,  KC.W, KC.E, KC.R,  KC.T, KC.Y,  KC.U,  KC.I, KC.O, KC.P,  KC.BSPC,
    KC.LSHIFT, KC.A, KC.S, KC.D, KC.F,  KC.G,     KC.H, KC.J, KC.K, KC.L, KC.SCOLON,  KC.ENT,
    KC.LCTRL, KC.Z, KC.X,  KC.C,  KC.V, KC.B,     KC.N, KC.M, KC.COMM,  KC.DOT,  KC.RSHIFT, KC.NO,
                                        KC.GP17, KC.LCMD, KC.SPACE,




                                        KC.SPACE, KC.RCMD, KC.ENT,

],
# EXTRA
[
KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.NO,

],
# TAP
[
KC.NO, KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT, KC.NO,
KC.NO, KC.A, KC.R, KC.S, KC.T, KC.G, KC.M, KC.N, KC.E, KC.I, KC.O, KC.NO,
KC.NO, KC.Z, KC.X, KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.DOT, KC.SLSH, KC.NO,
KC.ESC, KC.SPC, KC.TAB, KC.ENT, KC.BSPC, KC.DEL
],
# BUTTON
[
KC.NO, KC.LGUI(KC.Z), KC.LGUI(KC.X), KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LSFT(KC.LGUI(KC.Z)), KC.LSFT(KC.LGUI(KC.Z)), KC.LGUI(KC.V), KC.LGUI(KC.C), KC.LGUI(KC.X), KC.LGUI(KC.Z), KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.LGUI(KC.Z), KC.LGUI(KC.X), KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LSFT(KC.LGUI(KC.Z)), KC.LSFT(KC.LGUI(KC.Z)), KC.LGUI(KC.V), KC.LGUI(KC.C), KC.LGUI(KC.X), KC.LGUI(KC.Z), KC.NO,
KC.MB_MMB, KC.MB_LMB, KC.MB_RMB, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# NAV
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.LSFT(KC.LGUI(KC.Z)), KC.LGUI(KC.V), KC.LGUI(KC.C), KC.LGUI(KC.X), KC.LGUI(KC.Z), KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.CW, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END, KC.NO,
KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL
],
# MOUSE
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.LSFT(KC.LGUI(KC.Z)), KC.LGUI(KC.V), KC.LGUI(KC.C), KC.LGUI(KC.X), KC.LGUI(KC.Z), KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.NO, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.NO, KC.NO, KC.NO, KC.MW_DN, KC.MW_UP, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MB_RMB, KC.MB_LMB, KC.MB_MMB
],
# MEDIA
[
KC.NO, KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.PS_TOG, KC.MPRV, KC.VOLD, KC.VOLU, KC.MNXT, KC.NO,
KC.NO, KC.NO, KC.RALT, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.NO, KC.HID, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
KC.NO, KC.NO, KC.NO, KC.MSTP, KC.MPLY, KC.MUTE
],
# NUM
[
KC.NO, KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.DF(7), tap_time=200), KC.TD(KC.NO, KC.DF(4), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO
],
# SYM
[
KC.NO, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RCBR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.COLN, KC.DLR, KC.PERC, KC.CIRC, KC.PLUS, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.PIPE, KC.NO, KC.TD(KC.NO, KC.DF(8), tap_time=200), KC.TD(KC.NO, KC.DF(5), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.LPRN, KC.RPRN, KC.UNDS, KC.NO, KC.NO, KC.NO
],
# FUN
[
KC.NO, KC.F12, KC.F7, KC.F8, KC.F9, KC.PSCR, KC.NO, KC.TD(KC.NO, KC.DF(0), tap_time=200), KC.TD(KC.NO, KC.DF(1), tap_time=200), KC.TD(KC.NO, KC.DF(2), tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.NO,
KC.NO, KC.F11, KC.F4, KC.F5, KC.F6, KC.SLCK, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.NO,
KC.NO, KC.F10, KC.F1, KC.F2, KC.F3, KC.PAUS, KC.NO, KC.TD(KC.NO, KC.DF(9), tap_time=200), KC.TD(KC.NO, KC.DF(6), tap_time=200), KC.RALT, KC.NO, KC.NO,
KC.APP, KC.SPC, KC.TAB, KC.NO, KC.NO, KC.NO
],

]

layer_names_list = [
"Base", "Extra", "Tap", "Button", "Nav", "Mouse", "Media", "Num", "Sym", "Fun",
]

if __name__ == '__main__':
     print('starting Miryoku KMK')
     keyboard.go()
