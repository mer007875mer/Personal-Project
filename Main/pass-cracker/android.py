import subprocess

meta_data = subprocess.check_output(['termux-wifi-connectioninfo'])

data = meta_data.decode('utf-8', errors='replace')

wifi_info = {}
for line in data.split('\n'):
    parts = line.strip().split(': ')
    if len(parts) == 2:
        wifi_info[parts[0]] = parts[1]

if 'ssid' in wifi_info and 'psk' in wifi_info:
    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("----------------------------------------------")
    print("{:<30}| {:<}".format(wifi_info['ssid'], wifi_info['psk']))
else:
    print("Wi-Fi information not found.")
