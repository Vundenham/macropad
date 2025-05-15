from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode
import time

macropad = MacroPad()
macropad.pixels.brightness = 0.3

# Toggle states
toggle_e = False
toggle_mouse1 = False
toggle_mouse2 = False
toggle_hold_mouse1 = False  # Key 4
toggle_hold_mouse2 = False  # Key 5

# Track if buttons are being held
mouse1_held = False
mouse2_held = False

while True:
    event = macropad.keys.events.get()

    # Handle toggles and light up keys
    if event and event.pressed:
        if event.key_number == 0:
            toggle_e = not toggle_e
            macropad.pixels[0] = 0x00FF00 if toggle_e else 0
        elif event.key_number == 1:
            toggle_mouse1 = not toggle_mouse1
            macropad.pixels[1] = 0x00FF00 if toggle_mouse1 else 0
        elif event.key_number == 2:
            toggle_mouse2 = not toggle_mouse2
            macropad.pixels[2] = 0x00FF00 if toggle_mouse2 else 0
        elif event.key_number == 4:
            toggle_hold_mouse1 = not toggle_hold_mouse1
            macropad.pixels[4] = 0x00FF00 if toggle_hold_mouse1 else 0
            if toggle_hold_mouse1 and not mouse1_held:
                macropad.mouse.press(1)
                mouse1_held = True
            elif not toggle_hold_mouse1 and mouse1_held:
                macropad.mouse.release(1)
                mouse1_held = False
        elif event.key_number == 5:
            toggle_hold_mouse2 = not toggle_hold_mouse2
            macropad.pixels[5] = 0x00FF00 if toggle_hold_mouse2 else 0
            if toggle_hold_mouse2 and not mouse2_held:
                macropad.mouse.press(2)
                mouse2_held = True
            elif not toggle_hold_mouse2 and mouse2_held:
                macropad.mouse.release(2)
                mouse2_held = False

    # Repeating actions
    if toggle_e:
        macropad.keyboard.press(Keycode.E)
        macropad.keyboard.release_all()
        time.sleep(1)

    if toggle_mouse1:
        macropad.mouse.press(1)
        macropad.mouse.release(1)
        time.sleep(1)

    if toggle_mouse2:
        macropad.mouse.press(2)
        macropad.mouse.release(2)
        time.sleep(1)
