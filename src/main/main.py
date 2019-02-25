from src.main.command.systemctl_uptime_command import SystemctlUptimeCommand
from src.main.systemctl_service_parser import SystemctlServiceParser
import logging

from src.main.command.systemctl_status_command import SystemctlStatusCommand

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    request_list = [
        ("logrotate", "status"),
        ("lightdm", "uptime")
    ]

    whitelist = [("logrotate", "status"), ("snmpd", "status")]

    systemctlparser = SystemctlServiceParser()
    systemctlparser.add_command("status", SystemctlStatusCommand())
    systemctlparser.add_command("uptime", SystemctlUptimeCommand())
    systemctlparser.apply_whitelist(whitelist)
    service_parsers = [systemctlparser]

    for request in request_list:

        output = None
        for service_parser in service_parsers:
            service_parser_output = service_parser.get_service_info(request[0], request[1])
            if service_parser_output is not None:
                output = service_parser_output
                break
        logging.debug("Got output: %s", output)
