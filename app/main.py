import sys
import shutil

def main():
    builtins = {"echo", "exit", "type"}

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
        elif user_input.startswith("type "):
            command = user_input.split()[1]
            if command in builtins:
                print(f"{command} is a shell builtin")
            else:
                # Check if the command is an external command in PATH
                path = shutil.which(command)
                if path:
                    print(f"{command} is {path}")
                else:
                    print(f"{command} not found")
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()

