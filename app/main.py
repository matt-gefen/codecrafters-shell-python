import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    exit = False
    while exit == False:
        sys.stdout.write("$ ")
        command  = input()
        if command == "exit": 
            exit = True
        else:
            print(f"{command}: command not found")
        

if __name__ == "__main__":
    main()
