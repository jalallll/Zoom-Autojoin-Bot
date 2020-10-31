import subprocess
import pyautogui
import time
import pandas as pd
import cv2
from datetime import datetime
from PIL import ImageGrab
import numpy as np


class Bot:

    def start(self, id, key):
        print(id)
        subprocess.call(
            'C:\\Users\\Jalal\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        join = None

        while join is None:
            join = pyautogui.locateCenterOnScreen(
                'join.png', grayscale=True)
            print(join)
        print(join)
        pyautogui.moveTo(join)
        pyautogui.click()

        time.sleep(1)
        pyautogui.write(id)
        confirm = pyautogui.locateCenterOnScreen("confirm.PNG", grayscale=True)
        pyautogui.moveTo(confirm)
        pyautogui.click()
        time.sleep(2)
        pyautogui.write(key)
        agn = pyautogui.locateCenterOnScreen("agn.PNG", grayscale=True)
        pyautogui.moveTo(agn)
        pyautogui.click()

        time.sleep(2)
        wo = pyautogui.locateCenterOnScreen("wo.PNG", grayscale=True)
        pyautogui.moveTo(wo)
        pyautogui.click()
        time.sleep(1)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        o = cv2.VideoWriter("lec.avi", fourcc, 30.0, (3840, 2160))

        go = True

        while go == True:
            rec = ImageGrab.grab()
            ar = np.array(rec)
            f = cv2.cvtColor(ar, cv2.COLOR_BGR2RGB)
            cv2.imshow("Screen", f)
            o.write(f)

            if cv2.waitKey(1) == ord('x') or cv2.waitKey(1) == 27:
                leave = pyautogui.locateCenterOnScreen(
                    'leave.PNG', grayscale=False)
                pyautogui.moveTo(leave)
                pyautogui.click()
                cv2.destroyAllWindows()
                o.release()
                Bot.terminate()
                go = False
        Bot.terminate()
        return o, go

    def terminate(self, msg):
        print("Terminating")
        print(msg)
        leave = pyautogui.locateCenterOnScreen('leave.PNG', grayscale=False)
        pyautogui.moveTo(leave)
        pyautogui.click()
        return "done"
