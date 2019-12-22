import capture
import cv2
import win32api
import win32con
import numpy as np
import time
"""
The Brain of the "AI".
@Author Afaq Anwar
@Version 12/17/2019
"""

"""
Method that takes allows for efficient mouse click manipulation.
@param x: x coordinate of desired mouse click.
@param y: y coordinate of desired mouse click.
"""
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


"""
Plays the game.
@param x_pos: x coordinate of desired start to border.
@param y_pos: y coordinate of desired start to border.
@param width: width of window.
@param height: height of window.
"""
def play(x_pos, y_pos, width, height):
    # Upper limit of ranges to not black out.
    r_threshold = 90
    g_threshold = 90
    b_threshold = 90

    # Factor which the image is scaled down by.
    # Lower tends to be faster but is also inaccurate at times.
    # A good factor is dependent upon the scale of the game. Larger Original Window = Smaller Scale Factor.
    resize_factor = 0.5

    re_width = int(width * resize_factor)
    re_height = int(height * resize_factor)

    lower = np.array([0, 0, 0])
    upper = np.array([r_threshold, g_threshold, b_threshold])

    while True:
        game = capture.screenshot((x_pos, y_pos, width, height))
        mask = cv2.inRange(game, lower, upper)
        masked_game = cv2.bitwise_and(game, game, mask=mask)
        final_game = cv2.resize(masked_game, (re_width, re_height))
        white_pixels = np.array(np.where(final_game > 0))
        if len(white_pixels[0]) > 0:
            first_white_pixel = white_pixels[:, 0]
            click(int(first_white_pixel[1] / resize_factor) + x_pos, int(first_white_pixel[0] / resize_factor) + y_pos)
