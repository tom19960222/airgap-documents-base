---
collection: ansible
version: "6"
title: "community.general.one_host module – Manages OpenNebula Hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/one_host_module.html
fetched_at: 2026-07-27T17:11:13+00:00
---
# community.general.one_host module – Manages OpenNebula Hosts

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](one_host_module.md#ansible-collections-community-general-one-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.one_host`.

- [Synopsis](one_host_module.md#synopsis)
- [Requirements](one_host_module.md#requirements)
- [Parameters](one_host_module.md#parameters)
- [Examples](one_host_module.md#examples)

## [Synopsis](one_host_module.md#id1)

- Manages OpenNebula Hosts

## [Requirements](one_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyone

## [Parameters](one_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  aliases: api_token  string | The password or token for XMLRPC authentication.  If not specified then the value of the ONE_PASSWORD environment variable, if any, is used. |
| **api_url**  aliases: api_endpoint  string | The ENDPOINT URL of the XMLRPC server.  If not specified then the value of the ONE_URL environment variable, if any, is used. |
| **api_username**  string | The name of the user for XMLRPC authentication.  If not specified then the value of the ONE_USERNAME environment variable, if any, is used. |
| **cluster_id**  integer | The cluster ID.  Default: `0` |
| **cluster_name**  string | The cluster specified by name. |
| **im_mad_name**  string | The name of the information manager, this values are taken from the oned.conf with the tag name IM_MAD (name)  Default: `"kvm"` |
| **labels**  list / elements=string | The labels for this host. |
| **name**  string / required | Hostname of the machine to manage. |
| **state**  string | Takes the host to the desired lifecycle state.  If `absent` the host will be deleted from the cluster.  If `present` the host will be created in the cluster (includes `enabled`, `disabled` and `offline` states).  If `enabled` the host is fully operational.  `disabled`, e.g. to perform maintenance operations.  `offline`, host is totally offline.  Choices:   - `"absent"` - `"present"` ← (default) - `"enabled"` - `"disabled"` - `"offline"` |
| **template**  aliases: attributes  dictionary | The template or attribute changes to merge into the host template. |
| **validate_certs**  boolean | Whether to validate the SSL certificates or not.  This parameter is ignored if PYTHONHTTPSVERIFY environment variable is used.  Choices:   - `false` - `true` ← (default) |
| **vmm_mad_name**  string | The name of the virtual machine manager mad name, this values are taken from the oned.conf with the tag name VM_MAD (name)  Default: `"kvm"` |
| **wait_timeout**  integer | Time to wait for the desired state to be reached before timeout, in seconds.  Default: `300` |

## [Examples](one_host_module.md#id4)

```yaml+jinja
- name: Create a new host in OpenNebula
  community.general.one_host:
    name: host1
    cluster_id: 1
    api_url: http://127.0.0.1:2633/RPC2

- name: Create a host and adjust its template
  community.general.one_host:
    name: host2
    cluster_name: default
    template:
        LABELS:
            - gold
            - ssd
        RESERVED_CPU: -100
```

### Authors

- Rafael del Valle (@rvalle)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
