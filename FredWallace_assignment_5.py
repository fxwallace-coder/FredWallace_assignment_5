current_number = int(input("Enter starting number: "))
step_count = 0
print(f"Starting number: {current_number}")
while current_number !=1:
    if current_number%2 == 0:
        current_number /=2
        step_count += 1
        print(f"{current_number:.0f}",end=" ")
    else:
        current_number= (current_number*3)+1
        step_count += 1
        print(f"{current_number:.0f}",end=" ")
print()
print(f"steps: {step_count}")
