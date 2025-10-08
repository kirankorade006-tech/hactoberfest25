import pyautogui
import time

print("Mouse mover started. Press Ctrl+C to stop.")

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # Move slightly (e.g., 10 pixels right and down)
        pyautogui.moveTo(x + 10, y + 10, duration=0.2)
        pyautogui.moveTo(x, y, duration=0.2)
        
        # Wait 30 seconds
        time.sleep(30)

except KeyboardInterrupt:
    print("\nMouse mover stopped.")
