print("List Generator")
print()

start_value = int(input("Enter the starting value: "))
end_value = int(input("Enter the ending value: "))
increment_value = int(input("Enter the increment value: "))

for i in range(start_value, end_value, increment_value):
  print("\033[32m",i)