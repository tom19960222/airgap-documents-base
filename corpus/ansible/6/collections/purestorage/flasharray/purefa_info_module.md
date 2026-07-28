---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_info module – Collect information from Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_info_module.html
fetched_at: 2026-07-28T00:18:15+00:00
---
# purestorage.flasharray.purefa_info module – Collect information from Pure Storage FlashArray

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_info_module.md#ansible-collections-purestorage-flasharray-purefa-info-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_info`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_info_module.md#synopsis)
- [Requirements](purefa_info_module.md#requirements)
- [Parameters](purefa_info_module.md#parameters)
- [Notes](purefa_info_module.md#notes)
- [Examples](purefa_info_module.md#examples)
- [Return Values](purefa_info_module.md#return-values)

## [Synopsis](purefa_info_module.md#id1)

- Collect information from a Pure Storage Flasharray running the Purity//FA operating system. By default, the module will collect basic information including hosts, host groups, protection groups and volume counts. Additional information can be collected based on the configured set of arguements.

## [Requirements](purefa_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **gather_subset**  list / elements=string | When supplied, this argument will define the information to be collected. Possible values for this include all, minimum, config, performance, capacity, network, subnet, interfaces, hgroups, pgroups, hosts, admins, volumes, snapshots, pods, replication, vgroups, offload, apps, arrays, certs, kmip, clients, policies, dir_snaps, filesystems and virtual_machines.  Default: `["minimum"]` |

## [Notes](purefa_info_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_info_module.md#id5)

```yaml+jinja
- name: collect default set of information
  purestorage.flasharray.purefa_info:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: array_info
- name: show default information
  debug:
    msg: "{{ array_info['purefa_info']['default'] }}"

- name: collect configuration and capacity information
  purestorage.flasharray.purefa_info:
    gather_subset:
      - config
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: array_info
- name: show configuration information
  debug:
    msg: "{{ array_info['purefa_info']['config'] }}"

- name: collect all information
  purestorage.flasharray.purefa_info:
    gather_subset:
      - all
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: show all information
  debug:
    msg: "{{ array_info['purefa_info'] }}"
```

## [Return Values](purefa_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefa_info**  complex | Returns the information collected from the FlashArray  Returned: always  Sample: `{"admins": {"pureuser": {"role": "array_admin", "type": "local"}}, "apps": {"offload": {"description": "Snapshot offload to NFS or Amazon S3", "status": "healthy", "version": "5.2.1"}}, "arrays": {}, "capacity": {"data_reduction": 11.664774599686346, "free_space": 6995782867042, "provisioned_space": 442391871488, "shared_space": 3070918120, "snapshot_space": 284597118, "system_space": 0, "thin_provisioning": 0.8201773449669771, "total_capacity": 7002920315199, "total_reduction": 64.86821472825108, "volume_space": 3781932919}, "config": {"directory_service": {"data": {"base_dn": "dc=example,dc=lab", "bind_user": "CN=user,OU=Users,OU=Example Lab,DC=example,DC=lab", "enabled": true, "services": ["data"], "uris": ["ldap://1.2.3.11"]}, "management": {"base_dn": "DC=example,DC=lab", "bind_user": "svc.ldap", "enabled": true, "services": ["management"], "uris": ["ldap://1.2.3.10", "ldap://1.2.3.11"]}}, "directory_service_roles": {"array_admin": {"group": null, "group_base": null}, "ops_admin": {"group": null, "group_base": null}, "readonly": {"group": null, "group_base": null}, "storage_admin": {"group": null, "group_base": null}}, "dns": {"domain": "acme.com", "nameservers": ["8.8.4.4"]}, "global_admin": {"lockout_duration": null, "max_login_attempts": null, "min_password_length": 1, "single_sign_on_enabled": false}, "idle_timeout": 0, "ntp": ["prod-ntp1.puretec.purestorage.com"], "phonehome": "enabled", "proxy": "", "relayhost": "smtp.puretec.purestorage.com", "scsi_timeout": 60, "senderdomain": "purestorage.com", "smtp": [{"enabled": true, "name": "flasharray-alerts@purestorage.com"}], "snmp": [{"auth_passphrase": null, "auth_protocol": null, "community": "", "host": "10.21.23.34", "name": "manager1", "notification": "trap", "privacy_passphrase": null, "privacy_protocol": null, "user": null, "version": "v2c"}], "syslog": ["udp://prod-ntp2.puretec.purestorage.com:333"]}, "default": {"admins": 1, "array_model": "FA-405", "array_name": "array", "connected_arrays": 0, "connection_key": "c6033033-fe69-2515-a9e8-966bb7fe4b40", "hostgroups": 0, "hosts": 15, "pods": 1, "protection_groups": 1, "purity_version": "5.2.1", "safe_mode": "Disabled", "snapshots": 2, "volume_groups": 1}, "hgroups": {}, "hosts": {"@offload": {"hgroup": null, "iqn": [], "nqn": [], "personality": null, "preferred_array": [], "target_port": [], "wwn": []}, "docker-host": {"hgroup": null, "iqn": ["iqn.1994-05.com.redhat:d97adf78472"], "nqn": [], "personality": null, "preferred_array": [], "target_port": ["CT0.ETH4", "CT1.ETH4"], "wwn": []}}, "interfaces": {"CT0.ETH4": "iqn.2010-06.com.purestorage:flasharray.2111b767484e4682", "CT1.ETH4": "iqn.2010-06.com.purestorage:flasharray.2111b767484e4682"}, "network": {"@offload.data0": {"address": "10.21.200.222", "gateway": "10.21.200.1", "hwaddr": "52:54:30:02:b9:4e", "mtu": 1500, "netmask": "255.255.255.0", "services": ["app"], "speed": 10000000000}, "ct0.eth0": {"address": "10.21.200.211", "gateway": "10.21.200.1", "hwaddr": "ec:f4:bb:c8:8a:04", "mtu": 1500, "netmask": "255.255.255.0", "services": ["management"], "speed": 1000000000}, "ct0.eth2": {"address": "10.21.200.218", "gateway": null, "hwaddr": "ec:f4:bb:c8:8a:00", "mtu": 1500, "netmask": "255.255.255.0", "services": ["replication"], "speed": 10000000000}, "ct0.eth4": {"address": "10.21.200.214", "gateway": null, "hwaddr": "90:e2:ba:83:79:0c", "mtu": 1500, "netmask": "255.255.255.0", "services": ["iscsi"], "speed": 10000000000}, "ct1.eth0": {"address": "10.21.200.212", "gateway": "10.21.200.1", "hwaddr": "ec:f4:bb:e4:c6:3c", "mtu": 1500, "netmask": "255.255.255.0", "services": ["management"], "speed": 1000000000}, "ct1.eth2": {"address": "10.21.200.220", "gateway": null, "hwaddr": "ec:f4:bb:e4:c6:38", "mtu": 1500, "netmask": "255.255.255.0", "services": ["replication"], "speed": 10000000000}, "ct1.eth4": {"address": "10.21.200.216", "gateway": null, "hwaddr": "90:e2:ba:8b:b1:8c", "mtu": 1500, "netmask": "255.255.255.0", "services": ["iscsi"], "speed": 10000000000}, "vir0": {"address": "10.21.200.210", "gateway": "10.21.200.1", "hwaddr": "fe:ba:e9:e7:6b:0f", "mtu": 1500, "netmask": "255.255.255.0", "services": ["management"], "speed": 1000000000}}, "nfs_offload": {}, "performance": {"input_per_sec": 0, "local_queue_usec_per_op": 0, "output_per_sec": 0, "qos_rate_limit_usec_per_read_op": 0, "qos_rate_limit_usec_per_write_op": 0, "queue_depth": 0, "queue_usec_per_read_op": 0, "queue_usec_per_write_op": 0, "reads_per_sec": 0, "san_usec_per_read_op": 0, "san_usec_per_write_op": 0, "time": "2019-08-14T21:33:51Z", "usec_per_read_op": 0, "usec_per_write_op": 0, "writes_per_sec": 0}, "pgroups": {"test_pg": {"hgroups": null, "hosts": null, "source": "docker-host", "targets": null, "volumes": null}}, "pods": {"test": {"arrays": [{"array_id": "043be47c-1233-4399-b9d6-8fe38727dd9d", "mediator_status": "online", "name": "array2", "status": "online"}], "source": null}}, "s3_offload": {"s3-offload": {"access_key_id": "AKIAILNVEPWZTV4FGWZQ", "bucket": "offload-bucket", "protocol": "s3", "status": "connected"}}, "snapshots": {"@offload_boot.1": {"created": "2019-03-14T15:29:20Z", "size": 68719476736, "source": "@offload_boot"}}, "subnet": {}, "vgroups": {"test": {"volumes": ["test/test", "test/test1"]}}, "volumes": {"@offload_boot": {"bandwidth": null, "hosts": [["@offload", 1]], "nvme_guid": "eui.0043BE47C123343924a9379B00013959", "page83_naa": "naa.624a937043BE47C12334399B00013959", "serial": "43BE47C12334399B00013959", "size": 68719476736, "source": null}, "docker-store": {"bandwidth": null, "hosts": [["docker-host", 1]], "nvme_guid": "eui.0043BE47C14a93724a9379B00013959", "page83_naa": "naa.624a937043BE47C12334399B00011418", "serial": "43BE47C12334399B00011418", "size": 21474836480, "source": null}}}` |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
