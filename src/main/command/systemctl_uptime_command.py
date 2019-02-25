from src.main.command.command import Command
from commands import getstatusoutput
import datetime

from src.main.service_info import ServiceInfo


class SystemctlUptimeCommand(Command):

    def __init__(self):
        super(SystemctlUptimeCommand, self).__init__("systemctl", "status")

    def execute(self, servicename):
        command = self.command + " " + self.arg + " " + str(servicename) + " | awk '/Active: active/{print $6 \" \"$7}'"
        command_output = getstatusoutput(command)

        service_started = datetime.datetime.strptime(command_output[1], "%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()

        # micros -> seconds
        activity_output_seconds = (now - service_started).total_seconds()

        return ServiceInfo("uptime", str(activity_output_seconds))
