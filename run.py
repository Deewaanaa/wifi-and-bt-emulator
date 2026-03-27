import time
import random
import os
import sys
import subprocess
import platform

# ============================================================
#   🏆 DEEWANA STAR PRO - Ultra-Realistic Local Edition 🏆
#      100% Offline | Zero Data Sharing | Max Realism
# ============================================================

# Fallback names in case the computer has no Wi-Fi adapter
FALLBACK_WIFI = [
    "Netgear_5G", "Xfinitywifi", "ATT_WIFI_901", "Home_Network",
    "Linksys_Router", "SpectrumSetup", "Default", "Guest_Network"
]

FUNNY_BT_NAMES = [
    "AirPods Pro", "Samsung Galaxy S23", "JBL Charge 5", 
    "Sony WH-1000XM4", "LG Smart TV", "Unknown Device", 
    "DESKTOP-8V9B2", "Apple Watch", "Bose QC35"
]

# ── helpers ────────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.005):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def banner():
    clear()
    slow_print(color("""
██████╗ ███████╗███████╗██╗    ██╗ █████╗ ███╗   ██╗█████╗ 
██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗████╗  ██║██╔══██╗
██║  ██║█████╗  █████╗  ██║ █╗ ██║███████║██╔██╗ ██║███████║
██║  ██║██╔══╝  ██╔══╝  ██║███╗██║██╔══██║██║╚██╗██║██╔══██║
██████╔╝███████╗███████╗╚███╔███╔╝██║  ██║██║ ╚████║██║  ██║
╚═════╝ ╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    D E E W A N A   S T A R  🏆  REAL-SCAN EDITION
    """, "96"))

def generate_mac():
    """Generates a realistic looking MAC address."""
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )

# ── Safe Local Scanning (NO DATA SHARING) ──────────────────

