# Coder's Life State Machine

state = "coding"

while True:
    if state == "coding":
        print("\nYou are coding!")
        while True:
            feeling = input("How are you feeling? (tired / hungry): ").strip().lower()
            if feeling == "tired":
                state = "sleeping"
                break
            elif feeling == "hungry":
                state = "eating"
                break
            else:
                print("Invalid input. You are still coding.")

    elif state == "eating":
        print("\nYou are eating!")
        while True:
            feeling = input("How are you feeling? (full): ").strip().lower()
            if feeling == "full":
                state = "coding"
                break
            else:
                print("Invalid input. You are still eating.")

    elif state == "sleeping":
        print("\nYou are sleeping!")
        while True:
            feeling = input("How are you feeling? (awake): ").strip().lower()
            if feeling == "awake":
                state = "coding"
                break
            else:
                print("Invalid input. You are still sleeping.")