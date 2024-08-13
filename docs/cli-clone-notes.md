### Check the list of VMs registered on this ESXi host (we are going to clone the same Windows-VM, that is, the original VM in the previous example).
```
vim-cmd vmsvc/getallvms
```
### Confirm original VM is shutdown before clone
This command will also list running state

```
vim-cmd vmsvc/power.getstate <VM-ID>
```

### This command will shut down a VM

Power off command:
```
vim-cmd vmsvc/power.shutdown <VM-ID>
```
### Get the location of hte configuration file for to be cloned VM

Additionally, get the location of the virtual disks(s).
```
cat /etc/vmware/hostd/vmInventory.xml |grep -i Windows-VM | grep vmx

vim-cmd vmsvc/getallvms |grep -i Windows-VM
```

### The vmx file is listed under the File heading.

Read that file to determine location of the disk files.
```
Vmid          Name                                     File                                  Guest OS        Version   Annotation
12     debian12-base-image   [dataStorage] debian12-base-image/debian12-base-image.vmx   otherLinux64Guest   vmx-14
13     kb1                   [vmStorage] kb1/debian12-base-image.vmx                     otherLinux64Guest   vmx-14
2      Jump Box              [vmStorage] Jump Box/Jump Box.vmx                           debian10_64Guest    vmx-14
```
`less /vmfs/volumes/datastore10a/Windows-VM/Windows-VM.vmx`

### all disk images end in vmdk. Virtual disks in the same folder will not include /vmfs/
```
scsi0:0.fileName = "debian12-base-image.vmdk"
ide0:0.fileName = "/vmfs/volumes/5f3215f2-49c43e04-00b5-002481827d55/debian-12.5.0-amd64-netinst.iso"
```
### create a directory in the appropriate location for the new, about to be cloned VM
`mkdir /vmfs/volumes/UUID-of-Datastore/new-vm-name`

### Clone the config file and the virtual disk of the source VM to the new directory.
 Set new file names to match the name of the new VM clone.
 Clone the virtualdisks (.vmdk)

`vmkfstools -i /vmfs/volumes/datastore10a/Windows-VM/Windows-VM.vmdk /vmfs/volumes/datastore10c/Win-VM-Clone2/Win-VM-Clone2.vmdk -d thin`

# Copy the VM configuration file (.vmx)

`cp /vmfs/volumes/datastore10a/Windows-VM/Windows-VM.vmx /vmfs/volumes/datastore10c/Win-VM-Clone2/Win-VM-Clone2.vmx`

# Edit the new VM conf file (.vmx) to align the VM name and path to the virtual disks.

`%s/foo/bar/g `

# Register the VM clone on the ESXI host

`vim-cmd solo/registervm /vmfs/volumes/datastore10c/Win-VM-Clone2/Win-VM-Clone2.vmx`

# Get the information about the registered VMs to ensure that the cloned virtual machine has been registered:

`vim-cmd vmsvc/getallvms`

