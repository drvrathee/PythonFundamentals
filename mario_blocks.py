def main():
    n = int(input("Enter the size of the square: "))
    small_square(n)

def small_square(size):
    # outer loop for rows 
    for i in range(size):
        # inner loop for columns
        for j in range(size):
            #printing bricks to form a square
            print("#", end="")

        print()  # this will print a new line after each row of the square

main()