---
collection: ansible
version: "8"
title: "community.general.xenserver_guest_info module – Gathers information for virtual machines running on Citrix Hypervisor/XenServer host or pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xenserver_guest_info_module.html
fetched_at: 2026-07-28T01:51:31+00:00
---
# community.general.xenserver_guest_info module – Gathers information for virtual machines running on Citrix Hypervisor/XenServer host or pool

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](xenserver_guest_info_module.md#ansible-collections-community-general-xenserver-guest-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.xenserver_guest_info`.

- [Synopsis](xenserver_guest_info_module.md#synopsis)
- [Requirements](xenserver_guest_info_module.md#requirements)
- [Parameters](xenserver_guest_info_module.md#parameters)
- [Attributes](xenserver_guest_info_module.md#attributes)
- [Notes](xenserver_guest_info_module.md#notes)
- [Examples](xenserver_guest_info_module.md#examples)
- [Return Values](xenserver_guest_info_module.md#return-values)

## [Synopsis](xenserver_guest_info_module.md#id1)

- This module can be used to gather essential VM facts.

Aliases: cloud.xenserver.xenserver_guest_info

## [Requirements](xenserver_guest_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- XenAPI

## [Parameters](xenserver_guest_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: host, pool  string | The hostname or IP address of the XenServer host or XenServer pool master.  If the value is not specified in the task, the value of environment variable `XENSERVER_HOST` will be used instead.  **Default:** `"localhost"` |
| **name**  aliases: name_label  string | Name of the VM to gather facts from.  VMs running on XenServer do not necessarily have unique names. The module will fail if multiple VMs with same name are found.  In case of multiple VMs with same name, use `uuid` to uniquely specify VM to manage.  This parameter is case sensitive. |
| **password**  aliases: pass, pwd  string | The password to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_PASSWORD` will be used instead. |
| **username**  aliases: admin, user  string | The username to use for connecting to XenServer.  If the value is not specified in the task, the value of environment variable `XENSERVER_USER` will be used instead.  **Default:** `"root"` |
| **uuid**  string | UUID of the VM to gather fact of. This is XenServer’s unique identifier.  It is required if name is not unique. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `XENSERVER_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](xenserver_guest_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](xenserver_guest_info_module.md#id5)

> **Note:**
>
> - Minimal supported version of XenServer is 5.6.
> - Module was tested with XenServer 6.5, 7.1, 7.2, 7.6, Citrix Hypervisor 8.0, XCP-ng 7.6 and 8.0.
> - To acquire XenAPI Python library, just run `pip install XenAPI` on your Ansible Control Node. The library can also be found inside Citrix Hypervisor/XenServer SDK (downloadable from Citrix website). Copy the XenAPI.py file from the SDK to your Python site-packages on your Ansible Control Node to use it. Latest version of the library can also be acquired from GitHub: <https://raw.githubusercontent.com/xapi-project/xen-api/master/scripts/examples/python/XenAPI/XenAPI.py>
> - If no scheme is specified in `hostname`, module defaults to `http://` because `https://` is problematic in most setups. Make sure you are accessing XenServer host in trusted environment or use `https://` scheme explicitly.
> - To use `https://` scheme for `hostname` you have to either import host certificate to your OS certificate store or use `validate_certs: no` which requires XenAPI library from XenServer 7.2 SDK or newer and Python 2.7.9 or newer.
> - This module was called `xenserver_guest_facts` before Ansible 2.9. The usage did not change.

## [Examples](xenserver_guest_info_module.md#id6)

```yaml+jinja
- name: Gather facts
  community.general.xenserver_guest_info:
    hostname: "{{ xenserver_hostname }}"
    username: "{{ xenserver_username }}"
    password: "{{ xenserver_password }}"
    name: testvm_11
  delegate_to: localhost
  register: facts
```

## [Return Values](xenserver_guest_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | Metadata about the VM  **Returned:** always  **Sample:** `{"cdrom": {"type": "none"}, "customization_agent": "native", "disks": [{"name": "testvm_11-0", "name_desc": "", "os_device": "xvda", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "0"}, {"name": "testvm_11-1", "name_desc": "", "os_device": "xvdb", "size": 42949672960, "sr": "Local storage", "sr_uuid": "0af1245e-bdb0-ba33-1446-57a962ec4075", "vbd_userdevice": "1"}], "domid": "56", "folder": "", "hardware": {"memory_mb": 8192, "num_cpu_cores_per_socket": 2, "num_cpus": 4}, "home_server": "", "is_template": false, "name": "testvm_11", "name_desc": "", "networks": [{"gateway": "192.168.0.254", "gateway6": "fc00::fffe", "ip": "192.168.0.200", "ip6": ["fe80:0000:0000:0000:e9cb:625a:32c5:c291", "fc00:0000:0000:0000:0000:0000:0000:0001"], "mac": "ba:91:3a:48:20:76", "mtu": "1500", "name": "Pool-wide network associated with eth1", "netmask": "255.255.255.128", "prefix": "25", "prefix6": "64", "vif_device": "0"}], "other_config": {"base_template_name": "Windows Server 2016 (64-bit)", "import_task": "OpaqueRef:e43eb71c-45d6-5351-09ff-96e4fb7d0fa5", "install-methods": "cdrom", "instant": "true", "mac_seed": "f83e8d8a-cfdc-b105-b054-ef5cb416b77e"}, "platform": {"acpi": "1", "apic": "true", "cores-per-socket": "2", "device_id": "0002", "hpet": "true", "nx": "true", "pae": "true", "timeoffset": "-25200", "vga": "std", "videoram": "8", "viridian": "true", "viridian_reference_tsc": "true", "viridian_time_ref_count": "true"}, "state": "poweredon", "uuid": "e3c0b2d5-5f05-424e-479c-d3df8b3e7cda", "xenstore_data": {"vm-data": ""}}` |

### Authors

- Bojan Vitnik (@bvitnik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
