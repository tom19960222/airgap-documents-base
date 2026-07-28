---
collection: ansible
version: "8"
title: "google.cloud.gcp_compute_target_instance module – Creates a GCP TargetInstance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_compute_target_instance_module.html
fetched_at: 2026-07-28T02:32:53+00:00
---
# google.cloud.gcp_compute_target_instance module – Creates a GCP TargetInstance

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
> see [Requirements](gcp_compute_target_instance_module.md#ansible-collections-google-cloud-gcp-compute-target-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_compute_target_instance`.

- [Synopsis](gcp_compute_target_instance_module.md#synopsis)
- [Requirements](gcp_compute_target_instance_module.md#requirements)
- [Parameters](gcp_compute_target_instance_module.md#parameters)
- [Notes](gcp_compute_target_instance_module.md#notes)
- [Examples](gcp_compute_target_instance_module.md#examples)
- [Return Values](gcp_compute_target_instance_module.md#return-values)

## [Synopsis](gcp_compute_target_instance_module.md#id1)

- Represents a TargetInstance resource which defines an endpoint instance that terminates traffic of certain protocols. In particular, they are used in Protocol Forwarding, where forwarding rules can send packets to a non-NAT’ed target instance. Each target instance contains a single virtual machine instance that receives and handles traffic from the corresponding forwarding rules.

## [Requirements](gcp_compute_target_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_compute_target_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **description**  string | An optional description of this resource. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **instance**  dictionary / required | A URL to the virtual machine instance that handles traffic for this target instance. Accepts self-links or the partial paths with format `projects/project/zones/zone/instances/instance’ or `zones/zone/instances/instance` .  This field represents a link to a Instance resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘selfLink’ and value of your resource’s selfLink Alternatively, you can add `register: name-of-resource` to a gcp_compute_instance task and then set this instance field to “{{ name-of-resource }}” |
| **name**  string / required | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| **nat_policy**  string | NAT option controlling how IPs are NAT’ed to the instance.  Currently only NO_NAT (default value) is supported.  Some valid choices include: “NO_NAT”  **Default:** `"NO_NAT"` |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **zone**  string / required | URL of the zone where the target instance resides. |

## [Notes](gcp_compute_target_instance_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/compute/docs/reference/v1/targetInstances>
> - Using Protocol Forwarding: <https://cloud.google.com/compute/docs/protocol-forwarding>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_compute_target_instance_module.md#id5)

```yaml+jinja
- name: create a network
  google.cloud.gcp_compute_network:
    name: network-instance
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a instance
  google.cloud.gcp_compute_instance:
    name: "{{ resource_name }}"
    machine_type: n1-standard-1
    disks:
    - auto_delete: 'true'
      boot: 'true'
      initialize_params:
        source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts
    labels:
      environment: production
    network_interfaces:
    - network: "{{ network }}"
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instance

- name: create a target instance
  google.cloud.gcp_compute_target_instance:
    name: target
    instance: "{{ instance }}"
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_compute_target_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **creationTimestamp**  string | Creation timestamp in RFC3339 text format.  **Returned:** success |
| **description**  string | An optional description of this resource.  **Returned:** success |
| **instance**  dictionary | A URL to the virtual machine instance that handles traffic for this target instance. Accepts self-links or the partial paths with format `projects/project/zones/zone/instances/instance’ or `zones/zone/instances/instance` .  **Returned:** success |
| **name**  string | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]\*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  **Returned:** success |
| **natPolicy**  string | NAT option controlling how IPs are NAT’ed to the instance.  Currently only NO_NAT (default value) is supported.  **Returned:** success |
| **zone**  string | URL of the zone where the target instance resides.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
