---
collection: ansible
version: "8"
title: "vmware.vmware_rest.vcenter_vm_guest_customization module – Applies a customization specification on the virtual machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/vcenter_vm_guest_customization_module.html
fetched_at: 2026-07-28T02:57:58+00:00
---
# vmware.vmware_rest.vcenter_vm_guest_customization module – Applies a customization specification on the virtual machine

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](vcenter_vm_guest_customization_module.md#ansible-collections-vmware-vmware-rest-vcenter-vm-guest-customization-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.vcenter_vm_guest_customization`.

New in vmware.vmware_rest 0.1.0

- [Synopsis](vcenter_vm_guest_customization_module.md#synopsis)
- [Requirements](vcenter_vm_guest_customization_module.md#requirements)
- [Parameters](vcenter_vm_guest_customization_module.md#parameters)
- [Notes](vcenter_vm_guest_customization_module.md#notes)
- [Examples](vcenter_vm_guest_customization_module.md#examples)
- [Return Values](vcenter_vm_guest_customization_module.md#return-values)

## [Synopsis](vcenter_vm_guest_customization_module.md#id1)

- Applies a customization specification on the virtual machine in [{@param.name](mailto:{%40param.name) vm}. The actual customization happens inside the guest when the virtual machine is powered on. If there is a pending customization for the virtual machine and a new one is set, then the existing customization setting will be overwritten with the new settings.

## [Requirements](vcenter_vm_guest_customization_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](vcenter_vm_guest_customization_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configuration_spec**  dictionary / required | Settings to be applied to the guest during the customization. This parameter is mandatory.  Valid attributes are:  - `windows_config` (dict): Guest customization specification for a Windows guest operating system ([‘set’])    - Accepted keys:      - reboot (string): The `reboot_option` specifies what should be done to the guest after the customization.  Accepted value for this field:  - `NO_REBOOT` - `REBOOT` - `SHUTDOWN`   - sysprep (object): Customization settings like user details, administrator details, etc for the windows guest operating system. Exactly one of `#sysprep` or `#sysprep_xml` must be specified. - sysprep_xml (string): All settings specified in a XML format. This is the content of a typical answer.xml file that is used by System administrators during the Windows image customization. Check <https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs> Exactly one of `#sysprep` or `#sysprep_xml` must be specified.   - `linux_config` (dict): Guest customization specification for a linux guest operating system ([‘set’])    - Accepted keys:      - hostname (object): The computer name of the (Windows) virtual machine. A computer name may contain letters (A-Z), numbers(0-9) and hyphens (-) but no spaces or periods (.). The name may not consist entirely of digits. A computer name is restricted to 15 characters in length. If the computer name is longer than 15 characters, it will be truncated to 15 characters. Check [{@link](mailto:{%40link) HostnameGenerator} for various options.     - domain (string): The fully qualified domain name.     - time_zone (string): The case-sensitive time zone, such as Europe/Sofia. Valid time zone values are based on the tz (time zone) database used by Linux. The values are strings in the form “Area/Location,” in which Area is a continent or ocean name, and Location is the city, island, or other regional designation. See the <https://kb.vmware.com/kb/2145518> for a list of supported time zones for different versions in Linux.     - script_text (string): The script to run before and after Linux guest customization.<br> The max size of the script is 1500 bytes. As long as the script (shell, perl, python…) has the right “#!” in the header, it is supported. The caller should not assume any environment variables when the script is run. The script is invoked by the customization engine using the command line: 1) with argument “precustomization” before customization, 2) with argument “postcustomization” after customization. The script should parse this argument and implement pre-customization or post-customization task code details in the corresponding block. A Linux shell script example: <code> #!/bin/sh<br> if [ x$1 == x”precustomization” ]; then<br> echo “Do Precustomization tasks”<br> #code for pre-customization actions…<br> elif [ x$1 == x”postcustomization” ]; then<br> echo “Do Postcustomization tasks”<br> #code for post-customization actions…<br> fi<br> </code> |
| **global_DNS_settings**  dictionary / required | Global DNS settings constitute the DNS settings that are not specific to a particular virtual network adapter. This parameter is mandatory.  Valid attributes are:  - `dns_suffix_list` (list): List of name resolution suffixes for the virtual network adapter. This list applies to both Windows and Linux guest customization. For Linux, this setting is global, whereas in Windows, this setting is listed on a per-adapter basis. ([‘set’]) - `dns_servers` (list): List of DNS servers, for a virtual network adapter with a static IP address. If this list is empty, then the guest operating system is expected to use a DHCP server to get its DNS server settings. These settings configure the virtual machine to use the specified DNS servers. These DNS server settings are listed in the order of preference. ([‘set’]) |
| **interfaces**  list / elements=dictionary / required | IP settings that are specific to a particular virtual network adapter. The [{@link](mailto:{%40link) AdapterMapping} [{@term](mailto:{%40term) structure} maps a network adapter’s MAC address to its [{@link](mailto:{%40link) IPSettings}. May be empty if there are no network adapters, else should match number of network adapters configured for the VM. This parameter is mandatory.  Valid attributes are:  - `mac_address` (str): The MAC address of a network adapter being customized. ([‘set’]) - `adapter` (dict): The IP settings for the associated virtual network adapter. ([‘set’])  This key is required with [‘set’].    - Accepted keys:      - ipv4 (object): Specification to configure IPv4 address, subnet mask and gateway info for this virtual network adapter.     - ipv6 (object): Specification to configure IPv6 address, subnet mask and gateway info for this virtual network adapter.     - windows (object): Windows settings to be configured for this specific virtual Network adapter. This is valid only for Windows guest operating systems. |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **vm**  string / required | The unique identifier of the virtual machine that needs to be customized. This parameter is mandatory. |

## [Notes](vcenter_vm_guest_customization_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](vcenter_vm_guest_customization_module.md#id5)

```yaml+jinja
- name: Customize the VM
  vmware.vmware_rest.vcenter_vm_guest_customization:
    vm: "{{ lookup('vmware.vmware_rest.vm_moid', '/my_dc/vm/test_vm1') }}"
    configuration_spec:
      linux_config:
        domain: mydomain
        hostname:
          fixed_name: foobar
          type: FIXED
    interfaces:
    - adapter:
        ipv4:
          type: STATIC
          gateways:
          - 192.168.123.1
          ip_address: 192.168.123.50
          prefix: 24
    global_DNS_settings:
      dns_suffix_list: []
      dns_servers:
      - 1.1.1.1
```

## [Return Values](vcenter_vm_guest_customization_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  dictionary | Customize the VM  **Returned:** On success  **Sample:** `{}` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
