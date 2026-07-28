---
collection: ansible
version: "6"
title: "community.general.jenkins_plugin module – Add or remove Jenkins plugin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/jenkins_plugin_module.html
fetched_at: 2026-07-27T17:10:13+00:00
---
# community.general.jenkins_plugin module – Add or remove Jenkins plugin

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
> To use it in a playbook, specify: `community.general.jenkins_plugin`.

- [Synopsis](jenkins_plugin_module.md#synopsis)
- [Parameters](jenkins_plugin_module.md#parameters)
- [Notes](jenkins_plugin_module.md#notes)
- [Examples](jenkins_plugin_module.md#examples)
- [Return Values](jenkins_plugin_module.md#return-values)

## [Synopsis](jenkins_plugin_module.md#id1)

- Ansible module which helps to manage Jenkins plugins.

## [Parameters](jenkins_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the Jenkins group on the OS.  Default: `"jenkins"` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **jenkins_home**  path | Home directory of the Jenkins user.  Default: `"/var/lib/jenkins"` |
| **latest_plugins_url_segments**  list / elements=string  added in community.general 3.3.0 | Path inside the *updates_url* to get latest plugins from.  Default: `["latest"]` |
| **mode**  any | File mode applied on versioned plugins.  Default: `"0644"` |
| **name**  string / required | Plugin name. |
| **owner**  string | Name of the Jenkins user on the OS.  Default: `"jenkins"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | Desired plugin state.  If the `latest` is set, the check for new version will be performed every time. This is suitable to keep the plugin up-to-date.  Choices:   - `"absent"` - `"present"` ← (default) - `"pinned"` - `"unpinned"` - `"enabled"` - `"disabled"` - `"latest"` |
| **timeout**  integer | Server connection timeout in secs.  Default: `30` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **update_json_url_segment**  list / elements=string  added in community.general 3.3.0 | A list of URL segment(s) to retrieve the update center json file from.  Default: `["update-center.json", "updates/update-center.json"]` |
| **updates_expiration**  integer | Number of seconds after which a new copy of the *update-center.json* file is downloaded. This is used to avoid the need to download the plugin to calculate its checksum when `latest` is specified.  Set it to `0` if no cache file should be used. In that case, the plugin file will always be downloaded to calculate its checksum when `latest` is specified.  Default: `86400` |
| **updates_url**  list / elements=string | A list of base URL(s) to retrieve *update-center.json*, and direct plugin files from.  This can be a list since community.general 3.3.0.  Default: `["https://updates.jenkins.io", "http://mirrors.jenkins.io"]` |
| **url**  string | URL of the Jenkins server.  Default: `"http://localhost:8080"` |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Plugin version number.  If this option is specified, all plugin dependencies must be installed manually.  It might take longer to verify that the correct version is installed. This is especially true if a specific version number is specified.  Quote the version to prevent the value to be interpreted as float. For example if `1.20` would be unquoted, it would become `1.2`. |
| **versioned_plugins_url_segments**  list / elements=string  added in community.general 3.3.0 | Path inside the *updates_url* to get specific version of plugins from.  Default: `["download/plugins", "plugins"]` |
| **with_dependencies**  boolean | Defines whether to install plugin dependencies.  This option takes effect only if the *version* is not defined.  Choices:   - `false` - `true` ← (default) |

## [Notes](jenkins_plugin_module.md#id3)

> **Note:**
>
> - Plugin installation should be run under root or the same user which owns the plugin files on the disk. Only if the plugin is not installed yet and no version is specified, the API installation is performed which requires only the Web UI credentials.
> - It’s necessary to notify the handler or call the *service* module to restart the Jenkins service after a new plugin was installed.
> - Pinning works only if the plugin is installed and Jenkins service was successfully restarted after the plugin installation.
> - It is not possible to run the module remotely by changing the *url* parameter to point to the Jenkins server. The module must be used on the host where Jenkins runs as it needs direct access to the plugin files.

## [Examples](jenkins_plugin_module.md#id4)

```yaml+jinja
- name: Install plugin
  community.general.jenkins_plugin:
    name: build-pipeline-plugin

- name: Install plugin without its dependencies
  community.general.jenkins_plugin:
    name: build-pipeline-plugin
    with_dependencies: false

- name: Make sure the plugin is always up-to-date
  community.general.jenkins_plugin:
    name: token-macro
    state: latest

- name: Install specific version of the plugin
  community.general.jenkins_plugin:
    name: token-macro
    version: "1.15"

- name: Pin the plugin
  community.general.jenkins_plugin:
    name: token-macro
    state: pinned

- name: Unpin the plugin
  community.general.jenkins_plugin:
    name: token-macro
    state: unpinned

- name: Enable the plugin
  community.general.jenkins_plugin:
    name: token-macro
    state: enabled

- name: Disable the plugin
  community.general.jenkins_plugin:
    name: token-macro
    state: disabled

- name: Uninstall plugin
  community.general.jenkins_plugin:
    name: build-pipeline-plugin
    state: absent

#
# Example of how to authenticate
#
- name: Install plugin
  community.general.jenkins_plugin:
    name: build-pipeline-plugin
    url_username: admin
    url_password: p4ssw0rd
    url: http://localhost:8888

#
# Example of a Play which handles Jenkins restarts during the state changes
#
- name: Jenkins Master play
  hosts: jenkins-master
  vars:
    my_jenkins_plugins:
      token-macro:
        enabled: true
      build-pipeline-plugin:
        version: "1.4.9"
        pinned: false
        enabled: true
  tasks:
    - name: Install plugins without a specific version
      community.general.jenkins_plugin:
        name: "{{ item.key }}"
      register: my_jenkins_plugin_unversioned
      when: >
        'version' not in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Install plugins with a specific version
      community.general.jenkins_plugin:
        name: "{{ item.key }}"
        version: "{{ item.value['version'] }}"
      register: my_jenkins_plugin_versioned
      when: >
        'version' in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Initiate the fact
      ansible.builtin.set_fact:
        jenkins_restart_required: false

    - name: Check if restart is required by any of the versioned plugins
      ansible.builtin.set_fact:
        jenkins_restart_required: true
      when: item.changed
      with_items: "{{ my_jenkins_plugin_versioned.results }}"

    - name: Check if restart is required by any of the unversioned plugins
      ansible.builtin.set_fact:
        jenkins_restart_required: true
      when: item.changed
      with_items: "{{ my_jenkins_plugin_unversioned.results }}"

    - name: Restart Jenkins if required
      ansible.builtin.service:
        name: jenkins
        state: restarted
      when: jenkins_restart_required

    - name: Wait for Jenkins to start up
      ansible.builtin.uri:
        url: http://localhost:8080
        status_code: 200
        timeout: 5
      register: jenkins_service_status
      # Keep trying for 5 mins in 5 sec intervals
      retries: 60
      delay: 5
      until: >
         'status' in jenkins_service_status and
         jenkins_service_status['status'] == 200
      when: jenkins_restart_required

    - name: Reset the fact
      ansible.builtin.set_fact:
        jenkins_restart_required: false
      when: jenkins_restart_required

    - name: Plugin pinning
      community.general.jenkins_plugin:
        name: "{{ item.key }}"
        state: "{{ 'pinned' if item.value['pinned'] else 'unpinned'}}"
      when: >
        'pinned' in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Plugin enabling
      community.general.jenkins_plugin:
        name: "{{ item.key }}"
        state: "{{ 'enabled' if item.value['enabled'] else 'disabled'}}"
      when: >
        'enabled' in item.value
      with_dict: "{{ my_jenkins_plugins }}"
```

## [Return Values](jenkins_plugin_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **plugin**  string | plugin name  Returned: success  Sample: `"build-pipeline-plugin"` |
| **state**  string | state of the target, after execution  Returned: success  Sample: `"present"` |

### Authors

- Jiri Tyr (@jtyr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
