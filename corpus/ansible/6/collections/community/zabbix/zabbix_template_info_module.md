---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_template_info module – Gather information about Zabbix template"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_template_info_module.html
fetched_at: 2026-07-27T17:24:21+00:00
---
# community.zabbix.zabbix_template_info module – Gather information about Zabbix template

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_template_info_module.md#ansible-collections-community-zabbix-zabbix-template-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_template_info`.

- [Synopsis](zabbix_template_info_module.md#synopsis)
- [Requirements](zabbix_template_info_module.md#requirements)
- [Parameters](zabbix_template_info_module.md#parameters)
- [Notes](zabbix_template_info_module.md#notes)
- [Examples](zabbix_template_info_module.md#examples)
- [Return Values](zabbix_template_info_module.md#return-values)

## [Synopsis](zabbix_template_info_module.md#id1)

- This module allows you to search for Zabbix template.

## [Requirements](zabbix_template_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_template_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **format**  string | Format to use when dumping template.  `yaml` works only with Zabbix >= 5.2.  Choices:   - `"json"` ← (default) - `"xml"` - `"yaml"` - `"none"` |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **omit_date**  boolean | Removes the date field for the dumped template  Choices:   - `false` ← (default) - `true` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **template_name**  string / required | Name of the template in Zabbix. |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_template_info_module.md#id4)

> **Note:**
>
> - there where breaking changes in the Zabbix API with version 5.4 onwards (especially UUIDs) which may require you to export the templates again (see version tag >= 5.4 in the resulting file/data).
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_template_info_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Get Zabbix template as JSON
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: json
    omit_date: yes
  register: template_json

- name: Get Zabbix template as XML
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: xml
    omit_date: no
  register: template_json

- name: Get Zabbix template as YAML
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: yaml
    omit_date: no
  register: template_yaml

- name: Determine if Zabbix template exists
  community.zabbix.zabbix_template_info:
    template_name: Template
    format: none
  register: template
```

## [Return Values](zabbix_template_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **template_id**  string | The ID of the template  Returned: always |
| **template_json**  string | The JSON of the template  Returned: when format is json and omit_date is true  Sample: `"{'zabbix_export': {'groups': [{'name': 'Templates'}], 'templates': [{'applications': [{'name': 'Test Application'}], 'description': 'Testing template import', 'discovery_rules': [], 'groups': [{'name': 'Templates'}], 'httptests': [], 'items': [], 'macros': [], 'name': 'Template for Testing', 'screens': [], 'template': 'Test Template', 'templates': []}], 'version': '4.0'}}"` |
| **template_xml**  string | The XML of the template  Returned: when format is xml and omit_date is false  Sample: `"<zabbix_export>\n    <version>4.0</version>\n    <date>2019-10-27T14:49:57Z</date>\n    <groups>\n        <group>\n            <name>Templates</name>\n        </group>\n    </groups>\n    <templates>\n        <template>\n            <template>Test Template</template>\n            <name>Template for Testing</name>\n            <description>Testing template import</description>\n            <groups>\n                <group>\n                    <name>Templates</name>\n                </group>\n            </groups>\n            <applications>\n                <application>\n                    <name>Test Application</name>\n                </application>\n            </applications>\n            <items />\n            <discovery_rules />\n            <httptests />\n            <macros />\n            <templates />\n            <screens />\n        </template>\n    </templates>\n</zabbix_export>"` |
| **template_yaml**  string | The YAML of the template  Returned: when format is yaml and omit_date is false  Sample: `"zabbix_export:\n  version: '6.0'\n  date: '2022-07-09T13:25:18Z'\n  groups:\n    -\n      uuid: 7df96b18c230490a9a0a9e2307226338\n      name: Templates\n  templates:\n    -\n      uuid: 88a9ad240f924f669eb7d4eed736320c\n      template: 'Test Template'\n      name: 'Template for Testing'\n      description: 'Testing template import'\n      groups:\n        -\n          name: Templates"` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
