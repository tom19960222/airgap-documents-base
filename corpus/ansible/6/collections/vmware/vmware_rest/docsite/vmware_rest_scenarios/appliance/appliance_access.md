---
collection: ansible
version: "6"
title: "Configure the console and SSH access"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vmware/vmware_rest/docsite/vmware_rest_scenarios/appliance/appliance_access.html
fetched_at: 2026-07-28T00:25:33+00:00
---
# Configure the console and SSH access

## Introduction

This section show you how to manage the console and SSH access of the
vCenter Server Appliance (VCSA).

## Scenario requirements

You”ve got an up and running vCenter Server Appliance.

### Manage the shell access

Detect if the Shell is enabled.

```YAML+Jinja
- name: Check if the Shell is enabled
  vmware.vmware_rest.appliance_access_shell_info:
```

response

```YAML+Jinja
{
    "changed": false,
    "value": {
        "enabled": true,
        "timeout": 438
    }
}
```

Or turn on the Shell access with a timeout:

```YAML+Jinja
- name: Disable the Shell
  vmware.vmware_rest.appliance_access_shell:
    enabled: False
    timeout: 600
```

response

```YAML+Jinja
{
    "changed": true,
    "value": {}
}
```

### Manage the Direct Console User Interface (DCUI)

You can use vmware.vmware_rest.appliance_access_dcui_info_module to
get the current state of the configuration:

```YAML+Jinja
- name: Check if the Direct Console User Interface is enabled
  vmware.vmware_rest.appliance_access_dcui_info:
```

response

```YAML+Jinja
{
    "changed": false,
    "value": false
}
```

You can enable or disable the interface with appliance_access_dcui:

```YAML+Jinja
- name: Disable the Direct Console User Interface
  vmware.vmware_rest.appliance_access_dcui:
    enabled: False
```

response

```YAML+Jinja
{
    "changed": false,
    "value": false
}
```

### Manage the SSH interface

You can also get the status of the SSH interface with
appliance_access_ssh_info:

```YAML+Jinja
- name: Check is the SSH access is enabled
  vmware.vmware_rest.appliance_access_ssh_info:
```

response

```YAML+Jinja
{
    "changed": false,
    "value": true
}
```

And to enable the SSH interface:

```YAML+Jinja
- name: Ensure the SSH access ie enabled
  vmware.vmware_rest.appliance_access_ssh:
    enabled: true
```

response

```YAML+Jinja
{
    "changed": false,
    "value": true
}
```
