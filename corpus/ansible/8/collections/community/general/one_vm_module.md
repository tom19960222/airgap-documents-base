---
collection: ansible
version: "8"
title: "community.general.one_vm module – Creates or terminates OpenNebula instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/one_vm_module.html
fetched_at: 2026-07-28T01:48:22+00:00
---
# community.general.one_vm module – Creates or terminates OpenNebula instances

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](one_vm_module.md#ansible-collections-community-general-one-vm-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.one_vm`.

- [Synopsis](one_vm_module.md#synopsis)
- [Requirements](one_vm_module.md#requirements)
- [Parameters](one_vm_module.md#parameters)
- [Attributes](one_vm_module.md#attributes)
- [Examples](one_vm_module.md#examples)
- [Return Values](one_vm_module.md#return-values)

## [Synopsis](one_vm_module.md#id1)

- Manages OpenNebula instances

Aliases: cloud.opennebula.one_vm

## [Requirements](one_vm_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyone

## [Parameters](one_vm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  string | Password of the user to login into OpenNebula RPC server. If not set then the value of the [`ONE_PASSWORD`](../../environment_variables.md#envvar-ONE_PASSWORD) environment variable is used. if both `api_username` or `api_password` are not set, then it will try authenticate with ONE auth file. Default path is “~/.one/one_auth”.  Set environment variable [`ONE_AUTH`](../../environment_variables.md#envvar-ONE_AUTH) to override this path. |
| **api_url**  string | URL of the OpenNebula RPC server.  It is recommended to use HTTPS so that the username/password are not transferred over the network unencrypted.  If not set then the value of the [`ONE_URL`](../../environment_variables.md#envvar-ONE_URL) environment variable is used. |
| **api_username**  string | Name of the user to login into the OpenNebula RPC server. If not set then the value of the [`ONE_USERNAME`](../../environment_variables.md#envvar-ONE_USERNAME) environment variable is used. |
| **attributes**  dictionary | A dictionary of key/value attributes to add to new instances, or for setting `state` of instances with these attributes.  Keys are case insensitive and OpenNebula automatically converts them to upper case.  Be aware `NAME` is a special attribute which sets the name of the VM when it’s deployed.  `#` character(s) can be appended to the `NAME` and the module will automatically add indexes to the names of VMs.  For example’:’ `NAME':' foo-###` would create VMs with names `foo-000`, `foo-001`,…  When used with `count_attributes` and `exact_count` the module will match the base name without the index part.  **Default:** `{}` |
| **count**  integer | Number of instances to launch  **Default:** `1` |
| **count_attributes**  dictionary | A dictionary of key/value attributes that can only be used with `exact_count` to determine how many nodes based on a specific attributes criteria should be deployed. This can be expressed in multiple ways and is shown in the EXAMPLES section. |
| **count_labels**  list / elements=string | A list of labels that can only be used with `exact_count` to determine how many nodes based on a specific labels criteria should be deployed. This can be expressed in multiple ways and is shown in the EXAMPLES section. |
| **cpu**  float | Percentage of CPU divided by 100 required for the new instance. Half a processor is written 0.5. |
| **datastore_id**  integer  *added in community.general 0.2.0* | Name of Datastore to use to create a new instance |
| **datastore_name**  string  *added in community.general 0.2.0* | Name of Datastore to use to create a new instance |
| **disk_saveas**  dictionary | Creates an image from a VM disk.  It is a dictionary where you have to specify `name` of the new image.  Optionally you can specify `disk_id` of the disk you want to save. By default `disk_id` is 0.  **NOTE:** This operation will only be performed on the first VM (if more than one VM ID is passed) and the VM has to be in the `poweredoff` state.  Also this operation will fail if an image with specified `name` already exists. |
| **disk_size**  list / elements=string | The size of the disk created for new instances (in MB, GB, TB,…).  **NOTE:** If The Template hats Multiple Disks the Order of the Sizes is matched against the order specified in `template_id`/`template_name`. |
| **exact_count**  integer | Indicates how many instances that match `count_attributes` and `count_labels` parameters should be deployed. Instances are either created or terminated based on this value.  **NOTE:** Instances with the least IDs will be terminated first. |
| **group_id**  integer | ID of the group which will be set as the group of the instance |
| **hard**  boolean | Reboot, power-off or terminate instances `hard`.  **Choices:**   - `false` ← (default) - `true` |
| **instance_ids**  aliases: ids  list / elements=integer | A list of instance ids used for states: `absent`, `running`, `rebooted`, `poweredoff`. |
| **labels**  list / elements=string | A list of labels to associate with new instances, or for setting `state` of instances with these labels.  **Default:** `[]` |
| **memory**  string | The size of the memory for new instances (in MB, GB, …) |
| **mode**  string | Set permission mode of the instance in octet format, for example `0600` to give owner `use` and `manage` and nothing to group and others. |
| **networks**  list / elements=dictionary | A list of dictionaries with network parameters. See examples for more details.  **Default:** `[]` |
| **owner_id**  integer | ID of the user which will be set as the owner of the instance |
| **persistent**  boolean  *added in community.general 0.2.0* | Create a private persistent copy of the template plus any image defined in DISK, and instantiate that copy.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | `present` - create instances from a template specified with `template_id`/`template_name`.  `running` - run instances  `poweredoff` - power-off instances  `rebooted` - reboot instances  `absent` - terminate instances  **Choices:**   - `"present"` ← (default) - `"absent"` - `"running"` - `"rebooted"` - `"poweredoff"` |
| **template_id**  integer | ID of a VM template to use to create a new instance |
| **template_name**  string | Name of VM template to use to create a new instance |
| **updateconf**  dictionary  *added in community.general 6.3.0* | When `instance_ids` is provided, updates running VMs with the `updateconf` API call.  When new VMs are being created, emulates the `updateconf` API call via direct template merge.  Allows for complete modifications of the `CONTEXT` attribute. |
| **vcpu**  integer | Number of CPUs (cores) new VM will have. |
| **vm_start_on_hold**  boolean | Set to true to put vm on hold while creating  **Choices:**   - `false` ← (default) - `true` |
| **wait**  boolean | Wait for the instance to reach its desired state before returning. Keep in mind if you are waiting for instance to be in running state it doesn’t mean that you will be able to SSH on that machine only that boot process have started on that instance, see ‘wait_for’ example for details.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds  **Default:** `300` |

## [Attributes](one_vm_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](one_vm_module.md#id5)

```yaml+jinja
- name: Create a new instance
  community.general.one_vm:
    template_id: 90
  register: result

- name: Print VM properties
  ansible.builtin.debug:
    msg: result

- name: Deploy a new VM on hold
  community.general.one_vm:
    template_name: 'app1_template'
    vm_start_on_hold: 'True'

- name: Deploy a new VM and set its name to 'foo'
  community.general.one_vm:
    template_name: 'app1_template'
    attributes:
      name: foo

- name: Deploy a new VM and set its group_id and mode
  community.general.one_vm:
    template_id: 90
    group_id: 16
    mode: 660

- name: Deploy a new VM  as persistent
  community.general.one_vm:
    template_id: 90
    persistent: true

- name: Change VM's permissions to 640
  community.general.one_vm:
    instance_ids: 5
    mode: 640

- name: Deploy 2 new instances and set memory, vcpu, disk_size and 3 networks
  community.general.one_vm:
    template_id: 15
    disk_size: 35.2 GB
    memory: 4 GB
    vcpu: 4
    count: 2
    networks:
      - NETWORK_ID: 27
      - NETWORK: "default-network"
        NETWORK_UNAME: "app-user"
        SECURITY_GROUPS: "120,124"
      - NETWORK_ID: 27
        SECURITY_GROUPS: "10"

- name: Deploy a new instance which uses a Template with two Disks
  community.general.one_vm:
    template_id: 42
    disk_size:
      - 35.2 GB
      - 50 GB
    memory: 4 GB
    vcpu: 4
    count: 1
    networks:
      - NETWORK_ID: 27

- name: "Deploy an new instance with attribute 'bar: bar1' and set its name to 'foo'"
  community.general.one_vm:
    template_id: 53
    attributes:
      name: foo
      bar: bar1

- name: "Enforce that 2 instances with attributes 'foo1: app1' and 'foo2: app2' are deployed"
  community.general.one_vm:
    template_id: 53
    attributes:
      foo1: app1
      foo2: app2
    exact_count: 2
    count_attributes:
      foo1: app1
      foo2: app2

- name: Enforce that 4 instances with an attribute 'bar' are deployed
  community.general.one_vm:
    template_id: 53
    attributes:
      name: app
      bar: bar2
    exact_count: 4
    count_attributes:
      bar:

# Deploy 2 new instances with attribute 'foo: bar' and labels 'app1' and 'app2' and names in format 'fooapp-##'
# Names will be: fooapp-00 and fooapp-01
- name: Deploy 2 new instances
  community.general.one_vm:
    template_id: 53
    attributes:
      name: fooapp-##
      foo: bar
    labels:
      - app1
      - app2
    count: 2

# Deploy 2 new instances with attribute 'app: app1' and names in format 'fooapp-###'
# Names will be: fooapp-002 and fooapp-003
- name: Deploy 2 new instances
  community.general.one_vm:
    template_id: 53
    attributes:
      name: fooapp-###
      app: app1
    count: 2

# Reboot all instances with name in format 'fooapp-#'
# Instances 'fooapp-00', 'fooapp-01', 'fooapp-002' and 'fooapp-003' will be rebooted
- name: Reboot all instances with names in a certain format
  community.general.one_vm:
    attributes:
      name: fooapp-#
    state: rebooted

# Enforce that only 1 instance with name in format 'fooapp-#' is deployed
# The task will delete oldest instances, so only the 'fooapp-003' will remain
- name: Enforce that only 1 instance with name in a certain format is deployed
  community.general.one_vm:
    template_id: 53
    exact_count: 1
    count_attributes:
      name: fooapp-#

- name: Deploy an new instance with a network
  community.general.one_vm:
    template_id: 53
    networks:
      - NETWORK_ID: 27
  register: vm

- name: Wait for SSH to come up
  ansible.builtin.wait_for_connection:
  delegate_to: '{{ vm.instances[0].networks[0].ip }}'

- name: Terminate VMs by ids
  community.general.one_vm:
    instance_ids:
      - 153
      - 160
    state: absent

- name: Reboot all VMs that have labels 'foo' and 'app1'
  community.general.one_vm:
    labels:
      - foo
      - app1
    state: rebooted

- name: "Fetch all VMs that have name 'foo' and attribute 'app: bar'"
  community.general.one_vm:
    attributes:
      name: foo
      app: bar
  register: results

- name: Deploy 2 new instances with labels 'foo1' and 'foo2'
  community.general.one_vm:
    template_name: app_template
    labels:
      - foo1
      - foo2
    count: 2

- name: Enforce that only 1 instance with label 'foo1' will be running
  community.general.one_vm:
    template_name: app_template
    labels:
      - foo1
    exact_count: 1
    count_labels:
      - foo1

- name: Terminate all instances that have attribute foo
  community.general.one_vm:
    template_id: 53
    exact_count: 0
    count_attributes:
      foo:

- name: "Power-off the VM and save VM's disk with id=0 to the image with name 'foo-image'"
  community.general.one_vm:
    instance_ids: 351
    state: poweredoff
    disk_saveas:
      name: foo-image

- name: "Save VM's disk with id=1 to the image with name 'bar-image'"
  community.general.one_vm:
    instance_ids: 351
    disk_saveas:
      name: bar-image
      disk_id: 1

- name: "Deploy 2 new instances with a custom 'start script'"
  community.general.one_vm:
    template_name: app_template
    count: 2
    updateconf:
      CONTEXT:
        START_SCRIPT: ip r r 169.254.16.86/32 dev eth0

- name: "Add a custom 'start script' to a running VM"
  community.general.one_vm:
    instance_ids: 351
    updateconf:
      CONTEXT:
        START_SCRIPT: ip r r 169.254.16.86/32 dev eth0

- name: "Update SSH public keys inside the VM's context"
  community.general.one_vm:
    instance_ids: 351
    updateconf:
      CONTEXT:
        SSH_PUBLIC_KEY: |-
          ssh-rsa ...
          ssh-ed25519 ...
```

## [Return Values](one_vm_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | a list of instances info whose state is changed or which are fetched with `instance_ids` option.  **Returned:** success |
| **attributes**  dictionary | A dictionary of key/values attributes that are associated with the instance  **Returned:** success  **Sample:** `{"HYPERVISOR": "kvm", "LOGO": "images/logos/centos.png", "TE_GALAXY": "bar", "USER_INPUTS": null}` |
| **cpu**  float | Percentage of CPU divided by 100  **Returned:** success  **Sample:** `0.2` |
| **disk_size**  string | The size of the disk in MB  **Returned:** success  **Sample:** `"20480 MB"` |
| **group_id**  integer | vm’s group id  **Returned:** success  **Sample:** `1` |
| **group_name**  string | vm’s group name  **Returned:** success  **Sample:** `"one-users"` |
| **labels**  list / elements=string | A list of string labels that are associated with the instance  **Returned:** success  **Sample:** `["foo", "spec-label"]` |
| **lcm_state**  string | lcm state of an instance that is only relevant when the state is ACTIVE  **Returned:** success  **Sample:** `"RUNNING"` |
| **memory**  string | The size of the memory in MB  **Returned:** success  **Sample:** `"4096 MB"` |
| **mode**  string | vm’s mode  **Returned:** success  **Sample:** `"660"` |
| **networks**  list / elements=string | a list of dictionaries with info about IP, NAME, MAC, SECURITY_GROUPS for each NIC  **Returned:** success  **Sample:** `[{"ip": "10.120.5.33", "mac": "02:00:0a:78:05:21", "name": "default-test-private", "security_groups": "0,10"}, {"ip": "10.120.5.34", "mac": "02:00:0a:78:05:22", "name": "default-test-private", "security_groups": "0"}]` |
| **owner_id**  integer | vm’s owner id  **Returned:** success  **Sample:** `143` |
| **owner_name**  string | vm’s owner name  **Returned:** success  **Sample:** `"app-user"` |
| **state**  string | state of an instance  **Returned:** success  **Sample:** `"ACTIVE"` |
| **template_id**  integer | vm’s template id  **Returned:** success  **Sample:** `153` |
| **updateconf**  dictionary  *added in community.general 6.3.0* | A dictionary of key/values attributes that are set with the updateconf API call.  **Returned:** success  **Sample:** `{"CONTEXT": {"SSH_PUBLIC_KEY": "ssh-rsa ...\nssh-ed25519 ...", "START_SCRIPT": "ip r r 169.254.16.86/32 dev eth0"}, "OS": {"ARCH": "x86_64"}}` |
| **uptime_h**  integer | Uptime of the instance in hours  **Returned:** success  **Sample:** `35` |
| **vcpu**  integer | Number of CPUs (cores)  **Returned:** success  **Sample:** `2` |
| **vm_id**  integer | vm id  **Returned:** success  **Sample:** `153` |
| **vm_name**  string | vm name  **Returned:** success  **Sample:** `"foo"` |
| **instances_ids**  list / elements=string | a list of instances ids whose state is changed or which are fetched with `instance_ids` option.  **Returned:** success  **Sample:** `[1234, 1235]` |
| **tagged_instances**  complex | A list of instances info based on a specific attributes and/or  labels that are specified with `count_attributes` and `count_labels`  options.  **Returned:** success |
| **attributes**  dictionary | A dictionary of key/values attributes that are associated with the instance  **Returned:** success  **Sample:** `{"HYPERVISOR": "kvm", "LOGO": "images/logos/centos.png", "TE_GALAXY": "bar", "USER_INPUTS": null}` |
| **cpu**  float | Percentage of CPU divided by 100  **Returned:** success  **Sample:** `0.2` |
| **disk_size**  list / elements=string | The size of the disk in MB  **Returned:** success  **Sample:** `["20480 MB", "10240 MB"]` |
| **group_id**  integer | vm’s group id  **Returned:** success  **Sample:** `1` |
| **group_name**  string | vm’s group name  **Returned:** success  **Sample:** `"one-users"` |
| **labels**  list / elements=string | A list of string labels that are associated with the instance  **Returned:** success  **Sample:** `["foo", "spec-label"]` |
| **lcm_state**  string | lcm state of an instance that is only relevant when the state is ACTIVE  **Returned:** success  **Sample:** `"RUNNING"` |
| **memory**  string | The size of the memory in MB  **Returned:** success  **Sample:** `"4096 MB"` |
| **mode**  string | vm’s mode  **Returned:** success  **Sample:** `"660"` |
| **networks**  list / elements=string | a list of dictionaries with info about IP, NAME, MAC, SECURITY_GROUPS for each NIC  **Returned:** success  **Sample:** `[{"ip": "10.120.5.33", "mac": "02:00:0a:78:05:21", "name": "default-test-private", "security_groups": "0,10"}, {"ip": "10.120.5.34", "mac": "02:00:0a:78:05:22", "name": "default-test-private", "security_groups": "0"}]` |
| **owner_id**  integer | vm’s user id  **Returned:** success  **Sample:** `143` |
| **owner_name**  string | vm’s user name  **Returned:** success  **Sample:** `"app-user"` |
| **state**  string | state of an instance  **Returned:** success  **Sample:** `"ACTIVE"` |
| **template_id**  integer | vm’s template id  **Returned:** success  **Sample:** `153` |
| **updateconf**  dictionary  *added in community.general 6.3.0* | A dictionary of key/values attributes that are set with the updateconf API call  **Returned:** success  **Sample:** `{"CONTEXT": {"SSH_PUBLIC_KEY": "ssh-rsa ...\nssh-ed25519 ...", "START_SCRIPT": "ip r r 169.254.16.86/32 dev eth0"}, "OS": {"ARCH": "x86_64"}}` |
| **uptime_h**  integer | Uptime of the instance in hours  **Returned:** success  **Sample:** `35` |
| **vcpu**  integer | Number of CPUs (cores)  **Returned:** success  **Sample:** `2` |
| **vm_id**  integer | vm id  **Returned:** success  **Sample:** `153` |
| **vm_name**  string | vm name  **Returned:** success  **Sample:** `"foo"` |

### Authors

- Milan Ilic (@ilicmilan)
- Jan Meerkamp (@meerkampdvv)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
