import random 

print("Hi! I am going to try to guess your age.You think it is impossible for me. Let's see.")
name = input("What is your name?")

age = random.randint(15,30) 
answer = input(f"Are you {age} years old? (y/n): ")

while True:
    age = random.randint(15,30)
    answer = input(f"Are you {age} years old? : ")
    if answer == 'y':
        print(f"{name} is {age} years old!. I knew it")
        break
    else:
        print("Rats.")
         


