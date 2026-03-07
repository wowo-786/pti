import os, sys, time, platform, subprocess

# --- COLORS ---
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'; W = '\033[1;37m'; C = '\033[1;36m'

def clear():
    os.system('clear')

def update_python():
    """Python version check aur upgrade logic"""
    curr_v = sys.version_info.minor
    if curr_v < 13:
        print(f"{Y} [!] Current Python: 3.{curr_v} | Required: 3.13{W}")
        print(f"{G} [*] Updating Python environment for MHB binary...{W}")
        os.system('pkg update -y && pkg install python -y')
        print(f"{G} [√] Update Done! Please run 'python run.py' again.{W}")
        sys.exit()

def setup_env():
    print(f"{C} [*] Setting up dependencies...{W}")
    try:
        import requests
    except ImportError:
        os.system('pip install requests futures bs4 rich')

def check_file():
    # Aapki screenshot ke mutabiq binary file name
    binary = "MHB.cpython-313.so"
    if not os.path.isfile(binary):
        print(f"{R} [!] Error: {binary} not found in folder!{W}")
        print(f"{Y} [>] Downloading or checking files...{W}")
        # Agar file missing ho toh yahan git pull command auto chal sakti hai
        os.system('git pull')
        if not os.path.isfile(binary):
            sys.exit(f"{R} [!!] Critical Error: Binary missing.{W}")

def main_loader():
    clear()
    print(f"{C}--------------------------------------")
    print(f"{W}        MHB PREMIUM LOADER V17         ")
    print(f"{C}--------------------------------------{W}")
    
    update_python()
    setup_env()
    check_file()
    
    try:
        print(f"{G} [*] Loading Encrypted Module...{W}")
        time.sleep(2)
        import MHB
        MHB.approval() # .so file ke andar ka function
    except Exception as e:
        print(f"{R} [!] Error: {e}{W}")
        print(f"{Y} [Tip] Make sure you are using 64-bit Termux.{W}")

if __name__ == "__main__":
    main_loader()
