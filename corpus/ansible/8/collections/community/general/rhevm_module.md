---
collection: ansible
version: "8"
title: "community.general.rhevm module – RHEV/oVirt automation"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rhevm_module.html
fetched_at: 2026-07-28T01:49:57+00:00
---
# community.general.rhevm module – RHEV/oVirt automation

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
> see [Requirements](rhevm_module.md#ansible-collections-community-general-rhevm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rhevm`.

- [Synopsis](rhevm_module.md#synopsis)
- [Requirements](rhevm_module.md#requirements)
- [Parameters](rhevm_module.md#parameters)
- [Attributes](rhevm_module.md#attributes)
- [Examples](rhevm_module.md#examples)
- [Return Values](rhevm_module.md#return-values)

## [Synopsis](rhevm_module.md#id1)

- This module only supports oVirt/RHEV version 3.
- A newer module [ovirt.ovirt.ovirt_vm](../../ovirt/ovirt/ovirt_vm_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-module) supports oVirt/RHV version 4.
- Allows you to create/remove/update or powermanage virtual machines on a RHEV/oVirt platform.

Aliases: cloud.misc.rhevm

## [Requirements](rhevm_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovirtsdk

## [Parameters](rhevm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **boot_order**  list / elements=string | This option uses complex arguments and is a list of items that specify the bootorder.  **Default:** `["hd", "network"]` |
| **cd_drive**  string | The CD you wish to have mounted on the VM when `state=cd`. |
| **cluster**  string | The RHEV/oVirt cluster in which you want you VM to start.  **Default:** `""` |
| **cpu_share**  integer | This parameter is used to configure the CPU share.  **Default:** `0` |
| **datacenter**  string | The RHEV/oVirt datacenter in which you want you VM to start.  **Default:** `"Default"` |
| **del_prot**  boolean | This option sets the delete protection checkbox.  **Choices:**   - `false` - `true` ← (default) |
| **disks**  list / elements=string | This option uses complex arguments and is a list of disks with the options name, size and domain. |
| **ifaces**  aliases: interfaces, nics  list / elements=string | This option uses complex arguments and is a list of interfaces with the options name and vlan. |
| **image**  string | The template to use for the VM. |
| **insecure_api**  boolean | A boolean switch to make a secure or insecure connection to the server.  **Choices:**   - `false` ← (default) - `true` |
| **mempol**  integer | The minimum amount of memory you wish to reserve for this system.  **Default:** `1` |
| **name**  string | The name of the VM. |
| **osver**  string | The operating system option in RHEV/oVirt.  **Default:** `"rhel_6x64"` |
| **password**  string / required | The password for user authentication. |
| **port**  integer | The port on which the API is reachable.  **Default:** `443` |
| **server**  string | The name/IP of your RHEV-m/oVirt instance.  **Default:** `"127.0.0.1"` |
| **state**  string | This serves to create/remove/update or powermanage your VM.  **Choices:**   - `"absent"` - `"cd"` - `"down"` - `"info"` - `"ping"` - `"present"` ← (default) - `"restarted"` - `"up"` |
| **timeout**  integer | The timeout you wish to define for power actions.  When `state=up`.  When `state=down`.  When `state=restarted`. |
| **type**  string | To define if the VM is a server or desktop.  **Choices:**   - `"desktop"` - `"host"` - `"server"` ← (default) |
| **user**  string | The user to authenticate with.  **Default:** `"admin@internal"` |
| **vm_ha**  boolean | To make your VM High Available.  **Choices:**   - `false` - `true` ← (default) |
| **vmcpu**  integer | The number of CPUs you want in your VM.  **Default:** `2` |
| **vmhost**  string | The host you wish your VM to run on. |
| **vmmem**  integer | The amount of memory you want your VM to use (in GB).  **Default:** `1` |

## [Attributes](rhevm_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](rhevm_module.md#id5)

```yaml+jinja
- name: Basic get info from VM
  community.general.rhevm:
    server: rhevm01
    user: '{{ rhev.admin.name }}'
    password: '{{ rhev.admin.pass }}'
    name: demo
    state: info

- name: Basic create example from image
  community.general.rhevm:
    server: rhevm01
    user: '{{ rhev.admin.name }}'
    password: '{{ rhev.admin.pass }}'
    name: demo
    cluster: centos
    image: centos7_x64
    state: present

- name: Power management
  community.general.rhevm:
    server: rhevm01
    user: '{{ rhev.admin.name }}'
    password: '{{ rhev.admin.pass }}'
    cluster: RH
    name: uptime_server
    image: centos7_x64
    state: down

- name: Multi disk, multi nic create example
  community.general.rhevm:
    server: rhevm01
    user: '{{ rhev.admin.name }}'
    password: '{{ rhev.admin.pass }}'
    cluster: RH
    name: server007
    type: server
    vmcpu: 4
    vmmem: 2
    ifaces:
    - name: eth0
      vlan: vlan2202
    - name: eth1
      vlan: vlan36
    - name: eth2
      vlan: vlan38
    - name: eth3
      vlan: vlan2202
    disks:
    - name: root
      size: 10
      domain: ssd-san
    - name: swap
      size: 10
      domain: 15kiscsi-san
    - name: opt
      size: 10
      domain: 15kiscsi-san
    - name: var
      size: 10
      domain: 10kiscsi-san
    - name: home
      size: 10
      domain: sata-san
    boot_order:
    - network
    - hd
    state: present

- name: Add a CD to the disk cd_drive
  community.general.rhevm:
    user: '{{ rhev.admin.name }}'
    password: '{{ rhev.admin.pass }}'
    name: server007
    cd_drive: rhev-tools-setup.iso
    state: cd

- name: New host deployment + host network configuration
  community.general.rhevm:
    password: '{{ rhevm.admin.pass }}'
    name: ovirt_node007
    type: host
    cluster: rhevm01
    ifaces:
    - name: em1
    - name: em2
    - name: p3p1
      ip: 172.31.224.200
      netmask: 255.255.254.0
    - name: p3p2
      ip: 172.31.225.200
      netmask: 255.255.254.0
    - name: bond0
      bond:
      - em1
      - em2
      network: rhevm
      ip: 172.31.222.200
      netmask: 255.255.255.0
      management: true
    - name: bond0.36
      network: vlan36
      ip: 10.2.36.200
      netmask: 255.255.254.0
      gateway: 10.2.36.254
    - name: bond0.2202
      network: vlan2202
    - name: bond0.38
      network: vlan38
    state: present
```

## [Return Values](rhevm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm**  dictionary | Returns all of the VMs variables and execution.  **Returned:** always  **Sample:** `{"boot_order": ["hd", "network"], "changed": true, "changes": ["Delete Protection"], "cluster": "C1", "cpu_share": "0", "created": false, "datacenter": "Default", "del_prot": true, "disks": [{"domain": "ssd-san", "name": "OS", "size": 40}], "eth0": "00:00:5E:00:53:00", "eth1": "00:00:5E:00:53:01", "eth2": "00:00:5E:00:53:02", "exists": true, "failed": false, "ifaces": [{"name": "eth0", "vlan": "Management"}, {"name": "eth1", "vlan": "Internal"}, {"name": "eth2", "vlan": "External"}], "image": false, "mempol": "0", "msg": ["VM exists", "cpu_share was already set to 0", "VM high availability was already set to True", "The boot order has already been set", "VM delete protection has been set to True", "Disk web2_Disk0_OS already exists", "The VM starting host was already set to host416"], "name": "web2", "type": "server", "uuid": "4ba5a1be-e60b-4368-9533-920f156c817b", "vm_ha": true, "vmcpu": "4", "vmhost": "host416", "vmmem": "16"}` |

### Authors

- Timothy Vandenbrande (@TimothyVandenbrande)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
