size = int(input("Enter the size of the pattern:"))
row = 0

while size > row:
    for each in range(0, size):
        print("*", end="")
    print("")
    row += 1