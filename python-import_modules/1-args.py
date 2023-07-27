import sys

def print_arguments():
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}")

    # If no arguments were passed, print '.' and a new line
    if num_args == 0:
        print(".")
    else:
        # Print each argument with its position
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

# Check if the script is being run directly
if __name__ == "__main__":
    print_arguments()