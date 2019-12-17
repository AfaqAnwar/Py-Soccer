import capture
import cv2
import win32api
import win32con
import msvcrt
"""
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
    r_threshold = 120
    g_threshold = 120
    b_threshold = 120

    # Default down-scale factor is 0.05, this is for performance. If accuracy is compromised alter this.
    resize_factor = 0.0825

    while True:
        game = capture.screenshot((x_pos, y_pos, width, height))
        re_width = int(width * resize_factor)
        re_height = int(height * resize_factor)
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

        if msvcrt.kbhit():
            break
