---
collection: ansible
version: "8"
title: "telekom_mms.icinga_director.icinga_command module – Manage commands in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/telekom_mms/icinga_director/icinga_command_module.html
fetched_at: 2026-07-28T02:54:41+00:00
---
# telekom_mms.icinga_director.icinga_command module – Manage commands in Icinga2

> **Note:**
>
> This module is part of the [telekom_mms.icinga_director collection](https://galaxy.ansible.com/ui/repo/published/telekom_mms/icinga_director/) (version 1.35.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install telekom_mms.icinga_director`.
>
> To use it in a playbook, specify: `telekom_mms.icinga_director.icinga_command`.

New in telekom_mms.icinga_director 1.0.0

- [Synopsis](icinga_command_module.md#synopsis)
- [Parameters](icinga_command_module.md#parameters)
- [Notes](icinga_command_module.md#notes)
- [Examples](icinga_command_module.md#examples)

## [Synopsis](icinga_command_module.md#id1)

- Add or remove a command to Icinga2 through the director API.

## [Parameters](icinga_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in telekom_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **arguments**  dictionary | Arguments of the command.  Each argument can take either a string, a json or a dict  When using a dict as argument value, the following properties are supported. `skip_key`, `repeat_key`, `required`, `order`, `description`), `set_if`, `value`.  The `value` property can be either a string, a json or a dict. When used as a dict, you can define its `type` as `Function` and set its `body` property as an Icinga DSL piece of config. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **command**  string | The command Icinga should run. Required when state is `present`.  Absolute paths are accepted as provided, relative paths are prefixed with “PluginDir + “, similar Constant prefixes are allowed.  Spaces will lead to separation of command path and standalone arguments.  Please note that this means that we do not support spaces in plugin names and paths right now. |
| **disabled**  boolean | Disabled objects will not be deployed.  **Choices:**   - `false` ← (default) - `true` |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **imports**  list / elements=string | Importable templates, add as many as you want. Please note that order matters when importing properties from multiple templates - last one wins.  **Default:** `[]` |
| **methods_execute**  aliases: command_type  string | Plugin Check commands are what you need when running checks against your infrastructure.  Notification commands will be used when it comes to notify your users.  Event commands allow you to trigger specific actions when problems occur.  Some people use them for auto-healing mechanisms, like restarting services or rebooting systems at specific thresholds.  **Choices:**   - `"PluginCheck"` ← (default) - `"PluginNotification"` - `"PluginEvent"` |
| **object_name**  aliases: name  string / required | Name of the command. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | Optional command timeout. Allowed values are seconds or durations postfixed with a specific unit (for example 1m or also 3m 30s). |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vars**  dictionary | Custom properties of the command.  **Default:** `{}` |
| **zone**  string | Icinga cluster zone. Allows to manually override Directors decisions of where to deploy your config to.  You should consider not doing so unless you gained deep understanding of how an Icinga Cluster stack works. |

## [Notes](icinga_command_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_command_module.md#id4)

```yaml+jinja
- name: Create command
  telekom_mms.icinga_director.icinga_command:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    arguments:
      '--authpassphrase':
        value: $snmpv3_priv_key$
      '--authprotocol':
        value: $snmpv3_auth_protocol$
      '--critical':
        value: $centreon_critical$
      '--filter':
        value: $centreon_filter$
      '--hostname':
        value: $snmp_address$
      '--maxrepetitions':
        value: $centreon_maxrepetitions$
      '--mode':
        value: $centreon_mode$
      '--plugin':
        value: $centreon_plugin$
      '--privpassphrase':
        value: $snmpv3_auth_key$
      '--privprotocol':
        value: $snmpv3_priv_protocol$
      '--snmp-community':
        value: $snmp_community$
      '--snmp-timeout':
        value: $snmp_timeout$
      '--snmp-username':
        value: $snmpv3_user$
      '--snmp-version':
        value: $snmp_version$
      '--subsetleef':
        value: $centreon_subsetleef$
      '--verbose':
        set_if: $centreon_verbose$
      '--warning':
        value: $centreon_warning$
      '--dummy-arg':
        description: "dummy arg using Icinga DSL code"
        value:
          type: "Function"
          body: 'return macro("$dummy_var$")'
    command: "/opt/centreon-plugins/centreon_plugins.pl"
    command_type: "PluginCheck"
    disabled: false
    object_name: centreon-plugins
    imports:
      - centreon-plugins-template
    vars:
      centreon_maxrepetitions: 20
      centreon_subsetleef: 20
      centreon_verbose: false
      snmp_address: $address$
      snmp_timeout: 60
      snmp_version: '2'
      snmpv3_auth_key: authkey
      snmpv3_priv_key: privkey
      snmpv3_user: user

- name: Update command
  telekom_mms.icinga_director.icinga_command:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: centreon-plugins
    timeout: "1m"
    append: true

- name: Create event command
  telekom_mms.icinga_director.icinga_command:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    command: "/opt/scripts/restart_httpd"
    object_name: "restart_httpd"
    command_type: "PluginEvent"
    arguments:
      '-s':
        value: $service.state$
      '-t':
        value: $service.state_type$
      '-a':
        set_if: $service.check_attempt$
        value: $restart_service$
```

### Authors

- Sebastian Gumprich (@rndmh3ro)

### Collection links

- [Issue Tracker](https://github.com/telekom-mms/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/telekom-mms/ansible-collection-icinga-director)
