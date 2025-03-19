import os
import time

def fake_virus():
    messages = [
        "WARNING: System files are being deleted...",
        "CRITICAL ERROR: Your hard drive will be formatted!",
        "Contact technical support immediately!",
        "Virus detected! Removing all data...",
        "STARTING SHUTDOWN, AND FORMAT"
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(2)  # Delay for effect
    
    for i in range(10, 0, -1):
        print(f"Shutting down in {i} seconds...")
        time.sleep(1)
    
    print("Just kidding! Your system is safe :)")
    
    # Uncomment this line to actually shut down the system (DANGEROUS)
    # os.system("shutdown /s /t 1")  # Windows shutdown
    # os.system("sudo shutdown -h now")  # Linux shutdown

# Run the prank virus
fake_virus()
