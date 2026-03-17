import sys
import time

def deleted_notice():
    print("\n" + "!" * 45)
    print("      ⚠️  IMPORTANT ANNOUNCEMENT  ⚠️")
    print("!" * 45)
    
    # Aapka bataya hua message
    print("\n[ STATUS ] : COMMND DELETED")
    print("[ MSG ]    : Random Update Clossed dont Try again.")
    
    print("\n" + "-" * 45)
    print("Yahan naya script ya binary replace karein.")
    print("!" * 45 + "\n")
    
    # 3 second baad automatic exit
    time.sleep(3)
    sys.exit()

if __name__ == "__main__":
    deleted_notice()
