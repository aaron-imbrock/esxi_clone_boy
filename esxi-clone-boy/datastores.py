###
# esxcli --formatter=xml storage filesystem list

### TODO:
# convert xml to objects. Similar to elemtree_example.py

class Datastores:
    def __init__(self, mount_point, volume_name, uuid, mounted, type, size, free):
        self.mount_point = mount_point
        self.uuid = uuid
        self.volume_name = volume_name
        self.mounted = mounted
        self.type = type
        self.size = size
        self.free = free

    def __repr__(self):
        return f"Datastore(name={self.name}, uuid={self.uuid}, path={self.path})"
