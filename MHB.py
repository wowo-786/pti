import os
import sys

try:
    # Aapki compiled binary file ko import kar raha hai
    import MHB
except ImportError:
    print("\033[1;31m[!] Error: MHB.so file nahi mili ya compile nahi hui!")
    print("\033[1;37m[*] Pehle 'python setup.py build_ext --inplace' chalayein.")
    sys.exit()

def main():
    try:
        # MHB.pyx ke andar jo main function (old1) tha, use call kar raha hai
        MHB.old1()
    except Exception as e:
        print(f"\n\033[1;31m[!] Tool Crash: {e}")
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Allah Hafiz...")

if __name__ == "__main__":
    main()
