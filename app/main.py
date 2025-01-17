import sys
import os
import shutil
import subprocess

def main():
    builtins = {"echo", "exit", "type", "cd", "pwd"}

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
                path = args[0]
                if path == "~":
                    path = os.environ.get("HOME", "")
                try:
                    os.chdir(path)
                except FileNotFoundError:
                    print(f"{path}: No such file or directory")
                except NotADirectoryError:
                    print(f"{path}: Not a directory")
                except PermissionError:
                    print(f"{path}: Permission denied")
            else:
                print("cd: missing argument")
        elif command == "pwd":
            print(os.getcwd())
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
