---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_info module – Collect information from Pure Storage FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_info_module.html
fetched_at: 2026-07-28T00:18:49+00:00
---
# purestorage.flashblade.purefb_info module – Collect information from Pure Storage FlashBlade

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_info_module.md#ansible-collections-purestorage-flashblade-purefb-info-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_info`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_info_module.md#synopsis)
- [Requirements](purefb_info_module.md#requirements)
- [Parameters](purefb_info_module.md#parameters)
- [Notes](purefb_info_module.md#notes)
- [Examples](purefb_info_module.md#examples)
- [Return Values](purefb_info_module.md#return-values)

## [Synopsis](purefb_info_module.md#id1)

- Collect information from a Pure Storage FlashBlade running the Purity//FB operating system. By default, the module will collect basic information including hosts, host groups, protection groups and volume counts. Additional information can be collected based on the configured set of arguements.

## [Requirements](purefb_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **gather_subset**  list / elements=string | When supplied, this argument will define the information to be collected. Possible values for this include all, minimum, config, performance, capacity, network, subnets, lags, filesystems, snapshots, buckets, replication, policies, arrays, accounts, admins, ad, kerberos and drives.  Default: `["minimum"]` |

## [Notes](purefb_info_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_info_module.md#id5)

```yaml+jinja
- name: collect default set of info
  purestorage.flashblade.purefb_info:
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
  register: blade_info
- name: show default information
  debug:
    msg: "{{ blade_info['purefb_info']['default'] }}"

- name: collect configuration and capacity info
  purestorage.flashblade.purefb_info:
    gather_subset:
      - config
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
  register: blade_info
- name: show config information
  debug:
    msg: "{{ blade_info['purefb_info']['config'] }}"

- name: collect all info
  purestorage.flashblade.purefb_info:
    gather_subset:
      - all
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
  register: blade_info
- name: show all information
  debug:
    msg: "{{ blade_info['purefb_info'] }}"
```

## [Return Values](purefb_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefb_info**  complex | Returns the information collected from the FlashBlade  Returned: always  Sample: `{"admins": {"another_user": {"api_token_timeout": null, "local": false, "public_key": null}, "pureuser": {"api_token_timeout": null, "local": true, "public_key": null}}, "buckets": {"central": {"account_name": "jake", "bucket_type": "classic", "created": 1628900154000, "data_reduction": null, "destroyed": false, "id": "43758f09-9e71-7bf7-5757-2028a95a2b65", "lifecycle_rules": {}, "object_count": 0, "snapshot_space": 0, "time_remaining": null, "total_physical_space": 0, "unique_space": 0, "versioning": "none", "virtual_space": 0}, "test": {"account_name": "acme", "bucket_type": "classic", "created": 1630591952000, "data_reduction": 3.6, "destroyed": false, "id": "d5f6149c-fbef-f3c5-58b6-8fd143110ba9", "lifecycle_rules": {"test": {"abort_incomplete_multipart_uploads_after (days)": 1, "cleanup_expired_object_delete_marker": true, "enabled": true, "keep_current_version_for (days)": null, "keep_current_version_until": "2023-12-21", "keep_previous_version_for (days)": null, "prefix": "foo"}}}}, "capacity": {"aggregate": {"data_reduction": 1.1179228, "snapshots": 0, "total_physical": 17519748439, "unique": 17519748439, "virtual": 19585726464}, "file-system": {"data_reduction": 1.3642412, "snapshots": 0, "total_physical": 4748219708, "unique": 4748219708, "virtual": 6477716992}, "object-store": {"data_reduction": 1.0263462, "snapshots": 0, "total_physical": 12771528731, "unique": 12771528731, "virtual": 6477716992}, "total": 83359896948925}, "config": {"alert_watchers": {"enabled": true, "name": "notify@acmestorage.com"}, "array_management": {"base_dn": null, "bind_password": null, "bind_user": null, "enabled": false, "name": "management", "services": ["management"], "uris": []}, "directory_service_roles": {"array_admin": {"group": null, "group_base": null}, "ops_admin": {"group": null, "group_base": null}, "readonly": {"group": null, "group_base": null}, "storage_admin": {"group": null, "group_base": null}}, "dns": {"domain": "demo.acmestorage.com", "name": "demo-fb-1", "nameservers": ["8.8.8.8"], "search": ["demo.acmestorage.com"]}, "nfs_directory_service": {"base_dn": null, "bind_password": null, "bind_user": null, "enabled": false, "name": "nfs", "services": ["nfs"], "uris": []}, "ntp": ["0.ntp.pool.org"], "smb_directory_service": {"base_dn": null, "bind_password": null, "bind_user": null, "enabled": false, "name": "smb", "services": ["smb"], "uris": []}, "smtp": {"name": "demo-fb-1", "relay_host": null, "sender_domain": "acmestorage.com"}, "ssl_certs": {"certificate": "-----BEGIN CERTIFICATE-----\n\n-----END CERTIFICATE-----", "common_name": "Acme Storage", "country": "US", "email": null, "intermediate_certificate": null, "issued_by": "Acme Storage", "issued_to": "Acme Storage", "key_size": 4096, "locality": null, "name": "global", "organization": "Acme Storage", "organizational_unit": "Acme Storage", "passphrase": null, "private_key": null, "state": null, "status": "self-signed", "valid_from": "1508433967000", "valid_to": "2458833967000"}}, "default": {"blades": 15, "buckets": 7, "filesystems": 2, "flashblade_name": "demo-fb-1", "object_store_accounts": 1, "object_store_users": 1, "purity_version": "2.2.0", "smb_mode": "native", "snapshots": 1, "total_capacity": 83359896948925}, "filesystems": {"k8s-pvc-d24b1357-579e-11e8-811f-ecf4bbc88f54": {"default_group_quota": 0, "default_user_quota": 0, "destroyed": false, "fast_remove": false, "hard_limit": true, "nfs_rules": "10.21.255.0/24(rw,no_root_squash)", "provisioned": 21474836480, "snapshot_enabled": false}, "z": {"default_group_quota": 0, "default_user_quota": 0, "destroyed": false, "fast_remove": false, "hard_limit": false, "provisioned": 1073741824, "snapshot_enabled": false}}, "lag": {"uplink": {"lag_speed": 0, "port_speed": 40000000000, "ports": [{"name": "CH1.FM1.ETH1.1"}, {"name": "CH1.FM1.ETH1.2"}], "status": "healthy"}}, "network": {"fm1.admin0": {"address": "10.10.100.6", "gateway": "10.10.100.1", "mtu": 1500, "netmask": "255.255.255.0", "services": ["support"], "type": "vip", "vlan": 2200}, "fm2.admin0": {"address": "10.10.100.7", "gateway": "10.10.100.1", "mtu": 1500, "netmask": "255.255.255.0", "services": ["support"], "type": "vip", "vlan": 2200}, "nfs1": {"address": "10.10.100.4", "gateway": "10.10.100.1", "mtu": 1500, "netmask": "255.255.255.0", "services": ["data"], "type": "vip", "vlan": 2200}, "vir0": {"address": "10.10.100.5", "gateway": "10.10.100.1", "mtu": 1500, "netmask": "255.255.255.0", "services": ["management"], "type": "vip", "vlan": 2200}}, "performance": {"aggregate": {"bytes_per_op": 0, "bytes_per_read": 0, "bytes_per_write": 0, "read_bytes_per_sec": 0, "reads_per_sec": 0, "usec_per_other_op": 0, "usec_per_read_op": 0, "usec_per_write_op": 0, "write_bytes_per_sec": 0, "writes_per_sec": 0}, "http": {"bytes_per_op": 0, "bytes_per_read": 0, "bytes_per_write": 0, "read_bytes_per_sec": 0, "reads_per_sec": 0, "usec_per_other_op": 0, "usec_per_read_op": 0, "usec_per_write_op": 0, "write_bytes_per_sec": 0, "writes_per_sec": 0}, "nfs": {"bytes_per_op": 0, "bytes_per_read": 0, "bytes_per_write": 0, "read_bytes_per_sec": 0, "reads_per_sec": 0, "usec_per_other_op": 0, "usec_per_read_op": 0, "usec_per_write_op": 0, "write_bytes_per_sec": 0, "writes_per_sec": 0}, "s3": {"bytes_per_op": 0, "bytes_per_read": 0, "bytes_per_write": 0, "read_bytes_per_sec": 0, "reads_per_sec": 0, "usec_per_other_op": 0, "usec_per_read_op": 0, "usec_per_write_op": 0, "write_bytes_per_sec": 0, "writes_per_sec": 0}}, "snapshots": {"z.188": {"destroyed": false, "source": "z", "source_destroyed": false, "suffix": "188"}}, "subnet": {"new-mgmt": {"gateway": "10.10.100.1", "interfaces": [{"name": "fm1.admin0"}, {"name": "fm2.admin0"}, {"name": "nfs1"}, {"name": "vir0"}], "lag": "uplink", "mtu": 1500, "prefix": "10.10.100.0/24", "services": ["data", "management", "support"], "vlan": 2200}}}` |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
