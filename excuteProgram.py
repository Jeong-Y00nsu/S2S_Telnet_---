import subprocess
import os

class ExecuteProgram:
    def __init__(self, programPath):
        self.programPath = programPath

    def is_valid_path(self):
        return os.path.exists(self.programPath)

    def runProgram(self):
        if self.is_valid_path():
            try:
                process = subprocess.Popen([self.programPath], 
                                           stdout=subprocess.PIPE, 
                                           stderr=subprocess.PIPE)
                print("프로그램이 실행되었습니다.")

                stdout, stderr = process.communicate()

                if stdout:
                    print(f"표준 출력:\n{stdout.decode()}")
                if stderr:
                    print(f"오류 출력:\n{stderr.decode()}")

            except Exception as e:
                print(f"실행 중 오류가 발생했습니다: {e}")
        else:
            print(f"경로가 유효하지 않습니다: {self.programPath}")

# 사용 예제
if __name__ == "__main__":
    programPath = r"D:\ZoomInstaller.exe"
    
    runner = ExecuteProgram(programPath)
    runner.runProgram()
