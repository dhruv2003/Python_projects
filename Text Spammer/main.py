import pyautogui
import time
message=imput("Message: ")
n=input('How Many times: ')
time.sleep(5)
for i range(0,int(n)):
    pyautogui.typewrite(msg+'\n')