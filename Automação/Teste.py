from turtle import right
import pyautogui
import pyperclip
import time

pyautogui.hotkey("alt" , "tab")
pyautogui.hotkey("ctrl" , "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=318, y=265, clicks=2)

time.sleep(3)

pyautogui.click(x=389, y=455, button="right")
time.sleep(2)
pyautogui.click(x=541, y=909)

time.sleep(5)