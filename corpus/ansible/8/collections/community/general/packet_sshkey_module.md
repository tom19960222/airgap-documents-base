---
collection: ansible
version: "8"
title: "community.general.packet_sshkey module – Create/delete an SSH key in Packet host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/packet_sshkey_module.html
fetched_at: 2026-07-28T01:48:50+00:00
---
# community.general.packet_sshkey module – Create/delete an SSH key in Packet host

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
> see [Requirements](packet_sshkey_module.md#ansible-collections-community-general-packet-sshkey-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_sshkey`.

- [Synopsis](packet_sshkey_module.md#synopsis)
- [Requirements](packet_sshkey_module.md#requirements)
- [Parameters](packet_sshkey_module.md#parameters)
- [Attributes](packet_sshkey_module.md#attributes)
- [Examples](packet_sshkey_module.md#examples)
- [Return Values](packet_sshkey_module.md#return-values)

## [Synopsis](packet_sshkey_module.md#id1)

- Create/delete an SSH key in Packet host.
- API is documented at <https://www.packet.net/help/api/#page:ssh-keys,header:ssh-keys-ssh-keys-post>.

Aliases: cloud.packet.packet_sshkey

## [Requirements](packet_sshkey_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- packet-python

## [Parameters](packet_sshkey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Packet API token. You can also supply it in environment variable `PACKET_API_TOKEN`. |
| **fingerprint**  string | Fingerprint of the key which you want to remove. |
| **id**  string | UUID of the key which you want to remove. |
| **key**  string | Public Key string ({type} {base64 encoded key} {description}). |
| **key_file**  path | File with the public key. |
| **label**  aliases: name  string | Label for the key. If you keep it empty, it will be read from key string. |
| **state**  string | Indicate desired state of the target.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](packet_sshkey_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](packet_sshkey_module.md#id5)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass the api token in module param auth_token.

- name: Create sshkey from string
  hosts: localhost
  tasks:
    community.general.packet_sshkey:
      key: "{{ lookup('file', 'my_packet_sshkey.pub') }}"

- name: Create sshkey from file
  hosts: localhost
  tasks:
    community.general.packet_sshkey:
      label: key from file
      key_file: ~/ff.pub

- name: Remove sshkey by id
  hosts: localhost
  tasks:
    community.general.packet_sshkey:
      state: absent
      id: eef49903-7a09-4ca1-af67-4087c29ab5b6
```

## [Return Values](packet_sshkey_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if a sshkey was created or removed.  **Returned:** always  **Sample:** `true` |
| **sshkeys**  list / elements=string | Information about sshkeys that were created/removed.  **Returned:** always  **Sample:** `[{"fingerprint": "5c:93:74:7c:ed:07:17:62:28:75:79:23:d6:08:93:46", "id": "41d61bd8-3342-428b-a09c-e67bdd18a9b7", "key": "ssh-dss AAAAB3NzaC1kc3MAAACBAIfNT5S0ncP4BBJBYNhNPxFF9lqVhfPeu6SM1LoCocxqDc1AT3zFRi8hjIf6TLZ2AA4FYbcAWxLMhiBxZRVldT9GdBXile78kAK5z3bKTwq152DCqpxwwbaTIggLFhsU8wrfBsPWnDuAxZ0h7mmrCjoLIE3CNLDA/NmV3iB8xMThAAAAFQCStcesSgR1adPORzBxTr7hug92LwAAAIBOProm3Gk+HWedLyE8IfofLaOeRnbBRHAOL4z0SexKkVOnQ/LGN/uDIIPGGBDYTvXgKZT+jbHeulRJ2jKgfSpGKN4JxFQ8uzVH492jEiiUJtT72Ss1dCV4PmyERVIw+f54itihV3z/t25dWgowhb0int8iC/OY3cGodlmYb3wdcQAAAIBuLbB45djZXzUkOTzzcRDIRfhaxo5WipbtEM2B1fuBt2gyrvksPpH/LK6xTjdIIb0CxPu4OCxwJG0aOz5kJoRnOWIXQGhH7VowrJhsqhIc8gN9ErbO5ea8b1L76MNcAotmBDeTUiPw01IJ8MdDxfmcsCslJKgoRKSmQpCwXQtN2g== tomk@hp2", "label": "mynewkey33"}]` |

### Authors

- Tomas Karasek (@t0mk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
