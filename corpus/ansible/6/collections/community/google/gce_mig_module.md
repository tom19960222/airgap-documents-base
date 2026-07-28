---
collection: ansible
version: "6"
title: "community.google.gce_mig module – Create, Update or Destroy a Managed Instance Group (MIG)."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gce_mig_module.html
fetched_at: 2026-07-27T17:15:20+00:00
---
# community.google.gce_mig module – Create, Update or Destroy a Managed Instance Group (MIG).

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gce_mig_module.md#ansible-collections-community-google-gce-mig-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_mig`.

- [Synopsis](gce_mig_module.md#synopsis)
- [Requirements](gce_mig_module.md#requirements)
- [Parameters](gce_mig_module.md#parameters)
- [Notes](gce_mig_module.md#notes)
- [Examples](gce_mig_module.md#examples)
- [Return Values](gce_mig_module.md#return-values)

## [Synopsis](gce_mig_module.md#id1)

- Create, Update or Destroy a Managed Instance Group (MIG). See <https://cloud.google.com/compute/docs/instance-groups> for an overview. Full install/configuration instructions for the gce\* modules can be found in the comments of ansible/test/gce_tests.py.

## [Requirements](gce_mig_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 1.2.0

## [Parameters](gce_mig_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoscaling**  dictionary | A dictionary of configuration for the autoscaler. ‘enabled (bool)’, ‘name (str)’ and policy.max_instances (int) are required fields if autoscaling is used. See <https://cloud.google.com/compute/docs/reference/beta/autoscalers> for more information on Autoscaling. |
| **credentials_file**  path | Path to the JSON file associated with the service account email |
| **name**  string / required | Name of the Managed Instance Group. |
| **named_ports**  list / elements=string | Define named ports that backend services can forward data to. Format is a a list of name:port dictionaries. |
| **pem_file**  path | path to the pem file associated with the service account email This option is deprecated. Use ‘credentials_file’. |
| **project_id**  string | GCE project ID |
| **recreate_instances**  boolean | Recreate MIG instances.  Choices:   - `false` ← (default) - `true` |
| **service_account_email**  string | service account email |
| **service_account_permissions**  list / elements=string | service account permissions |
| **size**  integer | Size of Managed Instance Group. If MIG already exists, it will be resized to the number provided here. Required for creating MIGs. |
| **state**  string | desired state of the resource  Choices:   - `"absent"` - `"present"` ← (default) |
| **template**  string | Instance Template to be used in creating the VMs. See <https://cloud.google.com/compute/docs/instance-templates> to learn more about Instance Templates. Required for creating MIGs. |
| **zone**  string / required | The GCE zone to use for this Managed Instance Group. |

## [Notes](gce_mig_module.md#id4)

> **Note:**
>
> - Resizing and Recreating VM are also supported.
> - An existing instance template is required in order to create a Managed Instance Group.

## [Examples](gce_mig_module.md#id5)

```yaml+jinja
# Following playbook creates, rebuilds instances, resizes and then deletes a MIG.
# Notes:
# - Two valid Instance Templates must exist in your GCE project in order to run
#   this playbook.  Change the fields to match the templates used in your
#   project.
# - The use of the 'pause' module is not required, it is just for convenience.
- name: Managed Instance Group Example
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create MIG
      community.google.gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 1
        template: my-instance-template-1
        named_ports:
        - name: http
          port: 80
        - name: foobar
          port: 82

    - name: Pause for 30 seconds
      ansible.builtin.pause:
        seconds: 30

    - name: Recreate MIG Instances with Instance Template change.
      community.google.gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        template: my-instance-template-2-small
        recreate_instances: yes

    - name: Pause for 30 seconds
      ansible.builtin.pause:
        seconds: 30

    - name: Resize MIG
      community.google.gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 3

    - name: Update MIG with Autoscaler
      community.google.gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: present
        size: 3
        template: my-instance-template-2-small
        recreate_instances: yes
        autoscaling:
          enabled: yes
          name: my-autoscaler
          policy:
            min_instances: 2
            max_instances: 5
            cool_down_period: 37
            cpu_utilization:
              target: .39
            load_balancing_utilization:
              target: 0.4

    - name: Pause for 30 seconds
      ansible.builtin.pause:
        seconds: 30

    - name: Delete MIG
      community.google.gce_mig:
        name: ansible-mig-example
        zone: us-central1-c
        state: absent
        autoscaling:
          enabled: no
          name: my-autoscaler
```

## [Return Values](gce_mig_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created_autoscaler**  boolean | True if Autoscaler was attempted and created. False otherwise.  Returned: When the creation of an Autoscaler was attempted.  Sample: `true` |
| **created_instances**  list / elements=string | Names of instances created.  Returned: When instances are created.  Sample: `["ansible-mig-new-0k4y", "ansible-mig-new-0zk5", "ansible-mig-new-kp68"]` |
| **deleted_autoscaler**  boolean | True if an Autoscaler delete attempted and succeeded. False returned if delete failed.  Returned: When the delete of an Autoscaler was attempted.  Sample: `true` |
| **deleted_instances**  list / elements=string | Names of instances deleted.  Returned: When instances are deleted.  Sample: `["ansible-mig-new-0k4y", "ansible-mig-new-0zk5", "ansible-mig-new-kp68"]` |
| **name**  string | Name of the Managed Instance Group.  Returned: changed  Sample: `"my-managed-instance-group"` |
| **named_ports**  list / elements=string | list of named ports acted upon  Returned: when named_ports are initially set or updated  Sample: `[{"name": "http", "port": 80}, {"name": "foo", "port": 82}]` |
| **recreated_instances**  list / elements=string | Names of instances recreated.  Returned: When instances are recreated.  Sample: `["ansible-mig-new-0k4y", "ansible-mig-new-0zk5", "ansible-mig-new-kp68"]` |
| **resize_created_instances**  list / elements=string | Names of instances created during resizing.  Returned: When a resize results in the creation of instances.  Sample: `["ansible-mig-new-0k4y", "ansible-mig-new-0zk5", "ansible-mig-new-kp68"]` |
| **resize_deleted_instances**  list / elements=string | Names of instances deleted during resizing.  Returned: When a resize results in the deletion of instances.  Sample: `["ansible-mig-new-0k4y", "ansible-mig-new-0zk5", "ansible-mig-new-kp68"]` |
| **set_named_ports**  boolean | True if the named_ports have been set  Returned: named_ports have been set  Sample: `true` |
| **size**  integer | Number of VMs in Managed Instance Group.  Returned: changed  Sample: `4` |
| **template**  string | Instance Template to use for VMs. Must exist prior to using with MIG.  Returned: changed  Sample: `"my-instance-template"` |
| **updated_autoscaler**  boolean | True if an Autoscaler update was attempted and succeeded. False returned if update failed.  Returned: When the update of an Autoscaler was attempted.  Sample: `true` |
| **updated_named_ports**  boolean | True if the named_ports have been updated  Returned: named_ports have been updated  Sample: `true` |
| **zone**  string | Zone in which to launch MIG.  Returned: always  Sample: `"us-central1-b"` |

### Authors

- Tom Melendez (@supertom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
