---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_template module – Create, modify, deploy, delete, export, import and clone a template on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_template_module.html
fetched_at: 2026-07-27T17:25:50+00:00
---
# dellemc.openmanage.ome_template module – Create, modify, deploy, delete, export, import and clone a template on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_template_module.md#ansible-collections-dellemc-openmanage-ome-template-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_template`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_template_module.md#synopsis)
- [Requirements](ome_template_module.md#requirements)
- [Parameters](ome_template_module.md#parameters)
- [Notes](ome_template_module.md#notes)
- [Examples](ome_template_module.md#examples)
- [Return Values](ome_template_module.md#return-values)

## [Synopsis](ome_template_module.md#id1)

- This module creates, modifies, deploys, deletes, exports, imports and clones a template on OpenManage Enterprise.

## [Requirements](ome_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | Payload data for the template operations. All the variables in this option are added as payload for `create`, `modify`, `deploy`, `import`, and `clone` operations. It takes the following attributes.  Attributes: List of dictionaries of attributes (if any) to be modified in the deployment template. This is applicable when *command* is `deploy` and `modify`. Use the *Id* If the attribute Id is available. If not, use the comma separated I (DisplayName). For more details about using the *DisplayName*, see the example provided.  Name: Name of the template. This is mandatory when *command* is `create`, `import`, `clone`, and optional when *command* is `modify`.  Description: Description for the template. This is applicable when *command* is `create` or `modify`.  Fqdds: This allows to create a template using components from a specified reference server. One or more, of the following values must be specified in a comma-separated string: iDRAC, System, BIOS, NIC, LifeCycleController, RAID, and EventFilters. If none of the values are specified, the default value ‘All’ is selected. This is applicable when I (command) is `create`.  Options: Options to control device shutdown or end power state post template deployment. This is applicable for `deploy` operation.  Schedule: Provides options to schedule the deployment task immediately, or at a specified time. This is applicable when *command* is `deploy`.  NetworkBootIsoModel: Payload to specify the ISO deployment details. This is applicable when *command* is `deploy`.  Content: The XML content of template. This is applicable when *command* is `import`.  Type: Template type ID, indicating the type of device for which configuration is supported, such as chassis and servers. This is applicable when *command* is `import`.  TypeId: Template type ID, indicating the type of device for which configuration is supported, such as chassis and servers. This is applicable when *command* is `create`.  Refer OpenManage Enterprise API Reference Guide for more details. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  aliases: state  string | `create` creates a new template.  `modify` modifies an existing template.  `deploy` creates a template-deployment job.  `delete` deletes an existing template.  `export` exports an existing template.  `import` creates a template from a specified configuration text in SCP XML format.  `clone` creates a clone of a existing template.  Choices:   - `"create"` ← (default) - `"modify"` - `"deploy"` - `"delete"` - `"export"` - `"import"` - `"clone"` |
| **device_group_names**  list / elements=string | Specify the list of groups when I (command) is `deploy`.  Provide at least one of the mandatory options *device_id*, *device_service_tag*, or *device_group_names*.  Default: `[]` |
| **device_id**  list / elements=integer | Specify the list of targeted device ID(s) when *command* is `deploy`. When I (command) is `create`, specify the ID of a single device.  Either *device_id* or *device_service_tag* is mandatory or both can be applicable.  Default: `[]` |
| **device_service_tag**  list / elements=string | Specify the list of targeted device service tags when I (command) is `deploy`. When *command* is `create`, specify the service tag of a single device.  Either *device_id* or *device_service_tag* is mandatory or both can be applicable.  Default: `[]` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **template_id**  integer | ID of the existing template.  This option is applicable when *command* is `modify`, `deploy`, `delete` and `export`.  This option is mutually exclusive with *template_name*. |
| **template_name**  string | Name of the existing template.  This option is applicable when *command* is `modify`, `deploy`, `delete` and `export`.  This option is mutually exclusive with *template_id*. |
| **template_view_type**  string | Select the type of view of the OME template.  This is applicable when *command* is `create`,`clone` and `import`.  Choices:   - `"Deployment"` ← (default) - `"Compliance"` - `"Inventory"` - `"Sample"` - `"None"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_template_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_template_module.md#id5)

```yaml+jinja
---
- name: Create a template from a reference device
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25123
    attributes:
      Name: "New Template"
      Description: "New Template description"

- name: Modify template name, description, and attribute value
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "modify"
    template_id: 12
    attributes:
      Name: "New Custom Template"
      Description: "Custom Template Description"
      # Attributes to be modified in the template.
      # For information on any attribute id, use API /TemplateService/Templates(Id)/Views(Id)/AttributeViewDetails
      # This section is optional
      Attributes:
        - Id: 1234
          Value: "Test Attribute"
          IsIgnored: false

- name: Modify template name, description, and attribute using detailed view
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "modify"
    template_id: 12
    attributes:
      Name: "New Custom Template"
      Description: "Custom Template Description"
      Attributes:
        # Enter the comma separated string as appearing in the Detailed view on GUI
        # NIC -> NIC.Integrated.1-1-1 -> NIC Configuration -> Wake On LAN1
        - DisplayName: 'NIC, NIC.Integrated.1-1-1, NIC Configuration, Wake On LAN'
          Value: Enabled
          IsIgnored: false
        # System -> LCD Configuration -> LCD 1 User Defined String for LCD
        - DisplayName: 'System, LCD Configuration, LCD 1 User Defined String for LCD'
          Value: LCD str by OMAM
          IsIgnored: false

- name: Deploy template on multiple devices
  dellemc.openmanage.ome_template:
    hostname:  "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_id:
      - 12765
      - 10173
    device_service_tag:
      - 'SVTG123'
      - 'SVTG456'

- name: Deploy template on groups
  dellemc.openmanage.ome_template:
    hostname:  "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_group_names:
      - server_group_1
      - server_group_2

- name: Deploy template on multiple devices along with the attributes values to be modified on the target devices
  dellemc.openmanage.ome_template:
    hostname:  "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_id:
      - 12765
      - 10173
    device_service_tag:
      - 'SVTG123'
    attributes:
      # Device specific attributes to be modified during deployment.
      # For information on any attribute id, use API /TemplateService/Templates(Id)/Views(Id)/AttributeViewDetails
      # This section is optional
      Attributes:
        # specific device where attribute to be modified at deployment run-time.
        # The DeviceId should be mentioned above in the 'device_id' section.
        # Service tags not allowed.
        - DeviceId: 12765
          Attributes:
            - Id : 15645
              Value : "0.0.0.0"
              IsIgnored : false
        - DeviceId: 10173
          Attributes:
            - Id : 18968,
              Value : "hostname-1"
              IsIgnored : false

- name: Deploy template and Operating System (OS) on multiple devices
  dellemc.openmanage.ome_template:
    hostname:  "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_id:
      - 12765
    device_service_tag:
      - 'SVTG123'
    attributes:
      # Include this to install OS on the devices.
      # This section is optional
      NetworkBootIsoModel:
        BootToNetwork: true
        ShareType: "NFS"
        IsoTimeout: 1 # allowable values(1,2,4,8,16) in hours
        IsoPath: "/home/iso_path/filename.iso"
        ShareDetail:
          IpAddress: "192.168.0.2"
          ShareName: "sharename"
          User: "share_user"
          Password: "share_password"
      Options:
        EndHostPowerState: 1
        ShutdownType: 0
        TimeToWaitBeforeShutdown: 300
      Schedule:
        RunLater: true
        RunNow: false

- name: "Deploy template on multiple devices and changes the device-level attributes. After the template is deployed,
install OS using its image"
  dellemc.openmanage.ome_template:
    hostname:  "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_id:
      - 12765
      - 10173
    device_service_tag:
      - 'SVTG123'
      - 'SVTG456'
    attributes:
      Attributes:
        - DeviceId: 12765
          Attributes:
            - Id : 15645
              Value : "0.0.0.0"
              IsIgnored : false
        - DeviceId: 10173
          Attributes:
            - Id : 18968,
              Value : "hostname-1"
              IsIgnored : false
      NetworkBootIsoModel:
        BootToNetwork: true
        ShareType: "NFS"
        IsoTimeout: 1 # allowable values(1,2,4,8,16) in hours
        IsoPath: "/home/iso_path/filename.iso"
        ShareDetail:
          IpAddress: "192.168.0.2"
          ShareName: "sharename"
          User: "share_user"
          Password: "share_password"
      Options:
        EndHostPowerState: 1
        ShutdownType: 0
        TimeToWaitBeforeShutdown: 300
      Schedule:
        RunLater: true
        RunNow: false

- name: Delete template
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "delete"
    template_id: 12

- name: Export a template
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "export"
    template_id: 12

# Start of example to export template to a local xml file
- name: Export template to a local xml file
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "export"
    template_name: "my_template"
  register: result
- name: Save template into a file
  ansible.builtin.copy:
    content: "{{ result.Content}}"
    dest: "/path/to/exported_template.xml"
# End of example to export template to a local xml file

- name: Clone a template
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "clone"
    template_id: 12
    attributes:
      Name: "New Cloned Template Name"

- name: Import template from XML content
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "import"
    attributes:
      Name: "Imported Template Name"
      # Template Type from TemplateService/TemplateTypes
      Type: 2
      # xml string content
      Content: "<SystemConfiguration Model=\"PowerEdge R940\" ServiceTag=\"SVCTAG1\"
      TimeStamp=\"Tue Sep 24 09:20:57.872551 2019\">\n<Component FQDD=\"AHCI.Slot.6-1\">\n<Attribute
      Name=\"RAIDresetConfig\">True</Attribute>\n<Attribute Name=\"RAIDforeignConfig\">Clear</Attribute>\n
      </Component>\n<Component FQDD=\"Disk.Direct.0-0:AHCI.Slot.6-1\">\n<Attribute Name=\"RAIDPDState\">Ready
      </Attribute>\n<Attribute Name=\"RAIDHotSpareStatus\">No</Attribute>\n</Component>\n
      <Component FQDD=\"Disk.Direct.1-1:AHCI.Slot.6-1\">\n<Attribute Name=\"RAIDPDState\">Ready</Attribute>\n
      <Attribute Name=\"RAIDHotSpareStatus\">No</Attribute>\n</Component>\n</SystemConfiguration>\n"

- name: Import template from local XML file
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "import"
    attributes:
      Name: "Imported Template Name"
      Type: 2
      Content: "{{ lookup('ansible.builtin.file', '/path/to/xmlfile') }}"

- name: "Deploy template and Operating System (OS) on multiple devices."
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "deploy"
    template_id: 12
    device_id:
      - 12765
    device_service_tag:
      - 'SVTG123'
    attributes:
      # Include this to install OS on the devices.
      # This section is optional
      NetworkBootIsoModel:
        BootToNetwork: true
        ShareType: "CIFS"
        IsoTimeout: 1 # allowable values(1,2,4,8,16) in hours
        IsoPath: "/home/iso_path/filename.iso"
        ShareDetail:
          IpAddress: "192.168.0.2"
          ShareName: "sharename"
          User: "share_user"
          Password: "share_password"
      Options:
        EndHostPowerState: 1
        ShutdownType: 0
        TimeToWaitBeforeShutdown: 300
      Schedule:
        RunLater: true
        RunNow: false

- name: Create a compliance template from reference device
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "create"
    device_service_tag:
      - "SVTG123"
    template_view_type: "Compliance"
    attributes:
      Name: "Configuration Compliance"
      Description: "Configuration Compliance Template"
      Fqdds: "BIOS"

- name: Import a compliance template from XML file
  dellemc.openmanage.ome_template:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "import"
    template_view_type: "Compliance"
    attributes:
      Name: "Configuration Compliance"
      Content: "{{ lookup('ansible.builtin.file', './test.xml') }}"
      Type: 2
```

## [Return Values](ome_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **Content**  string | XML content of the exported template. This content can be written to a xml file.  Returned: success, when *command* is `export`  Sample: `"<SystemConfiguration Model=\"PowerEdge R940\" ServiceTag=\"DEFG123\" TimeStamp=\"Tue Sep 24 09:20:57.872551 2019\">\n<Component FQDD=\"AHCI.Slot.6-1\">\n<Attribute Name=\"RAIDresetConfig\">True</Attribute>\n<Attribute Name=\"RAIDforeignConfig\">Clear</Attribute>\n</Component>\n<Component FQDD=\"Disk.Direct.0-0:AHCI.Slot.6-1\"> \n<Attribute Name=\"RAIDPDState\">Ready</Attribute>\n<Attribute Name=\"RAIDHotSpareStatus\">No</Attribute> \n</Component>\n<Component FQDD=\"Disk.Direct.1-1:AHCI.Slot.6-1\">\n<Attribute Name=\"RAIDPDState\">Ready </Attribute>\n<Attribute Name=\"RAIDHotSpareStatus\">No</Attribute>\n</Component>\n</SystemConfiguration>"` |
| **devices_assigned**  dictionary | Mapping of devices with the templates already deployed on them.  Returned: *command* is `deploy`  Sample: `{"10312": 23, "10362": 28}` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the template operation.  Returned: always  Sample: `"Successfully created a template with ID 23"` |
| **return_id**  integer | ID of the template for `create`, `modify`, `import` and `clone` or task created in case of `deploy`.  Returned: success, when *command* is `create`, `modify`, `import`, `clone` and `deploy`  Sample: `12` |
| **TemplateId**  integer | ID of the template for `export`.  Returned: success, when *command* is `export`  Sample: `13` |

### Authors

- Jagadeesh N V (@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
