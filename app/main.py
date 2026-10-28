import sys


def echo(argument: str):
    print(argument)


def type(argument: str):
    builtins = ["exit", "echo", "type"]
    if argument in builtins:
        print(f"{argument} is a shell builtin")
    else:
        print(f"{argument}: not found")


def main():
    while True:
        sys.stdout.write("$ ")
        cli_input = input()
        cli_input_split = cli_input.split(" ", 1)
        command = cli_input_split[0]
        argument = cli_input_split[1] if len(cli_input_split) > 1 else ""
        if command == "exit":
            break
        elif command == "echo":
            echo(argument)
        elif command == "type":
            type(argument)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
