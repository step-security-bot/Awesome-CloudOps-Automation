##
# Copyright (c) 2021 unSkript, Inc
# All rights reserved.
##
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
import pprint


class InputSchema(BaseModel):
    hosts: List[str] = Field(
        title='Hosts',
        description='List of hosts to connect to. For eg. ["host1", "host2"].'
    )
    command: str = Field(
        title='Command',
        description='Command to be executed on the remote server.'
    )
    sudo: Optional[bool] = Field(
        default=False,
        title='Run with sudo',
        description='Run the command with sudo.'
    )


def ssh_execute_remote_command_printer(output):
    if output is None:
        return
    print("\n")
    pprint.pprint(output)


def ssh_execute_remote_command(sshClient, hosts: List[str], command: str, sudo: bool = False) -> Dict:
    """ssh_execute_remote_command executes the given command on the remote

        :type hosts: List[str]
        :param hosts: List of hosts to connect to. For eg. ["host1", "host2"].

        :type command: str
        :param command: Command to be executed on the remote server.

        :type sudo: bool
        :param sudo: Run the command with sudo.

        :rtype: dict of command output
    """

    client = sshClient(hosts)
    runCommandOutput = client.run_command(command=command, sudo=sudo)
    res = {}

    for host, host_output in runCommandOutput.items():
        hostname = host
        output = []
        for line in host_output:
            output.append(line)

        o = "\n".join(output)
        res[hostname] = o

    return res
