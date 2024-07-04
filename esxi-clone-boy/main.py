#!/bin/python

from vim_cmd import list_vm_ids

if __name__ == "__main__":
    vms = list_vm_ids()
    print(vms)
