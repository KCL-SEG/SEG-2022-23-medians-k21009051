"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if len(numbers) == 0:
    print('Error - empty list')
    median = None

elif len(numbers) % 2 == 0:
    lower_value = numbers[(len(numbers)//2)-1]
    upper_value = numbers[len(numbers)//2]
    
    median = (lower_value + upper_value) / 2

elif len(numbers) % 2 == 1:
    median = numbers[len(numbers)//2]

print(median)
