import logging
from abc import ABCMeta, abstractmethod
from src.main.command.command import Command


class ServiceParser:

    __metaclass__ = ABCMeta

    _commands = {}

    def __init__(self, name):
        self._name = name
        self._logger = logging.getLogger(self._name)

    def add_command(self, key, command):
        if isinstance(command, Command):
            self._logger.debug("Adding Command: {0}...".format(command))
            self._commands[key] = command
        else:
            self._logger.error("Not an instance of Command...");

    def get_service_info(self, servicename, arg):
        result = None

        command = self._commands[arg]
        if command is not None:
            self._logger.debug("Found Command: {0}, executing...".format(command))
            result = command.execute(servicename)
        self._logger.debug("Result: {0}".format(result))
        return result
