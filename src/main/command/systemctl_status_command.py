from src.main.service_info import ServiceInfo
from src.main.command.command import Command
from commands import getstatusoutput

class SystemctlStatusCommand(Command):

    def __init__(self):
        super(SystemctlStatusCommand, self).__init__("systemctl", "is-active")

    def execute(self, servicename):
        command_output = getstatusoutput(self.command + " " + self.arg + " " + str(servicename))
        splitted_output = command_output[1].split("\n")
        return ServiceInfo("status", splitted_output[0])
