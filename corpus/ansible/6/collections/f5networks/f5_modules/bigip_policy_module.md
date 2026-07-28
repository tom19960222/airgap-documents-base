---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_policy module – Manage general policy configuration on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_policy_module.html
fetched_at: 2026-07-27T17:27:24+00:00
---
# f5networks.f5_modules.bigip_policy module – Manage general policy configuration on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_policy`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_policy_module.md#synopsis)
- [Parameters](bigip_policy_module.md#parameters)
- [Notes](bigip_policy_module.md#notes)
- [Examples](bigip_policy_module.md#examples)
- [Return Values](bigip_policy_module.md#return-values)

## [Synopsis](bigip_policy_module.md#id1)

- Manages general policy configuration on a BIG-IP. This module is best used in conjunction with the `bigip_policy_rule` module. This module can handle general configuration, like setting the draft state of the policy, the description, and items unrelated to the policy rules themselves. It is also the first module that should be used when creating rules, as the `bigip_policy_rule` module requires a policy parameter.

## [Parameters](bigip_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description to attach to the policy.  This parameter is only supported on versions of BIG-IP >= 12.1.0. On earlier versions it is simply ignored. |
| **name**  string / required | The name of the policy to create. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **rules**  list / elements=string | Specifies a list of rules you want associated with this policy. The order of this list is the order they will be evaluated by BIG-IP. If the specified rules do not exist (for example when creating a new policy) they will be created.  The `conditions` for a default rule are `all`.  The `actions` for a default rule are `ignore`.  The `bigip_policy_rule` module can be used to create and edit existing and new rules. |
| **state**  string | When `state` is `present`, ensures the policy exists and is published. When `state` is `absent`, ensures the policy is removed, even if it is currently drafted.  When `state` is `draft`, ensures the policy exists and is drafted. When modifying rules, it is required that policies first be in a draft.  Drafting is only supported on versions of BIG-IP >= 12.1.0. On versions prior to that, specifying a `state` of `draft` will raise an error.  Choices:   - `"present"` ← (default) - `"absent"` - `"draft"` |
| **strategy**  string | Specifies the method to determine which actions get executed when there are multiple rules that match. When creating new policies, the default is `first`.  This module does not allow you to specify the `best` strategy to use. It will choose the system default (`/Common/best-match`) instead.  Choices:   - `"first"` - `"all"` - `"best"` |

## [Notes](bigip_policy_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_policy_module.md#id4)

```yaml+jinja
- name: Create policy which is immediately published
  bigip_policy:
    name: Policy-Foo
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add a rule to the new policy - Immediately published
  bigip_policy_rule:
    policy: Policy-Foo
    name: ABC
    conditions:
      - type: http_uri
        path_starts_with:
          - /ABC
          - foo
          - bar
        path_ends_with:
          - baz
    actions:
      - forward: yes
        select: yes
        pool: pool-svrs
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add multiple rules to the new policy - Added in the order they are specified
  bigip_policy_rule:
    policy: Policy-Foo
    name: "{{ item.name }}"
    conditions: "{{ item.conditions }}"
    actions: "{{ item.actions }}"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
  loop:
    - name: rule1
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /euro
    - name: HomePage
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_starts_with: /HomePage/

- name: Create policy specify default rules - Immediately published
  bigip_policy:
    name: Policy-Bar
    state: present
    rules:
      - rule1
      - rule2
      - rule3
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create policy specify default rules - Left in a draft
  bigip_policy:
    name: Policy-Baz
    state: draft
    rules:
      - rule1
      - rule2
      - rule3
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The new description of the policy.  This value is only returned for BIG-IP devices >= 12.1.0.  Returned: changed and success  Sample: `"This is my description"` |
| **rules**  list / elements=string | List of the rules, and their order, applied to the policy.  Returned: changed and success  Sample: `["/Common/rule1", "/Common/rule2"]` |
| **strategy**  integer | The new strategy set on the policy.  Returned: changed and success  Sample: `"first-match"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
