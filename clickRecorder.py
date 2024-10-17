import pynput

class ClickRecorder:
    def __init__(self, click_count):
        self.click_count = click_count 
        self.clicks_recorded = 0 
        self.xList = []  # X 좌표를 저장할 리스트
        self.yList = []  # Y 좌표를 저장할 리스트

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.clicks_recorded += 1
            print(f"클릭 {self.clicks_recorded}: ({x}, {y})")
            self.xList.append(x)
            self.yList.append(y)

            if self.clicks_recorded >= self.click_count:
                return False

    def start_listening(self):
        print(f"{self.click_count}번 클릭을 감지합니다. 클릭을 시작하세요...")
        with pynput.mouse.Listener(on_click=self.on_click) as listener:
            listener.join() 
        return self.xList, self.yList

if __name__ == "__main__":
    click_count = int(input("몇 번 클릭하시겠습니까? : "))
    recorder = ClickRecorder(click_count)
    recorder.start_listening()
