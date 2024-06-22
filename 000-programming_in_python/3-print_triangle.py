def print_right_triangle(height):
    # Iterate from 1 to height (inclusive)
    for i in range(1, height + 1):
        # Print i asterisks for the current row
        print('*' * i)

        print_right_triangle(5)