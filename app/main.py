import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input()

        if user_input.startswith("exit"):
            try:
                exit_code = int(user_input.split()[1])
            except (IndexError, ValueError):
                exit_code = 0
            sys.exit(exit_code)
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()


