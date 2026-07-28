---
collection: ansible
version: "8"
title: "community.google.gce_eip module – Create or Destroy Global or Regional External IP addresses."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gce_eip_module.html
fetched_at: 2026-07-28T01:53:03+00:00
---
# community.google.gce_eip module – Create or Destroy Global or Regional External IP addresses.

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
> see [Requirements](gce_eip_module.md#ansible-collections-community-google-gce-eip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gce_eip`.

- [Synopsis](gce_eip_module.md#synopsis)
- [Requirements](gce_eip_module.md#requirements)
- [Parameters](gce_eip_module.md#parameters)
- [Notes](gce_eip_module.md#notes)
- [Examples](gce_eip_module.md#examples)
- [Return Values](gce_eip_module.md#return-values)

## [Synopsis](gce_eip_module.md#id1)

- Create (reserve) or Destroy (release) Regional or Global IP Addresses. See <https://cloud.google.com/compute/docs/configure-instance-ip-addresses#reserve_new_static> for more on reserving static addresses.

## [Requirements](gce_eip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- apache-libcloud >= 0.19.0

## [Parameters](gce_eip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  path | The path to the JSON file associated with the service account email. |
| **name**  string / required | Name of Address. |
| **pem_file**  path | The path to the PEM file associated with the service account email.  This option is deprecated and may be removed in a future release. Use *credentials_file* instead. |
| **project_id**  string | The Google Cloud Platform project ID to use. |
| **region**  string / required | Region to create the address in. Set to ‘global’ to create a global address. |
| **service_account_email**  string | service account email |
| **service_account_permissions**  list / elements=string | service account permissions |
| **state**  string | The state the address should be in. `present` or `absent` are the only valid options.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gce_eip_module.md#id4)

> **Note:**
>
> - Global addresses can only be used with Global Forwarding Rules.

## [Examples](gce_eip_module.md#id5)

```yaml+jinja
- name: Create a Global external IP address
  community.google.gce_eip:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    name: my-global-ip
    region: global
    state: present

- name: Create a Regional external IP address
  community.google.gce_eip:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    name: my-global-ip
    region: us-east1
    state: present
```

## [Return Values](gce_eip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | IP address being operated on  **Returned:** always  **Sample:** `"35.186.222.233"` |
| **name**  string | name of the address being operated on  **Returned:** always  **Sample:** `"my-address"` |
| **region**  string | Which region an address belongs.  **Returned:** always  **Sample:** `"global"` |

### Authors

- Tom Melendez (@supertom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
