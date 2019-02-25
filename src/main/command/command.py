from abc import abstractmethod, ABCMeta


class Command:

    __metaclass__ = ABCMeta

    def __init__(self, command, arg):
        self.command = command
        self.arg = arg

    @abstractmethod
    def execute(self, servicename):
        pass
