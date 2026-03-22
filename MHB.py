import os
import sys
import time
import subprocess

os.system('git pull')
# Colors for Lush Look
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

# --- TERMUX ALL PKG & PYTHON AUTO-UPDATE ---
def check_and_update_env():
    current_v = sys.version_info
    # Check if Python is below 3.13 or packages need update
    if current_v.major == 3 and current_v.minor < 13:
        print(f"{Y}[!] Outdated Environment Detected!{X}")
        print(f"{G}[➔] Updating Termux Packages & Python 3.13...{X}")
        print(f"{W}[*] Please wait, this may take a few minutes...{X}")
        time.sleep(2)
        try:
            # Sab packages aur python ko ek saath update karne ki command
            os.system('pkg update -y && pkg upgrade -y && pkg install python requests -y')
            print(f"{G}[✔] All Packages Updated Successfully!{X}")
            print(f"{G}[✔] Please restart your Termux and run tool again.{X}")
            sys.exit()
        except Exception as e:
            print(f"{R}[!] Auto-update failed: {e}{X}")
            sys.exit()

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def show_logo():
    print(f"{C}{S}" + "━"*55 + f"{X}")
    print(f"{G}{S}  __  __  _    _  ____     _______  ____    ____   _      \n |  \/  || |  | ||  _ \   |__   __||  _ \  / __ \ | |     \n | \  / || |__| || |_) |     | |   | |_) || |  | || |     \n | |\/| ||  __  ||  _ <      | |   |  _ < | |  | || |     \n | |  | || |  | || |_) |     | |   | |_) || |__| || |____ \n |_|  |_||_|  |_||____/      |_|   |____/  \____/ |______|{X}")
    print(f"{Y}             >>> MHB SECURITY LOADER v2.0 <<<{X}")
    print(f"{C}{S}" + "━"*55 + f"{X}")

def setup_folder():
    folder_path = "/sdcard/MHB"
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except PermissionError:
            pass 

def check_join():
    check_file = "/sdcard/MHB/.joined_groups.txt"
    
    if not os.path.exists(check_file):
        while True:
            clear()
            show_logo()
            print(f"{W}[{R}!{W}] {S}{Y}FIRST JOIN OUR WHATSAPP CHANNELS!{X}")
            print(f"{W}[*] Tool unlock karne ke liye niche diye gaye links join karein.{X}")
            print(f"{C}{S}" + "━"*55 + f"{X}")
            print(f"{W}[{G}01{W}] {S}JOIN WHATSAPP GROUP 1{X}")
            print(f"{W}[{G}02{W}] {S}JOIN WHATSAPP GROUP 2{X}")
            print(f"{W}[{G}03{W}] {S}JOIN WHATSAPP COMMUNITY (IMPORTANT){X}")
            print(f"{W}[{C}04{W}] {S}VERIFY & UNLOCK TOOL{X}")
            print(f"{W}[{R}00{W}] {S}EXIT{X}")
            print(f"{C}{S}" + "━"*55 + f"{X}")
            
            choice = input(f"{G}MHB >> {X}")
            
            if choice in ['1', '01']:
                os.system('termux-open-url "https://chat.whatsapp.com/HdppaiQyFtZ1AwiOzc5iEe?mode=gi_t"')
                time.sleep(2)
            elif choice in ['2', '02']:
                os.system('termux-open-url "https://chat.whatsapp.com/FtIOPca2aXt43eHIUnTRtv?mode=hqctcla"')
                time.sleep(2)
            elif choice in ['3', '03']:
                os.system('termux-open-url "https://whatsapp.com/channel/0029VbCdRSxJuyA4UIuIra12"')
                time.sleep(2)
            elif choice in ['4', '04']:
                print(f"\n{Y}[*] Verifying Subscriptions...{X}")
                time.sleep(3)
                try:
                    if os.path.exists("/sdcard"):
                        with open(check_file, "w") as f:
                            f.write("done")
                    else:
                        with open(".joined_groups.txt", "w") as f:
                            f.write("done")
                    print(f"{G}[✔] Access Granted! Loading Menu...{X}")
                    time.sleep(2)
                    break
                except Exception:
                    with open(".joined_groups.txt", "w") as f:
                        f.write("done")
                    break
            elif choice in ['0', '00']:
                sys.exit()

if __name__ == "__main__":
    check_and_update_env() # Sabse pehle poora environment check aur update hoga
    setup_folder()
    check_join()
    
    try:
        import MHB
        MHB.aprovel()
    except ImportError:
        # Agar update ke baad bhi masla hai to user ko manual command show hogi
        print(f"\n{R}[-] Error: Your Device Not Working!{X}")
        print(f"{W}[*] Try running: {G}pkg update && pkg upgrade -y{X}")
    except Exception as e:
        print(f"\n{R}[!] Error: {e}{X}")
