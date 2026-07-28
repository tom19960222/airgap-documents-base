---
collection: ansible
version: "6"
title: "community.general.sensu_client module – Manages Sensu client configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sensu_client_module.html
fetched_at: 2026-07-27T17:13:10+00:00
---
# community.general.sensu_client module – Manages Sensu client configuration

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.sensu_client`.

- [Synopsis](sensu_client_module.md#synopsis)
- [Parameters](sensu_client_module.md#parameters)
- [Notes](sensu_client_module.md#notes)
- [Examples](sensu_client_module.md#examples)
- [Return Values](sensu_client_module.md#return-values)

## [Synopsis](sensu_client_module.md#id1)

- Manages Sensu client configuration.
- For more information, refer to the Sensu documentation: <https://sensuapp.org/docs/latest/reference/clients.html>

## [Parameters](sensu_client_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | An address to help identify and reach the client. This is only informational, usually an IP address or hostname.  If not specified it defaults to non-loopback IPv4 address as determined by Ruby Socket.ip_address_list (provided by Sensu). |
| **chef**  dictionary | The chef definition scope, used to configure the Sensu Enterprise Chef integration (Sensu Enterprise users only). |
| **deregister**  boolean | If a deregistration event should be created upon Sensu client process stop.  Default is `false`.  Choices:   - `false` - `true` |
| **deregistration**  dictionary | The deregistration definition scope, used to configure automated Sensu client de-registration. |
| **ec2**  dictionary | The ec2 definition scope, used to configure the Sensu Enterprise AWS EC2 integration (Sensu Enterprise users only). |
| **keepalive**  dictionary | The keepalive definition scope, used to configure Sensu client keepalives behavior (e.g. keepalive thresholds, etc). |
| **keepalives**  boolean | If Sensu should monitor keepalives for this client.  Choices:   - `false` - `true` ← (default) |
| **name**  string | A unique name for the client. The name cannot contain special characters or spaces.  If not specified, it defaults to the system hostname as determined by Ruby Socket.gethostname (provided by Sensu). |
| **puppet**  dictionary | The puppet definition scope, used to configure the Sensu Enterprise Puppet integration (Sensu Enterprise users only). |
| **redact**  list / elements=string | Client definition attributes to redact (values) when logging and sending client keepalives. |
| **registration**  dictionary | The registration definition scope, used to configure Sensu registration event handlers. |
| **safe_mode**  boolean | If safe mode is enabled for the client. Safe mode requires local check definitions in order to accept a check request and execute the check.  Choices:   - `false` ← (default) - `true` |
| **servicenow**  dictionary | The servicenow definition scope, used to configure the Sensu Enterprise ServiceNow integration (Sensu Enterprise users only). |
| **socket**  dictionary | The socket definition scope, used to configure the Sensu client socket. |
| **state**  string | Whether the client should be present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **subscriptions**  list / elements=string | An array of client subscriptions, a list of roles and/or responsibilities assigned to the system (e.g. webserver).  These subscriptions determine which monitoring checks are executed by the client, as check requests are sent to subscriptions.  The subscriptions array items must be strings. |

## [Notes](sensu_client_module.md#id3)

> **Note:**
>
> - Check mode is supported

## [Examples](sensu_client_module.md#id4)

```yaml+jinja
# Minimum possible configuration
- name: Configure Sensu client
  community.general.sensu_client:
    subscriptions:
      - default

# With customization
- name: Configure Sensu client
  community.general.sensu_client:
    name: "{{ ansible_fqdn }}"
    address: "{{ ansible_default_ipv4['address'] }}"
    subscriptions:
      - default
      - webserver
    redact:
      - password
    socket:
      bind: 127.0.0.1
      port: 3030
    keepalive:
      thresholds:
        warning: 180
        critical: 300
      handlers:
        - email
      custom:
        - broadcast: irc
      occurrences: 3
  register: client
  notify:
    - Restart sensu-client

- name: Secure Sensu client configuration file
  ansible.builtin.file:
    path: "{{ client['file'] }}"
    owner: "sensu"
    group: "sensu"
    mode: "0600"

- name: Delete the Sensu client configuration
  community.general.sensu_client:
    state: "absent"
```

## [Return Values](sensu_client_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config**  dictionary | Effective client configuration, when state is present  Returned: success  Sample: `{"name": "client", "subscriptions": ["default"]}` |
| **file**  string | Path to the client configuration file  Returned: success  Sample: `"/etc/sensu/conf.d/client.json"` |

### Authors

- David Moreau Simard (@dmsimard)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
