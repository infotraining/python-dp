import cmd


class MyCommandLoop(cmd.Cmd):

    def do_add(self, line):
        args = line.split()

        if len(args) != 2:
            print("*** invalid number of args")
            return

        try:
            numbers = [int(i) for i in args]
        except ValueError:
            print("*** arguments should be numbers")

        print(sum(numbers))

    def help_add(self):
        print('add two integral numbers')

    def do_exit(self, _):
        return True

    def help_exit(self):
        print("Exit the interpreter.")
        print("You can also use the Ctrl-D shortcut.")

    do_EOF = quit
    help_EOF = help_exit

    def onecmd(self, line):
        r = super().onecmd(line)
        if r and input('Exit anyway ? (yes/no): ') == 'yes':
             return True
        return False

    def default(self, line):
        print("Default echo:", line)

    def preloop(self):
        print('Hello')
        super().preloop()

    def postloop(self):
        print('Goodbye')
        super().postloop()

    def emptyline(self):
        print('Empty line is not allowed')
        return True

def main():
    interpreter = MyCommandLoop()    
    interpreter.cmdloop()

if __name__ == '__main__':
    main()


