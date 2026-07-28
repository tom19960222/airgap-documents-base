---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_install_os module – Set boot options like boot, kickstart image and issu."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_install_os_module.html
fetched_at: 2026-07-28T01:38:45+00:00
---
# cisco.nxos.nxos_install_os module – Set boot options like boot, kickstart image and issu.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_install_os`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_install_os_module.md#synopsis)
- [Parameters](nxos_install_os_module.md#parameters)
- [Notes](nxos_install_os_module.md#notes)
- [Examples](nxos_install_os_module.md#examples)
- [Return Values](nxos_install_os_module.md#return-values)

## [Synopsis](nxos_install_os_module.md#id1)

- Install an operating system by setting the boot options like boot image and kickstart image and optionally select to install using ISSU (In Server Software Upgrade).

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: install_os

## [Parameters](nxos_install_os_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **issu**  string | Upgrade using In Service Software Upgrade (ISSU). (Supported on N5k, N7k, N9k platforms)  Selecting ‘required’ or ‘yes’ means that upgrades will only proceed if the switch is capable of ISSU.  Selecting ‘desired’ means that upgrades will use ISSU if possible but will fall back to disruptive upgrade if needed.  Selecting ‘no’ means do not use ISSU. Forced disruptive.  **Choices:**   - `"required"` - `"desired"` - `"yes"` - `"no"` ← (default) |
| **kickstart_image_file**  string | Name of the kickstart image file on flash. (Not required on all Nexus platforms) |
| **system_image_file**  string / required | Name of the system (or combined) image file on flash. |

## [Notes](nxos_install_os_module.md#id3)

> **Note:**
>
> - Tested against the following platforms and images - N9k 7.0(3)I4(6), 7.0(3)I5(3), 7.0(3)I6(1), 7.0(3)I7(1), 7.0(3)F2(2), 7.0(3)F3(2) - N3k 6.0(2)A8(6), 6.0(2)A8(8), 7.0(3)I6(1), 7.0(3)I7(1) - N7k 7.3(0)D1(1), 8.0(1), 8.1(1), 8.2(1)
> - Tested against Cisco MDS NX-OS 9.2(1)
> - This module requires both the ANSIBLE_PERSISTENT_CONNECT_TIMEOUT and ANSIBLE_PERSISTENT_COMMAND_TIMEOUT timers to be set to 600 seconds or higher. The module will exit if the timers are not set properly.
> - When using connection local, ANSIBLE_PERSISTENT_CONNECT_TIMEOUT and ANSIBLE_PERSISTENT_COMMAND_TIMEOUT can only be set using ENV variables or the ansible.cfg file.
> - Do not include full file paths, just the name of the file(s) stored on the top level flash directory.
> - This module attempts to install the software immediately, which may trigger a reboot.
> - In check mode, the module will indicate if an upgrade is needed and whether or not the upgrade is disruptive or non-disruptive(ISSU).
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_install_os_module.md#id4)

```yaml+jinja
- name: Install OS on N9k
  check_mode: false
  cisco.nxos.nxos_install_os:
    system_image_file: nxos.7.0.3.I6.1.bin
    issu: desired

- name: Wait for device to come back up with new image
  wait_for:
    port: 22
    state: started
    timeout: 500
    delay: 60
    host: '{{ inventory_hostname }}'

- name: Check installed OS for newly installed version
  nxos_command:
    commands: [show version | json]
  register: output
- assert:
    that:
    - output['stdout'][0]['kickstart_ver_str'] == '7.0(3)I6(1)'
```

## [Return Values](nxos_install_os_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **install_state**  dictionary | Boot and install information.  **Returned:** always  **Sample:** `{"install_state": ["Compatibility check is done:", "Module  bootable          Impact  Install-type  Reason", "------  --------  --------------  ------------  ------", "     1       yes  non-disruptive         reset  ", "Images will be upgraded according to following table:", "Module       Image                  Running-Version(pri:alt)           New-Version  Upg-Required", "------  ----------  ----------------------------------------  --------------------  ------------", "     1        nxos                               7.0(3)I6(1)           7.0(3)I7(1)           yes", "     1        bios                        v4.4.0(07/12/2017)    v4.4.0(07/12/2017)            no"]}` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbibo (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
