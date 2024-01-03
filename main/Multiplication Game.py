print("Multiplication Game")
print()
print()


user_choice = int(input("Enter your Multlipy : "))
print()

attempts = 0

for i in range(1,11):
    correct_fact = i*user_choice
    print(user_choice, "x", i)
    user_input = int(input("Answer > "))
    if user_input == correct_fact:
        print("You Got it Right")
        attempts +=1
    else:
        print("You Got it Wrong,", "it's", correct_fact)

if user_input == 10:
    print("Perfecto.... You Got All 10 Right")
else:
    print("You Got", attempts, "Rightm, Way to Go!")
