---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_instance_group module – Creates a GCP InstanceGroup"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_instance_group_module.html
fetched_at: 2026-07-28T02:32:13+00:00
---
# google.cloud.gcp_compute_instance_group module – Creates a GCP InstanceGroup

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_compute_instance_group_module.md#ansible-collections-google-cloud-gcp-compute-instance-group-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_instance_group`.

- [Synopsis](gcp_compute_instance_group_module.md#synopsis)
- [Requirements](gcp_compute_instance_group_module.md#requirements)
- [Parameters](gcp_compute_instance_group_module.md#parameters)
- [Examples](gcp_compute_instance_group_module.md#examples)
- [Return Values](gcp_compute_instance_group_module.md#return-values)

## [Synopsis](gcp_compute_instance_group_module.md#id1)

- Represents an Instance Group resource. Instance groups are self-managed and can contain identical or different instances. Instance groups do not use an instance template. Unlike managed instance groups, you must create and add instances to an instance group manually.

## [Requirements](gcp_compute_instance_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_instance_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. Provide this property when you create the resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **instances**  list / elements=dictionary | The list of instances associated with this InstanceGroup.  All instances must be created before being added to an InstanceGroup.  All instances not in this list will be removed from the InstanceGroup and will not be deleted.  Only the full identifier of the instance will be returned. |
| **name**  string | The name of the instance group.  The name must be 1-63 characters long, and comply with RFC1035. |
| **named_ports**  list / elements=dictionary | Assigns a name to a port number.  For example: {name: “http”, port: 80}.  This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports.  For example: [{name: “http”, port: 80},{name: “http”, port: 8080}] Named ports apply to all instances in this instance group. |
| **name**  string | The name for this named port.  The name must be 1-63 characters long, and comply with RFC1035. |
| **port**  integer | The port number, which can be a value between 1 and 65535. |
| **network**  dictionary | The network to which all instances in the instance group belong.  This field represents a link to a Network resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_network task and then set this network field to “{{ name-of-resource }}” |
| **project**  string | The Google Cloud Platform project to use. |
| **region**  string | The region where the instance group is located (for regional resources). |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnetwork**  dictionary | The subnetwork to which all instances in the instance group belong.  This field represents a link to a Subnetwork resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork task and then set this subnetwork field to “{{ name-of-resource }}” |
| **zone**  string / required | A reference to the zone where the instance group resides. |

## [Examples](gcp_compute_instance_group_module.md#id4)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-instancegroup
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a instance group
  google.cloud.gcp_compute_instance_group:
    name: test_object
    named_ports:
    - name: ansible
      port: 1234
    network: "{{ network }}"
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_instance_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource. Provide this property when you create the resource.  **Returned:** success |
| **id**  integer | A unique identifier for this instance group.  **Returned:** success |
| **instances**  list / elements=string | The list of instances associated with this InstanceGroup.  All instances must be created before being added to an InstanceGroup.  All instances not in this list will be removed from the InstanceGroup and will not be deleted.  Only the full identifier of the instance will be returned.  **Returned:** success |
| **name**  string | The name of the instance group.  The name must be 1-63 characters long, and comply with RFC1035.  **Returned:** success |
| **namedPorts**  complex | Assigns a name to a port number.  For example: {name: “http”, port: 80}.  This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports.  For example: [{name: “http”, port: 80},{name: “http”, port: 8080}] Named ports apply to all instances in this instance group.  **Returned:** success |
| **name**  string | The name for this named port.  The name must be 1-63 characters long, and comply with RFC1035.  **Returned:** success |
| **port**  integer | The port number, which can be a value between 1 and 65535.  **Returned:** success |
| **network**  dictionary | The network to which all instances in the instance group belong.  **Returned:** success |
| **region**  string | The region where the instance group is located (for regional resources).  **Returned:** success |
| **subnetwork**  dictionary | The subnetwork to which all instances in the instance group belong.  **Returned:** success |
| **zone**  string | A reference to the zone where the instance group resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
