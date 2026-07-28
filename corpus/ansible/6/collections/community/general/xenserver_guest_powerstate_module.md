---
collection: ansible
version: "6"
title: "community.general.xenserver_guest_powerstate module – Manages power states of virtual machines running on Citrix Hypervisor/XenServer host or pool"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/xenserver_guest_powerstate_module.html
fetched_at: 2026-07-27T17:14:06+00:00
---
# community.general.xenserver_guest_powerstate module – Manages power states of virtual machines running on Citrix Hypervisor/XenServer host or pool

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](xenserver_guest_powerstate_module.md#ansible-collections-community-general-xenserver-guest-powerstate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.xenserver_guest_powerstate`.

- [Synopsis](xenserver_guest_powerstate_module.md#synopsis)
- [Requirements](xenserver_guest_powerstate_module.md#requirements)
- [Parameters](xenserver_guest_powerstate_module.md#parameters)
- [Notes](xenserver_guest_powerstate_module.md#notes)
- [Examples](xenserver_guest_powerstate_module.md#examples)
- [Return Values](xenserver_guest_powerstate_module.md#return-values)

## [Synopsis](xenserver_guest_powerstate_module.md#id1)

- This module can be used to power on, power off, restart or suspend virtual machine and gracefully reboot or shutdown guest OS of virtual machine.

## [Requirements](xenserver_guest_powerstate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- XenAPI

## [Parameters](xenserver_guest_powerstate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: host, pool  string | The hostname or IP address of the XenServer host or XenServer pool master.  If the value is not specified in the task, the value of environment variable `XENSERVER_HOST` will be used instead.  Default: `"localhost"` |
| **name**  aliases: name_label  string | Name of the VM to manage.  VMs running on XenServer do not necessarily have unique names. The module will fail if multiple VMs with same name are found.  In case of multiple VMs with same name, use `uuid` to uniquely specify VM to manage.  This parameter is case sensitive. |
| **password**  aliases: pass, pwd  string | The password to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_PASSWORD` will be used instead. |
| **state**  string | Specify the state VM should be in.  If `state` is set to value other than `present`, then VM is transitioned into required state and facts are returned.  If `state` is set to `present`, then VM is just checked for existence and facts are returned.  Choices:   - `"powered-on"` - `"powered-off"` - `"restarted"` - `"shutdown-guest"` - `"reboot-guest"` - `"suspended"` - `"present"` ← (default) |
| **state_change_timeout**  integer | By default, module will wait indefinitely for VM to change state or acquire an IP address if `wait_for_ip_address: true`.  If this parameter is set to positive value, the module will instead wait specified number of seconds for the state change.  In case of timeout, module will generate an error message.  Default: `0` |
| **username**  aliases: admin, user  string | The username to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_USER` will be used instead.  Default: `"root"` |
| **uuid**  string | UUID of the VM to manage if known. This is XenServer’s unique identifier.  It is required if name is not unique. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `XENSERVER_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **wait_for_ip_address**  boolean | Wait until XenServer detects an IP address for the VM.  This requires XenServer Tools to be preinstalled on the VM to work properly.  Choices:   - `false` ← (default) - `true` |

## [Notes](xenserver_guest_powerstate_module.md#id4)

> **Note:**
>
> - Minimal supported version of XenServer is 5.6.
> - Module was tested with XenServer 6.5, 7.1, 7.2, 7.6, Citrix Hypervisor 8.0, XCP-ng 7.6 and 8.0.
> - To acquire XenAPI Python library, just run `pip install XenAPI` on your Ansible Control Node. The library can also be found inside Citrix Hypervisor/XenServer SDK (downloadable from Citrix website). Copy the XenAPI.py file from the SDK to your Python site-packages on your Ansible Control Node to use it. Latest version of the library can also be acquired from GitHub: <https://raw.githubusercontent.com/xapi-project/xen-api/master/scripts/examples/python/XenAPI/XenAPI.py>
> - If no scheme is specified in `hostname`, module defaults to `http://` because `https://` is problematic in most setups. Make sure you are accessing XenServer host in trusted environment or use `https://` scheme explicitly.
> - To use `https://` scheme for `hostname` you have to either import host certificate to your OS certificate store or use `validate_certs: no` which requires XenAPI library from XenServer 7.2 SDK or newer and Python 2.7.9 or newer.

## [Examples](xenserver_guest_powerstate_module.md#id5)

```yaml+jinja
- name: Power on VM
  community.general.xenserver_guest_powerstate:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    name: testvm_11
    state: powered-on
  delegate_to: localhost
  register: facts
```

## [Return Values](xenserver_guest_powerstate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | Metadata about the VM  Returned: always  Sample: `{"cdrom": {"type": "none"}, "customization_agent": "native", "disks": [{"name": "windows-template-testing-0", "name_desc": "", "os_device": "xvda", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "0"}, {"name": "windows-template-testing-1", "name_desc": "", "os_device": "xvdb", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "1"}], "domid": "56", "folder": "", "hardware": {"memory_mb": 8192, "num_cpu_cores_per_socket": 2, "num_cpus": 4}, "home_server": "", "is_template": false, "name": "windows-template-testing", "name_desc": "", "networks": [{"gateway": "192.168.0.254", "gateway6": "fc00::fffe", "ip": "192.168.0.200", "ip6": ["fe80:0000:0000:0000:e9cb:625a:32c5:c291", "fc00:0000:0000:0000:0000:0000:0000:0001"], "mac": "ba:91:3a:48:20:76", "mtu": "1500", "name": "Pool-wide network associated with eth1", "netmask": "255.255.255.128", "prefix": "25", "prefix6": "64", "vif_device": "0"}], "other_config": {"base_template_name": "Windows Server 2016 (64-bit)", "import_task": "OpaqueRef:e43eb71c-45d6-5351-09ff-96e4fb7d0fa5", "install-methods": "cdrom", "instant": "true", "mac_seed": "f83e8d8a-cfdc-b105-b054-ef5cb416b77e"}, "platform": {"acpi": "1", "apic": "true", "cores-per-socket": "2", "device_id": "0002", "hpet": "true", "nx": "true", "pae": "true", "timeoffset": "-25200", "vga": "std", "videoram": "8", "viridian": "true", "viridian_reference_tsc": "true", "viridian_time_ref_count": "true"}, "state": "poweredon", "uuid": "e3c0b2d5-5f05-424e-479c-d3df8b3e7cda", "xenstore_data": {"vm-data": ""}}` |

### Authors

- Bojan Vitnik (@bvitnik)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
