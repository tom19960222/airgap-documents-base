---
collection: ansible
version: "6"
title: "community.general.lxd_container module – Manage LXD instances"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lxd_container_module.html
fetched_at: 2026-07-27T17:10:41+00:00
---
# community.general.lxd_container module – Manage LXD instances

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.lxd_container`.

- [Synopsis](lxd_container_module.md#synopsis)
- [Parameters](lxd_container_module.md#parameters)
- [Notes](lxd_container_module.md#notes)
- [Examples](lxd_container_module.md#examples)
- [Return Values](lxd_container_module.md#return-values)

## [Synopsis](lxd_container_module.md#id1)

- Management of LXD containers and virtual machines.

## [Parameters](lxd_container_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **architecture**  string | The architecture for the instance (for example `x86_64` or `i686`). See <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1>. |
| **client_cert**  aliases: cert_file  path | The client certificate file path.  If not specified, it defaults to `${HOME}/.config/lxc/client.crt`. |
| **client_key**  aliases: key_file  path | The client certificate key file path.  If not specified, it defaults to `${HOME}/.config/lxc/client.key`. |
| **config**  dictionary | The config for the instance (for example `{"limits.cpu": "2"}`). See <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1>.  If the instance already exists and its “config” values in metadata obtained from the LXD API <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#instances-containers-and-virtual-machines> are different, this module tries to apply the configurations.  The keys starting with `volatile.` are ignored for this comparison when *ignore_volatile_options=true*. |
| **devices**  dictionary | The devices for the instance (for example `{ "rootfs": { "path": "/dev/kvm", "type": "unix-char" }}`). See <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1>. |
| **ephemeral**  boolean | Whether or not the instance is ephemeral (for example `true` or `false`). See <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1>.  Choices:   - `false` - `true` |
| **force_stop**  boolean | If this is true, the `lxd_container` forces to stop the instance when it stops or restarts the instance.  Choices:   - `false` ← (default) - `true` |
| **ignore_volatile_options**  boolean  added in community.general 3.7.0 | If set to `true`, options starting with `volatile.` are ignored. As a result, they are reapplied for each execution.  This default behavior can be changed by setting this option to `false`.  The current default value `true` is deprecated since community.general 4.0.0, and will change to `false` in community.general 6.0.0.  Choices:   - `false` - `true` |
| **name**  string / required | Name of an instance. |
| **profiles**  list / elements=string | Profile to be used by the instance. |
| **project**  string  added in community.general 4.8.0 | Project of an instance. See <https://github.com/lxc/lxd/blob/master/doc/projects.md>. |
| **snap_url**  string | The unix domain socket path when LXD is installed by snap package manager.  Default: `"unix:/var/snap/lxd/common/lxd/unix.socket"` |
| **source**  dictionary | The source for the instance (e.g. { “type”: “image”, “mode”: “pull”, “server”: “<https://images.linuxcontainers.org>”, “protocol”: “lxd”, “alias”: “ubuntu/xenial/amd64” }).  See <https://github.com/lxc/lxd/blob/master/doc/rest-api.md#post-1> for complete API documentation.  Note that `protocol` accepts two choices: `lxd` or `simplestreams`. |
| **state**  string | Define the state of an instance.  Choices:   - `"started"` ← (default) - `"stopped"` - `"restarted"` - `"absent"` - `"frozen"` |
| **target**  string  added in community.general 1.0.0 | For cluster deployments. Will attempt to create an instance on a target node. If the instance exists elsewhere in a cluster, then it will not be replaced or moved. The name should respond to same name of the node you see in `lxc cluster list`. |
| **timeout**  integer | A timeout for changing the state of the instance.  This is also used as a timeout for waiting until IPv4 addresses are set to the all network interfaces in the instance after starting or restarting.  Default: `30` |
| **trust_password**  string | The client trusted password.  You need to set this password on the LXD server before running this module using the following command: `lxc config set core.trust_password <some random password>`. See <https://www.stgraber.org/2016/04/18/lxd-api-direct-interaction/>.  If trust_password is set, this module send a request for authentication before sending any requests. |
| **type**  string  added in community.general 4.1.0 | Instance type can be either `virtual-machine` or `container`.  Choices:   - `"container"` ← (default) - `"virtual-machine"` |
| **url**  string | The unix domain socket path or the https URL for the LXD server.  Default: `"unix:/var/lib/lxd/unix.socket"` |
| **wait_for_container**  boolean  added in community.general 4.4.0 | If set to `true`, the tasks will wait till the task reports a success status when performing container operations.  Choices:   - `false` ← (default) - `true` |
| **wait_for_ipv4_addresses**  boolean | If this is true, the `lxd_container` waits until IPv4 addresses are set to the all network interfaces in the instance after starting or restarting.  Choices:   - `false` ← (default) - `true` |

## [Notes](lxd_container_module.md#id3)

> **Note:**
>
> - Instances can be a container or a virtual machine, both of them must have unique name. If you attempt to create an instance with a name that already existed in the users namespace the module will simply return as “unchanged”.
> - There are two ways to run commands inside a container or virtual machine, using the command module or using the ansible lxd connection plugin bundled in Ansible >= 2.1, the later requires python to be installed in the instance which can be done with the command module.
> - You can copy a file from the host to the instance with the Ansible [ansible.builtin.copy](../../ansible/builtin/copy_module.md#ansible-collections-ansible-builtin-copy-module) and [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) module and the `community.general.lxd` connection plugin. See the example below.
> - You can copy a file in the created instance to the localhost with `command=lxc file pull instance_name/dir/filename filename`. See the first example below.

## [Examples](lxd_container_module.md#id4)

```yaml+jinja
# An example for creating a Ubuntu container and install python
- hosts: localhost
  connection: local
  tasks:
    - name: Create a started container
      community.general.lxd_container:
        name: mycontainer
        ignore_volatile_options: true
        state: started
        source:
          type: image
          mode: pull
          server: https://images.linuxcontainers.org
          protocol: lxd # if you get a 404, try setting protocol: simplestreams
          alias: ubuntu/xenial/amd64
        profiles: ["default"]
        wait_for_ipv4_addresses: true
        timeout: 600

    - name: Check python is installed in container
      delegate_to: mycontainer
      ansible.builtin.raw: dpkg -s python
      register: python_install_check
      failed_when: python_install_check.rc not in [0, 1]
      changed_when: false

    - name: Install python in container
      delegate_to: mycontainer
      ansible.builtin.raw: apt-get install -y python
      when: python_install_check.rc == 1

