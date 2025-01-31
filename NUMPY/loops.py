#condition statemants
print("Conditional statement : ")
x=10
if x>0:
    print(",{x} is positive ")
elif x==0:
    print(f"{x} is zero.")
else:
    print(f"{x} is negative.")

print("\nLoops: ")

# LOOPS
for i in range(5):
    print(f"Iterartion {i}")

#while LOOP
print("\nwhile loop example: ")
count =0
while count <10:
    print("count is ",count)
    count+=1


#BREAK statement
print("Break example: ")
for i in range(5):
    if i==3:
        print("Breaking the loop at i=3: ")
        break
    print(i)

#continue Statement
print("Continue example: ")
for i in range(5):
    if i==2:
        print("Skipping iteration for i=2")
        continue
    print(i)



# Loop with pass statement
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(f"Processing number {i}")



# Nested loop with match/case
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        match (i, j):  # Matching tuple of (i, j)
            case (0, 0):
                print(f"Special case: i={i}, j={j}")
            case (1, 1):
                print(f"Another special case: i={i}, j={j}")
            case _:
                print(f"Normal case: i={i}, j={j}")


# Loop with match/case
for x in [1, 2, 3, 4, 5]:
    match x:
        case 1:
            print(f"{x} is One")
        case 2:
            print(f"{x} is Two")
        case 3:
            print(f"{x} is Three")
        case _:
            print(f"{x} is another number")


#else with loops 
for i in range(5):
        print(i)
else:
    print("Loop completed without break.")