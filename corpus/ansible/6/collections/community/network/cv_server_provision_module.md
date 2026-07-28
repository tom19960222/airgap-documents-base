---
collection: ansible
version: "6"
title: "community.network.cv_server_provision module – Provision server port by applying or removing template configuration to an Arista CloudVision Portal configlet that is applied to a switch."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cv_server_provision_module.html
fetched_at: 2026-07-27T17:18:21+00:00
---
# community.network.cv_server_provision module – Provision server port by applying or removing template configuration to an Arista CloudVision Portal configlet that is applied to a switch.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](cv_server_provision_module.md#ansible-collections-community-network-cv-server-provision-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.cv_server_provision`.

- [Synopsis](cv_server_provision_module.md#synopsis)
- [Requirements](cv_server_provision_module.md#requirements)
- [Parameters](cv_server_provision_module.md#parameters)
- [Examples](cv_server_provision_module.md#examples)
- [Return Values](cv_server_provision_module.md#return-values)

## [Synopsis](cv_server_provision_module.md#id1)

- This module allows a server team to provision server network ports for new servers without having to access Arista CVP or asking the network team to do it for them. Provide the information for connecting to CVP, switch rack, port the new server is connected to, optional vlan, and an action and the module will apply the configuration to the switch port via CVP. Actions are add (applies template config to port), remove (defaults the interface config) and show (returns the current port config).

## [Requirements](cv_server_provision_module.md#id2)

The below requirements are needed on the host that executes this module.

- Jinja2
- cvprac >= 0.7.0

## [Parameters](cv_server_provision_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | The action for the module to take. The actions are add, which applies the specified template config to port, remove, which defaults the specified interface configuration, and show, which will return the current port configuration with no changes.  Choices:   - `"show"` ← (default) - `"add"` - `"remove"` |
| **auto_run**  boolean | Flag that determines whether or not the module will execute the CVP task spawned as a result of changes to a switch configlet. When an add or remove action is taken which results in a change to a switch configlet, CVP will spawn a task that needs to be executed for the configuration to be applied to the switch. If this option is True then the module will determined the task number created by the configuration change, execute it and wait for the task to complete. If the option is False then the task will remain in the Pending state in CVP for a network administrator to review and execute.  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | The hostname or IP address of the CVP node being connected to. |
| **password**  string / required | The password of the user that will be used to connect to CVP for API calls. |
| **port**  string | The port number to use when making API calls to the CVP node. This will default to the default port for the specified protocol. Port 80 for http and port 443 for https. |
| **port_vlan**  string | The vlan that should be applied to the port for this server. This parameter is dependent on a proper template that supports single vlan provisioning with it. If a port vlan is specified by the template specified does not support this the module will exit out with no changes. If a template is specified that requires a port vlan but no port vlan is specified the module will exit out with no changes. |
| **protocol**  string | The protocol to use when making API calls to CVP. CVP defaults to https and newer versions of CVP no longer support http.  Choices:   - `"https"` ← (default) - `"http"` |
| **server_name**  string / required | The hostname or identifier for the server that is having it’s switch port provisioned. |
| **switch_name**  string / required | The hostname of the switch is being configured for the server being provisioned. |
| **switch_port**  string / required | The physical port number on the switch that the new server is connected to. |
| **template**  string / required | A path to a Jinja formatted template file that contains the configuration block that will be applied to the specified switch port. This template will have variable fields replaced by the module before being applied to the switch configuration. |
| **username**  string / required | The user that will be used to connect to CVP for making API calls. |

## [Examples](cv_server_provision_module.md#id4)

```yaml+jinja
- name: Get current configuration for interface Ethernet2
  community.network.cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: template_file.j2
    action: show

- name: Remove existing configuration from interface Ethernet2. Run task.
  community.network.cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: template_file.j2
    action: remove
    auto_run: True

- name: Add template configuration to interface Ethernet2. No VLAN. Run task.
  community.network.cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    template: single_attached_trunk.j2
    action: add
    auto_run: True

- name: Add template with VLAN configuration to interface Ethernet2. Run task.
  community.network.cv_server_provision:
    host: cvp_node
    username: cvp_user
    password: cvp_pass
    protocol: https
    server_name: new_server
    switch_name: eos_switch_1
    switch_port: 2
    port_vlan: 22
    template: single_attached_vlan.j2
    action: add
    auto_run: True
```

## [Return Values](cv_server_provision_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Signifies if a change was made to the configlet  Returned: success  Sample: `true` |
| **currentConfigBlock**  string | The current config block for the user specified interface  Returned: when action = show  Sample: `"interface Ethernet4\n!\n"` |
| **fullConfig**  string | The full config of the configlet after being updated  Returned: when action = add or remove  Sample: `"!\ninterface Ethernet3\n!\ninterface Ethernet4\n!\n"` |
| **newConfigBlock**  string | The new config block for the user specified interface  Returned: when action = add or remove  Sample: `"interface Ethernet3\n    description example\n    no switchport\n!\n"` |
| **oldConfigBlock**  string | The current config block for the user specified interface before any changes are made  Returned: when action = add or remove  Sample: `"interface Ethernet3\n!\n"` |
| **portConfigurable**  boolean | Signifies if the user specified port has an entry in the configlet that Ansible has access to  Returned: success  Sample: `true` |
| **switchConfigurable**  boolean | Signifies if the user specified switch has a configlet applied to it that CVP is allowed to edit  Returned: success  Sample: `true` |
| **switchInfo**  dictionary | Information from CVP describing the switch being configured  Returned: success  Sample: `{"architecture": "i386", "bootupTimeStamp": 1491264298.21, "complianceCode": "0000", "complianceIndication": "NONE", "deviceInfo": "Registered", "deviceStatus": "Registered", "fqdn": "veos1", "hardwareRevision": "", "internalBuildId": "12-12", "internalVersion": "4.17.1F-11111.4171F", "ipAddress": "192.168.1.20", "isDANZEnabled": "no", "isMLAGEnabled": "no", "key": "00:50:56:5d:e5:e0", "lastSyncUp": 1496432895799, "memFree": 472976, "memTotal": 1893460, "modelName": "vEOS", "parentContainerId": "container_13_5776759195930", "serialNumber": "", "systemMacAddress": "00:50:56:5d:e5:e0", "taskIdList": [], "tempAction": null, "type": "netelement", "unAuthorized": false, "version": "4.17.1F", "ztpMode": "false"}` |
| **taskCompleted**  boolean | Signifies if the task created and executed has completed successfully  Returned: when action = add or remove, and auto_run = true, and configuration changes  Sample: `true` |
| **taskCreated**  boolean | Signifies if a task was created due to configlet changes  Returned: when action = add or remove, and auto_run = true or false, and configuration changes  Sample: `true` |
| **taskExecuted**  boolean | Signifies if the automation executed the spawned task  Returned: when action = add or remove, and auto_run = true, and configuration changes  Sample: `true` |
| **taskId**  string | The task ID created by CVP because of changes to configlet  Returned: when action = add or remove, and auto_run = true or false, and configuration changes  Sample: `"500"` |
| **updateConfigletResponse**  string | Response returned from CVP when configlet update is triggered  Returned: when action = add or remove and configuration changes  Sample: `"Configlet veos1-server successfully updated and task initiated."` |

### Authors

- EOS+ CS (@mharista)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
