import re
import pyautogui
from time import sleep

result =  '1,25'

res = []

if " " in result:
    result = result.replace(' ', '')
if ',' in result:
    result = result.replace(',', '')
if '.' in result:
    result = result.replace('.', '')

try:
    for char in result:
        res.append(int(char))
except:
    print "problem at ress.append(int(char))"


print res

pyautogui.moveTo(x=100, y=100)
sleep(2)
pyautogui.moveTo(710, 657, 3, pyautogui.easeInOutQuad)
