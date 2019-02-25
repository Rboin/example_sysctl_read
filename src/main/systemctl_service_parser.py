from src.main.service_parser import ServiceParser
from commands import getstatusoutput
from logging import getLogger


class SystemctlServiceParser(ServiceParser):

    def __init__(self):
        super(SystemctlServiceParser, self).__init__("systemctl")
        self.services.append("logrotate")
        self.logger = getLogger("SystemctlServiceParser")

    def parse_service_output(self, servicename, arg):
        self.logger.debug('service: %s, args: %s', str(servicename), str(arg))
        result = None
        command = self.commands[arg]
        if command is not None:
            result = command.execute(servicename)
        return result

    def get_service_activity(self, servicename):
        command = str(self.command) + " status " + str(servicename)
        status_output = getstatusoutput(command)
        return status_output

