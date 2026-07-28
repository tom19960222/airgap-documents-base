---
collection: ansible
version: "8"
title: "cisco.meraki.meraki_mx_intrusion_prevention module – Manage intrustion prevention in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/meraki_mx_intrusion_prevention_module.html
fetched_at: 2026-07-28T01:32:35+00:00
---
# cisco.meraki.meraki_mx_intrusion_prevention module – Manage intrustion prevention in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mx_intrusion_prevention`.

- [DEPRECATED](meraki_mx_intrusion_prevention_module.md#deprecated)
- [Synopsis](meraki_mx_intrusion_prevention_module.md#synopsis)
- [Parameters](meraki_mx_intrusion_prevention_module.md#parameters)
- [Notes](meraki_mx_intrusion_prevention_module.md#notes)
- [Examples](meraki_mx_intrusion_prevention_module.md#examples)
- [Return Values](meraki_mx_intrusion_prevention_module.md#return-values)
- [Status](meraki_mx_intrusion_prevention_module.md#status)

## [DEPRECATED](meraki_mx_intrusion_prevention_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Updated modules released with increased functionality

Alternative:
:   cisco.meraki.organizations_appliance_security_intrusion and cisco.meraki.networks_appliance_security_intrusion

## [Synopsis](meraki_mx_intrusion_prevention_module.md#id2)

- Allows for management of intrusion prevention rules networks within Meraki MX networks.

## [Parameters](meraki_mx_intrusion_prevention_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowed_rules**  list / elements=dictionary | List of IDs related to rules which are allowed for the organization. |
| **rule_id**  string | ID of rule as defined by Snort. |
| **rule_message**  aliases: message  string  *added in cisco.meraki 2.3.0* | Description of rule.  This is overwritten by the API.  Formerly `message` which was deprecated but still maintained as an alias. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  **Default:** `"api.meraki.com"` |
| **ids_rulesets**  string | Ruleset complexity setting.  **Choices:**   - `"connectivity"` - `"balanced"` - `"security"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  **Default:** `60` |
| **mode**  string | Operational mode of Intrusion Prevention system.  **Choices:**   - `"detection"` - `"disabled"` - `"prevention"` |
| **net_id**  string | ID number of a network. |
| **net_name**  aliases: name, network  string | Name of a network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  **Choices:**   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  **Choices:**   - `"debug"` - `"normal"` ← (default) |
| **protected_networks**  dictionary | Set included/excluded networks for Intrusion Prevention. |
| **excluded_cidr**  list / elements=string | List of network IP ranges to exclude from scanning. |
| **included_cidr**  list / elements=string | List of network IP ranges to include in scanning. |
| **use_default**  boolean | Whether to use special IPv4 addresses per RFC 5735.  **Choices:**   - `false` - `true` |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  **Default:** `165` |
| **state**  string | Create or modify an organization.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | Time to timeout for HTTP requests.  **Default:** `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](meraki_mx_intrusion_prevention_module.md#id4)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mx_intrusion_prevention_module.md#id5)

```yaml+jinja
- name: Set whitelist for organization
  meraki_intrusion_prevention:
    auth_key: '{{auth_key}}'
    state: present
    org_id: '{{test_org_id}}'
    allowed_rules:
      - rule_id: "meraki:intrusion/snort/GID/01/SID/5805"
        rule_message: Test rule
  delegate_to: localhost

- name: Query IPS info for organization
  meraki_intrusion_prevention:
    auth_key: '{{auth_key}}'
    state: query
    org_name: '{{test_org_name}}'
  delegate_to: localhost
  register: query_org

- name: Set full ruleset with check mode
  meraki_intrusion_prevention:
    auth_key: '{{auth_key}}'
    state: present
    org_name: '{{test_org_name}}'
    net_name: '{{test_net_name}} - IPS'
    mode: prevention
    ids_rulesets: security
    protected_networks:
      use_default: true
      included_cidr:
        - 192.0.1.0/24
      excluded_cidr:
        - 10.0.1.0/24
  delegate_to: localhost

- name: Clear rules from organization
  meraki_intrusion_prevention:
    auth_key: '{{auth_key}}'
    state: absent
    org_name: '{{test_org_name}}'
    allowed_rules: []
  delegate_to: localhost
```

## [Return Values](meraki_mx_intrusion_prevention_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about the Threat Protection settings.  **Returned:** success |
| **idsRulesets**  string | Setting of selected ruleset.  **Returned:** success, when network is queried or modified  **Sample:** `"balanced"` |
| **mode**  string | Enabled setting of intrusion prevention.  **Returned:** success, when network is queried or modified  **Sample:** `"enabled"` |
| **protectedNetworks**  complex | Networks protected by IPS.  **Returned:** success, when network is queried or modified |
| **excludedCidr**  string | List of CIDR notiation networks to exclude from protection.  **Returned:** success, when network is queried or modified  **Sample:** `"192.0.1.0/24"` |
| **includedCidr**  string | List of CIDR notiation networks to protect.  **Returned:** success, when network is queried or modified  **Sample:** `"192.0.1.0/24"` |
| **useDefault**  boolean | Whether to use special IPv4 addresses.  **Returned:** success, when network is queried or modified  **Sample:** `true` |
| **whitelistedRules**  complex | List of whitelisted IPS rules.  **Returned:** success, when organization is queried or modified |
| **rule_message**  string | Description of rule.  **Returned:** success, when organization is queried or modified  **Sample:** `"MALWARE-OTHER Trackware myway speedbar runtime detection - switch engines"` |
| **ruleId**  string | A rule identifier for an IPS rule.  **Returned:** success, when organization is queried or modified  **Sample:** `"meraki:intrusion/snort/GID/01/SID/5805"` |

## [Status](meraki_mx_intrusion_prevention_module.md#id7)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](meraki_mx_intrusion_prevention_module.md#deprecated).

### Authors

- Kevin Breit (@kbreit)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
