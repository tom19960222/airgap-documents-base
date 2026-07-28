---
collection: ansible
version: "8"
title: "openstack.cloud.server module – Create/Delete Compute Instances from OpenStack"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/server_module.html
fetched_at: 2026-07-28T02:48:46+00:00
---
# openstack.cloud.server module – Create/Delete Compute Instances from OpenStack

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
> see [Requirements](server_module.md#ansible-collections-openstack-cloud-server-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.server`.

- [Synopsis](server_module.md#synopsis)
- [Requirements](server_module.md#requirements)
- [Parameters](server_module.md#parameters)
- [Notes](server_module.md#notes)
- [Examples](server_module.md#examples)
- [Return Values](server_module.md#return-values)

## [Synopsis](server_module.md#id1)

- Create or Remove compute instances from OpenStack.

## [Requirements](server_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **auto_ip**  aliases: auto_floating_ip, public_ip  boolean | Ensure instance has public ip however the cloud wants to do that.  For example, the cloud could add a floating ip for the server or attach the server to a public network.  Requires *wait* to be `True` during server creation.  Floating IP support is unstable in this module, use with caution.  Options *auto_ip*, *floating_ip_pools* and *floating_ips* interact in non-obvious ways and undocumentable depth. For explicit and safe attaching and detaching of floating ip addresses use module *openstack.cloud.resource* instead.  **Choices:**   - `false` - `true` ← (default) |
| **availability_zone**  string | Availability zone in which to create the server.  This server attribute cannot be updated. |
| **boot_from_volume**  boolean | Should the instance boot from a persistent volume created based on the image given. Mutually exclusive with boot_volume.  This server attribute cannot be updated.  **Choices:**   - `false` ← (default) - `true` |
| **boot_volume**  aliases: root_volume  string | Volume name or id to use as the volume to boot from. Implies boot_from_volume. Mutually exclusive with image and boot_from_volume.  This server attribute cannot be updated. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **config_drive**  boolean | Whether to boot the server with config drive enabled.  This server attribute cannot be updated.  **Choices:**   - `false` ← (default) - `true` |
| **delete_ips**  aliases: delete_fip  boolean | When *state* is `absent` and this option is true, any floating IP address associated with this server will be deleted along with it.  Floating IP support is unstable in this module, use with caution.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Description of the server. |
| **flavor**  string | The name or id of the flavor in which the new instance has to be created.  Exactly one of *flavor* and *flavor_ram* must be defined when *state=present*.  This server attribute cannot be updated. |
| **flavor_include**  string | Text to use to filter flavor names, for the case, such as Rackspace, where there are multiple flavors that have the same ram count. flavor_include is a positive match filter - it must exist in the flavor name.  This server attribute cannot be updated. |
| **flavor_ram**  integer | The minimum amount of ram in MB that the flavor in which the new instance has to be created must have.  Exactly one of *flavor* and *flavor_ram* must be defined when *state=present*.  This server attribute cannot be updated. |
| **floating_ip_pools**  list / elements=string | Name of floating IP pool from which to choose a floating IP.  Requires *wait* to be `True` during server creation.  Floating IP support is unstable in this module, use with caution.  Options *auto_ip*, *floating_ip_pools* and *floating_ips* interact in non-obvious ways and undocumentable depth. For explicit and safe attaching and detaching of floating ip addresses use module *openstack.cloud.resource* instead. |
| **floating_ips**  list / elements=string | list of valid floating IPs that pre-exist to assign to this node.  Requires *wait* to be `True` during server creation.  Floating IP support is unstable in this module, use with caution.  Options *auto_ip*, *floating_ip_pools* and *floating_ips* interact in non-obvious ways and undocumentable depth. For explicit and safe attaching and detaching of floating ip addresses use module *openstack.cloud.resource* instead. |
| **image**  string | The name or id of the base image to boot.  Required when *boot_from_volume=true*.  This server attribute cannot be updated. |
| **image_exclude**  string | Text to use to filter image names, for the case, such as HP, where there are multiple image names matching the common identifying portions. image_exclude is a negative match filter - it is text that may not exist in the image name.  This server attribute cannot be updated.  **Default:** `"(deprecated)"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **key_name**  string | The key pair name to be used when creating a instance.  This server attribute cannot be updated. |
| **metadata**  aliases: meta  any | A list of key value pairs that should be provided as a metadata to the new instance or a string containing a list of key-value pairs. Example: metadata: “key1=value1,key2=value2” |
| **name**  string / required | Name that has to be given to the instance. It is also possible to specify the ID of the instance instead of its name if *state* is *absent*.  This server attribute cannot be updated. |
| **network**  string | Name or ID of a network to attach this instance to. A simpler version of the *nics* parameter, only one of *network* or *nics* should be supplied.  This server attribute cannot be updated. |
| **nics**  list / elements=any | A list of networks to which the instance’s interface should be attached. Networks may be referenced by net-id/net-name/port-id or port-name.  Also this accepts a string containing a list of (net/port)-(id/name) Example: `nics: "net-id=uuid-1,port-name=myport"`  Only one of *network* or *nics* should be supplied.  This server attribute cannot be updated.  **Default:** `[]` |
| **tag**  string | A *tag* for the specific port to be passed via metadata. Eg: `tag: test_tag` |
| **region_name**  string | Name of the region. |
| **reuse_ips**  boolean | When *auto_ip* is true and this option is true, the *auto_ip* code will attempt to re-use unassigned floating ips in the project before creating a new one. It is important to note that it is impossible to safely do this concurrently, so if your use case involves concurrent server creation, it is highly recommended to set this to false and to delete the floating ip associated with a server when the server is deleted using *delete_ips*.  Floating IP support is unstable in this module, use with caution.  This server attribute cannot be updated.  **Choices:**   - `false` - `true` ← (default) |
| **scheduler_hints**  dictionary | Arbitrary key/value pairs to the scheduler for custom use.  This server attribute cannot be updated. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **security_groups**  list / elements=string | Names or IDs of the security groups to which the instance should be added.  On server creation, if *security_groups* is omitted, the API creates the server in the default security group.  Requested security groups are not applied to pre-existing ports.  **Default:** `[]` |
| **state**  string | Should the resource be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **terminate_volume**  boolean | If `true`, delete volume when deleting the instance and if it has been booted from volume(s).  This server attribute cannot be updated.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | The amount of time the module should wait for the instance to get into active state.  **Default:** `180` |
| **userdata**  string | Opaque blob of data which is made available to the instance.  This server attribute cannot be updated. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **volume_size**  integer | The size of the volume to create in GB if booting from volume based on an image.  This server attribute cannot be updated. |
| **volumes**  list / elements=string | A list of preexisting volumes names or ids to attach to the instance  This server attribute cannot be updated.  **Default:** `[]` |
| **wait**  boolean | If the module should wait for the instance to be created.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](server_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](server_module.md#id5)

```yaml+jinja
- name: Create a new instance with metadata and attaches it to a network
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
        security_groups:
        - default
        auto_ip: true

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
        nics: >-
            net-id=4cb08b20-62fe-11e5-9d70-feff819cdc9f,
            net-id=542f0430-62fe-11e5-9d70-feff819cdc9f

- name: Creates a new instance with metadata and attaches it to a network
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
        image: "Ubuntu Server 22.04"
        flavor: "P-1"
        network: "Production"
        userdata: |
          #!/bin/sh
          apt update
          apt -y full-upgrade

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

## [Return Values](server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server**  dictionary | Dictionary describing the server.  **Returned:** On success when *state* is ‘present’. |
| **access_ipv4**  string | IPv4 address that should be used to access this server. May be automatically set by the provider.  **Returned:** success |
| **access_ipv6**  string | IPv6 address that should be used to access this server. May be automatically set by the provider.  **Returned:** success |
| **addresses**  dictionary | A dictionary of addresses this server can be accessed through. The dictionary contains keys such as ‘private’ and ‘public’, each containing a list of dictionaries for addresses of that type. The addresses are contained in a dictionary with keys ‘addr’ and ‘version’, which is either 4 or 6 depending on the protocol of the IP address.  **Returned:** success |
| **admin_password**  string | When a server is first created, it provides the administrator password.  **Returned:** success |
| **attached_volumes**  list / elements=string | A list of an attached volumes. Each item in the list contains at least an ‘id’ key to identify the specific volumes.  **Returned:** success |
| **availability_zone**  string | The name of the availability zone this server is a part of.  **Returned:** success |
| **block_device_mapping**  string | Enables fine grained control of the block device mapping for an instance. This is typically used for booting servers from volumes.  **Returned:** success |
| **compute_host**  string | The name of the compute host on which this instance is running. Appears in the response for administrative users only.  **Returned:** success |
| **config_drive**  string | Indicates whether or not a config drive was used for this server.  **Returned:** success |
| **created_at**  string | Timestamp of when the server was created.  **Returned:** success |
| **description**  string | The description of the server. Before microversion 2.19 this was set to the server name.  **Returned:** success |
| **disk_config**  string | The disk configuration. Either AUTO or MANUAL.  **Returned:** success |
| **flavor**  dictionary | The flavor property as returned from server.  **Returned:** success |
| **flavor_id**  string | The flavor reference, as a ID or full URL, for the flavor to use for this server.  **Returned:** success |
| **has_config_drive**  string | Indicates whether a configuration drive enables metadata injection. Not all cloud providers enable this feature.  **Returned:** success |
| **host_id**  string | An ID representing the host of this server.  **Returned:** success |
| **host_status**  string | The host status.  **Returned:** success |
| **hostname**  string | The hostname set on the instance when it is booted. By default, it appears in the response for administrative users only.  **Returned:** success |
| **hypervisor_hostname**  string | The hypervisor host name. Appears in the response for administrative users only.  **Returned:** success |
| **id**  string | ID of the server.  **Returned:** success |
| **image**  dictionary | The image property as returned from server.  **Returned:** success |
| **image_id**  string | The image reference, as a ID or full URL, for the image to use for this server.  **Returned:** success |
| **instance_name**  string | The instance name. The Compute API generates the instance name from the instance name template. Appears in the response for administrative users only.  **Returned:** success |
| **is_locked**  boolean | The locked status of the server  **Returned:** success |
| **kernel_id**  string | The UUID of the kernel image when using an AMI. Will be null if not. By default, it appears in the response for administrative users only.  **Returned:** success |
| **key_name**  string | The name of an associated keypair.  **Returned:** success |
| **launch_index**  integer | When servers are launched via multiple create, this is the sequence in which the servers were launched. By default, it appears in the response for administrative users only.  **Returned:** success |
| **launched_at**  string | The timestamp when the server was launched.  **Returned:** success |
| **links**  string | A list of dictionaries holding links relevant to this server.  **Returned:** success |
| **max_count**  string | The maximum number of servers to create.  **Returned:** success |
| **metadata**  dictionary | List of tag strings.  **Returned:** success |
| **min_count**  string | The minimum number of servers to create.  **Returned:** success |
| **name**  string | Name of the server  **Returned:** success |
| **networks**  string | A networks object. Required parameter when there are multiple networks defined for the tenant. When you do not specify the networks parameter, the server attaches to the only network created for the current tenant.  **Returned:** success |
| **power_state**  string | The power state of this server.  **Returned:** success |
| **progress**  integer | While the server is building, this value represents the percentage of completion. Once it is completed, it will be 100.  **Returned:** success |
| **project_id**  string | The ID of the project this server is associated with.  **Returned:** success |
| **ramdisk_id**  string | The UUID of the ramdisk image when using an AMI. Will be null if not. By default, it appears in the response for administrative users only.  **Returned:** success |
| **reservation_id**  string | The reservation id for the server. This is an id that can be useful in tracking groups of servers created with multiple create, that will all have the same reservation_id. By default, it appears in the response for administrative users only.  **Returned:** success |
| **root_device_name**  string | The root device name for the instance By default, it appears in the response for administrative users only.  **Returned:** success |
| **scheduler_hints**  dictionary | The dictionary of data to send to the scheduler.  **Returned:** success |
| **security_groups**  list / elements=dictionary | A list of applicable security groups. Each group contains keys for: description, name, id, and rules.  **Returned:** success |
| **server_groups**  list / elements=string | The UUIDs of the server groups to which the server belongs. Currently this can contain at most one entry.  **Returned:** success |
| **status**  string | The state this server is in. Valid values include ‘ACTIVE’, ‘BUILDING’, ‘DELETED’, ‘ERROR’, ‘HARD_REBOOT’, ‘PASSWORD’, ‘PAUSED’, ‘REBOOT’, ‘REBUILD’, ‘RESCUED’, ‘RESIZED’, ‘REVERT_RESIZE’, ‘SHUTOFF’, ‘SOFT_DELETED’, ‘STOPPED’, ‘SUSPENDED’, ‘UNKNOWN’, or ‘VERIFY_RESIZE’.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **task_state**  string | The task state of this server.  **Returned:** success |
| **terminated_at**  string | The timestamp when the server was terminated (if it has been).  **Returned:** success |
| **trusted_image_certificates**  list / elements=string | A list of trusted certificate IDs, that were used during image signature verification to verify the signing certificate.  **Returned:** success |
| **updated_at**  string | Timestamp of when this server was last updated.  **Returned:** success |
| **user_data**  string | Configuration information or scripts to use upon launch. Base64 encoded.  **Returned:** success |
| **user_id**  string | The ID of the owners of this server.  **Returned:** success |
| **vm_state**  string | The VM state of this server.  **Returned:** success |
| **volumes**  list / elements=string | Same as attached_volumes.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
