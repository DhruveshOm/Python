# num= int (input("Enter numbers: "))
# sum=0
# for i in range(num):
#     a=int(input())
#     sum+=a
# avg= sum/num
# print()

# Input the numbers as a space-separated string
input_str = input("Enter numbers separated by spaces: ")

# Split the input string by spaces and convert it to a list of integers
numbers = list(map(int, input_str.split()))

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the average, formatted to 1 decimal place
print(f"The average is: {average:.1f}")
