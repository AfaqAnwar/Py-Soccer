import numpy as np
import wx

app = wx.App()
screen = wx.ScreenDC()
"""
@Author Afaq Anwar
@Version 12/22/2019
"""

"""
Method that takes a screenshot of a specific region.
@param region: tuple of (x, y, w, h)
"""
def screenshot(region=None):
    global screen

    assert type(region) is tuple
    assert len(region) == 4

    x = region[0]
    y = region[1]
    w = region[2]
    h = region[3]

    # Construct a bitmap.
    bitmap = wx.Bitmap(w, h)

    # Fill bitmap delete memory, and avoid a memory leak.
    mem = wx.MemoryDC(bitmap)
    mem.Blit(0, 0, w, h, screen, x, y)
    del mem

    # Convert bitmap to image.
    raw_img = bitmap.ConvertToImage()

    # Get data buffer.
    img_data = raw_img.GetData()

    # Construct numpy array from data buffer and reshape it to an image.
    img_data_str = np.frombuffer(img_data, dtype='uint8')
    img = img_data_str.reshape((h, w, 3))
    return img
