#STILL WORKING ON IT NEEDS TO BE REDONE
import time


def main():
    pet = input("What's your pet's name? ").strip() or "Buddy"
    print(f"Alright, {pet} is set up. Type 'quit' anytime to get out.")
    print()

    state = "Idle"

    while True:
        if state == "Idle":
            print(f"[{pet}] Just relaxing.")
            action = input("What are we doing? (play / feed / sleep / quit): ").strip().lower()
            print()

            if action == "play":
                print(f"{pet} got excited.")
                state = "Playing"
            elif action == "feed":
                print(f"Getting some food for {pet}...")
                state = "Eating"
            elif action == "sleep":
                print(f"Heading over to the bed with {pet}.")
                state = "Sleeping"
            elif action == "quit":
                break
            else:
                print("That's not one of the choices, try again.")

        elif state == "Playing":
            print(f"[{pet}] Running around having a good time.")
            action = input("What's next? (stop / feed / quit): ").strip().lower()
            print()

            if action == "stop":
                print(f"{pet} settled back down.")
                state = "Idle"
            elif action == "feed":
                print(f"{pet} saw the food and stopped running immediately.")
                state = "Eating"
            elif action == "quit":
                break
            else:
                print("Pick a valid option.")

        elif state == "Eating":
            print(f"[{pet}] Eating up.")
            action = input("What's next? (done / sleep / quit): ").strip().lower()
            print()

            if action == "done":
                print(f"{pet} finished every last bite.")
                state = "Idle"
            elif action == "sleep":
                print(f"Full stomach got {pet} ready for a nap.")
                state = "Sleeping"
            elif action == "quit":
                break
            else:
                print("Not a valid input.")

        elif state == "Sleeping":
            print(f"[{pet}] Fast asleep.")
            action = input("What's next? (wake / dream / quit): ").strip().lower()
            print()

            if action == "wake":
                print(f"Woke {pet} up gently.")
                state = "Idle"
            elif action == "dream":
                print(f"{pet} is out cold, dreaming about chasing something.")
                state = "Playing"
            elif action == "quit":
                break
            else:
                print("Invalid command.")

        time.sleep(0.5)

    print(f"Alright, peace out. Take care of {pet}.")


if __name__ == "__main__":
    main()