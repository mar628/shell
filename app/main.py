import sys

def main():
    # Remove or comment out the debug print statement to avoid interference with test output
    # print("Logs from your program will appear here!")

    # Write the prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input()

if __name__ == "__main__":
    main()

