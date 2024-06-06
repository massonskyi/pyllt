__all__ = ['Command']

class Command(object):
    """
    This is the base class for all commands
    """

    def execute(self):
        """
        This is the method that will be called when the command is executed
        :return: None
        """
        pass


class SimpleCommand(Command):
    """
    This is the base class for all simple commands
    """

    def __init__(self, name, description):
        """
        This is the constructor for the SimpleCommand class
        :param name: the name of the command
        :param description: the description of the command
        """
        self.name = name
        self.description = description

    def execute(self):
        """
        This is the method that will be called when the command is executed
        :return: None
        """
        print(f"Executing command: {self.name} - {self.description}")


class Invoker(object):
    """
    This is the base class for all commands that can be executed by a user or a bot user
    """

    def __init__(self):
        """
        This is the constructor for the Invoker class
        """
        self._on_start = None
        self._on_finish = None

    def set_on_start(self, command):
        """
        This method sets the command that will be executed when the invoker starts
        :param command: the command to execute
        :return: None
        """
        self._on_start = command

    def set_on_finish(self, command):
        """
        This method sets the command that will be executed when the invoker finishes
        :param command: the command to execute
        :return: None
        """

        self._on_finish = command

    def do_something_important(self):
        """
        This method does something important
        :return: None
        """
        print('Invoker: Does anybody want something done before I begin?')
        if self._on_start:
            self._on_start.execute()

        print('Invoker: ...doing something really important...')

        print('Invoker: Does anybody want something done after I finish?')
        if self._on_finish:
            self._on_finish.execute()


if __name__ == '__main__':
    # Пример использования
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand('Start', "Description of the start command"))
    invoker.set_on_finish(SimpleCommand('Finish', "Description of the finish command"))

    invoker.do_something_important()
