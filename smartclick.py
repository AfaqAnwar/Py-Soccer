import capture
import cv2
import win32api
import win32con
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
    # Tolerances for the black on the soccer ball. Increase or decrease based on pixel density.
    r_threshold = 95
    g_threshold = 95
    b_threshold = 95

    # Factor which the image is scaled down by.
    # Lower tends to be faster but is also inaccurate at times.
    # A good factor is dependent upon the scale of the game.
    resize_factor = 0.08

    re_width = int(width * resize_factor)
    re_height = int(height * resize_factor)

    while True:
        game = capture.screenshot((x_pos, y_pos, width, height))
        game = cv2.resize(game, (re_width, re_height))

        clicked = False
        for i in range(re_height):
            for j in range(re_width):
                color_values = game[i][j]
                if color_values[0] <= r_threshold and color_values[1] <= b_threshold and color_values[2] <= g_threshold:
                    click(int((j / resize_factor) + x_pos), int((i / resize_factor) + y_pos))
                    clicked = True
                    break
            if clicked:
                break