import subprocess

try:
    nmcli_check = subprocess.Popen(["nmcli", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, nmcli_stderr = nmcli_check.communicate()
except FileNotFoundError:
    print("NetworkManager (nmcli) is not available on this system. This code is for Linux with NetworkManager.")

if "NetworkManager" not in nmcli_stderr.decode():
    exit(1)

profiles = subprocess.check_output(['nmcli', '-t', '-f', 'SSID', 'connection', 'show', '--active']).decode().strip().split('\n')

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for profile in profiles:
    ssid = profile.strip()
    
    try:
        password = subprocess.check_output(['nmcli', '-g', '802-11-wireless-security.psk', 'connection', 'show', ssid]).decode().strip()
        print("{:<30}| {:<}".format(ssid, password))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(ssid, "Password not found"))
