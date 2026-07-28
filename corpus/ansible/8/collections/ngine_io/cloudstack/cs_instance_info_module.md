---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_instance_info module – Gathering information from the API of instances from Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_instance_info_module.html
fetched_at: 2026-07-28T02:45:48+00:00
---
# ngine_io.cloudstack.cs_instance_info module – Gathering information from the API of instances from Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_instance_info_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_instance_info`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_instance_info_module.md#synopsis)
- [Requirements](cs_instance_info_module.md#requirements)
- [Parameters](cs_instance_info_module.md#parameters)
- [Notes](cs_instance_info_module.md#notes)
- [Examples](cs_instance_info_module.md#examples)
- [Return Values](cs_instance_info_module.md#return-values)

## [Synopsis](cs_instance_info_module.md#id1)

- Gathering information from the API of an instance.

Aliases: cs_instance_facts

## [Requirements](cs_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the instance is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the instance is related to. |
| **host**  string  *added in ngine_io.cloudstack 2.2.0* | Filter by host name. |
| **name**  string | Name or display name of the instance.  If not specified, all instances are returned |
| **project**  string | Project the instance is related to. |

## [Notes](cs_instance_info_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_instance_info_module.md#id5)

```yaml+jinja
- name: Gather instance information
  ngine_io.cloudstack.cs_instance_info:
    name: web-vm-1
  register: vm

- name: Show the returned results of the registered variable
  debug:
    msg: "{{ vm }}"

- name: Gather information from all instances
  ngine_io.cloudstack.cs_instance_info:
  register: vms

- name: Show information on all instances
  debug:
    msg: "{{ vms }}"

- name: Gather information from all instances on a host
  ngine_io.cloudstack.cs_instance_info:
    host: host01.example.com
  register: vms
```

## [Return Values](cs_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  list / elements=string | A list of matching instances.  **Returned:** success |
| **account**  string | Account the instance is related to.  **Returned:** success  **Sample:** `"example account"` |
| **affinity_groups**  list / elements=string | Affinity groups the instance is in.  **Returned:** success  **Sample:** `["[ \"webservers\" ]"]` |
| **created**  string | Date of the instance was created.  **Returned:** success  **Sample:** `"2014-12-01T14:57:57+0100"` |
| **default_ip**  string | Default IP address of the instance.  **Returned:** success  **Sample:** `"10.23.37.42"` |
| **display_name**  string | Display name of the instance.  **Returned:** success  **Sample:** `"web-01"` |
| **domain**  string | Domain the instance is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **group**  string | Group name of the instance is related.  **Returned:** success  **Sample:** `"web"` |
| **host**  string | Host the instance is running on.  **Returned:** success and instance is running  **Sample:** `"host01.example.com"` |
| **hypervisor**  string | Hypervisor related to this instance.  **Returned:** success  **Sample:** `"KVM"` |
| **id**  string | UUID of the instance.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **instance_name**  string | Internal name of the instance (ROOT admin only).  **Returned:** success  **Sample:** `"i-44-3992-VM"` |
| **iso**  string | Name of ISO the instance was deployed with.  **Returned:** success  **Sample:** `"Debian-8-64bit"` |
| **name**  string | Name of the instance.  **Returned:** success  **Sample:** `"web-01"` |
| **nic**  complex | List of dictionaries of the instance nics.  **Returned:** success |
| **broadcasturi**  string | The broadcast uri of the nic.  **Returned:** success  **Sample:** `"vlan://2250"` |
| **gateway**  string | The gateway of the nic.  **Returned:** success  **Sample:** `"10.1.2.1"` |
| **id**  string | The ID of the nic.  **Returned:** success  **Sample:** `"5dc74fa3-2ec3-48a0-9e0d-6f43365336a9"` |
| **ipaddress**  string | The ip address of the nic.  **Returned:** success  **Sample:** `"10.1.2.3"` |
| **isdefault**  boolean | True if nic is default, false otherwise.  **Returned:** success  **Sample:** `true` |
| **isolationuri**  string | The isolation uri of the nic.  **Returned:** success  **Sample:** `"vlan://2250"` |
| **macaddress**  string | The mac address of the nic.  **Returned:** success  **Sample:** `"06:a2:03:00:08:12"` |
| **netmask**  string | The netmask of the nic.  **Returned:** success  **Sample:** `"255.255.255.0"` |
| **networkid**  string | The ID of the corresponding network.  **Returned:** success  **Sample:** `"432ce27b-c2bb-4e12-a88c-a919cd3a3017"` |
| **networkname**  string | The name of the corresponding network.  **Returned:** success  **Sample:** `"network1"` |
| **traffictype**  string | The traffic type of the nic.  **Returned:** success  **Sample:** `"Guest"` |
| **type**  string | The type of the network.  **Returned:** success  **Sample:** `"Shared"` |
| **password**  string | The password of the instance if exists.  **Returned:** success  **Sample:** `"Ge2oe7Do"` |
| **password_enabled**  boolean | True if password setting is enabled.  **Returned:** success  **Sample:** `true` |
| **project**  string | Name of project the instance is related to.  **Returned:** success  **Sample:** `"Production"` |
| **public_ip**  string | Public IP address with instance via static NAT rule.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **security_groups**  list / elements=string | Security groups the instance is in.  **Returned:** success  **Sample:** `["[ \"default\" ]"]` |
| **service_offering**  string | Name of the service offering the instance has.  **Returned:** success  **Sample:** `"2cpu_2gb"` |
| **ssh_key**  string | Name of SSH key deployed to instance.  **Returned:** success  **Sample:** `"key@work"` |
| **state**  string | State of the instance.  **Returned:** success  **Sample:** `"Running"` |
| **tags**  list / elements=string | List of resource tags associated with the instance.  **Returned:** success  **Sample:** `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **template**  string | Name of template the instance was deployed with.  **Returned:** success  **Sample:** `"Debian-8-64bit"` |
| **volumes**  list / elements=string | List of dictionaries of the volumes attached to the instance.  **Returned:** success  **Sample:** `["[ { name: \"ROOT-1369\"", " type: \"ROOT\"", " size: 10737418240 }", " { name: \"data01", " type: \"DATADISK\"", " size: 10737418240 } ]"]` |
| **zone**  string | Name of zone the instance is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
