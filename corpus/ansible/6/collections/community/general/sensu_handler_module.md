---
collection: ansible
version: "6"
title: "community.general.sensu_handler module – Manages Sensu handler configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sensu_handler_module.html
fetched_at: 2026-07-27T17:13:10+00:00
---
# community.general.sensu_handler module – Manages Sensu handler configuration

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
> To use it in a playbook, specify: `community.general.sensu_handler`.

- [Synopsis](sensu_handler_module.md#synopsis)
- [Parameters](sensu_handler_module.md#parameters)
- [Notes](sensu_handler_module.md#notes)
- [Examples](sensu_handler_module.md#examples)
- [Return Values](sensu_handler_module.md#return-values)

## [Synopsis](sensu_handler_module.md#id1)

- Manages Sensu handler configuration
- For more information, refer to the Sensu documentation: <https://sensuapp.org/docs/latest/reference/handlers.html>

## [Parameters](sensu_handler_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **command**  string | The handler command to be executed.  The event data is passed to the process via STDIN.  NOTE: the command attribute is only required for Pipe handlers (i.e. handlers configured with “type”: “pipe”). |
| **filter**  string | The Sensu event filter (name) to use when filtering events for the handler. |
| **filters**  list / elements=string | An array of Sensu event filters (names) to use when filtering events for the handler.  Each array item must be a string. |
| **handle_flapping**  boolean | If events in the flapping state should be handled.  Choices:   - `false` ← (default) - `true` |
| **handle_silenced**  boolean | If events matching one or more silence entries should be handled.  Choices:   - `false` ← (default) - `true` |
| **handlers**  list / elements=string | An array of Sensu event handlers (names) to use for events using the handler set.  NOTE: the handlers attribute is only required for handler sets (i.e. handlers configured with “type”: “set”). |
| **mutator**  string | The Sensu event mutator (name) to use to mutate event data for the handler. |
| **name**  string / required | A unique name for the handler. The name cannot contain special characters or spaces. |
| **pipe**  dictionary | The pipe definition scope, used to configure the Sensu transport pipe.  NOTE: the pipe attribute is only required for Transport handlers (i.e. handlers configured with “type”: “transport”). |
| **severities**  list / elements=string | An array of check result severities the handler will handle.  NOTE: event resolution bypasses this filtering.  Example: [ ‘warning’, ‘critical’, ‘unknown’ ]. |
| **socket**  dictionary | The socket definition scope, used to configure the TCP/UDP handler socket.  NOTE: the socket attribute is only required for TCP/UDP handlers (i.e. handlers configured with “type”: “tcp” or “type”: “udp”). |
| **state**  string | Whether the handler should be present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The handler execution duration timeout in seconds (hard stop).  Only used by pipe and tcp handler types.  Default: `10` |
| **type**  string | The handler type  Choices:   - `"pipe"` - `"tcp"` - `"udp"` - `"transport"` - `"set"` |

## [Notes](sensu_handler_module.md#id3)

> **Note:**
>
> - Check mode is supported

## [Examples](sensu_handler_module.md#id4)

```yaml+jinja
# Configure a handler that sends event data as STDIN (pipe)
- name: Configure IRC Sensu handler
  community.general.sensu_handler:
    name: "irc_handler"
    type: "pipe"
    command: "/usr/local/bin/notify-irc.sh"
    severities:
      - "ok"
      - "critical"
      - "warning"
      - "unknown"
    timeout: 15
  notify:
    - Restart sensu-client
    - Restart sensu-server

# Delete a handler
- name: Delete IRC Sensu handler
  community.general.sensu_handler:
    name: "irc_handler"
    state: "absent"

# Example of a TCP handler
- name: Configure TCP Sensu handler
  community.general.sensu_handler:
    name: "tcp_handler"
    type: "tcp"
    timeout: 30
    socket:
      host: "10.0.1.99"
      port: 4444
  register: handler
  notify:
    - Restart sensu-client
    - Restart sensu-server

- name: Secure Sensu handler configuration file
  ansible.builtin.file:
    path: "{{ handler['file'] }}"
    owner: "sensu"
    group: "sensu"
    mode: "0600"
```

## [Return Values](sensu_handler_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config**  dictionary | Effective handler configuration, when state is present  Returned: success  Sample: `{"command": "/usr/local/bin/notify-irc.sh", "name": "irc", "type": "pipe"}` |
| **file**  string | Path to the handler configuration file  Returned: success  Sample: `"/etc/sensu/conf.d/handlers/irc.json"` |
| **name**  string | Name of the handler  Returned: success  Sample: `"irc"` |

### Authors

- David Moreau Simard (@dmsimard)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
