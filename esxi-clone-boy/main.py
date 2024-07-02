#!/bin/python

from vim_cmd import VMService

if __name__ == "__main__":
    vm_service = VMService()
    vm_service.run()
    # vm_service.print_output()
    vms = vm_service.get_vmids()
    for vm in vms:
        print(vm)
