---
collection: ansible
version: "6"
title: "openstack.cloud.quota module – Manage OpenStack Quotas"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/quota_module.html
fetched_at: 2026-07-28T00:16:59+00:00
---
# openstack.cloud.quota module – Manage OpenStack Quotas

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](quota_module.md#ansible-collections-openstack-cloud-quota-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.quota`.

- [Synopsis](quota_module.md#synopsis)
- [Requirements](quota_module.md#requirements)
- [Parameters](quota_module.md#parameters)
- [Notes](quota_module.md#notes)
- [Examples](quota_module.md#examples)
- [Return Values](quota_module.md#return-values)

## [Synopsis](quota_module.md#id1)

- Manage OpenStack Quotas. Quotas can be created, updated or deleted using this module. A quota will be updated if matches an existing project and is present.

## [Requirements](quota_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.4.0
- openstacksdk >= 0.13.0
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](quota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **backup_gigabytes**  integer | Maximum size of backups in GB’s. |
| **backups**  integer | Maximum number of backups allowed. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **cores**  integer | Maximum number of CPU’s per project. |
| **fixed_ips**  integer | Number of fixed IP’s to allow. |
| **floating_ips**  aliases: compute_floating_ips  integer | Number of floating IP’s to allow in Compute. |
| **floatingip**  aliases: network_floating_ips  integer | Number of floating IP’s to allow in Network. |
| **gigabytes**  integer | Maximum volume storage allowed for project. |
| **gigabytes_types**  dictionary | Per driver volume storage quotas. Keys should be prefixed with `gigabytes_` values should be ints. |
| **injected_file_size**  integer | Maximum file size in bytes. |
| **injected_files**  integer | Number of injected files to allow. |
| **injected_path_size**  integer | Maximum path size. |
| **instances**  integer | Maximum number of instances allowed. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **key_pairs**  integer | Number of key pairs to allow. |
| **loadbalancer**  integer | Number of load balancers to allow. |
| **metadata_items**  integer | Number of metadata items allowed per instance. |
| **name**  string / required | Name of the OpenStack Project to manage. |
| **network**  integer | Number of networks to allow. |
| **per_volume_gigabytes**  integer | Maximum size in GB’s of individual volumes. |
| **pool**  integer | Number of load balancer pools to allow. |
| **port**  integer | Number of Network ports to allow, this needs to be greater than the instances limit. |
| **project**  integer | Unused, kept for compatability |
| **properties**  integer | Number of properties to allow. |
| **ram**  integer | Maximum amount of ram in MB to allow. |
| **rbac_policy**  integer | Number of policies to allow. |
| **region_name**  string | Name of the region. |
| **router**  integer | Number of routers to allow. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_group**  integer | Number of security groups to allow. |
| **security_group_rule**  integer | Number of rules per security group to allow. |
| **server_group_members**  integer | Number of server group members to allow. |
| **server_groups**  integer | Number of server groups to allow. |
| **snapshots**  integer | Number of snapshots to allow. |
| **snapshots_types**  dictionary | Per-driver volume snapshot quotas. Keys should be prefixed with `snapshots_` values should be ints. |
| **state**  string | A value of present sets the quota and a value of absent resets the quota to system defaults.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subnet**  integer | Number of subnets to allow. |
| **subnetpool**  integer | Number of subnet pools to allow. |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **volumes**  integer | Number of volumes to allow. |
| **volumes_types**  dictionary | Per-driver volume count quotas. Keys should be prefixed with `volumes_` values should be ints. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](quota_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](quota_module.md#id5)

```yaml+jinja
# List a Project Quota
- openstack.cloud.quota:
    cloud: mycloud
    name: demoproject

# Set a Project back to the defaults
- openstack.cloud.quota:
    cloud: mycloud
    name: demoproject
    state: absent

# Update a Project Quota for cores
- openstack.cloud.quota:
    cloud: mycloud
    name: demoproject
    cores: 100

# Update a Project Quota
- openstack.cloud.quota:
    name: demoproject
    cores: 1000
    volumes: 20
    volumes_type:
      - volume_lvm: 10

# Complete example based on list of projects
- name: Update quotas
  openstack.cloud.quota:
    name: "{{ item.name }}"
    backup_gigabytes: "{{ item.backup_gigabytes }}"
    backups: "{{ item.backups }}"
    cores: "{{ item.cores }}"
    fixed_ips: "{{ item.fixed_ips }}"
    floating_ips: "{{ item.floating_ips }}"
    floatingip: "{{ item.floatingip }}"
    gigabytes: "{{ item.gigabytes }}"
    injected_file_size: "{{ item.injected_file_size }}"
    injected_files: "{{ item.injected_files }}"
    injected_path_size: "{{ item.injected_path_size }}"
    instances: "{{ item.instances }}"
    key_pairs: "{{ item.key_pairs }}"
    loadbalancer: "{{ item.loadbalancer }}"
    metadata_items: "{{ item.metadata_items }}"
    per_volume_gigabytes: "{{ item.per_volume_gigabytes }}"
    pool: "{{ item.pool }}"
    port: "{{ item.port }}"
    properties: "{{ item.properties }}"
    ram: "{{ item.ram }}"
    security_group_rule: "{{ item.security_group_rule }}"
    security_group: "{{ item.security_group }}"
    server_group_members: "{{ item.server_group_members }}"
    server_groups: "{{ item.server_groups }}"
    snapshots: "{{ item.snapshots }}"
    volumes: "{{ item.volumes }}"
    volumes_types:
      volumes_lvm: "{{ item.volumes_lvm }}"
    snapshots_types:
      snapshots_lvm: "{{ item.snapshots_lvm }}"
    gigabytes_types:
      gigabytes_lvm: "{{ item.gigabytes_lvm }}"
  with_items:
    - "{{ projects }}"
  when: item.state == "present"
```

## [Return Values](quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **openstack_quotas**  dictionary | Dictionary describing the project quota.  Returned: Regardless if changes where made or not  Sample: `{"openstack_quotas": {"compute": {"cores": 150, "fixed_ips": -1, "floating_ips": 10, "injected_file_content_bytes": 10240, "injected_file_path_bytes": 255, "injected_files": 5, "instances": 100, "key_pairs": 100, "metadata_items": 128, "ram": 153600, "security_group_rules": 20, "security_groups": 10, "server_group_members": 10, "server_groups": 10}, "network": {"floatingip": 50, "loadbalancer": 10, "network": 10, "pool": 10, "port": 160, "rbac_policy": 10, "router": 10, "security_group": 10, "security_group_rule": 100, "subnet": 10, "subnetpool": -1}, "volume": {"backup_gigabytes": 1000, "backups": 10, "gigabytes": 1000, "gigabytes_lvm": -1, "per_volume_gigabytes": -1, "snapshots": 10, "snapshots_lvm": -1, "volumes": 10, "volumes_lvm": -1}}}` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
