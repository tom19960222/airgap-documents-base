---
collection: ansible
version: "8"
title: "community.general.jenkins_script module – Executes a groovy script in the jenkins instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/jenkins_script_module.html
fetched_at: 2026-07-28T01:47:03+00:00
---
# community.general.jenkins_script module – Executes a groovy script in the jenkins instance

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.jenkins_script`.

- [Synopsis](jenkins_script_module.md#synopsis)
- [Parameters](jenkins_script_module.md#parameters)
- [Attributes](jenkins_script_module.md#attributes)
- [Notes](jenkins_script_module.md#notes)
- [Examples](jenkins_script_module.md#examples)
- [Return Values](jenkins_script_module.md#return-values)

## [Synopsis](jenkins_script_module.md#id1)

- The `jenkins_script` module takes a script plus a dict of values to use within the script and returns the result of the script being run.

Aliases: web_infrastructure.jenkins_script

## [Parameters](jenkins_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **args**  dictionary | A dict of key-value pairs used in formatting the script using string.Template (see <https://docs.python.org/2/library/string.html#template-strings>). |
| **password**  string | The password to connect to the jenkins server with. |
| **script**  string / required | The groovy script to be executed. This gets passed as a string Template if args is defined. |
| **timeout**  integer | The request timeout in seconds  **Default:** `10` |
| **url**  string | The jenkins server to execute the script against. The default is a local jenkins instance that is not being proxied through a webserver.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to connect to the jenkins server with. |
| **validate_certs**  boolean | If set to `false`, the SSL certificates will not be validated. This should only set to `false` used on personally controlled sites using self-signed certificates as it avoids verifying the source site.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](jenkins_script_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](jenkins_script_module.md#id4)

> **Note:**
>
> - Since the script can do anything this does not report on changes. Knowing the script is being run it’s important to set changed_when for the ansible output to be clear on any alterations made.

## [Examples](jenkins_script_module.md#id5)

```yaml+jinja
- name: Obtaining a list of plugins
  community.general.jenkins_script:
    script: 'println(Jenkins.instance.pluginManager.plugins)'
    user: admin
    password: admin

- name: Setting master using a variable to hold a more complicate script
  ansible.builtin.set_fact:
    setmaster_mode: |
        import jenkins.model.*
        instance = Jenkins.getInstance()
        instance.setMode(${jenkins_mode})
        instance.save()

- name: Use the variable as the script
  community.general.jenkins_script:
    script: "{{ setmaster_mode }}"
    args:
      jenkins_mode: Node.Mode.EXCLUSIVE

- name: Interacting with an untrusted HTTPS connection
  community.general.jenkins_script:
    script: "println(Jenkins.instance.pluginManager.plugins)"
    user: admin
    password: admin
    url: https://localhost
    validate_certs: false
```

## [Return Values](jenkins_script_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  string | Result of script  **Returned:** success  **Sample:** `"Result: true"` |

### Authors

- James Hogarth (@hogarthj)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
