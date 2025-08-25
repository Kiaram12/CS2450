import random

print("Hi! I am going to try to guess your age. You think it is impossible for me. Let's see.")
name = input("What is your name? ")

younger = 15
older = 30

while True:
    if younger > older:
        print("Wait... something doesn't make sense. Did you give me the right hints?")
        break

    age = random.randint(younger, older)
    answer = input(f"Are you {age} years old? (y/n): ").strip().lower()

    if answer == 'y':
        print(f"{name} is {age} years old! I knew it.")
        break
    else:
        print("Rats.")
        hint = input("Are you older or younger than that? (older/younger): ").strip().lower()

        if hint == 'older':
            younger = age + 1
        elif hint == 'younger':
            older = age - 1
        else:
            print("Please say 'older' or 'younger'.")
    


