---
collection: ansible
version: "8"
title: "openstack.cloud.quota module – Manage OpenStack Quotas"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/quota_module.html
fetched_at: 2026-07-28T02:48:32+00:00
---
# openstack.cloud.quota module – Manage OpenStack Quotas

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
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

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](quota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **backup_gigabytes**  integer | Maximum size of backups in GB’s. |
| **backups**  integer | Maximum number of backups allowed. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **cores**  integer | Maximum number of CPU’s per project. |
| **fixed_ips**  integer | Number of fixed IP’s to allow.  Available until Nova API version 2.35. |
| **floating_ips**  aliases: compute_floating_ips, floatingip, network_floating_ips  integer | Number of floating IP’s to allow. |
| **gigabytes**  integer | Maximum volume storage allowed for project. |
| **groups**  integer | Number of groups that are allowed for the project |
| **injected_file_content_bytes**  aliases: injected_file_size  integer | Maximum file size in bytes.  Available until Nova API version 2.56. |
| **injected_file_path_bytes**  aliases: injected_path_size  integer | Maximum path size.  Available until Nova API version 2.56. |
| **injected_files**  integer | Number of injected files to allow.  Available until Nova API version 2.56. |
| **instances**  integer | Maximum number of instances allowed. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **key_pairs**  integer | Number of key pairs to allow. |
| **load_balancers**  aliases: loadbalancer  integer | The maximum amount of load balancers you can create |
| **metadata_items**  integer | Number of metadata items allowed per instance. |
| **name**  string / required | Name of the OpenStack Project to manage. |
| **networks**  aliases: network  integer | Number of networks to allow. |
| **per_volume_gigabytes**  integer | Maximum size in GB’s of individual volumes. |
| **pools**  aliases: pool  integer | The maximum number of pools you can create |
| **ports**  aliases: port  integer | Number of Network ports to allow, this needs to be greater than the instances limit. |
| **ram**  integer | Maximum amount of ram in MB to allow. |
| **rbac_policies**  aliases: rbac_policy  integer | Number of policies to allow. |
| **region_name**  string | Name of the region. |
| **routers**  aliases: router  integer | Number of routers to allow. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_group_rules**  aliases: security_group_rule  integer | Number of rules per security group to allow. |
| **security_groups**  aliases: security_group  integer | Number of security groups to allow. |
| **server_group_members**  integer | Number of server group members to allow. |
| **server_groups**  integer | Number of server groups to allow. |
| **snapshots**  integer | Number of snapshots to allow. |
| **state**  string | A value of `present` sets the quota and a value of `absent` resets the quota to defaults.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnet_pools**  aliases: subnetpool  integer | Number of subnet pools to allow. |
| **subnets**  aliases: subnet  integer | Number of subnets to allow. |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volumes**  integer | Number of volumes to allow. |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](quota_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](quota_module.md#id5)

```yaml+jinja
- name: Fetch current project quota
  openstack.cloud.quota:
    cloud: mycloud
    name: demoproject

- name: Reset project quota back to defaults
  openstack.cloud.quota:
    cloud: mycloud
    name: demoproject
    state: absent

- name: Change number of cores and volumes
  openstack.cloud.quota:
    cloud: mycloud
    name: demoproject
    cores: 100
    volumes: 20

- name: Update quota again
  openstack.cloud.quota:
    cloud: mycloud
    name: demo_project
    floating_ips: 5
    networks: 50
    ports: 300
    rbac_policies: 5
    routers: 5
    subnets: 5
    subnet_pools: 5
    security_group_rules: 5
    security_groups: 5
    backup_gigabytes: 500
    backups: 5
    gigabytes: 500
    groups: 1
    pools: 5
    per_volume_gigabytes: 10
    snapshots: 5
    volumes: 5
    cores: 5
    instances: 5
    key_pairs: 5
    metadata_items: 5
    ram: 5
    server_groups: 5
    server_group_members: 5
```

## [Return Values](quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **quotas**  dictionary | Dictionary describing the project quota.  **Returned:** Regardless if changes where made or not  **Sample:** `{"quotas": {"compute": {"cores": "150,", "fixed_ips": "-1,", "floating_ips": "10,", "injected_file_content_bytes": "10240,", "injected_file_path_bytes": "255,", "injected_files": "5,", "instances": "100,", "key_pairs": "100,", "metadata_items": "128,", "networks": "-1,", "ram": "153600,", "security_group_rules": "-1,", "security_groups": "-1,", "server_group_members": "10,", "server_groups": "10,"}, "network": {"floating_ips": "50,", "load_balancers": "10,", "networks": "10,", "pools": "10,", "ports": "160,", "rbac_policies": "10,", "routers": "10,", "security_group_rules": "100,", "security_groups": "10,", "subnet_pools": "-1,", "subnets": "10,"}, "volume": {"backup_gigabytes": "1000,", "backups": "10,", "gigabytes": "1000,", "groups": "10,", "per_volume_gigabytes": "-1,", "snapshots": "10,", "volumes": "10,"}}}` |
| **compute**  dictionary | Compute service quotas  **Returned:** success |
| **cores**  integer | Maximum number of CPU’s per project.  **Returned:** success |
| **injected_file_content_bytes**  integer | Maximum file size in bytes.  **Returned:** success |
| **injected_file_path_bytes**  integer | Maximum path size.  **Returned:** success |
| **injected_files**  integer | Number of injected files to allow.  **Returned:** success |
| **instances**  integer | Maximum number of instances allowed.  **Returned:** success |
| **key_pairs**  integer | Number of key pairs to allow.  **Returned:** success |
| **metadata_items**  integer | Number of metadata items allowed per instance.  **Returned:** success |
| **ram**  integer | Maximum amount of ram in MB to allow.  **Returned:** success |
| **server_group_members**  integer | Number of server group members to allow.  **Returned:** success |
| **server_groups**  integer | Number of server groups to allow.  **Returned:** success |
| **network**  dictionary | Network service quotas  **Returned:** success |
| **floating_ips**  integer | Number of floating IP’s to allow.  **Returned:** success |
| **load_balancers**  integer | The maximum amount of load balancers one can create  **Returned:** success |
| **networks**  integer | Number of networks to allow.  **Returned:** success |
| **pools**  integer | The maximum amount of pools one can create.  **Returned:** success |
| **ports**  integer | Number of Network ports to allow, this needs to be greater than the instances limit.  **Returned:** success |
| **rbac_policies**  integer | Number of policies to allow.  **Returned:** success |
| **routers**  integer | Number of routers to allow.  **Returned:** success |
| **security_group_rules**  integer | Number of rules per security group to allow.  **Returned:** success |
| **security_groups**  integer | Number of security groups to allow.  **Returned:** success |
| **subnet_pools**  integer | Number of subnet pools to allow.  **Returned:** success |
| **subnets**  integer | Number of subnets to allow.  **Returned:** success |
| **volume**  dictionary | Block storage service quotas  **Returned:** success |
| **backup_gigabytes**  integer | Maximum size of backups in GB’s.  **Returned:** success |
| **backups**  integer | Maximum number of backups allowed.  **Returned:** success |
| **gigabytes**  integer | Maximum volume storage allowed for project.  **Returned:** success |
| **groups**  integer | Number of groups that are allowed for the project  **Returned:** success |
| **per_volume_gigabytes**  integer | Maximum size in GB’s of individual volumes.  **Returned:** success |
| **snapshots**  integer | Number of snapshots to allow.  **Returned:** success |
| **volumes**  integer | Number of volumes to allow.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