# An example for creating an Ubuntu 14.04 container using an image fingerprint.
# This requires changing 'server' and 'protocol' key values, replacing the
# 'alias' key with with 'fingerprint' and supplying an appropriate value that
# matches the container image you wish to use.
- hosts: localhost
  connection: local
  tasks:
    - name: Create a started container
      community.general.lxd_container:
        name: mycontainer
        ignore_volatile_options: true
        state: started
        source:
          type: image
          mode: pull
          # Provides current (and older) Ubuntu images with listed fingerprints
          server: https://cloud-images.ubuntu.com/releases
          # Protocol used by 'ubuntu' remote (as shown by 'lxc remote list')
          protocol: simplestreams
          # This provides an Ubuntu 14.04 LTS amd64 image from 20150814.
          fingerprint: e9a8bdfab6dc
        profiles: ["default"]
        wait_for_ipv4_addresses: true
        timeout: 600

# An example for creating container in project other than default
- hosts: localhost
  connection: local
  tasks:
    - name: Create a started container in project mytestproject
      community.general.lxd_container:
        name: mycontainer
        project: mytestproject
        ignore_volatile_options: true
        state: started
        source:
          protocol: simplestreams
          type: image
          mode: pull
          server: https://images.linuxcontainers.org
          alias: ubuntu/20.04/cloud
        profiles: ["default"]
        wait_for_ipv4_addresses: true
        timeout: 600

# An example for deleting a container
- hosts: localhost
  connection: local
  tasks:
    - name: Delete a container
      community.general.lxd_container:
        name: mycontainer
        state: absent
        type: container

# An example for restarting a container
- hosts: localhost
  connection: local
  tasks:
    - name: Restart a container
      community.general.lxd_container:
        name: mycontainer
        state: restarted
        type: container

# An example for restarting a container using https to connect to the LXD server
- hosts: localhost
  connection: local
  tasks:
    - name: Restart a container
      community.general.lxd_container:
        url: https://127.0.0.1:8443
        # These client_cert and client_key values are equal to the default values.
        #client_cert: "{{ lookup('env', 'HOME') }}/.config/lxc/client.crt"
        #client_key: "{{ lookup('env', 'HOME') }}/.config/lxc/client.key"
        trust_password: mypassword
        name: mycontainer
        state: restarted

# Note your container must be in the inventory for the below example.
#
# [containers]
# mycontainer ansible_connection=lxd
#
- hosts:
    - mycontainer
  tasks:
    - name: Copy /etc/hosts in the created container to localhost with name "mycontainer-hosts"
      ansible.builtin.fetch:
        src: /etc/hosts
        dest: /tmp/mycontainer-hosts
        flat: true

# An example for LXD cluster deployments. This example will create two new container on specific
# nodes - 'node01' and 'node02'. In 'target:', 'node01' and 'node02' are names of LXD cluster
# members that LXD cluster recognizes, not ansible inventory names, see: 'lxc cluster list'.
# LXD API calls can be made to any LXD member, in this example, we send API requests to
#'node01.example.com', which matches ansible inventory name.
- hosts: node01.example.com
  tasks:
    - name: Create LXD container
      community.general.lxd_container:
        name: new-container-1
        ignore_volatile_options: true
        state: started
        source:
          type: image
          mode: pull
          alias: ubuntu/xenial/amd64
        target: node01

    - name: Create container on another node
      community.general.lxd_container:
        name: new-container-2
        ignore_volatile_options: true
        state: started
        source:
          type: image
          mode: pull
          alias: ubuntu/xenial/amd64
        target: node02

# An example for creating a virtual machine
- hosts: localhost
  connection: local
  tasks:
    - name: Create container on another node
      community.general.lxd_container:
        name: new-vm-1
        type: virtual-machine
        state: started
        ignore_volatile_options: true
        wait_for_ipv4_addresses: true
        profiles: ["default"]
        source:
          protocol: simplestreams
          type: image
          mode: pull
          server: https://images.linuxcontainers.org
          alias: debian/11
        timeout: 600
```

## [Return Values](lxd_container_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  list / elements=string | List of actions performed for the instance.  Returned: success  Sample: `["create", "start"]` |
| **addresses**  dictionary | Mapping from the network device name to a list of IPv4 addresses in the instance.  Returned: when state is started or restarted  Sample: `{"eth0": ["10.155.92.191"]}` |
| **logs**  list / elements=string | The logs of requests and responses.  Returned: when ansible-playbook is invoked with -vvvv.  Sample: `["(too long to be placed here)"]` |
| **old_state**  string | The old state of the instance.  Returned: when state is started or restarted  Sample: `"stopped"` |

### Authors

- Hiroaki Nakamura (@hnakamur)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
