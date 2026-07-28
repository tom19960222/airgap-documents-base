---
collection: ansible
version: "6"
title: "community.grafana.grafana_team module – Manage Grafana Teams"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/grafana/grafana_team_module.html
fetched_at: 2026-07-27T17:15:29+00:00
---
# community.grafana.grafana_team module – Manage Grafana Teams

> **Note:**
>
> This module is part of the [community.grafana collection](https://galaxy.ansible.com/community/grafana) (version 1.5.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.grafana`.
> You need further requirements to be able to use this module,
> see [Requirements](grafana_team_module.md#ansible-collections-community-grafana-grafana-team-module-requirements) for details.
>
> To use it in a playbook, specify: `community.grafana.grafana_team`.

New in community.grafana 1.0.0

- [Synopsis](grafana_team_module.md#synopsis)
- [Requirements](grafana_team_module.md#requirements)
- [Parameters](grafana_team_module.md#parameters)
- [Examples](grafana_team_module.md#examples)
- [Return Values](grafana_team_module.md#return-values)

## [Synopsis](grafana_team_module.md#id1)

- Create/update/delete Grafana Teams through the Teams API.
- Also allows to add members in the team (if members exists).

## [Requirements](grafana_team_module.md#id2)

The below requirements are needed on the host that executes this module.

- The Teams API is only available starting Grafana 5 and the module will fail if the server version is lower than version 5.

## [Parameters](grafana_team_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **email**  string / required | The mail address associated with the Team. |
| **enforce_members**  boolean | Delete the members not found in the `members` parameters from the  list of members found on the Team.  Choices:   - `false` ← (default) - `true` |
| **grafana_api_key**  string | The Grafana API key.  If set, `url_username` and `url_password` will be ignored. |
| **members**  list / elements=string | List of team members (emails).  The list can be enforced with `enforce_members` parameter. |
| **name**  string / required | The name of the Grafana Team. |
| **skip_version_check**  boolean  added in community.grafana 1.2.0 | Skip Grafana version check and try to reach api endpoint anyway.  This parameter can be useful if you enabled `hide_version` in grafana.ini  Choices:   - `false` ← (default) - `true` |
| **state**  string | Delete the members not found in the `members` parameters from the  list of members found on the Team.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: grafana_url  string / required | The Grafana URL. |
| **url_password**  aliases: grafana_password  string | The Grafana password for API authentication.  Default: `"admin"` |
| **url_username**  aliases: grafana_user  string | The Grafana user for API authentication.  Default: `"admin"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](grafana_team_module.md#id4)

```yaml+jinja
---
- name: Create a team
  community.grafana.grafana_team:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      name: "grafana_working_group"
      email: "foo.bar@example.com"
      state: present

- name: Create a team with members
  community.grafana.grafana_team:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      name: "grafana_working_group"
      email: "foo.bar@example.com"
      members:
          - john.doe@example.com
          - jane.doe@example.com
      state: present

- name: Create a team with members and enforce the list of members
  community.grafana.grafana_team:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      name: "grafana_working_group"
      email: "foo.bar@example.com"
      members:
          - john.doe@example.com
          - jane.doe@example.com
      enforce_members: yes
      state: present

- name: Delete a team
  community.grafana.grafana_team:
      url: "https://grafana.example.com"
      grafana_api_key: "{{ some_api_token_value }}"
      name: "grafana_working_group"
      email: "foo.bar@example.com"
      state: absent
```

## [Return Values](grafana_team_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **team**  complex | Information about the Team  Returned: On success |
| **avatarUrl**  string | The url of the Team avatar on Grafana server  Returned: always  Sample: `"['/avatar/a7440323a684ea47406313a33156e5e9']"` |
| **email**  string | The Team email address  Returned: always  Sample: `"['foo.bar@example.com']"` |
| **id**  integer | The Team email address  Returned: always  Sample: `[42]` |
| **memberCount**  integer | The number of Team members  Returned: always  Sample: `[42]` |
| **members**  list / elements=string | The list of Team members  Returned: always  Sample: `[["john.doe@exemple.com"]]` |
| **name**  string | The name of the team.  Returned: always  Sample: `"['grafana_working_group']"` |
| **orgId**  integer | The organization id that the team is part of.  Returned: always  Sample: `[1]` |

### Authors

- Rémi REY (@rrey)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/grafana/issues)
[Homepage](https://github.com/ansible-collections/grafana)
[Repository (Sources)](https://github.com/ansible-collections/grafana.git)
