import time

# Extension Activity: Virtual Pet State Machine

print("*" * 50)
print("Welcome to the Ultimate Virtual Pet Simulator!")
print("*" * 50)

pet_name = input("First, what would you like to name your pet? ").strip()
if not pet_name:
    pet_name = "Buddy"  # Default name if the user leaves it blank

print(f"\nAwesome! {pet_name} is ready to hang out.")
print("Type 'quit' at any prompt to leave the game.")
time.sleep(1)

state = "Idle"

while True:
    if state == "Idle":
        print("\n" + "=" * 40)
        print(f"[STATE: IDLE] {pet_name} is just sitting around, wagging its tail.")
        time.sleep(0.5)
        action = input(f"What do you want to do with {pet_name}? (play / feed / sleep / quit): ").strip().lower()

        if action == "play":
            print(f"You grab a toy. {pet_name} looks excited!")
            time.sleep(1)
            state = "Playing"
        elif action == "feed":
            print("You shake the bag of treats...")
            time.sleep(1)
            state = "Eating"
        elif action == "sleep":
            print(f"You guide {pet_name} to their bed.")
            time.sleep(1)
            state = "Sleeping"
        elif action == "quit":
            print(f"Waving goodbye to {pet_name}. Thanks for playing!")
            break
        else:
            print(f"Invalid action. {pet_name} tilts its head and looks at you confused.")
            time.sleep(1)

    elif state == "Playing":
        print("\n" + "=" * 40)
        print(f"[STATE: PLAYING] {pet_name} is running in circles and having a blast!")
        time.sleep(0.5)
        action = input("What do you want to do now? (stop / feed / quit): ").strip().lower()

        if action == "stop":
            print("You put the toys away. Time to calm down.")
            time.sleep(1)
            state = "Idle"
        elif action == "feed":
            print(f"{pet_name} drops the toy instantly at the sound of food!")
            time.sleep(1)
            state = "Eating"
        elif action == "quit":
            print(f"Waving goodbye to {pet_name}. Thanks for playing!")
            break
        else:
            print(f"Invalid action. {pet_name} ignores you and keeps chasing its tail.")
            time.sleep(1)

    elif state == "Eating":
        print("\n" + "=" * 40)
        print(f"[STATE: EATING] {pet_name} is happily chomping down on some yummy food.")
        time.sleep(0.5)
        action = input("What do you want to do now? (done / sleep / quit): ").strip().lower()

        if action == "done":
            print(f"{pet_name} finishes the bowl and licks its chops.")
            time.sleep(1)
            state = "Idle"
        elif action == "sleep":
            print(f"A full belly makes {pet_name} very sleepy...")
            time.sleep(1)
            state = "Sleeping"
        elif action == "quit":
            print(f"Waving goodbye to {pet_name}. Thanks for playing!")
            break
        else:
            print(f"Invalid action. {pet_name} is too busy chewing to care.")
            time.sleep(1)

    elif state == "Sleeping":
        print("\n" + "=" * 40)
        print(f"[STATE: SLEEPING] {pet_name} is fast asleep. Zzz... Zzz...")
        time.sleep(0.5)
        action = input("What do you want to do now? (wake / dream / quit): ").strip().lower()

        if action == "wake":
            print(f"You gently pet {pet_name}. They wake up and stretch.")
            time.sleep(1)
            state = "Idle"
        elif action == "dream":
            print(f"{pet_name}'s paws are twitching! They are dreaming about playing.")
            time.sleep(1)
            state = "Playing"
        elif action == "quit":
            print(f"Leaving {pet_name} to rest peacefully. Goodbye!")
            break
        else:
            print("Invalid action. Shhh, you didn't trigger a valid state change.")
            time.sleep(1)