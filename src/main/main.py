import logging

from src.main.command.systemctl_restarted_command import SystemctlRestartedCommand
from src.main.command.systemctl_status_command import SystemctlStatusCommand
from src.main.command.systemctl_uptime_command import SystemctlUptimeCommand
from src.main.service_parser import ServiceParser

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    request_list = [
        ("logrotate", "status"),
        ("lightdm", "uptime"),
        ("lightdm", "restarted")
    ]

    systemctlparser = ServiceParser("systemctl")
    systemctl_status_command = SystemctlStatusCommand()
    systemctl_uptime_command = SystemctlUptimeCommand()
    systemctl_restarted_command = SystemctlRestartedCommand(systemctl_uptime_command)
    systemctlparser.add_command("status", systemctl_status_command)
    systemctlparser.add_command("uptime", systemctl_uptime_command)
    systemctlparser.add_command("restarted", systemctl_restarted_command)
    service_parsers = [systemctlparser]

    for request in request_list:
        output = None
        for service_parser in service_parsers:
            service_parser_output = service_parser.get_service_info(request[0], request[1])
            if service_parser_output is not None:
                output = service_parser_output
                break
        logging.debug("Got output: %s", output)
