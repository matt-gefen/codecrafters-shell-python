import os
import sys


class Builtins:
    def __init__(self):
        self.builtins = {"echo": self.echo, "type": self.type, "exit": self.exit}

    def echo(self, args: str):
        print(args)

    def type(self, args: str):
        pathsep = os.pathsep
        path_directories = os.environ["PATH"].split(pathsep)
        output = f"{args}: not found"
        if args in self.builtins:
            output = f"{args} is a shell builtin"
        else:
            for path in path_directories:
                try:
                    path_files = os.listdir(path)
                    for file in path_files:
                        full_path = f"{path}/{file}"
                        if file == args and os.access(full_path, os.X_OK):
                            output = f"{args} is {full_path}"
                except FileNotFoundError:
                    pass
        print(output)

    def exit(self, args: str):
        # ignores params
        sys.exit()


builtins = Builtins()


def main():
    while True:
        sys.stdout.write("$ ")
        cli_input = input()
        cli_input_split = cli_input.split(" ", 1)
        command = cli_input_split[0]
        args = cli_input_split[1] if len(cli_input_split) > 1 else ""
        try:
            builtins.builtins[command](args)
        except KeyError:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
