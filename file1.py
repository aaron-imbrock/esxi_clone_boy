import os
import subprocess
import sys

class Datastores:
    def __init__(self, name, uuid, path):
        self.name = name
        self.uuid = uuid
        self.path = path

    def __repr__(self):
        return f"Datastore(name={self.name}, uuid={self.uuid}, path={self.path})"

def run_command(command):
    result = {}
    try:
        proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
        )
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            result['stdout'] = stdout.decode('utf-8')
            result['stderr'] = stderr.decode('utf-8')
            result['returncode'] = proc.returncode
        else:
            result['error'] = stderr.decode('utf-8')
            result['returncode'] = proc.returncode
    except Exception as e:
        result['exception'] = str(e)
    return result

def parse_ls_output(output):
    datastores = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) > 8 and parts[0].startswith('l'):
            name = parts[8]
            uuid = parts[10]
            path = os.path.join('/vmfs/volumes', uuid)
            datastores.append(Datastore(name, uuid, path))
    return datastores

if __name__ == '__main__':

    command = ["vim-cmd", "vmsvc/getallvms"]
    results = run_command(command)
    datastores = parse_ls_output(results)
    for datastore in datastores:
        print(datastore)
