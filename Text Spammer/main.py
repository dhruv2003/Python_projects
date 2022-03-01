import pyautogui
import time
message=input("Message: ")
n=int(input('How Many times: '))
time.sleep(5)
for i in range(0,int(n)):
    pyautogui.typewrite(msg+'\n')