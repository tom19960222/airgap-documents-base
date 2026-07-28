---
collection: ansible
version: "6"
title: "openstack.cloud.server module – Create/Delete Compute Instances from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/server_module.html
fetched_at: 2026-07-28T00:17:05+00:00
---
# openstack.cloud.server module – Create/Delete Compute Instances from OpenStack

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
> see [Requirements](server_module.md#ansible-collections-openstack-cloud-server-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server`.

- [Synopsis](server_module.md#synopsis)
- [Requirements](server_module.md#requirements)
- [Parameters](server_module.md#parameters)
- [Notes](server_module.md#notes)
- [Examples](server_module.md#examples)

## [Synopsis](server_module.md#id1)

- Create or Remove compute instances from OpenStack.

## [Requirements](server_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **auto_ip**  aliases: auto_floating_ip, public_ip  boolean | Ensure instance has public ip however the cloud wants to do that  Choices:   - `false` - `true` ← (default) |
| **availability_zone**  string | Availability zone in which to create the server. |
| **boot_from_volume**  boolean | Should the instance boot from a persistent volume created based on the image given. Mutually exclusive with boot_volume.  Choices:   - `false` ← (default) - `true` |
| **boot_volume**  aliases: root_volume  string | Volume name or id to use as the volume to boot from. Implies boot_from_volume. Mutually exclusive with image and boot_from_volume. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **config_drive**  boolean | Whether to boot the server with config drive enabled  Choices:   - `false` ← (default) - `true` |
| **delete_fip**  boolean | When *state* is absent and this option is true, any floating IP associated with the instance will be deleted along with the instance.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Description of the server. |
| **flavor**  string | The name or id of the flavor in which the new instance has to be created.  Exactly one of *flavor* and *flavor_ram* must be defined when *state=present*. |
| **flavor_include**  string | Text to use to filter flavor names, for the case, such as Rackspace, where there are multiple flavors that have the same ram count. flavor_include is a positive match filter - it must exist in the flavor name. |
| **flavor_ram**  integer | The minimum amount of ram in MB that the flavor in which the new instance has to be created must have.  Exactly one of *flavor* and *flavor_ram* must be defined when *state=present*. |
| **floating_ip_pools**  list / elements=string | Name of floating IP pool from which to choose a floating IP |
| **floating_ips**  list / elements=string | list of valid floating IPs that pre-exist to assign to this node |
| **image**  string | The name or id of the base image to boot.  Required when *boot_from_volume=true* |
| **image_exclude**  string | Text to use to filter image names, for the case, such as HP, where there are multiple image names matching the common identifying portions. image_exclude is a negative match filter - it is text that may not exist in the image name.  Default: `"(deprecated)"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **key_name**  string | The key pair name to be used when creating a instance |
| **meta**  any | A list of key value pairs that should be provided as a metadata to the new instance or a string containing a list of key-value pairs. Eg: meta: “key1=value1,key2=value2” |
| **name**  string / required | Name that has to be given to the instance. It is also possible to specify the ID of the instance instead of its name if *state* is *absent*. |
| **network**  string | Name or ID of a network to attach this instance to. A simpler version of the nics parameter, only one of network or nics should be supplied. |
| **nics**  list / elements=any | A list of networks to which the instance’s interface should be attached. Networks may be referenced by net-id/net-name/port-id or port-name.  Also this accepts a string containing a list of (net/port)-(id/name) Eg: nics: “net-id=uuid-1,port-name=myport” Only one of network or nics should be supplied. |
| **tag**  string | A “tag” for the specific port to be passed via metadata. Eg: tag: test_tag |
| **region_name**  string | Name of the region. |
| **reuse_ips**  boolean | When *auto_ip* is true and this option is true, the *auto_ip* code will attempt to re-use unassigned floating ips in the project before creating a new one. It is important to note that it is impossible to safely do this concurrently, so if your use case involves concurrent server creation, it is highly recommended to set this to false and to delete the floating ip associated with a server when the server is deleted using *delete_fip*.  Choices:   - `false` - `true` ← (default) |
| **scheduler_hints**  dictionary | Arbitrary key/value pairs to the scheduler for custom use |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_groups**  list / elements=string | Names of the security groups to which the instance should be added. This may be a YAML list or a comma separated string.  Default: `["default"]` |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **terminate_volume**  boolean | If `yes`, delete volume when deleting instance (if booted from volume)  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The amount of time the module should wait for the instance to get into active state.  Default: `180` |
| **userdata**  aliases: user_data  string | Opaque blob of data which is made available to the instance |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **volume_size**  integer | The size of the volume to create in GB if booting from volume based on an image. |
| **volumes**  list / elements=string | A list of preexisting volumes names or ids to attach to the instance  Default: `[]` |
| **wait**  boolean | If the module should wait for the instance to be created.  Choices:   - `false` - `true` ← (default) |

## [Notes](server_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_module.md#id5)

```yaml+jinja
- name: Create a new instance and attaches to a network and passes metadata to the instance
  openstack.cloud.server:
       state: present
       auth:
         auth_url: https://identity.example.com
         username: admin
         password: admin
         project_name: admin
       name: vm1
       image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
       key_name: ansible_key
       timeout: 200
       flavor: 4
       nics:
         - net-id: 34605f38-e52a-25d2-b6ec-754a13ffb723
         - net-name: another_network
       meta:
         hostname: test1
         group: uge_master

# Create a new instance in HP Cloud AE1 region availability zone az2 and
# automatically assigns a floating IP
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        state: present
        auth:
          auth_url: https://identity.example.com
          username: username
          password: Equality7-2521
          project_name: username-project1
        name: vm1
        region_name: region-b.geo-1
        availability_zone: az2
        image: 9302692b-b787-4b52-a3a6-daebb79cb498
        key_name: test
        timeout: 200
        flavor: 101
        security_groups: default
        auto_ip: yes

# Create a new instance in named cloud mordred availability zone az2
# and assigns a pre-known floating IP
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        state: present
        cloud: mordred
        name: vm1
        availability_zone: az2
        image: 9302692b-b787-4b52-a3a6-daebb79cb498
        key_name: test
        timeout: 200
        flavor: 101
        floating_ips:
          - 12.34.56.79

# Create a new instance with 4G of RAM on Ubuntu Trusty, ignoring
# deprecated images
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        state: present
        cloud: mordred
        region_name: region-b.geo-1
        image: Ubuntu Server 14.04
        image_exclude: deprecated
        flavor_ram: 4096

# Create a new instance with 4G of RAM on Ubuntu Trusty on a Performance node
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        cloud: rax-dfw
        state: present
        image: Ubuntu 14.04 LTS (Trusty Tahr) (PVHVM)
        flavor_ram: 4096
        flavor_include: Performance

# Creates a new instance and attaches to multiple network
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance with a string
      openstack.cloud.server:
        auth:
           auth_url: https://identity.example.com
           username: admin
           password: admin
           project_name: admin
        name: vm1
        image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
        key_name: ansible_key
        timeout: 200
        flavor: 4
        nics: "net-id=4cb08b20-62fe-11e5-9d70-feff819cdc9f,net-id=542f0430-62fe-11e5-9d70-feff819cdc9f..."

- name: Creates a new instance and attaches to a network and passes metadata to the instance
  openstack.cloud.server:
       state: present
       auth:
         auth_url: https://identity.example.com
         username: admin
         password: admin
         project_name: admin
       name: vm1
       image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
       key_name: ansible_key
       timeout: 200
       flavor: 4
       nics:
         - net-id: 34605f38-e52a-25d2-b6ec-754a13ffb723
         - net-name: another_network
       meta: "hostname=test1,group=uge_master"

- name:  Creates a new instance and attaches to a specific network
  openstack.cloud.server:
    state: present
    auth:
      auth_url: https://identity.example.com
      username: admin
      password: admin
      project_name: admin
    name: vm1
    image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
    key_name: ansible_key
    timeout: 200
    flavor: 4
    network: another_network

# Create a new instance with 4G of RAM on a 75G Ubuntu Trusty volume
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        state: present
        cloud: mordred
        region_name: ams01
        image: Ubuntu Server 14.04
        flavor_ram: 4096
        boot_from_volume: True
        volume_size: 75

# Creates a new instance with 2 volumes attached
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        state: present
        cloud: mordred
        region_name: ams01
        image: Ubuntu Server 14.04
        flavor_ram: 4096
        volumes:
        - photos
        - music

# Creates a new instance with provisioning userdata using Cloud-Init
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        state: present
        image: "Ubuntu Server 14.04"
        flavor: "P-1"
        network: "Production"
        userdata: |
          #cloud-config
          chpasswd:
            list: |
              ubuntu:{{ default_password }}
            expire: False
          packages:
            - ansible
          package_upgrade: true

# Creates a new instance with provisioning userdata using Bash Scripts
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        name: vm1
        state: present
        image: "Ubuntu Server 14.04"
        flavor: "P-1"
        network: "Production"
        userdata: |
          {%- raw -%}#!/bin/bash
          echo "  up ip route add 10.0.0.0/8 via {% endraw -%}{{ intra_router }}{%- raw -%}" >> /etc/network/interfaces.d/eth0.conf
          echo "  down ip route del 10.0.0.0/8" >> /etc/network/interfaces.d/eth0.conf
          ifdown eth0 && ifup eth0
          {% endraw %}

# Create a new instance with server group for (anti-)affinity
# server group ID is returned from openstack.cloud.server_group module.
- name: launch a compute instance
  hosts: localhost
  tasks:
    - name: launch an instance
      openstack.cloud.server:
        state: present
        name: vm1
        image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
        flavor: 4
        scheduler_hints:
          group: f5c8c61a-9230-400a-8ed2-3b023c190a7f

# Create an instance with "tags" for the nic
- name: Create instance with nics "tags"
  openstack.cloud.server:
    state: present
    auth:
        auth_url: https://identity.example.com
        username: admin
        password: admin
        project_name: admin
    name: vm1
    image: 4f905f38-e52a-43d2-b6ec-754a13ffb529
    key_name: ansible_key
    flavor: 4
    nics:
      - port-name: net1_port1
        tag: test_tag
      - net-name: another_network

# Deletes an instance via its ID
- name: remove an instance
  hosts: localhost
  tasks:
    - name: remove an instance
      openstack.cloud.server:
        name: abcdef01-2345-6789-0abc-def0123456789
        state: absent
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
