import os, sys, time, platform, subprocess, hashlib

# --- COLORS ---
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'; W = '\033[1;37m'; C = '\033[1;36m'

# --- ANTI-EDIT HASH ---
# Jab aap script final kar lein, toh iska hash yahan daal dein (Optional but strong)
# Is waqt ye sirf basic check karega
def check_integrity():
    try:
        # Check if someone added 'print' or 'edit' statements
        if os.path.getsize(__file__) > 10000: # Agar file size limit se barh jaye
            print(f"{R} [!] Modification Detected!{W}")
            sys.exit()
    except: pass

def get_arch():
    """Device architecture check karne ke liye"""
    arch = platform.machine()
    if 'aarch64' in arch:
        return f"{G}64-Bit (aarch64){W}"
    elif 'arm' in arch or 'v7l' in arch:
        return f"{Y}32-Bit (armv7l){W}"
    else:
        return f"{C}{arch}{W}"

def setup_termux():
    print(f"{C} [*] Checking Device Environment...{W}")
    # Architecture Info Print karein
    print(f"{W} [>] Your Device Architecture: {get_arch()}")
    time.sleep(1)

    # Zaroori commands for Termux
    try:
        import requests
    except ImportError:
        print(f"{Y} [!] Installing Missing Modules...{W}")
        os.system('pip install requests futures bs4 rich')

def auto_update():
    print(f"{G} [*] Checking for Updates...{W}")
    if os.path.exists('.git'):
        try:
            update = subprocess.check_output('git pull', shell=True).decode()
            if 'Already up to date' in update:
                print(f"{G} [√] Script is already latest version.{W}")
            else:
                print(f"{Y} [!] Update applied! Restarting...{W}")
                os.system('python run.py')
                sys.exit()
        except:
            print(f"{R} [!] Git update failed.{W}")
    else:
        print(f"{Y} [!] Git not found, skipping update check.{W}")

def load_binary():
    # Aapki binary file ka naam
    so_file = "MHB.cpython-312.so"
    
    if not os.path.isfile(so_file):
        print(f"\n{R} [!] Error: {so_file} not found!{W}")
        print(f"{Y} [!] Make sure the binary file is in the same folder.{W}")
        sys.exit()

    try:
        print(f"{G} [*] Loading Encrypted Module...{W}")
        time.sleep(1)
        import MHB
        MHB.approval() # Aapki binary ka main function
    except Exception as e:
        print(f"{R} [!] Error loading binary: {e}{W}")
        print(f"{Y} [~] Tip: Ensure you are using Python 3.12{W}")

if __name__ == "__main__":
    os.system('clear')
    print(f"{C}--------------------------------------")
    print(f"{W}       MHB PREMIUM LOADER V16         ")
    print(f"{C}--------------------------------------{W}")
    
    check_integrity()
    setup_termux()
    auto_update()
    load_binary()
