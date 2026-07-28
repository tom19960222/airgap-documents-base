---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_instance module – Manages instances and virtual machines on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_instance_module.html
fetched_at: 2026-07-28T00:15:28+00:00
---
# ngine_io.cloudstack.cs_instance module – Manages instances and virtual machines on Apache CloudStack based clouds.

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
> see [Requirements](cs_instance_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_instance`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_instance_module.md#synopsis)
- [Requirements](cs_instance_module.md#requirements)
- [Parameters](cs_instance_module.md#parameters)
- [Notes](cs_instance_module.md#notes)
- [Examples](cs_instance_module.md#examples)
- [Return Values](cs_instance_module.md#return-values)

## [Synopsis](cs_instance_module.md#id1)

- Deploy, start, update, scale, restart, restore, stop and destroy instances.

## [Requirements](cs_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the instance is related to. |
| **affinity_groups**  aliases: affinity_group  list / elements=string | Affinity groups names to be applied to the new instance. |
| **allow_root_disk_shrink**  boolean | Enables a volume shrinkage when the new size is smaller than the old one.  Choices:   - `false` ← (default) - `true` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cluster**  string  added in ngine_io.cloudstack 2.3.0 | Cluster on which an instance should be deployed or started on.  Only considered when *state=started* or instance is running.  Requires root admin privileges. |
| **cpu**  integer | The number of CPUs to allocate to the instance, used with custom service offerings |
| **cpu_speed**  integer | The clock speed/shares allocated to the instance, used with custom service offerings |
| **details**  dictionary | Map to specify custom parameters. |
| **disk_offering**  string | Name of the disk offering to be used. |
| **disk_size**  integer | Disk size in GByte required if deploying instance from ISO. |
| **display_name**  string | Custom display name of the instances.  Display name will be set to *name* if not specified.  Either *name* or *display_name* is required. |
| **domain**  string | Domain the instance is related to. |
| **force**  boolean | Force stop/start the instance if required to apply changes, otherwise a running instance will not be changed.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Group in where the new instance should be in. |
| **host**  string | Host on which an instance should be deployed or started on.  Only considered when *state=started* or instance is running.  Requires root admin privileges. |
| **hypervisor**  string | Name the hypervisor to be used for creating the new instance.  Relevant when using *state=present*, but only considered if not set on ISO/template.  If not set or found on ISO/template, first found hypervisor will be used.  Possible values are `KVM`, `VMware`, `BareMetal`, `XenServer`, `LXC`, `HyperV`, `UCS`, `OVM`, `Simulator`. |
| **ip6_address**  string | IPv6 address for default instance’s network. |
| **ip_address**  string | IPv4 address for default instance’s network during creation. |
| **ip_to_networks**  aliases: ip_to_network  list / elements=dictionary | List of mappings in the form *{‘network’: NetworkName, ‘ip’: 1.2.3.4}*  Mutually exclusive with *networks* option. |
| **iso**  string | Name or id of the ISO to be used for creating the new instance.  Required when using *state=present*.  Mutually exclusive with *template* option. |
| **keyboard**  string | Keyboard device type for the instance.  Choices:   - `"de"` - `"de-ch"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"fr-ch"` - `"is"` - `"it"` - `"jp"` - `"nl-be"` - `"no"` - `"pt"` - `"uk"` - `"us"` |
| **memory**  integer | The memory allocated to the instance, used with custom service offerings |
| **name**  string | Host name of the instance. `name` can only contain ASCII letters.  Name will be generated (UUID) by CloudStack if not specified and can not be changed afterwards.  Either `name` or `display_name` is required. |
| **networks**  aliases: network  list / elements=string | List of networks to use for the new instance. |
| **pod**  string  added in ngine_io.cloudstack 2.3.0 | Pod on which an instance should be deployed or started on.  Only considered when *state=started* or instance is running.  Requires root admin privileges. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the instance to be deployed in. |
| **root_disk_size**  integer | Root disk size in GByte required if deploying instance with KVM hypervisor and want resize the root disk size at startup (needs CloudStack >= 4.4, cloud-initramfs-growroot installed and enabled in the template). |
| **security_groups**  aliases: security_group  list / elements=string | List of security groups the instance to be applied to. |
| **service_offering**  string | Name or id of the service offering of the new instance.  If not set, first found service offering is used. |
| **ssh_key**  string | Name of the SSH key to be deployed on the new instance. |
| **state**  string | State of the instance.  Choices:   - `"deployed"` - `"started"` - `"stopped"` - `"restarted"` - `"restored"` - `"destroyed"` - `"expunged"` - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys `key` and `value`.  If you want to delete all tags, set a empty list e.g. *tags: []*. |
| **template**  string | Name, display text or id of the template to be used for creating the new instance.  Required when using *state=present*.  Mutually exclusive with *iso* option. |
| **template_filter**  aliases: iso_filter  string | Name of the filter used to search for the template or iso.  Used for params *iso* or *template* on *state=present*.  Choices:   - `"all"` - `"featured"` - `"self"` - `"selfexecutable"` - `"sharedexecutable"` - `"executable"` ← (default) - `"community"` |
| **user_data**  string | Optional data (ASCII) that can be sent to the instance upon a successful deployment.  The data will be automatically base64 encoded.  Consider switching to HTTP_POST by using *CLOUDSTACK_METHOD=post* to increase the HTTP_GET size limit of 2KB to 32 KB. |
| **zone**  string / required | Name of the zone in which the instance should be deployed. |

## [Notes](cs_instance_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_instance_module.md#id5)

```yaml+jinja
# NOTE: Names of offerings and ISOs depending on the CloudStack configuration.
- name: create a instance from an ISO
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    iso: Linux Debian 7 64-bit
    hypervisor: VMware
    project: Integration
    zone: ch-zrh-ix-01
    service_offering: 1cpu_1gb
    disk_offering: PerfPlus Storage
    disk_size: 20
    networks:
      - Server Integration
      - Sync Integration
      - Storage Integration

- name: for changing a running instance, use the 'force' parameter
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    zone: zone01
    display_name: web-vm-01.example.com
    iso: Linux Debian 7 64-bit
    service_offering: 2cpu_2gb
    force: yes

# NOTE: user_data can be used to kickstart the instance using cloud-init yaml config.
- name: create or update a instance on Exoscale's public cloud using display_name.
  ngine_io.cloudstack.cs_instance:
    display_name: web-vm-1
    zone: zone01
    template: Linux Debian 7 64-bit
    service_offering: Tiny
    ssh_key: john@example.com
    tags:
      - key: admin
        value: john
      - key: foo
        value: bar
    user_data: |
        #cloud-config
        packages:
          - nginx

- name: create an instance with multiple interfaces specifying the IP addresses
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    zone: zone01
    template: Linux Debian 7 64-bit
    service_offering: Tiny
    ip_to_networks:
      - network: NetworkA
        ip: 10.1.1.1
      - network: NetworkB
        ip: 192.0.2.1

- name: ensure an instance is stopped
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    zone: zone01
    state: stopped

- name: ensure an instance is running
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    zone: zone01
    state: started

- name: remove an instance
  ngine_io.cloudstack.cs_instance:
    name: web-vm-1
    zone: zone01
    state: absent
```

## [Return Values](cs_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the instance is related to.  Returned: success  Sample: `"example account"` |
| **affinity_groups**  list / elements=string | Affinity groups the instance is in.  Returned: success  Sample: `["[ \"webservers\" ]"]` |
| **created**  string | Date of the instance was created.  Returned: success  Sample: `"2014-12-01T14:57:57+0100"` |
| **default_ip**  string | Default IP address of the instance.  Returned: success  Sample: `"10.23.37.42"` |
| **default_ip6**  string | Default IPv6 address of the instance.  Returned: if available  Sample: `"2a04:c43:c00:a07:4b4:beff:fe00:74"` |
| **display_name**  string | Display name of the instance.  Returned: success  Sample: `"web-01"` |
| **domain**  string | Domain the instance is related to.  Returned: success  Sample: `"example domain"` |
| **group**  string | Group name of the instance is related.  Returned: success  Sample: `"web"` |
| **host**  string | Hostname of hypervisor an instance is running on.  Returned: success and instance is running  Sample: `"host-01.example.com"` |
| **hypervisor**  string | Hypervisor related to this instance.  Returned: success  Sample: `"KVM"` |
| **id**  string | UUID of the instance.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **instance_name**  string | Internal name of the instance (ROOT admin only).  Returned: success  Sample: `"i-44-3992-VM"` |
| **iso**  string | Name of ISO the instance was deployed with.  Returned: if available  Sample: `"Debian-8-64bit"` |
| **name**  string | Name of the instance.  Returned: success  Sample: `"web-01"` |
| **password**  string | The password of the instance if exists.  Returned: if available  Sample: `"Ge2oe7Do"` |
| **password_enabled**  boolean | True if password setting is enabled.  Returned: success  Sample: `true` |
| **project**  string | Name of project the instance is related to.  Returned: success  Sample: `"Production"` |
| **public_ip**  string | Public IP address with instance via static NAT rule.  Returned: if available  Sample: `"1.2.3.4"` |
| **security_groups**  list / elements=string | Security groups the instance is in.  Returned: success  Sample: `["[ \"default\" ]"]` |
| **service_offering**  string | Name of the service offering the instance has.  Returned: success  Sample: `"2cpu_2gb"` |
| **ssh_key**  string | Name of SSH key deployed to instance.  Returned: if available  Sample: `"key@work"` |
| **state**  string | State of the instance.  Returned: success  Sample: `"Running"` |
| **tags**  list / elements=string | List of resource tags associated with the instance.  Returned: success  Sample: `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **template**  string | Name of template the instance was deployed with.  Returned: success  Sample: `"Linux Debian 9 64-bit"` |
| **template_display_text**  string | Display text of template the instance was deployed with.  Returned: success  Sample: `"Linux Debian 9 64-bit 200G Disk (2017-10-08-622866)"` |
| **user-data**  string | Optional data sent to the instance.  Returned: success  Sample: `"VXNlciBkYXRhIGV4YW1wbGUK"` |
| **zone**  string | Name of zone the instance is in.  Returned: success  Sample: `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
