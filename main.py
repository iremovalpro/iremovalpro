# Entry point of the mock iRemoval PRO application
# This simulates the workflow described in the README

import time
from device import Device
from license import use_trial, trials_left
from config import APP_NAME, APP_VERSION

def banner():
    print("=" * 50)
    print(f"{APP_NAME} v{APP_VERSION}")
    print("Ultimate iCloud Bypass Tool (Simulation)")
    print("=" * 50)

def main():
    banner()

    device = Device()

    print("[*] Waiting for device connection...")
    time.sleep(1)

    if not device.connect():
        print("[!] No device detected")
        return

    info = device.info()
    print(f"[+] Device connected: {info['model']} (iOS {info['ios']})")

    print(f"[*] Trials remaining: {trials_left()}")

    if not use_trial():
        print("[!] No trials left. Please purchase a license.")
        return

    print("[*] Starting bypass process...")
    time.sleep(2)

    device.activate_signal()

    print("[+] Bypass completed successfully")
    print("[+] GSM/LTE/5G signal: ACTIVE")
    print("[+] iCloud services: ENABLED")
    print("[+] Untethered status: TRUE")

    print("[✓] Device is fully functional")

if __name__ == "__main__":
    main()
