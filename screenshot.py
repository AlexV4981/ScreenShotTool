import keyboard
import mss
import time
import os

# Ensure the 'screenshots' directory exists
os.makedirs("screenshots", exist_ok=True)

def take_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        
        # Generate a unique filename based on timestamp
        filename = f"screenshots/screenshot_{int(time.time())}.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
        
        print(f"Saved {filename}")

def exit_program():
    print("Exiting program...")
    os._exit(0)  # Forcefully kills the script

# Register global hotkeys
keyboard.add_hotkey("p", take_screenshot)
keyboard.add_hotkey("l", exit_program)  # Now properly exits

print("Program is running. Press 'p' to take a screenshot, 'l' to exit.")
keyboard.wait()  # Keeps the program running
