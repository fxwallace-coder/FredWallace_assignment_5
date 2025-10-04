#1st Challenge
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

#2nd Challenge
print("=== Challenge 2: Prime Number Checker ===")
num_input=int(input("Enter a number:"))
print(f" Testing divisors from 2 to {num_input-1}...")
for i in range(2,num_input-1):
    if num_input%i==0:
        print(f"{num_input} is not prime (divisible by {i})")
        break
else:
    print(f"{num_input} is prime!")    
print()
