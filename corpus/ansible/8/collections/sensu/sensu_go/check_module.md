---
collection: ansible
version: "8"
title: "sensu.sensu_go.check module – Manage Sensu checks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/check_module.html
fetched_at: 2026-07-28T02:52:56+00:00
---
# sensu.sensu_go.check module – Manage Sensu checks

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](check_module.md#ansible-collections-sensu-sensu-go-check-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.check`.

New in sensu.sensu_go 1.0.0

- [Synopsis](check_module.md#synopsis)
- [Requirements](check_module.md#requirements)
- [Parameters](check_module.md#parameters)
- [See Also](check_module.md#see-also)
- [Examples](check_module.md#examples)
- [Return Values](check_module.md#return-values)

## [Synopsis](check_module.md#id1)

- Create, update or delete Sensu Go check.
- For more information, refer to the Sensu Go documentation at <https://docs.sensu.io/sensu-go/latest/reference/checks/>.

## [Requirements](check_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](check_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary | Custom metadata fields with fewer restrictions, as key/value pairs.  These are preserved by Sensu but not accessible as tokens or identifiers, and are mainly intended for use with external tools.  **Default:** `{}` |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **check_hooks**  dictionary | A mapping of response codes to hooks which will be run by the agent when that code is returned.  Note that the structure of this parameter is a bit different from the one described at <https://docs.sensu.io/sensu-go/latest/reference/checks/#check-hooks-attribute>.  See check hooks example below for more information on exact mapping structure. |
| **command**  string | Check command to run.  Required if *state* is `present`. |
| **cron**  string | Schedule check requests using crontab syntax.  Cannot be used when *interval* option is used. |
| **env_vars**  dictionary | A mapping of environment variable names and values to use with command execution. |
| **handlers**  list / elements=string | List of handlers which receive check results. |
| **high_flap_threshold**  integer | High flap threshold. |
| **interval**  integer | Check request interval.  Cannot be used when *cron* option is used. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs.  **Default:** `{}` |
| **low_flap_threshold**  integer | Low flap threshold. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  **Default:** `"default"` |
| **output_metric_format**  string | Enable parsing of metrics in the specified format from this check’s output.  **Choices:**   - `"graphite_plaintext"` - `"influxdb_line"` - `"nagios_perfdata"` - `"opentsdb_line"` |
| **output_metric_handlers**  list / elements=string | List of handlers which receive check results. I’m not sure why this exists. |
| **proxy_entity_name**  string | Entity name to associate this check with instead of the agent it ran on. |
| **proxy_requests**  dictionary | Allows you to assign the check to run for multiple entities according to their entity_attributes. |
| **entity_attributes**  list / elements=string | List of attribute checks for determining which proxy entities this check should be scheduled against. |
| **splay**  boolean | Enables or disables splaying of check request scheduling.  **Choices:**   - `false` - `true` |
| **splay_coverage**  integer | Percentage of the `interval` over which to splay checks. |
| **publish**  boolean | Enables or disables scheduled publication of check requests.  **Choices:**   - `false` - `true` |
| **round_robin**  boolean | An array of environment variables to use with command execution.  **Choices:**   - `false` - `true` |
| **runtime_assets**  list / elements=string | List of runtime assets required to run the check. |
| **secrets**  list / elements=dictionary  *added in sensu.sensu_go 1.6.0* | List of secrets that are available to the command. |
| **name**  string / required  *added in sensu.sensu_go 1.6.0* | Variable name that will contain the sensitive data. |
| **secret**  string / required  *added in sensu.sensu_go 1.6.0* | Name of the secret that contains sensitive data. |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stdin**  boolean | Enables writing of serialized JSON data to the check command’s stdin.  Only usable with checks written specifically for Sensu Go.  **Choices:**   - `false` - `true` |
| **subscriptions**  list / elements=string | List of subscriptions which receive check requests.  Required if *state* is `present`. |
| **timeout**  integer | Check execution timeout. |
| **ttl**  integer | Amount of time after which a check result is considered stale. |

## [See Also](check_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.check_info](check_info_module.md#ansible-collections-sensu-sensu-go-check-info-module)
> :   List Sensu checks.

## [Examples](check_module.md#id5)

```yaml+jinja
- name: Check executing command every 30 seconds
  sensu.sensu_go.check:
    name: check
    command: check-cpu.sh -w 75 -c 90
    subscriptions:
      - checks
    interval: 30
    publish: yes

- name: Check executing command with cron scheduler
  sensu.sensu_go.check:
    name: check
    command: check-cpu.sh -w 75 -c 90
    subscriptions:
      - systems
    handlers:
      - slack
    cron: "* * * * *"
    publish: yes

- name: Ad-hoc scheduling
  sensu.sensu_go.check:
    name: check
    command: check-cpu.sh -w 75 -c 90
    subscriptions:
      - systems
    handlers:
      - slack
    interval: 60
    publish: no

- name: Report events under proxy entity name instead of agent entity
  sensu.sensu_go.check:
    name: check
    command: http_check.sh https://sensu.io
    subscriptions:
      - proxy
    handlers:
      - slack
    interval: 60
    proxy_entity_name: sensu-site
    round_robin: yes
    publish: yes

- name: Event that triggers hooks
  sensu.sensu_go.check:
    name: check
    command: http_check.sh https://sensu.io
    subscriptions: [ proxy ]
    # The upstream JSON payload for the hooks below would look like this:
    #
    #   "check_hooks": [
    #     {"0": ["passing-hook", "always-run-this-hook"]},
    #     {"critical": ["failing-hook", "always-run-this-hook"]}
    #   ]
    #
    # Ansible task simplifies this structure into a simple mapping:
    check_hooks:
      "0":
        - passing-hook
        - always-run-this-hook
      critical:
        - failing-hook
        - always-run-this-hook

- name: Remove check
  sensu.sensu_go.check:
    name: my-check
    state: absent
```

## [Return Values](check_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu check.  **Returned:** success  **Sample:** `{"command": "collect.sh", "handlers": ["slack"], "interval": 10, "metadata": {"name": "check_minimum", "namespace": "default"}, "publish": true, "subscriptions": ["system"]}` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
