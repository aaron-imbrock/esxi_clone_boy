
[root@esxi1:~] vim-cmd hostsvc/datastore/listsummary
(vim.Datastore.Summary) [
   (vim.Datastore.Summary) {
      datastore = 'vim.Datastore:5f3215f2-49c43e04-00b5-002481827d55', 
      name = "dataStorage", 
      url = "/vmfs/volumes/5f3215f2-49c43e04-00b5-002481827d55", 
      capacity = 239981297664, 
      freeSpace = 214053158912, 
      uncommitted = 0, 
      accessible = true, 
      multipleHostAccess = <unset>, 
      type = "VMFS", 
      maintenanceMode = <unset>
   }, 
   (vim.Datastore.Summary) {
      datastore = 'vim.Datastore:5fbccd01-70743049-2728-002481827d55', 
      name = "vmStorage", 
      url = "/vmfs/volumes/5fbccd01-70743049-2728-002481827d55", 
      capacity = 499826819072, 
      freeSpace = 440241487872, 
      uncommitted = 1329283568, 
      accessible = true, 
      multipleHostAccess = <unset>, 
      type = "VMFS", 
      maintenanceMode = <unset>
   }
]


class Datastores:
    def __init__(self, name, uuid, path):
        self.name = name
        self.uuid = uuid
        self.path = path

    def __repr__(self):
        return f"Datastore(name={self.name}, uuid={self.uuid}, path={self.path})"
