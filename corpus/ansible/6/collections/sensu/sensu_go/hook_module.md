---
collection: ansible
version: "6"
title: "sensu.sensu_go.hook module – Manage Sensu hooks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/hook_module.html
fetched_at: 2026-07-28T00:19:35+00:00
---
# sensu.sensu_go.hook module – Manage Sensu hooks

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](hook_module.md#ansible-collections-sensu-sensu-go-hook-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.hook`.

New in sensu.sensu_go 1.0.0

- [Synopsis](hook_module.md#synopsis)
- [Requirements](hook_module.md#requirements)
- [Parameters](hook_module.md#parameters)
- [See Also](hook_module.md#see-also)
- [Examples](hook_module.md#examples)
- [Return Values](hook_module.md#return-values)

## [Synopsis](hook_module.md#id1)

- Create, update or delete Sensu hook.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/hooks/>.

## [Requirements](hook_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](hook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary | Custom metadata fields with fewer restrictions, as key/value pairs.  These are preserved by Sensu but not accessible as tokens or identifiers, and are mainly intended for use with external tools. |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **command**  string | Command to run when the hook is triggered.  Required if *state* is `present`. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  Default: `"default"` |
| **runtime_assets**  list / elements=string | List of runtime assets required to run the check. |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **stdin**  boolean | Controls whether Sensu writes serialized JSON data to the process’s stdin.  Choices:   - `false` - `true` |
| **timeout**  integer | The hook execution duration timeout in seconds (hard stop).  Required if *state* is `present`. |

## [See Also](hook_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.hook_info](hook_info_module.md#ansible-collections-sensu-sensu-go-hook-info-module)
> :   List Sensu hooks.

## [Examples](hook_module.md#id5)

```yaml+jinja
- name: Rudimentary auto-remediation hook
  sensu.sensu_go.hook:
    auth:
      url: http://localhost:8080
    name: restart_nginx
    command: sudo systemctl start nginx
    timeout: 60
    stdin: false

- name: Capture the process tree
  sensu.sensu_go.hook:
    auth:
      url: http://localhost:8080
    name: process_tree
    command: ps aux
    timeout: 60
    stdin: false

- name: Delete a hook
  sensu.sensu_go.hook:
    name: process_tree
    state: absent
```

## [Return Values](hook_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu hook.  Returned: success  Sample: `{"command": "sudo systemctl start nginx", "metadata": {"annotations": null, "labels": null, "name": "restart_nginx", "namespace": "default"}, "stdin": false, "timeout": 60}` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
