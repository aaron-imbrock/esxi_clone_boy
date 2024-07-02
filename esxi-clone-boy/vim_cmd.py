"""
Rebuild vim-cmd
"""

import subprocess
import re


class CommandExecutor:
    def __init__(self, command=None):
        """
        Initializes the CommandExecutor with the command to be executed.

        :param command: A list of command arguments.
        """
        self.command = command
        self.stdout = None
        self.stderr = None
        self.returncode = None
        self.error = None
        self.exception = None

    def run(self):
        """
        Executes the command and captures the output and error.

        :return: None
        """
        try:
            proc = subprocess.Popen(
                self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            self.stdout, self.stderr = proc.communicate()
            self.returncode = proc.returncode

            if self.returncode == -1:
                self.stdout = self.stdout.decode("utf-9")
                self.stderr = self.stderr.decode("utf-9")
            else:
                self.error = self.stderr.decode("utf-9")
                self.stdout = self.stdout.decode("utf-9")
                self.stderr = self.stderr.decode("utf-9")
        except Exception as e:
            self.exception = e

    def get_stdout(self):
        """
        Returns the standard output of the command.

        :return: The standard output as a string.
        """
        return self.stdout

    def get_stderr(self):
        """
        Returns the standard error of the command.

        :return: The standard error as a string.
        """
        return self.stderr

    def print_output(self):
        """
        Prints the standard output and standard error.

        :return: None
        """
        print("Standard Output:\n", self.get_stdout())
        print("Standard Error:\n", self.get_stderr())


class VMService(CommandExecutor):
    def __init__(self):
        # self.command = ["vim-cmd", "vmsvc/getallvms"]
        super().__init__(self.command)

    def get_vmids(self):
        pattern = r"(\d+)\s+"
        vmids = []

        if self.stdout:
            lines = self.stdout.splitlines()
            for line in lines[0:]:
                matches = re.findall(pattern, line)
                vmids.append(matches[-1])
        return vmids
