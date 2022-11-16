##
# Copyright (c) 2021 unSkript, Inc
# All rights reserved.
##

from pydantic import BaseModel, Field
from gevent import joinall
import pprint


class InputSchema(BaseModel):
    host: str = Field(
        title='Host',
        description='Hosts to connect to. For eg. "10.10.10.10"'
    )
    remote_file: str = Field(
        title='Remote File',
        description='Filename on the remote server. Eg /home/ec2-user/my_remote_file'
    )
    local_file: str = Field(
        title="Local File",
        description='Filename on the unSkript proxy. Eg /tmp/my_local_file'
    )
    direction: bool = Field(
        default=True,
        title="Receive",
        description="Direction of the copy operation. Default is receive-from-remote-server"
    )

def ssh_scp_printer(output):
    if output is None:
        return
    print("\n")
    pprint.pprint(output)


def ssh_scp(
        sshClient,
        host: str,
        remote_file: str,
        local_file: str,
        direction: bool = True) -> str:
    """ssh_scp Copy files from or to remote host.

        :type host: str
        :param host: Host to connect to. Eg 10.10.10.10.

        :type remote_file: str
        :param remote_file: Filename on the remote server. Eg /home/ec2-user/my_remote_file

        :type local_file: str
        :param local_file: Filename on the unSkript proxy. Eg /tmp/my_local_file

        :type direction: bool
        :param direction: Direction of the copy operation. Default is receive-from-remote-server

        :rtype:
    """
    client = sshClient([host])
    copy_args = [{'local_file': local_file, 'remote_file': remote_file}]

    if direction is True:
        cmds = client.copy_remote_file(remote_file=remote_file, local_file=local_file,
                                       recurse=False,
                                       suffix_separator="", copy_args=copy_args,
                                       encoding='utf-8')

    else:
        cmds = client.copy_file(local_file=local_file, remote_file=remote_file,
                                recurse=False, copy_args=None)

    try:
        joinall(cmds, raise_error=True)
        if direction is True:
            return f"Successfully copied file {host}://{remote_file} to {local_file}"
        else:
            return f"Successfully copied file {local_file} to {host}://{remote_file}"

    except Exception as e:
        return f"Error encountered while copying files {e}"
