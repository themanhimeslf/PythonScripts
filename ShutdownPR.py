#Shutdown OS protocol.py
import os
import time


print("Starting shutdown sequence")
time.sleep(3)
for i in range(10, 0, -1):
    print(f"Shutting down in {i} seconds...")
    time.sleep(1)

print("Just kidding! Your system is safe :)")
time.sleep(2)
print("Hehe")
time.sleep(1)
    # Uncomment this line to actually shut down the system (DANGEROUS)
    # os.system("shutdown /s /t 1")  # Windows shutdown
    # os.system("sudo shutdown -h now")  # Linux shutdown

