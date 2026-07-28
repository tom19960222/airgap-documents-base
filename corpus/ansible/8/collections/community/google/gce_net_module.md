---
collection: ansible
version: "8"
title: "community.google.gce_net module – create/destroy GCE networks and firewall rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gce_net_module.html
fetched_at: 2026-07-28T01:53:08+00:00
---
# community.google.gce_net module – create/destroy GCE networks and firewall rules

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/ui/repo/published/community/google/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_net_module.md#ansible-collections-community-google-gce-net-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_net`.

- [Synopsis](gce_net_module.md#synopsis)
- [Requirements](gce_net_module.md#requirements)
- [Parameters](gce_net_module.md#parameters)
- [Examples](gce_net_module.md#examples)
- [Return Values](gce_net_module.md#return-values)

## [Synopsis](gce_net_module.md#id1)

- This module can create and destroy Google Compute Engine networks and firewall rules <https://cloud.google.com/compute/docs/networking>. The *name* parameter is reserved for referencing a network while the *fwname* parameter is used to reference firewall rules. IPv4 Address ranges must be specified using the CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing> format. Full install/configuration instructions for the gce\* modules can be found in the comments of ansible/test/gce_tests.py.

## [Requirements](gce_net_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.13.3, >= 0.17.0 if using JSON credentials

## [Parameters](gce_net_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowed**  string | the protocol:ports to allow (*tcp:80* or *tcp:80,443* or *tcp:80-800;udp:1-25*) this parameter is mandatory when creating or updating a firewall rule |
| **credentials_file**  path | path to the JSON file associated with the service account email |
| **fwname**  string | name of the firewall rule |
| **ipv4_range**  string | the IPv4 address range in CIDR notation for the network this parameter is not mandatory when you specified existing network in name parameter, but when you create new network, this parameter is mandatory |
| **mode**  string | network mode for Google Cloud `legacy` indicates a network with an IP address range; `auto` automatically generates subnetworks in different regions; `custom` uses networks to group subnets of user specified IP address ranges <https://cloud.google.com/compute/docs/networking#network_types>  **Choices:**   - `"legacy"` ← (default) - `"auto"` - `"custom"` |
| **name**  string | name of the network |
| **pem_file**  path | path to the pem file associated with the service account email This option is deprecated. Use `credentials_file`. |
| **project_id**  string | your GCE project ID |
| **service_account_email**  string | service account email |
| **src_range**  list / elements=string | the source IPv4 address range in CIDR notation  **Default:** `[]` |
| **src_tags**  list / elements=string | the source instance tags for creating a firewall rule  **Default:** `[]` |
| **state**  string | desired state of the network or firewall  Available choices are: `active`, `present`, `absent`, `deleted`.  **Default:** `"present"` |
| **subnet_desc**  string | description of subnet to create |
| **subnet_name**  string | name of subnet to create |
| **subnet_region**  string | region of subnet to create |
| **target_tags**  list / elements=string | the target instance tags for creating a firewall rule  **Default:** `[]` |

## [Examples](gce_net_module.md#id4)

```yaml+jinja
# Create a 'legacy' Network
- name: Create Legacy Network
  community.google.gce_net:
    name: legacynet
    ipv4_range: '10.24.17.0/24'
    mode: legacy
    state: present

# Create an 'auto' Network
- name: Create Auto Network
  community.google.gce_net:
    name: autonet
    mode: auto
    state: present

# Create a 'custom' Network
- name: Create Custom Network
  community.google.gce_net:
    name: customnet
    mode: custom
    subnet_name: "customsubnet"
    subnet_region: us-east1
    ipv4_range: '10.240.16.0/24'
    state: "present"

# Create Firewall Rule with Source Tags
- name: Create Firewall Rule w/Source Tags
  community.google.gce_net:
    name: default
    fwname: "my-firewall-rule"
    allowed: tcp:80
    state: "present"
    src_tags: "foo,bar"

# Create Firewall Rule with Source Range
- name: Create Firewall Rule w/Source Range
  community.google.gce_net:
    name: default
    fwname: "my-firewall-rule"
    allowed: tcp:80
    state: "present"
    src_range: ['10.1.1.1/32']

# Create Custom Subnetwork
- name: Create Custom Subnetwork
  community.google.gce_net:
    name: privatenet
    mode: custom
    subnet_name: subnet_example
    subnet_region: us-central1
    ipv4_range: '10.0.0.0/16'
```

## [Return Values](gce_net_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allowed**  string | Rules (ports and protocols) specified by this firewall rule.  **Returned:** When specified  **Sample:** `"tcp:80;icmp"` |
| **fwname**  string | Name of the firewall rule.  **Returned:** When specified  **Sample:** `"my-fwname"` |
| **ipv4_range**  string | IPv4 range of the specified network or subnetwork.  **Returned:** when specified or when a subnetwork is created  **Sample:** `"10.0.0.0/16"` |
| **name**  string | Name of the network.  **Returned:** always  **Sample:** `"my-network"` |
| **src_range**  list / elements=string | IP address blocks a firewall rule applies to.  **Returned:** when specified  **Sample:** `["10.1.1.12/8"]` |
| **src_tags**  list / elements=string | Instance Tags firewall rule applies to.  **Returned:** when specified while creating a firewall rule  **Sample:** `["foo", "bar"]` |
| **state**  string | State of the item operated on.  **Returned:** always  **Sample:** `"present"` |
| **subnet_name**  string | Name of the subnetwork.  **Returned:** when specified or when a subnetwork is created  **Sample:** `"my-subnetwork"` |
| **subnet_region**  string | Region of the specified subnet.  **Returned:** when specified or when a subnetwork is created  **Sample:** `"us-east1"` |
| **target_tags**  list / elements=string | Instance Tags with these tags receive traffic allowed by firewall rule.  **Returned:** when specified while creating a firewall rule  **Sample:** `["foo", "bar"]` |

### Authors

- Eric Johnson (@erjohnso) , Tom Melendez (@supertom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
