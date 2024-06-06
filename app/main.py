import sys
import os

def main():
    while True:
        # Print the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        command = input().strip()

        # Handle empty command (just reprint the prompt)
        if not command:
            continue

        # Try to execute the command
        try:
            # Split the command and its arguments
            parts = command.split()
            cmd = parts[0]
            args = parts[1:]

            # Use os.execvp to execute the command
            os.execvp(cmd, parts)
        except FileNotFoundError:
            # If the command is not found, print the error message
            sys.stdout.write(f"{cmd}: command not found\n")
            sys.stdout.flush()
        except Exception as e:
            # Print any other exception that might occur (optional)
            sys.stdout.write(f"Error: {e}\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()


