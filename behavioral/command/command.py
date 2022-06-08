import abc
import os
import copy

history = []


class Command(abc.ABC):
    """Command interface"""

    @abc.abstractmethod
    def execute(self):
        """Method to execute the command"""
        pass


class UndoableCommand(Command):
    def __init__(self, history):
        self.history = history

    @abc.abstractmethod
    def undo(self):
        """Method to undo the command"""
        pass

    def clone(self):
        return copy.copy(self)


class LsCommand(Command):
    """Concrete command that emulates ls unix command behavior"""

    def __init__(self, path):
        self.path = path

    def execute(self):
        filenames = []

        for filename in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, filename)):
                filenames.append(filename)

        print('Content of dir:', ' '.join(filenames))


class TouchCommand(UndoableCommand):
    """Concrete command that emulates touch unix command behavior"""

    def __init__(self, history, filename):
        super().__init__(history)
        self.filename = filename

    def execute(self):
        self.history.append(self.clone())

        """Actual implementation of unix touch command."""
        with open(self.filename, 'a'):
            os.utime(self.filename, None)

    def undo(self):
        """Undo unix touch command. Here we simply delete the file."""
        os.remove(self.filename)


class RmCommand(UndoableCommand):
    """Concrete command that emulates rm unix command behavior"""

    def __init__(self, history, filename):
        super().__init__(history)
        self.filename = filename
        self.backup_name = ''

    def execute(self):
        self.backup_name = '~' + self.filename
        self.history.append(self.clone())

        """Deletes file with creating backup to restore it in undo method."""
        os.rename(self.filename, self.backup_name)

    def undo(self):
        os.rename(self.backup_name, self.filename)


class Button:
    """Invoker class"""

    def __init__(self, name, command):
        self.name = name
        self.__text = ''
        self.command = command

    def on_click(self):
        self.command.execute()


class KeyboardShortcut:
    """Invoker class"""

    def __init__(self, command):
        self.command = command

    def keypress(self):
        self.command.execute()


def main():
    ls_command = LsCommand('.')
    touch_command = TouchCommand(history, 'test_file.txt')
    rm_command = RmCommand(history, 'test_file.txt')

    btn_ls = Button("ls", ls_command)
    shrtcut_touch = KeyboardShortcut(touch_command)
    btn_rm = Button("rename", rm_command)   

    # executing commands
    btn_ls.on_click()
    shrtcut_touch.keypress()
    btn_ls.on_click()
    btn_rm.on_click()
    btn_ls.on_click()

    print("Undo " + '*' * 40)

    # undo commands

    for cmd in reversed(history):
        cmd.undo()

    btn_ls.on_click()


if __name__ == '__main__':
    main()