from abc import ABCMeta, abstractmethod

from src.main.command.command import Command


class ServiceParser:

    __metaclass__ = ABCMeta

    services = []
    commands = {}

    def __init__(self, info_command):
        self.command = info_command

    def add_command(self, key, command):
        if isinstance(command, Command):
            self.commands[key] = command

    def apply_whitelist(self, whitelist):
        filtered_whitelist = []
        for service in whitelist:
            if self.get_service_info(service[0], service[1]) is not None:
                filtered_whitelist.append(service)
        return filtered_whitelist

    def get_service_info(self, servicename, arg):
        result = None

        command = self.commands[arg]
        if command is not None:
            result = command.execute(servicename)

        return result

    @abstractmethod
    def parse_service_output(self, servicename, arg):
        pass
