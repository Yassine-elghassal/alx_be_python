# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through the rows
while row < size:
    # Use a for loop to print the asterisks for each row
    for col in range(size):
        print("*", end="")  # Print '*' without a newline
    print()  # After printing all stars in a row, print a newline
    row += 1  # Increment the row counter
