import os, sys, platform

def check_architecture():
    # Device ki architecture check ho rahi hai
    arch = platform.architecture()[0] # 64bit or 32bit
    machine = platform.machine()      # aarch64 means 64-bit
    
    if "64" in arch or "aarch64" in machine:
        # Agar 64-bit hai to tool start karega
        print("\033[1;32m [✔] 64-Bit Device Detected. Starting Tool...")
        try:
            # Yahan apni main file ka naam likhein jo aapne encrypt ki hai
            import file # Agar file.so hai to sirf 'file' likhein
        except ImportError as e:
            print(f"\033[1;31m [!] Error loading tool: {e}")
    else:
        # Agar 32-bit hai to error de kar ruk jayega
        print("\n\033[1;31m" + "="*45)
        print("\033[1;37m [✘] SORRY! YOUR DEVICE NOT SUPPORTED")
        print("\033[1;31m" + "="*45)
        print("\033[1;33m [!] This tool is only for 64-Bit devices.")
        print("\033[1;37m [!] Your Device Architecture: \033[1;31m" + machine)
        print("\033[1;31m" + "="*45)
        sys.exit()

if __name__ == "__main__":
    check_architecture()
