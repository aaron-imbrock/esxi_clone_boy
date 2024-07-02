"""
Rebuild vim-cmd
"""

import re
import subprocess


def run_command(command):
    """
    Executes the command and captures the output and error.

    :param command: A list of command arguments.
    :return: (stdout, stderr)
    """
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        returncode = proc.returncode

        if returncode == 0:
            stdout = stdout.decode("utf-8")
            stderr = stderr.decode("utf-8")
        else:
            stdout = stdout.decode("utf-8")
            stderr = stderr.decode("utf-8")

        return stdout, stderr
    except Exception as e:
        return None, str(e)


def vim_cmd(*args):
    """
    Build base vim-cmd command with the provided arguments
    :param args: Command arguments
    :return: (stdout, stderr)
    """
    command = ["vim-cmd"] + list(args)
    print("Executing command: {}".format(" ".join(command)))
    return run_command(command)


def run_getallvms():
    """
    Adds 'vmsvc' to the command and delegates to vim_cmd.

    :param args: Command arguments.
    :return: (stdout, stderr)
    """
    return vim_cmd("vmsvc/getallvms")


def list_vm_ids(*args):
    """
    Returns list of VM IDs
    :param args:
    :return: list[] if VM IDs
    """
    pattern = r"(\d+)\s+"
    vmids = list()
    stdout, stderr = run_getallvms()
    if stdout:
        lines = stdout.splitlines()
        for line in lines[1:]:
            matches = re.findall(pattern, line)
            vmids.append(matches[0])
    return vmids


if __name__ == "__main__":
    print(list_vm_ids())
