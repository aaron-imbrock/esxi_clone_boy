import xml.etree.ElementTree as ET


# Define the class for ConfigEntry
class ConfigEntry:
    def __init__(self, id, obj_id, sec_domain, vmx_cfg_path):
        self.id = id
        self.obj_id = obj_id
        self.sec_domain = sec_domain
        self.vmx_cfg_path = vmx_cfg_path

    def __repr__(self):
        return "ConfigEntry(id={}, obj_id={}, sec_domain={}, vmx_cfg_path={})".format(
            self.id, self.obj_id, self.sec_domain, self.vmx_cfg_path
        )


# XML data string
xml_data = """
<Root>
  <ConfigEntry id="0000">
    <objID>2</objID>
    <secDomain>11</secDomain>
    <vmxCfgPath>/vmfs/volumes/5fbccd01-70743049-2728-002481827d55/Jump Box/Jump Box.vmx</vmxCfgPath>
  </ConfigEntry>
  <ConfigEntry id="0001">
    <objID>12</objID>
    <secDomain/>
    <vmxCfgPath>/vmfs/volumes/5f3215f2-49c43e04-00b5-002481827d55/debian12-base-image/debian12-base-image.vmx</vmxCfgPath>
  </ConfigEntry>
  <ConfigEntry id="0002">
    <objID>16</objID>
    <secDomain/>
    <vmxCfgPath>/vmfs/volumes/5fbccd01-70743049-2728-002481827d55/kb1/kb1.vmx</vmxCfgPath>
  </ConfigEntry>
</Root>
"""


def get_vmxCfgPath(objID, xml_data):
    
    objID = str(objID)
    # Parse the XML data returned from `vim-cmd vmsvc/getallvms`
    root = ET.fromstring(xml_data)

    # List to hold ConfigEntry objects
    config_entries = []

    # Iterate over ConfigEntry elements in the XML
    for entry in root.findall("ConfigEntry"):
        id = entry.get("id")
        obj_id = entry.find("objID").text
        sec_domain = (
            entry.find("secDomain").text if entry.find("secDomain").text else None
        )
        vmx_cfg_path = entry.find("vmxCfgPath").text

        # Create a ConfigEntry object and add it to the list
        config_entry = ConfigEntry(id, obj_id, sec_domain, vmx_cfg_path)
        config_entries.append(config_entry)

    for entry in config_entries:
        if entry.obj_id == objID:
            return entry.vmx_cfg_path
    return None


if __name__ == "__main__":
    vmx_cfg_path = get_vmxCfgPath(12, xml_data)
    print(vmx_cfg_path)
