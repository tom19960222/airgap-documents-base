---
collection: ansible
version: "6"
title: "How to collect information about your environment"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/collect_information.html
fetched_at: 2026-07-27T16:43:18+00:00
---
# How to collect information about your environment

- [Introduction](collect_information.md#introduction)
- [Scenario requirements](collect_information.md#scenario-requirements)
- [How to collect information](collect_information.md#how-to-collect-information)

  - [Datacenter](collect_information.md#datacenter)

    - [Result](collect_information.md#result)
  - [Cluster](collect_information.md#cluster)

    - [Result](collect_information.md#id1)
    - [Result](collect_information.md#id2)
  - [Datastore](collect_information.md#datastore)

    - [Result](collect_information.md#id3)
  - [Folder](collect_information.md#folder)

    - [Result](collect_information.md#id4)
    - [Result](collect_information.md#id5)

## [Introduction](collect_information.md#id6)

This section shows you how to utilize Ansible to collect information about your environment.
This information is useful for the other tutorials.

## [Scenario requirements](collect_information.md#id7)

In this scenario we’ve got a vCenter with an ESXi host.

Our environment is pre-initialized with the following elements:

- A datacenter called `my_dc`
- A cluster called `my_cluster`
- An ESXi host called `esxi1` is in the cluster
- Two datastores on the ESXi: `rw_datastore` and `ro_datastore`
- A dvswitch based guest network

Finally, we use the environment variables to authenticate ourselves as explained in [How to configure the vmware_rest collection](authentication.md#vmware-rest-authentication).

## [How to collect information](collect_information.md#id8)

In these examples, we use the `vcenter_*_info` module to collect information about the associated resources.

All these modules return a `value` key. Depending on the context, this `value` key will be either a list or a dictionary.

### [Datacenter](collect_information.md#id9)

Here we use the `vcenter_datacenter_info` module to list all the datacenters:

```YAML+Jinja
- name: collect a list of the datacenters
  vmware.vmware_rest.vcenter_datacenter_info:
  register: my_datacenters
```

#### [Result](collect_information.md#id10)

As expected, the `value` key of the output is a list.

```YAML+Jinja
{
    "value": [
        {
            "name": "my_dc",
            "datacenter": "datacenter-1630"
        }
    ],
    "changed": false
}
```

### [Cluster](collect_information.md#id11)

Here we do the same with `vcenter_cluster_info`:

```YAML+Jinja
- name: Build a list of all the clusters
  vmware.vmware_rest.vcenter_cluster_info:
  register: all_the_clusters
```

#### [Result](collect_information.md#id12)

```YAML+Jinja
{
    "value": [
        {
            "drs_enabled": false,
            "cluster": "domain-c1636",
            "name": "my_cluster",
            "ha_enabled": false
        }
    ],
    "changed": false
}
```

And we can also fetch the details about a specific cluster, with the `cluster` parameter:

```YAML+Jinja
- name: Retrieve details about the first cluster
  vmware.vmware_rest.vcenter_cluster_info:
    cluster: "{{ all_the_clusters.value[0].cluster }}"
  register: my_cluster_info
```

#### [Result](collect_information.md#id13)

And the `value` key of the output is this time a dictionary.

```YAML+Jinja
{
    "value": {
        "name": "my_cluster",
        "resource_pool": "resgroup-1637"
    },
    "id": "domain-c1636",
    "changed": false
}
```

### [Datastore](collect_information.md#id14)

Here we use `vcenter_datastore_info` to get a list of all the datastores:

```YAML+Jinja
- name: Retrieve a list of all the datastores
  vmware.vmware_rest.vcenter_datastore_info:
  register: my_datastores
```

#### [Result](collect_information.md#id15)

```YAML+Jinja
{
    "value": [
        {
            "datastore": "datastore-1644",
            "name": "local",
            "type": "VMFS",
            "free_space": 13523484672,
            "capacity": 15032385536
        },
        {
            "datastore": "datastore-1645",
            "name": "ro_datastore",
            "type": "NFS",
            "free_space": 24638349312,
            "capacity": 26831990784
        },
        {
            "datastore": "datastore-1646",
            "name": "rw_datastore",
            "type": "NFS",
            "free_space": 24638349312,
            "capacity": 26831990784
        }
    ],
    "changed": false
}
```

### [Folder](collect_information.md#id16)

And here again, you use the `vcenter_folder_info` module to retrieve a list of all the folders.

```YAML+Jinja
- name: Build a list of all the folders
  vmware.vmware_rest.vcenter_folder_info:
  register: my_folders
```

#### [Result](collect_information.md#id17)

```YAML+Jinja
{
    "value": [
        {
            "folder": "group-d1",
            "name": "Datacenters",
            "type": "DATACENTER"
        }
    ],
    "changed": false
}
```

Most of the time, you will just want one type of folder. In this case we can use filters to reduce the amount to collect. Most of the `_info` modules come with similar filters.

```YAML+Jinja
- name: Build a list of all the folders with the type VIRTUAL_MACHINE and called vm
  vmware.vmware_rest.vcenter_folder_info:
    filter_type: VIRTUAL_MACHINE
    filter_names:
      - vm
  register: my_folders
```

#### [Result](collect_information.md#id18)

```YAML+Jinja
{
    "value": [
        {
            "folder": "group-v1631",
            "name": "vm",
            "type": "VIRTUAL_MACHINE"
        }
    ],
    "changed": false
}
```
