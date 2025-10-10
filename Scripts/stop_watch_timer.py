import time
import threading

def display_timer(start_time, running_flag):
    while running_flag[0]:
        elapsed = time.time() - start_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        millis = int((elapsed - int(elapsed)) * 1000)
        print(f"\rElapsed: {mins:02d}:{secs:02d}.{millis:03d}", end="")
        time.sleep(0.1)

def stopwatch():
    print("⏱️ Press Enter to start the stopwatch")
    input()
    start_time = time.time()
    running_flag = [True]

    # Start timer display in a separate thread
    timer_thread = threading.Thread(target=display_timer, args=(start_time, running_flag))
    timer_thread.start()

    print("\nPress Enter to stop the stopwatch")
    input()
    running_flag[0] = False
    timer_thread.join()

    total_time = time.time() - start_time
    mins = int(total_time // 60)
    secs = int(total_time % 60)
    millis = int((total_time - int(total_time)) * 1000)
    print(f"\nFinal Time: {mins:02d}:{secs:02d}.{millis:03d}")

if __name__ == "__main__":
    stopwatch()
