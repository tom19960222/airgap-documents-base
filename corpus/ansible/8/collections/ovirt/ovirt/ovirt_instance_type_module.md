---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirt_instance_type module – Module to manage Instance Types in oVirt/RHV"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirt_instance_type_module.html
fetched_at: 2026-07-28T02:49:36+00:00
---
# ovirt.ovirt.ovirt_instance_type module – Module to manage Instance Types in oVirt/RHV

> **Note:**
>
> This module is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
> You need further requirements to be able to use this module,
> see [Requirements](ovirt_instance_type_module.md#ansible-collections-ovirt-ovirt-ovirt-instance-type-module-requirements) for details.
>
> To use it in a playbook, specify: `ovirt.ovirt.ovirt_instance_type`.

New in ovirt.ovirt 1.0.0

- [Synopsis](ovirt_instance_type_module.md#synopsis)
- [Requirements](ovirt_instance_type_module.md#requirements)
- [Parameters](ovirt_instance_type_module.md#parameters)
- [Notes](ovirt_instance_type_module.md#notes)
- [Examples](ovirt_instance_type_module.md#examples)
- [Return Values](ovirt_instance_type_module.md#return-values)

## [Synopsis](ovirt_instance_type_module.md#id1)

- This module manages whole lifecycle of the Instance Type in oVirt/RHV.

## [Requirements](ovirt_instance_type_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- ovirt-engine-sdk-python >= 4.4.0

## [Parameters](ovirt_instance_type_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary / required | Dictionary with values needed to create HTTP/HTTPS connection to oVirt: |
| **ca_file**  string | A PEM file containing the trusted CA certificates.  The certificate presented by the server will be verified using these CA certificates.  If `ca_file` parameter is not set, system wide CA certificate store is used.  Default value is set by `OVIRT_CAFILE` environment variable. |
| **compress**  boolean | Flag indicating if compression is used for connection.  **Choices:**   - `false` - `true` ← (default) |
| **headers**  dictionary | Dictionary of HTTP headers to be added to each API call. |
| **hostname**  string | A string containing the hostname of the server, usually something like `*server.example.com*`.  Default value is set by `OVIRT_HOSTNAME` environment variable.  Either `url` or `hostname` is required. |
| **insecure**  boolean | A boolean flag that indicates if the server TLS certificate and host name should be checked.  **Choices:**   - `false` ← (default) - `true` |
| **kerberos**  boolean | A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.  **Choices:**   - `false` - `true` |
| **password**  string | The password of the user.  Default value is set by `OVIRT_PASSWORD` environment variable. |
| **timeout**  integer | Number of seconds to wait for response. |
| **token**  string | Token to be used instead of login with username/password.  Default value is set by `OVIRT_TOKEN` environment variable. |
| **url**  string | A string containing the API URL of the server, usually something like `*https://server.example.com/ovirt-engine/api*`.  Default value is set by `OVIRT_URL` environment variable.  Either `url` or `hostname` is required. |
| **username**  string | The name of the user, something like *admin@internal*.  Default value is set by `OVIRT_USERNAME` environment variable. |
| **ballooning_enabled**  boolean | If *true*, use memory ballooning.  Memory balloon is a guest device, which may be used to re-distribute / reclaim the host memory based on instance type needs in a dynamic way. In this way it’s possible to create memory over commitment states.  **Choices:**   - `false` - `true` |
| **boot_devices**  list / elements=string | List of boot devices which should be used to boot. For example `[ cdrom, hd ]`.  Default value is set by oVirt/RHV engine.  **Choices:**   - `"cdrom"` - `"hd"` - `"network"` |
| **cpu_cores**  integer | Number of virtual CPUs cores of the Instance Type.  Default value is set by oVirt/RHV engine. |
| **cpu_mode**  string | CPU mode of the instance type. It can be some of the following: *host_passthrough*, *host_model* or *custom*.  For *host_passthrough* CPU type you need to set `placement_policy` to *pinned*.  If no value is passed, default value is set by oVirt/RHV engine. |
| **cpu_pinning**  list / elements=dictionary | CPU Pinning topology to map instance type CPU to host CPU.  CPU Pinning topology is a list of dictionary which can have following values: |
| **cpu**  string | Number of the host CPU. |
| **vcpu**  string | Number of the instance type CPU. |
| **cpu_sockets**  integer | Number of virtual CPUs sockets of the Instance Type.  Default value is set by oVirt/RHV engine. |
| **cpu_threads**  integer | Number of virtual CPUs sockets of the Instance Type.  Default value is set by oVirt/RHV engine. |
| **description**  string | Description of the instance type. |
| **fetch_nested**  boolean | If *True* the module will fetch additional data from the API.  It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying `nested_attributes`.  **Choices:**   - `false` ← (default) - `true` |
| **graphical_console**  dictionary | Assign graphical console to the instance type.  Graphical console is a dictionary which can have following values:  `headless_mode` - If *true* disable the graphics console for this instance type.  `protocol` - Graphical protocol, a list of *spice*, *vnc*, or both. |
| **high_availability**  boolean | If *yes* Instance Type will be set as highly available.  If *no* Instance Type won’t be set as highly available.  If no value is passed, default value is set by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **high_availability_priority**  integer | Indicates the priority of the instance type inside the run and migration queues. Instance Type with higher priorities will be started and migrated before instance types with lower priorities. The value is an integer between 0 and 100. The higher the value, the higher the priority.  If no value is passed, default value is set by oVirt/RHV engine. |
| **host**  string | Specify host where Instance Type should be running. By default the host is chosen by engine scheduler.  This parameter is used only when `state` is *running* or *present*. |
| **id**  string | ID of the Instance Type to manage. |
| **io_threads**  integer | Number of IO threads used by instance type. *0* means IO threading disabled. |
| **memory**  string | Amount of memory of the Instance Type. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **memory_guaranteed**  string | Amount of minimal guaranteed memory of the Instance Type. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  `memory_guaranteed` parameter can’t be lower than `memory` parameter.  Default value is set by engine. |
| **memory_max**  string | Upper bound of instance type memory up to which memory hot-plug can be performed. Prefix uses IEC 60027-2 standard (for example 1GiB, 1024MiB).  Default value is set by engine. |
| **name**  string | Name of the Instance Type to manage.  If instance type don’t exists `name` is required. Otherwise `id` or `name` can be used. |
| **nested_attributes**  list / elements=string | Specifies list of the attributes which should be fetched from the API.  This parameter apply only when `fetch_nested` is *true*. |
| **nics**  list / elements=dictionary | List of NICs, which should be attached to Virtual Machine. NIC is described by following dictionary.  NOTE - This parameter is used only when `state` is *running* or *present* and is able to only create NICs. To manage NICs of the instance type in more depth please use [ovirt.ovirt.ovirt_nic](ovirt_nic_module.md#ansible-collections-ovirt-ovirt-ovirt-nic-module) module instead. |
| **interface**  string | Type of the network interface.  **Choices:**   - `"virtio"` ← (default) - `"e1000"` - `"rtl8139"` |
| **mac_address**  string | Custom MAC address of the network interface, by default it’s obtained from MAC pool. |
| **name**  string | Name of the NIC. |
| **profile_name**  string | Profile name where NIC should be attached. |
| **operating_system**  string | Operating system of the Instance Type, for example ‘rhel_8x64’.  Default value is set by oVirt/RHV engine.  Use the [ovirt.ovirt.ovirt_vm_os_info](ovirt_vm_os_info_module.md#ansible-collections-ovirt-ovirt-ovirt-vm-os-info-module) module to obtain the current list. |
| **placement_policy**  string | The configuration of the instance type’s placement policy.  Placement policy can be one of the following values:  `migratable` - Allow manual and automatic migration.  `pinned` - Do not allow migration.  `user_migratable` - Allow manual migration only.  If no value is passed, default value is set by oVirt/RHV engine. |
| **poll_interval**  integer | Number of the seconds the module waits until another poll request on entity status is sent.  **Default:** `3` |
| **rng_bytes**  integer | Number of bytes allowed to consume per period. |
| **rng_device**  string | Random number generator (RNG). You can choose of one the following devices *urandom*, *random* or *hwrng*.  In order to select *hwrng*, you must have it enabled on cluster first.  /dev/urandom is used for cluster version >= 4.1, and /dev/random for cluster version <= 4.0 |
| **rng_period**  integer | Duration of one period in milliseconds. |
| **serial_console**  boolean | *True* enable VirtIO serial console, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **smartcard_enabled**  boolean | If *true*, use smart card authentication.  **Choices:**   - `false` - `true` |
| **soundcard_enabled**  boolean | If *true*, the sound card is added to the instance type.  **Choices:**   - `false` - `true` |
| **state**  string | Should the Instance Type be present/absent.  *present* state will create/update instance type and don’t change its state if it already exists.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The amount of time in seconds the module should wait for the instance to get into desired state.  **Default:** `180` |
| **usb_support**  boolean | *True* enable USB support, *False* to disable it. By default is chosen by oVirt/RHV engine.  **Choices:**   - `false` - `true` |
| **virtio_scsi**  boolean | If *true*, virtio scsi will be enabled.  **Choices:**   - `false` - `true` |
| **wait**  boolean | `yes` if the module should wait for the entity to get into desired state.  **Choices:**   - `false` - `true` ← (default) |
| **watchdog**  dictionary | Assign watchdog device for the instance type.  Watchdogs is a dictionary which can have following values:  `model` - Model of the watchdog device. For example: *i6300esb*, *diag288* or *null*.  `action` - Watchdog action to be performed when watchdog is triggered. For example: *none*, *reset*, *poweroff*, *pause* or *dump*. |

## [Notes](ovirt_instance_type_module.md#id4)

> **Note:**
>
> - In order to use this module you have to install oVirt Python SDK. To ensure it’s installed with correct version you can create the following task: *pip: name=ovirt-engine-sdk-python version=4.4.0*

## [Examples](ovirt_instance_type_module.md#id5)

```yaml+jinja
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create instance type
- name: Create instance type
  ovirt.ovirt.ovirt_instance_type:
    state: present
    name: myit
    rng_device: hwrng
    rng_bytes: 200
    rng_period: 200
    soundcard_enabled: true
    virtio_scsi: true
    boot_devices:
      - network

# Remove instance type
- ovirt.ovirt.ovirt_instance_type:
    state: absent
    name: myit

# Create instance type with predefined memory and cpu limits.
- ovirt.ovirt.ovirt_instance_type:
    state: present
    name: myit
    memory: 2GiB
    cpu_cores: 2
    cpu_sockets: 2
    nics:
      - name: nic1

# Enable usb support and serial console
- ovirt.ovirt.ovirt_instance_type:
    name: myit
    usb_support: True
    serial_console: True

# Use graphical console with spice and vnc
- name: Create a instance type that has the console configured for both Spice and VNC
  ovirt.ovirt.ovirt_instance_type:
    name: myit
    graphical_console:
      protocol:
        - spice
        - vnc
```

## [Return Values](ovirt_instance_type_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the instance type which is managed  **Returned:** On success if instance type is found.  **Sample:** `"7de90f31-222c-436c-a1ca-7e655bd5b60c"` |
| **instancetype**  dictionary | Dictionary of all the instance type attributes. instance type attributes can be found on your oVirt/RHV instance at following url: <http://ovirt.github.io/ovirt-engine-api-model/master/#types/instance_type>.  **Returned:** On success if instance type is found. |

### Authors

- Martin Necas (@mnecas)
- Ondra Machacek (@machacekondra)

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
