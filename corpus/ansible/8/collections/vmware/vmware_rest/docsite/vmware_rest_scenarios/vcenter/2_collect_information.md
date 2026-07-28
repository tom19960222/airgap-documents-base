---
collection: ansible
version: "8"
title: "How to collect information about your environment"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/docsite/vmware_rest_scenarios/vcenter/2_collect_information.html
fetched_at: 2026-07-28T03:01:10+00:00
---
# How to collect information about your environment

## Introduction

This section shows you how to utilize Ansible to collect information
about your environment. This information is useful for the other
tutorials.

## Scenario requirements

In this scenario we”ve got a vCenter with an ESXi host.

Our environment is pre-initialized with the following elements:

- A datacenter called `my_dc`
- A cluster called `my_cluser`
- A cluster called `my_cluser`
- An ESXi host called `esxi1` is in the cluster
- Two datastores on the ESXi: `rw_datastore` and `ro_datastore`
- A dvswitch based guest network

Finally, we use the environment variables to authenticate ourselves as
explained in vmware_rest_authentication.

## How to collect information

In these examples, we use the `vcenter_*_info` module to collect
information about the associated resources.

All these modules return a `value` key. Depending on the context,
this `value` key will be either a list or a dictionary.

### Datacenter

Here we use the `vcenter_datacenter_info` module to list all the
datacenters. As expected, the `value` key of the output is a list.

```YAML+Jinja
- name: collect a list of the datacenters
  vmware.vmware_rest.vcenter_datacenter_info:
  register: my_datacenters
```

response

```YAML+Jinja
{
    "changed": false,
    "value": [
        {
            "datacenter": "datacenter-1160",
            "name": "my_dc"
        }
    ]
}
```

### Cluster

Here we do the same with `vcenter_cluster_info` module:

```YAML+Jinja
- name: Build a list of all the clusters
  vmware.vmware_rest.vcenter_cluster_info:
  register: all_the_clusters
```

response

```YAML+Jinja
{
    "changed": false,
    "value": [
        {
            "cluster": "domain-c1165",
            "drs_enabled": true,
            "ha_enabled": false,
            "name": "my_cluster"
        }
    ]
}
```

And we can also fetch the details about a specific cluster, with the
`cluster` parameter:

```YAML+Jinja
- name: Retrieve details about the first cluster
  vmware.vmware_rest.vcenter_cluster_info:
    cluster: "{{ all_the_clusters.value[0].cluster }}"
  register: my_cluster_info
```

response

```YAML+Jinja
{
    "changed": false,
    "id": "domain-c1165",
    "value": {
        "name": "my_cluster",
        "resource_pool": "resgroup-1166"
    }
}
```

And the `value` key of the output is this time a dictionary.

### Datastore

Here we use `vcenter_datastore_info` to get a list of all the
datastore called `rw_datastore`:

```YAML+Jinja
- name: Retrieve a list of all the datastores
  vmware.vmware_rest.vcenter_datastore_info:
    filter_names:
    - rw_datastore
  register: my_datastores
```

response

```YAML+Jinja
{
    "changed": false,
    "value": [
        {
            "capacity": 42314215424,
            "datastore": "datastore-1175",
            "free_space": 40362840064,
            "name": "rw_datastore",
            "type": "NFS"
        }
    ]
}
```

We save the first datastore in *my_datastore* fact for later use.

```YAML+Jinja
- name: Set my_datastore
  set_fact:
     my_datastore: '{{ my_datastores.value|first }}'
```

response

```YAML+Jinja
{
    "ansible_facts": {
        "my_datastore": {
            "capacity": 42314215424,
            "datastore": "datastore-1175",
            "free_space": 40362840064,
            "name": "rw_datastore",
            "type": "NFS"
        }
    },
    "changed": false
}
```

### Folder

And here again, you use the `vcenter_folder_info` module to retrieve
a list of all the folders.

```YAML+Jinja
- name: Build a list of all the folders
  vmware.vmware_rest.vcenter_folder_info:
  register: my_folders
```

response

```YAML+Jinja
{
    "changed": false,
    "value": [
        {
            "folder": "group-d1",
            "name": "Datacenters",
            "type": "DATACENTER"
        },
        {
            "folder": "group-h1162",
            "name": "host",
            "type": "HOST"
        },
        {
            "folder": "group-n1164",
            "name": "network",
            "type": "NETWORK"
        },
        {
            "folder": "group-s1163",
            "name": "datastore",
            "type": "DATASTORE"
        },
        {
            "folder": "group-v1161",
            "name": "vm",
            "type": "VIRTUAL_MACHINE"
        },
        {
            "folder": "group-v1169",
            "name": "Discovered virtual machine",
            "type": "VIRTUAL_MACHINE"
        },
        {
            "folder": "group-v1173",
            "name": "vCLS",
            "type": "VIRTUAL_MACHINE"
        }
    ]
}
```

Most of the time, you will just want one type of folder. In this case
we can use filters to reduce the amount to collect. Most of the
`_info` modules come with similar filters.

```YAML+Jinja
- name: Build a list of all the folders with the type VIRTUAL_MACHINE and called vm
  vmware.vmware_rest.vcenter_folder_info:
    filter_type: VIRTUAL_MACHINE
    filter_names:
      - vm
  register: my_folders
```

response

```YAML+Jinja
{
    "changed": false,
    "value": [
        {
            "folder": "group-v1161",
            "name": "vm",
            "type": "VIRTUAL_MACHINE"
        }
    ]
}
```

We register the first folder for later use with `set_fact`.

```YAML+Jinja
- name: Set my_virtual_machine_folder
  set_fact:
    my_virtual_machine_folder: '{{ my_folders.value|first }}'
```

response

```YAML+Jinja
{
    "ansible_facts": {
        "my_virtual_machine_folder": {
            "folder": "group-v1161",
            "name": "vm",
            "type": "VIRTUAL_MACHINE"
        }
    },
    "changed": false
}
```
