import pyautogui
from PIL import Image
import pytesseract

class ReadTextFromImg:
    x1:int
    y1: int
    x2: int
    y2: int

    def __init__(self):
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

    def readTextFromImg(self):
        min_x, max_x = min(self.x1, self.x2), max(self.x1, self.x2)
        min_y, max_y = min(self.y1, self.y2), max(self.y1, self.y2)

        width = max_x - min_x
        height = max_y - min_y

        screenshot = pyautogui.screenshot(region=(min_x, min_y, width, height))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(screenshot, lang ='eng') # 언어 선택

        return text
    