from src.main.command.command import Command
from src.main.service_info import ServiceInfo


class SystemctlRestartedCommand(Command):

    def __init__(self, uptime_command):
        super(SystemctlRestartedCommand, self).__init__(None, None)
        self._uptime_command = uptime_command

    def execute(self, servicename):
        service_uptime_info = self._uptime_command.execute(servicename)
        service_uptime = float(service_uptime_info.get_value())
        service_restarted = service_uptime < 180
        return ServiceInfo("restarted", str(service_restarted))
