---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_service_offering module – Manages service offerings on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_service_offering_module.html
fetched_at: 2026-07-28T00:15:46+00:00
---
# ngine_io.cloudstack.cs_service_offering module – Manages service offerings on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_service_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-service-offering-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_service_offering`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_service_offering_module.md#synopsis)
- [Requirements](cs_service_offering_module.md#requirements)
- [Parameters](cs_service_offering_module.md#parameters)
- [Notes](cs_service_offering_module.md#notes)
- [Examples](cs_service_offering_module.md#examples)
- [Return Values](cs_service_offering_module.md#return-values)

## [Synopsis](cs_service_offering_module.md#id1)

- Create and delete service offerings for guest and system VMs.
- Update display_text of existing service offering.

## [Requirements](cs_service_offering_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_service_offering_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cpu_number**  integer | The number of CPUs of the service offering. |
| **cpu_speed**  integer | The CPU speed of the service offering in MHz. |
| **deployment_planner**  string | The deployment planner heuristics used to deploy a VM of this offering.  If not set, the value of global config *vm.deployment.planner* is used. |
| **disk_bytes_read_rate**  aliases: bytes_read_rate  integer | Bytes read rate of the disk offering. |
| **disk_bytes_write_rate**  aliases: bytes_write_rate  integer | Bytes write rate of the disk offering. |
| **disk_iops_max**  integer | Max. iops of the compute offering. |
| **disk_iops_min**  integer | Min. iops of the compute offering. |
| **disk_iops_read_rate**  integer | IO requests read rate of the disk offering. |
| **disk_iops_write_rate**  integer | IO requests write rate of the disk offering. |
| **display_text**  string | Display text of the service offering.  If not set, *name* will be used as *display_text* while creating. |
| **domain**  string | Domain the service offering is related to.  Public for all domains and subdomains if not set. |
| **host_tags**  aliases: host_tag  list / elements=string | The host tags for this service offering. |
| **hypervisor_snapshot_reserve**  integer | Hypervisor snapshot reserve space as a percent of a volume.  Only for managed storage using Xen or VMware. |
| **is_customized**  boolean | Whether the offering is customizable or not.  Choices:   - `false` - `true` |
| **is_iops_customized**  aliases: disk_iops_customized  boolean | Whether compute offering iops is custom or not.  Choices:   - `false` - `true` |
| **is_system**  boolean | Whether it is a system VM offering or not.  Choices:   - `false` ← (default) - `true` |
| **is_volatile**  boolean | Whether the virtual machine needs to be volatile or not.  Every reboot of VM the root disk is detached then destroyed and a fresh root disk is created and attached to VM.  Choices:   - `false` - `true` |
| **limit_cpu_usage**  boolean | Restrict the CPU usage to committed service offering.  Choices:   - `false` - `true` |
| **memory**  integer | The total memory of the service offering in MB. |
| **name**  string / required | Name of the service offering. |
| **network_rate**  integer | Data transfer rate in Mb/s allowed.  Supported only for non-system offering and system offerings having *system_vm_type=domainrouter*. |
| **offer_ha**  boolean | Whether HA is set for the service offering.  Choices:   - `false` - `true` |
| **provisioning_type**  string | Provisioning type used to create volumes.  Choices:   - `"thin"` - `"sparse"` - `"fat"` |
| **service_offering_details**  list / elements=dictionary | Details for planner, used to store specific parameters.  A list of dictionaries having keys `key` and `value`. |
| **state**  string | State of the service offering.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_tags**  aliases: storage_tag  list / elements=string | The storage tags for this service offering. |
| **storage_type**  string | The storage type of the service offering.  Choices:   - `"local"` - `"shared"` |
| **system_vm_type**  string | The system VM type.  Required if *is_system=yes*.  Choices:   - `"domainrouter"` - `"consoleproxy"` - `"secondarystoragevm"` |

## [Notes](cs_service_offering_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_service_offering_module.md#id5)

```yaml+jinja
- name: Create a non-volatile compute service offering with local storage
  ngine_io.cloudstack.cs_service_offering:
    name: Micro
    display_text: Micro 512mb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 512
    host_tags: eco
    storage_type: local

- name: Create a volatile compute service offering with shared storage
  ngine_io.cloudstack.cs_service_offering:
    name: Tiny
    display_text: Tiny 1gb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 1024
    storage_type: shared
    is_volatile: yes
    host_tags: eco
    storage_tags: eco

- name: Create or update a volatile compute service offering with shared storage
  ngine_io.cloudstack.cs_service_offering:
    name: Tiny
    display_text: Tiny 1gb 1cpu
    cpu_number: 1
    cpu_speed: 2198
    memory: 1024
    storage_type: shared
    is_volatile: yes
    host_tags: eco
    storage_tags: eco

- name: Create or update a custom compute service offering
  ngine_io.cloudstack.cs_service_offering:
    name: custom
    display_text: custom compute offer
    is_customized: yes
    storage_type: shared
    host_tags: eco
    storage_tags: eco

- name: Remove a compute service offering
  ngine_io.cloudstack.cs_service_offering:
    name: Tiny
    state: absent

- name: Create or update a system offering for the console proxy
  ngine_io.cloudstack.cs_service_offering:
    name: System Offering for Console Proxy 2GB
    display_text: System Offering for Console Proxy 2GB RAM
    is_system: yes
    system_vm_type: consoleproxy
    cpu_number: 1
    cpu_speed: 2198
    memory: 2048
    storage_type: shared
    storage_tags: perf

- name: Remove a system offering
  ngine_io.cloudstack.cs_service_offering:
    name: System Offering for Console Proxy 2GB
    is_system: yes
    state: absent
```

## [Return Values](cs_service_offering_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cpu_number**  integer | Number of CPUs in the service offering  Returned: success  Sample: `4` |
| **cpu_speed**  integer | Speed of CPUs in MHz in the service offering  Returned: success  Sample: `2198` |
| **created**  string | Date the offering was created  Returned: success  Sample: `"2017-11-19T10:48:59+0000"` |
| **disk_bytes_read_rate**  integer | Bytes read rate of the service offering  Returned: success  Sample: `1000` |
| **disk_bytes_write_rate**  integer | Bytes write rate of the service offering  Returned: success  Sample: `1000` |
| **disk_iops_max**  integer | Max iops of the disk offering  Returned: success  Sample: `1000` |
| **disk_iops_min**  integer | Min iops of the disk offering  Returned: success  Sample: `500` |
| **disk_iops_read_rate**  integer | IO requests per second read rate of the service offering  Returned: success  Sample: `1000` |
| **disk_iops_write_rate**  integer | IO requests per second write rate of the service offering  Returned: success  Sample: `1000` |
| **display_text**  string | Display text of the offering  Returned: success  Sample: `"Micro 512mb 1cpu"` |
| **domain**  string | Domain the offering is into  Returned: success  Sample: `"ROOT"` |
| **host_tags**  list / elements=string | List of host tags  Returned: success  Sample: `["eco"]` |
| **id**  string | UUID of the service offering  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **is_customized**  boolean | Whether the offering is customizable or not  Returned: success  Sample: `false` |
| **is_iops_customized**  boolean | Whether the offering uses custom IOPS or not  Returned: success  Sample: `false` |
| **is_system**  boolean | Whether the offering is for system VMs or not  Returned: success  Sample: `false` |
| **is_volatile**  boolean | Whether the offering is volatile or not  Returned: success  Sample: `false` |
| **limit_cpu_usage**  boolean | Whether the CPU usage is restricted to committed service offering  Returned: success  Sample: `false` |
| **memory**  integer | Memory of the system offering  Returned: success  Sample: `512` |
| **name**  string | Name of the system offering  Returned: success  Sample: `"Micro"` |
| **network_rate**  integer | Data transfer rate in megabits per second allowed  Returned: success  Sample: `1000` |
| **offer_ha**  boolean | Whether HA support is enabled in the offering or not  Returned: success  Sample: `false` |
| **provisioning_type**  string | Provisioning type used to create volumes  Returned: success  Sample: `"thin"` |
| **service_offering_details**  dictionary | Additioanl service offering details  Returned: success  Sample: `{"pciDevice": "Group of NVIDIA Corporation GK107GL [GRID K1] GPUs", "vgpuType": "GRID K180Q"}` |
| **storage_tags**  list / elements=string | List of storage tags  Returned: success  Sample: `["eco"]` |
| **storage_type**  string | Storage type used to create volumes  Returned: success  Sample: `"shared"` |
| **system_vm_type**  string | System VM type of this offering  Returned: success  Sample: `"consoleproxy"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
