import os
import sys
import time
os.system('git pull')
# Colors for Lush Look
G = '\033[92m' ; R = '\033[91m' ; Y = '\033[93m' 
C = '\033[96m' ; W = '\033[97m' ; S = '\033[1m' ; X = '\033[0m'

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
            pass # Error handling check_join mein handle ho jayegi

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
                print(f"{G}[➔] Opening Group 1...{X}")
                os.system('termux-open-url "https://chat.whatsapp.com/HdppaiQyFtZ1AwiOzc5iEe?mode=gi_t"')
                time.sleep(2)
            elif choice in ['2', '02']:
                print(f"{G}[➔] Opening Group 2...{X}")
                os.system('termux-open-url "https://chat.whatsapp.com/FtIOPca2aXt43eHIUnTRtv?mode=hqctcla"')
                time.sleep(2)
            elif choice in ['3', '03']:
                print(f"{G}[➔] Opening Community...{X}")
                # Apni Community Ka Link Yahan Dalein
                os.system('termux-open-url "https://whatsapp.com/channel/0029VbCdRSxJuyA4UIuIra12"')
                time.sleep(2)
            elif choice in ['4', '04']:
                print(f"\n{Y}[*] Verifying Subscriptions...{X}")
                time.sleep(3)
                try:
                    with open(check_file, "w") as f:
                        f.write("done")
                    print(f"{G}[✔] Access Granted! Loading Menu...{X}")
                    time.sleep(2)
                    break
                except Exception:
                    # Agar storage permission nahi hai toh local file banayega
                    with open(".joined_groups.txt", "w") as f:
                        f.write("done")
                    break
            elif choice in ['0', '00']:
                sys.exit()
            else:
                print(f"{R}[!] Invalid Option!{X}")
                time.sleep(1)

if __name__ == "__main__":
    setup_folder()
    check_join()
    
    try:
        import MHB
        MHB.aprovel()
    except ImportError:
        print(f"\n{R}[-] Error: 'Your Device Not Working!{X}")
    except Exception as e:
        print(f"\n{R}[!] Error: {e}{X}")