def get_real_wifi_ssids():
    """
    Locally queries the OS for real Wi-Fi names. 
    100% offline. No data leaves the machine.
    """
    ssids = set()
    sys_os = platform.system()
    
    try:
        if sys_os == "Windows":
            result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0)
            for line in result.stdout.split('\n'):
                if "SSID" in line and ":" in line and "BSSID" not in line:
                    ssid = line.split(":")[1].strip()
                    if ssid: ssids.add(ssid)
                    
        elif sys_os == "Darwin": # macOS
            result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"], capture_output=True, text=True)
            for line in result.stdout.split('\n')[1:]:
                if len(line) > 0:
                    ssid = line[:32].strip()
                    if ssid: ssids.add(ssid)
                    
        elif sys_os == "Linux":
            result = subprocess.run(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                ssid = line.strip()
                if ssid: ssids.add(ssid)
    except Exception:
        pass # If command fails (e.g., no Wi-Fi card), fail silently

    return list(ssids) if ssids else FALLBACK_WIFI

# ── custom-name wizard ─────────────────────────────────────

def ask_custom_names(device_type):
    print()
    ans = input(color(f"  [?] Do you want to inject a DEEWANA {device_type} name? (y/n): ", "93")).strip().lower()

    if ans != 'y':
        return [] 

    name = ""
    while not name:
        name = input(color(f"  [+] Enter the fake {device_type} name to inject: ", "92")).strip()
        if not name:
            print(color("  [!] Name cannot be empty, try again.", "91"))

    while True:
        try:
            count = int(input(color("  [+] How many times should it flood the scan? (5 – 20): ", "92")).strip())
            if 5 <= count <= 20:
                break
            print(color("  [!] Please enter a number between 5 and 20.", "91"))
        except ValueError:
            print(color("  [!] Numbers only, please.", "91"))

    print(color(f"\n  ✅ Injecting '{name}' {count} times into real scan data...\n", "92"))
    time.sleep(0.8)
    return [name] * count

# ── scanners ───────────────────────────────────────────────

def fake_wifi_scanner(deewana_names):
    real_ssids = get_real_wifi_ssids()
    
    # Combine real nearby networks with your fake names
    pool = real_ssids + deewana_names
    random.shuffle(pool)

    clear()
    print(color("  [Terminal mode: airodump-ng emulation]", "90"))
    print(color("  CH 11 ][ Elapsed: 4 s ][ 100% Offline Privacy Mode\n", "97"))
    print(color("  BSSID              PWR  CH   ENC CIPHER AUTH ESSID", "97"))
    print(color("  " + "-"*56, "90"))
    
    time.sleep(1.4)

    for name in pool:
        time.sleep(random.uniform(0.05, 0.25))
        mac = generate_mac().upper()
        pwr = str(random.randint(-89, -30))
        ch = str(random.randint(1, 14)).ljust(2)
        enc = random.choice(["WPA2", "WPA3", "WEP ", "OPN "])
        ciph = "CCMP" if enc in ["WPA2", "WPA3"] else ("WEP " if enc == "WEP " else "    ")
        auth = "PSK " if enc in ["WPA2", "WPA3"] else "    "
        
        # Color code power levels for realism
        pwr_colored = color(pwr, "92") if int(pwr) > -60 else (color(pwr, "93") if int(pwr) > -75 else color(pwr, "91"))
        
        print(f"  {mac}  {pwr_colored}  {ch}   {enc} {ciph}   {auth} {name}")

    print()
    print(color("=" * 60, "96"))
    print(color(f"  [+] Scan complete. {len(pool)} networks mapped locally.", "96"))
    print(color("=" * 60, "96"))

def fake_bt_scanner(deewana_names):
    pool = random.sample(FUNNY_BT_NAMES, 6) + deewana_names
    random.shuffle(pool)

    clear()
    print(color("  [Terminal mode: hcitool / bluetoothctl emulation]", "90"))
    print(color("  Scanning for local Bluetooth LE devices...\n", "97"))
    print(color("  MAC Address         RSSI   Status        Device Name", "97"))
    print(color("  " + "-"*58, "90"))
    time.sleep(1.4)

    for name in pool:
        time.sleep(random.uniform(0.1, 0.35))
        mac = generate_mac().upper()
        rssi = str(random.randint(-95, -40))
        status = random.choice(["[Paired]  ", "[Visible] "])
        
        rssi_colored = color(rssi, "92") if int(rssi) > -65 else (color(rssi, "93") if int(rssi) > -80 else color(rssi, "91"))
        
        print(f"  {mac}   {rssi_colored}   {status}    {name}")

    print()
    print(color("=" * 60, "94"))
    print(color(f"  [+] Scan complete. {len(pool)} devices found.", "94"))
    print(color("=" * 60, "94"))

# ── main ───────────────────────────────────────────────────

def main():
    banner()
    print(color("  Welcome, Deewana Star! Choose your weapon:\n", "93"))
    print(f"  {color('[1]', '92')} 📡  Ultra-Realistic Wi-Fi Scanner")
    print(f"  {color('[2]', '94')} 🔵  Ultra-Realistic Bluetooth Scanner")
    print(f"  {color('[0]', '91')} ❌  Exit\n")

    choice = input(color("  Enter your choice (0 / 1 / 2): ", "97")).strip()

    if choice == "1":
        deewana_names = ask_custom_names("WiFi")
        fake_wifi_scanner(deewana_names)

    elif choice == "2":
        deewana_names = ask_custom_names("Bluetooth")
        fake_bt_scanner(deewana_names)

    elif choice == "0":
        print(color("\n  Exiting Deewana Star Pro… Stay crazy! 🏆\n", "91"))
        sys.exit()

    else:
        print(color("\n  [!] Invalid choice. Restarting…\n", "91"))
        time.sleep(1.2)
        main()
        return

    print(color("\n  [+] Deewana mode complete! Did they believe it? 😂\n", "96"))
    input("  Press Enter to run again or Ctrl+C to quit…\n")
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color("\n\n  [!] Deewana Star signing off! 🏆\n", "93"))
