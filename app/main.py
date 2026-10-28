import sys


class Builtins:
    def __init__(self):
        self.builtins = {"echo": self.echo, "type": self.type, "exit": self.exit}

    def echo(self, argument: str):
        print(argument)

    def type(self, argument: str):
        if argument in self.builtins:
            print(f"{argument} is a shell builtin")
        else:
            print(f"{argument}: not found")

    def exit(self):
        sys.exit()


builtins = Builtins()


def main():
    while True:
        sys.stdout.write("$ ")
        cli_input = input()
        cli_input_split = cli_input.split(" ", 1)
        command = cli_input_split[0]
        argument = cli_input_split[1] if len(cli_input_split) > 1 else ""
        if command in builtins.builtins:
            if command == "exit":
                builtins.builtins[command]()
            else:
                builtins.builtins[command](argument)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
