import pyautogui
import pyperclip
import time

text = "你好，这是一个自动打字的示例。"

time.sleep(3)  # 3秒内点到输入框

for char in text:
    pyperclip.copy(char)              
    pyautogui.hotkey("command", "v")    
    time.sleep(0.3)                   # 间隔时间，模拟打字
