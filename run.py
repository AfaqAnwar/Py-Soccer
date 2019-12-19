import smartclick
import win32gui
"""
Runs the "AI" that can play the Soccer Messenger game.
@Author Afaq Anwar
@Version 12/17/2019
"""
emulator_name = "MEmu"
emulator_window = ()


def callback(hwnd, extra):
    window = win32gui.GetWindowRect(hwnd)
    if win32gui.GetWindowText(hwnd) == emulator_name:
        global emulator_window
        emulator_window = window


# Goes through all open windows to hook onto specified emulator.
win32gui.EnumWindows(callback, None)

if emulator_window != ():
    x_pos = emulator_window[0]
    y_pos = emulator_window[1]
    width = emulator_window[2]
    height = emulator_window[3]
    # Modify to only allow opencv to see the game and nothing else.
    smartclick.play(x_pos + 1, y_pos + 65, width - x_pos - 42, height - y_pos - 68)
