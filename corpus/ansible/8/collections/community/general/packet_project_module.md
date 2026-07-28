---
collection: ansible
version: "8"
title: "community.general.packet_project module – Create/delete a project in Packet host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/packet_project_module.html
fetched_at: 2026-07-28T01:48:50+00:00
---
# community.general.packet_project module – Create/delete a project in Packet host

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
> see [Requirements](packet_project_module.md#ansible-collections-community-general-packet-project-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_project`.

New in community.general 0.2.0

- [Synopsis](packet_project_module.md#synopsis)
- [Requirements](packet_project_module.md#requirements)
- [Parameters](packet_project_module.md#parameters)
- [Attributes](packet_project_module.md#attributes)
- [Examples](packet_project_module.md#examples)
- [Return Values](packet_project_module.md#return-values)

## [Synopsis](packet_project_module.md#id1)

- Create/delete a project in Packet host.
- API is documented at <https://www.packet.com/developers/api/#projects>.

Aliases: cloud.packet.packet_project

## [Requirements](packet_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- packet-python >= 1.40

## [Parameters](packet_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Packet api token. You can also supply it in environment variable `PACKET_API_TOKEN`. |
| **custom_data**  string | Custom data about the project to create. |
| **id**  string | UUID of the project which you want to remove. |
| **name**  string | Name for/of the project. |
| **org_id**  string | UUID of the organization to create a project for.  When blank, the API assumes the default organization. |
| **payment_method**  string | Payment method is name of one of the payment methods available to your user.  When blank, the API assumes the default payment method. |
| **state**  string | Indicate desired state of the target.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](packet_project_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](packet_project_module.md#id5)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass the api token in module param auth_token.

- name: Create new project
  hosts: localhost
  tasks:
    community.general.packet_project:
      name: "new project"

- name: Create new project within non-default organization
  hosts: localhost
  tasks:
    community.general.packet_project:
      name: "my org project"
      org_id: a4cc87f9-e00f-48c2-9460-74aa60beb6b0

- name: Remove project by id
  hosts: localhost
  tasks:
    community.general.packet_project:
      state: absent
      id: eef49903-7a09-4ca1-af67-4087c29ab5b6

- name: Create new project with non-default billing method
  hosts: localhost
  tasks:
    community.general.packet_project:
      name: "newer project"
      payment_method: "the other visa"
```

## [Return Values](packet_project_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if a project was created or removed.  **Returned:** success  **Sample:** `true` |
| **id**  string | UUID of addressed project.  **Returned:** success |
| **name**  string | Name of addressed project.  **Returned:** success |

### Authors

- Tomas Karasek (@t0mk)
- Nurfet Becirevic (@nurfet-becirevic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
