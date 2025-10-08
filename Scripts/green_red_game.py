import random
import time

print("=== GREEN RED GAME ===")
print("Rules:")
print("- Wait for 'GREEN' to appear, then press Enter as fast as you can.")
print("- If you press Enter during 'RED', you lose!\n")

while True:
    # Random delay before showing color
    time.sleep(random.uniform(2, 5))

    color = random.choice(["RED", "GREEN"])
    print(color)

    if color == "RED":
        # Player must NOT press Enter
        try:
            start = time.time()
            input_timeout = 2  # seconds
            print("...Don't press anything for 2 seconds!")
            time.sleep(input_timeout)
        except KeyboardInterrupt:
            print("\nYou pressed something during RED! ❌ You lose!")
            break
    else:
        # Player must press Enter fast
        start = time.time()
        input("Press Enter NOW!")
        reaction_time = time.time() - start
        print(f"✅ Good job! Reaction time: {reaction_time:.3f} sec")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Goodbye!")
        break
