import pyautogui
print('Press Ctrl-C to quit.')
last = ""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        if positionStr != last:
            last = positionStr
            print(positionStr)
except KeyboardInterrupt:
    print('\n')