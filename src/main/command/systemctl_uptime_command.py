from src.main.command.command import Command
from commands import getstatusoutput


class SystemctlUptimeCommand(Command):

    def __init__(self):
        super(SystemctlUptimeCommand, self).__init__("systemctl", "show --all")

    def execute(self, servicename):
        command = self.command + " " + self.arg + " " + str(servicename) + " | grep \"ActiveEnterTimestampMonotonic\""
        command_output = getstatusoutput(command)
        split_output = command_output[1].split("=")

        # micros -> seconds
        activity_output_seconds = long(split_output[1]) / 1000000
        activity_output_minutes = activity_output_seconds / 60


        pass
