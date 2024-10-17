import win32gui
import win32con

class WindowFocusManager:
    def __init__(self, title):
        self.title = title
        self.hwnd = self.find_window_by_title()

    def find_window_by_title(self):
        """주어진 제목을 가진 창의 핸들을 찾습니다."""
        def enum_windows_proc(hwnd, result_list):
            if win32gui.IsWindowVisible(hwnd) and self.title in win32gui.GetWindowText(hwnd):
                result_list.append(hwnd)

        windows = []
        win32gui.EnumWindows(enum_windows_proc, windows)
        return windows[0] if windows else None

    def focus_window(self):
        """창에 포커스를 맞추고 활성화합니다."""
        if self.hwnd:
            win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)  # 최소화된 창을 복원
            win32gui.SetForegroundWindow(self.hwnd)  # 창을 포커스
            print(f"Window '{self.title}' is now focused.")
        else:
            print(f"Window with title '{self.title}' not found.")

# 예시 사용
if __name__ == "__main__":
    program_title = input("Enter the program window title to focus: ")
    manager = WindowFocusManager(program_title)
    manager.focus_window()
