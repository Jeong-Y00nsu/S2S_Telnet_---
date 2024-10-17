import pygetwindow as gw
from pywinauto import Application
import re

class WindowFocusManager:
    def __init__(self, title):
        self.title = title
        self.window = self.find_window_by_title()

    def find_window_by_title(self):
        """주어진 제목을 가진 창을 찾습니다."""
        windows = gw.getWindowsWithTitle(self.title)
        return windows[0] if windows else None

    def focus_window(self):
        """창에 포커스를 맞추고 활성화합니다."""
        if self.window:
            try:
                self.window.activate()  # 창을 활성화
                print(f"Window '{self.title}' is now focused.")
            except Exception as e:
                print(f"Error focusing the window: {e}")
        else:
            print(f"Window with title '{self.title}' not found.")

    def printAllWindowProgramTitles(self):
        windows = gw.getAllTitles()
        for w in windows:
            print(w)

    def focusWindowUsePywinauto(self, program_title):
        try:
            app = Application().connect(title_re=re.compile(".*"+program_title+".*"), backend="win32")
            window = app.top_window()
            window.set_focus()
            print("Window focused successfully!")
        except Exception as e:
            print(f"Error focusing the window: {e}")

# 예시 사용
if __name__ == "__main__":
    program_title = input("Enter the program window title to focus: ")
    manager = WindowFocusManager(program_title)
    #manager.focus_window()
    manager.focusWindowUsePywinauto(program_title)
