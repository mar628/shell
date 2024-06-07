import sys
import os
import shutil
import subprocess

def main():
    builtins = {"echo", "exit", "type", "cd"}

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        user_input = input().strip()
        if not user_input:
            continue
        
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            try:
                exit_code = int(args[0]) if args else 0
            except ValueError:
                exit_code = 0
            sys.exit(exit_code)
        elif command == "echo":
            print(" ".join(args))
        elif command == "type":
            if args:
                cmd = args[0]
                if cmd in builtins:
                    print(f"{cmd} is a shell builtin")
                else:
                    path = shutil.which(cmd)
                    if path:
                        print(f"{cmd} is {path}")
                    else:
                        print(f"{cmd} not found")
            else:
                print("type: missing argument")
        elif command == "cd":
            if args:
                try:
                    os.chdir(args[0])
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {args[0]}")
                except NotADirectoryError:
                    print(f"cd: not a directory: {args[0]}")
                except PermissionError:
                    print(f"cd: permission denied: {args[0]}")
            else:
                print("cd: missing argument")
        else:
            # Try to run the command as an external program
            path = shutil.which(command)
            if path:
                try:
                    result = subprocess.run([command] + args, capture_output=True, text=True)
                    print(result.stdout, end='')
                except Exception as e:
                    print(f"Error executing command: {e}")
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
