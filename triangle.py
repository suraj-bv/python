rows = int(input("Enter the number of rows for the triangle: "))

for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line
    print()