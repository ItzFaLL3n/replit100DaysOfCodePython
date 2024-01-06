import os, time, random

def info():
  name = input("Name Your Legend: ")
  char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return name, char_type

def health():
  health = random.randint(1,6) * random.randint(1,12) / 2 + 10
  return health

def strength():
  strength = random.randint(1,6) * random.randint(1,12) / 2 + 12
  return strength

def output():
  name, char_type = info()
  health_val = health()
  strength_val = strength()
  print("\n",name,"\n",char_type,"\n", "HEALTH:", health_val, "\n", "STRENGTH:", strength_val)
  return name, char_type, health_val, strength_val

while True:
  print("Character Builder")
  output()
  print()
  print("May your name go down in Legend...")
  time.sleep(1)
  again = input("Play Again?: ")
  if again == "no" or again == "No" or again == "n":
    break
  else:
    os.system("clear")