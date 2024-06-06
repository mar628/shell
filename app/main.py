import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().strip()

        if user_input.startswith("exit"):
            try:
                exit_code = int(user_input.split()[1])
            except (IndexError, ValueError):
                exit_code = 0
            sys.exit(exit_code)
        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input == "type echo":
            print("echo is a shell builtin")
        elif user_input == "type exit":
            print("exit is a shell builtin")
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()
