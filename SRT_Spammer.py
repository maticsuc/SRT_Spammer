import pyautogui
import time
import keyboard

file = "Home Alone-English.srt"


start_time = 10
speed_time = 0.1


time.sleep(start_time)


file = open(file, 'r').read().split("\n")


file = [x for x in file if '-->' not in x and len(x) != 0]

neki = {}
tmp = 1

for x in file:
    if x.isnumeric():
        neki[int(x)] = []
        tmp = int(x)
    else:
        x = x.replace('<i>','').replace('</i>','').replace('</font>','').replace('\i0','').replace('\i1','')
        if "font color=" in x:
            index = x.index("font color=")
            x = x[0:index] + x[index + 20:]
        neki[tmp].append(x)


start_index = 361
end_index = 396


for i in range(start_index, end_index + 1):
    if keyboard.is_pressed('q'):
        break
    for line in neki[i]:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        time.sleep(speed_time)
