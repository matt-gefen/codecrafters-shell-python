import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    exit = False
    while exit == False:
        sys.stdout.write("$ ")
        cli_input = input()
        command = cli_input.split(" ")[0]
        argument = False
        if len(cli_input.split(" ")) > 1:
            argument = cli_input.split(" ", 1)[1]

        if command == "exit":
            exit = True
        elif command == "echo":
            if argument != False:
                print(argument)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
