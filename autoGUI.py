import clickRecorder
import pyautogui
import time
import readTextFromImg
import pyperclip

class AutoGUI:
    def __init__(self, server_info, delay):
        self.info = server_info  # 서버 정보 목록
        self.delay = delay  # 지연 시간

    def click(self, x, y):
        time.sleep(self.delay)
        pyautogui.click(x, y)

    def inputCommand(self, x, y, command):
        self.click(x, y)  # 좌표를 클릭
        pyautogui.typewrite(command)  # 명령어 입력
        pyautogui.press('enter')  # 엔터키 입력

    def readCommandResult(self, x1, y1, x2, y2):
        recordImg = readTextFromImg.ReadTextFromImg()
        recordImg.x1 = x1
        recordImg.y1 = y1
        recordImg.x2 = x2
        recordImg.y2 = y2
        return recordImg.readTextFromImg()
    
    def inputCommandAtFocus(self, command):
        time.sleep(5)
        pyautogui.typewrite(command, interval=0.1)

    def copyFromFocusedText(self, lineCnt):
        time.sleep(3)
        result_text = ""
        
        for _ in range(lineCnt):
            pyautogui.keyDown('shift')
            pyautogui.press('end')
            pyautogui.keyUp('shift')
            
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.5)
            
            copiedText = pyperclip.paste()
            
            result_text += copiedText + "\n"
            
            pyautogui.press('up')
            time.sleep(0.2)
            
        return result_text



    def execute():
        ''' xshell 실행 '''
        ''' xshell에서 서버 목록 확인 '''
        ''' 서버 정보 목록 크기만큼 반복 '''
        '''     현재 출발지 서버가 xshell 서버 목록에 존재하지 않으면 다음 출발지 서버 진행 '''
        '''     현재 출발지 서버가 telent할 대상 서버들 목록만큼 반복 '''
        '''         연결되어 있는 서버의 입력창에 커서를 포커싱 '''
        '''         telnet [목적지 서버 ip] [목적지 서버 port] 명령어 입력 '''
        '''         sleep                                               '''
        '''         telnet 성공 메시지라면: 성공으로 결과 남기기'''
        '''         telnet 실패 메시지라면: 실패로 결과 남기기'''
        '''         다음 목적지 서버로 telnet 진행 '''

if __name__ == "__main__":
    # recorder = clickRecorder.ClickRecorder(1)
    # x_list, y_list = recorder.start_listening()  # 좌표 받기

    # # 첫 번째 클릭한 좌표를 이용해 AutoGUI 객체 생성
    # clicker = AutoGUI(server_info=[], delay=2)
    # if x_list and y_list:
    #     clicker.inputCommand(x_list[0], y_list[0], "Hello, World!")

    # recorder2 = clickRecorder.ClickRecorder(2)
    # x_list, y_list = recorder2.start_listening()

    # clicker2 = AutoGUI(server_info=[], delay=2)
    # if x_list and y_list:
    #     result = clicker2.readCommandResult(x_list[0], y_list[0], x_list[1], y_list[1])
    # print(result)                                                         
    # text = input("입력하실 문자열 : ")
    a = AutoGUI(server_info=[],delay=2)
    print(a.copyFromFocusedText(3))